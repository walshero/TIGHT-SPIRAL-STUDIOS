#!/usr/bin/env python3
# ============================================================================
# STUDIO EYES — PIXEL CHECKER (true-pixel contrast, light + dark)
# ----------------------------------------------------------------------------
# WHY THIS EXISTS
#   studio-eyes-sweep.py renders with WeasyPrint, which GROUNDS text to <body>
#   when the real painted background is a dark/gradient/overlay ancestor. That
#   produces BOTH errors:
#     - false positives (dark-ground text flagged unreadable), and
#     - false negatives (gold-on-gold / white-on-white text passes — the FERPA
#       label invisibility the manifest caught only with a Chromium sweep).
#   This tool loads the page in REAL Chromium (executes JS, real compositing),
#   then reads the ACTUAL painted pixels behind each text run. No grounding
#   guess. It checks regular AND dark mode.
#
# METHOD
#   For each (colorScheme in {light,dark}) x (viewport in {390,1100}):
#     - render the page, full-page screenshot at devicePixelRatio 1
#     - for every element with visible direct text: computed text color +
#       the MODE (dominant, quantized) painted color inside its box = the true
#       background. Mode beats anti-aliased glyph pixels, so invisible text
#       (text≈bg) reads as ~1:1 and is caught.
#     - WCAG contrast; large text = >=24px or >=18.66px bold (floor 3.0), else 4.5.
#
# TEETH: a gold-on-gold fixture MUST fail and a black-on-white fixture MUST
#   pass, in both modes, before any real file is judged. If the teeth misbehave
#   the tool HALTs (exit 2) rather than certify — an auditor that can't prove
#   itself does not get to pass anything.
#
# USAGE:  python3 studio-eyes-pixel.py <file.html> [more.html ...]
# EXIT :  0 all clear · 1 contrast HALT · 2 teeth failed / cannot run
# ============================================================================
import sys, os, glob, tempfile, collections
from playwright.sync_api import sync_playwright

def _chromium_exe():
    """Use the pre-installed Chromium if present (browser build may not match the
    pip playwright build); otherwise let Playwright use its default."""
    base = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "")
    for pat in (os.path.join(base, "chromium-*/chrome-linux/chrome"),
                os.path.join(base, "chromium-*/chrome-linux64/chrome")):
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    return None
from PIL import Image

WIDTHS = [390, 1100]
MODES  = ["light", "dark"]
AA = 4.5      # normal-text floor
AL = 3.0      # large-text floor

def _lin(c):
    c /= 255.0
    return c/12.92 if c <= 0.03928 else ((c+0.055)/1.055) ** 2.4

def contrast(a, b):
    la = 0.2126*_lin(a[0]) + 0.7152*_lin(a[1]) + 0.0722*_lin(a[2])
    lb = 0.2126*_lin(b[0]) + 0.7152*_lin(b[1]) + 0.0722*_lin(b[2])
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

