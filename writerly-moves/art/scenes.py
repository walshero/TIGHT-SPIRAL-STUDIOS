import math, random
exec(open('./base.py').read())
exec(open('./four.py').read())

AMBER = '#f0c46a'; RED = '#c23a2b'

def bg(col):
    return f'<rect x="-10" y="-60" width="428" height="440" fill="{col}"/>'

def sh(p, k=''):
    return f'url(#{p}sh{k})'

# ---------- paper-doll figure ----------
POSES = {
 'stand':  dict(head=(0,-.90), neck=(0,-.79), hip=(0,-.47),
                arms=[[(-.08,-.77),(-.12,-.60),(-.12,-.45)],[(.08,-.77),(.12,-.60),(.12,-.45)]],
                legs=[[(-.04,-.47),(-.05,-.24),(-.06,0)],[(.04,-.47),(.05,-.24),(.06,0)]]),
 'reach':  dict(head=(0,-.90), neck=(0,-.79), hip=(0,-.47),
                arms=[[(-.08,-.77),(-.12,-.60),(-.11,-.45)],[(.08,-.78),(.12,-.96),(.15,-1.14)]],
                legs=[[(-.04,-.47),(-.04,-.24),(-.03,-.03)],[(.04,-.47),(.05,-.24),(.05,-.03)]]),
 'run':    dict(head=(.06,-.89), neck=(.04,-.78), hip=(0,-.47),
                arms=[[(.02,-.76),(-.12,-.64),(-.18,-.70)],[(.06,-.76),(.16,-.62),(.24,-.68)]],
                legs=[[(0,-.47),(.16,-.30),(.13,-.06)],[(0,-.47),(-.08,-.26),(-.24,-.16)]]),
 'straddle':dict(head=(0,-.90), neck=(0,-.79), hip=(0,-.47),
                arms=[[(-.08,-.77),(-.24,-.74),(-.38,-.78)],[(.08,-.77),(.24,-.74),(.38,-.78)]],
                legs=[[(-.04,-.47),(-.16,-.24),(-.27,0)],[(.04,-.47),(.16,-.24),(.27,0)]]),
 'sit':    dict(head=(0,-.72), neck=(0,-.61), hip=(0,-.30),
                arms=[[(-.07,-.59),(-.06,-.44),(.10,-.36)],[(.07,-.59),(.10,-.44),(.18,-.36)]],
                legs=[[(-.02,-.30),(.18,-.30),(.18,0)],[(.04,-.30),(.22,-.30),(.22,0)]]),
 'hunch':  dict(head=(.13,-.62), neck=(.08,-.55), hip=(0,-.30),
                arms=[[(.05,-.53),(.10,-.40),(.17,-.30)],[(.09,-.53),(.15,-.40),(.20,-.31)]],
                legs=[[(-.02,-.30),(.20,-.30),(.20,0)],[(.03,-.30),(.25,-.30),(.25,-.05)]]),
 'carry':  dict(head=(0,-.90), neck=(0,-.79), hip=(0,-.47),
                arms=[[(-.08,-.77),(-.13,-.60),(-.14,-.46)],[(.08,-.77),(.16,-.64),(.24,-.58)]],
                legs=[[(-.04,-.47),(-.10,-.24),(-.14,0)],[(.04,-.47),(.10,-.24),(.13,0)]]),
 'mask':   dict(head=(0,-.90), neck=(0,-.79), hip=(0,-.47),
                arms=[[(-.08,-.77),(-.12,-.60),(-.12,-.45)],[(.08,-.77),(.18,-.80),(.12,-.90)]],
                legs=[[(-.04,-.47),(-.05,-.24),(-.06,0)],[(.04,-.47),(.05,-.24),(.06,0)]]),
 'slump':  dict(head=(.06,-.74), neck=(.03,-.68), hip=(0,-.30),
                arms=[[(-.02,-.66),(.06,-.62),(.07,-.74)],[(.05,-.66),(.12,-.62),(.10,-.74)]],
                legs=[[(-.02,-.30),(.16,-.30),(.17,0)],[(.04,-.30),(.21,-.30),(.21,0)]]),
 'bowed':  dict(head=(.07,-.84), neck=(.03,-.76), hip=(0,-.47),
                arms=[[(-.04,-.74),(.04,-.66),(.07,-.82)],[(.08,-.74),(.14,-.66),(.10,-.82)]],
                legs=[[(-.04,-.47),(-.04,-.24),(-.05,0)],[(.04,-.47),(.04,-.24),(.05,0)]]),
 'climb':  dict(head=(.10,-.82), neck=(.07,-.72), hip=(-.02,-.44),
                arms=[[(.05,-.70),(.16,-.58),(.26,-.44)],[(.09,-.70),(.20,-.56),(.30,-.45)]],
                legs=[[(-.02,-.44),(.10,-.30),(.08,-.06)],[(-.02,-.44),(-.12,-.24),(-.16,0)]]),
 'perch':  dict(head=(0,-.72), neck=(0,-.61), hip=(0,-.30),
                arms=[[(-.07,-.59),(-.18,-.50),(-.22,-.36)],[(.07,-.59),(.18,-.50),(.22,-.36)]],
                legs=[[(-.03,-.30),(.03,-.12),(-.02,0)],[(.03,-.30),(.10,-.14),(.08,0)]]),
}
def person(x, yf, h, col, pose='stand', lean=0, flip=False, p='', shadow=True):
    P = POSES[pose]; a = math.radians(lean)
    def T(pt):
        px, py = pt
        if flip: px = -px
        rx = px*math.cos(a) - py*math.sin(a); ry = px*math.sin(a) + py*math.cos(a)
        return (x + rx*h, yf + ry*h)
    def chain(pts, w):
        q = [T(t) for t in pts]
        d = 'M' + ' L'.join(f'{u:.1f} {v:.1f}' for u, v in q)
        return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w:.1f}" stroke-linecap="round" stroke-linejoin="round"/>'
    out = []
    for arm in P['arms']: out.append(chain(arm, h*.055))
    for leg in P['legs']: out.append(chain(leg, h*.07))
    n = T(P['neck']); hp = T(P['hip'])
    # torso as a fat stroke from neck to hip
    out.append(f'<path d="M{n[0]:.1f} {n[1]+h*.03:.1f} L{hp[0]:.1f} {hp[1]:.1f}" stroke="{col}" stroke-width="{h*.17:.1f}" stroke-linecap="round"/>')
    hc = T(P['head']); out.append(f'<circle cx="{hc[0]:.1f}" cy="{hc[1]:.1f}" r="{h*.085:.1f}" fill="{col}"/>')
    f = f' filter="url(#{p}shf)"' if shadow else ''
    return f'<g{f}>' + ''.join(out) + '</g>'

def figdefs(p):
    return (f'<defs><filter id="{p}shf" x="-60%" y="-30%" width="220%" height="160%" filterUnits="objectBoundingBox">'
            f'<feDropShadow dx="1" dy="3" stdDeviation="2" flood-color="#000" flood-opacity=".35"/></filter></defs>')

def blob(cx, cy, rx, ry, seed, n=18, amp=1.2):
    pts = [(cx + rx*math.cos(a/n*6.283), cy + ry*math.sin(a/n*6.283)) for a in range(n)]
    return wob(pts, amp, seed, 1)

def cloudpath(cx, cy, sc, seed, flatten=True):
    r = random.Random(seed); pts = []
    for a in range(30):
        t = a/30*6.283; rad = 1 + .17*math.sin(t*5 + seed) + r.uniform(-.03, .03)
        pts.append((cx + sc*1.9*rad*math.cos(t), cy + sc*.8*rad*math.sin(t)))
    if flatten: pts = [(u, min(v, cy + sc*.42)) for u, v in pts]
    return wob(pts, 1, seed, 1)

