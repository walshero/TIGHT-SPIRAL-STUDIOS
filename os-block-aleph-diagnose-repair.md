# OS BLOCK — The Aleph Diagnose→Repair Protocol

> **SUPERSEDED OPERATIONALLY 2026-08-07 by `os-block-aleph-fleet.md`.** The thinking here
> is intact and still canon — three independent lenses, agreement as the trust metric,
> repair in confidence order, harden the tool that missed. What changed is that all of it
> ran *by hand*, so it ended when the session ended. The fleet block adds two lenses
> (aesthetic, learning science), a shared taxonomy so agreement is a count rather than a
> judgement, a blind-spot register so the feedback tooth survives a stall, and a ledger so
> a finding can be NEW / REPEAT / REGRESSED / FIXED. **Run the fleet block.** Read this one
> for why.

**One job:** turn "this file feels off" into a ranked, evidence-backed repair list —
and make the diagnostic tools *sharper every time they miss*. This is the studio's
repeatable quality loop, not a one-off review.

Proven on `old-problems-at-new-speed.html` (2026-07-26): three lenses, one synthesis,
repairs shipped, and the miss that slipped through **hardened the tool that missed it.**

---

## THE THREE LENSES (run all three, independently)

Diagnose the same artifact three ways. Independence is the point — each lens is blind
to the others, so agreement between them is signal, not echo.

1. **TSP as-is** — the studio's own gates, run literally:
   `studio-eyes/studio-fingers.py` (touch), `preship-gate-v4.py` (render), `ratchet.py`
   (floor), plus the founder floors (comfort = knob-not-wall; scene-first; single-file
   offline; back+home on every screen; 44px targets). Concrete and runnable.
2. **Game-based, 3rd-party public** — evaluate it AS A PLAYABLE using published
   frameworks: Nielsen's 10 heuristics, Desurvire HEP / PLAY, FTUE onboarding, game-feel
   ("action and reaction in the same place"). Does it *play*?
3. **Media-based, 3rd-party public** — evaluate it AS COMMUNICATION using published
   frameworks: NN/g above-the-fold & value-proposition, progressive disclosure, WCAG 2.2,
   Flesch–Kincaid readability, Robin Williams' CRAP. Does the message *land*?

Each lens returns a ranked list: **framework violated · concrete problem (element/line) ·
severity (blocker/major/minor) · specific fix.** No generic advice.

---

## THE ALEPH SYNTHESIS (one question: what is actually wrong?)

The Aleph merges the three lists into ONE ranked defect list, **weighted by agreement**:

- **★★★ all three agree** → highest confidence, fix first. (Here: *comfort is a wall,
  front-loaded before the scene* — flagged by all three independently.)
- **★★ two agree** → high confidence.
- **★ one lens, high value** → real, but a single perspective; judge it.

Agreement is the trust metric. A blocker only one lens sees is a hypothesis; a defect all
three name from different vocabularies is a fact.

---

## THE REPAIR RULE

Repair in confidence order: unanimous blockers → clean logic bugs → safe minors →
structural/voice changes (these last touch authored craft — surface them, let the
founder steer, don't unilaterally rewrite the piece's voice).

Every repair is re-verified by the **same** lens that caught it (fix the wall → the wall
gate must flip to pass). A repair that doesn't move its own gate isn't done.

---

## THE FEEDBACK TOOTH (why the system gets robust, not just the file)

**When Lens 1 (TSP tools) PASSES something Lens 2 or 3 catches, the tool has a blind
spot — repair the tool, not just the file.**

Worked example (2026-07-26): Studio Fingers PASSED the paper's comfort wall because
`F-WALL` only matched label-words ("bigger text", "softer") and the wall said
"Warm-dark / Dim the room / Default." Fix: added **container-based** detection — any
visible comfort/settings/theme container holding 2+ controls with no collapsing toggle is
a wall, regardless of wording. Re-verified: catches the paper, still passes Flok and Dad
Energy (real toggles), self-test green. The tool is now harder to fool.

This is the ratchet applied to the *diagnostics themselves*: every escaped defect becomes
a permanent new check.

---

## HOW TO RUN IT

1. Point all three lenses at the file (Lens 1 = you, running the scripts; Lenses 2 & 3 =
   two independent subagents, one game-framework brief, one media-framework brief).
2. Aleph-synthesize: dedup, rank by agreement, mark blocker/major/minor.
3. Repair in confidence order; re-verify each fix against its own gate.
4. If a TSP gate missed something the other lenses caught, harden the gate and re-run its
   self-test. Log it.
5. Ship on the git/Pages lane.
