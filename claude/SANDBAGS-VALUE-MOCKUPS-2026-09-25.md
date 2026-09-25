# SANDBAGS VALUE MOCK-UPS — 2026-09-25
Base: sandbags.html v37, repo HEAD b891617. Nothing committed to the game.
Artifact: "Sandbags Value Pass" (claude.ai artifact PjBJcrT6zhzmTEcUM54f1N). Edits: claude/sandbags-value-mock-edits.py (string patches on SCENERY + CSS).

## Result (value-structure v1, desktop 1280, chips hidden, balloon in frame)
| Scene | masses | quiet strips | focal (need 1.25) | focal, set only |
|---|---|---|---|---|
| Echigo | 3 -> 2 | 0 -> 4 | 1.02 -> 1.11 | 1.02 -> 1.19 |
| Crosswalk | 4 -> 2 | 0 -> 2 | 1.32 -> 1.15 | 1.32 -> 1.05 |
| Peach Cobbler | 2 -> 2 | 1 -> 3 | 1.07 -> 1.10 | 1.07 -> 1.16 |
| Dead Ants | 2 -> 2 | 0 -> 2 | 1.03 -> 1.13 | 1.03 -> 1.46 PASS |
(Crosswalk "now" 1.32 winner was the red tower top by the sun; mock winner is the father at the crosswalk.)

## Findings
- V3 rest passes in all four mock-ups.
- Turning off lit windows alone changed almost nothing. The light masses were pale plaster, clouds, the white pavilion. The move that worked: a radial shadow veil closing toward the story spot.
- The balloon is first or second focal point in every scene.

## Founder calls pending
1. Gate measures the set with the balloon hidden? (Rec: yes.)
2. Build all four into v38? Flag: Crosswalk child's coat to pale yellow is a costume change.

## Round 2 — LENS PASS (founder 15:18: "each scene looks like a power outage. This isn't how photographers or filmmakers find focus")
Darkening veil RETIRED. New moves: shallow depth of field on ly1 (blur 1.5) and ly2 (blur .55), sky art blur, warm key light added on the subject (screen blend), light lens falloff at corners. Scene brightness unchanged from v37.
Edits: claude/sandbags-lens-mock-edits.py (applies on top of round-1 light edits minus silhouettes/haze).
Finding: value-structure v1 squints, so it is blind to focus. Probe claude/focus-sharpness-probe.py (background-band / foreground-band Laplacian energy, balloon hidden):
Echigo 0.80 -> 0.61 · Crosswalk 0.45 -> 0.21 · Peach 0.20 -> 0.15 · Dead Ants 0.30 -> 0.14
Remaining light problems (value, balloon hidden): Crosswalk sun behind red tower; Dead Ants Sparr's lunch counter.
Echigo limit: street houses share ly3 with the street; real depth split needs them on their own layer.
Calls pending: V5 focus check in Studio Eyes (rec yes); balloon hidden when measuring (rec yes); build lens pass into v38 (flags: child's coat, Echigo layer split).

## SHIPPED as sandbags.html v38 (founder 15:24: "Make these updates live everywhere and animations to match")
- Lens pass in the real source (claude/sandbags-v38-build.py reproduces it from v37).
- Funny failure: four village gags on crash, key light follows each gag. Timing floor held (fall .6, hold .4, gag 1.5-2.5s, then still); reduced motion shows the punchline still. No red, no stamp.
- Gates: preship-gate-v4 output identical to v37 (the E1-SVG and --stamp findings pre-date v38); preship-contrast-gate SHIP, worst pair 7.47; JS parses; no console errors; phone 390px no horizontal scroll.
- Still PENDING founder: V5 focus check in Studio Eyes; measure with balloon hidden; Crosswalk child's yellow coat shipped as mocked (reverse on his word).