# ======================= CORE CRAFT (indigo) =======================
C = G['Core Craft']; W_ = G['Workshop Diagnostic']; D = G['Drafty Air']; K = G['Cliché Clinic']

def s_domino(p):
    o = [defs(p), bg(C['dark'])]
    o.append(f'<circle cx="70" cy="40" r="46" fill="{C["mid"]}" opacity=".5"/><circle cx="70" cy="40" r="26" fill="{AMBER}" filter="{sh(p,2)}"/>')
    o.append(f'<path d="{band([(-10,236),(418,206)],seed=3)}" fill="#2e3f74" filter="{sh(p)}"/>')
    o.append(f'<path d="{band([(-10,300),(418,280)],seed=4)}" fill="{C["mid"]}" filter="{sh(p)}"/>')
    # dominoes recede along a line; the first one is falling into the second
    xs = [96, 156, 208, 254, 294, 330, 362]; base = [300, 288, 278, 270, 262, 255, 249]
    hs = [124, 112, 100, 90, 80, 72, 64]
    for i in range(len(xs)-1, 0, -1):
        x, yb, hh = xs[i], base[i], hs[i]; w = hh*.42
        o.append(f'<path d="M{x+w:.1f} {yb} L{x+w+hh*.55:.1f} {yb+6} L{x+w*1.1+hh*.55:.1f} {yb+10} L{x+w:.1f} {yb+8}Z" fill="#000" opacity=".22"/>')
        o.append(f'<g filter="{sh(p,2)}"><path d="{wob([(x,yb-hh),(x+w,yb-hh),(x+w,yb),(x,yb)],.8,40+i,2)}" fill="{CREAM}"/>'
                 f'<rect x="{x+3:.1f}" y="{yb-hh/2-1.5:.1f}" width="{w-6:.1f}" height="3" fill="{C["dark"]}"/>'
                 f'<circle cx="{x+w/2:.1f}" cy="{yb-hh*.75:.1f}" r="{w*.1:.1f}" fill="{C["dark"]}"/>'
                 f'<circle cx="{x+w/2:.1f}" cy="{yb-hh*.25:.1f}" r="{w*.1:.1f}" fill="{C["dark"]}"/></g>')
    x, yb, hh = xs[0], base[0], hs[0]; w = hh*.42
    o.append(f'<g transform="rotate(26 {x+w} {yb})" filter="{sh(p)}"><path d="{wob([(x,yb-hh),(x+w,yb-hh),(x+w,yb),(x,yb)],.8,40,2)}" fill="{CREAM}"/>'
             f'<rect x="{x+3}" y="{yb-hh/2-1.5}" width="{w-6:.1f}" height="3" fill="{C["dark"]}"/>'
             + ''.join(f'<circle cx="{x+w*u:.1f}" cy="{yb-hh*v:.1f}" r="{w*.09:.1f}" fill="{C["dark"]}"/>' for u, v in [(.3,.8),(.7,.7),(.5,.25)]) + '</g>')
    o.append(grain(p)); return ''.join(o)

def s_northstar(p):
    o = [defs(p), bg('#1a2448')]
    r = random.Random(5)
    for i in range(20):
        o.append(f'<circle cx="{r.uniform(10,398):.1f}" cy="{r.uniform(-20,150):.1f}" r="{r.uniform(.8,1.8):.1f}" fill="{CREAM}" opacity="{r.uniform(.4,.8):.2f}"/>')
    sx, sy = 300, 30
    o.append(f'<circle cx="{sx}" cy="{sy}" r="44" fill="{C["mid"]}" opacity=".45"/>')
    o.append(f'<path d="M{sx} {sy-30} L{sx+7} {sy-7} L{sx+30} {sy} L{sx+7} {sy+7} L{sx} {sy+30} L{sx-7} {sy+7} L{sx-30} {sy} L{sx-7} {sy-7}Z" fill="{CREAM}" filter="{sh(p,2)}"/>')
    for i, col in enumerate(['#24336a', C['dark'], '#1c2a55', '#16204a']):
        o.append(f'<path d="{band(wave(196+i*44,6,7,i*1.1),seed=10+i)}" fill="{col}" filter="{sh(p,2)}" opacity=".96"/>')
    # star's reflection path on the water
    for i, y in enumerate(range(212, 360, 18)):
        wv = 10 + i*5
        o.append(f'<path d="M{sx-wv*.4+i*-8:.1f} {y} h{wv:.1f}" stroke="{CREAM}" stroke-width="3" stroke-linecap="round" opacity="{.8-i*.08:.2f}"/>')
    # boat turned toward the star; wake curls behind it
    o.append(f'<path d="M120 300 Q146 296 170 292" fill="none" stroke="{C["light"]}" stroke-width="3" stroke-linecap="round" opacity=".8"/>')
    o.append(f'<path d="M110 310 Q140 304 166 298" fill="none" stroke="{C["light"]}" stroke-width="2.5" stroke-linecap="round" opacity=".55"/>')
    o.append(f'<g filter="{sh(p)}"><path d="M164 284 L236 266 L226 286 L178 296Z" fill="{CREAM}"/>'
             f'<rect x="200" y="176" width="4" height="98" fill="{CREAM}" transform="rotate(-8 202 274)"/>'
             f'<path d="M210 182 L252 256 L212 264Z" fill="{CREAM}"/><path d="M198 196 L172 262 L196 266Z" fill="{C["light"]}"/></g>')
    o.append(grain(p)); return ''.join(o)

def s_misbelief(p):
    o = [defs(p), figdefs(p), bg('#2b3a6c')]
    o.append(f'<path d="{band([(-10,190),(418,178)],seed=20)}" fill="{C["mid"]}" filter="{sh(p,2)}"/>')
    # open doorway with warm light: what the character needs
    o.append(f'<g filter="{sh(p)}"><path d="{wob([(300,60),(372,60),(372,192),(300,192)],1,21,2)}" fill="{C["dark"]}"/>'
             f'<rect x="310" y="72" width="52" height="120" fill="{AMBER}"/></g>')
    o.append(f'<path d="M310 192 L362 192 L400 300 L250 300Z" fill="{AMBER}" opacity=".55"/>')
    # the groove: a closed loop worn into the floor; the rule keeps them circling, never toward the door
    o.append(f'<ellipse cx="150" cy="262" rx="112" ry="36" fill="none" stroke="#1a2448" stroke-width="16"/>')
    o.append(f'<ellipse cx="150" cy="262" rx="112" ry="36" fill="none" stroke="{C["light"]}" stroke-width="2" stroke-dasharray="2 10" opacity=".7"/>')
    o.append(f'<g filter="{sh(p,2)}"><rect x="96" y="214" width="56" height="7" fill="{AMBER}"/><path d="M98 217 q-6 -30 -18 -28 q-10 4 -2 28 q-8 24 2 28 q12 2 18 -28Z" fill="{AMBER}"/></g>')
    o.append(person(150, 298, 140, CREAM, 'stand', p=p))
    o.append(grain(p)); return ''.join(o)

