#!/usr/bin/env python3
"""
STUDIO EYES v3  ·  Tight Spiral Productions
===========================================
The accessibility auditor for a founder with retinitis pigmentosa.
Contrast is ARITHMETIC, not judgment. This tool is in the critical path
of every ship, so it must first prove it can be trusted.

WHAT CHANGED FROM v2 (and why)
------------------------------
v2 parsed CSS with regex and GUESSED what the browser would do. It was wrong
seven times: comments glued to selectors, @media invisible, only the first
<style> block read, grouped selectors unfindable, ancestors mis-walked,
self-painting elements ignored, and key-class collisions grounding a caption
against an unrelated progress bar.

Every one of those is the same bug: *guessing the cascade instead of asking
the engine that runs it.* There is no regex that fixes this class. So:

    v2:  read CSS text -> guess cascade -> guess ground -> compute
    v3:  RENDER PAGE   -> ASK for ground              -> compute

The middle column is where all seven bugs lived. It is deleted.
getComputedStyle does not guess. elementFromPoint does not guess. And when
text sits on a photo or a gradient, v3 SCREENSHOTS THE PIXELS UNDER THE GLYPHS
— something regex can never do, and which v2's own gate admitted it could not see.

SELF-AUDIT (the thing that makes it world-class, not merely correct)
--------------------------------------------------------------------
Every v2 bug was found by a HUMAN noticing something was off. That is the real
failure. v3 ships with a canary corpus of known-verdict traps — half of them
FALSE-POSITIVE traps: files that are CORRECT and that v2 wrongly HALTed.

    studio-eyes.py --self-test

runs before any audit. If the auditor cannot grade its own canary, IT REFUSES
TO RUN. A tool that gates the studio must first gate itself.

USAGE
    studio-eyes.py --self-test              validate the auditor
    studio-eyes.py <file.html> [...]        audit (self-test runs first)
    studio-eyes.py --no-self-test <file>    skip (CI only; not for ship)

EXIT 0 = ship.  EXIT 1 = HALT, do not ship.
"""
import sys, os, json, base64, io, re

WCAG_TEXT = 4.5
WCAG_LARGE = 3.0
STOP_SEP_MIN = 0.12
MIN_TARGET = 44

# ---------------------------------------------------------------- colour math

def lum(rgb):
    def ch(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)

def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

def parse_rgb(s):
    m = re.findall(r'[\d.]+', s or '')
    if len(m) < 3:
        return None
    r, g, b = int(float(m[0])), int(float(m[1])), int(float(m[2]))
    a = float(m[3]) if len(m) > 3 else 1.0
    return (r, g, b, a)

def flatten(fg, bg):
    """Composite a translucent colour over its backdrop."""
    r, g, b, a = fg
    if a >= 0.999:
        return (r, g, b)
    br, bg_, bb = bg
    return (round(r * a + br * (1 - a)),
            round(g * a + bg_ * (1 - a)),
            round(b * a + bb * (1 - a)))

# ---------------------------------------------------------------- the probe
# This runs INSIDE the browser. It is the whole point: the page tells us what
# it actually painted, instead of us deducing it from source text.

