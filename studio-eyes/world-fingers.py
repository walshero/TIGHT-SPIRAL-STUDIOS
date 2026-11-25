#!/usr/bin/env python3
"""
WORLD FINGERS — Studio Fingers for the canvas (2026-11-25).

Studio Fingers measures DOM buttons. In a walkable world the things a thumb must hit are
drawn on a canvas: kiosks, doors, people, the ground. This gate measures those, on a phone
(390x844 @3x), through the world's test hook.

HOOK CONTRACT. The page, opened with ?debug=1, exposes window.__xen with:
  you{x,y,path}, cam{x,y}, scr(x,y)->[sx,sy] (canvas css px), walkPt(x,y), findPath(a,b),
  walkTo(x,y), OBJS[{fp,front,cx,cy,rx,ry,kind}], SPOTS[{id,p,door}], DIST{id:{x,y,name}}
Xenos v0.9+ ships it. A world without the hook is reported BLIND, never as a pass.

CHECKS (all measured):
  F-KIOSK   every kiosk's tappable art is >= 44 css px on both axes at phone zoom.  [LAW 44px]
  F-CENTER  after every walk the player stands inside the middle 60% of the canvas
            (founder ruling 2026-11-25: keep the player out of the outer 20%).   [FOUNDER]
  F-TAP     40 random taps near the player: a walk must be found for >= 95%.
  F-SOLID   paths between every district and kiosk door never cross a footprint.
  F-DEPTH   12 points ringed round every object: a ring point behind the object's front
            edge must be drawn behind it (geometry check of the depth rule).

Usage: python3 world-fingers.py <world.html> [...]    exit 0 ship, 1 HALT, 2 BLIND
"""
import asyncio, json, os, sys
from playwright.async_api import async_playwright

CHROME = next((p for p in ['/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser'] if os.path.exists(p)), None)

PROBE = r"""async () => {
  const X = window.__xen; if (!X || !X.scr || !X.findPath) return {blind: 'no window.__xen hook (open with ?debug=1)'};
  const out = {kiosk: [], center: [], tap: {n: 0, ok: 0}, solid: {pairs: 0, bad: 0, nopath: []}, depth: []};
  const cv = document.querySelector('canvas'); const W = cv.clientWidth, H = cv.clientHeight;
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const inside = (x, y, f) => { let c = false; for (let i = 0, j = f.length - 1; i < f.length; j = i++) { const [xi, yi] = f[i], [xj, yj] = f[j]; if (((yi > y) !== (yj > y)) && x < (xj - xi) * (y - yi) / (yj - yi) + xi) c = !c } return c };
  // F-KIOSK
  for (const s of (X.SPOTS || [])) { const xs = s.p.map(q => q[0]), ys = s.p.map(q => q[1]);
    const a = X.scr(Math.min(...xs), Math.min(...ys)), b = X.scr(Math.max(...xs), Math.max(...ys));
    out.kiosk.push([s.id, Math.round(b[0] - a[0]), Math.round(b[1] - a[1])]) }
  // F-CENTER: walk to every district, wait until the walk ends and the camera settles
  for (const d of Object.values(X.DIST || {})) { X.walkTo(d.x, d.y); let t = 0;
    while ((X.you.path.length || t < 10) && t < 300) { await sleep(100); t++ } await sleep(1200);
    const [sx, sy] = X.scr(X.you.x, X.you.y); out.center.push([d.name || d.id, +(sx / W).toFixed(2), +(sy / H).toFixed(2)]) }
  // F-TAP
  for (let i = 0; i < 40; i++) { const x = X.you.x + (Math.random() - .5) * 700, y = X.you.y + (Math.random() - .5) * 400;
    if (!X.walkPt(x, y)) continue; out.tap.n++; if (X.findPath([X.you.x, X.you.y], [x, y])) out.tap.ok++ }
  // F-SOLID
  const P = Object.values(X.DIST || {}).map(d => { let p = [d.x, d.y]; for (let r = 0; r < 400 && !X.walkPt(...p); r += 8) p = [d.x, d.y + r]; return [d.id, p] });
  for (const s of (X.SPOTS || [])) P.push([s.id, s.door]);
  for (const [a, pa] of P) for (const [c, pc] of P) { if (a === c) continue; out.solid.pairs++; const path = X.findPath(pa, pc);
    if (!path) { out.solid.nopath.push(a + '>' + c); continue } let prev = pa;
    for (const q of path) { const n = Math.ceil(Math.hypot(q[0] - prev[0], q[1] - prev[1]) / 3);
      for (let i = 1; i <= n; i++) { const x = prev[0] + (q[0] - prev[0]) * i / n, y = prev[1] + (q[1] - prev[1]) * i / n;
        if ((X.OBJS || []).some(o => inside(x, y, o.fp))) { out.solid.bad++; break } } prev = q } }
  // F-DEPTH (geometry): ring points; behind-ness must agree with the front edge; at least one ring point must be behind
  for (const o of (X.OBJS || [])) { if (!o.front) continue; let n = 0, beh = 0;
    for (let k = 0; k < 12; k++) { const a = k / 12 * Math.PI * 2, x = o.cx + Math.cos(a) * (o.rx + 14), y = o.cy + Math.sin(a) * (o.ry + 10);
      if (!X.walkPt(x, y)) continue; n++; const f = o.front; const xx = Math.max(f[0][0], Math.min(f[f.length - 1][0], x)); let fy = f[f.length - 1][1];
      for (let i = 1; i < f.length; i++) if (xx <= f[i][0]) { fy = f[i - 1][1] + (f[i][1] - f[i - 1][1]) * ((xx - f[i - 1][0]) / ((f[i][0] - f[i - 1][0]) || 1)); break }
      if (y < fy) beh++ } out.depth.push([o.kind || o.id, n, beh]) }
  return out }"""

