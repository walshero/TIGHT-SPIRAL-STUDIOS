# VOICE AND CLAIMS RUBRIC — Tight Spiral Studios copy auditor
*Built 2026-07-29 from the founder corpus: founder-canon.md, TSP_Ledger.md, index.html,
tight-spiral-runbook.html, os-block-hollow-claim.md, os-block-truth-ticks.md, the-coil-process.md,
TSP-GIT-LANE.md. Audits text AI agents add to studio HTML. No emoji, anywhere, ever.*

---

## 1. VOICE FINGERPRINT — what his prose observably does

1. **Second person doing, not being told.** The reader acts; the system answers.
   > "You pull the levers, then the seat turns around and shows you your own telemetry."
2. **Short declarative verdict after setup.** A long build, then a hammer under six words.
   > "Not a demo. These ran." / "Founder counted. Seven." / "Caught by a 404."
3. **The X-not-Y frame.** Corrects a category error in four words.
   > "Calibration, not certification." / "That is transfer, not recall." / "It is not metadata. It is the primary unit of meaning."
4. **Concrete nouns you could photograph.** Objects and figures carry the meaning; adjectives almost never do.
   > "a desk, a map, a phone, an empty chair" / "what a doorman actually costs — about $18,400 a year"
5. **Em-dash for the pivot or the gloss.** The dash lands the payload, mid-sentence.
   > "shows the dry cells — the places nobody is teaching what everybody is measuring."
6. **Aphoristic law-statements.** Rules read like physics, phrased to be checkable.
   > "A chat is not a lane." / "A discipline that depends on remembering is not a discipline." / "If a rule can't be a check, it's a wish."
7. **Shop-floor metaphor vocabulary, named once, then reused as terms.** Lanes, gates, ticks, belts, coils, ballast, the bench. Metaphors are load-bearing infrastructure, not decoration.
   > "The belt runs like a second hand, not an engine start."
8. **Labels and chips are terse states, never sells.** One or two words, factual.
   > "Live" / "In build" / "3 rooms" / "Judgment under uncertainty" / "Craft"
9. **Systems personified as workers with duties.** Tools act; they refuse, catch, guard.
   > "the machine that refuses a bad build" / "You learn the rules by running into them."
10. **Exact numbers, load-bearing, never rounded for flourish.**
    > "33 builds, live · 0 servers required · 0 trackers · 4.5:1 contrast floor, gated"
11. **The wry moral turn to close.** A paragraph ends on a judgment, lightly barbed.
    > "Published because a studio that hides its method is selling magic." / "Nobody chose these roads. Everybody walks them."
12. **Fragments allowed, hedges not.** "No tutorial, no menu, no account." He cuts qualifiers; he does not soften claims — he shrinks them until they are true.

## 2. BANNED — patterns the corpus never produces

- **Emoji. Absolute, zero-tolerance.** ("Zero emoji studio-wide — the no-emoji floor holds everywhere." It is a gated check, not a preference.)
- **Exclamation marks.** The corpus prose contains none. One "!" = not his voice.
- **Inflation adjectives:** seamless, robust, powerful, comprehensive, innovative, cutting-edge, world-class, stunning, dynamic, transformative, game-changing, best-in-class.
- **Corporate verbs:** leverage, empower, unlock, elevate, streamline, harness, supercharge, revolutionize, "utilize" for "use."
- **Ease-fluff:** simply, just, easily, effortlessly, "in seconds," "with a single click."
- **Generic CTAs:** "dive in," "explore now," "get started today," "learn more!", "check it out," "don't miss." His invitations name the act: "Play it, then the feel verdict."
- **Enthusiasm frames:** "we're excited/thrilled/proud to," "amazing," "love."
- **Hook questions:** "Ever wondered...?", "What if you could...?" He opens with a scene or a rule, never a tease.
- **Benefit-bullet lists with bolded lead-ins** ("**Fast:** ...") — his lists are steps, specimens, or laws.
- **Throat-clearing:** "In today's world," "It's important to note," "At its core." Also banned by founder ruling: "I hear you" as an opener; reminding him of things he already knows.
- **The promised payoff at the door.** His ruling: "the door does not promise the payoff. It promises *the world*." Copy that promises the outcome ("you'll master X") oversells; copy that opens the scene does not.

