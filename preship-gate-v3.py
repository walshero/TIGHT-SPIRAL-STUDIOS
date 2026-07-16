#!/usr/bin/env python3
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
    screens = len(re.findall(r'class="[^"]*\b(?:stage|screen|slide)\b', body, re.I))
    if screens < 2:
        return halts
    has_back = bool(re.search(r'\bback\b', html, re.I) and re.search(r'id=["\']backBtn|aria-label="[^"]*back|>\s*&larr;\s*back|>\s*back', html, re.I))
    has_home = bool(re.search(r'id=["\']homeBtn|aria-label="[^"]*(?:start|home)|>\s*home\b', html, re.I))
    if not has_back:
        halts.append('H-NAV-BACK multi-screen product has no BACK control (founder rule: back + home on ALL products).')
    if not has_home:
        halts.append('H-NAV-HOME multi-screen product has no HOME control (founder rule: back + home on ALL products).')
    return halts
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
    name = os.path.basename(path)
    print()
    print('  STUDIO EYES - PRE-SHIP GATE v3 - ' + name)
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
        print('  SHIP - every text token clears ' + str(AA_BODY) + '. Worst pair = ' + format(worst, '.2f'))
    else:
        print('  SHIP - no text tokens to check')
    print()
    return 0
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: preship-gate-v3.py <file.html> [more.html ...]')
        sys.exit(2)
    sys.exit(max(run(p) for p in sys.argv[1:]))
