#!/usr/bin/env python3
"""NUMBER-SENSE GATE - Studio Eyes learns layout + number sense.

Born 2026-08-11 after the founder's phone showed 'Studio $1,750-$2,100 / 1 /
Bedroom $2,400' - a rent line wrapping between a number and its unit at large
text size, and earlier 'Studio null' from an untyped backend column.

Rules, for any page that carries data-rentline elements:
  1. No junk tokens (null/undefined/NaN) in a rent line.
  2. Every unit+price pair is internally unbreakable: within a pair the only
     spaces are non-breaking (U+00A0); line-wrap may occur only at the
     middle-dot separators between pairs.
  3. Every price is well-formed: $X,XXX or a $X,XXX to $X,XXX en-dash range.
     Applies to rent lines and td.price cells on the same page.

Blocks. A number that wraps away from its label is a number the reader loses.
"""
import html
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
PRICE = re.compile(r'^\$\d{1,3},\d{3}(–\$\d{1,3},\d{3})?$')
SPAN = re.compile(r'data-rentline="([^"]+)"[^>]*>(.*?)</span>', re.S)
TDP = re.compile(r'<td class="price">(.*?)</td>', re.S)

halts = []
checked = 0
for f in sorted(root.rglob('*.html')):
    if any(part.startswith('.') or part == 'node_modules' for part in f.parts):
        continue
    src = f.read_text(encoding='utf-8', errors='replace')
    if 'data-rentline' not in src:
        continue
    checked += 1
    rel = f.relative_to(root)
    for key, raw in SPAN.findall(src):
        text = html.unescape(re.sub(r'<[^>]+>', '', raw)).strip()
        if re.search(r'\b(null|undefined|NaN)\b', text, re.I):
            halts.append(f'{rel} [{key}]: junk token in "{text}"')
        if '$' not in text:
            halts.append(f'{rel} [{key}]: no $ anywhere in rent line')
        for pair in text.split(' · '):
            if ' ' in pair:
                halts.append(f'{rel} [{key}]: breakable space inside pair "{pair}"')
            price = pair.split(' ')[-1]
            if not PRICE.match(price):
                halts.append(f'{rel} [{key}]: malformed price "{price}"')
    for raw in TDP.findall(src):
        text = html.unescape(re.sub(r'<[^>]+>', '', raw)).strip()
        if not PRICE.match(text):
            halts.append(f'{rel} td.price: malformed price "{text}"')

if halts:
    print('NUMBER-SENSE HALTS:')
    for h in halts:
        print(' - HALT ' + h)
    sys.exit(1)
print(f'number-sense: {checked} page(s) checked - rent lines coherent, pairs unbreakable, prices well-formed')
