# ALEPH A3 — LEARNING SCIENCE & EVIDENCE
## Six-month consultation, Tight Spiral Studios
**Seat:** does any of this actually teach, and what evidence would prove it?
**Date:** 2026-08-07 · **Method:** primary-source read of the repo, the L5 lens run, and the games themselves — no other seat's output consulted.

---

## 0. The one-line finding

Until today, nothing in this studio checked whether a build taught anything, and the first time something did, it found the flagship composition game's entire response to a student's written reasoning is `mine.card===preset.card` — a string compare on which of 8 buttons they pressed. That is not a rounding error. That is the whole grade.

---

## 1. Month-0 diagnosis: what these builds actually do pedagogically

### 1.1 `the-tell.html` — the case in evidence, and it is worse than the headline

I re-derived the L5 run (`aleph-runs/2026-08-07-the-tell/L5.json`) against the live file rather than trust the summary. It holds.

**The construct is real and well-chosen.** The header comment (`the-tell.html:6-10`) states the design honestly: "a flash piece carries a face-down tag a PRIOR READER placed. You read, call the move, WRITE YOUR WHY (the evidence), then FLIP to compare." Commit-before-flip is a legitimate retrieval-practice structure — the student must generate a judgment before seeing a model answer, which is the right shape for Nunan's task-based principle the studio's own OS invokes (`tight-spiral-studio-os.md:100`). The 8+8 card taxonomy (writerly moves vs. workshop moves) is a real disciplinary distinction pulled from the founder's own "Workshop Moves" handout, attributed (line 17).

**Then the loop breaks at the exact point that was supposed to be the point.** `renderFlip()` (lines 513-518):

```js
var same=(mine.card===preset.card);
```

That is the entire assessment. The student's typed answer in `#why` — the field the header comment itself calls "the evidence," the thing the whole exercise exists to produce — is written to the DOM via `esc()` at line 523 and never read by any comparison, scoring, or branching logic anywhere in the file. I confirmed this by reading the full 858-line file: `why` appears only as a string that gets displayed back, never as an input to a conditional. The commit gate that decides whether a student's turn even counts is `why.value.trim().length>=3` (line 504) — three characters. In the L5 playthrough, the string `"abc"` cleared the gate and produced the same verdict text a real, evidenced answer would have produced ("Both can be defended — that is the workshop").

This is a **construct-response interface wrapped around a construct-free engine**. It looks like it assesses written reasoning. It assesses button choice.

Three compounding findings from the same run, all independently verifiable against the source:

