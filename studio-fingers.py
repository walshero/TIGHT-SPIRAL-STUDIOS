#!/usr/bin/env python3
"""
STUDIO FINGERS - the gate that did not exist.

STUDIO EYES already exists: studio-eyes-sweep.py renders a file and shoots it dark and
light (studio-eyes-shots/*.png), and comfort-gate.py measures real painted contrast in
day / dusk / night. Both answer "can this be SEEN."

Nothing in this repo has ever answered "can this be TOUCHED." A player on a phone holds
the thing one-handed, with a thumb, at arm's length, outdoors. That is the shipping
condition for every game the studio makes, and it was ungated.

WHAT IS LAW AND WHAT IS HOUSE - the distinction that ends the argument
---------------------------------------------------------------------
The studio has four gates carrying four different numbers because nobody wrote down which
numbers are CITED and which are RULED. Every number below is tagged.

  [LAW]   WCAG 2.5.8 Target Size (Minimum), AA        24 x 24 CSS px
  [LAW]   WCAG 2.5.5 Target Size (Enhanced), AAA      44 x 44 CSS px
  [LAW]   WCAG 1.4.11 UI components / graphics        3:1 against adjacent colour
  [CITED] Apple HIG minimum tap target                44 pt
  [CITED] Material Design minimum tap target          48 dp
  [CITED] Gap between adjacent targets                8pt (>=44pt targets),
                                                      12pt (32-44pt targets),
                                                      16pt within 80pt of a screen edge
  [CITED] Comfortable one-thumb reach                 bottom 40% of the screen;
                                                      top-left is a regrip on large phones
  [CITED] Within 16pt of left/right edge              competes with system back-gestures
  [CITED] iOS zooms any input with font-size < 16px   (the classic cowpath tax)

  [HOUSE] TSP ships to a founder with retinitis pigmentosa, so the studio takes the
          STRICTER of Apple and Material and calls it the floor: 48 CSS px.
          A 24px target is legal and it is not ours.

STATIC ONLY, AND IT SAYS SO
---------------------------
Real geometry needs a render. This gate reads source, so it can only decide what source
decides. Anything needing layout is printed NOT COMPUTABLE by name - the same rule
resolve-canon.py uses for blind lanes. A check that quietly skips what it cannot see is
how you get a clean report on a broken screen.

EXIT CODES
    0  clean on every computable check
    1  HALT
    2  usage / unreadable input
"""

import sys, os, re

TARGET_FLOOR   = 48      # [HOUSE] px - stricter of Apple 44 / Material 48
LEGAL_FLOOR    = 24      # [LAW]   px - WCAG 2.5.8 AA
INPUT_FLOOR    = 16      # [CITED] px - below this iOS zooms the viewport on focus
EDGE_GUTTER    = 16      # [CITED] px - system gesture corridor, left/right

INTERACTIVE = re.compile(
    r'<(button|a|input|select|textarea|summary)\b|role="(button|link|tab|switch|checkbox)"', re.I)

DECL = re.compile(r'([-a-z]+)\s*:\s*([^;{}]+)', re.I)
RULE = re.compile(r'([^{}]+)\{([^{}]*)\}')
PX   = re.compile(r'(-?[\d.]+)px')


def px(v):
    m = PX.search(v or "")
    return float(m.group(1)) if m else None


def read(path):
    with open(path, "rb") as f:
        return f.read().decode("utf-8", "replace")


COMMENT = re.compile(r"/\*.*?\*/", re.S)


def css_rules(src):
    """Every rule body in every <style> block. Inline style= is checked separately.

    BUG FOUND 2026-08-07 on the first real run, against Flok: comments were not stripped,
    so a rule preceded by `/* ... BOTTOM NAV RAIL ... */` carried the comment INTO its
    selector string, matched the interactive test on the word 'nav', and manufactured two
    [LAW] halts against `.se-updated` (a date stamp) and `html.big` (a root class).
    Neither is a target. That is a gate crying wolf on its very first run - the exact
    defect this gate was written to replace. Strip comments before you parse.
    """
    out = []
    for style in re.findall(r"<style[^>]*>(.*?)</style>", src, re.S | re.I):
        style = COMMENT.sub(" ", style)
        for sel, body in RULE.findall(style):
            sel = " ".join(sel.split())
            if sel.startswith("@"):
                continue
            out.append((sel, body))
    return out


def looks_interactive(sel):
    s = sel.lower()
    return bool(re.search(r'\b(button|a|input|select|textarea|summary)\b', s) or
                re.search(r'(btn|tap|touch|click|control|toggle|nav|key|pad|chip|pill|'
                          r'\bcta\b|corner|switch)', s))


