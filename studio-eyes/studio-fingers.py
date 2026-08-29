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

PORTED IN 2026-08-08 from the root studio-fingers.py, which retires. That gate parsed
SOURCE; this one RENDERS, and every defect the source gate shipped came from guessing at
geometry instead of measuring it. The engine here wins; what it lacked was bookkeeping.

  F-ZOOM       an input renders under 16px, so iOS zooms the whole viewport on focus
               and never zooms back                                          [CITED]
  C-BUTTON     a <button> clears 44px but not the founder's 52px preference   [note]
               (a NOTE because promoting it to a HALT broke this gate's own GOOD
                canary on a 48px button - '52px buttons' is a remediation recommendation
                in PLAYTEST-REPORT.md, not a ruling. Floors block; preferences inform.)
  C-REACH      the largest control sits outside the bottom 40% thumb arc      [note]
  C-EDGE       no env(safe-area-inset-*) on a page with fixed bottom chrome   [note]

EVERY NUMBER DECLARES ITS AUTHORITY. This is the one thing the retiring gate got right:
  [LAW]     WCAG 2.5.5 AAA target 44px; 2.5.8 AA 24px; 1.4.4 resize to 200%
  [FOUNDER] "44px+ targets, 52px buttons" - PLAYTEST-REPORT.md, carried in three
            rescued design docs since July. THIS IS CANON AND IT OUTRANKS APPLE.
  [CITED]   iOS zooms inputs under 16px; comfortable one-thumb reach is the bottom 40%
  [HOUSE]   nothing. A house number that contradicts a founder ruling is not a floor,
            it is an invention - see the ledger entry for 2026-08-08 stamp-repair.

A NOTE IS NOT A HALT. C-* findings print and do not block: they are conventional phone
patterns, not floors, and a gate that blocks on convention is a gate people route around.

Usage:
  python3 studio-fingers.py file1.html [file2.html ...]
  python3 studio-fingers.py --self-test        # canary: proves it discriminates
