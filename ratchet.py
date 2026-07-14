#!/usr/bin/env python3
"""
THE RATCHET — the enforcement point the studio never had.

WHY THIS EXISTS
---------------
2026-07-14, teeth audit. The numbers:

    30 imperative rules across 10 OS blocks
     7 executable enforcers, 53 HALT paths between them
     0 enforcement points that cannot be skipped

Zero. Every gate in this studio runs only if the agent REMEMBERS to run it.
The one enforcer that fires without a human in the room — floor.yml, on every
push — was DISARMED with `continue-on-error: true`, and had been for three days.

Its own comment reads: "A gate that does not block is not a gate."

The access-control literature has a name for what is missing: a POLICY
ENFORCEMENT POINT — a chokepoint every request must physically pass through.
A policy without a PEP is not a policy. It is a document.

WHY THE GATE WAS DISARMED — AND WHY THAT REASON IS DEAD
--------------------------------------------------------
floor.yml was disarmed on 2026-07-11 over **104 pre-existing HALTs**. Blocking
then would have frozen the live site over a backlog, not a regression. That was
a correct call and it was explicitly labelled "a KNOWN, DATED, SCHEDULED
exception — not a policy."

Nobody came back. The platform-engineering literature warns about exactly this:
audit mode is a PHASE, not a DESTINATION.

And the backlog is gone. The eyes now report **15 HALTs, not 104**. The reason
for the exception expired and the exception outlived it.

WHAT THE RATCHET DOES
---------------------
Arming the gate outright would still freeze the site over 15 files. So don't.
Ratchet instead — the standard move, and the only one that converts a wish into
a PEP without stopping the world:

    BASELINE the known debt.  BLOCK anything new.  The debt can only SHRINK.

- A file already in the baseline may HALT. It is known. It does not block.
- A file NOT in the baseline that HALTs is a REGRESSION. It blocks. Exit 1.
- A baselined file that gets FIXED is removed from the baseline automatically.
  It can never quietly regress again. **The ratchet only turns one way.**

This is the whole point: the studio does not have to pay down 15 files of debt
today to stop creating new debt today.

USAGE
-----
    python3 ratchet.py --init      # write the baseline from the current sweep
    python3 ratchet.py             # CI mode: exit 1 on any NEW halt
    python3 ratchet.py --status    # what is in the baseline, what is fixed

EXIT CODES
----------
    0  no regressions (baseline debt may still exist — that is allowed)
    1  REGRESSION — a file that was clean now HALTs, or a new file HALTs
    2  cannot run (no sweep available) — fail loud, never guess
"""

import sys, os, json, subprocess, re

BASELINE = "floor-baseline.json"
SWEEP    = "studio-eyes-sweep.py"


def run_sweep():
    """Run the eyes. Return {filename: [halt lines]} for HALT files only.

    Fails LOUD if the sweep cannot run. An audit that cannot see must never
    report 'clean' — that is how resolve-canon once reported 111 fake orphans
    off a 403. A gate that goes blind is not a gate that passes.
    """
    if not os.path.exists(SWEEP):
        print("HALT — studio-eyes-sweep.py not found. Cannot audit.", file=sys.stderr)
        print("       An audit that cannot see does not report clean. It stops.",
              file=sys.stderr)
        sys.exit(2)

    r = subprocess.run([sys.executable, SWEEP, "."],
                       capture_output=True, text=True, timeout=600)
    out = r.stdout
    if not out.strip():
        print("HALT — the sweep produced no output. Refusing to guess.", file=sys.stderr)
        sys.exit(2)

    halts, cur = {}, None
    for line in out.splitlines():
        m = re.match(r'^HALT\s+(\S+)', line)
        if m:
            cur = m.group(1)
            halts[cur] = []
            continue
        if re.match(r'^warn\s+', line) or line.startswith('==='):
            cur = None
            continue
        if cur and line.strip().startswith(('H1:', 'H2:', 'H3:', 'H4:',
                                            'H6:', 'H7:', 'H8:')):
            halts[cur].append(line.strip())
    return halts


def load_baseline():
    if not os.path.exists(BASELINE):
        return None
    with open(BASELINE) as f:
        return json.load(f)


def init():
    """Freeze today's debt. This is the ONLY time the baseline may grow."""
    halts = run_sweep()
    data = {
        "created": "2026-07-14",
        "why": ("Known accessibility debt at the moment the floor gate was ARMED. "
                "These files may HALT without blocking a push. Anything NOT in this "
                "list that HALTs is a REGRESSION and blocks. This list may only "
                "SHRINK — the ratchet turns one way."),
        "rule": ("Fix a file, it leaves the baseline forever. It can never quietly "
                 "regress again."),
        "debt": sorted(halts.keys())
    }
    with open(BASELINE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"BASELINE WRITTEN — {len(data['debt'])} files carry known debt.")
    print("These do not block. Everything else does. The ratchet is armed.")
    for d in data["debt"]:
        print(f"   debt: {d}")
    return 0


def check():
    """CI mode. The PEP. This is the thing that cannot be skipped."""
    base = load_baseline()
    if base is None:
        print("HALT — no baseline. Run: python3 ratchet.py --init", file=sys.stderr)
        return 2

    debt  = set(base["debt"])
    halts = run_sweep()
    now   = set(halts.keys())

    regressions = sorted(now - debt)   # NEW halts. These block.
    fixed       = sorted(debt - now)   # repaid debt. Ratchet these away forever.
    remaining   = sorted(now & debt)

    print("=" * 70)
    print("THE RATCHET — accessibility floor")
    print("=" * 70)
    print(f"  known debt (allowed) : {len(remaining)}")
    print(f"  repaid this push     : {len(fixed)}")
    print(f"  REGRESSIONS          : {len(regressions)}")

    if fixed:
        print("\n  ## REPAID — leaving the baseline permanently")
        for f in fixed:
            print(f"     fixed: {f}")
        base["debt"] = sorted(debt - set(fixed))
        with open(BASELINE, "w") as fh:
            json.dump(base, fh, indent=2)
        print(f"\n  Baseline tightened: {len(debt)} -> {len(base['debt'])}.")
        print("  These files can never silently regress again.")

    if regressions:
        print("\n  " + "*" * 60)
        print("  *** HALT — REGRESSION ***")
        print("  " + "*" * 60)
        print("\n  These files were clean (or are new) and now FAIL the floor.")
        print("  Matt has retinitis pigmentosa. Contrast is arithmetic, not taste.")
        print("  This does not ship.\n")
        for f in regressions:
            print(f"  {f}")
            for line in halts[f][:4]:
                print(f"      {line}")
        return 1

    print("\n  No regressions. The floor holds.")
    if remaining:
        print(f"  ({len(remaining)} files still carry known debt — allowed, not forgotten.)")
    return 0


def status():
    base = load_baseline()
    if base is None:
        print("No baseline. Run --init.")
        return 2
    halts = run_sweep()
    print(f"BASELINE from {base['created']} — {len(base['debt'])} files of known debt\n")
    for d in base["debt"]:
        state = "still failing" if d in halts else "FIXED — will leave the baseline"
        print(f"  {d:<44} {state}")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--init":
        sys.exit(init())
    if a and a[0] == "--status":
        sys.exit(status())
    if a and a[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    sys.exit(check())