def s_frictive(p):
    o = [defs(p), figdefs(p), bg('#1f2b55')]
    o.append(f'<circle cx="60" cy="40" r="22" fill="{CREAM}" opacity=".85"/>')
    for i, col in enumerate(['#2c3c72', C['mid'], '#34478a']):
        o.append(f'<path d="{band(wave(170+i*50,5,8,i),seed=30+i)}" fill="{col}" filter="{sh(p,2)}"/>')
    # two rafts drifting apart; one carries a lit lantern (home), the other a sail (away)
    o.append(f'<g filter="{sh(p)}"><path d="{wob([(36,282),(160,276),(166,296),(42,302)],1,31,3)}" fill="#9a7a52"/>'
             f'<rect x="64" y="228" width="6" height="50" fill="{CREAM}"/><path d="M58 220 h18 v16 h-18z" fill="{AMBER}"/></g>')
    o.append(f'<g filter="{sh(p)}"><path d="{wob([(246,288),(372,282),(378,302),(252,308)],1,32,3)}" fill="#9a7a52"/>'
             f'<rect x="338" y="196" width="5" height="88" fill="{CREAM}"/><path d="M344 202 L388 272 L344 276Z" fill="{CREAM}"/></g>')
    # the gap: water opening between them
    for k in range(3):
        o.append(f'<path d="M172 {300+k*10} q38 8 74 0" fill="none" stroke="{C["light"]}" stroke-width="2.5" opacity="{.8-k*.2:.1f}"/>')
    o.append(person(206, 284, 150, CREAM, 'straddle', p=p))
    o.append(grain(p)); return ''.join(o)

def s_mindseye(p):
    o = [defs(p), bg('#cfe0ea')]
    # the vivid view: birches and a ripe peach, specific not generic
    o.append(f'<path d="{band(wave(250,6,6,0.5),seed=40)}" fill="#a9c79a"/>')
    o.append(f'<path d="{band(wave(290,5,6,2),seed=41)}" fill="#7fa772"/>')
    for i, (x, w_) in enumerate([(120, 16), (196, 20), (262, 14), (300, 11)]):
        o.append(f'<rect x="{x}" y="-30" width="{w_}" height="330" fill="{CREAM}" filter="{sh(p,2)}"/>')
        r = random.Random(42+i)
        for k in range(9):
            y = r.uniform(-20, 280)
            o.append(f'<rect x="{x+r.uniform(0,w_*.4):.1f}" y="{y:.1f}" width="{w_*r.uniform(.3,.7):.1f}" height="{r.uniform(2,4.5):.1f}" fill="{INK}"/>')
    o.append(f'<path d="M150 70 Q190 64 236 78" fill="none" stroke="#6b4a2c" stroke-width="5" stroke-linecap="round"/>')
    o.append(f'<g filter="{sh(p,2)}"><path d="M206 74 q-2 10 0 14" stroke="#6b4a2c" stroke-width="3"/><circle cx="206" cy="104" r="20" fill="#f0995a"/>'
             f'<path d="M206 86 q-8 18 0 36" stroke="#d9773f" stroke-width="2.5" fill="none"/><path d="M210 82 q16 -10 22 2 q-12 6 -22 -2Z" fill="#5f8a4a"/></g>')
    # the dark wall with an eye-shaped cut opening onto it
    eye = 'M-20 -60 L428 -60 L428 380 L-20 380Z M28 150 Q204 -40 380 150 Q204 340 28 150Z'
    o.append(f'<path d="{eye}" fill="{C["dark"]}" fill-rule="evenodd" filter="{sh(p)}"/>')
    o.append(f'<path d="M28 150 Q204 -40 380 150 Q204 340 28 150Z" fill="none" stroke="{C["mid"]}" stroke-width="8"/>')
    o.append(grain(p)); return ''.join(o)

def s_disclosure(p):
    o = [defs(p), figdefs(p), bg('#1f2b55')]
    o.append(f'<path d="{band([(-10,330),(418,330)],seed=50)}" fill="#16204a"/>')
    # dollhouse cutaway: three rooms, three people, one hidden letter only the reader sees
    o.append(f'<g filter="{sh(p)}"><path d="M74 104 L204 30 L334 104Z" fill="{C["mid"]}"/>'
             f'<rect x="84" y="104" width="240" height="226" fill="#2e3f74"/></g>')
    o.append(f'<rect x="96" y="114" width="216" height="96" fill="#e9dcc0"/><rect x="96" y="222" width="102" height="98" fill="#d9cba9"/><rect x="210" y="222" width="102" height="98" fill="#e9dcc0"/>')
    o.append(f'<rect x="84" y="206" width="240" height="18" fill="#6e5a3e"/>')
    # the letter under the floorboard, lit, between floors
    o.append(f'<g filter="{sh(p,2)}"><rect x="222" y="209" width="40" height="12" fill="#3e3020"/><rect x="226" y="211" width="32" height="8" fill="{AMBER}"/></g>')
    o.append(f'<path d="M226 212 l17 5 l17 -5" fill="none" stroke="#8a5d14" stroke-width="1.6"/>')
    o.append(person(242, 206, 70, C['dark'], 'stand', p=p, shadow=False))   # stands right on top of it, unaware
    o.append(person(140, 206, 70, C['dark'], 'stand', flip=True, p=p, shadow=False))
    o.append(person(150, 320, 70, C['dark'], 'sit', p=p, shadow=False))
    o.append(f'<rect x="250" y="276" width="48" height="10" fill="#8a7553"/><rect x="254" y="286" width="5" height="34" fill="#8a7553"/><rect x="290" y="286" width="5" height="34" fill="#8a7553"/>')
    o.append(grain(p)); return ''.join(o)

def s_afterstorm(p):
    o = [defs(p), figdefs(p), bg('#b9cbe3')]
    # the storm is leaving frame left; we arrive mid-run
    o.append(f'<path d="{cloudpath(40,30,70,51,False)}" fill="#46527c" filter="{sh(p)}"/>')
    o.append(f'<path d="M30 92 l14 26 l-10 2 l16 30" fill="none" stroke="{AMBER}" stroke-width="5" stroke-linejoin="round"/>')
    o.append(f'<circle cx="330" cy="40" r="26" fill="{CREAM}" opacity=".9"/>')
    o.append(f'<path d="{band([(-10,206),(80,198),(200,210),(418,196)],seed=52)}" fill="{C["light"]}" filter="{sh(p,2)}"/>')
    o.append(f'<path d="{band([(-10,250),(418,246)],seed=53)}" fill="{C["mid"]}" filter="{sh(p)}"/>')
    # puddles reflecting sky
    for (cx, cy, rx) in [(110, 310, 60), (300, 334, 74), (220, 282, 34)]:
        o.append(f'<path d="{blob(cx,cy,rx,rx*.16,cx)}" fill="#b9cbe3"/>')
    o.append(person(196, 300, 132, CREAM, 'run', p=p))
    for (x, y, dx, dy) in [(168, 296, -12, -14), (176, 300, -4, -20), (214, 298, 10, -16), (154, 302, -20, -6)]:
        o.append(f'<path d="M{x} {y} q{dx/2} {dy} {dx} {dy*.6}" fill="none" stroke="{CREAM}" stroke-width="3" stroke-linecap="round"/>')
    o.append(grain(p)); return ''.join(o)