async def run(path):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME) if CHROME else await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 390, 'height': 844}, device_scale_factor=3)
        await pg.goto('file://' + os.path.abspath(path) + '?debug=1'); await pg.wait_for_timeout(2500)
        r = await pg.evaluate(PROBE); await b.close(); return r

def judge(path):
    r = asyncio.run(run(path)); name = os.path.basename(path)
    print(f'\n  WORLD FINGERS  {name}  (390px phone, @3x)')
    if r.get('blind'): print('  BLIND ', r['blind']); return 2
    halts = []
    for k, w, h in r['kiosk']:
        if min(w, h) < 44: halts.append(f'F-KIOSK  "{k}" tappable art {w}x{h} css px < 44 [LAW]')
    for nm, fx, fy in r['center']:
        if not (0.2 <= fx <= 0.8 and 0.2 <= fy <= 0.8): halts.append(f'F-CENTER after walking to {nm}: player at {fx:.0%},{fy:.0%} of the canvas, outside the middle 60% [FOUNDER]')
    t = r['tap']; rate = t['ok'] / max(1, t['n'])
    if t['n'] and rate < 0.95: halts.append(f'F-TAP    only {t["ok"]}/{t["n"]} random taps found a walk')
    s = r['solid']
    if s['bad']: halts.append(f'F-SOLID  {s["bad"]} path samples inside a building footprint')
    if s['nopath']: halts.append(f'F-SOLID  {len(s["nopath"])} unreachable pairs, e.g. {s["nopath"][:3]}')
    for k, n, beh in r['depth']:
        if n >= 4 and beh == 0: halts.append(f'F-DEPTH  "{k}": no ring point ever goes behind it -- front edge is wrong')
    print(f'  kiosks {len(r["kiosk"])}  walks {len(r["center"])}  taps {t["ok"]}/{t["n"]}  routes {s["pairs"]}  objects {len(r["depth"])}')
    for h in halts: print('  HALT ', h)
    print(f'  === {"HALT" if halts else "SHIP"} ===')
    return 1 if halts else 0

if __name__ == '__main__':
    if not sys.argv[1:]: print(__doc__); sys.exit(2)
    sys.exit(max(judge(f) for f in sys.argv[1:]))