## 3. CLAIMS DISCIPLINE — the hollow-claim rule, operational

- **The definition:** "A HOLLOW CLAIM is a success message that is not backed by bytes." The law: "NO CLAIM OF SUCCESS MAY BE EMITTED THAT IS NOT DERIVED FROM THE ARTIFACT ITSELF." — "The bytes are the proof. Fetch them back. Compare them. Then speak."
- **COMPUTED > TYPED (TSP-GIT-LANE, 2026-07-29):** "Anything you **type** as a fact about state — a version, a date, a deployment status — is suspect by construction and rots. **Compute it.**" Precedents from his own face page: "running for a Manhattan relocation firm" corrected to **"designed for"** (the engagement, not the deployment, is what's provable); hardcoded "Last updated July 14" replaced with `document.lastModified`.
- **Counts (TICK 1, SOURCE-COUNT):** "Any claim about HOW MANY of something exists must be counted from the authoritative source, in the same turn it is asserted, and enumerated." A typed date or count in added copy is suspect until re-derived. The artifact under audit "is never its own reference."
- **Status words are probe results, not adjectives.** "Live," "deployed," "shipped," "complete," "runs on" may appear only when verified against the destination this turn (HTTP 200, byte-match, gate exit 0). "`success: true` is never proof."
- **Authority by claim type (TICK 2):** counts / numbering / verbatim official text → the published source; working vocabulary and current practice → Matt; what the artifact does → the artifact; whether it is *correct* → never the artifact.
- **Safe phrasings when unprovable:** "designed for," "built for," "In build," or say nothing. Never assert the stronger claim to sound finished.

## 4. AUDIT PROCEDURE — for any diff of added text, in order

**CHECK 1 — Emoji / punctuation floor.** Any emoji, any "!"?
Yes → **STRIKE** the character; re-check the sentence. (Not negotiable; this is a gate.)

**CHECK 2 — Hollow-claim scan.** Does the text assert a state fact — live/deployed/complete/running, a count, a date, a version, "used by," "trusted by"?
Yes and unverified this turn from the destination or source → **STRIKE** the claim, or **REWRITE** to the provable form ("designed for," "In build"). A typed number stays only if re-counted and enumerated.

**CHECK 3 — Banned lexicon.** Any word or pattern from Section 2?
Yes → **REWRITE**: delete the adjective, replace the verb with the plain act, replace the CTA with the named act or the scene.

**CHECK 4 — Voice test.** For each sentence: is the subject a person acting or a concrete thing? Is there a noun you could photograph or a number that is exact? Could the sentence run unchanged on any startup's landing page?
If it fails — abstract subject, adjective doing a fact's work, interchangeable copy → **REWRITE** in his register: shorter, second person or object-first, one em-dash pivot or X-not-Y frame allowed, verdict fragment permitted. (Rewrite "Our innovative platform makes peer review seamless" as "Peer review as a public act. What you say about someone's draft is a draft too.")

**CHECK 5 — Door test and prune.** Does it promise the payoff instead of opening the world? Does it add words without adding a fact ("adding requires pruning")?
Overpromise → **REWRITE** to the scene. Adds nothing → **STRIKE**.

**VERDICT:** all five pass → **KEEP**. Fails 3-5 but a true, concrete sentence exists inside → **REWRITE** (auditor supplies the rewrite). Fails 2 unverifiably, or nothing survives the prune → **STRIKE**.

*When Matt pushes back on any verdict this rubric produces, the rubric is the suspect. Re-derive from the corpus.*
