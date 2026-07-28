#!/usr/bin/env python3
"""
STUDIO FINGERS — the touch wing of Studio Eyes.

Studio Eyes checks what the reader SEES (contrast, image floor, ground).
Studio Fingers checks what the reader DOES with a thumb: tap, swipe, slide —
the full affordance of the device. It renders each page on a real mobile touch
viewport and HALTs on the ways a game fails a hand.

CHECKS (each a HALT, exit 1):
  F-TAP        an interactive control renders smaller than the 44px touch floor
               (founder floor: "44px+ targets, 52px buttons"). Inline text links
               are exempt (WCAG 2.5.5 inline exception).
  F-VIEWPORT   the page scrolls sideways on a phone (body wider than the viewport)
  F-METAVIEW   no <meta name="viewport" width=device-width> — pinch-zoom roulette
  F-WALL       comfort/display options are shown UNASKED (founder floor 2026-07-03:
               "comfort is a knob, not a wall"; sharpened 2026-07-22: the options
               stay hidden until the reader taps the comfort button). If two or
               more display-option controls are visible on load and no single
               collapsing comfort button gates them, that is a wall.

EXIT 0 = every hand lands.  EXIT 1 = HALT, do not ship.

Usage:
  python3 studio-fingers.py file1.html [file2.html ...]
  python3 studio-fingers.py --self-test        # canary: proves it discriminates
"""
import os, sys, tempfile

TAP_FLOOR = 44          # px, WCAG 2.5.5 AAA / founder floor
OVERFLOW_TOL = 2        # px slack for sub-pixel rounding

# Runs in the page. Returns a plain dict of findings — no DOM handles escape.
PROBE = r"""
() => {
  // clientWidth is the layout viewport; scrollWidth includes overflowing content.
  // Their difference is the canonical horizontal-overflow signal (window.innerWidth
  // is unreliable under mobile emulation).
  const de = document.documentElement;
  const vw = de.clientWidth;
  const out = { vw, metaViewport:false, overflow:0, small:[], comfort:{visibleOptions:0, hasToggle:false} };

  const mv = document.querySelector('meta[name="viewport"]');
  out.metaViewport = !!(mv && /width\s*=\s*device-width/i.test(mv.getAttribute('content')||''));

  out.overflow = Math.max(0, Math.round((de.scrollWidth||0) - vw));

  const vis = (el) => {
    const r = el.getBoundingClientRect();
    if (r.width <= 0 || r.height <= 0) return null;
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none' || parseFloat(cs.opacity) === 0) return null;
    if (el.closest('[hidden]')) return null;
    return r;
  };
  const name = (el) =>
    (el.getAttribute('aria-label') || el.textContent || el.getAttribute('title') || '').trim().replace(/\s+/g,' ').slice(0,40);

  // inline text link exemption: <a> sitting inside running prose
  const inlineLink = (el) =>
    el.tagName === 'A' && el.closest('p,li,dd,dt,blockquote,.fc-body,.prose,figcaption');

  const sel = 'button,a[href],[role="button"],input:not([type="hidden"]),select,textarea,[onclick],[tabindex]:not([tabindex="-1"])';
  document.querySelectorAll(sel).forEach(el => {
    const r = vis(el);
    if (!r) return;
    if (inlineLink(el)) return;
    const m = Math.min(r.width, r.height);
    if (m < 44) out.small.push({ tag: el.tagName.toLowerCase(), name: name(el), px: Math.round(m) });
  });

  // comfort wall: display/comfort controls shown WITHOUT being summoned.
  // Two signals so wording can't hide a wall:
  //  (a) LABEL — 2+ controls whose names read as display options, no collapsing toggle;
  //  (b) CONTAINER — a visible comfort/settings/theme container holding 2+ controls
  //      and no collapsing toggle (catches "Softer / Warm-dark / Dim the room / Default").
  const OPT = /bigger text|larger text|smaller text|reduce motion|reduced motion|text size|font size|high contrast|\bcontrast\b|comfort stop|softer|default|daylight|warm[\s-]?dark|dark mode|light mode|\bnight\b|dim the room|brightness|\btheme\b/i;
  const TOGGLE = /comfort|display option|accessibility|settings|\baa\b/i;
  const CONTAINER = /comfort|accessib|settings|display.?option|theme|palette|reading.?mode/i;
  const cname = (el) => {
    const cls = (el.className && el.className.baseVal !== undefined) ? el.className.baseVal : (el.className || '');
    return ((el.getAttribute('aria-label') || '') + ' ' + cls + ' ' + (el.id || '')).toLowerCase();
  };
  const collapses = (el) => el.hasAttribute('aria-expanded') || el.hasAttribute('aria-controls')
                            || !!el.querySelector('[aria-expanded],[aria-controls]');

  // STATUS chrome (draft ribbons, badges, deploy stamps) is not a comfort option,
  // even when its text happens to contain an option-word like "contrast" — the
  // draft ribbon reads "N contrast issues" and must not be counted as a display knob.
  const STATUS = /draft|ribbon|badge|\bstatus\b|deployed|last.?updated/i;
  let visibleOptions = 0, hasToggle = false, wallContainer = false;
  document.querySelectorAll(sel).forEach(el => {
    const n = name(el), r = vis(el);
    if (!r) return;
    if (STATUS.test(cname(el))) return;
    if (TOGGLE.test(n) && (el.hasAttribute('aria-expanded') || el.hasAttribute('aria-controls'))) hasToggle = true;
    else if (OPT.test(n)) visibleOptions++;
  });
  document.querySelectorAll('*').forEach(el => {
    if (!CONTAINER.test(cname(el)) || !vis(el) || collapses(el)) return;
    const ctrls = Array.prototype.slice.call(el.querySelectorAll(sel)).filter(vis);
    if (ctrls.length >= 2) wallContainer = true;
  });
  out.comfort.visibleOptions = visibleOptions;
  out.comfort.hasToggle = hasToggle;
  out.comfort.wallContainer = wallContainer;
  return out;
}
"""

