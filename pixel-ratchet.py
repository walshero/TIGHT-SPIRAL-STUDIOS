#!/usr/bin/env python3
# ============================================================================
# PIXEL RATCHET — arm studio-eyes-pixel.py across ALL TSP assets (incl. Confluence).
#
# Runs the true-pixel contrast checker over the corpus, baselines the files that
# already flag, and BLOCKS anything NEW that goes invisible/low-contrast. Same
# one-way ratchet as ratchet.py (studio-eyes): debt can only shrink; a file that
# gets fixed leaves the baseline and can never quietly regress.
#
# This also absorbs the known checker limit (text inside JS-animated intro
# overlays can read variably): such a file sits in the baseline and does not
# block — but a NEW file, or a clean file that starts flagging, does.
#
#   python3 pixel-ratchet.py            # check corpus vs baseline (exit 1 on regression)
#   python3 pixel-ratchet.py --init     # (re)seed the baseline from the current corpus
#   python3 pixel-ratchet.py a.html ... # check only these files vs baseline (PR diff)
# ============================================================================
import sys, os, json, subprocess, re, glob

HERE = os.path.dirname(os.path.abspath(__file__))
BASELINE = os.path.join(HERE, "pixel-baseline.json")
CHECKER = os.path.join(HERE, "studio-eyes-pixel.py")

def corpus():
    files = sorted(glob.glob("*.html")) + sorted(glob.glob("confluence-hub/*.html"))
    return [f for f in files if os.path.isfile(f)]

def sweep(files):
    if not files:
        return set(), "no HTML assets."
    p = subprocess.run(["python3", CHECKER] + files, capture_output=True, text=True)
    out = p.stdout + p.stderr
    halted = set(os.path.basename(x) for x in re.findall(r'^HALT\s+(\S+)', out, re.M))
    return halted, out

def load_debt():
    if not os.path.exists(BASELINE):
        return None
    return set(json.load(open(BASELINE)).get("debt", []))

def save_debt(debt):
    json.dump({"why": "Files with existing pixel-contrast HALTs when the visibility "
               "gate was armed. They may flag without blocking. Anything NOT here that "
               "flags is a REGRESSION and blocks. This list may only SHRINK.",
               "rule": "Fix a file and it leaves the baseline forever.",
               "debt": sorted(debt)}, open(BASELINE, "w"), indent=2)

def main(argv):
    args = [a for a in argv if not a.startswith("-")]
    init = "--init" in argv
    files = args or corpus()
    halted, out = sweep(files)

    if init:
        save_debt(halted)
        print(f"pixel baseline seeded: {len(halted)} file(s) — {', '.join(sorted(halted)) or 'none'}")
        return 0

    debt = load_debt()
    if debt is None:
        print("HALT — no pixel-baseline.json. Seed it first: pixel-ratchet.py --init")
        print(out)
        return 2

    regressions = sorted(halted - debt)
    fixed = sorted(f for f in debt if f not in halted and (not args or f in {os.path.basename(x) for x in files}))
    if fixed:
        save_debt(debt - set(fixed))
        print("baseline shrunk (fixed, can never regress):", ", ".join(fixed))

    if regressions:
        print("PIXEL REGRESSION — NEW invisible / low-contrast text (blocks):")
        for f in regressions:
            print("   ", f)
        print("\n" + out)
        return 1
    print(f"pixel ratchet OK — {len(halted & debt)} baselined file(s) flag, 0 regressions "
          f"({len(files)} asset(s) swept)")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