def s_residue(p):
    o = [defs(p), bg('#2a3769')]
    # night window, the room after: cup still steaming, chair pushed back, door left open
    o.append(f'<g filter="{sh(p,2)}"><rect x="40" y="20" width="110" height="140" fill="#16204a"/><rect x="40" y="88" width="110" height="5" fill="{C["mid"]}"/><rect x="92" y="20" width="5" height="140" fill="{C["mid"]}"/></g>')
    o.append(f'<circle cx="122" cy="52" r="12" fill="{CREAM}" opacity=".85"/>')
    o.append(f'<g filter="{sh(p)}"><path d="{wob([(290,30),(364,30),(364,250),(290,250)],1,60,2)}" fill="#1a2448"/>'
             f'<path d="M290 30 L322 40 L322 240 L290 250Z" fill="{AMBER}"/></g>')
    o.append(f'<path d="M290 250 L322 240 L380 330 L250 330Z" fill="{AMBER}" opacity=".5"/>')
    o.append(f'<path d="{band([(-10,250),(418,250)],seed=61)}" fill="#1c2750"/>')
    # table
    o.append(f'<g filter="{sh(p)}"><path d="M70 214 L250 214 L262 228 L58 228Z" fill="#8a6d4a"/><rect x="74" y="228" width="8" height="90" fill="#6e5538"/><rect x="236" y="228" width="8" height="90" fill="#6e5538"/></g>')
    # chair pushed back from the table, left where someone stood up
    o.append(f'<g filter="{sh(p)}"><rect x="300" y="180" width="7" height="140" fill="#7a603f"/><rect x="300" y="252" width="50" height="8" fill="#7a603f"/><rect x="343" y="260" width="7" height="60" fill="#7a603f"/></g>')
    # cup and steam
    o.append(f'<g filter="{sh(p,2)}"><path d="M136 190 h34 l-4 24 h-26z" fill="{CREAM}"/><path d="M170 196 a7 7 0 0 1 0 12" fill="none" stroke="{CREAM}" stroke-width="3.5"/></g>')
    for k, dx in enumerate([142, 152, 162]):
        o.append(f'<path d="M{dx} 184 q-8 -12 0 -24 q8 -12 0 -24" fill="none" stroke="{CREAM}" stroke-width="2.5" stroke-linecap="round" opacity="{.75-k*.15:.2f}"/>')
    o.append(grain(p)); return ''.join(o)

def s_retro(p):
    o = [defs(p), bg('#1d2850')]
    # a long hall; the key hangs here, the lock waits at the end
    o.append(f'<path d="M-10 -60 L170 120 L170 230 L-10 380Z" fill="#2e3f74" filter="{sh(p)}"/>')
    o.append(f'<path d="M418 -60 L238 120 L238 230 L418 380Z" fill="#26356a" filter="{sh(p)}"/>')
    o.append(f'<path d="M-10 380 L170 230 L238 230 L418 380Z" fill="#3a4c86"/>')
    for k in range(5):
        y = 236 + k*k*7 + k*10
        o.append(f'<path d="M{170-(y-230)*1.2:.1f} {y} L{238+(y-230)*1.2:.1f} {y}" stroke="{C["dark"]}" stroke-width="2" opacity=".6"/>')
    o.append(f'<rect x="170" y="120" width="68" height="110" fill="#16204a"/>')
    o.append(f'<g filter="{sh(p,2)}"><rect x="180" y="132" width="48" height="98" fill="{C["mid"]}"/></g>')
    o.append(f'<path d="M204 176 a5 5 0 1 1 0.1 0 M201 184 h6 l2 12 h-10z" fill="{AMBER}"/>')
    o.append(f'<path d="M204 196 L190 230 L218 230Z" fill="{AMBER}" opacity=".35"/>')
    # the key on its nail, close to us
    o.append(f'<circle cx="74" cy="104" r="4" fill="{INK}"/>')
    o.append(f'<path d="M74 104 L74 120" stroke="{INK}" stroke-width="2"/>')
    o.append(f'<g filter="{sh(p)}" transform="rotate(8 74 120)"><path fill-rule="evenodd" fill="{AMBER}" d="M74 120 a16 16 0 1 1 -0.1 0Z M74 128 a8 8 0 1 0 0.1 0Z"/>'
             f'<rect x="70" y="150" width="8" height="70"/><rect x="70" y="150" width="8" height="70" fill="{AMBER}"/><rect x="78" y="198" width="12" height="6" fill="{AMBER}"/><rect x="78" y="210" width="9" height="6" fill="{AMBER}"/></g>')
    o.append(grain(p)); return ''.join(o)

def s_status(p):
    o = [defs(p), figdefs(p), bg('#c9d2ec')]
    o.append(f'<path d="{cloudpath(320,40,26,70)}" fill="{CREAM}" filter="{sh(p,2)}"/>')
    o.append(f'<path d="{band(wave(250,8,5,1),seed=71)}" fill="{C["light"]}" filter="{sh(p,2)}"/>')
    o.append(f'<path d="{band([(-10,300),(160,286),(260,290),(418,302)],seed=72)}" fill="{C["mid"]}" filter="{sh(p)}"/>')
    # seesaw mid-tip: the high one is coming down, the low one rising
    cx, cy = 204, 268
    o.append(f'<path d="M{cx-16} 292 L{cx} {cy} L{cx+16} 292Z" fill="{C["dark"]}" filter="{sh(p)}"/>')
    ang = -14
    o.append(f'<g transform="rotate({ang} {cx} {cy})" filter="{sh(p)}"><rect x="{cx-140}" y="{cy-6}" width="280" height="10" rx="3" fill="#8a6d4a"/></g>')
    def endpt(dx):
        a = math.radians(ang); return (cx + dx*math.cos(a), cy + dx*math.sin(a))
    lx, ly = endpt(-122); rx, ry = endpt(122)
    o.append(person(lx-14, ly+26, 92, C['dark'], 'sit', p=p))
    o.append(person(rx+14, ry+26, 92, C['dark'], 'sit', flip=True, p=p))
    o.append(f'<path d="M{rx+28:.1f} {ry-58:.1f} a28 28 0 0 0 0 -30" fill="none" stroke="{C["dark"]}" stroke-width="3" stroke-dasharray="4 5"/>')
    o.append(f'<path d="M{lx-28:.1f} {ly-10:.1f} a28 28 0 0 0 0 30" fill="none" stroke="{C["dark"]}" stroke-width="3" stroke-dasharray="4 5"/>')
    o.append(grain(p)); return ''.join(o)

def s_honne(p):
    o = [defs(p), figdefs(p), bg('#e3d6b6')]
    # lamp at left throws her true posture onto the wall; in front, the mask is up
    o.append(f'<path d="M-10 -60 L418 -60 L418 300 L-10 300Z" fill="#d8c9a4"/>')
    o.append(f'<path d="M-10 -60 L120 -60 L60 300 L-10 300Z" fill="#efe4c8" opacity=".7"/>')
    o.append(f'<path d="{band([(-10,300),(418,300)],seed=80)}" fill="{C["mid"]}"/>')
    # shadow: hunched, head in hands
    o.append(person(300, 300, 200, '#3a3a52', 'bowed', p=p, shadow=False).replace('<g>', '<g opacity=".55">'))
    o.append(f'<g filter="{sh(p)}"><rect x="40" y="150" width="8" height="150" fill="{INK}"/><path d="M22 150 L66 150 L56 118 L32 118Z" fill="{AMBER}"/></g>')
    # the person, upright, holding a mask to the face
    o.append(person(170, 312, 210, C['dark'], 'mask', p=p))
    mx, my = 170, 124
    o.append(f'<g filter="{sh(p,2)}"><path d="M{mx-24} {my-30} Q{mx} {my-40} {mx+24} {my-30} Q{mx+28} {my+14} {mx} {my+34} Q{mx-28} {my+14} {mx-24} {my-30}Z" fill="{CREAM}"/>'
             f'<path d="M{mx-15} {my-8} q6 -5 12 0 q-6 3 -12 0Z M{mx+3} {my-8} q6 -5 12 0 q-6 3 -12 0Z" fill="{INK}"/>'
             f'<path d="M{mx-8} {my+14} q8 4 16 0" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>'
             f'<rect x="{mx+18}" y="{my+16}" width="4" height="30" fill="#8a6d4a" transform="rotate(-30 {mx+20} {my+16})"/></g>')
    o.append(grain(p)); return ''.join(o)

