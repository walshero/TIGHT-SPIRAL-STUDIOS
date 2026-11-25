# Xenos v0.13 painted ground: low-frequency paint fields (sea, sand, grass),
# grayscale detail tiles for overlay, inked decal sprites, decal placements,
# foam rings, glint points. Art direction: the 2012-13 Xenos Isle map (painted
# turquoise shallows, deep mottled ocean, gold beaches) and the Pier's cell water.
import json, io, base64, math, random
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFilter

I = '/home/claude/isle/'
D = json.load(open(I + 'isle_world.json'))
W, H = D['W'], D['H']
Q = 3                      # paint fields: 1 px = 3 world px
pw, ph = W // Q, H // Q
rng = np.random.default_rng(7)

def mask(polys, scale, w, h, width=None, closed=True):
    m = Image.new('L', (w, h), 0); g = ImageDraw.Draw(m)
    for p in polys:
        pts = [(x / scale, y / scale) for x, y in p]
        if closed: g.polygon(pts, fill=255)
        else: g.line(pts, fill=255, width=max(1, int(width / scale)), joint='curve')
    return np.array(m) > 127

def noise(w, h, octaves, seed, aniso=1.0):
    r = np.random.default_rng(seed); out = np.zeros((h, w), np.float32); amp = 1; tot = 0
    for o in octaves:
        sw, sh = max(2, int(w / o * aniso)), max(2, int(h / o))
        n = r.standard_normal((sh, sw)).astype(np.float32)
        out += cv2.resize(n, (w, h), interpolation=cv2.INTER_CUBIC) * amp; tot += amp; amp *= .55
    out /= tot; out = (out - out.mean()) / (out.std() + 1e-6); return out

def hexc(s): return np.array([int(s[i:i + 2], 16) for i in (1, 3, 5)], np.float32)
def ramp(t, stops):
    t = np.asarray(t, np.float32); xs = [s[0] for s in stops]; cs = np.stack([hexc(s[1]) for s in stops])
    out = np.zeros(t.shape + (3,), np.float32)
    for c in range(3): out[..., c] = np.interp(t, xs, cs[:, c])
    return out

land = mask(D['land'], Q, pw, ph); grass = mask(D['grass'], Q, pw, ph)
din = cv2.distanceTransform(land.astype(np.uint8), cv2.DIST_L2, 5) * Q          # world px inside land
dout = cv2.distanceTransform((~land).astype(np.uint8), cv2.DIST_L2, 5) * Q      # world px out to sea
dg = cv2.distanceTransform(grass.astype(np.uint8), cv2.DIST_L2, 5) * Q

# ---- sea: painted depth, glowing shallows, mottled deep water ----
n1 = noise(pw, ph, [220, 90, 40], 1); n2 = noise(pw, ph, [400, 160], 2, aniso=.45)
de = dout * np.clip(1 + .3 * n1, .75, 1.35)                                    # ragged reef edge, not an even band
sea = ramp(de, [(0, '#a9f3e3'), (18, '#6fe4d9'), (60, '#38c6cf'), (150, '#1c9fbb'),
                (330, '#137ea6'), (650, '#0e5c88'), (1100, '#0b4370'), (2000, '#0a335c')])
sea *= (1 + .06 * n2[..., None]) ; sea += np.stack([n1 * -3, n1 * 2, n1 * 4], -1)
streak = noise(pw, ph, [60, 25], 3, aniso=.25)                # horizontal brush drag
sea += (streak * 5)[..., None] * (dout > 80)[..., None]

# ---- sand: wet line at the water, warm dry beach, cool shade near turf ----
n3 = noise(pw, ph, [120, 50, 18], 4)
sand = ramp(din + n3 * 6, [(0, '#b98f4f'), (10, '#c9a461'), (26, '#e4c47c'), (60, '#f1d68e'), (400, '#f3dc98')])
sand += np.stack([n3 * 7, n3 * 6, n3 * 3], -1)

