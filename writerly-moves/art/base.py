import random, json, math, os
OUT='/home/claude/canvas/project'
W,H=408,600; AH=350  # artboard incl. 0.125in bleed (12px); art height
INK='#1b1712'; CREAM='#f4ecdc'
G={
 'Core Craft':        dict(dark='#23305a',mid='#3d5191',light='#8fa2d6',tint='#e4e8f4',glyph='circle'),
 'Workshop Diagnostic':dict(dark='#1f4a3e',mid='#2f6f5c',light='#8cc0a8',tint='#e2efe7',glyph='square'),
 'Drafty Air':        dict(dark='#7a2e14',mid='#b4502a',light='#e8a27c',tint='#f7e5d9',glyph='triangle'),
 'Cliché Clinic':     dict(dark='#4a2346',mid='#7a3c72',light='#c792bd',tint='#f1e3ee',glyph='diamond'),
}
def glyph(kind,color,s=14):
    h=s/2
    if kind=='circle': return f'<circle cx="{h}" cy="{h}" r="{h-1}" fill="{color}"/>'
    if kind=='square': return f'<rect x="1" y="1" width="{s-2}" height="{s-2}" fill="{color}"/>'
    if kind=='triangle': return f'<path d="M{h} 1 L{s-1} {s-1} L1 {s-1}Z" fill="{color}"/>'
    return f'<path d="M{h} 0 L{s} {h} L{h} {s} L0 {h}Z" fill="{color}"/>'
def gsvg(kind,color,s=14):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 {s} {s}" aria-hidden="true" style="flex: 0 0 auto">{glyph(kind,color,s)}</svg>'

def wob(pts,amp=1.6,seed=1,steps=3):
    r=random.Random(seed); out=[]
    n=len(pts)
    for i in range(n):
        x1,y1=pts[i]; x2,y2=pts[(i+1)%n]
        for k in range(steps):
            t=k/steps; x=x1+(x2-x1)*t; y=y1+(y2-y1)*t
            if k: x+=r.uniform(-amp,amp); y+=r.uniform(-amp,amp)
            out.append((x,y))
    return 'M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in out)+'Z'
def band(top_pts,bottom=None,seed=1,amp=1.4):
    b=bottom if bottom is not None else 380
    pts=top_pts+[(top_pts[-1][0],b),(top_pts[0][0],b)]
    return wob(pts,amp,seed,2)
def wave(y,amp,n,phase=0,x0=-10,x1=418):
    pts=[]
    for i in range(n+1):
        x=x0+(x1-x0)*i/n; pts.append((x,y+amp*math.sin(i*1.3+phase)))
    return pts

def defs(p):
    return f'''<defs>
<filter id="{p}sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="1.5" dy="4" stdDeviation="3" flood-color="#000" flood-opacity=".38"/></filter>
<filter id="{p}sh2" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="1" dy="2.5" stdDeviation="1.8" flood-color="#000" flood-opacity=".32"/></filter>
<filter id="{p}gr" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="4" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
</defs>'''
def grain(p,op=.09):
    return f'<rect x="-10" y="-60" width="428" height="440" filter="url(#{p}gr)" opacity="{op}" style="mix-blend-mode: multiply"/>'

