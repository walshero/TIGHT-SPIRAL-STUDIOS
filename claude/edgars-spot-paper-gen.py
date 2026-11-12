#!/usr/bin/env python3
"""Generator for lab/edgars-spot-paper.html (Edgar's Spot: Paper Look).

Founder 2026-11-12: Edgar's Spot "graphics never make me want to stay with it"; chose the
paper direction: the high-top at eye level as a cut-paper miniature at dusk (Lumino City
bar). This script draws every shape with hand-cut edges: straight runs are subdivided and
each vertex is nudged by a seeded jitter, so no edge is machine-straight, and the same
seed always yields the same file. Run: python3 claude/edgars-spot-paper-gen.py
"""
import math, random

R = random.Random(1972)

def cut(pts, amp=1.2, step=10, closed=True):
    """Subdivide a polyline into ~step-px runs and jitter each vertex: a scissor edge."""
    out = []
    n = len(pts)
    segs = n if closed else n - 1
    for i in range(segs):
        x1, y1 = pts[i]; x2, y2 = pts[(i + 1) % n]
        L = math.hypot(x2 - x1, y2 - y1); k = max(1, int(L / step))
        for j in range(k):
            t = j / k
            out.append((x1 + (x2 - x1) * t + R.uniform(-amp, amp), y1 + (y2 - y1) * t + R.uniform(-amp, amp)))
    if not closed:
        out.append(pts[-1])
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in out) + (" Z" if closed else "")

def ell(cx, cy, rx, ry, amp=0.9, n=56):
    pts = [(cx + rx * math.cos(2 * math.pi * i / n), cy + ry * math.sin(2 * math.pi * i / n)) for i in range(n)]
    return cut(pts, amp, step=999)

def rect(x, y, w, h, amp=1.0):
    return cut([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], amp)

def P(d, fill, extra=""):
    return f'<path d="{d}" fill="{fill}"{extra}/>'

S = []  # scene layers, back to front
# ---- 1. dusk sky inside the window (window opening 40..196 x 70..300)
sky = [("#3E3566", 70), ("#6A4377", 118), ("#A2557A", 160), ("#E07A6A", 205), ("#F6B98A", 250)]
g = []
for col, y in sky:
    g.append(P(cut([(36, y), (200, y - 4), (200, 304), (36, 304)], 1.6, 12), col))
g.append(P(ell(160, 236, 15, 15, 0.6), "#FFE3B0"))  # low sun, half behind the roofs
# far roofs then near roofs
far = [(36, 262), (58, 262), (58, 244), (80, 244), (80, 256), (104, 256), (104, 236), (122, 236), (122, 226), (132, 226),
       (132, 250), (156, 250), (156, 240), (178, 240), (178, 254), (200, 254), (200, 304), (36, 304)]
g.append(P(cut(far, 0.9, 8), "#5A3F66"))
near = [(36, 276), (70, 276), (70, 258), (96, 258), (96, 272), (118, 272), (118, 250), (148, 250), (148, 268), (174, 268),
        (174, 262), (200, 262), (200, 304), (36, 304)]
g.append(P(cut(near, 0.9, 8), "#2E2846"))
wins = [(78, 262), (86, 262), (124, 256), (132, 256), (124, 264), (154, 274), (182, 270), (104, 278), (46, 282)]
for i, (x, y) in enumerate(wins):
    g.append(f'<rect class="citywin" data-i="{i}" x="{x}" y="{y}" width="5" height="6" fill="#FFD98A" opacity="0"/>')
S.append(('sky', "".join(g), 0))

# ---- 2. the red wall with the window cut out, wainscot, trim
wall = ("M0 0 H400 V430 H0 Z M40 70 L196 66 L198 302 L38 304 Z")
g = [f'<path d="{wall}" fill="#B5121B" fill-rule="evenodd"/>']
g.append(P(cut([(0, 330), (400, 326), (400, 430), (0, 430)], 1.2, 12), "#8E0E16"))
g.append(P(cut([(0, 322), (400, 318), (400, 332), (0, 336)], 1.0, 12), "#E23A2E"))
# window frame: four cream strips and a muntin cross
for d in [rect(30, 58, 178, 12), rect(30, 300, 178, 14), rect(30, 58, 12, 256), rect(196, 58, 12, 256),
          rect(113, 66, 7, 236), rect(40, 182, 158, 7)]:
    g.append(P(d, "#F3E6CF"))
S.append(('wall', "".join(g), 4))

# ---- 3. the back bar on the right: shelf, bottles, counter
g = [P(rect(250, 150, 150, 10), "#7A4A35"), P(rect(250, 222, 150, 10), "#7A4A35")]
bottles = [(262, "#2F5D4A", 46), (282, "#C77A2A", 38), (300, "#CFE6EE", 42), (318, "#5A0A1E", 48), (338, "#2F5D4A", 40),
           (356, "#C77A2A", 44), (376, "#CFE6EE", 36)]
