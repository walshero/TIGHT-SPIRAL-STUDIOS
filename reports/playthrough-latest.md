# Playthrough Sweep — 2026-11-16

**Run:** 2026-11-16 11:14 UTC · repo commit `565e848` · agent `playthrough-agent.py` (reporter, always exits 0 — never a deploy gate)
**Surfaces swept (5):** index.html · arcade.html · choose-your-leader-v7.html · choose-your-leader-v6.html · the-tell.html
**Prior report:** `reports/playthrough-latest.md` @ 2026-11-09 (HTTP 200, 16,762 B) — 7 days back, a clean one-week diff
**Runner:** scheduled cloud routine, unattended. One invocation, exit 0. All five surfaces completed; none errored.

## Classification

| | count | detail |
|---|---|---|
| **NEW** | **0** | no finding line appeared that was not in the 2026-11-09 report |
| **FIXED** | **0 confirmed** | one line cleared, but off byte-identical bytes — see below. Not a fix. |
| **REPEAT** | **4 finding lines** | `index.html` DEAD BUTTONS (2) · v7 CLIPPED TEXT (3) · v7 DEAD BUTTONS (2) · v7 INERT TOUCHES (8) |

**Read this line and stop if you are busy:** nothing was fixed and nothing broke. One surface
changed bytes (`index.html`) and kept exactly the findings it had. The interesting event this week
is not in the build at all — it is in the instrument, and it is below.

## The one thing worth your attention — the instrument disagreed with itself

Last week `choose-your-leader-v6.html` reported **CLIPPED TEXT (7)** and was written up as the
surface "to look at". This week the same file reports **CLEAN**, with no clipped text at all.

**The file did not change.** md5 `3e8388c22801` on 2026-11-09 and `3e8388c22801` today — byte-identical.
Nobody edited v6. So this is **not** a FIXED finding, and it is not being counted as one.

I re-ran v6 on its own to check: **CLEAN both times**, same seed, same bytes. The clean result is
reproducible today; last week's seven clips are not.

What that points at, from the evidence already on the page: every one of last week's v6 clip entries
measured its box at **`(0px box, 0px of content)`** — all six of them, on a card that counted seven.
A zero-width box cannot clip text, and a card that cannot agree with its own list is not measuring
cleanly. Compare this week's v7 clips, which carry real numbers: **`(400px box, 417px of content)`**.
Those three are credible. `playthrough-agent.py` says so itself at line 219, in the settle path:
*"a looping animation never settles; measure anyway."* On a surface with a looping animation, that
fallback can measure before layout exists and report the nothing it found as a clip.

**The 2026-11-09 report saw this same signal and read it the other way** — it advised trusting "the
*fact* of the clip and the pixel amount, not the box geometry," and tabled six findings on that
basis. That was a reasonable call with one run of evidence. It does not survive a second run: the
bytes never moved and the clips did not come back. When a 0px box and a count that disagrees with
its own list both show up on the same card, the card is the thing that is broken.

**Consequence:** last week's headline finding was an instrument artifact, and the v6 fix ticket it
implied should be closed unopened. The real work is a guard in the agent — skip any clip whose box
measures 0px rather than reporting it — so a 0px box never again costs a reader a week of attention.
That is a one-condition change at the CLIPPED TEXT assembly (around line 644–651), not a rewrite.

## REPEAT — 4 finding lines, summarised not listed

- `index.html` — DEAD BUTTONS (2): `Studio`, `Home`. **Repeat on changed bytes** (md5 moved
  `ec9c721a497a` → `55be71998ace`), so an edit landed this week without touching these two.
- `choose-your-leader-v7.html` — the known August set, unchanged and unsurprising: CLIPPED TEXT (3),
  DEAD BUTTONS (2), INERT TOUCHES (8) in world `#roomStage` (television, evening paper, telephone,
  doorway, bulletin, wall map). Byte-frozen since before 2026-10-12 — **8th identical run**. These stay
  REPEAT until someone opens the build; their disappearance is the signal worth shouting about, and
  it has not happened.
