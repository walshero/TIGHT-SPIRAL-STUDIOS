#!/usr/bin/env python3
# PRE-SHIP GATE v4 - render-proof teeth
# ------------------------------------------------------------------
# v3 (contrast + flip_check + image_floor + nav_floor) preserved verbatim.
# v4 ADDS, per the 2026-07-16 handoff (a screen passed at 13:1, rendered at 1.17:1):
#   TOOTH 5  opacity_floor  - a full-screen surface must PAINT an opaque bg in
#                             EVERY comfort mode, or light text can land on the
#                             white in-app-browser sheet showing through. This is
#                             the class that was structurally invisible to v3.
#   TOOTH 6  hue_floor      - RP reader: warm-mode TEXT must be COOL near-white at
#                             full strength. Amber/gold is fill/accent only, never
#                             color:. WCAG can pass 13:1 while the retina fails.
# The gate stops trusting the token the author HOPED applied; it reasons about
# whether the surface under that text is proven opaque.
import re, sys, os
AA_BODY = 4.5
AAA     = 7.0

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
def token_blocks(css):
    def grab(sel):
        m = re.search(re.escape(sel) + r'\s*\{([^}]*)\}', css)
        if not m:
            return {}
        return dict(re.findall(r'(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})', m.group(1)))
    root  = grab(':root')
    modes = {'default': dict(root)}
    for m in re.findall(r'body\.([\w-]+)\s*\{', css):
        blk = grab('body.' + m)
        if blk:
            merged = dict(root); merged.update(blk)
            modes[m] = merged
    return modes
TEXT_PROPS = ('color',)
DECO_PROPS = ('background', 'background-color', 'background-image', 'border', 'border-color', 'border-top', 'border-bottom', 'border-left', 'border-right', 'box-shadow', 'fill', 'stroke', 'outline', 'outline-color', 'text-shadow')
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
            surface_use.update(vars_in)
            deco_use.update(vars_in)
        elif prop in DECO_PROPS or 'gradient' in val:
            deco_use.update(vars_in)
    return text_use, deco_use, surface_use
def _lum(rgb):
    def f(c):
        c/=255; return c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
    return .2126*f(rgb[0])+.7152*f(rgb[1])+.0722*f(rgb[2])
def flip_check(modes, text_use, surface_use):
    halts = []
    LIGHT, DARK = 0.5, 0.18
    def band(hx):
        rgb = hex2rgb(hx)
        if not rgb: return None
        L=_lum(rgb)
        return 'light' if L>=LIGHT else ('dark' if L<=DARK else 'mid')
    for tv in sorted(text_use):
        bands = {}
        for mode, tok in modes.items():
            if tv in tok:
                b = band(tok[tv])
                if b: bands[mode] = b
        if len(set(bands.values())) > 1:
            for mode, tok in modes.items():
                tb = bands.get(mode)
                if not tb or tb=='mid': continue
                opp = 'dark' if tb=='light' else 'light'
                has_opp = any(band(tok[s])==opp for s in surface_use if s in tok)
                if not has_opp:
                    halts.append('H-FLIP [' + mode + '] text token ' + tv + ' is ' + tb + ' here but no ' + opp + ' surface exists in this mode - it will render ' + tb + '-on-' + tb + ' (the yellow-on-white class). Give ' + mode + ' a full inverse palette.')
    return halts
def image_floor(html):
    halts, warns = [], []
    body = re.sub(r'<(script|style)[\s\S]*?</\1>', ' ', html, flags=re.I)
    visual = 0
    visual += len(re.findall(r'<img\b', body, re.I))
    visual += len(re.findall(r'<svg\b', body, re.I))
    visual += len(re.findall(r'<picture\b', body, re.I))
    visual += len(re.findall(r'<video\b', body, re.I))
    visual += len(re.findall(r'<canvas\b', body, re.I))
    visual += len(re.findall(r'background-image\s*:', html, re.I))
    screens = len(re.findall(r'class="[^"]*\b(?:stage|screen|slide|scene)\b', body, re.I))
    text = re.sub(r'<[^>]+>', ' ', body)
    text = re.sub(r'&[a-z]+;', ' ', text)
    chars = len(re.sub(r'\s+', ' ', text).strip())
    if screens >= 1 and visual == 0 and chars > 400:
        halts.append('H-IMAGE-FLOOR ' + str(screens) + ' screen-section(s), ' + str(chars) + ' chars of text, and ZERO images/svg/canvas. Founder rule: screens must be >50% image. This is a text-wall - add authored visual or justify the exemption.')
    elif screens >= 3 and visual < screens/2 and chars > 1500:
        warns.append('[image-floor] ' + str(visual) + ' visual element(s) across ' + str(screens) + ' screens, ' + str(chars) + ' chars text - likely under the 50% image floor; verify by eye.')
    return halts, warns
