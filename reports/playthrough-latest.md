# Playthrough Sweep — 2026-09-07

**Run:** 2026-09-07T11:23Z · repo commit `2aaa91a` · agent `playthrough-agent.py` (reporter, always exits 0 — never a deploy gate)
**Surfaces swept (5):** index.html · arcade.html · choose-your-leader-v7.html · choose-your-leader-v6.html · the-tell.html
**Prior report:** `reports/playthrough-latest.md` @ 2026-08-31 (HTTP 200, 13,524 B) — first real diff in this lane.

## Classification

- **NEW: 2** — v7 clipped text (3 lines); index.html JS error count drifted 8 → 9
- **REPEAT: 5 finding lines** across 3 surfaces (index Studio dead · arcade Cabinet dead · arcade OFFLINE FLOOR · v7 DEAD BUTTONS 2 · v7 INERT TOUCHES 8)
- **FIXED: 0** — nothing from 2026-08-31 has gone away
- **CLEAN:** choose-your-leader-v6.html (clean both runs)

---

## NEW — the two lines worth your eyes

### 1. choose-your-leader-v7.html — CLIPPED TEXT (3), and it is text being thrown away

```
"The shelf"                        cut by 5px in div.walkbox (400px box, 417px of content) · after 'Walk the house'
"The back room"                    cut by 5px in div.walkbox (400px box, 417px of content) · after 'Walk the house'
"Touch the thing you were fixing"  cut by 5px in div.walkbox (400px box, 417px of content) · after 'Walk the house'
```

**Read this carefully before filing it as a regression — it is not one.** `choose-your-leader-v7.html`
last changed on **2026-08-26** (commit `e7c8686`); it is byte-identical to the build the baseline swept.
What changed is the *instrument*: the CLIPPED TEXT detector landed **2026-09-01** in commit `23bce7d`
("Flok: the research card sizes to its text, not the other way round"), one day after the baseline run.

So this is a **pre-existing defect newly visible**, not new breakage. That makes it more actionable, not
less — it has been shipping since at least 2026-08-26 and nobody could see it. It is also the same
defect class documented in `CLIPPED-TEXT-FLOOR-2026-09-01.md`: a fixed pixel number deciding how much
text a reader gets. Three walk options in the walkbox lose their last 5px. Anyone reading at increased
text size loses more, which is the part that matters.

### 2. index.html — JS errors 8 → 9 on the front door

Same three distinct undefined references as the baseline (`start is not defined`,
`onHasParentDirectory is not defined`, `addRow is not defined`) — but one more thrown instance.
`index.html` took three commits on **2026-09-01** (`1c21667` Mail Drop, `24cf8f7` bottom rail,
`ab40b70` merge). The count moved with the build. Low severity per instance, but it is the studio's
front door and the trend is the wrong direction.

## REPEAT — 5 finding lines, summarised not listed

Everything documented at 2026-08-28 and confirmed at 2026-08-31 reproduces exactly:

| Surface | Repeat finding lines |
|---|---|
| index.html | DEAD BUTTONS (1): Studio |
| arcade.html | DEAD BUTTONS (1): Cabinet · OFFLINE FLOOR (1 external request, eclectic-youtiao-c065da.netlify.app) |
| choose-your-leader-v7.html | DEAD BUTTONS (2) · INERT TOUCHES (8) in world `#roomStage` |

The v7 known state — eight inert touches (television, evening paper, telephone, doorway, bulletin,
wall map) plus two dead buttons — **reproduces exactly, ten of ten**. v7 has still not drifted. Their
disappearance remains the FIXED signal worth shouting about; it has not happened yet.

## FIXED — none

No finding from 2026-08-31 has cleared. Stated plainly so the absence is on the record.

## Run notes

- **The five-surface invocation did not finish in one pass.** `index`, `arcade`, `v7` and `v6`
  completed; the run hit a 9-minute ceiling before `the-tell.html`. `the-tell.html` was swept in a
  second invocation of the same agent, exit 0, and its card is reproduced below unedited. All five
  surfaces are covered; the cards are simply from two invocations, not one.