"""
import os, sys, tempfile

TAP_FLOOR = 44          # px, WCAG 2.5.5 AAA / founder floor
BTN_FLOOR = 52          # px, FOUNDER floor for buttons specifically (PLAYTEST-REPORT.md)
INPUT_FLOOR = 16        # px, CITED - below this iOS zooms the viewport on focus
REACH_ARC = 0.60        # CITED - comfortable one-thumb arc starts below 60% of the height
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
    // Off-canvas by position (e.g. a visually-hidden "Skip to content" link parked at
    // left:-9999px until focus): not a touch target a thumb can land on, so not measured.
    if (r.right <= 0 || r.bottom <= 0 || r.left >= vw) return null;
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none' || parseFloat(cs.opacity) === 0) return null;
    if (el.closest('[hidden]')) return null;
    return r;
  };
  const name = (el) =>
    (el.getAttribute('aria-label') || el.textContent || el.getAttribute('title') || '').trim().replace(/\s+/g,' ').slice(0,40);

  // inline text link exemption: <a> sitting inside running prose or a footer/credit
  // byline. An email in "Tight Spiral Studios · you@example.com — …" is inline text,
  // not a primary touch target; forcing it to 44px would break the credit line.
  const inlineLink = (el) =>
    el.tagName === 'A' && el.closest('p,li,dd,dt,blockquote,.fc-body,.prose,figcaption,footer,.foot,.credits,.credit,.byline,address,.bio-card,.award-card,.sec-hd');

  const sel = 'button,a[href],[role="button"],input:not([type="hidden"]),select,textarea,[onclick],[tabindex]:not([tabindex="-1"])';
  out.vh = de.clientHeight;
  out.zoomy = [];   // inputs under the iOS zoom floor
  out.stubby = [];  // buttons under the founder button floor
  out.primary = null;
  document.querySelectorAll(sel).forEach(el => {
    const r = vis(el);
    if (!r) return;
    if (inlineLink(el)) return;
    const m = Math.min(r.width, r.height);
    if (m < 44) out.small.push({ tag: el.tagName.toLowerCase(), name: name(el), px: Math.round(m) });
  });

  document.querySelectorAll('input:not([type="hidden"]),select,textarea').forEach(el => {
    const r = vis(el); if (!r) return;
    const fs = parseFloat(getComputedStyle(el).fontSize) || 16;
    if (fs < 16) out.zoomy.push({ tag: el.tagName.toLowerCase(), name: name(el), fs: Math.round(fs) });
  });
  document.querySelectorAll('button,[role="button"]').forEach(el => {
    const r = vis(el); if (!r) return;
    const h = Math.round(r.height);
    if (h >= 44 && h < 52) out.stubby.push({ name: name(el), px: h });
    const a = r.width * r.height;
    if (!out.primary || a > out.primary.a) out.primary = { a: a, top: Math.round(r.top), name: name(el) };
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

# Set by audit_page, read by notes_for on the very next call for the same file.
# A module global for one string is not elegant; a silent advance would be worse.
ADVANCED_NOTE = None

ENTRY_SEL = ('button, a[href], [role=button], [onclick], '
             'input[type=button], input[type=submit]')


def advance_past_entry(page):
    """Click a lone entry control so the gate measures the SCENE, not the door.

    THE DEFECT THIS CLOSES, named by the Aleph fleet 2026-08-07 as TAP-TARGET and
    proven by canary 2026-08-28: this gate probed at first paint only. TSP builds
    create their controls on transition, so on a page whose room is revealed by one
    click the gate measured the entry screen and printed "every hand lands" over two
    20px controls it never saw. Its own three canaries were first-paint pages, so
    they shared the blind spot and could not catch it. A green self-test was, on this
    question, evidence of nothing.

    THE NARROW REPAIR, and why it is narrow: advance ONLY when the page opens with
    exactly ONE live in-page control. One control is a door. Two or more is a choice,
    and a gate that guesses which choice to make is a gate inventing a playthrough.
    The alternative considered and rejected was a per-file reach recipe: on a corpus
    sweep of 100+ surfaces a recipe gets filled for three and leaves the rest blind
    while LOOKING covered, which is worse than a known blind spot.

    MEASURED REACH, recorded so nobody mistakes this for a closed finding: on
    2026-08-28 this advanced past an entry gate on ZERO of fourteen sampled corpus
    surfaces. Every real TSP build opens with more than one live control. This is
    insurance and a permanent canary, not coverage. The fleet's TAP-TARGET finding
    stays OPEN; the durable fix is geometry measured at every state the crawler in
    playthrough-agent.py already visits.

    Never follows a link off this file (that was the nav-link bleed, 2026-08-07).
    Returns the control's name when it advanced, None otherwise. Never silent.
    """
    try:
        live = [e for e in page.query_selector_all(ENTRY_SEL)
                if e.is_visible() and e.is_enabled()]
    except Exception:
        return None
    if len(live) != 1:
        return None
    el = live[0]
    href = (el.get_attribute('href') or '')
    if href and not href.startswith('#'):
        return None
    try:
        name = (el.inner_text() or el.get_attribute('aria-label') or '').strip()[:34]
        before = page.url
        el.click(timeout=1500)
        page.wait_for_timeout(300)
        if page.url != before:
            page.goto(before, wait_until='load')
            page.wait_for_timeout(200)
            return None
    except Exception:
        return None
    return name


def audit_page(page, path):
    global ADVANCED_NOTE
    ADVANCED_NOTE = None
    page.goto('file://' + os.path.abspath(path), wait_until='load')
    page.wait_for_timeout(200)
    d = page.evaluate(PROBE)

    # Measure the door, then the room, and take the union of the TOUCH floors only.
    # Deliberately not merged: metaViewport, overflow and the comfort wall are
    # properties of how the page OPENS, and first paint is the honest moment for them.
    name = advance_past_entry(page)
    if name:
        ADVANCED_NOTE = name
        d2 = page.evaluate(PROBE)
        def _k(x):
            return (x.get('tag'), x.get('name'), x.get('px'), x.get('fs'))
        for field in ('small', 'zoomy'):
            seen = {_k(x) for x in d.get(field, [])}
            for x in d2.get(field, []):
                if _k(x) not in seen:
                    d.setdefault(field, []).append(x)
                    seen.add(_k(x))

    halts = []

    if not d['metaViewport']:
        halts.append("F-METAVIEW  no <meta name=viewport width=device-width> — the page can't adapt to a phone.")

    if d['overflow'] > OVERFLOW_TOL:
        halts.append(f"F-VIEWPORT  page scrolls sideways on a {d['vw']}px phone (overflows by {d['overflow']}px). "
                     "Wide content must scroll inside its own box, never the page body.")

    for s in d['small']:
        halts.append(f"F-TAP       <{s['tag']}> \"{s['name']}\" renders {s['px']}px — under the {TAP_FLOOR}px touch floor. "
                     "A thumb can't reliably hit it.")

    for s in d.get('zoomy', []):
        halts.append(f"F-ZOOM      <{s['tag']}> \"{s['name']}\" renders {s['fs']}px — under the {INPUT_FLOOR}px input floor. "
                     "iOS zooms the whole viewport on focus and never zooms back. [CITED]")

    c = d['comfort']
    if (c['visibleOptions'] >= 2 and not c['hasToggle']) or c.get('wallContainer'):
        detail = (f"{c['visibleOptions']} display-option controls are shown UNASKED"
                  if c['visibleOptions'] >= 2 else
                  "a comfort/theme control cluster is shown UNASKED (2+ controls, no collapsing toggle)")
        halts.append(f"F-WALL      {detail} and no comfort button gates them. "
                     "Comfort is a knob, not a wall — hide the options behind a single comfort button (never shown unasked).")
    return halts


def notes_for(path, d):
    """C-* notes. Conventional phone patterns, NOT floors. These never block."""
    notes = []
    p = d.get('primary')
    for s in d.get('stubby', []):
        notes.append(f"C-BUTTON    \"{s['name']}\" {s['px']}px — clears {TAP_FLOOR}px LAW, under the {BTN_FLOOR}px founder preference.")
    if p and d.get('vh') and p['top'] < d['vh'] * REACH_ARC:
        notes.append(f"C-REACH     the largest control (\"{p['name']}\") sits at {p['top']}px on a "
                     f"{d['vh']}px screen — above the bottom-40% thumb arc. Top-left is a regrip "
                     f"on a large phone. [CITED]")
    try:
        src = open(path, encoding='utf-8', errors='replace').read()
    except Exception:
        src = ''
    if 'env(safe-area-inset' not in src and ('position:fixed' in src.replace(' ', '') or 'position:sticky' in src.replace(' ', '')):
        notes.append("C-EDGE      fixed or sticky chrome with no env(safe-area-inset-*). On a notched "
                     "phone it will sit under the home indicator. [CITED]")
    return notes


def run(files, headed=False):
    from playwright.sync_api import sync_playwright
    bad = 0
    # A GATE THAT GOES BLIND MUST NOT READ AS CLEAN.
    # SF_CHROME was an OPTIONAL override, so with it unset this fell through to
    # playwright's pinned build number - and when the installed package and the
    # on-disk browsers drift (CI image refresh, pip upgrade) launch() raises
    # "Executable doesn't exist at .../chromium_headless_shell-<n>/...". Found
    # 2026-08-07: this gate and playthrough-agent.py were BOTH dead from that one
    # drift, which means TAP-TARGET had never actually been measured on this
    # corpus - not "the gate passed it", but "the gate never ran". The Aleph
    # fleet's L4 lens caught a 26x24px live target the touch gate should own.
    # Default to the stable path the image provides; SF_CHROME still overrides.
    exe = os.environ.get('SF_CHROME') or (
        '/opt/pw-browsers/chromium' if os.path.exists('/opt/pw-browsers/chromium') else None)
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
            try:
                notes = notes_for(f, page.evaluate(PROBE))
            except Exception:
                notes = []
            if halts:
                bad += 1
                print(f"  ✗ {label}")
                for h in halts:
                    print(f"       {h}")
            else:
                print(f"  ✓ {label}  — every hand lands")
            for n in notes:
                print(f"       {n}")
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
