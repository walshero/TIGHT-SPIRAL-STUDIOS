#!/usr/bin/env python3
"""
STUDIO EYES - PRE-SHIP GATE  v4
Tight Spiral Productions

v4 REPLACES v3 AND ABSORBS svg-text-floor.py.
Delete both. Three files implementing overlapping teeth is the ~30-rules
problem in script form: when six checks should have caught something and
only the arithmetic one did, the answer is more arithmetic in ONE place.

WHAT v3 GOT WRONG - three holes, all on the dark axis
-----------------------------------------------------
1. prefers-color-scheme appeared ZERO times in preship-contrast-gate.py,
   preship-gate-v3.py and studio-eyes-sweep.py. The palette the operating
   system actually applies had never been measured by anything. C1 checked
   that a color-scheme DECLARATION existed - it verified the promise and
   never the palette. Declaring "light dark" and shipping no dark tokens is
   worse than declaring nothing: it tells the OS not to force-darken, then
   hands it a light palette to render on a dark surface.

2. v3 lost v2's html[data-comfort="x"] parsing. v2 had 2 occurrences, v3 had
   0. Any file using that convention was checked in light mode only and
   printed "modes: default" while a whole second palette sat unread. A
   silent regression is worse than a missing feature because the output
   still looks like a pass.

3. E1 (font floor, 18px absolute / 20px body) was correct and blind. Studio
   Eyes reads sizes off the WeasyPrint box tree, and WeasyPrint treats <svg>
   as a replaced image, so it never builds text boxes for SVG glyphs. A
   <text font-size="3.4"> in viewBox="0 0 100 66" is 3.4 USER UNITS: on a
   330px surface that paints at 11.2px. table-four.html passed both gates at
   exit 0, worst pair 6.38:1, and the founder could not read the labels.
   Same shape as your-rp-world.html: token claimed 13.23:1, device painted
   1.17:1. The gate certifies declarations. The eye reads pixels.

DARK IS NOT OPTIONAL HERE. A file with no dark palette HALTs. Every text
token is measured in every mode, and a mode is any of the four conventions
below - not just the one this month's gate happens to parse.

Studio Eyes keeps the render lens (WeasyPrint, real widths, pixel sampling).
It should CALL floors() from this module rather than reimplement it, so each
tooth has exactly one implementation.

exit 0 = ship.  exit 1 = HALT.
"""
import re, sys, os, json

# ---------- RATCHET ----------
# Founder ruling 2026-07-26: "dark mode ready everywhere" is reached by burning
# down a counted debt, not by freezing the repo. A halt already recorded in the
# baseline for that exact path is DEBT and prints as a warning. A halt NOT in the
# baseline is a REGRESSION and exits 1. A file absent from the baseline is new
# work and is held to the full floor. Debt count prints every run so it cannot
# rot quietly. Ratchet only ever tightens: nothing is added to the baseline by
# the gate itself.
BASELINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gate-baseline.json')

def load_baseline():
    try:
        return json.load(open(BASELINE))
    except Exception:
        return {}

def key_for(path, repo):
    """Baseline key = <repo>/<path relative to the repo root>.

    Was the bare basename until 2026-08-07, when this gate went onto the studio
    belt and started running against all five repos. Three of them ship an
    index.html; keyed by basename they collide into one entry and the last one
    written silently grants or denies the other two. Legacy basename entries are
    still honoured on read (see known_for) so the existing baseline keeps working."""
    ap  = os.path.abspath(path)
    rel = os.path.relpath(ap, os.getcwd())
    if rel.startswith(os.pardir):
        rel = os.path.basename(ap)
    return repo + '/' + rel.replace(os.sep, '/')

def known_for(base, path, repo):
    """Codes this file is allowed to carry. Repo-qualified key first, then the
    legacy bare-basename key, so a baseline written before 2026-08-07 still counts."""
    base = base or {}
    return set(base.get(key_for(path, repo), [])) | set(base.get(os.path.basename(path), []))

def code_of(halt):
    return halt.split()[0]

LAST_CODES = []   # codes tripped by the most recent run(); --init reads this