for x, col, h in bottles:
    g.append(P(cut([(x, 150), (x + 13, 150), (x + 13, 150 - h + 16), (x + 9, 150 - h + 8), (x + 9, 150 - h),
                    (x + 4, 150 - h), (x + 4, 150 - h + 8), (x, 150 - h + 16)], 0.6, 6), col))
for x, col in [(264, "#E8D8BC"), (290, "#E8D8BC"), (318, "#F3E6CF"), (346, "#E8D8BC"), (372, "#F3E6CF")]:
    g.append(P(cut([(x, 222), (x + 18, 222), (x + 15, 200), (x + 3, 200)], 0.6, 6), col))
g.append(P(cut([(236, 300), (400, 296), (400, 430), (236, 430)], 1.2, 12), "#6E4533"))
g.append(P(cut([(230, 292), (400, 288), (400, 304), (230, 306)], 1.0, 12), "#8C5842"))
S.append(('bar', "".join(g), 5))

# ---- 4. floor
g = [P(cut([(0, 430), (400, 426), (400, 560), (0, 560)], 1.2, 14), "#5E3A2B")]
for y in (452, 482, 518):
    g.append(P(cut([(0, y), (400, y - 3), (400, y - 1), (0, y + 2)], 0.6, 16), "#6E4533"))
S.append(('floor', "".join(g), 0))

# ---- 5. the lamp's pool of light on the wall and table (atmosphere, not text)
S.append(('glow', '<ellipse cx="190" cy="350" rx="150" ry="120" fill="url(#pool)"/>'
                  '<path d="M174 150 L206 150 L268 392 L112 392 Z" fill="url(#cone)"/>', 0))

# ---- 6. the high-top: pedestal, base, top, edge band, plaque; the stool
g = [P(cut([(183, 392), (197, 392), (199, 508), (181, 508)], 0.7, 8), "#4A2E22"),
     P(ell(190, 512, 52, 12, 0.8), "#3B241B"),
     P(ell(190, 380, 104, 30, 1.0), "#5E3A2B"),
     P(ell(190, 372, 104, 30, 1.0), "#8C5842"),
     P(ell(190, 370, 90, 22, 0.8), "#9A6550")]
g.append(f'<g id="plaque">{P(cut([(170, 398), (210, 398), (210, 408), (170, 408)], 0.4, 6), "#C9A24A")}'
         f'{P(cut([(175, 402.5), (205, 402.5), (205, 404), (175, 404)], 0.2, 8), "#7A5A1A")}</g>')
g.append('<rect id="glint" x="170" y="398" width="40" height="10" fill="#FFF3B0" opacity="0"/>')
S.append(('table', "".join(g), 6))
g = [P(ell(330, 456, 30, 9, 0.7), "#3B241B"),
     P(cut([(310, 456), (316, 456), (320, 540), (312, 540)], 0.5, 8), "#3B241B"),
     P(cut([(344, 456), (350, 456), (348, 540), (340, 540)], 0.5, 8), "#3B241B"),
     P(ell(330, 450, 30, 9, 0.7), "#6E4533")]
S.append(('stool', "".join(g), 6))

# ---- 7. on the table: water glass, napkin (the bread plate arrives in the hand)
g = [P(cut([(138, 330), (156, 330), (154, 366), (140, 366)], 0.5, 6), "#CFE6EE"),
     P(cut([(142, 334), (146, 334), (145, 360), (142, 360)], 0.3, 6), "#FFFFFF", ' opacity=".75"'),
     P(cut([(214, 366), (250, 362), (254, 374), (218, 378)], 0.6, 6), "#F3EEE6"),
     P(cut([(216, 371), (252, 367), (252, 368.6), (216, 372.6)], 0.2, 8), "#D7CFC2")]
S.append(('tabletop', "".join(g), 3))

# ---- 8. the pendant lamp (sways from its cord top at 190,0)
lamp = (P(cut([(189, 0), (191, 0), (191, 118), (189, 118)], 0.2, 20), "#2B2422") +
        P(cut([(160, 150), (220, 150), (204, 116), (176, 116)], 0.7, 6), "#2B2422") +
        P(ell(190, 150, 30, 6, 0.4), "#FFD98A") +
        P(ell(190, 151, 10, 4, 0.3), "#FFF3B0"))
S.append(('lamp', f'<g id="lamp">{lamp}</g>', 5))

# ---- 9. steam over the bread (drawn later in the hand group) and the server's hand
steam = "".join(f'<path class="steam" data-i="{i}" d="M{x} 352 c-6 -10 6 -18 0 -28 c-6 -10 6 -18 0 -28" '
                f'fill="none" stroke="#FBF3E4" stroke-width="3" stroke-linecap="round" opacity="0"/>'
                for i, x in enumerate((182, 192, 202)))
