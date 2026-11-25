# OS block: world gates (canvas worlds and art provenance)
**Mounted 2026-11-25 · belt tick 15 · owner lane: TSP hub (RW), spokes mount (RO)**

## The defect
Xenos v0.8 passed Studio Eyes and Studio Fingers. The founder rejected it on sight:
"this landscape is blurry and glitchy and layers are off and seams are noticeable."
Both gates read the DOM. The island is a `<canvas>`. Nothing on the belt could see it.

## The checks (all measured, none remembered)
| Gate | What it measures | Verdict |
|---|---|---|
| `studio-eyes/world-eyes.py` | spawn + every Places walk, desktop @2x and phone @3x: W-SMEAR (smeared land tiles, water skipped), W-SEAM (straight plate breaks), W-EMPTY (empty ground) | SMEAR mean > 5% or a view > 10%: HALT. SEAM: HALT. EMPTY: warn only (taste number, not armed) |
| `studio-eyes/world-fingers.py` | phone via the `?debug=1` hook: F-KIOSK >= 44 css px, F-CENTER player in the middle 60% after every walk (founder ruling 2026-11-25), F-TAP >= 95% of taps find a walk, F-SOLID no path crosses a footprint, F-DEPTH front edges work | any fail: HALT. No hook: BLIND (exit 2), never a pass |
| `studio-eyes/art-ledger.py <manifest.json>` | every art asset has source, author, license, license URL, exact URL and sha256, or is in-house with author and sha256 | any missing: BLOCK |

## How the gates learn: founder rejections become fixtures
`studio-eyes/founder-rejections.json` lists every build the founder rejected for a reason a gate should catch. `world-eyes.py --self-test` must HALT on each one. If a gate passes a rejected build, the gate is broken, and belt tick 15 says so instead of passing.
Each new rejection of a world build: copy the build into `studio-eyes/canary-world/`, add a row with the founder's words, re-calibrate until the self-test HALTs it.

## Calibration record
| Build | Smear mean (max) | Empty | Fingers |
|---|---|---|---|
| Xenos v0.8, founder-rejected | 7.8% (14.8%) | 10-26% | n/a |
| Xenos v0.11 | 2.4% (3.6%) | 20-61% | 5 kiosks, 6 walks centred, 30/30 taps, 110 routes clean, 20 objects |
| canary: v0.11 with a loose camera | n/a | n/a | F-CENTER HALT on 5 of 6 walks (player at 1-99% of the screen) |

Tried and dropped: two edge-width blur measures. Neither separated v0.8 from v0.11 (both 2.5 css px). Dropped, not tuned to fit.

## Opt in
A canvas world declares `<meta name="tsp:world" content="canvas">` and exposes `window.__xen` under `?debug=1` (contract in the `world-fingers.py` docstring).
Xenos builds live in the Drive lane, not this repo; each Xenos build runs both gates before it ships.
