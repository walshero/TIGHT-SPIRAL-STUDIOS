# THE TABLEAU GATE + THE NEW ROOM
*Tight Spiral Studios · retrain order · 2026-07-12 · portable Markdown.*
*Companion to `studio-forward-guard.md` (what watches) and `tsp-delegation-charter.md` (who may act). This doc seats the room and grows one new tooth.*
*Amended 2026-07-12 (same day): Eagle Eye + Props Room seated in every rebuild; gate findings reframed as moves, not verdicts.*

---

## THE DIAGNOSIS (one line)

The games don't fail on beauty. They fail on the *first second*. Too many open with a control panel or a fork instead of one scene and one invitation — and the "scene-first floor" that should have caught it was a wish, not a check. Matt named it: *"Give me ONE small thing that matters at a time and let me expand as I'm ready."* That is now arithmetic.

The scene-first floor was already locked (2026-06-27, `choose-your-leader-map.md`): a game opens by landing the player in a scene, never a wall of text. Nothing ran it. This order gives it teeth and adds the two teeth it was missing — **one invitation** and **entry-tableau image share**.

---

## THE ROOM (who sits where, from 2026-07-12)

Voices argue from their published principles — the case each tradition would make, not literal quotes. Same convention as the existing panels.

| Seat | Who | The one thing they hold |
|---|---|---|
| **PM** | **Jared Cooney Horvath** *(attention & memory)* | Owns pipeline priority. *Protect the player's attention from everything competing for it.* Attention is the budget; one thing at a time is how you spend it. |
| Learning | **James Paul Gee** *(situated learning)* | Regime of competence — order the demands so each is *pleasantly* hard. Never two new demands in one scene. |
| Designed experience | **Kurt Squire** *(games as designed learning)* | Curated sequence over randomness; a difficulty curve, not a dump. *(retained)* |
| Narrative | **Ursula K. Le Guin** *(carrier bag)* | Scene first; gather, don't shoot; the story is the container. *(retained)* |
| Staging *(Pixar aleph)* | the storyboard tradition | One clear idea per frame; the stakes read at a glance; if the eye doesn't know where to look, the frame is broken. |
| Interface restraint *(Apple HIG aleph)* | the one-primary-action tradition | Exactly one primary action per screen; progressive disclosure — defer, don't dump; comfort lives in a corner control, never a gate. |
| Learning-game craft *(Filament aleph)* | the curriculum-games tradition | The mechanic *is* the learning act; playable in one sitting; classroom-real. |
| Low floor / wide walls *(MIT · Resnick–Papert aleph)* | the constructionist tradition | Trivial to start, room to grow, many paths — the literal engineering of "expand as I'm ready." |
| **Strategy scout** *(Eagle Eye)* | the opportunity vantage | **Sits in on every rebuild.** Names the impact / reuse / revenue angle the build isn't seeing; flags where one small move buys a large return. Strategic work, kept distinct from the craft. |
| **Staging bench** *(Props Room)* | the visual-craft floor | **Sits in on every rebuild.** Every prop carries its role; the objects in the frame carry the meaning before any text does; the majority-image tableau is built here, not bolted on afterward. |
| Reader proxies *(house)* | **AI Skeptic** · **TLDR Kids** | The five-second test: does a tired kid know what to do before reading a word? Skeptic asks what the screen is hiding. *(retained)* |

**Horvath as PM means:** when two voices conflict, attention wins the tie. A gorgeous frame that splits attention loses to a plainer frame that holds it.

**Eagle Eye and Props Room are not on-call — they sit in on every rebuild by default.** Strategy and staging stop being things we remember to add; they are in the room every time a game is touched.

---

## THE TABLEAU GATE (the new tooth — a check, not a wish)

Guard shape, same as the Forward Guard's four fields.

- **GATE.** Every game's *first paint* is one scene with one invitation. Three teeth:
  1. **No wall** — the opening is a scene, not a block of prose. *(scene-first floor, now measured)*
  2. **One invitation** — exactly one primary call-to-act on entry. Zero = mute; two-plus = a fork before the player has a reason to choose.
  3. **Entry tableau** — the first paint is majority image. *(Visual Constitution §13, measured at the entry, not just page-wide.)*