- Click depth rose on three surfaces versus baseline (v7 23 → 40, v6 20 → 40, the-tell 30 → 40).
  Deeper traversal is part of why the v7 walkbox state was reached this week.
- `world '#roomStage' resolved from tsp-worlds.json` on v7 — expected and correct, the sidecar doing
  its job.
- `the-tell.html`'s 14 no-DOM-change controls are again reported as **likely select-state**
  (canvas/style redraw), explicitly *not asserted dead*. Unchanged from baseline. Not a fix ticket.
- `choose-your-leader-v6.html` again logged one click timeout on `Sound` and still scored CLEAN.

## Raw agent cards

```
PLAYTHROUGH AGENT — 5 game(s)

┌─ index.html
│  verdict: NOTES   clicks: 40   end-reached: yes
│  ✗ DEAD BUTTONS (1): Studio
│  ✗ JS ERRORS (9): start is not defined | onHasParentDirectory is not defined | addRow is not defined
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
│  · 'Mail Drop

Nib has read ' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
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
│  verdict: NOTES   clicks: 40   end-reached: yes
│  ✗ CLIPPED TEXT (3) — laid out, then thrown away:
│      "The shelf" cut by 5px in div.walkbox (400px box, 417px of content) · after 'Walk the house'
│      "The back room" cut by 5px in div.walkbox (400px box, 417px of content) · after 'Walk the house'
│      "Touch the thing you were fixing" cut by 5px in div.walkbox (400px box, 417px of content) · after 'Walk the house'
│  ✗ DEAD BUTTONS (2): The shift
Ask for the hours you need
The, The back room
Touch the thing you were f
│  ✗ INERT TOUCHES (8) in world '#roomStage' (scope: #noticeRow button, #noticeRow [role=button]): The television, The evening paper, The telephone, The doorway, The bulletin, The wall map
│    the page changed but the world did not — text appeared outside the scene while the scene stayed byte-identical
│  · world '#roomStage' resolved from tsp-worlds.json — this build does not declare its own; a sidecar world is never silent
│  · 'Day' is an already-active toggle — skipped, not dead
│  · 'Text A' is an already-active toggle — skipped, not dead
│  · 'The television' is an already-active toggle — skipped, not dead
│  · 'The television' is an already-active toggle — skipped, not dead
│  · 'The television' is an already-active toggle — skipped, not dead
│  · 'The television' is an already-active toggle — skipped, not dead
│  · 'The television' is an already-active toggle — skipped, not dead
│  · 'The television' is an already-active toggle — skipped, not dead
│  · 'The television' is an already-active toggle — skipped, not dead
│  · 'The television' is an already-active toggle — skipped, not dead
│  · 'The television' is an already-active toggle — skipped, not dead
│  · 'The television' is an already-active toggle — skipped, not dead
│  · 'The television' is an already-active toggle — skipped, not dead
│  · 'The evening paper' is an already-active toggle — skipped, not dead
│  · 'The evening paper' is an already-active toggle — skipped, not dead
│  · 'The evening paper' is an already-active toggle — skipped, not dead
│  · 'The evening paper' is an already-active toggle — skipped, not dead
│  · 'The evening paper' is an already-active toggle — skipped, not dead
│  · 'The evening paper' is an already-active toggle — skipped, not dead
│  · 'The evening paper' is an already-active toggle — skipped, not dead
│  · 'The evening paper' is an already-active toggle — skipped, not dead
│  · 'The evening paper' is an already-active toggle — skipped, not dead
│  · 'The evening paper' is an already-active toggle — skipped, not dead
│  · 'The evening paper' is an already-active toggle — skipped, not dead
│  · 'The telephone' is an already-active toggle — skipped, not dead
│  · 'The telephone' is an already-active toggle — skipped, not dead
│  · 'The telephone' is an already-active toggle — skipped, not dead
│  · 'The telephone' is an already-active toggle — skipped, not dead
│  · 'The telephone' is an already-active toggle — skipped, not dead
│  · 'The telephone' is an already-active toggle — skipped, not dead
│  · 'The telephone' is an already-active toggle — skipped, not dead
│  · 'The telephone' is an already-active toggle — skipped, not dead
│  · 'The telephone' is an already-active toggle — skipped, not dead
│  · 'The telephone' is an already-active toggle — skipped, not dead
│  · 'The telephone' is an already-active toggle — skipped, not dead
│  · 'The doorway' is an already-active toggle — skipped, not dead
│  · 'The doorway' is an already-active toggle — skipped, not dead
│  · 'The doorway' is an already-active toggle — skipped, not dead
│  · 'The doorway' is an already-active toggle — skipped, not dead
│  · 'The doorway' is an already-active toggle — skipped, not dead
│  · 'The doorway' is an already-active toggle — skipped, not dead
│  · 'The doorway' is an already-active toggle — skipped, not dead
│  · 'The doorway' is an already-active toggle — skipped, not dead
│  · 'The doorway' is an already-active toggle — skipped, not dead
│  · 'The doorway' is an already-active toggle — skipped, not dead
│  · 'The doorway' is an already-active toggle — skipped, not dead
│  · 'The bulletin' is an already-active toggle — skipped, not dead
│  · 'The bulletin' is an already-active toggle — skipped, not dead
│  · 'The bulletin' is an already-active toggle — skipped, not dead
│  · 'The bulletin' is an already-active toggle — skipped, not dead
│  · 'The bulletin' is an already-active toggle — skipped, not dead
│  · 'The bulletin' is an already-active toggle — skipped, not dead
│  · 'The bulletin' is an already-active toggle — skipped, not dead
│  · 'The bulletin' is an already-active toggle — skipped, not dead
│  · 'The bulletin' is an already-active toggle — skipped, not dead
│  · 'The bulletin' is an already-active toggle — skipped, not dead
│  · 'The bulletin' is an already-active toggle — skipped, not dead
│  · 'The wall map' is an already-active toggle — skipped, not dead
│  · 'The wall map' is an already-active toggle — skipped, not dead
│  · 'The wall map' is an already-active toggle — skipped, not dead
│  · 'The wall map' is an already-active toggle — skipped, not dead
│  · 'The wall map' is an already-active toggle — skipped, not dead
│  · 'The wall map' is an already-active toggle — skipped, not dead
│  · 'The wall map' is an already-active toggle — skipped, not dead
│  · 'The wall map' is an already-active toggle — skipped, not dead
│  · 'The wall map' is an already-active toggle — skipped, not dead
│  · 'The wall map' is an already-active toggle — skipped, not dead
│  · 'The wall map' is an already-active toggle — skipped, not dead
└────────────────────────────────────────

┌─ choose-your-leader-v6.html
│  verdict: CLEAN   clicks: 40   end-reached: yes
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
│  · 'Sound' is an already-active toggle — skipped, not dead
│  · 'Sound' is an already-active toggle — skipped, not dead
│  · 'Sound' is an already-active toggle — skipped, not dead
│  · 'Sound' is an already-active toggle — skipped, not dead
│  · 'Sound' is an already-active toggle — skipped, not dead
│  · 'Sound' is an already-active toggle — skipped, not dead
│  · 'Sound' is an already-active toggle — skipped, not dead
│  · 'Sound' is an already-active toggle — skipped, not dead
│  · 'Sound' is an already-active toggle — skipped, not dead
│  · 'Sound' is an already-active toggle — skipped, not dead
│  · 'Sound' is an already-active toggle — skipped, not dead
│  nothing mechanical to fix — ready for founder taste-play
└────────────────────────────────────────

┌─ the-tell.html
│  verdict: NOTES   clicks: 40   end-reached: yes
│  ? 14 controls showed no DOM change on click — LIKELY select-state (canvas/style redraw); VERIFY BY EYE, not asserted dead
│  · 'Studio' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Cabinet' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Back' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Home' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
└────────────────────────────────────────
```
