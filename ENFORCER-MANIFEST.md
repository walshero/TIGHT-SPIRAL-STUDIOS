# Enforcer Manifest — what runs, what's manual, what's dead
*2026-08-05. The survey found 34 enforcer scripts and ~4 wired. This is the ground truth: every gate, and whether anything actually invokes it. Keep this current — a gate not on this list is a gate nobody is accountable for.*

## TIER 1 — WIRED, AUTOMATIC (`.github/workflows/floor.yml`, every push to main)
These cannot be skipped. They are the real floor.
| Gate | Role | Blocks? |
|---|---|---|
| `studio-eyes-sweep.py` | v4 render-proof accessibility sweep | reports (feeds ratchet) |
| `ratchet.py` | blocks accessibility **regressions** vs `floor-baseline.json` | **BLOCKS** |
| `matt-eyes-lane-check.py` | no private material on the public repo | **BLOCKS** |
| `funes-tendrils.py` | post-stall loose-ends walk | reports |
| `secret-scan-gate.py` | no committed secrets | reports (arm later) |

## TIER 2 — WIRED, MANUAL RUNNERS (only if someone runs the script)
| Runner | Invokes |
|---|---|
| `ci.sh` | `preship-gate-v4.py --ratchet`, `emit-state.py`, `parsecheck.py` |
| `safe-push.sh` | `art-gate.py`, `comfort-gate.py`, `version-stamp.py` |
| `studio-belt.sh` | `comfort-gate.py` |
| `emit-state.py` | `preship-gate-v4.py` |

## TIER 3 — MANUAL / NOT WIRED (run only if remembered — the gap)
`comfort-sweep.py` · `e2e-s2.py` · `floor-status.py` · `founder-gate.py` · `handoff.py` · `lane-fidelity.py` · `medium-gate-check.py` · `playthrough-agent.py` · `preship-contrast-gate.py` · `release-steward.py` · `reply-shape-gate.py` · `resolve-canon.py` · `shelf-safe-to-delete.py` · `staging-area.py` · `structure-gate.py` · `studio-eyes/studio-eyes.py` · `studio-eyes/studio-fingers.py` · `studio-voice-gate.py` · `svg-text-floor.py`

**Flags worth resolving:**
- **`preship-gate-v5.py` supersedes v4 in its own docstring — but every runner (`ci.sh`, `emit-state.py`) still calls v4.** Either wire v5 in and retire v4, or drop v5. Right now v5 is aspirational.
- **`studio-fingers.py` is unwired** — yet the 2026-08-05 playtest found systemic 44px touch-floor misses it would have caught. Recommend wiring into `floor.yml` (report-only first).
- **`medium-gate-check.py`** (Medium Gate) and **`studio-voice-gate.py`** (Studio Voice) are unwired — both are "fool-me-once" gates that only bite if remembered.

## SUPERSEDED — archived (`archive/enforcers/`)
| Gate | Superseded by | Why safe to archive |
|---|---|---|
| `preship-gate-v3.py` | v4 / v5 | no runner references it; only historical notes do |

*(`preship-contrast-gate.py` is also superseded per `studio-type-contrast-standard.md`, but left in place until confirmed no local muscle-memory calls it.)*

## THE RULE
Every gate is **wired or retired**. A check that runs only when remembered is not a floor — it is a document. When you add a gate, add it here and wire it (or mark it explicitly manual with a reason).
