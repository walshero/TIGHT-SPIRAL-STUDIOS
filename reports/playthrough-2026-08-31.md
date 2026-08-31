# Playthrough Sweep — 2026-08-31

**Run:** 2026-08-31T11:12Z · repo commit `b8516a2` · agent `playthrough-agent.py` (reporter, always exits 0 — never a deploy gate)
**Surfaces swept (5):** index.html · arcade.html · choose-your-leader-v7.html · choose-your-leader-v6.html · the-tell.html
**Prior report:** none. `reports/playthrough-latest.md` returned HTTP 404 and no `reports/` directory exists on `main`.

## Classification — BASELINE

This is the first run of this lane. There is nothing to diff against, so **every finding below is BASELINE**, not NEW. Next week's run is the first that can say NEW / REPEAT / FIXED.

- **NEW:** none (no prior record)
- **REPEAT:** none (no prior record)
- **FIXED:** none (no prior record)
- **BASELINE findings:** 5 finding lines across 4 surfaces; 1 surface CLEAN

### Cross-check against the documented 2026-08-28 known state

The v7 known-issue note (eight inert touches — television, evening paper, telephone, doorway, bulletin, wall map — plus two dead buttons) reproduces **exactly**: `INERT TOUCHES (8)` on those six labels, `DEAD BUTTONS (2)`. So choose-your-leader-v7.html has **not drifted** since 2026-08-28. Treat those ten as REPEAT-in-spirit from next run onward; their disappearance is the FIXED signal to shout about.

## Findings at a glance

| Surface | Verdict | Finding lines | Baseline state |
|---|---|---|---|
| index.html | NOTES | DEAD BUTTONS (1): Studio · JS ERRORS (8) | not previously reported — worth eyes |
| arcade.html | NOTES | DEAD BUTTONS (1): Cabinet · OFFLINE FLOOR (1 external request) | not previously reported |
| choose-your-leader-v7.html | NOTES | DEAD BUTTONS (2) · INERT TOUCHES (8) in world `#roomStage` | matches documented 2026-08-28 state |
| choose-your-leader-v6.html | CLEAN | none | clean |
| the-tell.html | NOTES | 0 asserted findings; 14 controls flagged VERIFY BY EYE | not a defect claim |

### The two that would be NEW if we had a prior week

1. **index.html — 8 JS errors on the front door.** Three distinct undefined references: `start is not defined`, `onHasParentDirectory is not defined`, `addRow is not defined`. This is the studio's front door throwing on load-path interaction. Highest-value line in the sweep.
2. **arcade.html — OFFLINE FLOOR breach.** One external request to `https://eclectic-youtiao-c065da.netlify.app/`. The arcade is not offline-clean; a student on a dead connection loses whatever that call feeds.

Also standing: the `Studio` button is dead on index.html and the `Cabinet` button is dead on arcade.html — the two halves of the same nav chrome, each dead on the other's page.

### Not findings

- the-tell.html's 14 no-DOM-change controls are reported by the agent as **likely select-state** (canvas/style redraw), explicitly *not asserted dead*. They need a human eye, not a fix ticket.
- choose-your-leader-v6.html logged one click timeout on `Sound` (visible but not clickable in place) and still scored CLEAN.
- The v7 line `world '#roomStage' resolved from tsp-worlds.json` is expected and correct — the sidecar world file doing its job.

## Raw agent cards

```
PLAYTHROUGH AGENT — 5 game(s)

┌─ index.html
│  verdict: NOTES   clicks: 40   end-reached: yes
│  ✗ DEAD BUTTONS (1): Studio
│  ✗ JS ERRORS (8): start is not defined | onHasParentDirectory is not defined | addRow is not defined
│  · 'Cabinet' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Flok

You take a growth ' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Borges Was Here

Five ro' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Choose Your Leader — The' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Choose Your Leader — The' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Choose Your Leader

Octo' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Reading the Fireground

' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The Tell

Reading the mo' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Found

A letter, a paten' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Cliché Hunter

A cliché ' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Cliché Cowpaths

Nobody ' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Soundings

Fourteen plac' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Behind This Door

A noti' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Dad Energy

A Father’s D' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Funny Boney's Factory

W' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Warriors Fantasy Arcade
' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'How an Idea Travels

Wat' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The Compound Capstone

W' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The Arcade

Everything, ' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Funny Boney's Factory

B' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Treasure Trove

First-ye' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The iSLO Suite

Every ga' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'EN195 — What Counts Now
' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The Course Hub

Every do' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The EN195 Arcade

Pick u' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Enjambment

A poem comes' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Enjambment skins

Four r' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Repos

Every repo on thi' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Sandbags

Cut the weight' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The Workshop Wall

Peer ' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The Review Bench

Sit wi' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The Course River

The se' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Flash Ballast

What a ve' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Play the Semester

The w' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Workshop in a Box

Every' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'MASSBAY COMMUNITY COLLEG' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'ADVANTAGE RELOCATION · M' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'THE STUDIO ITSELF
The Ru' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The Runbook & the Gates
' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
└────────────────────────────────────────

┌─ arcade.html
│  verdict: NOTES   clicks: 10   end-reached: yes
│  ✗ DEAD BUTTONS (1): Cabinet
│  · 'Studio' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · '1
Cliché Cowpaths
THREE ' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · '2
Sandbags
A FLASH FICTI' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · '3
The Tell
AN ASYNC WORK' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · '4
The Workshop Wall
WRIT' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · '5
The Review Bench
FLASH' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · '6
Barcelona Summers
GUES' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Back' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Home' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · OFFLINE FLOOR: 1 external request(s) e.g. https://eclectic-youtiao-c065da.netlify.app/
└────────────────────────────────────────

┌─ choose-your-leader-v7.html
│  verdict: NOTES   clicks: 23   end-reached: yes
│  ✗ DEAD BUTTONS (2): The shift
Ask for the hours you need
The, The back room
Touch the thing you were f
│  ✗ INERT TOUCHES (8) in world '#roomStage' (scope: #noticeRow button, #noticeRow [role=button]): The television, The evening paper, The telephone, The doorway, The bulletin, The wall map
│    the page changed but the world did not — text appeared outside the scene while the scene stayed byte-identical
│  · world '#roomStage' resolved from tsp-worlds.json — this build does not declare its own; a sidecar world is never silent
│  · 'Day' is an already-active toggle — skipped, not dead
│  · 'Text A' is an already-active toggle — skipped, not dead
└────────────────────────────────────────

┌─ choose-your-leader-v6.html
│  verdict: CLEAN   clicks: 20   end-reached: yes
│  · 'Home' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Default' is an already-active toggle — skipped, not dead
│  · 'A' is an already-active toggle — skipped, not dead
│  · 'High contrast
On' is an already-active toggle — skipped, not dead
│  · 'Reduce motion
On' is an already-active toggle — skipped, not dead
│  · 'Colorblind cues
On' is an already-active toggle — skipped, not dead
│  · click timed out on 'Sound' — visible but not clickable in place
│  · 'Back' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  nothing mechanical to fix — ready for founder taste-play
└────────────────────────────────────────

┌─ the-tell.html
│  verdict: NOTES   clicks: 30   end-reached: yes
│  ? 14 controls showed no DOM change on click — LIKELY select-state (canvas/style redraw); VERIFY BY EYE, not asserted dead
│  · 'Studio' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Cabinet' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Back' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Home' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
└────────────────────────────────────────
```
