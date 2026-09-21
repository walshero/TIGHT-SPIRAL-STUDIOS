# Playthrough Sweep — 2026-09-21

**Run:** 2026-09-21T11:18Z · repo commit `273dc22` · agent `playthrough-agent.py` (reporter, always exits 0 — never a deploy gate)
**Surfaces swept (5):** index.html · arcade.html · choose-your-leader-v7.html · choose-your-leader-v6.html · the-tell.html
**Prior report:** `reports/playthrough-latest.md` @ 2026-09-14 (HTTP 200, 19,521 B)

## Classification

- **NEW: 0**
- **REPEAT: 7 finding lines** across 3 surfaces — every finding from 2026-09-14 reproduces
- **FIXED: 0** — nothing has cleared
- **CLEAN:** choose-your-leader-v6.html (clean four runs running)

**No drift, and the reason is now established rather than assumed.** Finding lines were compared as
sets, per surface: zero added, zero removed, on all five. The raw agent-card block of this run is
**byte-identical** to both 2026-09-14 and 2026-09-07 — md5 `ef99147cf086` three weeks running.

This run also checked *why*. All five swept builds were hashed against last week's commit
`03e3684`; **all five are byte-identical to it.** The repo moved (`03e3684` → `273dc22`), but
nothing in it touched these five files. Identical output from identical input is the instrument
working, not the instrument stuck — and the checksums below are the evidence rather than the claim.

| Surface | md5 (12) | vs 2026-09-14 |
|---|---|---|
| index.html | `3dd76ddee5c2` | unchanged |
| arcade.html | `db16d2f65732` | unchanged |
| choose-your-leader-v7.html | `98c3037f89d8` | unchanged |
| choose-your-leader-v6.html | `11865a501f35` | unchanged |
| the-tell.html | `a324c0e1e656` | unchanged |

No ledger row was written for this run. `FUNES-LEDGER.md` is append-only, and a row saying nothing
happened is the kind of entry that makes a ledger unreadable. Rows on change, silence otherwise.

## NEW — none

## FIXED — none

The v7 known state — eight inert touches (television, evening paper, telephone, doorway, bulletin,
wall map), two dead buttons, and the three clipped walkbox lines — **reproduces exactly, four weeks
running**. Its disappearance is still the signal worth shouting about, and it still has not
happened. v7 last changed 2026-08-26; nothing has touched it in the 26 days since. The inert
touches are a build defect waiting on a fix, not a finding that has settled.

**The standing read, fourth week unchanged:** this sweep is now confirming a known state rather
than discovering anything. Four identical reports is the report earning less each week. The fix is
upstream of the instrument — someone has to open v7 — and until that happens the weekly run's only
job is to catch the week the hashes move.

## REPEAT — 7 finding lines, summarised not listed

| Surface | Repeat finding lines |
|---|---|
| index.html | DEAD BUTTONS (1): Studio · JS ERRORS (9): `start`, `onHasParentDirectory`, `addRow` undefined |
| arcade.html | DEAD BUTTONS (1): Cabinet · OFFLINE FLOOR (1 external request, eclectic-youtiao-c065da.netlify.app) |
| choose-your-leader-v7.html | CLIPPED TEXT (3) in `div.walkbox` (400px box, 417px of content) · DEAD BUTTONS (2) · INERT TOUCHES (8) in world `#roomStage` |

The index.html JS error count held at 9 for the third week. That drift settled two runs ago.

## Run notes

- **All five surfaces completed in a single invocation**, ~9 minutes wall clock.
- `world '#roomStage' resolved from tsp-worlds.json` on v7 — expected and correct, the sidecar
  doing its job. v7 still does not declare its own world.
- `the-tell.html`'s 14 no-DOM-change controls are again reported as **likely select-state**
  (canvas/style redraw), explicitly *not asserted dead*. Unchanged for three runs. Not a fix ticket.
- `choose-your-leader-v6.html` again logged one click timeout on `Sound` and still scored CLEAN.
- Click depth steady: 40 on index, v7, v6 and the-tell; 10 on arcade.
- Run was unattended (scheduled, cloud container, no founder in the loop). No subagents, no
  full-corpus sweep — five named surfaces only.

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
