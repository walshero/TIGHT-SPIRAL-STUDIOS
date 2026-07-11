#!/usr/bin/env python3
"""
STUDIO EYES v4 — Tight Spiral Productions
The executable organ. Runs in CI on every push; blocks the pipe on HALT.

TWO LAYERS:
  LAYER 0 (static)   — always runs. No deps. Parses CSS/HTML.
  LAYER 1 (rendered) — runs if Playwright is present. Degrades to GAP if not.
                       This is the layer that catches what static cannot:
                       what the DEVICE actually paints.

WHY v4 EXISTS: v3.5 audited the file's declared palette only. It could not see
what the OS forced (dark mode), what the browser actually rendered, whether a
tap target was really 44px, or whether focus was visible. Three hollow artifacts
(2026-07-10) proved that "validated in-session" is not landed and static is not
enough.

EXIT CODES:  0 = clean (may carry WARNs).  1 = HALT (pipe stops).
"""

import sys, os, re, json, glob, math

# ─────────────────────────────────────────────────────────────────────────────
# FLOORS — Tight Spiral Visual Constitution
# ─────────────────────────────────────────────────────────────────────────────
CONTRAST_FLOOR   = 4.5     # WCAG AA body text. Matt's eyes are the real verdict.
LARGE_FLOOR      = 3.0     # 24px+ or 19px+bold
STOP_SEPARATION  = 0.12    # a knob that changes nothing is a WALL
TAP_MIN          = 44      # px — Apple HIG / WCAG 2.5.5
VIEWPORT         = (390, 844)   # iPhone. The device Matt actually holds.
IMAGE_FLOOR      = 0.50    # >50% of first viewport must be image

HALTS, WARNS, GAPS, NOTES = [], [], [], []

def halt(f, msg): HALTS.append(f"[HALT] {f}: {msg}")
def warn(f, msg): WARNS.append(f"[WARN] {f}: {msg}")
def gap(msg):     GAPS.append(f"[GAP]  {msg}")
def note(msg):    NOTES.append(f"       {msg}")

# ─────────────────────────────────────────────────────────────────────────────
# COLOR
# ─────────────────────────────────────────────────────────────────────────────
def _srgb(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

def luminance(rgb):
    r, g, b = rgb
    return 0.2126 * _srgb(r) + 0.7152 * _srgb(g) + 0.0722 * _srgb(b)

def contrast(c1, c2):
    l1, l2 = luminance(c1), luminance(c2)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)

def parse_color(s):
    if not s: return None
    s = s.strip().lower()
    m = re.match(r'#([0-9a-f]{3})$', s)
    if m:
        h = m.group(1)
        return tuple(int(c * 2, 16) for c in h)
    m = re.match(r'#([0-9a-f]{6})$', s)
    if m:
        h = m.group(1)
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    m = re.match(r'rgba?\(([^)]+)\)', s)
    if m:
        parts = [p.strip() for p in m.group(1).replace('/', ',').split(',')]
        try:
            return tuple(int(float(p)) for p in parts[:3])
        except ValueError:
            return None
    named = {'white': (255,255,255), 'black': (0,0,0), 'red': (255,0,0)}
    return named.get(s)

# ─────────────────────────────────────────────────────────────────────────────
# LAYER 0 — STATIC
# ─────────────────────────────────────────────────────────────────────────────
def resolve_vars(css):
    """Resolve --custom-property references one level deep."""
    varmap = dict(re.findall(r'(--[\w-]+)\s*:\s*([^;]+);', css))
    def sub(v, depth=0):
        if depth > 4: return v
        m = re.search(r'var\((--[\w-]+)', v)
        if m and m.group(1) in varmap:
            return sub(varmap[m.group(1)].strip(), depth + 1)
        return v
    return {k: sub(v.strip()) for k, v in varmap.items()}

