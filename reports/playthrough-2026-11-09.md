# Playthrough Sweep — 2026-11-09

**Run:** 2026-11-09 11:04 UTC · repo commit `4403701` · agent `playthrough-agent.py` (reporter, always exits 0 — never a deploy gate)
**Surfaces swept (5):** index.html · arcade.html · choose-your-leader-v7.html · choose-your-leader-v6.html · the-tell.html
**Prior report:** `reports/playthrough-latest.md` @ 2026-10-12 (HTTP 200, 22,125 B) — 28 days back, so this diff covers four weeks, not one
**Runner:** scheduled cloud routine, unattended. One invocation, exit 0. All five surfaces completed; none errored.

## Classification

- **NEW: 2** — `choose-your-leader-v6.html` CLIPPED TEXT (7), and a second dead button (`Home`) on `index.html`
- **FIXED: 1** — `index.html` JS ERRORS (9) cleared
- **REPEAT: 4 finding lines** across 2 surfaces (`index.html` 1, `choose-your-leader-v7.html` 3)
- **CLEAN:** `arcade.html` (third run clean, and again off changed bytes), `the-tell.html` (no asserted findings, off changed bytes)

**Four of five surfaces changed bytes since 2026-10-12.** After six weeks of a frozen diff this is the
first run where the instrument has something to say. Two things moved in opposite directions on the
same two builds: the front door got better, and v6 got worse.

## NEW — 2

### `choose-your-leader-v6.html` — CLIPPED TEXT (7). This is the one to look at.

v6 had been **CLEAN for six consecutive runs**. Its bytes changed this cycle (`11865a501f35` →
`3e8388c22801`) and it came back with seven clipped-text findings, three of them large and two of
them on story text a player has to read:

| Clipped line | Cut by | Where | When |
|---|---|---|---|
| "Choose Your Leader — October 22, 1…" | **158px** | viewport | first paint |
| "The map. Cuba. Eight days ago a U-…" | **200px** | viewport | after 'The map' |
| "The telephone. It has not rung ton…" | **119px** | viewport | after 'The telephone' |
| "Dusk" | 5px | `div.se-panel` | after 'Dusk' |
| "Warm-dark" | 5px | `div.se-panel` | after 'Warm-dark' |
| "Text size A+" | 6px | `div.se-panel` | after 'A+' |

The 158px cut is **at first paint, on the title** — the first thing a player sees is the thing that
is cut. The 200px and 119px cuts are the Cuba beat and the telephone beat: scene prose laid out and
then thrown away. These three are viewport-level, not container-level, which usually means a fixed
height or an overflow rule rather than one bad box.

Two caveats, stated rather than smoothed over:

1. **The agent reports `CLIPPED TEXT (7)` but prints six lines.** The count and the list disagree.
   That is an instrument discrepancy; six is what can be evidenced, so six is what is tabled above.
2. Every clipped box reports `(0px box, 0px of content)`. Zero-sized boxes mean the measurement is
   taken on an element the layout has collapsed, so trust the *fact* of the clip and the pixel
   amount, not the box geometry.

**Governance note, not an agent finding:** the three 5–6px clips sit on `Dusk`, `Warm-dark` and
`Text size A+`, and v6 also still exposes `High contrast`, `Reduce motion` and `Colorblind cues`
toggles. That is the retired comfort wall — `CLAUDE.md` (founder, 2026-08-29, amended 2026-10-13:
three modes on one icon-only button) says no preference panel, no text-size row. v6 still has one.
Whoever opens v6 for the clipping is already standing in front of the wall that is supposed to be
gone; cutting it removes three of the seven findings for free.

### `index.html` — DEAD BUTTONS went (1) → (2): `Studio`, `Home`

`Home` is new. `Studio` is the six-week repeat. Both are in the universal navigation that
`CLAUDE.md` names as the one universal home — the top `se-chrome` header and the bottom `se-rail`.
The front door was rebuilt this cycle (see byte evidence; the tile list is entirely different and
click depth fell 40 → 24), the rebuild cleared the JS errors, and it left **both** nav anchors dead.
Same pattern flagged on 2026-10-05 and 2026-10-12: index gets edited, index's own navigation does not
get re-tested. Two dead nav buttons on the studio front door is the cheapest high-visibility fix in
this report.

## FIXED — 1

### `index.html` — JS ERRORS (9) cleared

Gone: `start is not defined`, `onHasParentDirectory is not defined`, `addRow is not defined`. Nine
console errors on the front door, carried for at least five runs, now absent off changed bytes. That
is a real clearance, not a quiet file: the bytes moved and the errors did not come back. The three
undefined symbols looked like leftovers from another surface pasted into the front door; the rebuild
appears to have taken them out with it.

## REPEAT — 4 finding lines, summarised not listed

| Surface | Repeat finding lines |
|---|---|
| index.html | DEAD BUTTONS: `Studio` (7th run) |
| choose-your-leader-v7.html | CLIPPED TEXT (3) in `div.walkbox` (400px box, 417px of content) · DEAD BUTTONS (2) · INERT TOUCHES (8) in world `#roomStage` |

