# Playthrough Sweep — 2026-11-23

**Run:** 2026-11-23 11:11 UTC · repo commit `0ee39e1` · agent `playthrough-agent.py` (reporter, always exits 0 — never a deploy gate)
**Surfaces swept (5):** index.html · arcade.html · choose-your-leader-v7.html · choose-your-leader-v6.html · the-tell.html
**Prior report:** `reports/playthrough-latest.md` @ 2026-11-16 (HTTP 200, 16,351 B) — 7 days back, a clean one-week diff
**Runner:** scheduled cloud routine, unattended. One invocation, exit 0. All five surfaces completed; none errored.

## Classification

| | count | detail |
|---|---|---|
| **NEW** | **0** | no finding line appeared that was not in the 2026-11-16 report |
| **FIXED** | **0** | no finding line cleared |
| **REPEAT** | **4 finding lines** | `index.html` DEAD BUTTONS (2) · v7 CLIPPED TEXT (3) · v7 DEAD BUTTONS (2) · v7 INERT TOUCHES (8) |

**Read this line and stop if you are busy:** no change since 2026-11-16. Nothing broke, nothing was
fixed, and **not one of the five swept files changed a byte.** All five md5s are identical to last
week's. This is the quietest possible result: the build stood still and the instrument agreed with
itself about it.

## The one thing worth your attention — last week's instrument fault held clean, but is still unguarded

Last week's report called out `choose-your-leader-v6.html` reporting **CLIPPED TEXT (7)** on
2026-11-09 and **CLEAN** on 2026-11-16 off byte-identical bytes, and diagnosed it as an instrument
fault: every one of those seven clip entries measured `(0px box, 0px of content)`, and a zero-width
box cannot clip text. The looping-animation settle path at `playthrough-agent.py:219`
(*"a looping animation never settles; measure anyway"*) can measure before layout exists and report
the nothing it found as a clip.

**This week v6 reports CLEAN again — same bytes (`3e8388c22801`), third consecutive identical
build, second consecutive clean run.** That is the diagnosis confirmed. The seven clips were never
in the file.

**But the guard was never added.** I checked the CLIPPED TEXT assembly in `playthrough-agent.py`
(lines 644–654): there is still no `boxH > 0` condition. The false positive is dormant, not fixed —
it fired once in three runs on unchanged bytes, so it can fire again on any surface with a looping
animation, and next time it may land on a file somebody *did* edit, where it will read as a real
regression. Compare v7's three clips this week, which carry real geometry — `(400px box, 417px of
content)` — and are credible findings.

The fix is still the one line last week asked for: at the CLIPPED TEXT assembly, drop any entry
whose measured box is `0px`. One condition, not a rewrite. It is the only open item in this sweep.

## REPEAT — 4 finding lines, summarised not listed

- `index.html` — DEAD BUTTONS (2): `Studio`, `Home`. Unchanged bytes this week (`55be71998ace`),
  and unchanged findings. These two have now survived an edit (last week) and a quiet week.
- `choose-your-leader-v7.html` — the known August set, unchanged and unsurprising: CLIPPED TEXT (3),
  DEAD BUTTONS (2), INERT TOUCHES (8) in world `#roomStage` (television, evening paper, telephone,
  doorway, bulletin, wall map). World resolved from `tsp-worlds.json` as designed — the
  "resolved from tsp-worlds.json" line is expected and correct. Both routes reached their ending.
- `arcade.html` — CLEAN, unchanged bytes, 3rd consecutive clean run.
- `choose-your-leader-v6.html` — CLEAN, unchanged bytes, 2nd consecutive clean run (see above).
- `the-tell.html` — 14 controls showed no DOM change on click, flagged `?` as LIKELY select-state
  (canvas/style redraw), **not asserted dead**. Identical to last week, down to the count. Still
  wants one pass by eye; still not a finding the agent is willing to assert.

## Byte evidence — what actually moved

| Surface | md5 (12) | vs 2026-11-16 | findings |
|---|---|---|---|
| index.html | `55be71998ace` | unchanged | DEAD BUTTONS (2) — repeat |
| arcade.html | `95a6d717d4a6` | unchanged | CLEAN |
| choose-your-leader-v7.html | `98c3037f89d8` | unchanged | CLIPPED 3 · DEAD 2 · INERT 8 — all repeat |
| choose-your-leader-v6.html | `3e8388c22801` | unchanged | CLEAN (2nd consecutive, same bytes) |
| the-tell.html | `5312b9da8012` | unchanged | 14 select-state controls, not asserted |

Zero surfaces moved this week, against one last week. Repo `HEAD` did advance
(`565e848` → `0ee39e1`), so work landed in the repo — just not in any of the five swept surfaces.

## Run notes

- Five surfaces, one invocation, exit 0. No surface errored; no Chromium launch fallback needed.
- `tsp-worlds.json` read automatically; v7's world `#roomStage` resolved from the sidecar as designed.
- No ledger row written this week. There were no NEW and no FIXED findings, and an append-only
  record of "nothing happened" is noise. `FUNES-LEDGER.md` is untouched by this run, deliberately.

## What to do with this, shortest path first

1. **Add the 0px-box guard to `playthrough-agent.py`** (CLIPPED TEXT assembly, ~line 644–654): skip
   any clip entry whose box measures 0px. One condition. This is the only open item here, and it is
   in the instrument, not the build — it protects every future sweep from a phantom regression.
2. **v7's eight inert touches and two dead buttons** remain the real build debt, carried since
   2026-08-28. Unchanged and not urgent, but they are the thing a founder taste-play would notice.
3. **`the-tell.html`'s 14 select-state controls** want one look by eye, once. The agent will keep
   declining to assert them, so this will repeat every week until a human confirms them.
4. Nothing else. `arcade.html` and `v6` are clean and ready for founder taste-play.

## Raw agent cards

Runs of identical consecutive lines are collapsed as `[xN]`; nothing else is edited.

```
PLAYTHROUGH AGENT — 5 game(s)

┌─ index.html
│  verdict: NOTES   clicks: 24   end-reached: yes   seed: 1
│  · NO ROUTE — no entry in tsp-routes.json; endings not checked for this build
│  ✗ DEAD BUTTONS (2): Studio, Home
│  · 'Cabinet' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Flok
V35

Night shift on' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Kireji Pond

Phrases dri' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Reading Lamp

Trade over' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Dress Rehearsal

Each sc' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The Asking Room

Sit at ' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Sandbags

Cut the weight' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Choose Your Leader — The' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The Arcade

Everything, ' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Workshop in a Box

Every' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'The iSLO Suite

Every ga' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'MASSBAY COMMUNITY COLLEG' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'ADVANTAGE RELOCATION · M' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'THE STUDIO ITSELF
The Ru' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
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
│  ✗ DEAD BUTTONS (2): The shift
Ask for the hours you need
The, The back room
Touch the thing you were f
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
│  · 'High contrast
On' is an already-active toggle — skipped, not dead
│  · 'Reduce motion
On' is an already-active toggle — skipped, not dead
│  · 'Colorblind cues
On' is an already-active toggle — skipped, not dead
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