def static_pass(path):
    fn = os.path.basename(path)
    html = open(path, encoding='utf-8', errors='replace').read()

    # ── H1: pure black / pure white banned (Visual Constitution) ──
    for bad, label in [('#000000', 'pure black'), ('#ffffff', 'pure white'),
                       ('#000;', 'pure black'), ('#fff;', 'pure white')]:
        if bad in html.lower():
            warn(fn, f"{label} detected ({bad}) — Constitution bans #000/#fff as paper or ink")

    # ── H2: emoji ban (absolute) ──
    emoji = re.findall(r'[\U0001F300-\U0001FAFF\u2600-\u27BF]', html)
    if emoji:
        halt(fn, f"EMOJI FOUND ({len(emoji)}) — banned in all output, all venues")

    # ── H3: dark-mode inheritance (the recurring EN195 bug) ──
    has_scheme  = 'color-scheme' in html
    has_dark_mq = 'prefers-color-scheme' in html
    if not has_scheme and not has_dark_mq:
        halt(fn, "NO color-scheme AND NO prefers-color-scheme — the OS will force "
                 "its own dark palette and drive text below the floor. "
                 "Set color-scheme, or ship an explicit passing dark palette.")

    # ── H4: dead links (nav anchors exempt — only resource loads flag) ──
    for href in re.findall(r'href=["\']([^"\'#][^"\']*)["\']', html):
        if href.startswith(('http', 'mailto:', 'tel:', 'data:')): continue
        target = os.path.join(os.path.dirname(path), href.split('?')[0].split('#')[0])
        if href.endswith(('.html', '.css', '.js', '.png', '.jpg', '.svg')) \
           and not os.path.exists(target):
            halt(fn, f"DEAD LINK — href='{href}' does not resolve")

    # ── H5: comfort stop separation (a fake knob is a wall) ──
    css = ' '.join(re.findall(r'<style[^>]*>(.*?)</style>', html, re.S))
    stops = re.findall(r'\[data-(?:stop|comfort|theme)=["\']?(\w+)["\']?\][^{]*\{([^}]*)\}', css)
    if len(stops) >= 2:
        lums = {}
        for name, block in stops:
            bg = re.search(r'--bg\s*:\s*([^;]+)', block)
            if bg:
                c = parse_color(bg.group(1))
                if c: lums[name] = luminance(c)
        names = list(lums)
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                d = abs(lums[names[i]] - lums[names[j]])
                if d < STOP_SEPARATION:
                    halt(fn, f"FAKE KNOB — stops '{names[i]}' and '{names[j]}' differ by "
                             f"only {d:.3f} paper luminance (floor {STOP_SEPARATION}). "
                             f"A comfort control that changes nothing visible is a WALL.")

    # ── H6: NO OPENING WALL — first screen must be scene, not a preference gate ──
    first = html[:8000].lower()
    gate_words = ['choose your palette', 'pick a comfort', 'select a theme',
                  'choose a lens', 'paste your', 'select difficulty']
    for g in gate_words:
        if g in first:
            halt(fn, f"OPENING WALL — first screen carries a preference gate ('{g}'). "
                     f"Games open SCENE-FIRST. Comfort is a live corner control, never a door.")

    # ── H7: provenance ──
    if 'provenance' not in html.lower() and 'changelog' not in html.lower():
        warn(fn, "no provenance/changelog block in file")

    return html