def nav_floor(html):
    halts = []
    body = re.sub(r'<(script|style)[\s\S]*?</\1>', ' ', html, flags=re.I)
    screens = len(re.findall(r'class="[^"]*\b(?:stage|screen|slide|scene)\b', body, re.I))
    toggled = len(re.findall(r'\bclass="[^"]*\bhidden\b', body, re.I))
    view_count = max(screens, toggled + 1 if toggled else 0)
    if view_count < 2:
        return halts
    has_back = bool(re.search(
        r'id=["\']backBtn|class="[^"]*\bback(nav|btn)?\b|aria-label="[^"]*\bback\b'
        r'|onclick="[^"]*(?:goBack|backTo)|>\s*(?:&larr;\s*)?back\b', html, re.I))
    has_home = bool(re.search(
        r'id=["\']homeBtn|class="[^"]*\bhome(nav|btn)?\b|aria-label="[^"]*\b(?:home|start)\b'
        r'|onclick="[^"]*(?:goHome|toHome|homeScreen)|>\s*home\b', html, re.I))
    if not has_back:
        halts.append('H-NAV-BACK multi-screen product has no BACK control (founder rule: back + home on ALL products).')
    if not has_home:
        halts.append('H-NAV-HOME multi-screen product has no HOME control (founder rule: back + home on ALL products).')
    return halts

# ---- TOOTH 5: OPACITY FLOOR ---------------------------------------------
# The bug this exists for: warm ink #f6ecda passed at 13:1 on --paper #151210,
# but --paper never painted opaque over the viewport, so the near-white ink
# landed on the white iOS in-app sheet at 1.17:1. INVISIBLE.
# The check: for any mode whose TEXT is light (near-white), the mode must prove
# a full-viewport OPAQUE dark surface is painted by body (or a full-cover
# ancestor). If body's background in that mode is missing, transparent, or a
# gradient/image only (no opaque solid fallback), the light text is a HALT -
# it is one un-painted div away from landing on white.
def _body_bg_decls(css):
    # returns {mode: raw background value string} for body and body.<mode>
    out = {}
    m = re.search(r'(?:^|[}\s])body\s*\{([^}]*)\}', css)
    if m:
        bm = re.search(r'background(?:-color)?\s*:\s*([^;]+)', m.group(1))
        out['default'] = bm.group(1).strip() if bm else None
    for mode in re.findall(r'body\.([\w-]+)\s*\{', css):
        blk = re.search(r'body\.' + re.escape(mode) + r'\s*\{([^}]*)\}', css)
        if blk:
            bm = re.search(r'background(?:-color)?\s*:\s*([^;]+)', blk.group(1))
            if bm:
                out[mode] = bm.group(1).strip()
    return out
def _resolve_bg_rgb(valstr, tok):
    # resolve a background value to an opaque rgb if it is a solid color;
    # return None if transparent / gradient-only / unresolvable / has alpha.
    if not valstr:
        return None
    v = valstr.strip()
    if 'gradient' in v.lower():
        # gradient with no solid fallback color does not guarantee opaque cover
        # (and even opaque gradients aren't a flat surface to measure text on)
        return None
    if re.search(r'\b(transparent|none)\b', v, re.I):
        return None
    if re.search(r'rgba?\([^)]*,\s*0?\.\d+\s*\)', v):  # explicit alpha < 1
        return None
    mv = re.search(r'var\((--[\w-]+)', v)
    if mv:
        hx = tok.get(mv.group(1))
        return hex2rgb(hx) if hx else None
    mh = re.search(r'#[0-9a-fA-F]{3,6}', v)
    if mh:
        return hex2rgb(mh.group(0))
    return None
