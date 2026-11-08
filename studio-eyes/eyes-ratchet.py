#!/usr/bin/env python3
"""
STUDIO EYES · PUSH RATCHET                                Tight Spiral Productions
-----------------------------------------------------------------------------
Added 2026-11-08. lab/en195-course.html v1.0 landed on main (db05d24) with 25 Studio
Eyes HALTs, and the founder found the worst of them on his phone. The auditor had run
on that push and said HALT. CI ran it with continue-on-error, so the HALT was a log
line, not a gate. A gate that reports is a wish (LAWS-REGISTRY hook principle).

This arms it without freezing the studio over old debt:
  - a NEW surface must pass Studio Eyes outright
  - a CHANGED surface may not add a defect its parent did not have
  - defects the parent already carried are reported and do not block (debt only shrinks)

A defect is compared by its signature: floor code, mode and target, with every number
removed, so 2.1:1 becoming 2.3:1 is the same defect and not a new one.

USAGE  eyes-ratchet.py <before-sha|""> <file.html> [...]      exit 1 = new defects
"""
import sys, os, re, subprocess, tempfile, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('studio_eyes', os.path.join(HERE, 'studio-eyes.py'))
se = importlib.util.module_from_spec(spec); spec.loader.exec_module(se)

def sig(h):
    h = re.sub(r'\d+(\.\d+)?', '#', h)
    return h.split('. ')[0][:160]

def parent_halts(before, path):
    if not before:
        return None
    try:
        body = subprocess.run(['git', 'show', f'{before}:{path}'], capture_output=True, check=True).stdout
    except subprocess.CalledProcessError:
        return None                          # the file is new on this push
    d = os.path.dirname(os.path.abspath(path))
    with tempfile.NamedTemporaryFile('wb', suffix='.html', dir=d, delete=False) as t:
        t.write(body); tmp = t.name
    try:
        return se.audit(tmp)
    finally:
        os.unlink(tmp); se.ADVISORIES.clear()

def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    before, files = sys.argv[1], [f for f in sys.argv[2:] if f.endswith('.html') and os.path.exists(f)]
    if not se.self_test(verbose=False):
        sys.exit(1)
    blocked = 0
    for f in files:
        now = se.audit(f); se.ADVISORIES.clear()
        old = parent_halts(before, f)
        if old is None:
            new = now; label = 'NEW SURFACE'
        else:
            had = {sig(h) for h in old}
            new = [h for h in now if sig(h) not in had]; label = f'{len(now)-len(new)} carried'
        print(f'\n  {f}  ({label}; {len(now)} total)')
        if new:
            blocked += 1
            print(f'     BLOCK — {len(new)} new defect(s):')
            for h in new[:14]: print(f'       {h}')
            if len(new) > 14: print(f'       ... +{len(new)-14} more')
        else:
            print('     ok — nothing new')
    print(f'\n  === {blocked} of {len(files)} surfaces add defects ===')
    sys.exit(1 if blocked else 0)

if __name__ == '__main__':
    main()
