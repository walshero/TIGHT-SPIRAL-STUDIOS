#!/usr/bin/env python3
"""
STUDIO EYES - PRE-SHIP GATE  v4
Tight Spiral Productions

v4 REPLACES v3 AND ABSORBS svg-text-floor.py.
Delete both. Three files implementing overlapping teeth is the ~30-rules
problem in script form: when six checks should have caught something and
only the arithmetic one did, the answer is more arithmetic in ONE place.

WHAT v3 GOT WRONG - three holes, all on the dark axis
-----------------------------------------------------
1. prefers-color-scheme appeared ZERO times in preship-contrast-gate.py,
   preship-gate-v3.py and studio-eyes-sweep.py. The palette the operating
   system actually applies had never been measured by anything. C1 checked
   that a color-scheme DECLARATION existed - it verified the promise and
   never the palette. Declaring "light dark" and shipping no dark tokens is
   worse than declaring nothing: it tells the OS not to force-darken, then
   hands it a light palette to render on a dark surface.

2. v3 lost v2's html[data-comfort="x"] parsing. v2 had 2 occurrences, v3 had
   0. Any file using that convention was checked in light mode only and
   printed "modes: default" while a whole second palette sat unread. A
   silent regression is worse than a missing feature because the output
   still looks like a pass.

3. E1 (font floor, 18px absolute / 20px body) was correct and blind. Studio
   Eyes reads sizes off the WeasyPrint box tree, and WeasyPrint treats <svg>
   as a replaced image, so it never builds text boxes for SVG glyphs. A
   <text font-size="3.4"> in viewBox="0 0 100 66" is 3.4 USER UNITS: on a
   330px surface that paints at 11.2px. table-four.html passed both gates at
   exit 0, worst pair 6.38:1, and the founder could not read the labels.
   Same shape as your-rp-world.html: token claimed 13.23:1, device painted
   1.17:1. The gate certifies declarations. The eye reads pixels.

DARK IS NOT OPTIONAL HERE. A file with no dark palette HALTs. Every text
token is measured in every mode, and a mode is any of the four conventions
below - not just the one this month's gate happens to parse.

Studio Eyes keeps the render lens (WeasyPrint, real widths, pixel sampling).
It should CALL floors() from this module rather than reimplement it, so each
tooth has exactly one implementation.

exit 0 = ship.  exit 1 = HALT.
"""
import re, sys, os, json

# ---------- RATCHET ----------
# Founder ruling 2026-07-26: "dark mode ready everywhere" is reached by burning
# down a counted debt, not by freezing the repo. A halt already recorded in the
# baseline for that exact path is DEBT and prints as a warning. A halt NOT in the
# baseline is a REGRESSION and exits 1. A file absent from the baseline is new
# work and is held to the full floor. Debt count prints every run so it cannot
# rot quietly. Ratchet only ever tightens: nothing is added to the baseline by
# the gate itself.
BASELINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gate-baseline.json')

def load_baseline():
    try:
        return json.load(open(BASELINE))
    except Exception:
        return {}

def code_of(halt):
    return halt.split()[0]

AA_BODY, AAA = 4.5, 7.0
FONT_FLOOR_ABS, FONT_FLOOR_BODY = 18.0, 20.0
SVG_RENDER_W = 330.0   # 360px Android viewport less 24px scene padding and 6px border
                       # - the narrowest real surface in the corpus

TEXT_PROPS = ('color',)
DECO_PROPS = ('background', 'background-color', 'background-image', 'border',
              'border-color', 'border-top', 'border-bottom', 'border-left',
              'border-right', 'box-shadow', 'fill', 'stroke', 'outline',
              'outline-color', 'text-shadow')

# ---------- colour arithmetic ----------
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

# ---------- token blocks: ALL FOUR CONVENTIONS ----------
def _decls(block):
    return dict(re.findall(r'(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})', block))

