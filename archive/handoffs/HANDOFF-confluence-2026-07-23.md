# HANDOFF → Confluence Project
**From:** TSP (RO mount) · **As-of:** 2026-07-23 · **Author:** Claude/walshero session

## Why this exists
The Confluence trunk was edited on 07-21 but the shared index (TSP Command Center)
still records the pre-edit byte/md5. Two silos, one file, no notification. This
note resyncs the facts. Confluence project OWNS the trunk (RW); TSP only reads it.

## Current canon — VERIFIED FROM FILE THIS TURN
| Field | Value |
|---|---|
| File | `confluence-TRUNK.html` |
| Path | raw.githubusercontent.com/walshero/TIGHT-SPIRAL-STUDIOS/main/confluence-TRUNK.html |
| Title | Confluence Calibration: An Assessment Hub |
| Version marker in file | v44 |
| Bytes | **611,046** |
| md5 | **4b5c61b88ea52085efedf4fbefeb921e** |
| Last commit | `441b669c5b3fac69fae5485b85ffc3cfea918e2d` — 2026-07-21 10:09 UTC |

## What the 07-21 commit changed
"Turn sideways for more room" hint on the three canvas games (Field / Line / City).
- Dismissible hint, touch devices in portrait only, on pages that declare controls.
- Positioned below the Home/Back row in the empty top margin; auto-hides in landscape.
- No storage used (stays within the offline floor).
- Implemented in `tsp-mobile.js`, re-inlined into all pages.

## STALE FACTS TO RETIRE (were in the shared index)
- ~~598,114 B~~ → 611,046 B
- ~~md5 8dcf9903~~ → 4b5c61b8…
- ~~commit abbddc6 as latest~~ → 441b669c

## STILL OPEN — Confluence project owns the decision
**ISLO 1–7 correction.** Committed then reverted (39f3cb1 → 2622a83). That real
work is NOT live in the current trunk. Someone must decide: revert-the-revert, or
discard. TSP cannot make this call — it is RW territory.

## Also parked (Confluence-owned)
- Faculty Directory v34 edits: Sean McCarthy + Catherine Gildae.

## Concurrent-writer hazard
Trunk is a shared write target. Before editing, check cross-lane-manifest.md.
TSP writes nothing here; this handoff is a sibling report, not a trunk edit.
