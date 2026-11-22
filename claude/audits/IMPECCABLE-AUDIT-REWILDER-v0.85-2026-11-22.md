---
title: Impeccable audit — Rewilder v0.85 (HTML layer)
date: 2026-11-22
tool: Impeccable 4.10.0 (.claude/skills/impeccable), `audit` command, plus its detector
target: Rewilder v0.85 (shelf build, sha256 3345c39f…; repo lab/rewilder.html is still v0.84)
scope: the HTML around the canvas (title, top bar, menu, d-pad, Smash, labels). The canvas art is outside what Impeccable reads.
fixes made: none (audit only)
---

# Impeccable audit — Rewilder v0.85

Measured in headless Chrome at phone size, landscape 844x390 and portrait 390x844, touch on.

## Scores

| Area | Score (0–4) | Main finding |
|---|---|---|
| Accessibility | 3 | Labels, focus ring, reduced motion and live regions are all present. Minor: two h1s, no main landmark, and the canvas description never changes after level 1. |
| Responsive | 2 | In landscape the beaver starts behind the d-pad. The title is cut off at the top right. |
| Implementation | 4 | 4 detector prompts, all style checks; 3 fit the cut-paper look. |
| Performance | not scored | Not profiled in this pass. |
| Theming | not scored | Studio rule is a per-game palette; not assessed against tokens. |

## Findings

| Severity | Finding | Evidence | Suggested next step |
|---|---|---|---|
| P1 | **Landscape: the player starts hidden behind the d-pad.** The beaver spawns at world x 120, which on a landscape phone sits under the d-pad, and stays there until the player moves. A new player sees no character. | rewilder-v0.85-landscape-dpad.png (4 s after Start) | Start the camera or the beaver clear of the d-pad in landscape (adapt) |
| P1 | **Landscape title clipped.** "Rewilder" runs off the top right; the last letters are cut. Founder reported the same on 2026-11-11 (v0.9). | rewilder-v0.85-landscape-title.png | Fit the hanging letters to the viewport width (adapt / typeset) |
| P2 | Canvas description is fixed to the level 1 scene ("a parking garage, an elevated highway…") on every level. | aria-label on the canvas | Update the label on level change (harden) |
| P3 | Two h1 elements and no main landmark. | DOM count | One h1, wrap the play area in main |
| P3 | Detector: 3 hard offset shadows (buttons and bar). They match the cut-paper card look, so keep them. 1 torn-edge clip-path to check by eye. | impeccable detect | Founder's eye |

## What already passes
- All 4 play controls are at least 44x44 px (menu 50, lens 49, sound 50, Smash 104). None are under 24 px.
- Every control has a name. The keyboard focus ring is visible (3 px solid plus a gold shadow).
- Smallest visible text is 18 px in play and 22 px on the title. Nothing is under 16 px.
- `prefers-reduced-motion` is handled. Two aria-live regions. `lang="en"`.
- Studio contrast gate: SHIP, worst pair 10.17.

## How to rerun
In a Claude Code session on this repo, ask for "impeccable audit lab/rewilder.html", or run
`sh .claude/skills/impeccable/scripts/impeccable detect --json lab/rewilder.html` for the detector alone.
