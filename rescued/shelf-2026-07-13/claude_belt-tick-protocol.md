# The Belt Tick — lossless capture, one tick per chat entry

*Tight Spiral Studios operating standard. Answers the question: how do we make each entry in a TSP chat advance the timing belt so no win, insight, or asset is ever lost? Proposed as a rule for the OS; drafted 2026-07-13.*

---

## The problem it solves

Right now a chat produces real value — a build, a design decision, a panelist verdict, a bug caught — and most of it evaporates when the chat ends. "Nothing survives a chat unless it's pushed." The belt (the studio's turn-by-turn OS cycle) moves builds and catches bugs, but it does not force *capture*. So the studio re-derives what it already knew, and wins don't compound across chats. Lossless work means: every turn ends by writing durable state, so the next chat — or a colleague — starts from what's already been learned, not from zero.

## The rule (one line)

**No substantive turn ends without a Belt Tick: a four-beat append to the Ledger.** If a turn produced nothing durable, the tick says so explicitly — silence is not allowed, because a silent gap reads as "covered" when it wasn't.

## The four beats

Each tick is a short, dated, append-only block. Four beats, one line each:

1. **BUILT** — the artifact or decision this turn produced. Name the file and the lane. *("cliche-field.html — added one-button 5-mode comfort toggle incl. screen-reader-playable mode; shelf.")*
2. **LEARNED** — the insight worth keeping so it isn't re-derived: a design principle, a panel verdict, a gotcha, a measured fact. *("`updateHUD` ran before `state=PLAY`, so the SR layer never re-rendered — set state before the HUD refresh.")*
3. **LANDED** — where it was saved and how it was verified. Lane + proof, never "success: true." *("shelf via project_write; embedded copy in PLAY file byte-matches standalone — diffed.")*
4. **NEXT** — the single next action, owned, phrased as a decision not a question. *("Roll comfort toggle to Cabinet, Line, City; then Line fuse redesign; then publish.")*

That's it. Thirty seconds. The discipline is that it happens *every* turn.

## Where it lands

The tick appends to the existing **`TSP Ledger.md`** — the ledger is the belt's long-term memory, and it already carries dated KD! appends. The Belt Tick formalizes what a KD! append must contain (the four beats), so the ledger becomes a complete, append-only history of what the studio built, learned, where it lives, and what's next. Reading the tail of the ledger is how any new chat "spins up to speed" losslessly.

## The asset index (so wins are reusable, not just recorded)

Recording isn't enough for the *collective* job — a colleague or a future chat has to be able to *find and reuse* an asset. So the tick has one optional fifth move: if the turn produced a **reusable asset** (a spec, a panel doc, a component, a validated pattern), add a one-line entry to a running **`studio-asset-index.md`**:

`asset · what it's for · path · reuse note`

Example rows this suite already earns:
- `Design panel (Zimmerman/Squire/Le Guin/Horvath) · argue a game mechanic from theory · claude/cliche-games-design-panel.md · reuse the four-voice format for any build's dynamics`
- `Comfort toggle · one-button, five-mode accessibility incl. screen-reader-playable · in cliche-field.html · lift the module (CF[], cfApply, refreshSR) into any studio page`
- `Train-Up coach pattern · show-don't-tell onboarding with agent coaches · in cliche-field.html · reuse to train staff on any skill`

The index turns one-off wins into studio infrastructure — the difference between a studio and a pile of chats.

## Why this makes the belt "tick" per entry

The belt was a set of *checks* that ran each turn (PATTERN-TICK, VISUAL-TICK). The Belt Tick adds the missing beat: a *capture* that runs each turn. Checks keep a build on the rails; the tick keeps the *knowledge* on the rails. One append per entry, and the studio stops leaking.

## If a rule can't be a check, it's a wish — so here's the check

Per the OS's own doctrine, this only counts if it's enforceable, not exhortation. The check: **a turn that writes a file to a lane but adds no Ledger tick is out of spec.** A cheap automated version: a scheduled Integrity-Guard beat that diffs "files changed on the shelf since last tick" against "ticks appended since last run" and flags any build with no matching tick. That makes losslessness arithmetic, not diligence.

---

## This turn's tick (worked example)

**BUILT** — `cliche-field.html` / `PLAY-Cliche-Cabinet.html`: one-button comfort toggle cycling Studio → High Contrast → Calm → Large Print → Screen Reader, persisted studio-wide (`tsp_comfort`); the Screen Reader mode is fully playable via labeled buttons + an aria-live region. Shelf.
**LEARNED** — order-of-operations bug: refreshing the accessible layer before setting `state=PLAY` left it stale; always set state, then refresh views. Also: `localStorage` keyed studio-wide (`tsp_comfort`, `tsp_cliche_bank`, `tsp_revisions`) makes settings and progress follow the player across every cartridge for free.
**LANDED** — shelf via `project_write` (field + PLAY); suite rebuilt and verified (comfort button present in embedded Field, SR-mode win reached through its buttons, zero console errors).
**NEXT** — (owned, no PM ask): roll the comfort toggle to Cabinet + Line + City → rebuild Cliché Line as the fuse-and-clear design (fixes "too fast") → publish the one file to GitHub Pages for the tap-and-play link.
