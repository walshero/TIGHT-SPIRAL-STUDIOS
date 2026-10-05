# Playthrough Sweep — 2026-10-05

**Run:** 2026-10-05 · repo commit `fe67915` · agent `playthrough-agent.py` (reporter, always exits 0 — never a deploy gate)
**Surfaces swept (5):** index.html · arcade.html · choose-your-leader-v7.html · choose-your-leader-v6.html · the-tell.html
**Prior report:** `reports/playthrough-latest.md` @ 2026-09-21 (HTTP 200, 20,414 B)
**Runner:** scheduled cloud routine, unattended. Single invocation, 9m53s wall clock. All five surfaces completed; none errored.

## Classification

- **NEW: 0**
- **FIXED: 2 finding lines** — both on `arcade.html`, which is now CLEAN
- **REPEAT: 5 finding lines** across 2 surfaces (`index.html`, `choose-your-leader-v7.html`)
- **CLEAN:** `arcade.html` (new this week), `choose-your-leader-v6.html` (five runs running)

**The four-week stalemate broke.** After three byte-identical reports, a finding has actually cleared.

## FIXED — 2, and this is the headline

`arcade.html` went **NOTES to CLEAN**. Both findings it carried on 2026-09-21 are gone:

| surface | finding cleared |
|---|---|
| arcade.html | **DEAD BUTTONS (1): Cabinet** — the top-chrome Cabinet link registers a click again |
| arcade.html | **OFFLINE FLOOR (1 external request)** — `eclectic-youtiao-c065da.netlify.app` is no longer fetched; the cabinet now runs with no outbound call |

**This is a real fix, not instrument flake, and the hashes are the evidence rather than the claim.**
`arcade.html` changed on disk between the two runs (`db16d2f65732` → `97082185c87a`). A finding that
clears on a file whose bytes moved is a fix; a finding that clears on an unchanged file would have been
a reason to distrust the agent. The surface now prints *"nothing mechanical to fix — ready for founder
taste-play"*, and the agent's click depth on it fell from **10 to 6**, consistent with a dead control and
an external fetch both leaving the build rather than being papered over.

| Surface | md5 (12) | vs 2026-09-21 | findings |
|---|---|---|---|
| index.html | `a9c0167e2af0` | **changed** (was `3dd76ddee5c2`) | identical — the edit missed both |
| arcade.html | `97082185c87a` | **changed** (was `db16d2f65732`) | **2 cleared** |
| choose-your-leader-v7.html | `98c3037f89d8` | unchanged | identical |
| choose-your-leader-v6.html | `11865a501f35` | unchanged | CLEAN, as before |
| the-tell.html | `a324c0e1e656` | unchanged | identical |

**Worth a second look:** `index.html` also changed this week, and its findings did not move at all —
still the dead `Studio` button, still the same nine JS errors. Whoever touched the front door did not
touch either defect. That is the one place this week's diff suggests a near-miss rather than progress.

Neither the arcade fix nor the index edit was logged. No `FUNES-LEDGER.md` row exists for either, so
the clearance is recorded here and in the ledger row appended with this run.

## NEW — none

No finding appeared on any surface that was not already present on 2026-09-21.

## REPEAT — 5 finding lines, summarised not listed

| Surface | Repeat finding lines |
|---|---|
| index.html | DEAD BUTTONS (1): Studio · JS ERRORS (9): `start`, `onHasParentDirectory`, `addRow` undefined |
| choose-your-leader-v7.html | CLIPPED TEXT (3) in `div.walkbox` (400px box, 417px of content) · DEAD BUTTONS (2) · INERT TOUCHES (8) in world `#roomStage` |

The v7 known state — eight inert touches (television, evening paper, telephone, doorway, bulletin,
wall map), two dead buttons, three clipped walkbox lines — reproduces exactly for the **fifth week**,
off a byte-identical build. v7 last changed 2026-08-26; nothing has touched it in the 40 days since.
These stay REPEAT until someone opens v7. Their disappearance is still the signal worth shouting about.

The `index.html` JS error count held at 9 for the fourth week — but see the note above: that file *did*
change this week, so the count holding is now a missed opportunity rather than a quiet file.

## Run notes

- `world '#roomStage' resolved from tsp-worlds.json` on v7 — expected and correct, the sidecar doing
  its job. v7 still does not declare its own world.
- `the-tell.html` again reports **14 controls with no DOM change**, explicitly flagged *likely
  select-state (canvas/style redraw), VERIFY BY EYE, not asserted dead*. Unchanged for five runs, off an
  unchanged build. Not a fix ticket, and not counted as a finding line.
- `choose-your-leader-v6.html` again logged one click timeout on `Sound` and still scored CLEAN. Fifth
  run with the same note, same bytes.
- Click depth: 40 on index, v7, v6 and the-tell; **6 on arcade (was 10)**.
- Cost discipline per `CLAUDE.md`: no subagents, no full-corpus sweep, five named surfaces only, all
  browser work in bash inside the cloud container.

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
│  verdict: CLEAN   clicks: 6   end-reached: yes
│  · 'Play Kireji Pond' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Play Reading Lamp' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Play Dress Rehearsal' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Play The Asking Room' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Play Sandbags' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Dark mode' is an already-active toggle — skipped, not dead
│  · 'Dark mode' is an already-active toggle — skipped, not dead
│  · 'Dark mode' is an already-active toggle — skipped, not dead
│  · 'Dark mode' is an already-active toggle — skipped, not dead
│  · 'Dark mode' is an already-active toggle — skipped, not dead
│  · 'Dark mode' is an already-active toggle — skipped, not dead
│  · 'Dark mode' is an already-active toggle — skipped, not dead
│  · 'Dark mode' is an already-active toggle — skipped, not dead
│  · 'Dark mode' is an already-active toggle — skipped, not dead
│  · 'Dark mode' is an already-active toggle — skipped, not dead
│  · 'Dark mode' is an already-active toggle — skipped, not dead
│  · 'Dark mode' is an already-active toggle — skipped, not dead
│  nothing mechanical to fix — ready for founder taste-play
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