# ======================= WORKSHOP DIAGNOSTIC (pine) =======================
def s_hunger(p):
    o = [defs(p), figdefs(p), bg('#dfe9e0')]
    o.append(f'<rect x="-10" y="300" width="428" height="80" fill="{W_["mid"]}"/>')
    # high shelf, a jar of honey just out of reach
    o.append(f'<g filter="{sh(p)}"><rect x="190" y="48" width="230" height="12" fill="#8a6d4a"/><path d="M220 60 l14 22 h-8 l-12 -22Z M390 60 l14 22 h-8 l-12 -22Z" fill="#6e5538"/></g>')
    o.append(f'<g filter="{sh(p)}"><rect x="250" y="-4" width="46" height="52" rx="6" fill="{AMBER}"/><rect x="246" y="-12" width="54" height="12" rx="2" fill="{W_["dark"]}"/><rect x="256" y="12" width="34" height="18" fill="{CREAM}"/></g>')
    o.append(f'<g filter="{sh(p)}"><rect x="94" y="252" width="70" height="10" fill="#8a6d4a"/><rect x="100" y="262" width="7" height="40" fill="#6e5538"/><rect x="150" y="262" width="7" height="40" fill="#6e5538"/></g>')
    o.append(person(128, 252, 156, W_['dark'], 'reach', lean=8, p=p))
    o.append(grain(p)); return ''.join(o)

def s_friction(p):
    o = [defs(p), figdefs(p), bg('#cfe2d6')]
    # the lit house is the want; a fallen trunk blocks the road to it
    o.append(f'<path d="{band(wave(150,8,5,.3),seed=90)}" fill="{W_["light"]}" filter="{sh(p,2)}"/>')
    o.append(f'<g filter="{sh(p,2)}"><rect x="300" y="110" width="50" height="40" fill="{CREAM}"/><path d="M294 112 L325 88 L356 112Z" fill="{W_["dark"]}"/><rect x="318" y="122" width="14" height="14" fill="{AMBER}"/></g>')
    o.append(f'<path d="{band(wave(196,6,5,1.5),seed=91)}" fill="{W_["mid"]}" filter="{sh(p)}"/>')
    o.append(f'<path d="M150 380 L216 196 L240 196 L300 380Z" fill="#c8b48c"/>')
    o.append(f'<path d="M226 210 v16 M224 246 v20 M222 290 v26" stroke="{CREAM}" stroke-width="4"/>')
    o.append(f'<g filter="{sh(p)}"><path d="{wob([(80,262),(380,236),(386,262),(86,290)],1.6,92,4)}" fill="#6b4a2c"/>'
             f'<path fill="#a07a50" d="{blob(383,249,7,13,93,12,.6)}"/></g>')
    o.append(f'<path d="M120 274 l40 -4 M200 266 l60 -6 M300 256 l40 -3" stroke="#4e3520" stroke-width="2"/>')
    o.append(person(212, 330, 112, W_['dark'], 'climb', flip=False, lean=-4, p=p))
    o.append(grain(p)); return ''.join(o)

def s_microtension(p):
    o = [defs(p), bg('#2a5a4c')]
    # a full glass at the very edge of the table
    o.append(f'<rect x="-10" y="-60" width="428" height="300" fill="#24504a"/>')
    o.append(f'<g filter="{sh(p)}"><path d="M-10 214 L300 214 L300 380 L-10 380Z" fill="#d8cba9"/><path d="M-10 226 L300 226" stroke="#b8a882" stroke-width="2"/></g>')
    o.append(f'<path d="M300 214 L300 380" stroke="#9c8c66" stroke-width="3"/>')
    gx = 298
    o.append(f'<g filter="{sh(p)}" transform="rotate(4 {gx} 214)"><path d="M{gx-26} 96 L{gx+26} 96 L{gx+20} 214 L{gx-20} 214Z" fill="#e8f1ee" opacity=".55"/>'
             f'<path d="M{gx-24} 110 L{gx+24} 110 L{gx+20} 212 L{gx-20} 212Z" fill="{W_["light"]}" opacity=".9"/>'
             f'<path d="M{gx-24} 110 q24 -4 48 0" fill="none" stroke="{CREAM}" stroke-width="2.5"/>'
             f'<path d="M{gx-26} 96 L{gx-20} 214" stroke="{CREAM}" stroke-width="2.5" opacity=".7"/></g>')
    o.append(f'<path d="M306 170 q6 10 0 14 q-6 -4 0 -14Z" fill="{W_["light"]}"/>')
    o.append(f'<path d="M309 240 q5 8 0 11 q-5 -3 0 -11Z" fill="{W_["light"]}" opacity=".8"/>')
    o.append(f'<path d="M60 180 L130 180 L126 212 L64 212Z" fill="{CREAM}" filter="{sh(p,2)}"/><path d="M130 186 a8 8 0 0 1 0 16" fill="none" stroke="{CREAM}" stroke-width="4"/>')
    o.append(grain(p)); return ''.join(o)

def s_worlddetail(p):
    o = [defs(p), bg('#2f6f5c')]
    # grand door, worn shoes on the step; the lens finds the taped sole
    o.append(f'<g filter="{sh(p)}"><path d="{wob([(150,-40),(330,-40),(330,250),(150,250)],1,100,2)}" fill="#3b2a1c"/>'
             f'<rect x="166" y="-24" width="70" height="120" fill="#4e3726"/><rect x="246" y="-24" width="70" height="120" fill="#4e3726"/>'
             f'<rect x="166" y="112" width="70" height="120" fill="#4e3726"/><rect x="246" y="112" width="70" height="120" fill="#4e3726"/>'
             f'<circle cx="240" cy="100" r="11" fill="none" stroke="{AMBER}" stroke-width="5"/></g>')
    o.append(f'<path d="M100 250 L380 250 L404 280 L76 280Z" fill="#b8b0a0" filter="{sh(p)}"/><path d="M60 280 L418 280 L418 380 L60 380Z" fill="#8f877a"/>')
    def shoe(x, y, tape=False):
        g = f'<path d="M{x} {y} L{x} {y-18} Q{x+2} {y-34} {x+24} {y-34} L{x+40} {y-34} Q{x+48} {y-18} {x+76} {y-12} Q{x+88} {y-8} {x+88} {y} Z" fill="#7a4e2c"/>'
        g += f'<rect x="{x-2}" y="{y-2}" width="92" height="6" fill="#3b2516"/>'
        g += f'<path d="M{x+30} {y-28} l12 6 M{x+28} {y-20} l14 6" stroke="{CREAM}" stroke-width="2"/>'
        if tape: g += f'<rect x="{x+50}" y="{y-16}" width="24" height="18" fill="#e6dccb" transform="rotate(-10 {x+62} {y-7})"/>'
        return f'<g filter="{sh(p,2)}">{g}</g>'
    o.append(shoe(150, 274) + shoe(250, 276, True))
    # magnifier over the taped shoe
    o.append(f'<g filter="{sh(p)}"><circle cx="312" cy="258" r="44" fill="#ffffff" opacity=".18"/><circle cx="312" cy="258" r="44" fill="none" stroke="{CREAM}" stroke-width="9"/>'
             f'<path d="M342 290 L384 336" stroke="{CREAM}" stroke-width="16" stroke-linecap="round"/></g>')
    o.append(grain(p)); return ''.join(o)