def check(path):
    src = read(path)
    halts, notes, notcomp = [], [], []

    # ---- VIEWPORT ------------------------------------------------------------------
    vp = re.search(r'<meta[^>]+name=["\']viewport["\'][^>]*>', src, re.I)
    if not vp:
        halts.append("VIEWPORT  no <meta name=viewport>. On a phone the page renders at "
                     "980px and every target shrinks below any floor. This is the single "
                     "highest-value line in a mobile build.")
    else:
        tag = vp.group(0)
        if re.search(r'user-scalable\s*=\s*(no|0)', tag, re.I):
            halts.append("VIEWPORT  user-scalable=no forbids pinch-zoom. That is the one "
                         "magnifier a low-vision player has. Never ship it.")
        m = re.search(r'maximum-scale\s*=\s*([\d.]+)', tag, re.I)
        if m and float(m.group(1)) < 2:
            halts.append(f"VIEWPORT  maximum-scale={m.group(1)} caps zoom below 2x. "
                         f"Same failure as user-scalable=no, wearing a number.")
        if "width=device-width" not in tag.replace(" ", ""):
            halts.append("VIEWPORT  missing width=device-width.")

    # ---- TARGETS -------------------------------------------------------------------
    sized, unsized = [], []
    for sel, body in css_rules(src):
        if not looks_interactive(sel):
            continue
        d = {k.strip().lower(): v.strip() for k, v in DECL.findall(body)}
        h = px(d.get("min-height") or d.get("height") or "")
        w = px(d.get("min-width") or d.get("width") or "")
        pad = px(d.get("padding") or "") or 0
        fs = px(d.get("font-size") or "")
        # A target with padding and a line box is plausibly tall enough; source cannot
        # prove it. Only DECLARED height is decidable here.
        eff = h if h is not None else (None if fs is None else fs + 2 * pad)
        if eff is None:
            unsized.append(sel)
            continue
        sized.append((sel, eff, w))
        if eff < LEGAL_FLOOR:
            halts.append(f"TARGET    {sel}  ~{eff:g}px tall  < {LEGAL_FLOOR}px WCAG 2.5.8 AA floor [LAW]")
        elif eff < TARGET_FLOOR:
            halts.append(f"TARGET    {sel}  ~{eff:g}px tall  < {TARGET_FLOOR}px studio floor [HOUSE] "
                         f"(legal at 24, but this studio ships to RP eyes and RP thumbs)")

    # ---- INPUT ZOOM TAX ------------------------------------------------------------
    for sel, body in css_rules(src):
        if not re.search(r'\b(input|select|textarea)\b', sel, re.I):
            continue
        fs = px(dict((k.strip().lower(), v.strip()) for k, v in DECL.findall(body)).get("font-size", ""))
        if fs is not None and fs < INPUT_FLOOR:
            halts.append(f"INPUT     {sel}  font-size {fs:g}px < {INPUT_FLOOR}px. iOS will zoom the "
                         f"whole viewport on focus and never zoom back. [CITED]")

    # ---- EDGE GUTTER ---------------------------------------------------------------
    if not re.search(r'env\(\s*safe-area-inset', src):
        notes.append("EDGE      no env(safe-area-inset-*) anywhere. On a notched phone the "
                     "bottom bar and the home indicator will overlap. [CITED]")

    # ---- THUMB REACH ---------------------------------------------------------------
    if not re.search(r'(position\s*:\s*fixed[^}]*bottom|bottom\s*:\s*0)', src, re.I):
        notes.append("REACH     nothing is pinned to the bottom of the screen. The "
                     "comfortable one-thumb arc is the bottom 40%; top-left is a regrip. "
                     "If the primary action lives up top, the player is stretching. [CITED]")

    # ---- WHAT SOURCE CANNOT DECIDE -------------------------------------------------
    if unsized:
        notcomp.append(f"{len(unsized)} interactive selector(s) declare no height and no "
                       f"font-size, so their rendered box is NOT COMPUTABLE from source. "
                       f"Render them: {', '.join(sorted(set(unsized))[:6])}"
                       + (" ..." if len(set(unsized)) > 6 else ""))
    notcomp.append("Gap between adjacent targets (8/12/16pt [CITED]) needs laid-out "
                   "positions. NOT COMPUTABLE statically.")
    notcomp.append("Whether the primary action falls inside the bottom-40% thumb arc "
                   "needs a viewport. NOT COMPUTABLE statically.")

    # ---- REPORT --------------------------------------------------------------------
    name = os.path.basename(path)
    print("=" * 74)
    print(f"STUDIO FINGERS  {name}")
    print("=" * 74)
    if halts:
        print(f"\n## HALT  [{len(halts)}]")
        for h in halts:
            print("  " + h)
    else:
        print("\n## HALT  [0]\n   (clean on every computable check)")
    if notes:
        print(f"\n## COWPATH  [{len(notes)}]")
        print("   Conventional phone patterns this file does not follow. Not illegal.")
        for n in notes:
            print("  " + n)
    print(f"\n## NOT COMPUTABLE FROM SOURCE  [{len(notcomp)}]")
    print("   Named, not skipped. Silence is never agreement.")
    for n in notcomp:
        print("  " + n)
    print(f"\n   targets measured: {len(sized)}   targets undecidable: {len(set(unsized))}")
    print("=" * 74)
    return 1 if halts else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        print("  studio-fingers.py <file.html> [more.html ...]")
        sys.exit(2)
    rc = 0
    for p in sys.argv[1:]:
        if not os.path.exists(p):
            print(f"HALT - not found: {p}")
            rc = max(rc, 2)
            continue
        rc = max(rc, check(p))
    sys.exit(rc)