PROBE = r"""
() => {
  const out = {texts:[], targets:[], stops:[], firstScreen:null, emoji:[], tokens:{}};

  // ---- every visible text node, with its REAL computed colour and the REAL
  // ---- chain of ancestors that paint behind it.
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  let n;
  while (n = walker.nextNode()) {
    const t = n.textContent.trim();
    if (!t) continue;
    const el = n.parentElement;
    if (!el || seen.has(el)) continue;
    seen.add(el);
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) continue;

    // walk up for the nearest OPAQUE painted background. The browser knows.
    const chain = [];
    let p = el;
    while (p) {
      const pcs = getComputedStyle(p);
      chain.push({
        bg: pcs.backgroundColor,
        img: pcs.backgroundImage !== 'none' ? pcs.backgroundImage.slice(0,60) : null,
        sel: p.tagName.toLowerCase() + (p.className && typeof p.className === 'string'
              ? '.' + p.className.trim().split(/\s+/).join('.') : '')
      });
      p = p.parentElement;
    }
    const fs = parseFloat(cs.fontSize);
    const bold = (parseInt(cs.fontWeight) || 400) >= 700;
    out.texts.push({
      text: t.slice(0,40),
      sel: chain[0].sel,
      color: cs.color,
      chain: chain,
      large: (fs >= 24 || (fs >= 18.66 && bold)),
      rect: {x:r.x, y:r.y, w:r.width, h:r.height}
    });

    // emoji, in RENDERED text (not source) — catches JS-injected ones too
    const EM = /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}\u{FE0F}\u{1F000}-\u{1F02F}]/u;
    if (EM.test(t)) out.emoji.push(t.slice(0,30));
  }

  // ---- interactive targets: real rendered box + real focus ring
  document.querySelectorAll('a,button,input,select,textarea,[role=button],[tabindex]').forEach(el=>{
    const cs = getComputedStyle(el);
    if (cs.display==='none' || cs.visibility==='hidden') return;
    const r = el.getBoundingClientRect();
    if (r.width < 1 && r.height < 1) return;
    el.focus();
    const f = getComputedStyle(el);
    const ring = (f.outlineStyle !== 'none' && parseFloat(f.outlineWidth) > 0)
              || (f.boxShadow && f.boxShadow !== 'none')
              || (f.borderColor !== cs.borderColor);
    out.targets.push({
      sel: el.tagName.toLowerCase() + (el.className && typeof el.className==='string'
            ? '.'+el.className.trim().split(/\s+/)[0] : ''),
      w: r.width, h: r.height, ring: ring
    });
    el.blur();
  });

  // ---- TOKEN-ROLE LAW: a token is atmosphere OR text, never both.
  // Read the real stylesheets the browser assembled (not a regex over source).
  // TOKEN-ROLE LAW.
  // NOTE: the CSSOM is USELESS for this. Chromium resolves var() into a computed
  // value before it ever reaches cssText or getPropertyValue, so no token name
  // survives. The RAW <style> source is the only place --amber is still spelled
  // '--amber'. So we read the source text -- but ONLY to find token NAMES, never
  // to reason about the cascade. Grounding still comes from the renderer.
  const asText = new Set(), asDeco = new Set();
  const DECO = /^(background|background-color|background-image|fill|stroke|box-shadow|border-color|border|outline-color|outline)$/;
  let raw = '';
  document.querySelectorAll('style').forEach(el => { raw += el.textContent + '\n'; });
  raw = raw.replace(/\/\*[\s\S]*?\*\//g, ' ');          // comments lie; strip them
  // every declaration, anywhere (inside @media too -- we only want prop:value pairs)
  const declRe = /([-\w]+)\s*:\s*([^;{}]+)/g;
  let dm;
  while ((dm = declRe.exec(raw)) !== null) {
    const prop = dm[1].trim();
    const val  = dm[2];
    if (prop.startsWith('--')) continue;                 // a definition, not a use
    const m = val.match(/var\(\s*(--[\w-]+)/g);
    if (!m) continue;
    const toks = m.map(x => x.replace(/var\(\s*/, ''));
    if (prop === 'color') toks.forEach(t => asText.add(t));
    else if (DECO.test(prop)) toks.forEach(t => asDeco.add(t));
  }
  out.tokens.text = [...asText];
  out.tokens.deco = [...asDeco];

  // ---- NO OPENING WALL: what is actually on screen at first paint?
  const vis = [...document.body.querySelectorAll('*')].filter(el=>{
    const cs = getComputedStyle(el);
    if (cs.display==='none'||cs.visibility==='hidden') return false;
    const r = el.getBoundingClientRect();
    return r.width>0 && r.height>0 && r.top < innerHeight && r.bottom > 0;
  });
  const GATEWORDS = /(comfort|palette|contrast|theme|colou?r scheme|text size|font size|choose your|pick a|preference|difficulty|accessib)/i;
  const gateEls = vis.filter(el=>{
    const cls = (typeof el.className==='string'? el.className:'') + ' ' + (el.id||'');
    const txt = (el.textContent||'').slice(0,80);
    const isCtl = /^(button|select|input)$/i.test(el.tagName) || /swatch|palette|stop|comfort/i.test(cls);
    return isCtl && (GATEWORDS.test(cls) || GATEWORDS.test(txt));
  });
  // scene = meaningful prose visible on load
  const prose = vis.filter(el=>{
    if (!/^(P|H1|H2|H3|LI|BLOCKQUOTE|FIGCAPTION)$/.test(el.tagName)) return false;
    const t = (el.textContent||'').trim();
    if (t.length <= 25) return false;
    // A gate's OWN headline is not a scene. 'Choose your comfort setting' cannot
    // rescue the wall it is the title of.
    if (GATEWORDS.test(t)) return false;
    // Nor can prose nested INSIDE the gate container.
    let p = el;
    while (p && p !== document.body) {
      const cls = (typeof p.className==='string'? p.className:'') + ' ' + (p.id||'');
      if (/swatch|palette|comfort|preference|gate|settings/i.test(cls)) return false;
      p = p.parentElement;
    }
    return true;
  });
  // is a gate element in the MAIN flow (not parked in a corner)?
  const inFlow = gateEls.filter(el=>{
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    if (cs.position === 'fixed' || cs.position === 'absolute') return false;   // corner control: fine
    return r.width > innerWidth * 0.25 || r.height > 60;
  });
  out.firstScreen = {gates: inFlow.length, gateTxt: inFlow.slice(0,3).map(e=>(e.textContent||'').trim().slice(0,40)),
                     prose: prose.length, proseTxt: prose.slice(0,2).map(e=>(e.textContent||'').trim().slice(0,50))};

  // ---- comfort stops: find the classes that repaint the page
  const bodyClasses = new Set();
  for (const ss of document.styleSheets) {
    let rules; try { rules = ss.cssRules; } catch(e){ continue; }
    if (!rules) continue;
    for (const r of rules) {
      if (!r.selectorText) continue;
      const m = r.selectorText.match(/body\.([\w-]+)/g);
      if (m) m.forEach(x=>bodyClasses.add(x.replace('body.','')));
    }
  }
  out.stops = [...bodyClasses];
  return out;
}
"""