def s_interior(p):
    o = [defs(p), figdefs(p), bg('#cfe0d4')]
    # sunny outside the window; inside, it rains on one person only
    o.append(f'<g filter="{sh(p)}"><rect x="232" y="20" width="140" height="150" fill="#e9d48a"/></g>')
    o.append(f'<circle cx="320" cy="70" r="26" fill="#f6e7b0"/><path d="M232 128 Q270 116 300 126 Q340 136 372 122 L372 170 L232 170Z" fill="#a9cf9a"/>')
    o.append(f'<rect x="232" y="90" width="140" height="6" fill="{W_["dark"]}"/><rect x="298" y="20" width="6" height="150" fill="{W_["dark"]}"/>')
    o.append(f'<rect x="-10" y="290" width="428" height="90" fill="{W_["mid"]}"/>')
    o.append(f'<g filter="{sh(p)}"><path d="M70 214 L170 214 L170 290 L70 290Z" fill="#8a6d4a"/><rect x="70" y="140" width="14" height="150" fill="#7a603f"/></g>')
    o.append(person(100, 292, 150, W_['dark'], 'sit', p=p))
    o.append(f'<path d="{cloudpath(118,40,24,111)}" fill="#6f8f86" filter="{sh(p)}"/>')
    r = random.Random(112)
    for k in range(14):
        x = r.uniform(84, 158); y = r.uniform(70, 160)
        o.append(f'<path d="M{x:.1f} {y:.1f} l-3 12" stroke="#4d6f86" stroke-width="3" stroke-linecap="round"/>')
    o.append(f'<path d="{blob(116,292,46,6,113)}" fill="#4d6f86" opacity=".6"/>')
    o.append(grain(p)); return ''.join(o)

def s_stakes(p):
    o = [defs(p), figdefs(p), bg('#cfe2d6')]
    # a rope bridge over a drop; one strand frayed; she carries the only lantern
    o.append(f'<path d="M-10 160 L110 150 L140 380 L-10 380Z" fill="{W_["mid"]}" filter="{sh(p)}"/>')
    o.append(f'<path d="M418 150 L300 158 L270 380 L418 380Z" fill="{W_["mid"]}" filter="{sh(p)}"/>')
    o.append(f'<path d="M110 150 L140 380 L270 380 L300 158Z" fill="#163a31"/>')
    for i, op in enumerate([.5, .35, .25]):
        o.append(f'<path d="{band(wave(250+i*36,6,6,i),seed=120+i)}" fill="{CREAM}" opacity="{op}"/>')
    o.append(f'<path d="M100 150 Q205 196 310 156" fill="none" stroke="#6b4a2c" stroke-width="5"/>')
    o.append(f'<path d="M100 110 Q160 140 196 146" fill="none" stroke="#6b4a2c" stroke-width="3.5"/><path d="M214 146 Q260 140 310 116" fill="none" stroke="#6b4a2c" stroke-width="3.5"/>')
    o.append(f'<path d="M196 146 l-4 6 M196 146 l2 7 M214 146 l-3 7 M214 146 l4 5" stroke="#6b4a2c" stroke-width="2"/>')
    for k in range(9):
        t = k/8; x = 104 + t*202; y = 150 + 46*4*t*(1-t) - (6 if k in (4, 5) else 0)
        o.append(f'<rect x="{x-5:.1f}" y="{y-2:.1f}" width="10" height="7" fill="#9a7a52"/>')
    o.append(person(232, 172, 96, W_['dark'], 'carry', p=p))
    o.append(f'<g filter="{sh(p,2)}"><path d="M252 118 v8" stroke="{INK}" stroke-width="2"/><rect x="246" y="126" width="12" height="16" fill="{AMBER}"/></g>')
    o.append(f'<circle cx="252" cy="134" r="22" fill="{AMBER}" opacity=".25"/>')
    o.append(grain(p)); return ''.join(o)

def s_turnshift(p):
    o = [defs(p), bg('#cfe2d6')]
    # the weather turns: storm behind, clearing ahead, the vane mid-swing
    o.append(f'<path d="M-10 -60 L180 -60 L120 380 L-10 380Z" fill="#7f9a90"/>')
    o.append(f'<path d="{cloudpath(60,40,46,130,False)}" fill="#55706a" filter="{sh(p)}"/>')
    for x in (30, 56, 82, 108):
        o.append(f'<path d="M{x} 92 l-6 18" stroke="#3e5a54" stroke-width="3" stroke-linecap="round"/>')
    o.append(f'<circle cx="340" cy="44" r="28" fill="#f6e7b0"/>')
    o.append(f'<g filter="{sh(p)}"><path d="M60 380 L60 286 L204 210 L348 286 L348 380Z" fill="{W_["dark"]}"/><rect x="200" y="120" width="8" height="96" fill="{INK}"/></g>')
    o.append(f'<path d="M150 264 L258 264" stroke="{CREAM}" stroke-width="3" opacity=".25"/>')
    # vane: arrow swinging from the storm side to the clear side
    o.append(f'<path d="M140 120 A64 32 0 0 1 268 120" fill="none" stroke="{CREAM}" stroke-width="3" stroke-dasharray="5 7"/>')
    o.append(f'<path d="M262 112 l10 8 l-12 4" fill="none" stroke="{CREAM}" stroke-width="3" stroke-linejoin="round"/>')
    o.append(f'<g transform="rotate(-22 204 128)" filter="{sh(p)}"><rect x="146" y="124" width="116" height="8" fill="{AMBER}"/>'
             f'<path d="M262 116 L292 128 L262 140Z" fill="{AMBER}"/><path d="M146 116 L132 116 L140 128 L132 140 L146 140Z" fill="{AMBER}"/></g>')
    o.append(f'<circle cx="204" cy="128" r="7" fill="{INK}"/>')
    o.append(grain(p)); return ''.join(o)

# ======================= DRAFTY AIR (rust) =======================
def s_suitcase(p):
    o = [defs(p), figdefs(p), bg('#f3d3bb')]
    o.append(f'<rect x="-10" y="300" width="428" height="80" fill="{D["mid"]}"/>')
    # sitting on the lid to make it close; too much is sticking out
    o.append(f'<g filter="{sh(p)}"><path d="M96 300 L96 202 Q96 192 106 192 L302 192 Q312 192 312 202 L312 300Z" fill="{D["dark"]}"/>'
             f'<path d="M92 196 Q204 160 316 196 L316 210 L92 210Z" fill="#8f3a1c"/>'
             f'<rect x="150" y="190" width="14" height="110" fill="#5a2210"/><rect x="246" y="190" width="14" height="110" fill="#5a2210"/></g>')
    o.append(f'<g filter="{sh(p,2)}"><path d="M84 204 q-30 4 -44 26 l10 6 q12 -16 36 -20Z" fill="{CREAM}"/>'
             f'<path d="M316 206 l40 -20 l6 10 l-42 20Z" fill="#3e6f8a"/><path d="M356 186 l18 -8 l4 12 l-16 6Z" fill="{CREAM}"/>'
             f'<path d="M120 200 l-10 -26 l14 -4 l8 28Z" fill="{AMBER}"/><path d="M286 196 q10 -30 30 -40 l6 8 q-18 10 -26 34Z" fill="#7a8a5a"/></g>')
    o.append(person(204, 186, 120, CREAM, 'sit', p=p))
    o.append(grain(p)); return ''.join(o)