- **SCAN.** `one-thing-gate.py` renders the real first paint (headless Chromium, 1280×800) and computes: largest-visual share of the entry viewport, count of primary invitations, count of competing controls, prose-word count, emoji count. Fires at **scene-paint** (on any new/edited game) and at **belt close** (across the whole shelf).
- **ACT.** Ranks findings — WALL and emoji = CRITICAL, wrong invitation count = HIGH, sub-50% entry image / control clutter = WARN. Writes the run to the belt inventory, appends one line to the TSP Ledger. `exit 1` on any CRITICAL or HIGH: **the build does not ship until the move is made.**
- **ESCALATE.** The gate never publishes. It emits the move; the belt makes it in scratch (see below). What escalates to Matt is *which build to touch next* and *anything that would go to public web* — never a verdict to file.

**Thresholds (the arithmetic, all in one place in the script):** wall = >40 prose words with <20% entry image · invitation count must equal 1 · entry image floor 50% (WARN; `studio-eyes-sweep.py` keeps the hard page-wide image/contrast gate — one canon writes, others read) · control clutter warns above 3.

---

## MOVES, NOT VERDICTS (amended 2026-07-12)

A gate finding is not a grade to file and review later — it is *the move the build needs*. Matt does not review stale. So the pipeline changes shape:

- The gate emits a **move list** ("lead with one invitation · demote the bar to a corner knob · grow the frame past 50%"), not a verdict.
- Executing those moves **in scratch is GREEN** — drafting and building through Stage 5 already is. The belt *makes the move and rebuilds the game*, with **Eagle Eye and Props Room in the room**, instead of handing Matt a queue.
- What reaches Matt is the **improved build**, one at a time — never the finding. He reviews *forward motion*, not a backlog.
- Publishing the rebuilt game to public web stays **gated** (YELLOW/RED per the charter). Making the move is free; shipping it is his call.

---

## FIRST BITE (proof the tooth is sharp — 2026-07-12)

Run across two fixtures and one real build:

| Build | Entry image | Primary invites | Controls | Gate read |
|---|---|---|---|---|
| clean fixture | 78% | 1 | 1 | **PASS** — one scene, one invitation |
| **Funny Boney's Factory** | **43%** | **2** *(Step in / How this plays)* | **7** | **MOVE NEEDED** — two co-equal invitations, entry under 50% image |
| wall fixture | 0% | 0 | 1 | **MOVE NEEDED** — 85 words, no scene, no invitation |

The move list for Funny Boney's: **lead with the one invitation ("Step in") · demote the lens/comfort bar to a corner control (comfort is a knob, not a gate — already studio doctrine) · let "How this plays" be discovered, not co-equal · grow the frame to majority-image at entry.** None of it is a rewrite; it is a re-order.

---

## THE STANDING LOOP (learn and grow without being asked)

Ratified 2026-07-12: this is not a one-time retrain. The studio tightens on a cadence.

```
weekly sweep  ->  one-thing-gate.py over the whole shelf
      |
   moves ranked  ->  belt makes the re-order in scratch (Eagle Eye + Props Room in room)
      |            ->  Ledger line + one-line phone summary (builds moved, worst offender)
      |
   a FAILURE CLASS repeats (e.g. "control bars before the scene" on N games)
      |
   -> the studio DRAFTS a new panelist mandate or a new threshold to catch the class
      -> Matt ratifies at a belt close (RED stays gated; drafting is GREEN)
      |
   next sweep inherits the sharper tooth — the room gets deeper, the gate gets stricter, on its own
```

The recruitment habit is the growth engine: every recurring failure the sweep finds is a candidate for a new seat in the room or a new line in the gate. The studio proposes; Matt disposes. No new prose rules — only new checks and new voices tied to a check.

---

## AUTHORITY

- Seating the room, writing this doctrine, building and running the gate: **GREEN** (new additive canon + read-only audit).
- Rebuilding a game *in scratch* to clear the gate — moves made, Eagle Eye + Props Room in the room: **GREEN**. Matt sees the better build, not a verdict.
- The weekly sweep as a scheduled task: **YELLOW** (created, reported; it makes moves in scratch, never publishes).
- Publishing any rebuilt game to public web: **gated** (YELLOW/RED per the charter). Making the move is free; shipping is Matt's call.

*Repo canonization pending: this doc and `one-thing-gate.py` are on the Project shelf lane. Mirror to the GitHub repo at next belt so the raw CDN and shelf agree.*