# ---------------------------------------------------------------- audit core

def px_bg_under(png_bytes, rect, dpr=1):
    """Sample the ACTUAL painted pixels behind a text box.
    This is the check the old gate confessed it could not do: text on a photo
    or a gradient. Returns the WORST-CASE (most extreme) backdrop found."""
    try:
        from PIL import Image
    except ImportError:
        return None
    im = Image.open(io.BytesIO(png_bytes)).convert('RGB')
    x, y = int(rect['x']*dpr), int(rect['y']*dpr)
    w, h = int(rect['w']*dpr), int(rect['h']*dpr)
    x, y = max(0,x), max(0,y)
    w, h = min(w, im.width-x), min(h, im.height-y)
    if w < 2 or h < 2:
        return None
    crop = im.crop((x, y, x+w, y+h))
    px = list(crop.getdata())
    if not px:
        return None
    # worst case = the two luminance extremes actually present behind the glyphs
    lo = min(px, key=lum); hi = max(px, key=lum)
    return lo, hi

def resolve_ground(chain):
    """Nearest ancestor with an OPAQUE background. No guessing — the browser
    already told us the computed backgroundColor of every ancestor."""
    acc = None
    for link in chain:
        # An image or gradient ANYWHERE in the chain means the true backdrop is
        # not a single colour. Bail to pixel sampling immediately — this is the
        # case the old gate confessed it could not see.
        if link['img']:
            return (acc or (255, 255, 255)), link['sel'], link['img']
        c = parse_rgb(link['bg'])
        if not c:
            continue
        if c[3] <= 0.001:
            continue
        if acc is None:
            acc = flatten(c, (255,255,255))
        if c[3] >= 0.999:
            return flatten(c, (255,255,255)), link['sel'], None
    return (acc or (255,255,255)), '(page)', None