def audit_page(page, path):
    page.goto('file://' + os.path.abspath(path), wait_until='load')
    page.wait_for_timeout(200)
    d = page.evaluate(PROBE)
    halts = []

    if not d['metaViewport']:
        halts.append("F-METAVIEW  no <meta name=viewport width=device-width> — the page can't adapt to a phone.")

    if d['overflow'] > OVERFLOW_TOL:
        halts.append(f"F-VIEWPORT  page scrolls sideways on a {d['vw']}px phone (overflows by {d['overflow']}px). "
                     "Wide content must scroll inside its own box, never the page body.")

    for s in d['small']:
        halts.append(f"F-TAP       <{s['tag']}> \"{s['name']}\" renders {s['px']}px — under the {TAP_FLOOR}px touch floor. "
                     "A thumb can't reliably hit it.")

    c = d['comfort']
    if (c['visibleOptions'] >= 2 and not c['hasToggle']) or c.get('wallContainer'):
        detail = (f"{c['visibleOptions']} display-option controls are shown UNASKED"
                  if c['visibleOptions'] >= 2 else
                  "a comfort/theme control cluster is shown UNASKED (2+ controls, no collapsing toggle)")
        halts.append(f"F-WALL      {detail} and no comfort button gates them. "
                     "Comfort is a knob, not a wall — hide the options behind a single comfort button (never shown unasked).")
    return halts


