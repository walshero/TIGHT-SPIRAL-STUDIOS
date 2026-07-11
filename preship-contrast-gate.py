#!/usr/bin/env python3
# ══════════════════════════════════════════════════════════════════
# STUDIO EYES — PRE-SHIP CONTRAST GATE   (Tight Spiral Productions)
# Locked 2026-07-10. The tool the studio was missing: contrast is no
# longer eyeballed or run-on-request. This RUNS before every ship.
#
#   python3 preship-contrast-gate.py <file.html>
#   exit 0 = PASS (safe to present)   exit 1 = HALT (do not ship)
#
# It answers the two questions that let "white and yellow" ship:
#   1. Does every TEXT/SURFACE pair clear the floor in EVERY comfort mode?
#      (WCAG: 4.5 body / 3.0 large / target 7.0 AAA)
#   2. Does any token do DOUBLE DUTY — used as text AND as decoration?
#      (the root cause today: --glow was room-light AND caption text)
#
# Light may be dim. Text may not. This gate enforces that line.
# ══════════════════════════════════════════════════════════════════
import re, sys

AA_BODY, AA_LARGE, AAA = 4.5, 3.0, 7.0

def hex2rgb(h):
    h=h.lstrip('#')
    if len(h)==3: h=''.join(c*2 for c in h)
    if len(h)!=6: return None
    try: return tuple(int(h[i:i+2],16) for i in (0,2,4))
    except ValueError: return None

def lum(rgb):
    def f(c):
        c/=255; return c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(rgb[0])+0.7152*f(rgb[1])+0.0722*f(rgb[2])

def ratio(a,b):
    la,lb=lum(a),lum(b); hi,lo=max(la,lb),min(la,lb)
    return (hi+0.05)/(lo+0.05)

# ── extract :root and each html[data-comfort="X"] token block ──────
def token_blocks(css):
    """Return {mode: {var: hexvalue}} merging :root then mode overrides."""
    def grab(selector):
        m=re.search(re.escape(selector)+r'\s*\{([^}]*)\}', css)
        if not m: return {}
        return dict(re.findall(r'(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})', m.group(1)))
    root=grab(':root')
    modes={'default':dict(root)}
    for mode in re.findall(r'html\[data-comfort="([\w-]+)"\]', css):
        blk=grab(f'html[data-comfort="{mode}"]')
        merged=dict(root); merged.update(blk); modes[mode]=merged
    return modes

# ── classify each token by how it's USED in the file ───────────────
# text-role  : appears in `color:` or is named --ink/--label/--accent-ink
# deco-role  : appears in background/border/fill/box-shadow/gradient/stroke
def token_roles(css, html):
    """Role is read PER DECLARATION (split on ;), not per line — so a rule with
    `color:var(--ink); border-color:var(--rule)` tags --ink text and --rule deco,
    never both to both."""
    text_use, deco_use = set(), set()
    decls = re.split(r'[;{}]', css)
    for d in decls:
        d=d.strip()
        # a declaration is `prop: value`
        m=re.match(r'([\w-]+)\s*:\s*(.*)', d, re.S)
        if not m: continue
        prop, val = m.group(1).lower(), m.group(2)
        vars_in = re.findall(r'var\((--[\w-]+)\)', val)
        if not vars_in: continue
        if prop == 'color':
            for v in vars_in: text_use.add(v)
        elif prop in ('background','background-color','background-image','border','border-color',
                      'box-shadow','fill','stroke','outline','outline-color') or 'gradient' in val:
            for v in vars_in: deco_use.add(v)
    return text_use, deco_use

# ── surfaces text lands on, mapped to the text tokens that ACTUALLY sit
#    on them. Body text never lands on --accent (buttons use --accent-ink),
#    so testing --ink on --accent is a false alarm. Pair explicitly. ──
SURFACE_TEXT = {
    '--paper':    ['--ink','--ink-dim','--label','--brake-ink','--pull-ink'],
    '--wall':     ['--ink','--ink-dim','--label','--brake-ink','--pull-ink'],
    '--wall-lit': ['--ink','--ink-dim','--label','--brake-ink','--pull-ink'],
    '--accent':   ['--accent-ink'],   # button surface: only its own ink rides here
}
TEXT_VARS = ['--ink','--ink-dim','--label','--accent-ink','--brake-ink','--pull-ink']

def run(path):
    html=open(path,encoding='utf-8',errors='replace').read()
    css=''.join(re.findall(r'<style[^>]*>(.*?)</style>', html, re.S))
    modes=token_blocks(css)
    text_use, deco_use = token_roles(css, html)

    halts, warns, rows = [], [], []

    # ── CHECK 1: WCAG per mode, each surface × the text tokens that ride it ──
    for mode, tok in modes.items():
        for sv, texts in SURFACE_TEXT.items():
            if sv not in tok: continue
            srgb=hex2rgb(tok[sv])
            if not srgb: continue
            for tv in texts:
                if tv not in tok: continue
                trgb=hex2rgb(tok[tv])
                if not trgb: continue
                r=ratio(trgb,srgb)
                tag = 'AAA' if r>=AAA else ('AA' if r>=AA_BODY else 'FAIL')
                rows.append((mode,tv,sv,round(r,2),tag))
                if r < AA_BODY:
                    halts.append(f"H-CONTRAST [{mode}] {tv} on {sv} = {r:.2f} (< {AA_BODY})")

    # ── CHECK 2: dual-role tokens (text riding a decorative color) ──
    # a token used BOTH as color: and as background/fill/gradient is the bug.
    for t in sorted(text_use & deco_use):
        # --accent legitimately backs buttons with --accent-ink on top; allow that pair
        if t in ('--accent',):  # button surface, ink rides separate token
            continue
        halts.append(f"H-DUALROLE {t} is used as BOTH text (color:) and decoration "
                     f"(bg/fill/gradient). Light may be dim; text may not. Split the token.")

    # ── CHECK 3: no pure white/black as a token value in dark modes ──
    for mode,tok in modes.items():
        for v,hx in tok.items():
            rgb=hex2rgb(hx)
            if rgb==(255,255,255): warns.append(f"[{mode}] {v} is pure #fff (floor: never pure white)")
            if rgb==(0,0,0):       warns.append(f"[{mode}] {v} is pure #000 (floor: never pure black)")

    # ── REPORT ─────────────────────────────────────────────────────
    print(f"\n  STUDIO EYES · PRE-SHIP CONTRAST GATE — {path.split('/')[-1]}")
    print("  " + "─"*58)
    modes_seen=sorted(modes)
    print(f"  modes: {', '.join(modes_seen)}   text tokens: {', '.join(t for t in TEXT_VARS if any(t in modes[m] for m in modes))}")
    print("  " + "─"*58)
    worst={}
    for mode,tv,sv,r,tag in rows:
        worst[mode]=min(worst.get(mode,99), r)
    for mode in modes_seen:
        if mode in worst:
            v=worst[mode]; mark='OK ' if v>=AA_BODY else 'HALT'
            print(f"  [{mark}] {mode:<8} worst text/surface pair = {v:.2f}")
    if halts:
        print("\n  ✗ HALT — do not ship:")
        for h in halts: print("     "+h)
    if warns:
        print("\n  ! warnings:")
        for w in warns: print("     "+w)
    if not halts:
        print("\n  ✓ PASS — every text/surface pair clears the floor in every mode.")
    print()
    return 1 if halts else 0

if __name__=='__main__':
    if len(sys.argv)<2:
        print("usage: python3 preship-contrast-gate.py <file.html>"); sys.exit(2)
    sys.exit(run(sys.argv[1]))
