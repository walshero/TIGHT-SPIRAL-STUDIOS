# OS BLOCK — PLAYTEST INSTRUMENT

**Status:** locked 2026-07-10
**Origin:** built twice with the same shape (CYL playtest layer, then Funny Boney's `funny-boneys-oops.html`). Two occurrences = a pattern that needs a spec before it drifts. This block turns the next wrapper into a fill-in, not a rebuild.
**Folds into:** OS §6 pipeline (playtest stage) + OS §7 patterns. Not a new standalone system — a named pattern under the existing pipeline.

---

## What it is

A capture layer that **rides on top of an existing playable build** — never a fresh game. The build stays untouched; the instrument is added, and can be stripped back out. Purpose: let a named playtester record phase-tagged thoughts and hand back one report, with the offline floor intact.

## The floor (every playtest wrapper carries all six)

1. **Rides on top, never rebuilds.** Copy the canonical build, add the layer, change nothing in the game logic. The base build must remain independently shippable.
2. **Phase auto-tag off the build's own choke-point.** Find the single function every screen transition already passes through (in Funny Boney's: `setRail(stage)`; in CYL: the screen-show call). Hook one line — `if(window.PT) PT.phase = stage;` — so notes tag themselves. Never make the tester say where they were.
3. **≤5 one-tap reactions.** Fixed set, tuned to the build. Default vocabulary: This landed / I snagged / Confused me / I'd cut this / Delight. Plus one free-text box.
4. **3 founder-chosen closing questions.** Founder names them per build. Standing default: (a) did the core loop do its job; (b) what surprised you; (c) one thing to fix first.
5. **Clipboard-only report.** One button assembles the whole session — notes in play order + closing answers — onto the clipboard. Tester pastes it back. **No per-screen email, no network emit, no storage.** This is a hard refusal (breaks the single-file offline floor).
6. **Accessibility floor unchanged.** Notebook control is a fixed 44px+ corner button, reachable immediately and always, keyboard-navigable, visible focus ring, works in all comfort stops. It is a live corner control, never a gate.

## Ship rule

The wrapper itself gets GATE 1 — founder cold-plays it once on phone to confirm the capture control is reachable and the report copies **on the tester's device class** — before it goes to the playtester. The playtester is the game's Gate 1; the founder is the wrapper's.

## Provenance line

Every wrapper states in-file: base build name + version, "playtest layer added [date]", offline badge. So the report reader knows exactly which build was played.

---

*Skill-file candidate after one more proven build (three total). Until then: this block is the spec; read it before building the next playtest layer.*