def run(files, headed=False):
    from playwright.sync_api import sync_playwright
    bad = 0
    exe = os.environ.get('SF_CHROME')  # optional explicit chromium path
    with sync_playwright() as p:
        launch = {}
        if exe: launch['executable_path'] = exe
        browser = p.chromium.launch(**launch)
        # a real mid-size phone: touch + coarse pointer + narrow viewport
        ctx = browser.new_context(viewport={'width':412,'height':915},
                                  device_scale_factor=2, is_mobile=True, has_touch=True)
        page = ctx.new_page()
        for f in files:
            # Paste-snippets / component fragments are not pages a phone loads —
            # no <html>/<body> root means there is nothing for a viewport to govern.
            try:
                head = open(f, encoding='utf-8', errors='replace').read(4000).lower()
                if '<html' not in head and '<body' not in head:
                    print(f"  – {os.path.basename(f)}  — fragment (snippet), not a page; skipped")
                    continue
            except Exception:
                pass
            try:
                halts = audit_page(page, f)
            except Exception as e:
                halts = [f"F-ERROR     could not audit ({e})"]
            label = os.path.basename(f)
            if halts:
                bad += 1
                print(f"  ✗ {label}")
                for h in halts:
                    print(f"       {h}")
            else:
                print(f"  ✓ {label}  — every hand lands")
        browser.close()
    print(f"\n  === {bad} of {len(files)} at HALT ===\n")
    return 1 if bad else 0


# --- self-test: two canaries, one clean one broken. Crying wolf is the failure. ---
GOOD = """<!doctype html><html lang=en><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1"><title>good</title>
<style>button{min-height:48px;min-width:48px;font-size:16px}.panel[hidden]{display:none}</style></head>
<body><button id=ct aria-expanded=false aria-controls=pan aria-label="Comfort and display options">Comfort</button>
<div class=panel id=pan hidden><button>Bigger text</button><button>Reduce motion</button></div>
<button>Play</button></body></html>"""

# BAD1 keeps a correct meta-viewport so the 1400px row genuinely overflows a
# 412px phone (F-VIEWPORT), plus a 22px control (F-TAP) and two display options
# shown unasked with no comfort toggle (F-WALL).
BAD1 = """<!doctype html><html lang=en><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1"><title>bad1</title>
<style>.tiny{width:22px;height:22px}</style></head>
<body><button class=tiny aria-label="menu">x</button>
<button>Bigger text</button><button>Reduce motion</button>
<div style="width:1400px">very wide row that overflows a phone</div></body></html>"""

# BAD2 isolates the missing-meta-viewport check (F-METAVIEW).
BAD2 = """<!doctype html><html lang=en><head><meta charset=utf-8><title>bad2</title>
<style>button{min-height:48px;min-width:48px}</style></head>
<body><button>Play</button></body></html>"""

def self_test():
    from playwright.sync_api import sync_playwright
    r = {}
    exe = os.environ.get('SF_CHROME')
    with tempfile.TemporaryDirectory() as td:
        paths = {}
        for k, html in (('good',GOOD), ('bad1',BAD1), ('bad2',BAD2)):
            paths[k] = os.path.join(td, k+'.html'); open(paths[k],'w').write(html)
        with sync_playwright() as p:
            b = p.chromium.launch(**({'executable_path': exe} if exe else {}))
            ctx = b.new_context(viewport={'width':412,'height':915}, is_mobile=True, has_touch=True)
            pg = ctx.new_page()
            for k in paths: r[k] = audit_page(pg, paths[k])
            b.close()
    codes1 = {h.split()[0] for h in r['bad1']}
    codes2 = {h.split()[0] for h in r['bad2']}
    ok_good = len(r['good']) == 0
    ok_bad1 = {'F-TAP','F-VIEWPORT','F-WALL'}.issubset(codes1)
    ok_bad2 = 'F-METAVIEW' in codes2
    print("  self-test:")
    print(f"    GOOD canary clean          : {'PASS' if ok_good else 'FAIL -> '+str(r['good'])}")
    print(f"    BAD1 (tap/viewport/wall)   : {'PASS' if ok_bad1 else 'FAIL -> got '+str(sorted(codes1))}")
    print(f"    BAD2 (missing meta view)   : {'PASS' if ok_bad2 else 'FAIL -> got '+str(sorted(codes2))}")
    return 0 if (ok_good and ok_bad1 and ok_bad2) else 1


def main():
    args = sys.argv[1:]
    if '--self-test' in args:
        sys.exit(self_test())
    files = [a for a in args if not a.startswith('--')]
    if not files:
        print(__doc__); sys.exit(2)
    print("\n  STUDIO FINGERS — touch-affordance wing (412px phone, touch)\n")
    sys.exit(run(files))


if __name__ == '__main__':
    main()