# ---- grass: sunlit and shaded patches, darker front lip, lighter back lip ----
n4 = noise(pw, ph, [260, 110, 45], 5); n5 = noise(pw, ph, [70, 30], 6)
g = ramp(n4, [(-2.2, '#2f9a30'), (-.8, '#3fb436'), (0, '#4fc63c'), (.9, '#6bd447'), (2.2, '#9be15a')])
g += np.stack([n5 * 6, n5 * 9, n5 * 2], -1)
gy, gx = np.gradient(cv2.GaussianBlur(dg, (0, 0), 4))
front = np.clip(-gy / (np.hypot(gx, gy) + 1e-3), -1, 1)       # +1 where the edge faces the viewer
rim = np.clip(1 - dg / 34, 0, 1) ** 1.5
g *= (1 - rim[..., None] * (.18 + .16 * np.clip(front, 0, 1)[..., None]))
g += (rim * np.clip(-front, 0, 1) * 26)[..., None] * np.array([.6, 1, .4])

def save_field(a, name):
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)); im.save(I + name + '.png')
    b = io.BytesIO(); im.save(b, 'WEBP', quality=82, method=6); return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()

out = {'Q': Q, 'sea': save_field(sea, 'paint_sea'), 'sand': save_field(sand, 'paint_sand'), 'grass': save_field(g, 'paint_grass')}

# ---- grayscale detail tiles (2x, seamless) for 'overlay' compositing ----
T = 512
def tile_png(a, name):
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), 'L'); im.save(I + name + '.png')
    b = io.BytesIO(); im.save(b, 'WEBP', quality=88, method=6); return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()

def wrapnoise(seed, cells):
    r = np.random.default_rng(seed); n = r.standard_normal((cells, cells)).astype(np.float32)
    n = np.tile(n, (3, 3)); n = cv2.resize(n, (T * 3, T * 3), interpolation=cv2.INTER_CUBIC)[T:2 * T, T:2 * T]
    return (n - n.mean()) / n.std()

# grass: short painted blade strokes, iso-leaning, light tips
S4 = 4; big = Image.new('L', (T * S4, T * S4), 128); d = ImageDraw.Draw(big); R = random.Random(11)
for _ in range(3800):
    x, y = R.uniform(0, T), R.uniform(0, T); L = R.uniform(7, 16); a = math.radians(R.uniform(-115, -65))
    v = int(R.gauss(128, 30)); wdt = R.uniform(1.4, 2.6)
    for ox in (-T, 0, T):
        for oy in (-T, 0, T):
            x0, y0 = x + ox, y + oy; bend = R.uniform(-3, 3)
            pts = [(x0, y0), (x0 + math.cos(a) * L * .5 + bend * .5, y0 + math.sin(a) * L * .5), (x0 + math.cos(a) * L + bend, y0 + math.sin(a) * L)]
            d.line([(p[0] * S4, p[1] * S4) for p in pts], fill=v, width=int(wdt * S4), joint='curve')
gt = np.array(big.resize((T, T), Image.LANCZOS)).astype(np.float32)
gt = 128 + (gt - 128) * .7 + wrapnoise(12, 16) * 9 + wrapnoise(16, 48) * 5
out['dGrass'] = tile_png(gt, 'detail_grass')

# sand: grain, speckle, faint wind ripples
r = np.random.default_rng(13); st = 128 + r.standard_normal((T, T)) * 9 + wrapnoise(14, 32) * 8
yy, xx = np.mgrid[0:T, 0:T]; st += np.sin((yy * 2 + np.sin(xx / T * 2 * math.pi * 3) * 6) / T * 2 * math.pi * 14) * 5
for _ in range(900):
    x, y = r.integers(0, T, 2); rad = r.uniform(.8, 2.2); v = r.choice([-45, -30, 40, 55])
    cv2.circle(st, (int(x), int(y)), int(round(rad)), float(128 + v), -1, cv2.LINE_AA)
out['dSand'] = tile_png(st, 'detail_sand')