def token_blocks(css):
    """:root  +  @media (prefers-color-scheme: dark)  +  html[data-comfort="x"]
       +  body.x.  v2 knew two of these, v3 knew one, nothing knew the media
       query. Parse all four or the report is a guess."""
    m = re.search(r':root\s*\{([^}]*)\}', css)
    root = _decls(m.group(1)) if m else {}
    modes = {'default': dict(root)}

    # the OS-applied palette. nested braces, so match to the inner :root.
    for mm in re.finditer(
            r'@media[^{]*prefers-color-scheme\s*:\s*dark[^{]*\{\s*:root\s*\{([^}]*)\}', css, re.I):
        blk = dict(root); blk.update(_decls(mm.group(1)))
        modes['os-dark'] = blk

    for name in re.findall(r'html\[data-comfort\s*=\s*"([\w-]+)"\]', css):
        blk = _decls((re.search(r'html\[data-comfort\s*=\s*"' + re.escape(name) + r'"\]\s*\{([^}]*)\}', css) or
                      re.match('', '')).group(1)) if re.search(
                      r'html\[data-comfort\s*=\s*"' + re.escape(name) + r'"\]\s*\{([^}]*)\}', css) else {}
        if blk:
            merged = dict(root); merged.update(blk)
            modes[name] = merged

    for name in re.findall(r'body\.([\w-]+)\s*\{', css):
        mm = re.search(r'body\.' + re.escape(name) + r'\s*\{([^}]*)\}', css)
        blk = _decls(mm.group(1)) if mm else {}
        if blk:
            merged = dict(root); merged.update(blk)
            modes[name] = merged
    return modes

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
            surface_use.update(vars_in); deco_use.update(vars_in)
        elif prop in DECO_PROPS or 'gradient' in val:
            deco_use.update(vars_in)
    return text_use, deco_use, surface_use

# ---------- floors. Studio Eyes should import these, not restate them ----------
def dark_floor(html, css, modes):
    """A file with no dark palette is not dark-mode ready, and one that
       declares color-scheme without a dark palette actively lies to the OS."""
    halts = []
    # two distinct shapes, and v4's first cut only knew one of them:
    #   CSS   ->  color-scheme: light dark
    #   meta  ->  <meta name="color-scheme" content="light dark">
    declares = bool(re.search(r'color-scheme\s*:\s*[^;}]*dark', css, re.I)) or \
               bool(re.search(r'<meta[^>]*name\s*=\s*["\']color-scheme["\'][^>]*'
                              r'content\s*=\s*["\'][^"\']*dark', html, re.I))
    dark_modes = [k for k in modes if k != 'default' and
                  any(h in k.lower() for h in ('dark', 'night', 'dim', 'warmdark'))]
    has_os = 'os-dark' in modes
    if not dark_modes and not has_os:
        halts.append('H-DARK-MISSING no dark palette in any convention (@media '
                     'prefers-color-scheme, html[data-comfort], body.class). Phone OS dark '
                     'mode will force-darken this page and no gate has measured the result.')
    if declares and not has_os:
        halts.append('H-DARK-PROMISE color-scheme declares dark but there is no @media '
                     '(prefers-color-scheme:dark) palette. That tells the OS not to '
                     'force-darken and then hands it light tokens on a dark surface.')
    return halts

def svg_text_floor(html):
    """SVG text is user units, not px. 'font-size:' is CSS and measured in px;
       'font-size=' is an SVG attribute and measured in user units - that
       discriminator holds whether the attribute is static markup or written by
       script, which matters because the script block sits after </svg>."""
    halts = []
    widths = [float(m.group(1)) for m in re.finditer(
        r'viewBox\s*=\s*"\s*[\d.-]+\s+[\d.-]+\s+([\d.]+)\s+([\d.]+)\s*"', html, re.I)]
    if not widths:
        return halts
    vw = max(widths)                 # widest viewBox = fewest px per unit = wor