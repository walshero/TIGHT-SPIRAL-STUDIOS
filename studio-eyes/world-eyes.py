#!/usr/bin/env python3
"""
WORLD EYES — Studio Eyes for the canvas (2026-11-25).

Why it exists. Studio Eyes reads the DOM: buttons, text, contrast. Xenos v0.8 drew its
whole island on a <canvas>, and the founder rejected it as "blurry and glitchy ... seams
are noticeable". Studio Eyes and Studio Fingers both passed it, because neither looks
inside a canvas. A gate that passes a build the founder rejected is a broken gate.

What it does. Renders the world on desktop (1280x800 @2x) and phone (390x844 @3x), at the
spawn view and after walking to each place in the Places menu (the same buttons a player
uses, so it needs no hook). On each canvas screenshot it MEASURES:

  W-SMEAR   share of land tiles (32 css px) with large colour shifts but no fine detail:
            the smeared fog left by blending or inpainting pasted plates. Water tiles are
            skipped (sea gradients are meant to be smooth). HALT if the mean across views
            exceeds SMEAR_MEAN or any one view exceeds SMEAR_VIEW.
            Calibrated 2026-11-25: founder-rejected Xenos v0.8 mean 7.8% (max 14.8%);
            Xenos v0.11 mean 2.4% (max 3.3%). Edge-width blur measures were tried first and
            could NOT separate the two builds (both 2.5 css px); they were dropped, not tuned.
  W-SEAM    long straight horizontal/vertical breaks (>= 35% of the canvas) -- the
            signature of pasted rectangular plates. Iso art has almost none.  HALT if any.
  W-EMPTY   share of 32px tiles with nothing in them (flat colour, no edges). Reported,
            WARN above EMPTY_WARN. A density floor is a taste number; it is not armed
            until the founder rates a few builds against it.

Teeth. --self-test runs every founder-rejected build listed in
studio-eyes/founder-rejections.json and FAILS if World Eyes passes any of them.
Every new founder rejection of a world build becomes a fixture there.

Usage:  python3 world-eyes.py <world.html> [...]     exit 0 ship, 1 HALT, 2 tool broken, 3 self-test BLIND
        Fixtures are full builds; public-repo rule: they live in Drive Claude_files and are mounted locally, never committed.
        python3 world-eyes.py --self-test
"""
import asyncio, json, os, sys, hashlib, statistics
import numpy as np, cv2
from playwright.async_api import async_playwright

SMEAR_MEAN = 0.05   # mean share of smeared land tiles across views
SMEAR_VIEW = 0.10   # worst single view
SEAM_FRAC = 0.35    # line length as share of canvas side
EMPTY_WARN = 0.55   # share of empty tiles in a view
HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = next((p for p in ['/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser'] if os.path.exists(p)), None)

def smear(img, dsf):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB).astype(np.float32); hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    water = (hsv[..., 0] >= 78) & (hsv[..., 0] <= 112) & (hsv[..., 1] > 50)
    L = lab[..., 0]; lo = cv2.GaussianBlur(lab, (0, 0), 4 * dsf); hf = np.abs(L - cv2.GaussianBlur(L, (0, 0), 1.0 * dsf))
    t = int(32 * dsf); H, W = L.shape; n = s = 0
    for y in range(0, H - t + 1, t):
        for x in range(0, W - t + 1, t):
            if water[y:y + t, x:x + t].mean() > 0.3: continue
            n += 1
            if lo[y:y + t, x:x + t].reshape(-1, 3).std(0).max() > 9 and hf[y:y + t, x:x + t].mean() < 1.6: s += 1
    return s / max(n, 1)

def edge_width(g, dsf):
    e = cv2.Canny(g.astype(np.uint8), 60, 150)
    ys, xs = np.nonzero(e[:, 2:-2]); xs = xs + 2
    if len(ys) == 0: return 0.0
    idx = np.random.default_rng(0).choice(len(ys), min(4000, len(ys)), replace=False)
    w = []; H, W = g.shape
    for y, x in zip(ys[idx], xs[idx]):
        s = np.sign(g[y, x + 1] - g[y, x - 1])
        if s == 0: continue
        r = 0
        while x + r + 1 < W - 1 and (g[y, x + r + 1] - g[y, x + r]) * s > 0 and r < 30: r += 1
        l = 0
        while x - l - 1 > 0 and (g[y, x - l] - g[y, x - l - 1]) * s > 0 and l < 30: l += 1
        if 0 < r + l < 30: w.append(r + l)
    return (statistics.median(w) / dsf) if w else 0.0

def seams(g):
    H, W = g.shape
    e = cv2.Canny(g.astype(np.uint8), 40, 120)
    out = []
    for horiz in (True, False):
        L = int((W if horiz else H) * SEAM_FRAC)
        lines = cv2.HoughLinesP(e, 1, np.pi / 360, threshold=int(L * 0.8), minLineLength=L, maxLineGap=3)
        for l in (lines.reshape(-1, 4) if lines is not None else []):
            x1, y1, x2, y2 = l; ang = abs(np.degrees(np.arctan2(y2 - y1, x2 - x1))) % 180
            if (horiz and (ang < 1.5 or ang > 178.5)) or (not horiz and abs(ang - 90) < 1.5):
                out.append((int(x1), int(y1), int(x2), int(y2)))
    return out

def emptiness(g, dsf):
    t = int(32 * dsf); H, W = g.shape; e = cv2.Canny(g.astype(np.uint8), 40, 120) > 0
    n = em = 0
    for y in range(0, H - t + 1, t):
        for x in range(0, W - t + 1, t):
            n += 1
            if g[y:y + t, x:x + t].std() < 9 and e[y:y + t, x:x + t].mean() < 0.012: em += 1
    return em / max(1, n)

