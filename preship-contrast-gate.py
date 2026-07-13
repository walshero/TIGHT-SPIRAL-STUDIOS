#!/usr/bin/env python3
"""
STUDIO EYES · PRE-SHIP CONTRAST GATE  v2
Tight Spiral Productions

WHY v2:
  v1 flagged any token used BOTH as color: and as decoration. That is symmetric.
  The danger is NOT symmetric.
      DECORATIVE token used as TEXT   -> the bug (--glow: dim yellow, unreadable)
      TEXT token used as DECORATION   -> normal CSS (--ink on a border rule)
  v1 therefore HALTed 100% of the corpus and carried zero information.
  A gate that fails everything is a wall, not a gate.

v2 REPLACES THE HEURISTIC WITH ARITHMETIC:
  Every token that appears in a `color:` declaration is TEXT.
  Every TEXT token must clear AA_BODY against every surface it can land on.
  If it can't, HALT with the measured number.
  That catches --glow instantly and clears --ink on a border, because the
  arithmetic knows the difference and the heuristic never could.

  Inversion is real: light text on a dark surface is legitimate. A text token
  passes if it clears the bar on AT LEAST ONE declared surface (its home), and
  we report its worst *usable* pairing. A token that clears NOTHING is dead.
"""
import re, sys, os

AA_BODY = 4.5
AAA     = 7.0

# ── color math ────────────────────────────────────────────────────
def hex2rgb(h):
    h = h.strip().lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    if len(h) != 6:
        return None
    try:
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    except ValueError:
        return None

def lum(rgb):
    def f(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (f(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

# ── token blocks: :root plus every comfort-stop override ──────────
def token_blocks(css):
    def grab(sel):
        m = re.search(re.escape(sel) + r'\s*\{([^}]*)\}', css)
        if not m:
            return {}
        return dict(re.findall(r'(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})', m.group(1)))

    root  = grab(':root')
    modes = {'default': dict(root)}

    # support both conventions in the corpus
    for m in re.findall(r'html\[data-comfort="([\w-]+)"\]', css):
        blk = dict(root); blk.update(grab(f'html[data-comfort="{m}"]'))
        modes[m] = blk
    for m in re.findall(r'body\.([\w-]+)\s*\{', css):
        blk = grab(f'body.{m}')
        if blk:                       # only palette-bearing body classes
            merged = dict(root); merged.update(blk)
            modes[m] = merged
    return modes

# ── role detection, per DECLARATION not per line ──────────────────
TEXT_PROPS = ('color',)
DECO_PROPS = ('background', 'background-color', 'background-image', 'border',
              'border-color', 'border-top', 'border-bottom', 'border-left',
              'border-right', 'box-shadow', 'fill', 'stroke', 'outline',
              'outline-color', 'text-shadow')

def token_roles(css):
    text_use, deco_use, surface_use = set(), set(), set()
    for d in re.split(r'[;{}]', css):
        d = d.strip()
        m = re.match(r'([\w-]+)\s*:\s*(.*)', d, re.S)
        if not m:
            continue
        prop, val = m.group(1).lower(), m.group(2)
        vars_in = re.findall(r'var\((--[\w-]+)', val)
        if not vars_in:
            continue
        if prop in TEXT_PROPS:
            text_use.update(vars_in)
        elif prop in ('background', 'background-color'):
            # a real surface: text can land ON this
            surface_use.update(vars_in)
            deco_use.update(vars_in)
        elif prop in DECO_PROPS or 'gradient' in val:
            deco_use.update(vars_in)
    return text_use, deco_use, surface_use

# ── the check ─────────────────────────────────────────────────────
def run(path):
    html = open(path, encoding='utf-8', errors='replace').read()
    css  = ''.join(re.findall(r'<style[^>]*>(.*?)</style>', html, re.S))
    modes = token_blocks(css)
    text_use, deco_use, surface_use = token_roles(css)

    halts, warns, rows = [], [], []

    for mode, tok in sorted(modes.items()):
        surfaces = {s: hex2rgb(tok[s]) for s in surface_use
                    if s in tok and hex2rgb(tok[s])}
        if not surfaces:
            continue

        for tv in sorted(text_use):
            if tv not in tok:
                continue
            trgb = hex2rgb(tok[tv])
            if not trgb:
                continue

            pairs = {sv: ratio(trgb, srgb) for sv, srgb in surfaces.items()}
            best  = max(pairs.values())
            home  = max(pairs, key=pairs.get)

            if best < AA_BODY:
                # clears NOTHING. This is the --glow bug.
                halts.append(
                    f"H-TEXT-UNREADABLE [{mode}] {tv} clears no surface in this file. "
                    f"Best pairing is {home} at {best:.2f} (needs {AA_BODY}). "
                    f"This token is decoration wearing text's clothes — split it."
                )
            else:
                tag = 'AAA' if best >= AAA else 'AA '
                rows.append((mode, tv, home, round(best, 2), tag))
                # a text token that fails on a surface it plausibly rides
                for sv, r in sorted(pairs.items()):
                    if r < AA_BODY and sv != home:
                        warns.append(f"[{mode}] {tv} on {sv} = {r:.2f} — only safe on {home}")

    # floors: never pure black, never pure white
    for mode, tok in modes.items():
        for v, hx in tok.items():
            rgb = hex2rgb(hx)
            if rgb == (255, 255, 255):
                warns.append(f"[{mode}] {v} is pure #fff (floor: never pure white)")
            if rgb == (0, 0, 0):
                warns.append(f"[{mode}] {v} is pure #000 (floor: never pure black)")

    # ── report ────────────────────────────────────────────────────
    name = os.path.basename(path)
    print()
    print(f"  STUDIO EYES · PRE-SHIP CONTRAST GATE v2 — {name}")
    print("  " + "─" * 58)
    print(f"  modes: {', '.join(sorted(modes))}")
    print(f"  text tokens: {', '.join(sorted(text_use)) or '(none)'}")
    print("  " + "─" * 58)

    for mode, tv, sv, r, tag in rows:
        print(f"  [{tag}] {mode:<10} {tv:<14} on {sv:<12} = {r:>6.2f}")

    if warns:
        print()
        print("  ⚠ warnings:")
        for w in sorted(set(warns)):
            print(f"     {w}")

    print()
    if halts:
        print("  ✗ HALT — do not ship:")
        for h in halts:
            print(f"     {h}")
        print()
        return 1

    worst = min((r for *_, r, _ in rows), default=None)
    if worst is not None:
        print(f"  ✓ SHIP — every text token clears {AA_BODY}. Worst pair = {worst:.2f}")
    else:
        print("  ✓ SHIP — no text tokens to check")
    print()
    return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: preship-contrast-gate.py <file.html> [more.html ...]")
        sys.exit(2)
    sys.exit(max(run(p) for p in sys.argv[1:]))