# water: the Pier's cell pattern, squashed for iso, bright cell rims
gv = np.stack(np.meshgrid(np.arange(12), np.arange(12)), -1).reshape(-1, 2) * (T / 12); pts = (gv + r.uniform(.15, .85, gv.shape) * (T / 12)) % T; tiled = np.concatenate([pts + [dx, dy] for dx in (-T, 0, T) for dy in (-T, 0, T)])
P = np.stack([xx.ravel(), (yy * 1.0).ravel()], 1).astype(np.float32)
from scipy.spatial import cKDTree
dd, _ = cKDTree(tiled * [1, 1]).query(P * [1, 1], k=2)
edge = (dd[:, 1] - dd[:, 0]).reshape(T, T)
wt = 128 - 26 + np.clip(edge / 14, 0, 1) * 0 + 52 * np.exp(-edge / 2.6) + wrapnoise(15, 8) * 6
wt += (np.clip(edge / 22, 0, 1) * -14)
wt = cv2.resize(wt.astype(np.float32), (T, T))
wq = cv2.resize(wt, (T, T // 2 * 2))  # keep square tile; squash applied in engine transform
out['dWater'] = tile_png(wq, 'detail_water')

# ---- inked decal sprites at 2x (drawn 4x then downsampled) ----
def sprite(w, h, draw):
    S = 4; im = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0)); dr = ImageDraw.Draw(im); draw(dr, S, w, h)
    return im.resize((w, h), Image.LANCZOS)
INK = (40, 98, 36, 255)
def tuft(seed, flowers=None):
    def f(dr, S, w, h):
        R = random.Random(seed); bx = w / 2
        blades = []
        for i in range(R.randint(7, 10)):
            x = bx + R.uniform(-w * .32, w * .32); L = R.uniform(h * .45, h * .9); lean = R.uniform(-.5, .5)
            blades.append((x, L, lean, R.choice([(46, 150, 44), (62, 176, 52), (84, 196, 62), (120, 214, 80)])))
        blades.sort(key=lambda b: -b[1])
        for x, L, lean, col in blades:
            base = h - 3; tip = (x + lean * L * .6, base - L)
            poly = [(x - 3.2, base), (x - 1 + lean * L * .25, base - L * .55), tip, (x + 1 + lean * L * .3, base - L * .5), (x + 3.2, base)]
            pp = [(p[0] * S, p[1] * S) for p in poly]
            dr.polygon(pp, fill=col + (255,), outline=INK); dr.line(pp + [pp[0]], fill=INK, width=int(.9 * S), joint='curve')
        if flowers:
            for k in range(R.randint(3, 5)):
                cx, cy = bx + R.uniform(-w * .3, w * .3), R.uniform(h * .2, h * .55); col = R.choice(flowers)
                for p in range(5):
                    a = p / 5 * 2 * math.pi; px, py = cx + math.cos(a) * 3.4, cy + math.sin(a) * 2.6
                    dr.ellipse([(px - 2.6) * S, (py - 2.2) * S, (px + 2.6) * S, (py + 2.2) * S], fill=col + (255,), outline=(70, 40, 40, 255), width=S)
                dr.ellipse([(cx - 1.7) * S, (cy - 1.4) * S, (cx + 1.7) * S, (cy + 1.4) * S], fill=(245, 196, 40, 255), outline=(90, 60, 20, 255), width=S)
    return f
def stone(seed, w, h):
    def f(dr, S, W_, H_):
        R = random.Random(seed)
        dr.ellipse([3 * S, (H_ * .62) * S, (W_ - 2) * S, (H_ - 1) * S], fill=(40, 60, 30, 70))
        pts = [(W_ / 2 + math.cos(a) * (W_ * .42 + R.uniform(-2, 2)), H_ * .52 + math.sin(a) * (H_ * .36 + R.uniform(-1.5, 1.5))) for a in np.linspace(0, 2 * math.pi, 9)[:-1]]
        dr.polygon([(x * S, y * S) for x, y in pts], fill=(150, 146, 132, 255))
        dr.polygon([(x * S, (y - 1.5) * S) for x, y in pts[4:8] + [pts[0]]], fill=(196, 192, 176, 255))
        dr.line([(x * S, y * S) for x, y in pts + [pts[0]]], fill=(54, 50, 44, 255), width=int(1.4 * S), joint='curve')
    return f
