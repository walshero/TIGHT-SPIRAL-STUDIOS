#!/usr/bin/env python3
"""
RETIRED 2026-08-08 — this gate is not canon. Do not call it. Do not revive it.

It parsed SOURCE. The surviving gate RENDERS:

    studio-eyes/studio-fingers.py          # 412x915 touch viewport, real geometry
    python3 studio-eyes/studio-fingers.py --self-test

WHY IT LOST, recorded so nobody rebuilds it a third time:

Two sessions in ONE lane built two gates of this name on 2026-08-07/08. Neither read
cross-lane-manifest.md, and the manifest could not have stopped them — it governed docs
and named no gate, and both sessions held RW on the same lane. That is a within-lane
concurrency hazard the studio's lane-level RW/RO model cannot express.

On the merits it was not close. This gate shipped FOUR false positives against Flok in
one afternoon, every one from guessing at geometry instead of measuring it:
  - CSS comments leaked into selector names
  - var() went unresolved, so 44px controls were reported at 28.5px
  - ::after was treated as an independent tap target
  - the cascade was ignored, so it read the FIRST rule per selector and flagged a fix
    as the defect while Chromium rendered the correct value
It also carried a 48px "house floor" the agent DERIVED FROM APPLE while the founder's
own 44px/52px ruling sat in PLAYTEST-REPORT.md and three rescued design docs since July.
That invented number manufactured 66 surfaces and 121 halts of debt that never existed.

What survived the merge, ported into the winner: F-ZOOM (16px input floor), C-REACH,
C-EDGE, C-BUTTON, and the [LAW]/[FOUNDER]/[CITED] authority tagging so every number
declares where it came from.

Exits 2 — LOUD. A retired gate that exits 0 reads as a pass, and a gate that goes blind
must never read as clean.
"""
import sys

print(__doc__, file=sys.stderr)
print("HALT — studio-fingers.py at repo root is RETIRED. "
      "Use studio-eyes/studio-fingers.py.", file=sys.stderr)
sys.exit(2)
