#!/usr/bin/env python3
"""
ART EXECUTION GATE  ·  Tight Spiral Studios  ·  the teeth on "proper execution"
==============================================================================
Founder ruling 2026-08-13: "No MJ in studio as we can do better than we have so
far with proper execution." Affirmed 2026-08-14: the studio needs processes and
assets for producing quality art.

That ruling only means something if "proper execution" is CHECKABLE. Otherwise it
is a wish, and the studio has been here before: a rule that lives in prose and
gets re-argued every session is not a rule. This gate turns three execution
failures the studio has actually shipped into arithmetic.

WHY THESE THREE. Each one is a real defect found in a real build, not a style
opinion. All three were shipped by this studio and then caught by eye, which is
the expensive way to catch things:

  1. TYPE DOMINANCE — scene art out-glowing the text sitting on it.
     The Reads-As-Legibility seat's standing HALT. Text on a scene must be the
     brightest thing in that scene, because it is what the reader is reading and
     often what they are tapping. Measured, not eyeballed: every text node in a
     scene is walked to its real painted colour, every scene shape to its real
     painted fill, and the brightest shape must not reach the brightest type.

  2. CROSS-HATCH TEXTURE — two repeating gradients crossed to fake detail.
     A grid reads as a grid. Shipped 2026-08-13 in enjambment.html, where a
     window pattern painted the lower half of the frame as one magenta mesh.
     Texture is made of direction and interval, not of intersection.

  3. FLAT LAYER — every shape in a scene layer at one identical value.
     Shipped in the same file: pines drawn the same value as their own ridge, so
     the whole lower half painted as a single black band with no silhouette.
     Depth needs at least two values. One value is a shape, not a scene.

WHAT IS EXEMPT, AND WHY. Instruments — anything marked data-art-class="instrument"
— are excluded from TYPE DOMINANCE. A beat lamp, a meter, a blade indicator is
FOREGROUND that reports state; it is allowed and often required to be brighter
than body type. This reuses art-gate.py's existing vocabulary rather than
inventing a second one. Instruments are still checked for cross-hatch.

SCOPE. Only elements marked as scenes are examined: [data-scene] or .stage. A
gate that inspects every page cries wolf on ordinary documents, and an auditor
that cries wolf trains the founder to ignore it (the comfort-gate doctrine). A
page with no scene is not a failure, it is not this gate's business.

HONEST LIMITS, stated rather than implied:
  - Pseudo-element art (::before / ::after) is not enumerable from the DOM and is
    not measured. Marquee bulbs and scanlines pass unexamined.
  - Gradient fills are measured by their declared colour stops, alpha-composited
    over the scene's own ground. Mid-gradient blends are not sampled, so a stop is
    judged at full strength wherever it lands.
  - Overlap and abutment are not computed; FLAT LAYER checks value spread within
    a layer, not whether two same-value shapes actually touch.
  - FIRST PAINT ONLY. The gate measures the page as it loads. Art that appears
    later, mid-game, is not seen. Mark such art data-art-class="instrument" if it
    is state, or give its screen its own scene marker if it is scenery.

Usage:
  art-execution-gate.py <file.html> [more.html ...]   exit 1 on any HALT
  art-execution-gate.py --selftest                    prove the teeth still bite
"""
import sys, glob, pathlib

FLAT_MIN_SHAPES = 4     # below this a "layer" is not a layer worth judging