plate = (P(ell(192, 360, 30, 8, 0.6), "#C9C2B6") + P(ell(192, 357, 30, 8, 0.6), "#FDFCF9") +
         P(ell(184, 352, 11, 6, 0.6), "#E0C1A3") + P(ell(198, 353, 10, 5.5, 0.6), "#D2AC86") +
         P(cut([(178, 351), (186, 349), (187, 350.5), (179, 352.5)], 0.2, 6), "#B98A62"))
hand = (P(cut([(214, 352), (400, 330), (400, 372), (220, 380)], 1.0, 10), "#2B2422") +    # black sleeve
        P(cut([(206, 352), (226, 350), (230, 378), (210, 381)], 0.6, 6), "#F3EEE6") +      # shirt cuff
        P(cut([(182, 358), (206, 352), (212, 380), (196, 386), (180, 374), (172, 366)], 0.8, 5), "#E0C1A3") +  # palm under plate
        P(cut([(176, 362), (160, 356), (158, 360), (174, 368)], 0.5, 4), "#D2AC86"))       # thumb over the rim
S.append(('hand', f'<g id="plateIn">{plate}</g>{steam}<g id="hand">{hand}</g>', 4))

# Composition: the table group comes forward (scaled up, nudged right and down) and the lamp
# moves with it, so the shade clears the window frame and the table fills the lower frame.
FWD = "translate(232 392) scale(1.18) translate(-190 -372)"
MOVE = {"table": FWD, "tabletop": FWD, "hand": FWD, "glow": "translate(54 6)", "lamp": "translate(54 0)",
        "stool": "translate(40 6)"}
layers = []
for name, body, depth in S:
    filt = f' filter="url(#d{depth})"' if depth else ""
    tr = f' transform="{MOVE[name]}"' if name in MOVE else ""
    inner = f'<g data-layer="{name}"{filt}>{body}</g>'
    layers.append(f'<g{tr}>{inner}</g>' if tr else inner)

defs = """<defs>
  <filter id="d3" x="-10%" y="-10%" width="130%" height="140%"><feDropShadow dx="2" dy="3" stdDeviation="1.4" flood-color="#1A0606" flood-opacity=".45"/></filter>
  <filter id="d4" x="-10%" y="-10%" width="130%" height="140%"><feDropShadow dx="3" dy="4" stdDeviation="2" flood-color="#1A0606" flood-opacity=".5"/></filter>
  <filter id="d5" x="-10%" y="-10%" width="130%" height="140%"><feDropShadow dx="4" dy="6" stdDeviation="2.6" flood-color="#1A0606" flood-opacity=".5"/></filter>
  <filter id="d6" x="-10%" y="-10%" width="130%" height="140%"><feDropShadow dx="5" dy="8" stdDeviation="3" flood-color="#1A0606" flood-opacity=".55"/></filter>
  <filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="7"/><feColorMatrix values="0 0 0 0 .35  0 0 0 0 .25  0 0 0 0 .18  0 0 0 .55 0"/></filter>
  <radialGradient id="pool" cx=".5" cy=".42" r=".5"><stop offset="0" stop-color="#FFD98A" stop-opacity=".42"/><stop offset=".6" stop-color="#FFB85A" stop-opacity=".14"/><stop offset="1" stop-color="#FFB85A" stop-opacity="0"/></radialGradient>
  <linearGradient id="cone" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE7B0" stop-opacity=".34"/><stop offset="1" stop-color="#FFE7B0" stop-opacity="0"/></linearGradient>
  <radialGradient id="vig" cx=".5" cy=".45" r=".75"><stop offset=".6" stop-color="#0A0303" stop-opacity="0"/><stop offset="1" stop-color="#0A0303" stop-opacity=".5"/></radialGradient>
</defs>"""

svg = (f'<svg id="scene" viewBox="0 0 400 560" role="img" aria-labelledby="sceneT" data-art-class="studio-cut">'
       f'<title id="sceneT">A cut-paper miniature of a small cafe at dusk, seen at eye level. A round wooden high-top '
       f'with a brass plaque stands under a hanging lamp; beyond it a red wall and a window onto a peach and violet '
       f'sky over rooftops, and a back bar of paper bottles. A server\'s hand sets down a warm bread plate.</title>'
       f'{defs}{"".join(layers)}'
       f'<rect width="400" height="560" filter="url(#grain)" opacity=".22" style="mix-blend-mode:multiply" pointer-events="none"/>'
       f'<rect width="400" height="560" fill="url(#vig)" pointer-events="none"/></svg>')

html = open(__file__.replace("edgars-spot-paper-gen.py", "edgars-spot-paper-shell.html")).read().replace("<!--SCENE-->", svg)
open(__file__.replace("claude/edgars-spot-paper-gen.py", "lab/edgars-spot-paper.html"), "w").write(html)
print("wrote lab/edgars-spot-paper.html", len(html), "bytes")
