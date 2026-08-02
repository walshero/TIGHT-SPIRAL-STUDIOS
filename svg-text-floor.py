#!/usr/bin/env python3
"""
STUDIO EYES - SVG TEXT FLOOR TOOTH  v1
Tight Spiral Productions

WHY THIS EXISTS:
  table-four.html passed preship-contrast-gate v2 and preship-gate v3 at exit 0,
  worst text pair 6.38:1, ink-on-paper 17.86:1. The founder then could not read
  the labels. Both gates were right and both gates were useless, because
  neither one knows that SVG text does not render at its declared size.

  A <text font-size="3.4"> inside viewBox="0 0 100 66" is 3.4 USER UNITS.
  On a phone that svg is about 330 css px wide, so one unit is 3.3px and the
  glyph paints at 11.2px. The CSS font floor is 18px absolute / 20px body.
  Contrast arithmetic cannot see this. Only scale arithmetic can.

  This is the same failure shape as your-rp-world.html: the token claimed
  13.23:1 and the device painted 1.17:1. The gate certifies declarations.
  The eye reads pixels. Measure pixels.

FLOOR:
  RENDER_W = 330  -- a 360px phone viewport, less 24px scene padding and
                     6px of border. The narrowest real surface in the corpus.
  MIN_PX   = 18   -- founder floor, absolute, all text everywhere.

  required units = MIN_PX / (RENDER_W / viewBox_width)
                 = 5.45 units at viewBox width 100

exit 0 = ship.  exit 1 = HALT.
"""
import re, sys

RENDER_W = 330
MIN_PX   = 18.0

def scan(path):
    html = open(path, encoding='utf-8', errors='replace').read()

    # DISCRIMINATOR: "font-size:" is CSS and measured in px.
    #                "font-size=" is an SVG attribute and measured in USER UNITS.
    # That holds whether the attribute is static markup or emitted by script into
    # an svg, which is why v1's <svg>...</svg> span walk was wrong: the script
    # block sits after </svg> in source order, so every generated label escaped.
    widths = [float(m.group(1)) for m in re.finditer(
        r'viewBox\s*=\s*"\s*[\d.-]+\s+[\d.-]+\s+([\d.]+)\s+([\d.]+)\s*"', html, re.I)]
    if not widths:
        print('  no svg with a viewBox - nothing to scale-check')
        return []

    vw  = max(widths)          # widest viewBox = fewest px per unit = worst case
    ppu = RENDER_W / vw
    need = MIN_PX / ppu

    print('  STUDIO EYES - SVG TEXT FLOOR - ' + path)
    print('  narrowest render width ' + str(RENDER_W) + 'px   floor ' + str(MIN_PX) + 'px')
    print('  viewBox widths seen: ' + ', '.join(str(w) for w in sorted(set(widths))) +
          '  -> worst case ' + str(vw))
    print('  1 unit = ' + format(ppu, '.2f') + 'px; svg text needs >= ' +
          format(need, '.2f') + ' units')
    print('  ' + '-' * 58)

    seen = {}
    for f in re.finditer(r'font-size\s*=\s*\\?["\']([\d.]+)\\?["\']', html):
        u = float(f.group(1))
        seen[u] = seen.get(u, 0) + 1
    if not seen:
        print('     (no svg text attributes found)')
        return []

    halts = []
    for u in sorted(seen):
        px = u * ppu
        ok = px >= MIN_PX
        print('     font-size ' + format(u, '>5') + ' units x' + str(seen[u]) +
              ' = ' + format(px, '5.1f') + 'px  ' + ('ok' if ok else 'FAIL'))
        if not ok:
            halts.append('H-SVG-TEXT-FLOOR font-size ' + str(u) + ' renders at ' +
                         format(px, '.1f') + 'px at viewBox width ' + str(vw) +
                         ' on a ' + str(RENDER_W) + 'px surface (floor ' + str(MIN_PX) +
                         '). Raise to >= ' + format(need, '.2f') +
                         ' units or move the label to HTML.')
    return halts

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: svg-text-floor.py <file.html>'); sys.exit(2)
    bad = []
    for p in sys.argv[1:]:
        bad += scan(p)
        print('')
    if bad:
        print('  HALT - do not ship:')
        for b in bad:
            print('     ' + b)
        sys.exit(1)
    print('  SHIP - all svg text clears ' + str(MIN_PX) + 'px at ' + str(RENDER_W) + 'px width')
    sys.exit(0)
