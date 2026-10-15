#!/usr/bin/env python3
"""
STUDIO EYES · TOP FLOOR                                   Tight Spiral Productions
-----------------------------------------------------------------------------
Built 2026-10-15. Founder, on his iPhone, opening Flok v34:

    "Why does it load with empty space at top? That should be a studio wide no-no."

The empty space was the Lab status band. Every lab build carried it above the
Studio/Cabinet bar, and Flok's full-screen .scene-bg (position:fixed; z-index:0)
painted OVER it: a dark strip with its text buried underneath. No gate saw it.
Studio Eyes measured the band's contrast (13.4:1, passing) against its own
background, never against what was stacked on top of it. An occlusion probe that
asks elementFromPoint() is blind too: the overlay is pointer-events:none, and
elementFromPoint skips such layers. This probe turns pointer events back on for
the duration of the look, so a painted-over layer is seen as painted over.

THE FLOORS (first paint, each viewport)
  T1 BURIED TEXT   visible text in the top 140 px whose centre is covered by a   HALT
                   layer that paints (pointer-events forced on during the probe;
                   screen-reader-only text and transparent tap layers excluded).
  T2 DEAD TOP      the first unburied text, image or control starts more than   HALT
                   48 px below the top of the screen: the page opens on nothing.

Usage:
  python3 studio-senses/top-floor.py <page.html> [...]     exit 1 on any HALT
"""
import sys, pathlib
from playwright.sync_api import sync_playwright

VIEWPORTS = [("iphone", 390, 844), ("iphone-se", 375, 667)]
DEAD_TOP = 48
# Retired surfaces, named with the ruling that retired them. Printed as SKIP, never PASS.
RETIRED = {"comfort-control.html": "Comfort Control retired, founder 2026-10-13 (CLAUDE.md, three modes)",
           "confluence-TRUNK.html": "tombstone 2026-09-21, canon moved to tss-playtest"}

PROBE = """(deadTop) => {
  const TOP_BAND = 140;   // the opening band of the screen: what the founder sees first
  const st = document.createElement('style');
  st.textContent = '*,*::before,*::after{pointer-events:auto!important}';
  document.head.appendChild(st);
  const vis = e => { const cs = getComputedStyle(e); const r = e.getBoundingClientRect();
    return r.width > 0 && r.height > 0 && r.bottom > 0 && r.top < innerHeight &&
           cs.visibility !== 'hidden' && cs.display !== 'none' && +cs.opacity > 0.05; };
  const own = e => [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1);
  const buried = [], firsts = [];
  for (const e of document.querySelectorAll('body *')) {
    if (!vis(e)) continue;
    if (e.closest('[aria-hidden="true"]') && !own(e)) continue;
    const isMedia = /^(IMG|SVG|CANVAS|VIDEO)$/i.test(e.tagName) && e.getBoundingClientRect().width > 24;
    const isCtl = e.matches('a[href],button,[role=button],input,select,textarea');
    if (!own(e) && !isMedia && !isCtl) continue;
    const r = e.getBoundingClientRect();
    const x = r.left + Math.min(r.width / 2, 24), y = r.top + Math.min(r.height / 2, 12);
    if (x < 0 || y < 0 || x >= innerWidth || y >= innerHeight) continue;   // only what is on screen
    const h = document.elementFromPoint(x, y);
    // a cover counts only if something between it and the shared ancestor PAINTS: a
    // transparent tap layer over a map label is not burying it.
    const paints = n => { const cs = getComputedStyle(n);
      // a CANVAS is not counted: full-screen canvases here are transparent effect layers
      // (Kireji Pond's ripples); a game drawn on canvas has no DOM text to bury
      return /^(IMG|svg|SVG|VIDEO)$/.test(n.tagName) ||
             (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && cs.backgroundColor !== 'transparent') ||
             cs.backgroundImage !== 'none'; };
    let covered = false;
    if (h && h !== e && !e.contains(h) && !h.contains(e)) {
      for (let n = h; n && !n.contains(e); n = n.parentElement) { if (paints(n)) { covered = true; break; } }
    }
    const srOnly = r.width <= 2 || r.height <= 2 || getComputedStyle(e).clip.startsWith('rect(0');
    if (covered && own(e) && !srOnly && r.top < TOP_BAND) buried.push(((typeof e.className === 'string' && e.className) || e.tagName) + ' "' + e.textContent.trim().slice(0, 40) + '" under ' + (h.className || h.tagName));
    if (!covered) firsts.push(Math.round(r.top));
  }
  st.remove();
  const first = firsts.length ? Math.min(...firsts.filter(t => t >= -2).concat([99999])) : 99999;
  return { buried: buried.slice(0, 6), nBuried: buried.length, first };
}"""

def run(paths):
    halts = skips = 0
    with sync_playwright() as p:
        b = p.chromium.launch()
        for path in paths:
            if pathlib.Path(path).name in RETIRED:
                print(f"SKIP {path}  ({RETIRED[pathlib.Path(path).name]})"); skips += 1; continue
            msgs = []
            for name, w, h in VIEWPORTS:
                pg = b.new_page(viewport={"width": w, "height": h}, is_mobile=True, has_touch=True)
                try:
                    pg.goto(pathlib.Path(path).resolve().as_uri(), timeout=30000); pg.wait_for_timeout(500)
                    m = pg.evaluate(PROBE, DEAD_TOP)
                except Exception as e:
                    msgs.append(f"  HALT {name}: could not open ({str(e)[:60]})"); pg.close(); continue
                pg.close()
                if m['nBuried']:
                    msgs.append(f"  HALT T1 {name}: {m['nBuried']} buried text: " + "; ".join(m['buried'][:2]))
                if m['first'] > DEAD_TOP:
                    msgs.append(f"  HALT T2 {name}: the page opens on {m['first']} px of nothing")
            print(("HALT " if msgs else "PASS ") + path)
            for x in msgs: print(x)
            halts += bool(msgs)
        b.close()
    print(f"TOP FLOOR: {len(paths) - halts - skips} pass, {halts} halt, {skips} retired (skipped)")
    return 1 if halts else 0

if __name__ == "__main__":
    sys.exit(run(sys.argv[1:] or ["the-console.html"]))