def shell(seed):
    def f(dr, S, w, h):
        R = random.Random(seed); col = R.choice([(246, 222, 206), (240, 196, 186), (250, 238, 214)])
        cx, cy = w / 2, h * .62
        pts = [(cx, cy + 4)] + [(cx + math.cos(a) * 7, cy - 1 + math.sin(a) * 5) for a in np.linspace(math.pi * 1.05, math.pi * 1.95, 7)]
        dr.polygon([(x * S, y * S) for x, y in pts], fill=col + (255,))
        for x, y in pts[1:]: dr.line([(cx * S, (cy + 4) * S), (x * S, y * S)], fill=(150, 110, 90, 255), width=S)
        dr.line([(x * S, y * S) for x, y in pts + [pts[0]]], fill=(110, 80, 60, 255), width=int(1.3 * S), joint='curve')
    return f
SPR = [('tuftA', 34, 26, tuft(1)), ('tuftB', 30, 22, tuft(2)), ('tuftC', 40, 30, tuft(3)),
       ('flowW', 38, 30, tuft(4, [(250, 250, 244), (236, 240, 255)])), ('flowP', 38, 30, tuft(5, [(240, 120, 170), (226, 92, 150)])),
       ('flowY', 38, 30, tuft(6, [(255, 214, 70), (255, 236, 120)])), ('flowV', 38, 30, tuft(7, [(170, 120, 230), (140, 100, 220)])),
       ('stoneA', 22, 16, stone(8, 22, 16)), ('stoneB', 30, 20, stone(9, 30, 20)), ('shellA', 18, 12, shell(10)), ('shellB', 18, 12, shell(11))]
ims = []
for name, w, h, fn in SPR:
    S = 8; im = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0)); dr = ImageDraw.Draw(im); fn(dr, S, w, h)
    ims.append(im.resize((w * 2, h * 2), Image.LANCZOS))
ims = ims + [i.transpose(Image.FLIP_LEFT_RIGHT) for i in ims]; SPR = SPR + [(n + '_m', w, h, f) for n, w, h, f in SPR]
AW = sum(i.width + 2 for i in ims); AH = max(i.height for i in ims); atl = Image.new('RGBA', (AW, AH)); x = 0; meta = []
for (name, w, h, _), im in zip(SPR, ims):
    atl.paste(im, (x, 0)); meta.append([x, 0, im.width, im.height, w, h]); x += im.width + 2
atl.save(I + 'decal_atlas.png'); b = io.BytesIO(); atl.save(b, 'WEBP', quality=92, method=6, lossless=False)
out['decalAtlas'] = 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode(); out['decalMeta'] = meta
out['decalNames'] = [s[0] for s in SPR]

# ---- placement: tufts/flowers/stones on open grass, shells on dry sand, ragged tufts along the turf lip ----
Q2 = 2; w2, h2 = W // Q2, H // Q2
G2 = mask(D['grass'], Q2, w2, h2); L2 = mask(D['land'], Q2, w2, h2)
block = mask(D['roads'], Q2, w2, h2, width=96, closed=False) | mask([z['p'] for z in D['plazas']], Q2, w2, h2)
block |= mask([p['fp'] for p in D['props']], Q2, w2, h2)
block = cv2.dilate(block.astype(np.uint8), np.ones((9, 9), np.uint8)) > 0
inG = cv2.distanceTransform(G2.astype(np.uint8), cv2.DIST_L2, 5) * Q2
inL = cv2.distanceTransform(L2.astype(np.uint8), cv2.DIST_L2, 5) * Q2
dens = noise(w2, h2, [300, 120], 21)
R = random.Random(5); dec = []
def ok(x, y, mind, pts):
    return all((x - a) ** 2 + (y - b) ** 2 > mind * mind for a, b in pts)