# ─────────────────────────────────────────────────────────────────────────────
# LAYER 1 — RENDERED (Playwright)
# ─────────────────────────────────────────────────────────────────────────────
def rendered_pass(paths, shotdir):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        gap("Playwright not installed — LAYER 1 SKIPPED. "
            "Rendered contrast, dark mode, tap targets, focus rings, and axe-core "
            "were NOT checked. Static only. Install: pip install playwright && playwright install chromium")
        return

    os.makedirs(shotdir, exist_ok=True)
    axe = None
    for cand in ['node_modules/axe-core/axe.min.js',
                 '/usr/lib/node_modules/axe-core/axe.min.js']:
        if os.path.exists(cand):
            axe = open(cand, encoding='utf-8').read()
            break
    if not axe:
        gap("axe-core not found — WCAG rule engine SKIPPED (R4). "
            "Install: npm install axe-core")

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for scheme in ['light', 'dark']:
            ctx = browser.new_context(
                viewport={'width': VIEWPORT[0], 'height': VIEWPORT[1]},
                color_scheme=scheme,
                device_scale_factor=2,
            )
            page = ctx.new_page()

            for path in paths:
                fn = os.path.basename(path)
                try:
                    page.goto('file://' + os.path.abspath(path),
                              wait_until='networkidle', timeout=15000)
                except Exception as e:
                    warn(fn, f"[{scheme}] render failed: {e}")
                    continue

                # ── R1: RENDERED CONTRAST — what the device actually paints ──
                bad = page.evaluate("""() => {
                    const srgb = c => { c/=255; return c<=0.03928 ? c/12.92
                                        : Math.pow((c+0.055)/1.055, 2.4); };
                    const lum = ([r,g,b]) => .2126*srgb(r)+.7152*srgb(g)+.0722*srgb(b);
                    const parse = s => {
                        const m = s.match(/rgba?\\(([^)]+)\\)/);
                        if(!m) return null;
                        const p = m[1].split(',').map(x=>parseFloat(x));
                        if(p.length>3 && p[3]===0) return null;   // transparent
                        return p.slice(0,3);
                    };
                    const bgOf = el => {
                        let n = el;
                        while(n && n !== document.documentElement){
                            const c = parse(getComputedStyle(n).backgroundColor);
                            if(c) return c;
                            n = n.parentElement;
                        }
                        return parse(getComputedStyle(document.body).backgroundColor) || [255,255,255];
                    };
                    const out = [];
                    document.querySelectorAll('*').forEach(el => {
                        if(!el.offsetParent && getComputedStyle(el).position!=='fixed') return;
                        const txt = Array.from(el.childNodes)
                            .filter(n=>n.nodeType===3)
                            .map(n=>n.textContent.trim()).join('');
                        if(!txt) return;
                        const cs = getComputedStyle(el);
                        const fg = parse(cs.color);
                        if(!fg) return;
                        const bg = bgOf(el);
                        const l1 = lum(fg), l2 = lum(bg);
                        const ratio = (Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05);
                        const size = parseFloat(cs.fontSize);
                        const bold = parseInt(cs.fontWeight) >= 700;
                        const floor = (size>=24 || (size>=19 && bold)) ? 3.0 : 4.5;
                        if(ratio < floor){
                            out.push({
                                tag: el.tagName.toLowerCase(),
                                cls: (el.className||'').toString().slice(0,30),
                                txt: txt.slice(0,40),
                                ratio: +ratio.toFixed(2),
                                floor, size
                            });
                        }
                    });
                    return out.slice(0, 12);
                }""")
                for b in bad:
                    halt(fn, f"[{scheme}] RENDERED CONTRAST {b['ratio']}:1 (floor {b['floor']}) "
                             f"on <{b['tag']} .{b['cls']}> \"{b['txt']}\" @{b['size']}px")

                # ── R3: TAP TARGETS — 44px truth ──
                small = page.evaluate("""() => {
                    const out=[];
                    document.querySelectorAll('a,button,input,select,[role=button],[tabindex]')
                      .forEach(el=>{
                        if(!el.offsetParent) return;
                        const r = el.getBoundingClientRect();
                        if(r.width===0||r.height===0) return;
                        if(r.width < 44 || r.height < 44){
                            out.push({tag:el.tagName.toLowerCase(),
                                      txt:(el.textContent||'').trim().slice(0,30),
                                      w:Math.round(r.width), h:Math.round(r.height)});
                        }
                    });
                    return out.slice(0,10);
                }""")
                if scheme == 'light':
                    for s in small:
                        halt(fn, f"TAP TARGET {s['w']}x{s['h']}px (floor {TAP_MIN}) "
                                 f"on <{s['tag']}> \"{s['txt']}\"")

                # ── R2: FOCUS TRUTH — walk the tab order, is focus VISIBLE? ──
                if scheme == 'light':
                    invisible = page.evaluate("""() => {
                        const out=[];
                        const ctrls = document.querySelectorAll(
                          'a[href],button,input,select,textarea,[tabindex]:not([tabindex="-1"])');
                        Array.from(ctrls).slice(0,40).forEach(el=>{
                            if(!el.offsetParent) return;
                            el.focus();
                            const cs = getComputedStyle(el);
                            const hasOutline = cs.outlineStyle!=='none' &&
                                               parseFloat(cs.outlineWidth)>0;
                            const hasShadow  = cs.boxShadow && cs.boxShadow!=='none';
                            const hasBorder  = parseFloat(cs.borderWidth)>0;
                            if(!hasOutline && !hasShadow && !hasBorder){
                                out.push({tag:el.tagName.toLowerCase(),
                                          txt:(el.textContent||'').trim().slice(0,30)});
                            }
                        });
                        return out.slice(0,8);
                    }""")
                    for i in invisible:
                        halt(fn, f"NO VISIBLE FOCUS on <{i['tag']}> \"{i['txt']}\" — "
                                 f"keyboard users cannot see where they are")

                # ── R4: axe-core WCAG engine ──
                if axe and scheme == 'light':
                    try:
                        page.add_script_tag(content=axe)
                        res = page.evaluate("""async () => {
                            const r = await axe.run(document, {
                                runOnly:{type:'tag', values:['wcag2a','wcag2aa','wcag21aa']}
                            });
                            return r.violations.map(v=>({
                                id:v.id, impact:v.impact,
                                help:v.help, n:v.nodes.length
                            }));
                        }""")
                        for v in res:
                            msg = f"axe [{v['impact']}] {v['id']}: {v['help']} ({v['n']} nodes)"
                            if v['impact'] in ('critical', 'serious'):
                                halt(fn, msg)
                            else:
                                warn(fn, msg)
                    except Exception as e:
                        gap(f"axe run failed on {fn}: {e}")

                # ── R6: image share of first viewport ──
                if scheme == 'light':
                    share = page.evaluate("""() => {
                        const V = 390*844;
                        let px = 0;
                        document.querySelectorAll('img,svg,canvas,video,picture')
                          .forEach(el=>{
                            const r = el.getBoundingClientRect();
                            if(r.top > 844 || r.bottom < 0) return;
                            const h = Math.min(r.bottom,844) - Math.max(r.top,0);
                            const w = Math.min(r.right,390) - Math.max(r.left,0);
                            if(h>0 && w>0) px += h*w;
                        });
                        // background-images on large elements count too
                        document.querySelectorAll('*').forEach(el=>{
                            const bi = getComputedStyle(el).backgroundImage;
                            if(bi && bi!=='none' && !bi.includes('gradient')){
                                const r = el.getBoundingClientRect();
                                if(r.top>844 || r.bottom<0) return;
                                const h = Math.min(r.bottom,844)-Math.max(r.top,0);
                                const w = Math.min(r.right,390)-Math.max(r.left,0);
                                if(h>0&&w>0) px += h*w;
                            }
                        });
                        return Math.min(px/V, 1);
                    }""")
                    if share < IMAGE_FLOOR:
                        warn(fn, f"IMAGE SHARE {share*100:.0f}% of first viewport "
                                 f"(floor {IMAGE_FLOOR*100:.0f}%) — screens must be >50% image")

                # ── SCREENSHOT — this is what Matt sees on his phone ──
                shot = os.path.join(shotdir, f"{fn.replace('.html','')}--{scheme}.png")
                try:
                    page.screenshot(path=shot)
                except Exception:
                    pass

            ctx.close()
        browser.close()