def audit_page(page, path, mode_label):
    halts = []
    d = page.evaluate(PROBE)

    # -- 1. CONTRAST (computed grounds)
    shot = None
    for t in d['texts']:
        fg = parse_rgb(t['color'])
        if not fg:
            continue
        ground, gsel, gimg = resolve_ground(t['chain'])
        fgc = flatten(fg, ground)
        floor = WCAG_LARGE if t['large'] else WCAG_TEXT

        if gimg:  # text sits on an image/gradient -> MEASURE THE PIXELS
            if shot is None:
                shot = page.screenshot()
            got = px_bg_under(shot, t['rect'])
            if got:
                lo, hi = got
                r = min(ratio(fgc, lo), ratio(fgc, hi))
                if r < floor:
                    halts.append(f"CONTRAST [{mode_label}] {t['sel']} \"{t['text'][:24]}\" "
                                 f"= {r:.1f}:1 on IMAGE/GRADIENT (floor {floor})")
                continue

        r = ratio(fgc, ground)
        if r < floor:
            halts.append(f"CONTRAST [{mode_label}] {t['sel']} \"{t['text'][:24]}\" "
                         f"= {r:.1f}:1 (floor {floor}, ground {gsel})")

    # -- 2. TOKEN-ROLE LAW
    dual = set(d['tokens']['text']) & set(d['tokens']['deco'])
    for tok in sorted(dual):
        halts.append(f"TOKEN_ROLE {tok} is BOTH text and decoration. "
                     f"Light may be dim; text may not. Split it.")

    # -- 3. TOUCH TARGETS + FOCUS
    for t in d['targets']:
        if t['w'] < MIN_TARGET or t['h'] < MIN_TARGET:
            halts.append(f"TOUCH_TARGET [{mode_label}] {t['sel']} "
                         f"{t['w']:.0f}x{t['h']:.0f}px (floor {MIN_TARGET})")
        if not t['ring']:
            halts.append(f"FOCUS [{mode_label}] {t['sel']} has no visible focus ring")

    # -- 4. EMOJI
    for e in d['emoji']:
        halts.append(f"EMOJI in rendered text: \"{e}\"")

    # -- 5. NO OPENING WALL
    fs = d['firstScreen']
    if fs['gates'] > 0 and fs['prose'] == 0:
        halts.append(f"OPENING_WALL first paint shows {fs['gates']} preference control(s) "
                     f"{fs['gateTxt']} and NO scene. Comfort is a corner control, never a gate.")

    # -- 6. >50% IMAGE (founder standing floor — NEVER ENFORCED UNTIL 2026-07-13)
    #
    # The postmortem named this gap out loud: ">50% IMAGE — a stated founder floor.
    # Unchecked." So it was a wish. Every game shipped without anyone measuring it,
    # and Choose Your Leader v5 shipped a text wall as a result.
    #
    # SCOPE (caught by the canary, 2026-07-13): this floor is a GAME floor. The
    # golden canary p07 is a 3-line fixture with zero art and it must still pass —
    # it exists to test contrast, not scenery. A spec, a hub, a report, and a test
    # fixture are not games and are not graded as broken ones. Tableau Sweep #1 made
    # exactly this mistake, grading a spec-log as a failed game.
    #
    # A surface declares itself a game with:  <meta name="tsp:surface" content="game">
    # Absent that tag, the floor still runs on anything that ALREADY carries scene
    # art (>=1 media element) — because a game with a picture in it is a game.
    #
    # ARITHMETIC, not judgment: on the FIRST SCREEN, sum the area of every
    # scene-carrying element — svg/img/canvas/video/picture, or any element painting
    # a background-image or gradient — and divide by the viewport. Under 50% HALTs.
    img = page.evaluate("""() => {
      const vw = innerWidth, vh = innerHeight, VP = vw * vh;
      const seen = [], hits = [];
      for (const el of document.querySelectorAll('*')) {
        const r = el.getBoundingClientRect();
        if (r.width < 8 || r.height < 8) continue;
        if (r.top > vh || r.bottom < 0 || r.left > vw || r.right < 0) continue;
        const cs = getComputedStyle(el);
        if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) continue;
        const tag = el.tagName.toLowerCase();
        const painted = cs.backgroundImage && cs.backgroundImage !== 'none';
        const isMedia = ['svg','img','canvas','video','picture'].includes(tag);
        if (!isMedia && !painted) continue;
        if (seen.some(s => s.contains(el))) continue;   // no double-count of children
        seen.push(el);
        const w = Math.min(r.right, vw) - Math.max(r.left, 0);
        const h = Math.min(r.bottom, vh) - Math.max(r.top, 0);
        hits.push({ tag, area: Math.max(0, w) * Math.max(0, h) });
      }
      const m = document.querySelector('meta[name="tsp:surface"]');
      return { pct: VP ? (hits.reduce((a,b)=>a+b.area,0) / VP) * 100 : 0,
               n: hits.length,
               surface: m ? m.content : '',
               top: hits.sort((a,b)=>b.area-a.area).slice(0,3).map(h=>h.tag) };
    }""")
    is_game = img['surface'] == 'game' or (not img['surface'] and img['n'] > 0)
    if is_game and img['pct'] < 50:
        halts.append(f"IMAGE_FLOOR [{mode_label}] first screen is {img['pct']:.0f}% image "
                     f"(floor 50). {img['n']} scene element(s): {', '.join(img['top']) or 'none'}. "
                     f"Scene-first is a floor, not a preference — a first paint that is mostly "
                     f"prose is a document with buttons.")

    return halts, d

