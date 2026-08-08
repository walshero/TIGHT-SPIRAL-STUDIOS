# Playtest Report — Studio Eyes + Fingers + agent playtester
*2026-08-05. Ran the studio's own quality engine over the flagship builds. Undated filename on purpose; history in git. Refreshed on demand.*

## Engine (all local, no LLM credits — deterministic)
- **Studio Eyes** (`studio-eyes/studio-eyes.py`) — render/visual: contrast, focus, touch, token roles. Self-test 20/20.
- **Studio Fingers** (`studio-eyes/studio-fingers.py`) — touch: 44px targets, no sideways scroll, comfort-is-a-knob-not-a-wall. Self-test passes.
- **Agent playtester** (`playthrough-agent.py`) — breadth-first plays each game; catches dead buttons, JS errors, dead ends, opening walls. Self-test passes.

*(Env note: Playwright 1.61 was bridged to the pre-installed Chromium-1194 via symlinks under `/opt/pw-browsers/chromium-1228*` — no `playwright install`.)*

## Headline finding — the 44px touch floor is systemic
The just-shipped **`en195-arcade.html` passes clean** ("every hand lands"). The **older ISLO suite systematically fails** the 44px touch floor — the shared button/input styling sits at 26–42px:

| Build | Touch-floor misses (Studio Fingers) |
|---|---|
| `en195-arcade.html` | ✅ clean — the reference standard |
| `rubric-forge.html` | inputs 37px, "Remove" 29px, "+ Add a dimension" 39px, "Copy"/"Print" 37–39px |
| `close-the-loop.html` | ~25 inputs at 37px, mode buttons 32px, copy/print 37–39px |
| `score-the-room.html` | "Meet the normed score" 40px, "Next ›" 42px |
| `scorer-norming.html` | same wizard buttons 40/42px |
| `update-the-model.html` | confidence slider 26px, buttons 40/42px |
| `whose-draft.html` | "Make the call" 40px |
| `reading-the-fireground.html` | Back/Home/comfort 40px — **FIXED** (see below) |

**Root cause:** shared, copy-pasted control styling below the founder's 44px floor (52px for buttons). Not one bug — one pattern repeated. This matches the survey's "copy-paste chrome" coherence note.

## Studio Eyes (render) — fireground, before/after
- Before: 15 defects (warm-mode nav contrast 2.0–2.9:1, no focus ring, 4 sub-44px targets, 5 token-role dual-uses).
- **After my fix: 15 → 9.** Cleared: nav/comfort touch targets **and** warm-mode button contrast. Studio Fingers now **passes**.
- **Remaining 9 = studio-wide design-system debt, not fireground-specific:** `TOKEN_ROLE` (`--ink/--paper/--field/--dusk/--alarm` used as *both* text and decoration — needs the token set split), plus the skip-link measured off-screen (a keyboard-only element). These recur across the corpus; fix at the token-system level, not per file.

## Agent playtester — games are mechanically playable
Every build **reached an end state** (playable, no hard dead-ends in the game proper). Caveat: the agent returned *identical* output across 4 distinct ISLO files — it's exercising a **shared studio overlay** (a "north_trail"/compass widget with unclickable-in-place items), not each game's mechanics. That's a harness limitation + a shared-widget flag to verify by hand, **not** four separate bugs. Fireground played clean end-to-end (12 clicks) with only chrome/navigation artifacts under `file://`.

## What I fixed this pass
- **`reading-the-fireground.html`** (fireground branch): `.comfort`/`.nav` buttons → 44px, larger skip target, `button:focus-visible` fallback. Studio Fingers **green**; Studio Eyes 15 → 9. Committed + pushed.

## Recommended next (not auto-applied — needs your go)
1. **Suite-wide touch-floor fix:** bump the shared control CSS in the ISLO tools (rubric-forge, close-the-loop, score-the-room, scorer-norming, update-the-model, whose-draft) to `min-height:44px` (52px buttons), inputs to 44px. Use `en195-arcade.html` as the reference. Each is self-contained, so it's a per-file bump — mechanical, low-risk, but touches ~6 live files on main.
2. **Split the token roles** (`--ink/--paper/--field/--dusk/--alarm`) into text vs decoration tokens — clears the recurring `TOKEN_ROLE` HALT studio-wide.
3. **Wire Studio Fingers into `floor.yml`** so the touch floor is a gate, not a memory (only Studio Eyes render is wired today — the survey's "34 enforcers, ~4 wired" gap).
