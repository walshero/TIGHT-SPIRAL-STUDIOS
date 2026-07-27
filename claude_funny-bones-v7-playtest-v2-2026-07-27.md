# FUNNY BONES v7 — PLAYTEST RE-RUN through the v2 instrument
<!-- 2026-07-27 · same three personas (cold first-timer / kid / educator), v2 protocol (comprehension-first, behaviour trace, surprise+follow-up, felt map, retention-as-behaviour, worst-moment-as-problem). Compare to the v1 two-question run in claude_funny-bones-v7-review-2026-07-27.md. -->

## THE INSTRUMENT PROVED ITSELF (v2 vs v1)
The weak frame ("did it do its job / what surprised you") got us "neat but not sticky." The v2 protocol, on the *same build and same personas*, surfaced two things v1 could not:

- **A comprehension gap** (from the non-leading "what IS this?" asked FIRST): all three read **screen 1 as a toy that makes a cat laugh** — then screen 2 reveals a **prediction quiz**. *"I did NOT understand this was a guessing game… the guess idea only showed up on screen 2"* (first-timer). *"I was trying to make the cat actually LAUGH, not smile"* (kid). *"a calibration trainer wearing a Rube-Goldberg costume"* (educator). The opening and the product diverge. A "did it do its job?" question can never find this.
- **A structural bug** (from the behaviour-trace + real-number reasoning): **the headline payoff is unreachable from most setups.** The cat "cracks up" only at 6+/10 = **3 of 16 cells** (cat·Boing 6, kids·Chicken 8, web·Chicken 6). Both example openings drop the player into **Tired grown-ups, which caps at 4** — so "Make the cat laugh" is *impossible* in the room you start in. Found by an attentive tester computing the grid; invisible to opinion polling.

## CONVERGENT FINDINGS (ranked)

**A. The opening mis-sells the game (comprehension gap).** Screen 1 promises a toy; screen 2 delivers a quiz. Two fixes on the table: (i) let the machine BE a toy first — replayable, the cat reacts — and introduce the guessing as a second act (first-timer + kid instinct); or (ii) change the promise from *"Make the cat laugh"* to *"Read the room"* (educator). Either closes the gap; (ii) also fixes B.

**B. The headline payoff is unreachable from most setups (structural).** 6+ exists in only 3/16 cells and players open into a room that can't reach it. Fix: guarantee ≥1 "cracks-up" bit per room, **or** reframe the goal to "read the room." This also resolves the kid's core letdown: *"I did the whole thing and the cat didn't crack up… a polite smile and a grade."*

**C. `lastmiss` is unanchored and mis-carries (worst moment, educator).** It shows a bare "3 off" with no gag/room and **survives a room switch** — "same room, or find an easier one?" can be advice about a room you already left. *"Feedback with no anchor teaches the wrong lesson — I'll attribute the 3 off to whatever I'm now looking at."* Fix: stamp it `The Chicken · Tired grown-ups: 3 off`, and blank it the instant a bit or room changes.

**D. Everyone stops early — for the same reason (retention as behaviour).** First-timer: 1 more round ("answers are fixed → memorization"). Kid: **0** more rounds ("if the cat had cracked up I'd have chased it 3-4 times"). Educator: 3 rounds — "solved my corner and ran out of reasons," which for a calibration tool is a *soft failure* (norming should keep you moving across cases). Root cause: no progression, and the payoff is rare/unreachable, so calibration has no carrot.

**E. The machine is one-and-done (felt map).** The chain-fire is the unanimous peak and the only *Show-someone-this*; its back half and "Back to the machine" go **dead by round 2** (*"inert to me"*). The slider drew a flat *"nothing"* from the kid. Fix: replayable machine + the cat reacts on screen 1 (this is also fix A-i).

## DELTA TO THE EARLIER PUNCH-LIST
The v1 P1 items stand (replayable machine, celebrate the win, explain the disabled CTA, fix lastmiss). v2 **adds two P1-level items v1 missed** and sharpens one:
- **NEW P1 — fix the promise/product gap** (A): the opening has to mean what the game is.
- **NEW P1 — make the payoff reachable** (B): guarantee a crack-up per room, or reframe the goal to "read the room."
- **Sharpened:** lastmiss isn't just cosmetic — for a calibration tool, unanchored feedback *teaches the wrong thing* (C).

<!-- MANIFEST: the v2 instrument is validated (it found a comprehension gap + a structural
unreachability bug that v1 missed). Recommend folding A/B/C into the P1 build pass before
re-running the two standing axes. -->