def audit(path, no_net=True):
    from playwright.sync_api import sync_playwright
    halts = []
    external = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        try:
            ctx = b.new_context(viewport={'width':390,'height':844})  # phone-width

            def on_req(r):
                u = r.url
                if u.startswith(('http://','https://')) and 'file://' not in u:
                    host = re.match(r'https?://([^/]+)', u)
                    if host:
                        external.append(host.group(1))
            ctx.on('request', on_req)

            page = ctx.new_page()
            page.goto('file://' + os.path.abspath(path), wait_until='load')
            page.wait_for_timeout(250)

            h, d = audit_page(page, path, 'default')
            halts += h

            # -- 6. OFFLINE FLOOR
            for host in sorted(set(external)):
                halts.append(f"OFFLINE external host contacted: {host} "
                             f"(single-file, offline floor)")

            # -- 7. COMFORT STOPS: separation + each stop audited independently
            stops = d['stops']
            lums = {}
            base = page.evaluate("()=>getComputedStyle(document.body).backgroundColor")
            bc = parse_rgb(base)
            if bc:
                lums['(default)'] = lum(flatten(bc,(255,255,255)))
            for s in stops:
                page.evaluate(f"()=>{{document.body.className='{s}';}}")
                page.wait_for_timeout(80)
                sb = parse_rgb(page.evaluate("()=>getComputedStyle(document.body).backgroundColor"))
                if sb:
                    lums[s] = lum(flatten(sb,(255,255,255)))
                h2, _ = audit_page(page, path, s)
                halts += [x for x in h2 if x.startswith('CONTRAST')]
            page.evaluate("()=>{document.body.className='';}")

            ks = list(lums.items())
            for i in range(len(ks)):
                for j in range(i+1, len(ks)):
                    (n1,l1),(n2,l2) = ks[i], ks[j]
                    if abs(l1-l2) < STOP_SEP_MIN:
                        halts.append(f"STOP_SEPARATION '{n1}' and '{n2}' differ by only "
                                     f"{abs(l1-l2):.3f} luminance (floor {STOP_SEP_MIN}). "
                                     f"A knob that changes nothing is a WALL.")

            # -- 8. DARK MODE / FORCED COLORS (where the EN195 bug hides)
            for scheme in ('dark',):
                page.emulate_media(color_scheme=scheme)
                page.wait_for_timeout(80)
                h3, _ = audit_page(page, path, f'prefers-{scheme}')
                halts += [x for x in h3 if x.startswith('CONTRAST')]
            page.emulate_media(color_scheme='light')
        finally:
            b.close()

    # dedupe, then order by severity. The headline defect must lead: a preference
    # gate on first paint is a WALL, and reporting its button size first buries it.
    SEV = {'OPENING_WALL':0, 'OFFLINE':1, 'EMOJI':2, 'CONTRAST':3,
           'TOKEN_ROLE':4, 'STOP_SEPARATION':5, 'FOCUS':6, 'TOUCH_TARGET':7}
    out, s = [], set()
    for x in halts:
        if x not in s:
            s.add(x); out.append(x)
    out.sort(key=lambda h: SEV.get(h.split()[0], 9))
    return out