- **`MISCONCEPTION-UNADDRESSED`** — of the 8 cards on any given span, 7 are unconditionally validated as "defensible" regardless of which one the student picked (line 518's diff branch has no per-card content). Span B ("three of them") is preset as `Overpacked Suitcase`; the predictable student miscall — that any concrete detail is automatically good specificity (`World Detail That Matters`, a different card) — is never named, contrasted, or corrected. A student who walks in with that misconception walks out with it affirmed by the interface.
- **`TRANSFER-UNSUPPORTED`** — one text ("The Spare Key"), and the two lenses' spans are disjoint sets (`writerly: ['A','C','E']`, `workshop: ['N','B','D']`, line 423) — no line in the piece is ever read through both decks, so nothing varies against a constant and nothing generalizes past this one passage.
- **`RUBRIC-UNLINKED`** — the verdict text asks the student twice to judge "is your evidence as strong as theirs?" and the export at `#close` calls the artifact "a workshop comment set — a real one, with evidence" for a peer or instructor to read. No criterion for what makes evidence strong appears anywhere on the surface. `close-the-loop.html` and `scorer-norming.html` both load real MassBay rubric text elsewhere in this same studio (see 1.3) — the pattern exists in the codebase. It just wasn't reused here.

And the outcome map is stale in a way that matters for evidence: `islo-hub.html:421` files The Tell under Graduation Competency 1 with the blurb "Ten craft moves, and the reader-test for each," but the shipped file has an 8+8 deck. A faculty member reading the hub cannot tell what this build actually measures, because the hub's own description of it is wrong.

### 1.2 This is not a universal indictment of the studio — the spread matters

I checked three other ISLO-suite builds against the same question (does the feedback loop read the student's actual reasoning, or a proxy for it):

- **`who-holds-the-room.html`** does noticeably better. Lines 606-609 pull a real rubric level and render the *next* rung up (`"One rung up (level "+up+"): "+advByNum(up)`) — feed-forward, not just right/wrong, tied to the verbatim MassBay ISLO #5 rubric text loaded at line 428 ("the exact rubric faculty use to score the graduation portfolio... never ranks you against a classmate"). This is closer to Hattie & Timperley's three questions (where am I going / how am I doing / where next) than anything in The Tell.
- **`update-the-model.html`** states the construct explicitly in its own metadata comment (line 14: `tsp:measure — AAC&U Scientific Reasoning — Hypothesis · Evidence · Revision. No normed MassBay rubric yet`) and structures the loop as predict → commit to a falsification criterion → meet evidence → revise "by however much the evidence earns" (line 263) — a real hypothesis/test/revision cycle, honestly labeled as unnormed.
- **`sticker-price.html`** and its sibling `real-cost.html` use a guess-first-then-reveal structure against a fixed answer (arithmetic, amortization) — a domain where a string/number compare is actually a valid check, because the target *is* a fact, not a judgment.

The pattern: **builds whose target is a fact tolerate a shallow check; builds whose target is a judgment (The Tell) need a rubric-shaped check and don't have one.** The Tell is not an outlier because the studio doesn't know how to do better — `who-holds-the-room.html` sits in the same repo and does the harder thing. It's an outlier because nothing checked for the gap between "looks like an evidence-graded workshop tool" and "is one" until the L5 lens ran today.

### 1.3 The measure side is real but thin, in the founder's own assessment

`close-the-loop.html` records results per rubric dimension rather than one holistic score — this is a direct, named response to the founder's own written critique of the ISLO scoring initiative (`ISLO-SCORING-REFLECTION-2026-mwalsh.md:28`): *"the holistic model of assessment that we use doesn't capture important information about specific learning objectives... we currently collect no data about areas of student strength or weakness."* That's a real diagnosis-to-fix chain, and it's worth crediting: the founder identified the exact failure mode (holistic score, no per-skill signal) that his own studio's flagship writing game (The Tell) then also fell into, independently, a week later.

But per the proposal doc (`ISLO-GAME-SUITE-PROPOSAL.md:34-35`), only **2 of 7** outcomes (Written Communication, DEI) have a locally-normed rubric; Critical Thinking's is "in development"; four outcomes (Quantitative, Tech/Info-Sci, Natural World, Personal/Civic) have no locally-normed instrument at all — the games for those four outcomes are scored against "suite-proposed criteria," which is the studio's own honest label for "we wrote a plausible rubric, nobody at MassBay has normed it."

### 1.4 Named against the frameworks in `aleph-lenses/L5.md`

- **Constructive alignment (Biggs):** fails on The Tell specifically — outcome (write defensible textual evidence), activity (write in a textarea), and assessment (which of 8 buttons was clicked) do not point at the same thing. Passes, provisionally, on `who-holds-the-room.html`, where the rubric level shown is the rubric level the founder says faculty actually use.
- **Retrieval/generation:** The Tell genuinely asks the student to generate before seeing the model answer — that part of the design is sound. The failure is downstream of generation, not in it.
- **Formative feedback (Hattie & Timperley):** feed-forward exists ("Read both whys. Which evidence convinces you?"); feed-up and feedback-on-performance do not, because performance was never scored.
- **Desirable difficulty vs. confusing interface:** the L5 run also found `SPLIT-ATTENTION` (measured at 390×844: opening a tag spot leaves the passage entirely off-screen — 0px of it visible — while the student chooses among 8 cards and writes evidence about text they can no longer see) and a data-destroying control (`LABEL-AMBIGUOUS`: "Read it the other way" silently wipes every written answer, verified going from "1 of 3" tagged to "0 of 3" with no confirm). These are genuine extraneous load, not productive struggle — they cost effort on the interface, not on the idea.

---

## 2. What evidence would count — to three different audiences, without becoming a research project

Be precise about *whose* bar this is, because the three bars are different heights.

**To the founder** (lowest bar, highest trust — he already believes in the pedagogy spine): evidence that a build's scored output actually reflects what the student wrote, not what they clicked. This is checkable today, offline, by the L5 lens itself, run against every shipped build. No classroom needed. The Tell's `mine.card===preset.card` is the kind of thing a code read catches; it doesn't need a semester.

**To MassBay** (the ISLO scoring initiative bar): per-dimension rubric scores on real MassBay rubric language, produced by real student work, normed the way the founder's own initiative normed the portfolio scoring — multiple readers, a norming session, an inter-rater check. `scorer-norming.html` (The Norming Table) already builds the *mechanic* for this — score sample excerpts, meet the normed score, feel the disagreement collapse. What's missing is real EN195 artifacts run through it, not more mechanic. This is the honest evidence tier: it proves the rubric is applied consistently, not that the game caused the growth.

**To an outside adopter** (the highest bar, and the one the studio's own SWOT names as missing — "no external proof point," `CONSULT-GROUNDING-2026-08-07.md:99`): one build, one term, a pre/post comparison on a rubric dimension the founder already trusts (Written Communication or DEI, the two live rubrics), with an n large enough to say something and small enough to be one class section. This is not a study — no IRB, no control group, no publication claim. It's "here is a rubric score before the unit and after it, on real MassBay language, for the students who consented to have their work used this way" (which the studio's own settled ruling already permits — published/consented student work is not a FERPA question here, `CLAUDE.md`).

**What would NOT count**, and I'd say so if asked: completion counts, time-on-task, "students said they liked it," or click-through funnels. None of those are evidence of learning. They're evidence of engagement, which this studio already has other lenses for (L2, L3). Conflating them with the learning claim is exactly the move I'd refuse in §5.

---

## 3. The phased plan

### Months 1-2 — fix the instrument before trusting it

1. **Run the L5 lens against the rest of the shipped ISLO suite**, not just The Tell — at minimum `who-holds-the-room.html` (already scored well informally above, but not yet run through the formal lens), `update-the-model.html`, `sticker-price.html`, `score-the-room.html`, and `real-cost.html`. Seven outcomes, nineteen-plus games (`ISLO-GAME-SUITE-PROPOSAL.md` §3) — the studio does not yet know, in the aggregate, how many of them share The Tell's failure mode versus who-holds-the-room's better one.
2. **Fix The Tell specifically**, because it is the flagship of the strongest-covered outcome (Written Communication, `ISLO-GAME-SUITE-PROPOSAL.md:64` — "strongest lane") and because the fix is well-scoped by the L5 findings themselves: author per-(span, card) response content for the 7 non-matching cards per span (splitting them into "defensible" vs. "not supported by these words" — the `MISCONCEPTION-UNADDRESSED` fix), replace the 3-character gate with something that requires the answer to engage the actual span (e.g., must quote a fragment of the tagged text), and put the rubric criteria the verdict is silently applying into visible text next to the `#why` field (the `RUBRIC-UNLINKED` fix). This is authored content work, not new architecture — the engine (commit-before-flip, two decks, carry-out) is sound and shouldn't be rebuilt.
3. **Correct the hub-to-build drift**: `islo-hub.html:421`'s "Ten craft moves" blurb against the shipped 8+8 deck, and put one line on `#scene` naming the actual outcome and rubric dimension this build feeds (the `OUTCOME-UNMAPPED` fix) — cheap, and it's the difference between a student being able to say what they practiced and not.

### Months 3-4 — get one real evidence artifact, on the outcome that's already strongest

Run The Tell (post-fix) and `who-holds-the-room.html` in the actual EN195 classroom, on real assignments, scored against the live rubrics (Written Communication VALUE for The Tell's outcome, ISLO #5 for Who Holds the Room). Use `scorer-norming.html` for the norming pass. This is the month the studio gets its first per-dimension score data from real students on a build that has been checked to actually assess what it claims to assess — not a new instrument, the existing measure-side tools (`close-the-loop.html`, `scorer-norming.html`) pointed at real classroom output for the first time.

I would **not** spend months 3-4 building the EN Placement Skill-Scorer the brainstorm doc ranks highest (`ISLO-GAPS-BRAINSTORM.md:20-23`) — it is explicitly **parked**, its premise (EN98-vs-EN101 placement) is **void** (MassBay is a co-req pioneer with no developmental courses, confirmed by the founder 2026-07-30), and it is waiting on a founder briefing on the co-req model that hasn't happened. Building evidence infrastructure for a placement mechanism that doesn't exist is exactly the kind of confident-but-wrong move this consultation exists to prevent.

### Months 5-6 — one defensible outcome claim, and only one

By month 6, the studio should be able to say, in the founder's own voice, something like: *"On [The Tell / Who Holds the Room], EN195 students' [Sources & Evidence / Advocacy] rubric scores moved from [X] to [Y] across N students in one term, scored on MassBay's own rubric by a norming process modeled on the college's 2026 ISLO initiative."* That is one outcome, one rubric dimension, one term, real numbers, no inference beyond what the numbers show. It is not "the studio's pedagogy works" — it's "this one build, checked, produced this one measured change." That's the legible PoC win the SWOT names as the missing next move (`CONSULT-GROUNDING-2026-08-07.md:107`), sized to what one term of one class can actually produce.

---

## 4. The instrumentation question

**What the builds should capture:** the rubric-dimension score or level itself (a number 0-4, a level name), computed locally, at the moment of assessment — not the free text that produced it. `who-holds-the-room.html`'s pattern (compute the level, show the level and the next rung, keep the underlying advocacy-move choice on-device) is the right shape to generalize. For the norming/close-the-loop side, the capture is explicitly per-dimension, which is the entire point per the founder's own reflection (§1.3).

**What the builds must not capture:**

- **No raw student text leaves the device by default.** This repo's offline-first floor is real and load-bearing — every ISLO-suite build I checked is single-file HTML with zero network calls (`ISLO-GAME-SUITE-PROPOSAL.md:141`: "single-file, offline, zero network calls"). The Tell's own header comment states the FERPA floor explicitly (line 18): "Neutral studio-written piece (FERPA floor: never real student work)" — for the *source text in the game*. That same floor has to extend to *student-authored answers*: nothing typed into `#why` should ever transmit anywhere without an explicit, separate opt-in the student makes at the point of sharing — which is precisely what The Tell's own carry-out screen already does correctly ("I chose to share this. Nothing was sent automatically," line 549). That pattern — compute locally, export only on explicit action, never auto-transmit — is the right default and should be the studio-wide standard for any instrumentation, not just this one build's copy line.
- **The live backend (Supabase, wired into the Workshop Vending Machine per `en195-arcade.html:739` and `index.html:553-554`) is a named, deliberate, single exception to offline-first — not a precedent.** Any new instrumentation that wants a backend needs to clear the same bar that exception cleared, not get grandfathered in because the exception already exists. I have not verified the Vending Machine's specific RLS/anon-insert configuration myself — that's a systems-seat question, not mine — but the governing principle for my seat is: assessment data is a *harder* case than a coin-mint counter, and should face stricter scrutiny, not looser.
- **No re-identifiable data beyond what a classroom roster already is.** A rubric score tied to "the student in seat 14" inside the class the founder already teaches is not a new privacy surface; a rubric score tied to anything that could follow a student past that class (an email, a persistent ID, a cross-build profile) is a new surface and needs the founder's explicit sign-off before it exists, not after.
- **Never a transcript of spoken work.** This isn't hypothetical — the brainstorm doc's own proposed oral-communication builds (`Dry Run`, prosody meters) already solved this correctly: capture pace/pauses/energy only, never transcribe, which keeps the build offline-floor-compliant *and* sidesteps ever scoring accent or dialect (`ISLO-GAPS-BRAINSTORM.md:19`, "capture the mic, analyze prosody only... never scores words/accent/dialect"). Any oral build that ships in months 5-6 or later must hold that line exactly; a transcript is a FERPA question, a re-identification risk, and a dignity violation in one move.

---

## 5. What I would refuse to claim

**I would refuse to claim The Tell (or any current-state build) "assesses" written evidence in any report or pitch, until the fix in §3 lands.** Right now the honest sentence is "The Tell records which of 8 tags a student picked and displays their typed reasoning to the group; it does not evaluate that reasoning." Calling the current build "graded on evidence" is a claim the code doesn't support, and per `CLAUDE.md`'s standing rule — no invented or inflated claims, use the founder's actual words — that's not a claim I'll write into a deliverable.

**I would refuse to claim any correlation between rubric score and "learning gain" without a real pre/post measure.** A per-dimension score from `close-the-loop.html` or `scorer-norming.html` is evidence of *alignment* — the game asked for the thing the rubric measures, and the rubric was applied consistently. It is not evidence of *growth* unless there's a before-and-after on the same student. Conflating "we can now score this" with "students are learning more" would be the exact inflation this studio's own voice rule forbids.

**I would refuse — flatly, per the standing founder ruling — any claim that a blind or low-vision student "can play" these games, that their version of the game "is the game," or that sighted and blind players "play the same way."** There is no playtest behind that claim anywhere in this repo, and the founder has never asserted it. What's real and defensible: the founder's own retinitis pigmentosa, and an accessibility-first design intent that shows up as real, checkable floors — contrast gates, dark-mode support, the comfort-gate ratchet. That's a design-intent claim about *why the studio builds the way it does*, and it stands on its own without needing an outcome claim it can't back. I will not write "blind students can play" or any paraphrase of it into this consultation or any deliverable that follows from it.

**I would refuse to recommend building new instrumentation before fixing the instrument that's already lying.** Adding a scored oral-communication build, or wiring the placement scorer, before The Tell's assessment logic actually reads what students write would mean the studio's evidence infrastructure grows faster than its evidence honesty. Month 1-2 fixes come first because everything downstream — the norming, the pre/post claim, the outside-adopter pitch — inherits whatever the instrument was actually measuring.

---

*Sources cited: `the-tell.html` (full read, 858 lines), `who-holds-the-room.html`, `update-the-model.html`, `sticker-price.html`, `islo-hub.html`, `ISLO-GAME-SUITE-PROPOSAL.md`, `ISLO-GAPS-BRAINSTORM.md`, `ISLO-SCORING-REFLECTION-2026-mwalsh.md`, `student-attribution-standard.md`, `aleph-lenses/L5.md`, `aleph-runs/2026-08-07-the-tell/L5.json` and `synthesis.txt`, `tight-spiral-studio-os.md` (pedagogy spine, §1 and §4.3), `CONSULT-GROUNDING-2026-08-07.md`, `CLAUDE.md`. All line numbers verified against live file contents on 2026-08-07, not recalled.*
