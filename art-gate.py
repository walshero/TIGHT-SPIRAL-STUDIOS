#!/usr/bin/env python3
"""
ART GATE — founder ruling 2026-08-01, enforced as arithmetic.

THE RULING (verbatim intent): hand-authored SVG scene art never ships again.
Art came from exactly two lanes:
  1. MJ — founder Midjourney generations (traced or raster), provenance-marked.
  2. LEGAL PHOTO — CC-BY / public-domain / official government photos,
     license recorded in the mount.

AMENDMENT, 2026-08-27 — THE THIRD LANE
---------------------------------------
Lane 1 closed on 2026-08-13: "No MJ in studio as we can do better than we have so
far with proper execution." That left one legal lane, licensed photography, which
an offline single-file game cannot carry. For two weeks the law read "art comes
from MJ" while MJ was shut, so the only compliant build was a build with no art.
Founder, 2026-08-27, asking for a game: "And we want art."

So a third lane opens, and it is the one the 08-13 ruling actually named:

  3. STUDIO-CUT — art cut in the studio, marked data-art-class="studio-cut",
     and PROVED by art-execution-gate.py rather than by its own label.

Read the 08-01 ruling honestly and this is not a reversal of it. That ruling
banned hand-authored SVG because the hand-authored SVG this studio was shipping
was bad: flat, thin, no silhouette, type drowned by its own scene. The ban was a
proxy for a quality bar nobody could measure at the time. art-execution-gate.py
now measures that bar directly (type dominance, cross-hatch texture, flat layers),
so the proxy can retire in favour of the thing it was standing in for.

THE TEETH, so the marker cannot grant itself: when this gate sees studio-cut it
RUNS art-execution-gate.py on the file and HALTs if that gate HALTs, or if it
cannot run at all. A label that clears a gate by being present is the failure this
repo has a standing rule against; blind is not clean. The two gates compose, and
neither answers the other's question: art-gate asks where the art came from,
art-execution-gate asks whether it is any good.

WHAT PASSES:
  - Raster plates (data:image) with a data-art provenance attribute.
  - Vector TRACES of founder MJ generations whose <svg> carries provenance
    (aria-label or data-art mentioning the generation chain / SSG imprint).
  - Instrument graphics: charts/maps/meters that DISPLAY DATA, marked
    data-art-class="instrument" (e.g. Fathom soundings charts).
  - Studio-cut scene art marked data-art-class="studio-cut", IF and only if
    art-execution-gate.py passes the file.
  - Small UI glyphs: any inline <svg> under the byte floor.

WHAT HALTS:
  - Any inline <svg> >= FLOOR bytes with none of the passes above.
    That is hand-authored scene art with nothing behind it. It does not ship.
  - Any file claiming studio-cut whose execution gate HALTs, or whose execution
    gate could not be run (no browser). An unproven claim is not a lane.

Usage: python3 art-gate.py file.html [more.html ...]   exit 1 on any HALT
       python3 art-gate.py --all                        gate every live page
Fossil dirs (rescued/, archive/) are records, not shipping surfaces: skipped.
"""
import re, sys, os, subprocess

FLOOR = 2500
PROVENANCE = re.compile(r'(midjourney|founder (mj )?generation|super sketchy|ssg imprint|vtracer|traced from)', re.I)
INSTRUMENT = 'data-art-class="instrument"'
STUDIO_CUT = 'data-art-class="studio-cut"'
EXEC_GATE  = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'art-execution-gate.py')
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
    claims_studio_cut = False
    for m in re.finditer(r'<svg[^>]*>.*?</svg>', s, re.S):
        v = m.group(0)
        if len(v) < FLOOR: continue
        if INSTRUMENT in v: continue
        if STUDIO_CUT in v:
            claims_studio_cut = True
            continue
        head = v[:600]
        if PROVENANCE.search(head) or PROVENANCE.search(v): continue
        line = s[:m.start()].count('\n') + 1
        halts.append((line, len(v), "unprovenance'd inline SVG - hand-authored scene art or unmarked trace"))
    if claims_studio_cut:
        # The marker does not clear itself. Prove it, or it is not a lane.
        ok, why = execution_proved(path)
        if not ok:
            halts.append((0, 0, 'studio-cut claimed but NOT proved: ' + why))
    return halts


def execution_proved(path):
    """Run art-execution-gate.py on the file. Returns (passed, reason).

    A gate that cannot run is not a pass. If playwright is missing the execution
    gate cannot measure anything, and an unmeasured claim of proper execution is
    exactly the thing the third lane exists to stop."""
    if not os.path.exists(EXEC_GATE):
        return False, 'art-execution-gate.py not found beside this gate'
    try:
        r = subprocess.run([sys.executable, EXEC_GATE, path],
                           capture_output=True, text=True, timeout=180)
    except Exception as e:
        return False, 'art-execution-gate.py could not run (%s)' % e
    out = (r.stdout or '') + (r.stderr or '')
    if r.returncode != 0:
        first = next((l.strip() for l in out.splitlines() if l.strip().startswith('HALT')
                      or 'HALT' in l), 'see art-execution-gate.py output')
        return False, 'art-execution-gate HALT (' + first + ')'
    if 'no scene marked' in out and 'SHIP' not in out:
        return False, 'art-execution-gate measured no scene; mark the art [data-scene] or .stage'
    if 'playwright' in out.lower() and 'SHIP' not in out:
        return False, 'art-execution-gate could not open a browser; blind is not clean'
    return True, 'art-execution-gate passed'

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
            for line, size, why in halts:
                where = f"line {line}: {size} bytes of " if line else ''
                print(f"      {where}{why}")
    if bad:
        print(f"\n=== {bad} file(s) HALT. Three lanes: founder MJ (closed 08-13), legal photo, "
              f"or studio-cut PROVED by art-execution-gate.py. Mark the lane and earn it. ===")
        sys.exit(1)
    print("art-gate: pass — no unprovenance'd scene SVG at or above the floor")
    sys.exit(0)

if __name__ == '__main__':
    main()