- `arcade.html` — CLEAN, unchanged bytes, 2nd consecutive clean run.
- `the-tell.html` — the recurring *14 controls showed no DOM change* line, explicitly flagged by the
  agent as **likely select-state, verify by eye, not asserted dead**. 8th run with that line. Not a
  finding, not counted, still not a fix ticket.

## Byte evidence — what actually moved

| Surface | md5 (12) | vs 2026-11-09 | findings |
|---|---|---|---|
| index.html | `55be71998ace` | **changed** (was `ec9c721a497a`) | DEAD BUTTONS (2) — unchanged across the edit |
| arcade.html | `95a6d717d4a6` | unchanged | CLEAN |
| choose-your-leader-v7.html | `98c3037f89d8` | unchanged | CLIPPED 3 · DEAD 2 · INERT 8 — all repeat |
| choose-your-leader-v6.html | `3e8388c22801` | unchanged | **CLIPPED TEXT (7) → none, on identical bytes** |
| the-tell.html | `5312b9da8012` | unchanged | 14 select-state controls, not asserted |

One surface moved this week, against four last week. A quiet week in the build and a loud one in the
instrument.

## Run notes

- Five surfaces, one invocation, exit 0, well inside the 560s ceiling. Plus one extra single-surface
  re-run of v6 for the reproducibility check above.
- `world '#roomStage' resolved from tsp-worlds.json` on v7 — expected and correct, the sidecar doing
  its job. v7 still does not declare its own world.
- Four of five surfaces still print `NO ROUTE — no entry in tsp-routes.json`. Only v7 has a route
  entry, so it remains the only surface whose endings are actually verified (`routes: 2 of 2 reached
  their ending`). Adding route entries for v6 and `the-tell.html` is still the cheapest way to turn
  this sweep from "nothing crashed" into "the story finishes" — carried forward from 2026-11-09,
  still not done.
- `choose-your-leader-v6.html` again logged a click timeout on `Sound` (already-active toggle,
  skipped rather than called dead) — unchanged note, present in both runs today and last week.
- Click depth: 40 on v7, v6 and the-tell; 24 on index; 8 on arcade. Identical to last week.
- **Ledger:** one row written to `FUNES-LEDGER.md` this run, verdict `CAUGHT` — not a build change
  but an instrument catch, which is what that verdict is for. No NEW and no confirmed FIXED build
  findings, so no SHIP row was written.
- Cost discipline per `CLAUDE.md`: no subagents, no full-corpus sweep, five named surfaces only, all
  browser work in bash inside the cloud container, two agent invocations (sweep + one re-run).

## What to do with this, shortest path first

1. **Close the v6 clipped-text ticket if one was opened on 2026-11-09.** The bytes never changed and
   the finding does not reproduce. Nothing to fix in that build.
2. **Add the 0px-box guard to `playthrough-agent.py`.** One condition at the CLIPPED TEXT assembly:
   a clip whose box measures 0px is a failed measurement, not a finding. This is the whole lesson of
   the week and it is cheap.
3. **v7 is still the real backlog** — eight inert touches and two dead buttons, frozen since August.
   Nothing will change there until someone opens the file.
4. Route entries for v6 and `the-tell.html` when convenient.

## Raw agent cards

Verbatim from the run, with consecutive identical lines collapsed as `[xN]` and multi-line button
labels joined with ` / ` — same convention as prior reports.