def init(paths, repo, merge=None):
    """Freeze today's debt. This is the ONLY time the baseline may grow.

    Re-seeded 2026-08-07: the previous baseline was written before this gate grew
    its E1-CSS tooth, so 109 of 131 surfaces read as REGRESSIONS the moment the
    gate went on the belt. A baseline that predates the gate's teeth is not a
    baseline, it is a red wall."""
    import io, contextlib
    debt = dict(merge or {})
    for p in paths:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            run(p, False, None, repo)
        if LAST_CODES:
            debt[key_for(p, repo)] = list(LAST_CODES)
    with open(BASELINE, 'w') as f:
        json.dump(dict(sorted(debt.items())), f, indent=1)
        f.write('\n')
    tot = sum(len(v) for v in debt.values())
    print('BASELINE WRITTEN - ' + str(len(debt)) + ' file(s) carrying ' +
          str(tot) + ' known halts.')
    print('These do not block. Everything else does. The ratchet is armed.')
    return 0

AA_BODY, AAA = 4.5, 7.0
FONT_FLOOR_ABS, FONT_FLOOR_BODY = 18.0, 20.0
SVG_RENDER_W = 330.0   # 360px Android viewport less 24px scene padding and 6px border
                       # - the narrowest real surface in the corpus

TEXT_PROPS = ('color',)
DECO_PROPS = ('background', 'background-color', 'background-image', 'border',
              'border-color', 'border-top', 'border-bottom', 'border-left',
              'border-right', 'box-shadow', 'fill', 'stroke', 'outline',
              'outline-color', 'text-shadow')

# ---------- colour arithmetic ----------
def hex2rgb(h):
    h = h.strip().lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    if len(h) != 6:
        return None
    try:
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    except ValueError:
        return None

