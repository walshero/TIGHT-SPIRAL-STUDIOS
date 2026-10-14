#!/usr/bin/env python3
"""
STUDIO FINGERS · FEEDBACK FLOOR                          Tight Spiral Productions
-----------------------------------------------------------------------------
Built 2026-10-13 after the founder, on his own iPhone, playing Flok v31 lever 1:

    "The buttons we are talking about are cut off. And after the pop up, I can't
     see what just flashed if I miss it. It should be captured and explained ON
     screen."

Neither failure was visible to any gate. Static Fingers reads first paint; Play mode
reads whether controls are reachable. Nobody measured whether the THING THE LEVER
IS ABOUT (the like count on her newest post) was inside the window, or whether the
payout survived past its animation. This drives the core verb and measures both.

THE FLOORS (per viewport, per tap)
  F1 SUBJECT IN WINDOW  the newest post's action row (heart, count, comment) sits   HALT
                        fully inside the feed window AND the screen after every tap.
  F2 RESULT PERSISTS    2.5 s after a tap (all animation over) a receipt naming     HALT
                        THAT tap's result is on screen and inside the viewport.
  W1 POST TOP CLIPPED  the newest post's head is above the screen.                WARN
  F3 VERB IN VIEW       the verb button is inside the viewport after every tap.    HALT

Taps stop at the win. On the WINNING tap the game scrolls toward Next by design, so F1
checks the feed window only and F3 is skipped; F2 still binds, because that is the
moment a missed flash is likeliest. Post-win taps are exempt, as in fingers-play P1.

Viewports include the founder's: iPhone, Safari, toolbar collapsed (393x760), and the
same phone with the toolbar up (393x660). Exit 1 on any HALT.

Usage:
  python3 studio-senses/feedback-floor.py the-console.html
"""
import sys, pathlib, time
from playwright.sync_api import sync_playwright

VIEWPORTS = [("founder-iphone", 393, 760), ("iphone-toolbar", 393, 660),
             ("iphone-se", 375, 553), ("android", 412, 780)]
TAPS = 12

PROBE = """() => {
  const r = e => e ? e.getBoundingClientRect() : null;
  const feed = document.getElementById('feed');
  const card = feed && feed.querySelector('.feed-card');
  const act = card && card.querySelector('.fc-actions');
  const fr = r(feed), ar = r(act);
  // the receipt, or (winning tap) the line beside Next: whichever holds this tap's result
  const tapNo = (typeof T !== 'undefined' && T.taps) || 0;
  const holders = [document.getElementById('receipt'), document.getElementById('actHint')]
    .filter(e => e && !e.hidden && e.textContent.includes('Boost ' + tapNo + ':'));
  const vis = e => { const q = r(e); return q.height > 0 && q.top >= 0 && q.bottom <= innerHeight &&
                     getComputedStyle(e).visibility !== 'hidden' && +getComputedStyle(e).opacity > 0.9; };
  const rc = holders.find(vis) || holders[0] || document.getElementById('receipt');
  const rr = r(rc);
  const btn = document.querySelector('#actZone .act-btn'), br = r(btn);
  const vh = innerHeight;
  return {
    actionsInside: !!(fr && ar) && ar.top >= fr.top - 0.5 && ar.bottom <= fr.bottom + 0.5 && ar.top >= 0 && ar.bottom <= innerHeight,
    actionsInWindow: !!(fr && ar) && ar.top >= fr.top - 0.5 && ar.bottom <= fr.bottom + 0.5,
    cardTopOff: card ? Math.round(-Math.min(0, card.getBoundingClientRect().top)) : 0,
    actBottom: ar ? Math.round(ar.bottom) : null, feedBottom: fr ? Math.round(fr.bottom) : null,
    receipt: rc ? rc.textContent.trim() : '',
    receiptVisible: !!rr && rr.height > 0 && rr.top >= 0 && rr.bottom <= vh &&
                    getComputedStyle(rc).visibility !== 'hidden' && +getComputedStyle(rc).opacity > 0.9,
    verbVisible: !!br && br.top >= 0 && br.bottom <= vh,
    tap: (typeof T !== 'undefined' && T.taps) || 0,
    won: (typeof hit !== 'undefined') && hit
  };
}"""

def run(path):
    url = pathlib.Path(path).resolve().as_uri()
    halts, warns = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, w, h in VIEWPORTS:
            pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2,
                            has_touch=True, is_mobile=True)
            pg.goto(url); pg.wait_for_timeout(400)
            pg.evaluate("startTraining(); if (typeof beginLever === 'function') beginLever();"); pg.wait_for_timeout(700)
            for i in range(1, TAPS + 1):
                # a thumb, not a script: scroll only until Boost is fully on screen (bottom
                # edge, 16 px gap), never centre it, then tap where it is
                pg.evaluate("""() => { const b = document.querySelector('#actZone .act-btn').getBoundingClientRect();
                  if (b.bottom > innerHeight - 16) scrollBy(0, b.bottom - innerHeight + 16);
                  else if (b.top < 0) scrollBy(0, b.top - 16); }""")
                bb = pg.locator('#actZone .act-btn').bounding_box()
                pg.mouse.click(bb['x'] + bb['width'] / 2, bb['y'] + bb['height'] / 2)
                pg.wait_for_timeout(2500)
                m = pg.evaluate(PROBE)
                inside = m['actionsInside'] if not m['won'] else m['actionsInWindow']
                if not inside:
                    halts.append(f"F1 {name} tap {i}: action row bottom {m['actBottom']} > feed window {m['feedBottom']}")
                if not m['receipt'] or f"Boost {i}" not in m['receipt'] or not m['receiptVisible']:
                    halts.append(f"F2 {name} tap {i}: no on-screen receipt for this tap (got '{m['receipt'][:60]}')")
                if m['cardTopOff'] > 0 and not m['won']:
                    warns.append(f"W1 {name} tap {i}: top {m['cardTopOff']}px of her newest post is above the screen")
                if not m['verbVisible'] and not m['won']:
                    halts.append(f"F3 {name} tap {i}: Boost is off screen")
                if i == 5:
                    pg.screenshot(path=f"reports/feedback-floor-{name}.png")
                if m['won']:
                    break   # past the win the game scrolls to its reveal on purpose (Play mode P1 rule)
            pg.close()
        b.close()
    print(f"STUDIO FINGERS · FEEDBACK FLOOR  {path}  ({len(VIEWPORTS)} viewports x {TAPS} taps)")
    seen = set()
    for x in halts:
        k = x.split(' tap ')[0]
        if k in seen: continue
        seen.add(k); print("  HALT", x, f"(+{sum(1 for y in halts if y.startswith(k))-1} more)")
    for k in sorted({w.split(' tap ')[0] for w in warns}):
        print("  WARN", next(w for w in warns if w.startswith(k)))
    print("  VERDICT", "HALT" if halts else "PASS")
    return 1 if halts else 0

if __name__ == "__main__":
    sys.exit(run(sys.argv[1] if len(sys.argv) > 1 else "the-console.html"))