```
PLAYTHROUGH AGENT — 5 game(s)

┌─ index.html
│  verdict: NOTES   clicks: 24   end-reached: yes   seed: 1
│  · NO ROUTE — no entry in tsp-routes.json; endings not checked for this build
│  ✗ DEAD BUTTONS (2): Studio, Home
│  · 'Cabinet' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Flok / V35 Night shift on' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Kireji Pond Phrases dri' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Reading Lamp Trade over' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Dress Rehearsal Each sc' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The Asking Room Sit at ' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Sandbags Cut the weight' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Choose Your Leader — The' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The Arcade Everything, ' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Workshop in a Box Every' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The iSLO Suite Every ga' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'MASSBAY COMMUNITY COLLEG' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'ADVANTAGE RELOCATION · M' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'THE STUDIO ITSELF / The Ru' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The Ferry Crossing' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Dress Rehearsal: Dramati' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Reading the Fireground' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'EN195 Creative Writing: ' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'everything in the lab' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'What this studio is' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'How it runs' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Back' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
└────────────────────────────────────────

┌─ arcade.html
│  verdict: CLEAN   clicks: 8   end-reached: yes   seed: 1
│  · NO ROUTE — no entry in tsp-routes.json; endings not checked for this build
│  · 'How EN195 works: the cou' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Play Kireji Pond' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Play Reading Lamp' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Play Dress Rehearsal' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Play The Asking Room' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Play Sandbags' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Play Writerly Moves' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Dark mode' is an already-active toggle — skipped, not dead  [x12]
│  nothing mechanical to fix — ready for founder taste-play
└────────────────────────────────────────

┌─ choose-your-leader-v7.html
│  verdict: NOTES   clicks: 40   end-reached: yes   seed: 1
│  routes: 2 of 2 reached their ending
│    ✓ six eras, trust held (Some, then Mostly)
│    ✓ six eras, trust withheld (Not much)
│  ✗ CLIPPED TEXT (3) — laid out, then thrown away:
│      "The shelf" cut by 5px in div.walkbox (400px box, 417px of content) · after 'Walk the house'
│      "The back room" cut by 5px in div.walkbox (400px box, 417px of content) · after 'Walk the house'
│      "Touch the thing you were fixing" cut by 5px in div.walkbox (400px box, 417px of content) · after 'Walk the house'
│  ✗ DEAD BUTTONS (2): The shift / Ask for the hours you need / The, The back room / Touch the thing you were f
│  ✗ INERT TOUCHES (8) in world '#roomStage' (scope: #noticeRow button, #noticeRow [role=button]): The television, The evening paper, The telephone, The doorway, The bulletin, The wall map
│    the page changed but the world did not — text appeared outside the scene while the scene stayed byte-identical
│  · world '#roomStage' resolved from tsp-worlds.json — this build does not declare its own; a sidecar world is never silent
│  · 'Day' is an already-active toggle — skipped, not dead
│  · 'Text A' is an already-active toggle — skipped, not dead
│  · 'The television' is an already-active toggle — skipped, not dead  [x11]
│  · 'The evening paper' is an already-active toggle — skipped, not dead  [x11]
│  · 'The telephone' is an already-active toggle — skipped, not dead  [x11]
│  · 'The doorway' is an already-active toggle — skipped, not dead  [x11]
│  · 'The bulletin' is an already-active toggle — skipped, not dead  [x11]
│  · 'The wall map' is an already-active toggle — skipped, not dead  [x11]
└────────────────────────────────────────

┌─ choose-your-leader-v6.html
│  verdict: CLEAN   clicks: 40   end-reached: yes   seed: 1
│  · NO ROUTE — no entry in tsp-routes.json; endings not checked for this build
│  · 'Home' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Default' is an already-active toggle — skipped, not dead
│  · 'A' is an already-active toggle — skipped, not dead
│  · 'High contrast / On' is an already-active toggle — skipped, not dead
│  · 'Reduce motion / On' is an already-active toggle — skipped, not dead
│  · 'Colorblind cues / On' is an already-active toggle — skipped, not dead
│  · click timed out on 'Sound' — visible but not clickable in place
│  · 'Back' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Sound' is an already-active toggle — skipped, not dead  [x11]
│  nothing mechanical to fix — ready for founder taste-play
└────────────────────────────────────────

┌─ the-tell.html
│  verdict: NOTES   clicks: 40   end-reached: yes   seed: 1
│  · NO ROUTE — no entry in tsp-routes.json; endings not checked for this build
│  ? 14 controls showed no DOM change on click — LIKELY select-state (canvas/style redraw); VERIFY BY EYE, not asserted dead
│  · 'Studio' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Cabinet' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Back' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Home' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
└────────────────────────────────────────
```
