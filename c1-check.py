#!/usr/bin/env python3
# ============================================================================
# c1-check.py — the color-scheme tooth, as a standalone static check.
#
# Confluence-owned (derived from the Studio Eyes C1 tooth). Unlike the full
# render-proof gate, this executes no layout and reads no JS — so it works on a
# JS-driven SPA shell too, where render-proof can only see an empty page.
#
# C1 LAW: a page that themes for dark MUST declare color-scheme, or a phone in OS
# dark mode force-darkens it and destroys the computed contrast (live-device
# failure, 2026-07-22). Declaration = <meta name="color-scheme"> OR a CSS
# `color-scheme:` property reachable from the page.
#
#   usage: c1-check.py <file.html> [more.html ...]
#          c1-check.py --css-ok <file.html> --css styles.css   (treat external css as reachable)
# exit 0 = all declare color-scheme; exit 1 = at least one does not.
# ============================================================================
import re, sys

META = re.compile(r'<meta[^>]+name\s*=\s*["\']color-scheme["\']', re.I)
CSSP = re.compile(r'color-scheme\s*:', re.I)
LINK = re.compile(r'<link[^>]+rel\s*=\s*["\']stylesheet["\'][^>]*href\s*=\s*["\']([^"\']+)', re.I)

def declares(path, seen=None):
    seen = seen or set()
    try:
        with open(path, encoding='utf-8', errors='replace') as fh:
            src = fh.read()
    except OSError as e:
        print(f"  ERR   {path}: {e}"); return False
    if META.search(src) or CSSP.search(src):
        return True
    # follow same-dir external stylesheets one level (relative hrefs only)
    import os
    base = os.path.dirname(path)
    for href in LINK.findall(src):
        if href.startswith(('http://', 'https://', '//')):
            continue
        cand = os.path.normpath(os.path.join(base, href))
        if cand not in seen and os.path.isfile(cand):
            seen.add(cand)
            try:
                if CSSP.search(open(cand, encoding='utf-8', errors='replace').read()):
                    return True
            except OSError:
                pass
    return False

def main(argv):
    files = [a for a in argv if not a.startswith('-')]
    if not files:
        print("usage: c1-check.py <file.html> [more.html ...]"); return 2
    bad = 0
    for f in files:
        ok = declares(f)
        print(f"  {'C1 ok' if ok else 'C1 HALT'}  {f}")
        if not ok:
            print(f"          -> no color-scheme declaration; phone OS dark mode will force-darken.")
            bad = 1
    print(f"\n=== {sum(1 for f in files if not declares(f))} of {len(files)} at C1 HALT ===")
    return bad

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