def s_thread(p):
    o = [defs(p), bg('#f1d2bb')]
    # a red thread leaves the spool, crosses the room, goes out the window and just stops
    o.append(f'<rect x="-10" y="290" width="428" height="90" fill="{D["mid"]}"/>')
    o.append(f'<g filter="{sh(p)}"><rect x="250" y="40" width="130" height="150" fill="#f7e7d4"/><rect x="250" y="40" width="130" height="150" fill="none" stroke="{D["dark"]}" stroke-width="8"/>'
             f'<path d="M250 40 L222 54 L222 200 L250 190Z" fill="{D["dark"]}"/></g>')
    o.append(f'<path d="{band(wave(150,6,4,1),bottom=186,seed=140,amp=.6)}" fill="{D["light"]}" transform="translate(0,0)" clip-path="none" opacity=".0"/>')
    o.append(f'<path d="M258 150 q30 -12 60 -2 q30 10 58 -4 L376 186 L258 186Z" fill="{D["light"]}"/>')
    o.append(f'<g filter="{sh(p)}"><path d="M40 230 L170 230 L180 244 L30 244Z" fill="#8a6d4a"/><rect x="40" y="244" width="8" height="50" fill="#6e5538"/><rect x="152" y="244" width="8" height="50" fill="#6e5538"/></g>')
    o.append(f'<g filter="{sh(p,2)}"><rect x="70" y="196" width="34" height="8" fill="#c8a878"/><rect x="74" y="204" width="26" height="22" fill="{RED}"/><rect x="70" y="226" width="34" height="6" fill="#c8a878"/></g>')
    o.append(f'<path d="M100 214 C150 214 170 320 230 316 C290 312 270 210 296 150 C306 124 330 112 352 100" fill="none" stroke="{RED}" stroke-width="3.5" stroke-linecap="round"/>')
    o.append(f'<path d="M352 100 q6 -2 8 4" fill="none" stroke="{RED}" stroke-width="3" stroke-linecap="round"/>')
    o.append(grain(p)); return ''.join(o)

def s_stock(p):
    o = [defs(p), bg('#2a1208')]
    # the screen plays the sunset everyone has seen; the seats are all the same too
    o.append(f'<g filter="{sh(p)}"><rect x="56" y="10" width="296" height="176" fill="#120804"/></g>')
    o.append(f'<rect x="66" y="20" width="276" height="156" fill="#f2b07a"/><circle cx="204" cy="132" r="34" fill="#f7d7a0"/>')
    o.append(f'<rect x="66" y="132" width="276" height="44" fill="#c4643a"/>')
    for k in range(4):
        o.append(f'<rect x="{150+k*6}" y="{140+k*8}" width="{108-k*12}" height="3" fill="#f7d7a0" opacity=".8"/>')
    o.append(f'<g fill="#3a1608"><circle cx="186" cy="102" r="6"/><rect x="180" y="108" width="12" height="26" rx="4"/><circle cx="214" cy="104" r="6"/><rect x="208" y="110" width="12" height="24" rx="4"/></g>')
    for x in range(56, 352, 18):
        o.append(f'<rect x="{x+4}" y="13" width="9" height="4" fill="#3a2a20"/><rect x="{x+4}" y="179" width="9" height="4" fill="#3a2a20"/>')
    for row, (y, s_) in enumerate([(250, 1.0), (300, 1.25), (352, 1.5)]):
        w = 52*s_
        for i in range(-1, 9):
            x = i*w + (row % 2)*w/2 - 10
            o.append(f'<path d="M{x:.1f} {y} q0 -{30*s_:.1f} {w*.45:.1f} -{32*s_:.1f} q{w*.45:.1f} 2 {w*.45:.1f} {32*s_:.1f}Z" fill="{["#5a2210","#4a1c0c","#3a1608"][row]}" filter="{sh(p,2)}"/>')
    o.append(grain(p)); return ''.join(o)

def s_toofast(p):
    o = [defs(p), bg('#2a1810')]
    # the party is happening right there, and the car is already past it
    o.append(f'<path d="{band(wave(200,8,5,.5),seed=150)}" fill="#3e2214" filter="{sh(p,2)}"/>')
    o.append(f'<g filter="{sh(p,2)}"><rect x="60" y="120" width="120" height="80" fill="#5a2a14"/><path d="M50 122 L120 78 L190 122Z" fill="{D["dark"]}"/>'
             f'<rect x="76" y="138" width="34" height="30" fill="{AMBER}"/><rect x="128" y="138" width="34" height="30" fill="{AMBER}"/></g>')
    r = random.Random(151)
    for k in range(10):
        x = r.uniform(70, 170); y = r.uniform(40, 110)
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r.uniform(2,4):.1f}" fill="{["#f0c46a","#e8a27c","#f4ecdc"][k%3]}"/>')
    o.append(f'<path d="M-10 250 L418 236 L418 380 L-10 380Z" fill="#1a0e08"/>')
    o.append(f'<path d="M-10 300 L418 288" stroke="{CREAM}" stroke-width="4" stroke-dasharray="26 22" opacity=".7"/>')
    for k, y in enumerate([226, 240, 254, 268]):
        o.append(f'<path d="M{20+k*14} {y} L{230-k*6} {y-6}" stroke="{D["light"]}" stroke-width="{5-k}" stroke-linecap="round" opacity="{.8-k*.15:.2f}"/>')
    o.append(f'<g filter="{sh(p)}"><path d="M232 270 L250 238 Q262 224 290 224 L330 224 Q346 226 356 242 L384 248 Q396 252 396 266 L396 276 L232 276Z" fill="{D["mid"]}"/>'
             f'<path d="M262 242 L274 230 L300 230 L300 244Z M308 230 L332 230 L344 244 L308 244Z" fill="#f3cdb2"/>'
             f'<circle cx="266" cy="278" r="15" fill="{INK}"/><circle cx="364" cy="278" r="15" fill="{INK}"/><circle cx="266" cy="278" r="6" fill="#8a7a6a"/><circle cx="364" cy="278" r="6" fill="#8a7a6a"/>'
             f'<path d="M392 254 l14 -2 l0 8 l-14 0Z" fill="{AMBER}"/></g>')
    o.append(grain(p)); return ''.join(o)

def s_dump(p):
    o = [defs(p), figdefs(p), bg('#f3d3bb')]
    o.append(f'<path d="{band(wave(220,8,5,1),seed=160)}" fill="{D["light"]}" filter="{sh(p,2)}"/>')
    o.append(f'<path d="M-10 280 L418 270 L418 380 L-10 380Z" fill="{D["mid"]}"/>')
    # the truck tips a load of paper across the road; the reader is stuck behind it
    o.append(f'<g filter="{sh(p)}"><path d="M250 250 L250 196 L292 196 L310 220 L338 222 L338 270 L250 270Z" fill="{D["dark"]}"/><path d="M262 204 L288 204 L300 222 L262 222Z" fill="#f3cdb2"/>'
             f'<circle cx="270" cy="274" r="14" fill="{INK}"/><circle cx="320" cy="274" r="14" fill="{INK}"/></g>')
    o.append(f'<g filter="{sh(p)}" transform="rotate(-32 252 254)"><path d="M120 200 L252 200 L252 254 L132 254Z" fill="#8f3a1c"/></g>')
    r = random.Random(161)
    pile = [(r.uniform(60, 240), r.uniform(220, 300), r.uniform(-40, 40)) for _ in range(46)]
    pile.sort(key=lambda t: t[1])
    for (x, y, a) in pile:
        o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="22" height="16" fill="{["#f4ecdc","#efe2c8","#e6d6b6"][int(x)%3]}" transform="rotate({a:.0f} {x+11:.1f} {y+8:.1f})" filter="{sh(p,2)}"/>')
    for (x, y, a) in [(150, 150, 20), (178, 128, -30), (126, 172, 48), (196, 160, 10)]:
        o.append(f'<rect x="{x}" y="{y}" width="20" height="14" fill="{CREAM}" transform="rotate({a} {x+10} {y+7})" filter="{sh(p,2)}"/>')
    o.append(person(30, 316, 70, D['dark'], 'stand', p=p))
    o.append(grain(p)); return ''.join(o)