def opacity_floor(css, modes, text_use, surface_use):
    # The real class: a mode paints LIGHT body text but the VIEWPORT surface
    # (body's own background) is not a proven-opaque DARK color. Then the light
    # ink can land on the white in-app sheet = the 13:1-passes-1.17:1-renders bug.
    # Precision guard (anti-cry-wolf): a light text token that always sits on an
    # explicit dark surface token (e.g. --paper used only as band-ink on --ink)
    # is NOT this bug - it is only a HALT when the light text has NO dark surface
    # partner anywhere in the mode AND the body bg itself isn't proven dark-opaque.
    halts = []
    LIGHT = 0.5
    bg_decls = _body_bg_decls(css)
    for mode, tok in modes.items():
        raw = bg_decls.get(mode, bg_decls.get('default'))
        bg_rgb = _resolve_bg_rgb(raw, tok)
        body_is_dark_opaque = bg_rgb is not None and _lum(bg_rgb) < 0.5
        # dark surface tokens available in this mode (partners text can sit on)
        dark_surfaces = [s for s in surface_use
                         if s in tok and hex2rgb(tok[s]) and _lum(hex2rgb(tok[s])) < 0.5]
        for tv in sorted(text_use):
            hx = tok.get(tv)
            rgb = hex2rgb(hx) if hx else None
            if not (rgb and _lum(rgb) >= LIGHT):
                continue
            # light text is safe if EITHER the body paints dark-opaque OR the mode
            # offers a dark surface token this text can legitimately land on.
            if body_is_dark_opaque or dark_surfaces:
                continue
            if bg_rgb is None:
                halts.append('H-OPACITY [' + mode + '] light text ' + tv + ' but body has NO proven-opaque dark background in this mode (bg = ' + repr(raw) + ') and no dark surface token to sit on. Light ink can land on the white in-app sheet - the 13:1-passes-1.17:1-renders bug. Give body an opaque solid dark --paper in ' + mode + '.')
            else:
                halts.append('H-OPACITY [' + mode + '] light text ' + tv + ' on a LIGHT body background (lum ' + format(_lum(bg_rgb), '.2f') + ') with no dark surface partner - light-on-light. Fix the surface for ' + mode + '.')
    return halts

# ---- TOOTH 6: RP HUE FLOOR ----------------------------------------------
# Founder's retina, not WCAG. Warm/amber/gold as TEXT smears for an RP reader
# even at 13:1. Warm-mode text must be cool near-white; amber is fill/accent
# only. Flags any text token whose hue is warm (R dominant, B starved) AND
# light. Cool near-white (R~=G~=B) passes; gold (R>G>B, low B) HALTs.
def hue_floor(css, modes, text_use):
    # Founder's retina, not WCAG. Warm/amber/gold as TEXT smears for an RP reader
    # even at 13:1. Warm-mode text must be cool near-white; amber is fill/accent
    # only. HALT on warm near-white used as BODY-size text; WARN (not HALT) when
    # the same token is only used at large display size (>=32px) or on icon
    # glyphs - large amber numerals/glyphs are accent, the role the floor permits.
    halts, warns = [], []
    # for each text token, find the largest font-size it is ever set at (px).
    def max_px_for(tok_name):
        biggest = 0.0
        for m in re.finditer(r'([^{}]+)\{([^}]*)\}', css):
            body = m.group(2)
            if 'color:var(' + tok_name not in body.replace(' ', ''):
                # tolerate spaces: re-check loosely
                if not re.search(r'color\s*:\s*var\(\s*' + re.escape(tok_name), body):
                    continue
            fs = re.search(r'font-size\s*:\s*([\d.]+)px', body)
            if fs:
                biggest = max(biggest, float(fs.group(1)))
            else:
                biggest = max(biggest, 0.0)  # inherited/unknown -> treat as body
        return biggest
    for mode, tok in modes.items():
        for tv in sorted(text_use):
            hx = tok.get(tv)
            rgb = hex2rgb(hx) if hx else None
            if not rgb:
                continue
            r, g, b = rgb
            if _lum(rgb) < 0.5:
                continue
            warm_gap = r - b
            if warm_gap >= 24 and b < 235:
                big = max_px_for(tv) >= 32
                msg = ('text token ' + tv + ' = #' + '%02x%02x%02x' % rgb +
                       ' is WARM near-white (R-B gap ' + str(warm_gap) + '). RP floor: '
                       'warm-mode TEXT must be COOL near-white; amber/gold is fill/accent '
                       'only, never color:.')
                if big:
                    warns.append('[' + mode + '] (large-display only, >=32px) ' + msg + ' Accept only if this token is never body-size text.')
                else:
                    halts.append('H-HUE [' + mode + '] ' + msg + ' Cool this token (raise blue toward R=G=B) or demote it to a decoration token.')
    return halts, warns

