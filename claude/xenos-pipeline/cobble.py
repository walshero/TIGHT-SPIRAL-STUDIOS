# v0.18 cobblestone, in the 2013 Market's style: iso square stones, ochre-tan with pink and sage strays,
# dark grout, bevels lit from the upper left, cracks, moss in the joints. Seamless; drawn at 2x.
import numpy as np, cv2, io, base64, json
from PIL import Image
TW, TH = 480, 504            # world px; lattice periods (60, 25.2) divide both
S = 2; W, H = TW * S, TH * S
rng = np.random.default_rng(18)
def pnoise(w, h, cutoff, seed):           # periodic low-pass noise via FFT
    r = np.random.default_rng(seed); n = r.standard_normal((h, w))
    F = np.fft.fft2(n); fy = np.fft.fftfreq(h)[:, None]; fx = np.fft.fftfreq(w)[None, :]
    F *= np.exp(-(fx ** 2 + fy ** 2) / (2 * cutoff ** 2)); o = np.real(np.fft.ifft2(F)); return (o - o.mean()) / o.std()
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32) / S
dx = pnoise(W, H, .02, 1) * .9 + pnoise(W, H, .004, 11) * 1.6; dy = pnoise(W, H, .02, 2) * .4   # wobble so stones are not ruled
X = xx + dx; Y = yy + dy
a = X / 60 + Y / 25.2; b = X / 60 - Y / 25.2
ia, ib = np.floor(a), np.floor(b); fa, fb = a - ia, b - ib
cxw = (30 * (ia + ib + 1)) % TW; cyw = (12.6 * (ia - ib)) % TH       # stone centre, wrapped: periodic identity
h = (np.sin(cxw * 12.9898 + cyw * 78.233) * 43758.5453) % 1.0
h2 = (np.sin(cxw * 39.3468 + cyw * 11.135) * 24634.6345) % 1.0
pal = np.array([[0x97,0x7e,0x46],[0xa1,0x87,0x4f],[0x8c,0x74,0x3d],[0x7e,0x69,0x34],[0xa8,0x94,0x5b],[0xb0,0x8a,0x66],[0x8f,0x92,0x66],[0xb5,0x9c,0x6a]],np.float32)
wts = np.array([.18,.17,.15,.11,.13,.09,.07,.10]); cum = np.cumsum(wts) / wts.sum()
idx = np.searchsorted(cum, h); base = pal[np.clip(idx, 0, 7)]
base *= (0.9 + 0.2 * h2)[..., None]
# within-stone painting: bevel light from upper left, darker lower right, soft mottling
e = np.minimum(np.minimum(fa, 1 - fa), np.minimum(fb, 1 - fb))
lit = (1 - fa) * .5 + fb * .5          # toward the upper-left edges
shade = 1 + .16 * (lit - .5) + .10 * np.clip((.16 - e) / .16, 0, 1) * np.sign(lit - .5)
hl = np.clip(1 - np.abs(np.minimum(1 - fa, fb) - .09) / .03, 0, 1) * .12; sh = np.clip(1 - np.abs(np.minimum(fa, 1 - fb) - .09) / .03, 0, 1) * .12
shade = shade + hl - sh
mott = pnoise(W, H, .06, 3); col = base * (shade + .05 * mott)[..., None]
# grout
g = np.clip((.055 - e) / .035, 0, 1)
grout = np.array([0x55, 0x45, 0x1c], np.float32); col = col * (1 - g[..., None]) + grout * g[..., None]
# moss: low-frequency patches, strongest in the joints
moss = np.clip(pnoise(W, H, .004, 4) * .9 + .1, 0, 1); mj = moss * np.clip((.16 - e) / .12, 0, 1)
mosscol = np.array([0x5c, 0x62, 0x2a], np.float32)
col = col * (1 - .55 * mj[..., None]) + mosscol * .55 * mj[..., None]
col = col * (1 - .10 * moss[..., None]) + mosscol * .10 * moss[..., None]
# stains
st = np.clip(pnoise(W, H, .008, 5), 0, None); col *= (1 - .10 * st)[..., None]
out = np.clip(col, 0, 255).astype(np.uint8)
# cracks on a few stones
r = np.random.default_rng(9); img = out.copy()
for _ in range(26):
    x0, y0 = r.uniform(0, W), r.uniform(0, H); L = r.uniform(5, 11) * S; ang = r.uniform(0, np.pi)
    pts = [(x0, y0)]
    for k in range(3): x0 += np.cos(ang) * L / 3 + r.normal(0, 2); y0 += np.sin(ang) * L / 3 * .5 + r.normal(0, 2); pts.append((x0, y0))
    for ox in (-W, 0, W):
        for oy in (-H, 0, H):
            p = np.array([(px + ox, py + oy) for px, py in pts], np.int32)
            cv2.polylines(img, [p], False, (78, 62, 32), 2, cv2.LINE_AA)
Image.fromarray(img).save('/home/claude/isle14/tex_cobble2.png')
b = io.BytesIO(); Image.fromarray(img).save(b, 'WEBP', quality=86, method=6)
json.dump({'w': TW, 'h': TH, 'png': 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()}, open('/home/claude/isle14/cobble.json', 'w'))
print(W, H, len(b.getvalue()) // 1024, 'KB')