MEASURE_JS = r"""
() => {
  const lin = c => { c /= 255; return c <= 0.03928 ? c/12.92 : Math.pow((c+0.055)/1.055, 2.4); };
  const lum = ([r,g,b]) => 0.2126*lin(r) + 0.7152*lin(g) + 0.0722*lin(b);

  // every colour mentioned in a computed value, gradients included, WITH ALPHA.
  // Ignoring alpha made a 13%-opacity wash read as full-strength paint and the
  // gate cried wolf on its own studio's frame. A translucent layer is measured
  // as what it actually paints: composited over the ground beneath it.
  const colours = s => {
    const out = [];
    if (!s || s === 'none') return out;
    const re = /rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:[,\s/]+([\d.]+))?\s*\)/g;
    let m; while ((m = re.exec(s))) out.push([+m[1], +m[2], +m[3], m[4] === undefined ? 1 : +m[4]]);
    return out;
  };
  // effective luminance of a colour painted over a ground of luminance g
  const eff = (c, g) => { const a = c[3]; return a * lum(c) + (1 - a) * g; };
  const visible = el => {
    const s = getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden') return false;
    if (parseFloat(s.opacity || '1') === 0) return false;
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  };
  const isInstrument = el => !!el.closest('[data-art-class="instrument"]');

  const scenes = [...document.querySelectorAll('[data-scene], .stage')];
  return scenes.map((scene, si) => {
    const all = [...scene.querySelectorAll('*')].filter(visible);

    // ---- brightest TYPE actually painted in this scene
    let maxType = -1, typeWhere = '';
    const walker = document.createTreeWalker(scene, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      const t = walker.currentNode;
      if (!t.nodeValue || !t.nodeValue.trim()) continue;
      const el = t.parentElement;
      if (!el || !visible(el)) continue;
      const c = colours(getComputedStyle(el).color)[0];
      if (!c) continue;
      const L = eff(c, 0);
      if (L > maxType) { maxType = L; typeWhere = (el.className || el.tagName) + '' ; }
    }

    // ---- the ground everything else is painted over
    const ss = getComputedStyle(scene);
    let ground = 0;
    for (const c of colours(ss.backgroundColor).concat(colours(ss.backgroundImage))) {
      const L = eff(c, 0);
      if (L > ground) ground = L;
    }

    // ---- brightest SCENE SHAPE (instruments excluded: they report state)
    let maxShape = -1, shapeWhere = '';
    for (const el of all) {
      if (isInstrument(el)) continue;
      if (el.textContent && el.textContent.trim() && el.children.length === 0) continue;
      const s = getComputedStyle(el);
      const own = parseFloat(s.opacity || '1');
      for (const c of colours(s.backgroundColor).concat(colours(s.backgroundImage))) {
        const L = own * eff(c, ground) + (1 - own) * ground;
        if (L > maxShape) { maxShape = L; shapeWhere = (el.className || el.tagName) + ''; }
      }
    }

    // ---- CROSS-HATCH: two repeating gradients at different angles on one element
    const hatch = [];
    for (const el of all) {
      const bi = getComputedStyle(el).backgroundImage || '';
      const reps = bi.match(/repeating-linear-gradient\([^)]*/g) || [];
      if (reps.length < 2) continue;
      const angles = new Set(reps.map(r => (r.match(/(-?[\d.]+)deg/) || [,'none'])[1]));
      if (angles.size > 1) hatch.push({ where: (el.className || el.tagName) + '', angles: [...angles] });
    }

    // ---- FLAT LAYER: a layer whose every shape is one identical value
    const flat = [];
    const layers = new Map();
    for (const el of all) {
      if (isInstrument(el)) continue;
      const p = el.parentElement;
      if (!p) continue;
      const bg = getComputedStyle(el).backgroundColor;
      const c = colours(bg)[0];
      if (!c || c[3] === 0) continue;          // an unpainted child is not a shape
      const key = (p.className || p.tagName) + '';
      if (!layers.has(key)) layers.set(key, []);
      layers.get(key).push(bg);
    }
    for (const [key, vals] of layers) {
      if (vals.length < %FLAT_MIN%) continue;  // threshold counts PAINTED shapes only
      const uniq = new Set(vals);
      if (uniq.size === 1) flat.push({ where: key, n: vals.length, value: [...uniq][0] });
    }

    return {
      scene: (scene.className || scene.tagName) + '' , index: si,
      maxType, typeWhere, maxShape, shapeWhere, hatch, flat,
      shapes: all.length
    };
  });
}
"""


