#!/usr/bin/env python3
"""chrome-scroll-check.py — the studio chrome scrolls away. Arithmetic, not a wish.

Founder, 2026-10-13: the Studio / Cabinet bar should scroll away "when you're moving",
studio-wide. Flok v30 fixed its own bar; this lists every page whose .se-chrome is still
pinned (position: sticky or fixed in its CSS) and whose Studio/Cabinet links are still the
big boxed mono buttons. Report mode until the founder approves the 110% rollout
(claude/RULING-110-PERCENT-2026-10-13.md); then it joins the belt.

Usage: python3 chrome-scroll-check.py [files...]   (default: every live .html page)
Exit 1 if any page pins the chrome.
"""
import re, sys, glob, os
SKIP = ('archive/', 'rescued/', 'shelf-rescue', 'reports/', 'studio-eyes/canary', 'node_modules/')
files = sys.argv[1:] or [f for f in glob.glob('**/*.html', recursive=True) if not f.startswith(SKIP)]
pinned, boxed = [], []
for f in sorted(files):
    s = open(f, encoding='utf-8', errors='ignore').read()
    if 'class="se-chrome"' not in s: continue
    rules = ' '.join(re.findall(r'\.se-chrome\{[^}]*\}', s))
    if re.search(r'position:\s*(sticky|fixed)', rules): pinned.append(f)
    if 'v30 (founder, 2026-10-13' not in s: boxed.append(f)
print(f"chrome-scroll-check: {len(pinned)} page(s) pin the studio bar; {len(boxed)} page(s) still use the boxed Studio/Cabinet buttons")
for f in pinned: print("  PINNED", f)
sys.exit(1 if pinned else 0)