# ======================= CLICHÉ CLINIC (plum) =======================
def s_fourth(p):
    o = [defs(p), bg('#3a1b37')]
    o.append(f'<path d="{band(wave(232,4,6,1),seed=170)}" fill="#2a1428"/>')
    o.append(f'<g filter="{sh(p)}"><path d="M-10 236 L418 228 L418 248 L-10 256Z" fill="#6e5538"/></g>')
    # three plain lanterns, the same; the fourth is the one only you would find
    for i, x in enumerate([60, 140, 220]):
        o.append(f'<rect x="{x-3}" y="110" width="6" height="128" fill="#5a4630" filter="{sh(p,2)}"/>')
        o.append(f'<g filter="{sh(p,2)}"><path d="M{x} 110 v10" stroke="{INK}" stroke-width="2"/><path d="{blob(x,140,18,22,171+i,16,.6)}" fill="#cbb9c4"/><rect x="{x-10}" y="116" width="20" height="4" fill="{K["mid"]}"/><rect x="{x-10}" y="160" width="20" height="4" fill="{K["mid"]}"/></g>')
    x = 316
    o.append(f'<rect x="{x-3}" y="100" width="6" height="134" fill="#5a4630" filter="{sh(p,2)}"/>')
    o.append(f'<circle cx="{x+6}" cy="146" r="48" fill="{AMBER}" opacity=".22"/>')
    o.append(f'<g filter="{sh(p)}"><path d="M{x} 100 v12" stroke="{INK}" stroke-width="2"/>'
             f'<path d="M{x-34} 146 Q{x-4} 110 {x+30} 140 L{x+48} 126 L{x+44} 148 L{x+48} 168 L{x+30} 152 Q{x-4} 180 {x-34} 146Z" fill="{AMBER}"/>'
             f'<circle cx="{x-18}" cy="142" r="3.5" fill="{INK}"/><path d="M{x-4} 128 q6 18 0 34 M{x+10} 132 q5 14 0 26" fill="none" stroke="#c8902e" stroke-width="2"/></g>')
    for i, xx in enumerate([60, 140, 220]):
        o.append(f'<path d="M{xx-12} {276+i%2*4} h24" stroke="#cbb9c4" stroke-width="3" opacity=".25"/>')
    for k in range(4):
        o.append(f'<path d="M{x-30+k*4} {272+k*14} h{60-k*12}" stroke="{AMBER}" stroke-width="4" stroke-linecap="round" opacity="{.7-k*.13:.2f}"/>')
    o.append(grain(p)); return ''.join(o)

def s_concrete(p):
    o = [defs(p), bg('#e6d4e0')]
    o.append(f'<rect x="-10" y="250" width="428" height="130" fill="{K["mid"]}"/>')
    o.append(f'<g filter="{sh(p)}"><path d="M30 196 L378 196 L390 214 L18 214Z" fill="#8a6d4a"/><rect x="36" y="214" width="10" height="110" fill="#6e5538"/><rect x="362" y="214" width="10" height="110" fill="#6e5538"/></g>')
    # on the right, the things themselves: a red boot, an apple with a bite, a brass key
    o.append(f'<g filter="{sh(p)}"><path d="M236 196 L236 112 L268 112 L270 168 Q296 170 304 188 L304 196Z" fill="{RED}"/><rect x="232" y="106" width="40" height="10" fill="#7a1f16"/></g>')
    o.append(f'<g filter="{sh(p)}"><path d="M330 196 a22 22 0 1 1 30 -20 a8 8 0 0 0 -4 14 a22 22 0 0 1 -26 6Z" fill="#7a9a3c"/><path d="M340 156 q2 -10 8 -12" stroke="#4e3520" stroke-width="3" fill="none"/></g>')
    o.append(f'<g filter="{sh(p,2)}"><circle cx="190" cy="186" r="9" fill="none" stroke="#9a6a14" stroke-width="5"/><rect x="199" y="183" width="30" height="6" fill="#9a6a14"/><rect x="220" y="189" width="5" height="7" fill="#9a6a14"/><rect x="212" y="189" width="4" height="5" fill="#9a6a14"/></g>')
    # on the left, the same shelf lost in fog: vague, nothing to hold
    for k, (x, y, rx, ry) in enumerate([(60, 160, 40, 30), (120, 172, 34, 22), (40, 110, 70, 44), (130, 80, 80, 50), (170, 150, 60, 50), (60, 230, 90, 30)]):
        o.append(f'<path d="{blob(x,y,rx,ry,180+k,20,2)}" fill="#f4ecf2" opacity=".82"/>')
    o.append(f'<path d="M80 196 L80 150 L100 150 L100 196Z" fill="#c9a8bf" opacity=".5"/>')
    o.append(grain(p)); return ''.join(o)

def s_bodyknows(p):
    o = [defs(p), figdefs(p), bg('#d9c3d3')]
    o.append(f'<path d="{band(wave(220,6,5,1),seed=190)}" fill="{K["light"]}" filter="{sh(p,2)}"/>')
    o.append(f'<rect x="-10" y="300" width="428" height="80" fill="{K["mid"]}"/>')
    o.append(f'<g filter="{sh(p)}"><rect x="90" y="238" width="240" height="12" fill="#6e5538"/><rect x="100" y="250" width="8" height="52" fill="#5a4630"/><rect x="312" y="250" width="8" height="52" fill="#5a4630"/><rect x="90" y="196" width="240" height="10" fill="#6e5538"/><rect x="100" y="206" width="6" height="32" fill="#5a4630"/><rect x="314" y="206" width="6" height="32" fill="#5a4630"/></g>')
    # an unopened letter beside her; her whole body is waiting
    o.append(f'<g filter="{sh(p,2)}"><rect x="262" y="224" width="40" height="15" fill="{CREAM}" transform="rotate(-6 282 232)"/></g>')
    o.append(f'<path d="M263 226 l19 7 l19 -9" fill="none" stroke="{K["mid"]}" stroke-width="1.6" transform="rotate(-6 282 232)"/>')
    o.append(person(186, 302, 168, K['dark'], 'hunch', p=p))
    o.append(f'<path d="M232 274 q8 -6 14 0 M234 262 q8 -6 14 0" fill="none" stroke="{K["dark"]}" stroke-width="3" stroke-linecap="round"/>')
    o.append(grain(p)); return ''.join(o)

SCENES = {
 'domino': s_domino, 'northstar': s_northstar, 'misbelief': s_misbelief, 'frictive': s_frictive,
 'kisho': scene_kisho, 'mindseye': s_mindseye, 'disclosure': s_disclosure, 'afterstorm': s_afterstorm,
 'residue': s_residue, 'retro': s_retro, 'status': s_status, 'honne': s_honne,
 'anchor': scene_anchor, 'hunger': s_hunger, 'friction': s_friction, 'microtension': s_microtension,
 'worlddetail': s_worlddetail, 'interior': s_interior, 'stakes': s_stakes, 'turnshift': s_turnshift,
 'suitcase': s_suitcase, 'camera': scene_camera, 'thread': s_thread, 'stock': s_stock,
 'toofast': s_toofast, 'dump': s_dump,
 'fourth': s_fourth, 'strange': scene_strange, 'concrete': s_concrete, 'bodyknows': s_bodyknows,
}
ORDER = list(SCENES.keys())
