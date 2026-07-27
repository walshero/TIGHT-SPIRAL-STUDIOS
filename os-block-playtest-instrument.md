# OS BLOCK — PLAYTEST INSTRUMENT

**Status:** locked 2026-07-10 · **signal layer upgraded to v2, ratified 2026-07-27** (§3–§4 below; the six floors are unchanged). Full rationale: `claude_playtest-instrument-v2-2026-07-27.md`.
**Origin:** built twice with the same shape (CYL playtest layer, then Funny Boney's `funny-boneys-oops.html`). Two occurrences = a pattern that needs a spec before it drifts. This block turns the next wrapper into a fill-in, not a rebuild.
**Folds into:** OS §6 pipeline (playtest stage) + OS §7 patterns. Not a new standalone system — a named pattern under the existing pipeline.

---

## What it is

A capture layer that **rides on top of an existing playable build** — never a fresh game. The build stays untouched; the instrument is added, and can be stripped back out. Purpose: let a named playtester record phase-tagged thoughts and hand back one report, with the offline floor intact.

## The floor (every playtest wrapper carries all six)

1. **Rides on top, never rebuilds.** Copy the canonical build, add the layer, change nothing in the game logic. The base build must remain independently shippable.
2. **Phase auto-tag off the build's own choke-point.** Find the single function every screen transition already passes through (in Funny Boney's: `setRail(stage)`; in CYL: the screen-show call). Hook one line — `if(window.PT) PT.phase = stage;` — so notes tag themselves. Never make the tester say where they were.
3. **≤5 one-tap reactions — behaviour/feeling-anchored, never praise-skewed (v2).** Fixed set, tuned to the build. Default vocabulary: **Lost — didn't know what to do / Re-read · re-tapped / Something moved in me (tester flicks +/−) / Went dead here / Show-someone-this.** Plus one free-text box. These are behaviours and felt beats, not verdicts — dropped "I'd cut this" (asks the tester to design) and the praise-skewed old set (This landed / Delight …). Every tap phase-auto-tags itself (floor 2).
4. **Closing is an ADAPTIVE SEQUENCE, not a list of opinions (v2).** The spine: *never ask a question whose answer confirms the designer; capture what the player DID and MODELED; follow every surprise exactly once; keep the problem (data) apart from the tester's fix (a hunch); a signal without its rater is noise.* Standing v2 protocol — (a) **comprehension first, non-leading:** "in one line, what is this, and what were you trying to do?"; (b) **behaviour trace:** where did you stall / re-read / mis-tap / almost quit?; (c) **surprise WITH the follow-up:** "what did it do you didn't expect?" → "where exactly, and what did you expect instead?"; (d) **felt map:** where did you feel the most (±) and where nothing?; (e) **retention as behaviour:** "did you go again? how many rounds — and what made you stop?" (not "would you"); (f) **worst moment = the problem;** any tester-proposed fix is filed under a separate tag, "tester's hunch — not the data." Every report is stamped with **who played** (from the Who-Are-You panel). The founder may still swap specifics per build; the *shape* is the floor.
5. **Clipboard-only report.** One button assembles the whole session — notes in play order + closing answers — onto the clipboard. Tester pastes it back. **No per-screen email, no network emit, no storage.** This is a hard refusal (breaks the single-file offline floor).
6. **Accessibility floor unchanged.** Notebook control is a fixed 44px+ corner button, reachable immediately and always, keyboard-navigable, visible focus ring, works in all comfort stops. It is a live corner control, never a gate.

## Ship rule

The wrapper itself gets GATE 1 — founder cold-plays it once on phone to confirm the capture control is reachable and the report copies **on the tester's device class** — before it goes to the playtester. The playtester is the game's Gate 1; the founder is the wrapper's.

## Provenance line

Every wrapper states in-file: base build name + version, "playtest layer added [date]", offline badge. So the report reader knows exactly which build was played.

---

*Skill-file candidate after one more proven build (three total). Until then: this block is the spec; read it before building the next playtest layer.*