`choose-your-leader-v7.html` is the **only surface whose bytes did not move** (`98c3037f89d8`,
unchanged since 2026-08-26 — 75 days). Its known state reproduces exactly for the **seventh run**:
eight inert touches (television, evening paper, telephone, doorway, bulletin, wall map), two dead
buttons, three walkbox lines clipped by 5px. REPEAT until someone opens v7. Their disappearance
remains the signal worth shouting about; nothing to shout this week.

## Byte evidence — what actually moved

| Surface | md5 (12) | vs 2026-10-12 | findings |
|---|---|---|---|
| index.html | `ec9c721a497a` | **changed** (was `a9c0167e2af0`) | **JS ERRORS cleared; dead buttons 1 → 2** |
| arcade.html | `95a6d717d4a6` | **changed** (was `9b05b5afdbb4`) | **still CLEAN — no regression** |
| choose-your-leader-v7.html | `98c3037f89d8` | unchanged | identical, 7th run |
| choose-your-leader-v6.html | `3e8388c22801` | **changed** (was `11865a501f35`) | **CLEAN → CLIPPED TEXT (7)** |
| the-tell.html | `5312b9da8012` | **changed** (was `a324c0e1e656`) | no asserted findings, as before |

Four surfaces moved. Two held clean through the edit (`arcade.html`, `the-tell.html`) — a clean
verdict on *changed* bytes is worth more than a repeat, because it means an edit landed without
re-breaking anything the instrument can see. One improved and regressed at once (`index.html`). One
broke (`choose-your-leader-v6.html`). The frozen one is v7, which is frozen because nobody has
opened it since August.

## Run notes

- **The instrument itself changed since 2026-10-12.** Cards now print `seed: 1`, and four of five
  surfaces print `NO ROUTE — no entry in tsp-routes.json; endings not checked for this build`.
  Neither line appeared in the 2026-10-12 cards. These are agent-version notes, **not** build
  findings, and they are not counted in the classification above. The practical consequence is real
  though: only `choose-your-leader-v7.html` has a `tsp-routes.json` entry, so it is the only surface
  whose endings are actually verified (`routes: 2 of 2 reached their ending`). The other four are
  click-swept without ending checks. Adding route entries for v6 and the-tell would convert this
  sweep from "nothing crashed" to "the story finishes" on two more builds.
- One invocation, five surfaces, well inside the 540s ceiling. Last cycle needed two invocations
  against a 9-minute ceiling; this ceiling was not approached. Keep it.
- `world '#roomStage' resolved from tsp-worlds.json` on v7 — expected and correct, the sidecar doing
  its job. v7 still does not declare its own world.
- `the-tell.html` again reports **14 controls with no DOM change**, explicitly flagged *likely
  select-state (canvas/style redraw), VERIFY BY EYE, not asserted dead*. Seventh run with that line,
  but this time off **changed** bytes. Still not a fix ticket and still not counted as a finding.
- `choose-your-leader-v6.html` again logged a click timeout on `Sound` (already-active toggle,
  skipped rather than called dead) — unchanged note, but v6 no longer scores CLEAN around it.
- Click depth: 40 on v7, v6 and the-tell; 24 on index (was 40 — the front door has fewer tiles now);
  8 on arcade.
- **Ledger:** one row written to `FUNES-LEDGER.md` this run, because there are both NEW and FIXED
  findings.
- Cost discipline per `CLAUDE.md`: no subagents, no full-corpus sweep, five named surfaces only, all
  browser work in bash inside the cloud container, one agent invocation.

## What to do with this, shortest path first

1. **`index.html` nav** — `Studio` and `Home` are dead on the front door. Two anchors, one edit.
2. **`choose-your-leader-v6.html` first-paint title clipped 158px** — the first thing a player sees.
3. **v6 comfort wall** — cutting it per the standing ruling removes three of v6's seven findings and
   is a deletion, not a design task.
4. **v6 scene prose** (Cuba 200px, telephone 119px) — same overflow family as #2, likely same fix.
5. Everything on v7 stays parked until someone opens v7.

## Raw agent cards

