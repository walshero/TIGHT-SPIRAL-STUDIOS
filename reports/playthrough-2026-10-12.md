# Playthrough Sweep — 2026-10-12

**Run:** 2026-10-12 · repo commit `6cb1ad5` · agent `playthrough-agent.py` (reporter, always exits 0 — never a deploy gate)
**Surfaces swept (5):** index.html · arcade.html · choose-your-leader-v7.html · choose-your-leader-v6.html · the-tell.html
**Prior report:** `reports/playthrough-latest.md` @ 2026-10-05 (HTTP 200, 21,420 B)
**Runner:** scheduled cloud routine, unattended. Two invocations — see Run notes. All five surfaces completed; none errored.

## Classification

- **NEW: 0**
- **FIXED: 0**
- **REPEAT: 5 finding lines** across 2 surfaces (`index.html`, `choose-your-leader-v7.html`)
- **CLEAN:** `arcade.html` (second run, and this time off changed bytes), `choose-your-leader-v6.html` (six runs running)

**No change since 2026-10-05.** The finding lines are byte-identical to last week's, line for line.
Last week broke a four-week stalemate; this week nothing moved either way.

## NEW — none

No finding appeared on any surface that was not already present on 2026-10-05.

## FIXED — none

Nothing cleared. Last week's `arcade.html` clearance holds — see below, where it is now
corroborated by a second signal rather than merely repeated.

## REPEAT — 5 finding lines, summarised not listed

| Surface | Repeat finding lines |
|---|---|
| index.html | DEAD BUTTONS (1): Studio · JS ERRORS (9): `start`, `onHasParentDirectory`, `addRow` undefined |
| choose-your-leader-v7.html | CLIPPED TEXT (3) in `div.walkbox` (400px box, 417px of content) · DEAD BUTTONS (2) · INERT TOUCHES (8) in world `#roomStage` |

The v7 known state — eight inert touches (television, evening paper, telephone, doorway, bulletin,
wall map), two dead buttons, three clipped walkbox lines — reproduces exactly for the **sixth week**,
off byte-identical bytes. v7 last changed 2026-08-26; nothing has touched it in the 47 days since.
These stay REPEAT until someone opens v7. Their disappearance is still the signal worth shouting about.

`index.html` is **unchanged this week** (`a9c0167e2af0`, same hash as 2026-10-05). Last week's note
stands unresolved: the front door was edited the week before and both of its defects were missed.
This week nobody touched it at all, so the count holding at 9 is a quiet file rather than a near-miss.

## Byte evidence — what actually moved

| Surface | md5 (12) | vs 2026-10-05 | findings |
|---|---|---|---|
| index.html | `a9c0167e2af0` | unchanged | identical |
| arcade.html | `9b05b5afdbb4` | **changed** (was `97082185c87a`) | **still CLEAN — no regression** |
| choose-your-leader-v7.html | `98c3037f89d8` | unchanged | identical |
| choose-your-leader-v6.html | `11865a501f35` | unchanged | CLEAN, as before |
| the-tell.html | `a324c0e1e656` | unchanged | identical |

**One surface moved, and it held.** `arcade.html` is the only swept build whose bytes changed this
week, and it came back CLEAN a second time. That is worth more than a repeat: a clean verdict on
unchanged bytes proves nothing but that the file sat still, whereas a clean verdict on *changed*
bytes means an edit landed on the cabinet without re-breaking the Cabinet link or re-introducing
the outbound fetch. Last week's fix is now corroborated rather than merely restated.

Its card is in fact identical to last week's line for line — same `clicks: 6`, same twelve
`Dark mode` already-active-toggle notes, same closing *"nothing mechanical to fix"*. An edit landed
on the arcade that the agent cannot see at all, which is what a safe edit looks like from this
instrument. Worth one founder eye on whether the change was meant to be visible; if it was, the
agent is the wrong witness for it and Studio Eyes is the right one.

The whole raw-card block below is byte-identical to the 2026-10-05 block. That is the cleanest way
to state this week's result: the instrument saw exactly what it saw last Monday.

No ledger row was written for this run. There are no NEW and no FIXED findings, and an
append-only record of "nothing happened" is noise — `FUNES-LEDGER.md` is deliberately untouched.

## Run notes

- **The sweep needed two invocations, which is a runner note and not a build finding.** The single
  five-surface call was cut at a 9-minute ceiling with `the-tell.html` still to go (last week's run
  took 9m53s, so the ceiling was set too tight, not the agent being slow). `the-tell.html` was
  re-run alone, exited 0, and its card is reproduced below unmodified. The first four cards come
  from the five-surface invocation. No surface errored, and nothing was skipped or inferred. Next
  run should allow ~12 minutes, or split the five surfaces into two calls up front.
- `world '#roomStage' resolved from tsp-worlds.json` on v7 — expected and correct, the sidecar doing
  its job. v7 still does not declare its own world.
- `the-tell.html` again reports **14 controls with no DOM change**, explicitly flagged *likely
  select-state (canvas/style redraw), VERIFY BY EYE, not asserted dead*. Unchanged for six runs, off
  unchanged bytes. Not a fix ticket, and not counted as a finding line.
- `choose-your-leader-v6.html` again logged click timeouts on `Sound` (an already-active toggle,
  skipped rather than called dead) and still scored CLEAN. Sixth run, same note, same bytes.
- Click depth: 40 on index, v7, v6 and the-tell; 6 on arcade.
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