def measure(path):
    from playwright.sync_api import sync_playwright
    uri = pathlib.Path(path).resolve().as_uri()
    js = MEASURE_JS.replace('%FLAT_MIN%', str(FLAT_MIN_SHAPES))
    with sync_playwright() as pw:
        try:
            b = pw.chromium.launch()
        except Exception:
            b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        pg = b.new_page(viewport={'width': 390, 'height': 844})
        pg.goto(uri)
        pg.wait_for_timeout(450)
        out = pg.evaluate(js)
        b.close()
    return out


def judge(path, scenes):
    halts = []
    for s in scenes:
        tag = "%s scene[%d]" % (s['scene'].split()[0] if s['scene'] else '?', s['index'])
        if s['maxType'] >= 0 and s['maxShape'] >= 0 and s['maxShape'] >= s['maxType']:
            halts.append(
                "TYPE-DOMINANCE %s: scene art (%s, lum %.3f) is at or brighter than the "
                "brightest type on it (%s, lum %.3f). The reader's text must win."
                % (tag, s['shapeWhere'].split()[0] if s['shapeWhere'] else '?', s['maxShape'],
                   s['typeWhere'].split()[0] if s['typeWhere'] else '?', s['maxType']))
        for h in s['hatch']:
            halts.append(
                "CROSS-HATCH %s: '%s' crosses repeating gradients at angles %s. "
                "A grid reads as a grid; texture is direction and interval, not intersection."
                % (tag, h['where'].split()[0] if h['where'] else '?', ','.join(h['angles'])))
        for f in s['flat']:
            halts.append(
                "FLAT-LAYER %s: layer '%s' holds %d shapes at one identical value (%s). "
                "Depth needs two values; one value is a shape, not a scene."
                % (tag, f['where'].split()[0] if f['where'] else '?', f['n'], f['value']))
    return halts


CANARIES = {
    'art-exec-canary-dim-type.html': 'TYPE-DOMINANCE',
    'art-exec-canary-crosshatch.html': 'CROSS-HATCH',
    'art-exec-canary-flat.html': 'FLAT-LAYER',
}


def selftest():
    """A gate that stops false-positiving by going blind is broken the other way."""
    ok = True
    for f, expect in CANARIES.items():
        if not pathlib.Path(f).exists():
            print("  MISSING CANARY %s" % f); ok = False; continue
        halts = judge(f, measure(f))
        hit = any(h.startswith(expect) for h in halts)
        print("  %-34s expect %-16s -> %s" % (f, expect, "CAUGHT" if hit else "MISSED"))
        if not hit: ok = False
    p = 'art-exec-canary-pass.html'
    if pathlib.Path(p).exists():
        halts = judge(p, measure(p))
        print("  %-34s expect %-16s -> %s" % (p, "clean", "clean" if not halts else "FALSE POSITIVE: %s" % halts))
        if halts: ok = False
    print("\nSELFTEST: %s" % ("teeth still bite" if ok else "BROKEN"))
    return 0 if ok else 1


def main(argv):
    if not argv:
        print(__doc__); return 0
    if argv[0] == '--selftest':
        print("ART EXECUTION GATE - selftest\n" + "=" * 60)
        return selftest()

    files = []
    for a in argv:
        files.extend(sorted(glob.glob(a)) if any(c in a for c in '*?[') else [a])

    bad = 0
    print("ART EXECUTION GATE  ·  proper execution, as arithmetic")
    print("=" * 62)
    for f in files:
        scenes = measure(f)
        if not scenes:
            print("  %-34s no scene marked, not this gate's business" % f)
            continue
        halts = judge(f, scenes)
        if halts:
            bad += 1
            print("\nHALT  %s" % f)
            for h in halts: print("      " + h)
        else:
            print("  SHIP  %-30s %d scene(s) measured" % (f, len(scenes)))
    if bad:
        print("\n=== %d file(s) HALT on execution. Fix the frame, not the gate. ===" % bad)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
