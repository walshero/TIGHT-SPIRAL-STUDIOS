#!/usr/bin/env python3
"""
contrast-plus.py — the two industry checks the WCAG-2.x text gates don't do.
Tight Spiral Productions.

A SECONDARY, advisory lens. The primary render-proof gate stays studio-eyes-sweep.py
(v4). This adds two things the corpus verified were missing (2026-07-27):

  APCA  — the WCAG-3.0-draft Accessible Perceptual Contrast Algorithm. Unlike WCAG 2.x
          (which rewards max contrast and is blind to halation and to polarity/weight),
          APCA is perceptual: it accounts for light-on-dark vs dark-on-light and reports
          a signed Lc. This FORMALIZES the studio's own "never #000 on #fff, max contrast
          blooms" rule — that rule is APCA's whole argument. Reported, never a hard gate:
          WCAG 2.x is still the legal floor; APCA is the second opinion that catches what
          2.x misses (dark mode, thin fonts — exactly where the JS comfort stops live).

  1.4.11 — WCAG 2.x SC 1.4.11 Non-text Contrast (AA): UI components, states, focus
          indicators, and meaningful graphics must clear 3:1. The text gates check text
          only. This checks focus-indicator + border/outline + SVG stroke/fill tokens at
          3:1 against the surfaces they can land on. Token-level (a second opinion; the
          render-proof primary is the sweep) — it is honest about that.

Self-test runs first and REFUSES if its APCA canary does not hit published reference Lc
values (a lens that gates the studio must first gate itself — house rule).

USAGE
    contrast-plus.py --self-test
    contrast-plus.py <file.html> [...]      report APCA + 1.4.11 (exit 0; advisory)
    contrast-plus.py --strict <file.html>   exit 1 if any 1.4.11 non-text pair < 3:1
"""
import re, sys, os

# ---- WCAG 2.x luminance (for the 1.4.11 3:1 ratio) ----
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