# Measure the world, not the UI laid over it: every sibling of the canvas (popups, prompts, panels)
# is hidden for the instant of the screenshot. Found 2026-11-25: an entry button's straight edges
# read as W-SEAM. Hiding by sibling, not by a name list, so a new overlay can't slip in.
HIDE = "(()=>{const c=document.querySelector('canvas');if(!c)return;window.__we=[];for(const e of c.parentElement.children){if(e!==c){window.__we.push([e,e.style.visibility]);e.style.visibility='hidden'}}})()"
SHOW = "(()=>{for(const [e,v] of (window.__we||[]))e.style.visibility=v;window.__we=[]})()"
async def snap(pg, cv, fn):
    await pg.evaluate(HIDE); await cv.screenshot(path=fn); await pg.evaluate(SHOW)

async def shoot(path, outdir):
    shots = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME) if CHROME else await p.chromium.launch()
        for name, vp, dsf in [('desk', {'width': 1280, 'height': 800}, 2), ('phone', {'width': 390, 'height': 844}, 3)]:
            pg = await b.new_page(viewport=vp, device_scale_factor=dsf)
            await pg.goto('file://' + os.path.abspath(path)); await pg.wait_for_timeout(2500)
            cv = pg.locator('canvas').first
            fn = f'{outdir}/{name}_00_spawn.png'; await snap(pg, cv, fn); shots.append((fn, dsf, name, 'spawn'))
            names = []
            try:
                await pg.click('#bPlaces'); await pg.wait_for_timeout(300)
                names = [t.strip() for t in await pg.locator('#placeList button').all_inner_texts()]
                await pg.click('#bPlaces')
            except Exception: names = []
            for i, nm in enumerate(names[:6]):
                try:
                    await pg.click('#bPlaces'); await pg.wait_for_timeout(250)
                    await pg.locator('#placeList button').nth(i).click(); await pg.wait_for_timeout(15000)
                    fn = f'{outdir}/{name}_{i+1:02d}.png'; await snap(pg, cv, fn); shots.append((fn, dsf, name, nm))
                except Exception as ex:
                    shots.append((None, dsf, name, f'{nm}: could not walk ({ex.__class__.__name__})'))
            await pg.close()
        await b.close()
    return shots

def judge(path, quiet=False):
    outdir = f'/tmp/world-eyes/{os.path.basename(path)}'; os.makedirs(outdir, exist_ok=True)
    shots = asyncio.run(shoot(path, outdir))
    halts, warns, rows = [], [], []
    for fn, dsf, dev, where in shots:
        if fn is None: warns.append(f'{dev}: {where}'); continue
        img = cv2.imread(fn); g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
        bw, sm, em = smear(img, dsf), seams(g), emptiness(g, dsf)
        rows.append((dev, where, bw, len(sm), em))
        if bw > SMEAR_VIEW: halts.append(f'W-SMEAR {dev} {where}: {bw:.1%} of land is smeared > {SMEAR_VIEW:.0%}')
        if sm: halts.append(f'W-SEAM  {dev} {where}: {len(sm)} long straight break(s), e.g. {sm[0]}')
        if em > EMPTY_WARN: warns.append(f'W-EMPTY {dev} {where}: {em:.0%} of the view is empty ground')
    mean = float(np.mean([r[2] for r in rows])) if rows else 0.0
    if mean > SMEAR_MEAN: halts.insert(0, f'W-SMEAR mean {mean:.1%} of land smeared across {len(rows)} views > {SMEAR_MEAN:.0%}')
    if not quiet:
        print(f'\n  WORLD EYES  {os.path.basename(path)}')
        print('  view                          smear  seams  empty')
        for dev, where, bw, ns, em in rows: print(f'  {dev:5} {where[:22]:22}  {bw:6.1%}  {ns:5}  {em:5.0%}')
        for h in halts: print('  HALT ', h)
        for w in warns: print('  warn ', w)
        print(f'  === {"HALT" if halts else "SHIP"} ===  shots in {outdir}')
    return (1 if halts else 0), rows

def self_test():
    reg = json.load(open(os.path.join(HERE, 'founder-rejections.json')))
    bad = blind = 0
    for r in reg['rejections']:
        if 'world-eyes' not in r['must_fail']: continue
        f = os.path.join(HERE, r['fixture'])
        if not os.path.exists(f): print(f'  BLIND  fixture not mounted: {f} (Drive {r.get("drive_id","?")}). Not a pass.'); blind += 1; continue
        if hashlib.sha256(open(f, 'rb').read()).hexdigest() != r['sha256']: print('  BROKEN fixture hash changed', f); bad += 1; continue
        code, _ = judge(f, quiet=True)
        print(f'  [{"PASS" if code == 1 else "FAIL"}] founder-rejected {r["fixture"]} ("{r["verdict"][:60]}") -> {"HALT" if code else "SHIP"}')
        if code != 1: bad += 1
    print('  self-test:', f'{bad} BROKEN -- World Eyes passes a build the founder rejected' if bad else (f'{blind} fixture(s) BLIND -- teeth NOT verified' if blind else 'teeth verified'))
    return 2 if bad else (3 if blind else 0)

if __name__ == '__main__':
    if not sys.argv[1:]: print(__doc__); sys.exit(2)
    if sys.argv[1] == '--self-test': sys.exit(self_test())
    worst = 0
    for f in sys.argv[1:]: worst = max(worst, judge(f)[0])
    sys.exit(worst)