def run(path):
    html = open(path, encoding='utf-8', errors='replace').read()
    css  = ''.join(re.findall(r'<style[^>]*>(.*?)</style>', html, re.S))
    modes = token_blocks(css)
    text_use, deco_use, surface_use = token_roles(css)
    halts, warns, rows = [], [], []
    for mode, tok in sorted(modes.items()):
        surfaces = {s: hex2rgb(tok[s]) for s in surface_use if s in tok and hex2rgb(tok[s])}
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
                halts.append('H-TEXT-UNREADABLE [' + mode + '] ' + tv + ' clears no surface. Best ' + home + ' at ' + format(best, '.2f') + ' (needs ' + str(AA_BODY) + '). Split it.')
            else:
                tag = 'AAA' if best >= AAA else 'AA '
                rows.append((mode, tv, home, round(best, 2), tag))
                for sv, r in sorted(pairs.items()):
                    if r < AA_BODY and sv != home:
                        warns.append('[' + mode + '] ' + tv + ' on ' + sv + ' = ' + format(r, '.2f') + ' - only safe on ' + home)
    for mode, tok in modes.items():
        for v, hx in tok.items():
            rgb = hex2rgb(hx)
            if rgb == (255, 255, 255):
                warns.append('[' + mode + '] ' + v + ' is pure #fff')
            if rgb == (0, 0, 0):
                warns.append('[' + mode + '] ' + v + ' is pure #000')
    halts += flip_check(modes, text_use, surface_use)
    halts += nav_floor(html)
    ifh, ifw = image_floor(html)
    halts += ifh
    warns += ifw
    halts += opacity_floor(css, modes, text_use, surface_use)   # TOOTH 5
    hfh, hfw = hue_floor(css, modes, text_use)      # TOOTH 6
    halts += hfh
    warns += hfw
    name = os.path.basename(path)
    print()
    print('  STUDIO EYES - PRE-SHIP GATE v4 (render-proof) - ' + name)
    print('  ' + '-' * 58)
    print('  modes: ' + ', '.join(sorted(modes)))
    print('  text tokens: ' + (', '.join(sorted(text_use)) or '(none)'))
    print('  ' + '-' * 58)
    for mode, tv, sv, r, tag in rows:
        print('  [' + tag + '] ' + mode.ljust(10) + ' ' + tv.ljust(14) + ' on ' + sv.ljust(12) + ' = ' + format(r, '6.2f'))
    if warns:
        print()
        print('  warnings:')
        for w in sorted(set(warns)):
            print('     ' + w)
    print()
    if halts:
        print('  HALT - do not ship:')
        for h in halts:
            print('     ' + h)
        print()
        return 1
    worst = min((r for mode, tv, sv, r, tag in rows), default=None)
    if worst is not None:
        print('  SHIP - every text token clears ' + str(AA_BODY) + ', paints opaque, cools warm-mode ink. Worst pair = ' + format(worst, '.2f'))
    else:
        print('  SHIP - no text tokens to check')
    print()
    return 0
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: preship-gate-v4.py <file.html> [more.html ...]')
        sys.exit(2)
    sys.exit(max(run(p) for p in sys.argv[1:]))
