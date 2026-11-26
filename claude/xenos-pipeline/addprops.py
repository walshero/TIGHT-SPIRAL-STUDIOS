# v0.15 prop atlas: repair video-cut sprites, harden and ink every edge, add in-house art.
import json, math
import numpy as np, cv2
from PIL import Image, ImageDraw

I = '/home/claude/isle14/'; ART = '/home/claude/art14/'
P = json.load(open(I + 'props_orig.json'))
INK = (43, 32, 24)

def crop(k):
    v = P[k]; return Image.open(I + 'props_atlas_orig.webp').convert('RGBA').crop((int(v['ax']), int(v['ay']), int(v['ax'] + v['aw']), int(v['ay'] + v['ah'])))

def clean(im, ink=True):
    a = np.array(im).astype(np.float32); al = a[..., 3]
    al = np.clip((al - 90) / 90, 0, 1) * 255                     # harden the feathered video edge
    solid = (al > 250).astype(np.uint8); edge = ((al > 0) & (al <= 250)).astype(np.uint8)
    if edge.any():                                                # defringe: edge pixels take interior colour
        rgb = a[..., :3].astype(np.uint8).copy(); rgb = cv2.inpaint(rgb, edge * 255, 3, cv2.INPAINT_TELEA)
        a[..., :3] = np.where(edge[..., None] > 0, rgb, a[..., :3])
    a[..., 3] = al; out = Image.fromarray(a.astype(np.uint8))
    if not ink: return out
    m = (al > 127).astype(np.uint8) * 255; m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    ring = cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
    ring = cv2.GaussianBlur(ring, (0, 0), .7)
    base = np.zeros(a.shape, np.uint8); base[..., 0], base[..., 1], base[..., 2] = INK; base[..., 3] = (ring * .9).astype(np.uint8)
    b = Image.fromarray(base); b.alpha_composite(out); return b

S = {}
# ---- fish house: the chopped door, keyhole gap and stray string light become a plain side wall ----
im = crop('fishhouse'); d = ImageDraw.Draw(im)
wall = [(568, 420), (712, 392), (712, 588), (568, 648)]
d.polygon(wall, fill=(190, 178, 160, 255));
for i in range(6):
    y0 = 430 + i * 36; d.line([(572, y0), (708, y0 - 28)], fill=(170, 158, 140, 255), width=2)
d.line([(568, 420), (568, 648)], fill=INK + (255,), width=3); d.line([(568, 648), (712, 588)], fill=INK + (255,), width=3); d.line([(712, 392), (712, 588)], fill=INK + (255,), width=3)
a_ = np.array(im); a_[380:, 715:, 3] = 0; S['fishhouse'] = clean(Image.fromarray(a_))
# ---- crates: lift the grey tarp and the ground scraps left from the video ----
im = crop('crates'); a = np.array(im); hsv = cv2.cvtColor(a[..., :3], cv2.COLOR_RGB2HSV)
for (x0, y0, x1, y1) in [(0, 95, 36, 160), (285, 120, 352, 245), (185, 0, 320, 170)]:
    sub = hsv[y0:y1, x0:x1]; kill = sub[..., 1] < 72; a[y0:y1, x0:x1, 3][kill] = 0
S['crates'] = clean(Image.fromarray(a))
# ---- Triangulate ruin (was Glyphs): carved triangles replace the word; ragged top instead of a straight cut ----
im = crop('glyphs'); a = np.array(im)
x0, y0, x1, y1 = 195, 95, 402, 210; sub = a[y0:y1, x0:x1, :3].astype(np.int16); g = sub.mean(-1)
med = cv2.medianBlur(g.astype(np.uint8), 21).astype(np.int16); mask = ((med - g) > 22).astype(np.uint8) * 255
mask = cv2.dilate(mask, np.ones((5, 5), np.uint8)); rgb = a[..., :3].copy()
rgb[y0:y1, x0:x1] = cv2.inpaint(np.ascontiguousarray(rgb[y0:y1, x0:x1]), mask, 6, cv2.INPAINT_TELEA); a[..., :3] = rgb
H, W = a.shape[:2]; xs = np.arange(W)
top = (8 + 6 * np.sin(xs / 23.0) + 4 * np.sin(xs / 7.3 + 1)).astype(int)
for x in range(W): a[:max(0, top[x]), x, 3] = 0
im = Image.fromarray(a); d = ImageDraw.Draw(im)
# lintel face runs from about (150,172) to (395,122): carve five alternating triangles along it
for k in range(5):
    t = (k + .5) / 5; cx = 165 + t * 215; cy = 168 - t * 46; up = k % 2 == 0; s = 15
    pts = [(cx - s, cy + s * .55), (cx + s, cy + s * .55 - 6), (cx + 1, cy - s * .7 - 3)] if up else [(cx - s, cy - s * .5), (cx + s, cy - s * .5 - 6), (cx - 1, cy + s * .75 - 3)]
    d.polygon(pts, fill=(118, 108, 94, 255)); d.line(pts + [pts[0]], fill=(72, 62, 52, 255), width=3)
    lo = sorted(pts, key=lambda p: -p[1])[:2]; d.line(lo, fill=(226, 218, 200, 255), width=2)
S['glyphs'] = clean(im)
for k in ['pagoda', 'cartM', 'aquarium', 'iowcart', 'emptyH', 'clock', 'planter', 'news', 'train']:
    S[k] = clean(crop(k))
# ---- in-house art (already crisp; light hardening only, no extra ink) ----
M = json.load(open(ART + 'meta.json'))
for k in M: S[k] = clean(Image.open(ART + k + '.png').convert('RGBA'), ink=False)

# ---- pack (shelf) ----
order = sorted(S, key=lambda k: -S[k].height); AW = 2048; x = y = sh = 0; pos = {}
for k in order:
    w, h = S[k].size
    if x + w > AW: x = 0; y += sh + 4; sh = 0
    pos[k] = (x, y); x += w + 4; sh = max(sh, h)
atl = Image.new('RGBA', (AW, y + sh + 4))
for k, (px, py) in pos.items(): atl.paste(S[k], (px, py))
atl.save(I + 'props_atlas.webp', 'WEBP', quality=88, method=6); atl.save('/tmp/atlas15.png')
NP = {}
pad = 2  # ink ring grows each video sprite by 2 atlas px on every side? no: same size canvas, ring stays inside the crop
for k, (px, py) in pos.items():
    w, h = S[k].size
    if k in P: v = dict(P[k]); v.update(ax=px, ay=py, aw=w, ah=h)
    else:
        m = M[k]; v = dict(ax=px, ay=py, aw=w, ah=h, w=m['w'], h=m['h'], fp=m['fp'], src=[0, 0])
    NP[k] = v
# new props take the old prop's src so place.py's cluster maths still lands them in the same spot
def fpc(fp): return (sum(p[0] for p in fp) / len(fp), sum(p[1] for p in fp) / len(fp))
for new, old in [('maildrop', 'board'), ('loteria', 'treeS'), ('treeX1', 'treeS'), ('treeX2', 'treeS'), ('lampX', 'lampM1')]:
    o = P[old]; oc = fpc(o['fp']); nc = fpc(NP[new]['fp']); NP[new]['src'] = [o['src'][0] + oc[0] - nc[0], o['src'][1] + oc[1] - nc[1]]
json.dump(NP, open(I + 'props.json', 'w'))
print('atlas', atl.size, 'props', len(NP))