# ─────────────────────────────────────────────────────────────────────────────
# SELFTEST LAW — the auditor must catch a planted defect before it may gate
# ─────────────────────────────────────────────────────────────────────────────
BAD_FILE = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
body{background:#ffffff;color:#c8c8c8;}
[data-stop=default]{--bg:#d9d2c4;}
[data-stop=softer]{--bg:#dad3c5;}
a{outline:none;border:0;box-shadow:none;font-size:12px;}
</style></head><body>
<p>Choose your palette to begin</p>
<a href="does-not-exist.html" style="display:inline-block;width:20px;height:20px">x</a>
</body></html>"""

def selftest():
    import tempfile
    global HALTS, WARNS, GAPS
    saveH, saveW, saveG = HALTS, WARNS, GAPS
    HALTS, WARNS, GAPS = [], [], []
    d = tempfile.mkdtemp()
    p = os.path.join(d, 'planted-bad.html')
    open(p, 'w').write(BAD_FILE)
    static_pass(p)
    caught = {
        'no color-scheme':  any('color-scheme' in h for h in HALTS),
        'fake knob (H5)':   any('FAKE KNOB' in h for h in HALTS),
        'opening wall':     any('OPENING WALL' in h for h in HALTS),
        'dead link':        any('DEAD LINK' in h for h in HALTS),
        'pure white':       any('pure white' in w for w in WARNS),
    }
    HALTS, WARNS, GAPS = saveH, saveW, saveG
    return caught

# ─────────────────────────────────────────────────────────────────────────────
def main():
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    shotdir = os.environ.get('SHOTDIR', 'studio-eyes-shots')

    print("=" * 72)
    print("STUDIO EYES v4 — Tight Spiral Productions")
    print("=" * 72)

    # SELFTEST FIRST. An auditor that cannot catch a planted bug may not gate.
    st = selftest()
    print("\nSELFTEST (planted-defect file):")
    for k, v in st.items():
        print(f"  {'CAUGHT ' if v else 'MISSED!'} {k}")
    if not all(st.values()):
        print("\n[FATAL] SELFTEST FAILED — the auditor is broken and may not certify anything.")
        print("        (Lesson 2026-07-05: never trust a sweep you have not validated.)")
        sys.exit(1)
    print("  → auditor validated. Proceeding.\n")

    paths = sorted(glob.glob(os.path.join(target, '*.html')))
    if not paths:
        print("No HTML files found."); sys.exit(0)
    print(f"Auditing {len(paths)} files at {VIEWPORT[0]}x{VIEWPORT[1]} (iPhone)\n")

    for p in paths:
        static_pass(p)

    rendered_pass(paths, shotdir)

    print("-" * 72)
    for g in GAPS:  print(g)
    for w in WARNS: print(w)
    for h in HALTS: print(h)
    print("-" * 72)
    print(f"HALTS: {len(HALTS)}   WARNS: {len(WARNS)}   GAPS: {len(GAPS)}")

    if HALTS:
        print("\nFAIL — the pipe stops here. Nothing ships with a HALT.")
        sys.exit(1)
    print("\nPASS — 0 HALT.")
    sys.exit(0)

if __name__ == '__main__':
    main()
