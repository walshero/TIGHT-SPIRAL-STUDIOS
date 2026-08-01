#!/usr/bin/env python3
"""
ART GATE — founder ruling 2026-08-01, enforced as arithmetic.

THE RULING (verbatim intent): hand-authored SVG scene art never ships again.
Art comes from exactly two lanes:
  1. MJ — founder Midjourney generations (traced or raster), provenance-marked.
  2. LEGAL PHOTO — CC-BY / public-domain / official government photos,
     license recorded in the mount.

WHAT PASSES:
  - Raster plates (data:image) with a data-art provenance attribute.
  - Vector TRACES of founder MJ generations whose <svg> carries provenance
    (aria-label or data-art mentioning the generation chain / SSG imprint).
  - Instrument graphics: charts/maps/meters that DISPLAY DATA, marked
    data-art-class="instrument" (e.g. Fathom soundings charts).
  - Small UI glyphs: any inline <svg> under the byte floor.

WHAT HALTS:
  - Any inline <svg> >= FLOOR bytes with none of the passes above.
    That is hand-authored scene art. It does not ship.

Usage: python3 art-gate.py file.html [more.html ...]   exit 1 on any HALT
       python3 art-gate.py --all                        gate every live page
Fossil dirs (rescued/, archive/) are records, not shipping surfaces: skipped.
"""
import re, sys, os

FLOOR = 2500
PROVENANCE = re.compile(r'(midjourney|founder (mj )?generation|super sketchy|ssg imprint|vtracer|traced from)', re.I)
INSTRUMENT = 'data-art-class="instrument"'
SKIP_DIRS = ('rescued/', 'archive/', '.git/')
# Confluence lane owns its trunk files; this lane reports, never gates them.
FOREIGN = ('confluence-TRUNK.html', '_confluence-v48-canon.html')

def gate(path):
    rel = path.lstrip('./')
    if rel.startswith(SKIP_DIRS) or os.path.basename(rel) in FOREIGN:
        return None
    try:
        s = open(path, encoding='utf-8', errors='replace').read()
    except OSError:
        return None
    halts = []
    for m in re.finditer(r'<svg[^>]*>.*?</svg>', s, re.S):
        v = m.group(0)
        if len(v) < FLOOR: continue
        if INSTRUMENT in v: continue
        head = v[:600]
        if PROVENANCE.search(head) or PROVENANCE.search(v): continue
        line = s[:m.start()].count('\n') + 1
        halts.append((line, len(v)))
    return halts

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(2)
    files = []
    if args[0] == '--all':
        for root, dirs, fs in os.walk('.'):
            dirs[:] = [d for d in dirs if d not in ('.git', 'rescued', 'archive')]
            files += [os.path.join(root, f) for f in fs if f.endswith('.html')]
    else:
        files = args
    bad = 0
    for f in sorted(files):
        halts = gate(f)
        if halts is None: continue
        if halts:
            bad += 1
            print(f"HALT  {f.lstrip('./')}")
            for line, size in halts:
                print(f"      line {line}: {size} bytes of unprovenance'd inline SVG — hand-authored scene art or unmarked trace")
    if bad:
        print(f"\n=== {bad} file(s) HALT — MJ lane or legal photo, never hand-drawn. Fix or mark provenance/instrument class. ===")
        sys.exit(1)
    print("art-gate: pass — no unprovenance'd scene SVG at or above the floor")
    sys.exit(0)

if __name__ == '__main__':
    main()