def lum(rgb):
    def f(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (f(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

# ---------- token blocks: ALL FOUR CONVENTIONS ----------
def _decls(block):
    return dict(re.findall(r'(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})', block))

def token_blocks(css):
    """:root  +  @media (prefers-color-scheme: dark)  +  html[data-comfort="x"]
       +  body.x.  v2 knew two of these, v3 knew one, nothing knew the media
       query. Parse all four or the report is a guess."""
    m = re.search(r':root\s*\{([^}]*)\}', css)
    root = _decls(m.group(1)) if m else {}
    modes = {'default': dict(root)}

    # the OS-applied palette. nested braces, so match to the inner :root.
    for mm in re.finditer(
            r'@media[^{]*prefers-color-scheme\s*:\s*dark[^{]*\{\s*:root\s*\{([^}]*)\}', css, re.I):
        blk = dict(root); blk.update(_decls(mm.group(1)))
        modes['os-dark'] = blk

    for name in re.findall(r'html\[data-comfort\s*=\s*"([\w-]+)"\]', css):
        blk = _decls((re.search(r'html\[data-comfort\s*=\s*"' + re.escape(name) + r'"\]\s*\{([^}]*)\}', css) or
                      re.match('', '')).group(1)) if re.search(
                      r'html\[data-comfort\s*=\s*"' + re.escape(name) + r'"\]\s*\{([^}]*)\}', css) else {}
        if blk:
            merged = dict(root); merged.update(blk)
            modes[name] = merged

    for name in re.findall(r'body\.([\w-]+)\s*\{', css):
        mm = re.search(r'body\.' + re.escape(name) + r'\s*\{([^}]*)\}', css)
        blk = _decls(mm.group(1)) if mm else {}
        if blk:
            merged = dict(root); merged.update(blk)
            modes[name] = merged
    return modes

def token_roles(css):
    text_use, deco_use, surface_use = set(), set(), set()
    for d in re.split(r'[;{}]', css):
        d = d.strip()
        m = re.match(r'([\w-]+)\s*:\s*(.*)', d, re.S)
        if not m:
            continue
        prop, val = m.group(1).lower(), m.group(2)
        vars_in = re.findall(r'var\((--[\w-]+)', val)
        if not vars_in:
            continue
        if prop in TEXT_PROPS:
            text_use.update(vars_in)
        elif prop in ('background', 'background-color'):
            surface_use.update(vars_in); deco_use.update(vars_in)
        elif prop in DECO_PROPS or 'gradient' in val:
            deco_use.update(vars_in)
    return text_use, deco_use, surface_use

# ---------- floors. Studio Eyes should import these, not restate them ----------
def dark_floor(html, css, modes):
    """A file with no dark palette is not dark-mode ready, and one that
       declares color-scheme without a dark palette actively lies to the OS."""
    halts = []
    # two distinct shapes, and v4's first cut only knew one of them:
    #   CSS   ->  color-scheme: light dark
    #   meta  ->  <meta name="color-scheme" content="light dark">
    declares = bool(re.search(r'color-scheme\s*:\s*[^;}]*dark', css, re.I)) or \
               bool(re.search(r'<meta[^>]*name\s*=\s*["\']color-scheme["\'][^>]*'
                              r'content\s*=\s*["\'][^"\']*dark', html, re.I))
    dark_modes = [k for k in modes if k != 'default' and
                  any(h in k.lower() for h in ('dark', 'night', 'dim', 'warmdark'))]
    has_os = 'os-dark' in modes
    if not dark_modes and not has_os:
        halts.append('H-DARK-MISSING no dark palette in any convention (@media '
                     'prefers-color-scheme, html[data-comfort], body.class). Phone OS dark '
                     'mode will force-darken this page and no gate has measured the result.')
    if declares and not has_os:
        halts.append('H-DARK-PROMISE color-scheme declares dark but there is no @media '
                     '(prefers-color-scheme:dark) palette. That tells the OS not to '
                     'force-darken and then hands it light tokens on a dark surface.')
    return halts

def svg_text_floor(html):
    """SVG text is user units, not px. 'font-size:' is CSS and measured in px;
       'font-size=' is an SVG attribute and measured in user units - that
       discriminator holds whether the attribute is static markup or written by
       script, which matters because the script block sits after </svg>."""
    halts = []
    widths = [float(m.group(1)) for m in re.finditer(
        r'viewBox\s*=\s*"\s*[\d.-]+\s+[\d.-]+\s+([\d.]+)\s+([\d.]+)\s*"', html, re.I)]
    if not widths:
        return halts
    vw = max(widths)                 # widest viewBox = fewest px per unit = worst case
    ppu = SVG_RENDER_W / vw
    need = FONT_FLOOR_ABS / ppu
    seen = {}
    for f in re.finditer(r'font-size\s*=\s*\\?["\']([\d.]+)\\?["\']', html):
        u = float(f.group(1))
        seen[u] = seen.get(u, 0) + 1
    for u in sorted(seen):
        px = u * ppu
        if px < FONT_FLOOR_ABS:
            halts.append('E1-SVG font-size ' + str(u) + ' units x' + str(seen[u]) +
                         ' renders at ' + format(px, '.1f') + 'px at viewBox width ' +
                         str(vw) + ' on a ' + str(int(SVG_RENDER_W)) + 'px surface (floor ' +
                         str(FONT_FLOOR_ABS) + '). Raise to >= ' + format(need, '.2f') +
                         ' units or move the label to HTML.')
    return halts

def root_px(css):
    """The px value one rem resolves to. rem is ROOT-relative, never body-relative --
    the whole reason the rem tooth below exists."""
    m = re.search(r'(?:^|[{}\s,])(?:html|:root)\s*\{[^}]*?font-size\s*:\s*([\d.]+)(%|px|rem|em)', css, re.S)
    if not m:
        return 16.0
    v, unit = float(m.group(1)), m.group(2)
    if unit == 'px':
        return v
    if unit == '%':
        return 16.0 * v / 100.0
    return 16.0 * v          # rem/em on the root both resolve against the 16px initial


def css_text_floor(css):
    """ADDED 2026-09-01, the rem tooth. Found by aleph L4 on flash-compression-blockout.html:
    36 rendered text nodes sat under the floor at 16.00-16.32px and this gate passed the
    file clean, because it only ever matched 'font-size:Npx'. The author had set
    body{font-size:1.1875rem} and then written child rules in rem believing rem inherited
    the body size. It does not -- rem is root-relative, so every 1.02rem child resolved
    against the 16px root, not the 19px body. A floor that only reads one unit is a floor
    with a door in it. em is deliberately NOT flagged: it is context-dependent and cannot
    be resolved statically without lying."""
    halts = []
    for m in re.finditer(r'font-size\s*:\s*([\d.]+)px', css):
        v = float(m.group(1))
        if v < FONT_FLOOR_ABS:
            halts.append('E1-CSS font-size ' + format(v, '.0f') + 'px < ' +
                         str(FONT_FLOOR_ABS) + 'px floor.')
    rpx = root_px(css)
    for m in re.finditer(r'font-size\s*:\s*([\d.]+)rem', css):
        px = float(m.group(1)) * rpx
        if px < FONT_FLOOR_ABS:
            halts.append('E1-REM font-size ' + m.group(1) + 'rem resolves to ' +
                         format(px, '.2f') + 'px against a ' + format(rpx, '.0f') +
                         'px root < ' + str(FONT_FLOOR_ABS) + 'px floor. rem is '
                         'root-relative, not body-relative.')
    return sorted(set(halts))

def image_floor(html):
    halts, warns = [], []
    body = re.sub(r'<(script|style)[\s\S]*?</\1>', ' ', html, flags=re.I)
    visual = sum(len(re.findall(r'<' + t + r'\b', body, re.I))
                 for t in ('img', 'svg', 'picture', 'video', 'canvas'))
    visual += len(re.findall(r'background-image\s*:', html, re.I))
    screens = len(re.findall(r'class="[^"]*\b(?:stage|screen|slide|scene)\b', body, re.I))
    chars = len(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', body)).strip())
    if screens >= 1 and visual == 0 and chars > 400:
        halts.append('H-IMAGE-FLOOR ' + str(screens) + ' screen(s), ' + str(chars) +
                     ' chars, ZERO visual. Screens must be >50% image.')
    elif screens >= 3 and visual < screens / 2 and chars > 1500:
        warns.append('[image-floor] ' + str(visual) + ' visual across ' + str(screens) +
                     ' screens, ' + str(chars) + ' chars - verify by eye.')
    return halts, warns

def nav_floor(html):
    halts = []
    body = re.sub(r'<(script|style)[\s\S]*?</\1>', ' ', html, flags=re.I)
    screens = len(re.findall(r'class="[^"]*\b(?:stage|screen|slide|scene)\b', body, re.I))
    toggled = len(re.findall(r'\bclass="[^"]*\bhidden\b', body, re.I))
    if max(screens, toggled + 1 if toggled else 0) < 2:
        return halts
    if not re.search(r'id=["\']backBtn|class="[^"]*\bback(nav|btn)?\b|aria-label="[^"]*\bback\b'
                     r'|onclick="[^"]*(?:goBack|backTo)|>\s*(?:&larr;\s*)?back\b', html, re.I):
        halts.append('H-NAV-BACK multi-screen product has no BACK control.')
    if not re.search(r'id=["\']homeBtn|class="[^"]*\bhome(nav|btn)?\b'
                     r'|aria-label="[^"]*\b(?:home|start)\b'
                     r'|onclick="[^"]*(?:goHome|toHome|homeScreen)|>\s*home\b', html, re.I):
        halts.append('H-NAV-HOME multi-screen product has no HOME control.')
    return halts

def emoji_floor(html):
    vis = re.sub(r'<(script|style)[\s\S]*?</\1>', ' ', html, flags=re.I)
    if re.search(r'[\U0001F000-\U0001FAFF\u2600-\u26FF]', vis):
        return ['H-EMOJI emoji in visible text. Never, in any venue.']
    return []

def floors(html, css, modes):
    """The single list of source-computable teeth. Studio Eyes calls this."""
    halts = []
    halts += dark_floor(html, css, modes)
    halts += svg_text_floor(html)
    halts += css_text_floor(css)
    halts += nav_floor(html)
    halts += emoji_floor(html)
    ih, iw = image_floor(html)
    return halts + ih, iw

# ---------- run ----------
def run(path, ratchet=False, base=None, repo=''):
    html = open(path, encoding='utf-8', errors='replace').read()
    css  = ''.join(re.findall(r'<style[^>]*>(.*?)</style>', html, re.S))
    modes = token_blocks(css)
    text_use, deco_use, surface_use = token_roles(css)
    halts, warns, rows = [], [], []

    for mode, tok in sorted(modes.items()):
        surfaces = {s: hex2rgb(tok[s]) for s in surface_use if s in tok and hex2rgb(tok[s])}
        if not surfaces:
            warns.append('[' + mode + '] declares tokens but no surface token - unmeasurable')
            continue
        for tv in sorted(text_use):
            if tv not in tok:
                continue
            trgb = hex2rgb(tok[tv])
            if not trgb:
                continue
            pairs = {sv: ratio(trgb, srgb) for sv, srgb in surfaces.items()}
            best, home = max(pairs.values()), max(pairs, key=pairs.get)
            if best < AA_BODY:
                halts.append('H-TEXT-UNREADABLE [' + mode + '] ' + tv +
                             ' clears no surface. Best ' + home + ' at ' +
                             format(best, '.2f') + ' (needs ' + str(AA_BODY) + '). Split it.')
            else:
                rows.append((mode, tv, home, round(best, 2),
                             'AAA' if best >= AAA else 'AA '))
                for sv, r in sorted(pairs.items()):
                    if r < AA_BODY and sv != home:
                        warns.append('[' + mode + '] ' + tv + ' on ' + sv + ' = ' +
                                     format(r, '.2f') + ' - only safe on ' + home)

    for mode, tok in modes.items():
        for v, hx in tok.items():
            rgb = hex2rgb(hx)
            if rgb == (255, 255, 255):
                warns.append('[' + mode + '] ' + v + ' is pure #fff')
            if rgb == (0, 0, 0):
                warns.append('[' + mode + '] ' + v + ' is pure #000')

    fh, fw = floors(html, css, modes)
    halts += fh; warns += fw
    # every code this file currently trips, before the ratchet forgives any of it.
    # --init freezes exactly this set; nothing else may write the baseline.
    global LAST_CODES
    LAST_CODES = sorted({code_of(h) for h in halts})

    debt = []
    if ratchet:
        known = known_for(base, path, repo)
        keep = []
        for h in halts:
            if code_of(h) in known:
                debt.append(h)
            else:
                keep.append(h)
        halts = keep

    print()
    print('  STUDIO EYES - PRE-SHIP GATE v4 - ' + os.path.basename(path))
    print('  ' + '-' * 60)
    print('  modes measured: ' + ', '.join(sorted(modes)))
    print('  text tokens: ' + (', '.join(sorted(text_use)) or '(none)'))
    print('  ' + '-' * 60)
    for mode, tv, sv, r, tag in rows:
        print('  [' + tag + '] ' + mode.ljust(10) + ' ' + tv.ljust(10) +
              ' on ' + sv.ljust(10) + ' = ' + format(r, '6.2f'))
    if debt:
        print()
        print('  DEBT carried by the ratchet (' + str(len(debt)) + ') - counted, not forgiven:')
        for d in sorted(set(debt)):
            print('     ' + d)
    if warns:
        print()
        print('  warnings:')
        for w in sorted(set(warns)):
            print('     ' + w)
    print()
    if halts:
        print('  HALT - do not ship' + (' (REGRESSION - not in baseline)' if ratchet else '') + ':')
        for h in sorted(set(halts)):
            print('     ' + h)
        print()
        return 1
    worst = min((r for _, _, _, r, _ in rows), default=None)
    print('  SHIP - every text token clears ' + str(AA_BODY) + ' in every mode' +
          ('. Worst pair = ' + format(worst, '.2f') if worst is not None else ''))
    print()
    return 0

# ---------- self-test teeth: a gate that cannot fail a bad file is a wall ----------
BAD = ('<html><head><meta name="color-scheme" content="light dark"></head>'
       '<style>:root{--p:#fff;--i:#111}html{font-size:100%}'
       'body{background:var(--p);color:var(--i);font-size:1.1875rem}'
       '.scene{}.body p{font-size:1.02rem}</style><body><div class="scene">'
       '<svg viewBox="0 0 100 60"><text font-size="3">tiny</text></svg>'
       '</div></body></html>')

def self_test():
    import tempfile
    p = os.path.join(tempfile.mkdtemp(), 'bad.html')
    open(p, 'w').write(BAD)
    html = BAD
    css = ''.join(re.findall(r'<style[^>]*>(.*?)</style>', html, re.S))
    fh, _ = floors(html, css, token_blocks(css))
    got = ' '.join(fh)
    ok_svg  = 'E1-SVG' in got
    ok_dark = 'H-DARK-PROMISE' in got
    ok_rem  = 'E1-REM' in got
    if not (ok_svg and ok_dark and ok_rem):
        print('  SELF-TEST FAILED - svg:%s dark:%s rem:%s -> the gate is not biting'
              % (ok_svg, ok_dark, ok_rem))
        sys.exit(3)
    print('  self-test ok: svg scale tooth bites, dark-promise tooth bites, rem tooth bites')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: preship-gate-v4.py <file.html> [more.html ...]')
        sys.exit(2)
    self_test()
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    repo = next((a.split('=', 1)[1] for a in sys.argv[1:] if a.startswith('--repo=')),
                os.path.basename(os.getcwd()))
    if '--init' in sys.argv:
        # --merge keeps entries already frozen for OTHER repos; the belt seeds one
        # repo at a time and a plain rewrite would drop the others' debt.
        sys.exit(init(args, repo, load_baseline() if '--merge' in sys.argv else None))
    ratchet = '--ratchet' in sys.argv
    base = load_baseline() if ratchet else None
    if ratchet:
        tot = sum(len(v) for v in base.values())
        print('  RATCHET on: ' + str(len(base)) + ' files carrying ' + str(tot) +
              ' known halts. New halts and new files are held to the full floor.')
    sys.exit(max(run(p, ratchet, base, repo) for p in args))