# ---------------------------------------------------------------- self-test

def self_test(verbose=True):
    """The auditor gates itself before it gates anything else.
    Half these canaries are FALSE-POSITIVE traps: correct files that v2 wrongly
    HALTed. Crying wolf is the failure that got the tool ignored."""
    here = os.path.dirname(os.path.abspath(__file__))
    cdir = os.path.join(here, 'canary')
    exp_path = os.path.join(cdir, 'EXPECTED.json')
    if not os.path.exists(exp_path):
        print("  SELF-TEST: canary corpus missing. Refusing to run.")
        return False
    expected = json.load(open(exp_path))

    fails = []
    for c in expected:
        f = os.path.join(cdir, c['file'])
        halts = audit(f)
        got = 'HALT' if halts else 'PASS'
        ok = (got == c['expect'])
        if ok and c['expect'] == 'HALT' and c['code']:
            if not any(h.startswith(c['code']) for h in halts):
                ok = False
                got = f"HALT (wrong code: {halts[0].split()[0]})"
        if not ok:
            fails.append((c, got, halts))
        if verbose:
            mark = 'ok  ' if ok else 'FAIL'
            print(f"  {mark} {c['file']:<32} expect {c['expect']:<4} got {got}")

    if fails:
        print(f"\n  SELF-TEST FAILED — {len(fails)}/{len(expected)} canaries misgraded.")
        for c, got, halts in fails:
            print(f"\n    {c['file']}  ({c['why']})")
            print(f"      expected {c['expect']}, got {got}")
            for h in halts[:3]:
                print(f"        - {h}")
        print("\n  The auditor cannot grade its own canary. IT WILL NOT AUDIT.")
        return False
    print(f"\n  SELF-TEST PASSED — {len(expected)}/{len(expected)} canaries graded correctly.")
    return True

# ---------------------------------------------------------------- cli

def main():
    args = [a for a in sys.argv[1:]]
    if '--self-test' in args:
        print("\n  STUDIO EYES v3 · SELF-TEST\n  " + "-"*46)
        sys.exit(0 if self_test() else 1)

    skip = '--no-self-test' in args
    files = [a for a in args if not a.startswith('--')]
    if not files:
        print(__doc__)
        sys.exit(2)

    if not skip:
        print("\n  STUDIO EYES v3 · self-test\n  " + "-"*46)
        if not self_test(verbose=False):
            sys.exit(1)

    bad = 0
    for f in files:
        halts = audit(f)
        print(f"\n  {os.path.basename(f)}")
        if not halts:
            print("     PASS")
        else:
            bad += 1
            print(f"     HALT — {len(halts)} defect(s):")
            for h in halts[:14]:
                print(f"       {h}")
            if len(halts) > 14:
                print(f"       ... +{len(halts)-14} more")
    print(f"\n  === {bad} of {len(files)} at HALT ===\n")
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