# JS: text elements INTERSECTING THE CURRENT VIEWPORT, with an occlusion test.
# Viewport-relative coords match a viewport (not full_page) screenshot, so
# fixed/overlay elements are sampled where they actually paint. elementFromPoint
# drops anything not truly on top (closed overlays, occluded text).
COLLECT_VP = r"""
() => {
  const out = [], vw = innerWidth, vh = innerHeight;
  for (const el of document.body.querySelectorAll('*')) {
    let t = '';
    for (const n of el.childNodes) if (n.nodeType === 3) t += n.textContent;
    t = t.replace(/\s+/g, ' ').trim();
    if (!t) continue;
    const r = el.getBoundingClientRect();
    if (r.bottom <= 0 || r.top >= vh || r.right <= 0 || r.left >= vw) continue;  // not in viewport
    if (r.width < 2 || r.height < 2) continue;
    const cs = getComputedStyle(el);
    if (el.checkVisibility && !el.checkVisibility({checkOpacity: true, checkVisibilityCSS: true})) continue;
    if (cs.visibility === 'hidden' || cs.display === 'none' || parseFloat(cs.opacity) === 0) continue;
    // WCAG exempts disabled / inactive controls from contrast.
    if (el.closest('[disabled], [aria-disabled="true"], fieldset:disabled')) continue;
    const m = (cs.color.match(/[\d.]+/g) || []).map(Number);
    if (m.length < 3) continue;
    if (m.length >= 4 && m[3] === 0) continue;
    const area = r.width * r.height;
    if (el.children.length > 0 && area > vw * vh * 0.55) continue;  // skip big containers
    // OCCLUSION: is this element (or its own subtree) the topmost paint at its center?
    const cx = Math.min(vw - 1, Math.max(0, r.left + r.width / 2));
    const cy = Math.min(vh - 1, Math.max(0, r.top + r.height / 2));
    const top = document.elementFromPoint(cx, cy);
    if (!top) continue;
    if (top !== el && !el.contains(top) && !top.contains(el)) continue;   // occluded / hidden
    out.push({
      x: Math.round(r.left), y: Math.round(r.top),        // viewport-relative
      w: Math.round(r.width), h: Math.round(r.height),
      color: [m[0], m[1], m[2]],
      fontPx: parseFloat(cs.fontSize), weight: parseInt(cs.fontWeight) || 400,
      tag: el.tagName.toLowerCase(), text: t.slice(0, 42),
      id: el.tagName + '|' + t.slice(0, 50) + '|' + Math.round(r.left + scrollX) + ',' + Math.round(r.top + scrollY)
    });
  }
  return out;
}
"""