grid = {}
def near_ok(x, y, mind):
    gx, gy = int(x // 60), int(y // 60)
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            for a, b in grid.get((gx + i, gy + j), []):
                if (x - a) ** 2 + (y - b) ** 2 < mind * mind: return False
    return True
def add(t, x, y):
    dec.append([t, int(x), int(y)]); grid.setdefault((int(x // 60), int(y // 60)), []).append((x, y))
names = out['decalNames']; T_ = {n: i for i, n in enumerate(names)}
NB = len(names) // 2
def put(t, x, y, sc):
    dec.append([T_[t] + (NB if R.random() < .5 else 0), int(x), int(y), int(sc * 100)])
for _ in range(9000):
    x, y = R.uniform(0, W), R.uniform(0, H); ix, iy = int(x / Q2), int(y / Q2)
    if ix >= w2 or iy >= h2 or block[iy, ix]: continue
    if G2[iy, ix] and inG[iy, ix] > 30:
        if R.random() > .18 + .5 * (dens[iy, ix] > .3) or not near_ok(x, y, 120): continue
        grid.setdefault((int(x // 60), int(y // 60)), []).append((x, y))
        kind = R.random(); n = R.randint(2, 6)
        pool = ['tuftA', 'tuftB', 'tuftC'] if kind < .5 else [R.choice(['flowW', 'flowP', 'flowY', 'flowV'])] * 2 + ['tuftB'] if kind < .85 else ['stoneA', 'stoneB', 'tuftB']
        for k in range(n):
            px, py = x + R.gauss(0, 22), y + R.gauss(0, 12); jx, jy = int(px / Q2), int(py / Q2)
            if not (0 <= jx < w2 and 0 <= jy < h2) or block[jy, jx] or not G2[jy, jx]: continue
            put(R.choice(pool), px, py, R.uniform(.7, 1.25))
    elif L2[iy, ix] and not G2[iy, ix] and 22 < inL[iy, ix] < 120:
        if R.random() > .25 or not near_ok(x, y, 90): continue
        grid.setdefault((int(x // 60), int(y // 60)), []).append((x, y))
        put(R.choice(['shellA', 'shellB', 'stoneA']), x, y, R.uniform(.8, 1.15))
# ragged lip: tufts every ~26 px along the grass outline, a little inside the edge
for poly in D['grass']:
    for (x0, y0), (x1, y1) in zip(poly, poly[1:] + poly[:1]):
        L = math.hypot(x1 - x0, y1 - y0); n = max(1, int(L / 48))
        for k in range(n):
            if R.random() < .45: continue
            t = (k + R.random()) / n; x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
            ix, iy = int(x / Q2), int(y / Q2)
            if 0 <= ix < w2 and 0 <= iy < h2 and block[iy, ix]: continue
            put(R.choice(['tuftA', 'tuftB', 'tuftB']), x + R.uniform(-6, 6), y + R.uniform(3, 10), R.uniform(.55, .95))
dec.sort(key=lambda d: d[2]); out['decals'] = dec

# ---- foam rings: coastline offset outward 14 / 34 / 60 world px ----
Lm = mask(D['land'], Q2, w2, h2).astype(np.uint8) * 255
rings = []
for off in (14, 34, 60):
    k = int(off / Q2) * 2 + 1; dm = cv2.dilate(Lm, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k)))
    cs, _ = cv2.findContours(dm, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE); ring = []
    for c in cs:
        a = cv2.approxPolyDP(c, 1.2, True)[:, 0, :] * Q2
        if len(a) > 8: ring.append(a.astype(int).tolist())
    rings.append(ring)
out['foam'] = rings

# ---- glints: points in the shallows ----
gl = []
while len(gl) < 520:
    x, y = R.uniform(0, W), R.uniform(0, H); ix, iy = int(x / Q), int(y / Q)
    if ix < pw and iy < ph and 30 < dout[iy, ix] < 260: gl.append([int(x), int(y), round(R.uniform(0, 6.28), 2)])
out['glints'] = gl
json.dump(out, open(I + 'paint.json', 'w'), separators=(',', ':'))
print('decals', len(dec), 'rings', [sum(len(r) for r in ring) for ring in rings], 'bytes', len(json.dumps(out)) // 1024, 'KB')
