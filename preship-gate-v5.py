#!/usr/bin/env python3
"""
Tight Spiral Productions preship gate v5 - the single type & contrast gate.
Enforces studio-type-contrast-standard.md v1.0 by arithmetic.
Supersedes preship-contrast-gate.py, preship-gate-v3.py, preship-gate-v4.py.

Usage:
  preship-gate-v5.py <file.html>      # one file; exit 0 = SHIP, 1 = HALT
  preship-gate-v5.py --sweep [dir]    # every .html under dir; scorecard; exit 1 if any HALT

Checks (each maps to a clause in the standard):
  FONT   font-size < 18px anywhere a human reads text            (clause 1)
  TAP    interactive min-height/min-width < 44px                 (clause 2)
  CON    co-occurring text/bg token pair < 7:1 (4.5:1 if large)  (clause 4)
  DARK   measured dark path: prefers-color-scheme or color-scheme:dark (clause 5)
  HOST   external font/style host (offline violation)            (clause 6)
  EMOJI  pictographic emoji codepoint (not arrows/shapes/box-drawing) (studio law)
"""
import sys, re, os, glob

def _lin(c):
    c/=255.0
    return c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
def _lum(rgb):
    r,g,b=rgb
    return 0.2126*_lin(r)+0.7152*_lin(g)+0.0722*_lin(b)
def ratio(a,b):
    la,lb=_lum(a),_lum(b)
    hi,lo=max(la,lb),min(la,lb)
    return (hi+0.05)/(lo+0.05)
def hexrgb(h):
    h=h.strip().lstrip('#')
    if len(h)==3: h=''.join(c*2 for c in h)
    if len(h)==8: h=h[:6]
    try: return (int(h[0:2],16),int(h[2:4],16),int(h[4:6],16))
    except: return None

def palettes(css):
    out={'default':{},'warm':{}}
    root=re.search(r':root\s*\{([^}]*)\}',css,re.S)
    if root:
        for m in re.finditer(r'(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,8})',root.group(1)):
            out['default'][m.group(1)]=m.group(2)
    warm=re.search(r'body\.warm\s*\{([^}]*)\}',css,re.S)
    if warm:
        out['warm']=dict(out['default'])
        for m in re.finditer(r'(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,8})',warm.group(1)):
            out['warm'][m.group(1)]=m.group(2)
    return out

REAL_PAIRS=[('--ink','--paper'),('--ink2','--paper'),('--ink','--card'),
            ('--ink2','--card'),('--band-ink','--band'),('--ink','--shade')]

def check_contrast(pal, name, halts):
    for fg,bg in REAL_PAIRS:
        if fg in pal and bg in pal:
            rgb_fg,rgb_bg=hexrgb(pal[fg]),hexrgb(pal[bg])
            if rgb_fg and rgb_bg:
                r=ratio(rgb_fg,rgb_bg)
                if r<7.0:
                    halts.append(f"CON [{name}] {fg} on {bg} = {r:.2f}:1 < 7:1 body floor")

def check_fonts(css, halts):
    for m in re.finditer(r'font(?:-size)?\s*:\s*[^;{}]*?(\d+(?:\.\d+)?)px',css):
        px=float(m.group(1))
        if px<18.0:
            halts.append(f"FONT {px:g}px < 18px floor")

def check_taps(css, halts):
    for m in re.finditer(r'(min-height|min-width)\s*:\s*(\d+(?:\.\d+)?)px',css):
        px=float(m.group(2))
        if px<44.0:
            halts.append(f"TAP {m.group(1)} {px:g}px < 44px floor")

def check_dark(html, halts):
    if re.search(r'prefers-color-scheme', html) or re.search(r'color-scheme\s*:\s*dark', html):
        return
    halts.append("DARK no measured dark path (no prefers-color-scheme / color-scheme:dark)")

def check_host(html, halts):
    for m in re.finditer(r'<link[^>]+href="(https?://[^"]+)"',html):
        if 'font' in m.group(1).lower() or 'css' in m.group(1).lower():
            halts.append(f"HOST external style/font: {m.group(1)[:50]}")
    if 'fonts.googleapis' in html or 'fonts.gstatic' in html:
        halts.append("HOST Google Fonts reference")

def check_emoji(html, halts):
    for ch in html:
        o=ord(ch)
        if (0x1F000<=o<=0x1FAFF) or (0x2600<=o<=0x26FF) or (0x2700<=o<=0x27BF) or o==0xFE0F:
            halts.append(f"EMOJI codepoint U+{o:04X}")
            break

def gate(path):
    html=open(path,encoding='utf-8',errors='replace').read()
    css=' '.join(re.findall(r'<style[^>]*>(.*?)</style>',html,re.S)) or html
    halts=[]
    check_fonts(css,halts)
    check_taps(css,halts)
    pal=palettes(css)
    check_contrast(pal['default'],'default',halts)
    if pal['warm']: check_contrast(pal['warm'],'warm',halts)
    check_dark(html,halts)
    check_host(html,halts)
    check_emoji(html,halts)
    seen=set(); uniq=[h for h in halts if not (h in seen or seen.add(h))]
    return uniq

def main():
    args=sys.argv[1:]
    if args and args[0]=='--sweep':
        root=args[1] if len(args)>1 else '.'
        files=sorted(glob.glob(os.path.join(root,'**','*.html'),recursive=True))
        any_halt=False; rows=[]
        for f in files:
            h=gate(f)
            classes=sorted(set(x.split()[0] for x in h))
            status='SHIP' if not h else 'HALT:'+','.join(classes)
            if h: any_halt=True
            rows.append((status,f,len(h)))
        w=max(len(r[0]) for r in rows)
        for status,f,n in rows:
            print(f"{status:<{w}}  {os.path.basename(f):<42} {n if n else ''}")
        print(f"\n{sum(1 for r in rows if r[0]=='SHIP')}/{len(rows)} SHIP")
        sys.exit(1 if any_halt else 0)
    if not args:
        print("usage: preship-gate-v5.py <file.html> | --sweep [dir]"); sys.exit(2)
    h=gate(args[0])
    if not h:
        print(f"SHIP  {args[0]}  (0 halts)"); sys.exit(0)
    print(f"HALT  {args[0]}  ({len(h)} halts):")
    for x in h: print("   "+x)
    sys.exit(1)

if __name__=='__main__':
    main()
