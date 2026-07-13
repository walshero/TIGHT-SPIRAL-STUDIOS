# PIPELINE UPDATE — 2026-07-13
*Amends `tableau-gate-and-room-2026-07-12.md`. Portable Markdown. Additive canon.*

## NEW TEETH (checks, not wishes)

**NAV FLOOR — added to `one-thing-gate.py`.** Every game must expose a **Home** control and a **Back** control (button/link whose accessible name contains "home"/"back"), present in the DOM even if hidden on the home screen. Missing either = HIGH (ship-affecting). The gate now scans the whole document for these. Reference implementation: `cliche-field-v6` — a corner nav (top-left) that hides on the home screen so entry stays one-invitation, plus a three-screen router (Home clears history; Back pops it).

**DARK-MODE-PROOF — studio-eyes lane.** Every game must be legible in a dark AND a light comfort stop. Structural check: does the build define both stops? Contrast arithmetic stays with `studio-eyes-sweep.py` / `preship-contrast-gate.py` (one canon writes, others read). Dark-locked or light-locked builds fail the principle. The sweep runs both stops now.

## NEW NAMED FAILURE CLASS

**COMFORT-GATE-AS-WALL.** A build that opens on a comfort/palette selection screen instead of a scene. It is the wall-before-the-scene anti-pattern wearing an accessibility costume — and it is exactly what "the review bench is gated" turned out to be (no lock; a palette picker standing where the scene belongs). Comfort is a corner knob, never the front door. Caught by the wall + one-invitation teeth; now named so the sweep can flag the class. Current instances: `flash-ballast`, `review-bench`.

## THE AUTONOMY DIAL (founder-set, 2026-07-13, temporary)

Matt: *"Until founder locks down builds, all tendrils are updating best possibly without HITL until I get there."*

Dial for this window:
- **Tendrils apply moves in scratch WITHOUT per-step approval** — rebuild to clear the gate, gate-verify, land in a lane, deliver. This is an aggressive read of the GREEN lane (build through Stage 5), authorized by the founder.
- **Reserved for founder lockdown (unchanged RED):** locking canon (which build replaces which — e.g. v5 vs v6), publishing any build to public web, anything touching student data (FERPA), real-money, external comms as Matt.
- **Reverts** to the default dial (GREEN auto / YELLOW report / RED gated) when Matt says "locked" or amends at a belt close.

Guardrails still live under the grant: accessibility floors, no emoji, majority image, single-file/offline, and byte-verified landing in a real lane every turn.

## SWEEP UPGRADE
The weekly Tableau Sweep now also: checks the nav floor, runs both comfort stops for dark-mode-proof, flags comfort-gate-as-wall, reconciles design docs to the current principle set, and — under the autonomy dial — applies move lists in scratch and delivers rebuilt gate-clean builds rather than queuing verdicts.

## POINTERS
- Full state of the shelf: `suite-reconcile-2026-07-13.md`.
- The room + the gate: `tableau-gate-and-room-2026-07-12.md`.