def wcag_lum(rgb):
    def f(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (f(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def wcag_ratio(a, b):
    la, lb = wcag_lum(a), wcag_lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

# ---- APCA 0.1.9 (SAPC) Lc ----
# constants per the published APCA 0.1.9 lookup (Myndex/Somers).
_MAIN_TRC = 2.4
_S_TX, _S_BG = 0.57, 0.56           # normal-polarity exponents (text, bg)
_R_TX, _R_BG = 0.62, 0.65           # reverse-polarity exponents
_B_THR, _B_CLIP = 0.022, 1.414      # black soft-clamp
_SCALE = 1.14
_LO_CLIP, _LO_OFFSET = 0.1, 0.027   # low-contrast clamp + offset

def apca_lum(rgb):
    r, g, b = ((c / 255.0) ** _MAIN_TRC for c in rgb)
    return 0.2126729 * r + 0.7151522 * g + 0.0721750 * b

def apca_lc(txt_rgb, bg_rgb):
    """Signed Lc. |Lc| ~ 106 for #000 on #fff; ~ -108 for #fff on #000."""
    ytxt, ybg = apca_lum(txt_rgb), apca_lum(bg_rgb)
    ytxt = ytxt if ytxt > _B_THR else ytxt + (_B_THR - ytxt) ** _B_CLIP
    ybg = ybg if ybg > _B_THR else ybg + (_B_THR - ybg) ** _B_CLIP
    if abs(ybg - ytxt) < 0.0005:
        return 0.0
    if ybg > ytxt:                                  # normal: dark text on light bg
        c = (ybg ** _S_BG - ytxt ** _S_TX) * _SCALE
        sapc = 0.0 if c < _LO_CLIP else c - _LO_OFFSET
    else:                                           # reverse: light text on dark bg
        c = (ybg ** _R_BG - ytxt ** _R_TX) * _SCALE
        sapc = 0.0 if c > -_LO_CLIP else c + _LO_OFFSET
    return round(sapc * 100.0, 1)

# APCA "bronze" use-case minimums (|Lc|): body text 75, large/bold 60, non-text/large 45.
APCA_BODY, APCA_LARGE, APCA_NONTEXT = 75, 60, 45

# ---- token parsing (secondary lens; the render-proof primary is the sweep) ----
def token_blocks(css):
    def grab(sel):
        m = re.search(re.escape(sel) + r'\s*\{([^}]*)\}', css)
        return dict(re.findall(r'(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})', m.group(1))) if m else {}
    root = grab(':root')
    modes = {'default': dict(root)}
    for m in re.findall(r'html\[data-comfort="([\w-]+)"\]', css):
        b = dict(root); b.update(grab(f'html[data-comfort="{m}"]')); modes[m] = b
    for m in re.findall(r'body\.([\w-]+)\s*\{', css):
        b = grab(f'body.{m}')
        if b:
            merged = dict(root); merged.update(b); modes[m] = merged
    return modes

def roles(css):
    text, surface, nontext = set(), set(), set()
    for d in re.split(r'[;{}]', css):
        m = re.match(r'([\w-]+)\s*:\s*(.*)', d.strip(), re.S)
        if not m:
            continue
        prop, val = m.group(1).lower(), m.group(2)
        vs = re.findall(r'var\((--[\w-]+)', val)
        if not vs:
            continue
        if prop == 'color':
            text.update(vs)
        elif prop in ('background', 'background-color'):
            surface.update(vs)
        elif prop in ('outline', 'outline-color', 'border', 'border-color',
                      'border-top', 'border-bottom', 'border-left', 'border-right',
                      'stroke', 'fill'):
            nontext.update(vs)      # 1.4.11: focus rings, borders, meaningful graphics
    return text, surface, nontext

def run(path, strict=False):
    html = open(path, encoding='utf-8', errors='replace').read()
    css = ''.join(re.findall(r'<style[^>]*>(.*?)</style>', html, re.S))
    modes = token_blocks(css)
    text_use, surface_use, nontext_use = roles(css)
    name = os.path.basename(path)
    print()
    print(f"  CONTRAST-PLUS (APCA + WCAG 1.4.11 non-text) - {name}")
    print("  " + "-" * 58)
    hard = 0
    for mode, tok in sorted(modes.items()):
        surfaces = {s: hex2rgb(tok[s]) for s in surface_use if s in tok and hex2rgb(tok[s])}
        if not surfaces:
            continue
        # APCA secondary opinion on text tokens
        for tv in sorted(text_use):
            if tv not in tok or not hex2rgb(tok[tv]):
                continue
            best = max((abs(apca_lc(hex2rgb(tok[tv]), s)) for s in surfaces.values()), default=0)
            flag = "" if best >= APCA_BODY else ("  APCA: below body Lc75 (large-only)" if best >= APCA_LARGE else "  APCA: WEAK (<Lc60)")
            print(f"  [APCA {mode}] {tv}: best |Lc| {best}{flag}")
        # 1.4.11 non-text at 3:1
        for nv in sorted(nontext_use):
            if nv not in tok or not hex2rgb(tok[nv]):
                continue
            best = max((wcag_ratio(hex2rgb(tok[nv]), s) for s in surfaces.values()), default=0)
            if best < 3.0:
                hard += 1
                print(f"  [1.4.11 {mode}] {nv}: best {best:.2f} < 3:1  (focus/border/graphic non-text FAILS AA)")
            else:
                print(f"  [1.4.11 {mode}] {nv}: {best:.2f} >= 3:1  ok")
    print()
    if strict and hard:
        print(f"  HALT (--strict) — {hard} non-text pair(s) below WCAG 1.4.11 (3:1).")
        return 1
    print(f"  report only — APCA is advisory; 1.4.11 has {hard} sub-3:1 pair(s) (use --strict to gate).")
    return 0

def self_test():
    # APCA canary against published reference Lc (Myndex): black-on-white ~106, white-on-black ~-108.
    bw = apca_lc((0, 0, 0), (255, 255, 255))
    wb = apca_lc((255, 255, 255), (0, 0, 0))
    ok = (104 <= bw <= 108) and (-110 <= wb <= -106) and abs(wcag_ratio((0,0,0),(255,255,255)) - 21.0) < 0.5
    if not ok:
        print(f"  SELF-TEST FAIL — APCA canary off (blackOnWhite={bw} want ~106; whiteOnBlack={wb} want ~-108). Do not trust.")
        return 2
    print(f"  SELF-TEST OK — APCA Lc: black/white={bw}, white/black={wb} (match published reference); WCAG ratio math verified.")
    return 0

def main(argv):
    if "--self-test" in argv:
        return self_test()
    if self_test() == 2:
        return 2
    strict = "--strict" in argv
    files = [a for a in argv if a not in ("--strict",)]
    if not files:
        print("usage: contrast-plus.py [--self-test] [--strict] <file.html> ...")
        return 2
    return max((run(f, strict) for f in files), default=0)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