```
PLAYTHROUGH AGENT — 5 game(s)

┌─ index.html
│  verdict: NOTES   clicks: 24   end-reached: yes   seed: 1
│  · NO ROUTE — no entry in tsp-routes.json; endings not checked for this build
│  ✗ DEAD BUTTONS (2): Studio, Home
│  · 'Cabinet' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Flok V35 Night shift on' navigates to another page (expected for a nav link) — returning to this file to keep testing it, not that one
│  · 'Kireji Pond / Phrases dri' navigates to another page (expected for a nav link)
│  · 'Reading Lamp / Trade over' navigates to another page (expected for a nav link)
│  · 'Dress Rehearsal / Each sc' navigates to another page (expected for a nav link)
│  · 'The Asking Room / Sit at ' navigates to another page (expected for a nav link)
│  · 'Sandbags / Cut the weight' navigates to another page (expected for a nav link)
│  · 'Choose Your Leader — The' navigates to another page (expected for a nav link)
│  · 'The Arcade / Everything, ' navigates to another page (expected for a nav link)
│  · 'Workshop in a Box / Every' navigates to another page (expected for a nav link)
│  · 'The iSLO Suite / Every ga' navigates to another page (expected for a nav link)
│  · 'MASSBAY COMMUNITY COLLEG' navigates to another page (expected for a nav link)
│  · 'ADVANTAGE RELOCATION · M' navigates to another page (expected for a nav link)
│  · 'THE STUDIO ITSELF / The Ru' navigates to another page (expected for a nav link)
│  · 'The Ferry Crossing' navigates to another page (expected for a nav link)
│  · 'Dress Rehearsal: Dramati' navigates to another page (expected for a nav link)
│  · 'Reading the Fireground' navigates to another page (expected for a nav link)
│  · 'EN195 Creative Writing: ' navigates to another page (expected for a nav link)
│  · 'everything in the lab' navigates to another page (expected for a nav link)
│  · 'What this studio is' navigates to another page (expected for a nav link)
│  · 'How it runs' navigates to another page (expected for a nav link)
│  · 'Back' navigates to another page (expected for a nav link)
└────────────────────────────────────────

┌─ arcade.html
│  verdict: CLEAN   clicks: 8   end-reached: yes   seed: 1
│  · NO ROUTE — no entry in tsp-routes.json; endings not checked for this build
│  · 'How EN195 works: the cou' navigates to another page (expected for a nav link)
│  · 'Play Kireji Pond' navigates to another page (expected for a nav link)
│  · 'Play Reading Lamp' navigates to another page (expected for a nav link)
│  · 'Play Dress Rehearsal' navigates to another page (expected for a nav link)
│  · 'Play The Asking Room' navigates to another page (expected for a nav link)
│  · 'Play Sandbags' navigates to another page (expected for a nav link)
│  · 'Play Writerly Moves' navigates to another page (expected for a nav link)
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
│  · 'The television' is an already-active toggle — skipped, not dead  [x12]
│  · 'The evening paper' is an already-active toggle — skipped, not dead  [x11]
│  · 'The telephone' is an already-active toggle — skipped, not dead  [x11]
│  · 'The doorway' is an already-active toggle — skipped, not dead  [x11]
│  · 'The bulletin' is an already-active toggle — skipped, not dead  [x11]
│  · 'The wall map' is an already-active toggle — skipped, not dead  [x11]
└────────────────────────────────────────

┌─ choose-your-leader-v6.html
│  verdict: NOTES   clicks: 40   end-reached: yes   seed: 1
│  · NO ROUTE — no entry in tsp-routes.json; endings not checked for this build
│  ✗ CLIPPED TEXT (7) — laid out, then thrown away:
│      "Choose Your Leader — October 22, 1" cut by 158px in viewport (0px box, 0px of content) · first paint
│      "Dusk" cut by 5px in div.se-panel (0px box, 0px of content) · after 'Dusk'
│      "Warm-dark" cut by 5px in div.se-panel (0px box, 0px of content) · after 'Warm-dark'
│      "Text size A+" cut by 6px in div.se-panel (0px box, 0px of content) · after 'A+'
│      "The map. Cuba. Eight days ago a U-" cut by 200px in viewport (0px box, 0px of content) · after 'The map'
│      "The telephone. It has not rung ton" cut by 119px in viewport (0px box, 0px of content) · after 'The telephone'
│  · 'Home' navigates to another page (expected for a nav link)
│  · 'Default' is an already-active toggle — skipped, not dead
│  · 'A' is an already-active toggle — skipped, not dead
│  · 'High contrast / On' is an already-active toggle — skipped, not dead
│  · 'Reduce motion / On' is an already-active toggle — skipped, not dead
│  · 'Colorblind cues / On' is an already-active toggle — skipped, not dead
│  · click timed out on 'Sound' — visible but not clickable in place
│  · 'Back' navigates to another page (expected for a nav link)
│  · 'Sound' is an already-active toggle — skipped, not dead  [x11]
└────────────────────────────────────────

┌─ the-tell.html
│  verdict: NOTES   clicks: 40   end-reached: yes   seed: 1
│  · NO ROUTE — no entry in tsp-routes.json; endings not checked for this build
│  ? 14 controls showed no DOM change on click — LIKELY select-state (canvas/style redraw); VERIFY BY EYE, not asserted dead
│  · 'Studio' navigates to another page (expected for a nav link)
│  · 'Cabinet' navigates to another page (expected for a nav link)
│  · 'Back' navigates to another page (expected for a nav link)
│  · 'Home' navigates to another page (expected for a nav link)
└────────────────────────────────────────
```

*Repeated already-active-toggle notes are collapsed as `[xN]` in this transcript; the agent printed each one on its own line. Everything else is verbatim.*