def mode_bg(img, el, tc):
    """True painted background inside the element box.
    The dominant colour band that is NOT the text colour = the background — so a
    small button whose glyphs fill most of its box is grounded to the button
    fill, not to its own text. If NO band is far from the text colour, the box is
    essentially one colour with the text: that IS invisible text, so we return
    the dominant colour (~text) and contrast reads ~1:1 and is flagged."""
    W, H = img.size
    x0 = max(0, el["x"]); y0 = max(0, el["y"])
    x1 = min(W, el["x"] + el["w"]); y1 = min(H, el["y"] + el["h"])
    if x1 <= x0 or y1 <= y0:
        return None
    sx = max(1, (x1 - x0) // 40); sy = max(1, (y1 - y0) // 40)
    far = collections.defaultdict(list)    # pixels NOT the text colour (candidate bg)
    allb = collections.defaultdict(list)   # every pixel (fallback = invisible case)
    px = img.load()
    for yy in range(y0, y1, sy):
        for xx in range(x0, x1, sx):
            p = px[xx, yy]
            key = (p[0] >> 4, p[1] >> 4, p[2] >> 4)   # quantize /16
            allb[key].append(p)
            if max(abs(p[0]-tc[0]), abs(p[1]-tc[1]), abs(p[2]-tc[2])) > 40:
                far[key].append(p)
    src = far if far else allb
    if not src:
        return None
    best = max(src.values(), key=len)
    n = len(best)
    return (sum(p[0] for p in best)//n, sum(p[1] for p in best)//n, sum(p[2] for p in best)//n)

def is_large(el):
    return el["fontPx"] >= 24 or (el["fontPx"] >= 18.66 and el["weight"] >= 700)

VH = 1000   # viewport height per tile

def check(page, url):
    """Viewport-tiled true-pixel sweep across modes x widths for one url."""
    fails = []
    FREEZE = ("*,*::before,*::after{animation:none!important;"
              "transition:none!important;animation-duration:0s!important;"
              "animation-delay:0s!important;transition-duration:0s!important}")
    for mode in MODES:
        page.emulate_media(color_scheme=mode, reduced_motion="reduce")
        for w in WIDTHS:
            page.set_viewport_size({"width": w, "height": VH})
            page.goto(url, wait_until="load")
            # measure the SETTLED UI: kill transitions/animations so overlays are
            # sampled at their final opacity, not a mid-fade blend.
            page.add_style_tag(content=FREEZE)
            page.wait_for_timeout(300)
            doch = page.evaluate("Math.max(document.documentElement.scrollHeight, innerHeight)")
            seen = set()
            y = 0
            while y < doch:
                page.evaluate(f"scrollTo(0,{y})")
                page.wait_for_timeout(60)
                els = page.evaluate(COLLECT_VP)
                shot = tempfile.mktemp(suffix=".png")
                page.screenshot(path=shot)                 # VIEWPORT only — coords align
                img = Image.open(shot).convert("RGB")
                for el in els:
                    if el["id"] in seen:
                        continue
                    seen.add(el["id"])
                    bg = mode_bg(img, el, el["color"])      # viewport-relative box
                    if bg is None:
                        continue
                    cr = contrast(el["color"], bg)
                    floor = AL if is_large(el) else AA
                    if cr < floor:
                        fails.append({
                            "mode": mode, "w": w, "cr": round(cr, 2), "floor": floor,
                            "text": el["text"], "fontPx": round(el["fontPx"], 1),
                            "color": tuple(el["color"]), "bg": bg, "tag": el["tag"]
                        })
                os.remove(shot)
                y += VH - 50                                # small overlap
    return fails

def self_test(page):
    bad = tempfile.mktemp(suffix=".html")
    good = tempfile.mktemp(suffix=".html")
    open(bad, "w").write(
        '<!doctype html><meta name=color-scheme content="light dark">'
        '<body style="background:#e8c96a;margin:0;padding:40px">'
        '<p style="color:#e8c96a;font-size:20px">FERPA — gold on gold, invisible</p></body>')
    open(good, "w").write(
        '<!doctype html><meta name=color-scheme content="light dark">'
        '<body style="background:#ffffff;margin:0;padding:40px">'
        '<p style="color:#111111;font-size:20px">Black on white, readable</p></body>')
    bad_fail = len(check(page, "file://" + bad)) > 0
    good_fail = len(check(page, "file://" + good)) > 0
    os.remove(bad); os.remove(good)
    return bad_fail and not good_fail

def main(argv):
    files = [a for a in argv if not a.startswith("-")]
    if not files:
        print("usage: studio-eyes-pixel.py <file.html> [more.html ...]"); return 2
    with sync_playwright() as pw:
        exe = _chromium_exe()
        browser = pw.chromium.launch(executable_path=exe) if exe else pw.chromium.launch()
        page = browser.new_page(device_scale_factor=1)
        if not self_test(page):
            print("HALT — teeth failed: the pixel checker cannot prove itself; refusing to certify.")
            browser.close(); return 2
        print("self-test: teeth verified (gold-on-gold HALTs, black-on-white passes) — light+dark")
        total = 0
        for f in files:
            url = "file://" + os.path.abspath(f)
            fails = check(page, url)
            # dedupe identical (text, mode, w) rows
            seen = set(); uniq = []
            for x in fails:
                k = (x["text"], x["mode"], x["w"], x["cr"])
                if k in seen: continue
                seen.add(k); uniq.append(x)
            if not uniq:
                print(f"\nSHIP  {os.path.basename(f)} — every text run clears its floor in light + dark")
                continue
            total += 1
            print(f"\nHALT  {os.path.basename(f)} — {len(uniq)} text run(s) below floor:")
            for x in sorted(uniq, key=lambda r: r["cr"])[:40]:
                print("   [%s@%d] %s:1 < %s  '%s' fs=%s  color%s on bg%s"
                      % (x["mode"], x["w"], x["cr"], x["floor"], x["text"],
                         x["fontPx"], x["color"], x["bg"]))
            if len(uniq) > 40:
                print("   (+%d more)" % (len(uniq) - 40))
        browser.close()
        print("\n=== %d file(s) at HALT of %d (true-pixel, %d modes x %d widths) ==="
              % (total, len(files), len(MODES), len(WIDTHS)))
        return 1 if total else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
