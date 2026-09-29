#!/usr/bin/env python3
"""
PII-GATE — faculty email addresses do not enter a public repo.

This repo is public and netlify.toml publishes the whole root, so every tracked
file is on the open web. On 2026-09-28 three files carried other people's
@massbay.edu addresses (a faculty roster). They were removed from the tree.
This gate is the check that keeps it from coming back.

Ratchet, same pattern as the other gates: pii-baseline.json records how many
non-allowlisted addresses each file holds today. A new file, or a higher count,
exits 1. Counts may only go down.

    python3 pii-gate.py            check (exit 0 clean, 1 new exposure)
    python3 pii-gate.py --update   rewrite the baseline (only after a deliberate call)

Allowed: the owner's own addresses and role addresses.
"""
import json, os, re, subprocess, sys

ALLOW = re.compile(r'^(mwalsh|litmag|enchair|you)@', re.I)
EMAIL = re.compile(r'[A-Za-z0-9._-]+@(?:post\.)?massbay\.edu', re.I)
BASE = 'pii-baseline.json'

def tracked():
    out = subprocess.run(['git', 'ls-files', '-z'], capture_output=True, check=True).stdout
    return [p for p in out.decode().split('\0') if p and p != BASE]

def scan():
    found = {}
    for p in tracked():
        try:
            raw = open(p, 'rb').read()
        except OSError:
            continue
        if b'\0' in raw[:4096]:
            continue
        hits = {m.group(0).lower() for m in EMAIL.finditer(raw.decode('utf8', 'ignore'))}
        hits = {h for h in hits if not ALLOW.match(h)}
        if hits:
            found[p] = len(hits)
    return found

now = scan()
if '--update' in sys.argv:
    json.dump(now, open(BASE, 'w'), indent=1, sort_keys=True)
    print(f'baseline written: {len(now)} files, {sum(now.values())} addresses')
    sys.exit(0)
try:
    base = json.load(open(BASE))
except OSError:
    print('HALT: no pii-baseline.json. Run with --update once, deliberately.'); sys.exit(2)
bad = {p: n for p, n in now.items() if n > base.get(p, 0)}
if bad:
    print('PII-GATE: NEW EXPOSURE')
    for p, n in sorted(bad.items()):
        print(f'  {p}: {n} address(es), baseline {base.get(p, 0)}')
    sys.exit(1)
print(f'PII-GATE clean: {len(now)} files hold {sum(now.values())} known addresses (baseline), none new.')
