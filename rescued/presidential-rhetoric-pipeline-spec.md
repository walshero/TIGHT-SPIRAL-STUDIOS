# CHOOSE YOUR LEADER — Pipeline Strategy & Build Spec

*A Tight Spiral Studios project. First test case of an agent-driven pipeline for building a complex system. Single-file, offline, accessible-first — the studio defaults hold.*

*Drafted 2026-06-24. Concept passed full-roster panel review with conditions, no hard HALT. Architecture locked this session.*

---

## 0. What this is

A player-choice learning game. Players study six real leaders through their public record and learn **what a leader can DO with a given skill profile, comparatively** — not "who said this," but "given these mapped skills, what can this leader actually accomplish, and what can't they?"

The rubric mapping is the **stat sheet**, not an answer key. Players see what high Critical Thinking + low Communication produces in the world versus the inverse, across six leaders, and learn the AAC&U VALUE principles by watching the **consequences** of each profile. The core teaching move is **comparative leadership capacity, shown as trade-offs — never rankings.**

The game embodies **choice architecture**: players pick one of three epistemic frames (views) to investigate through, and the rubrics land differently depending on the lens. Each view is a different way of knowing the same figures.

This is also the **first agent-pipeline test case**: proof that a documented brief can drive agents to build three coordinated corpora, score them, and feed one game — with the human as the final gate at every stage.

---

## 1. Locked architecture

- **Name:** Choose Your Leader
- **Brand:** Tight Spiral Studios
- **Core MVP claim:** comparative leadership capacity — what a leader can DO with a mapped skill profile, shown as trade-offs, not rankings
- **Six leaders (locked):** Biden, Trump, Obama, Lincoln, FDR, Theodore Roosevelt
- **3 content views (player-choosable epistemic frames):** Rhetoric · Visual · Socioeconomic
- **2 meta toggles** overlaying ANY view: **design** scaffolding · **assessment** mapping
- **v1 scope:** all three views ship in v1 (deliberate override of ship-one-first — the comparative-capacity thesis needs all three lenses to land; Socioeconomic is where "what they can DO" is most truly shown)
- **Build path:** full Tight Spiral Build, art table seated live, Visual Critic HALT through founder's eyes

### The three views
1. **Rhetoric** — the language itself; full-range quote corpus.
2. **Visual** — campaign imagery, signage, design and body-language strategy.
3. **Socioeconomic** — spending and policy per administration, tied to the communication record. Heaviest corpus; most exposed to even-handedness failure.

### The two meta toggles
Independent overlays on any content view, off by default (a learner just plays):
- **Design toggle** — surfaces the streambed/move scaffolding behind the moment.
- **Assessment toggle** — surfaces the rubric mapping (proven-vs-needs-validation labeling intact).

This is the Confluence honesty discipline applied to a game: score separated from flag, scaffolding separated from play, each independently surfaceable on demand. The toggles are also how the **faculty advisory board** reads the assessment architecture under the play.

---

## 2. The rubrics (the teaching layer)

Three AAC&U VALUE rubrics: **Critical Thinking**, **Communication** (oral/written), **Leadership** (Foundations & Skills for Lifelong Learning maps closest; confirm exact instrument). The lens, not a displayed score. Players learn the principles by watching what each skill profile can and can't do.

**Panel condition (Assessment & Outcomes):** the named learner outcome is *predicting capacity from a skill profile* — a higher-order critical-thinking move than recognition. State it in plain player language up front.

---

## 3. The game mechanic — comparative capacity

"Choose Your Leader," built on the streambed beat order (Name the water / Show / Try-with-help / Try-alone / See-yourself):

- Player picks a content view (Rhetoric / Visual / Socioeconomic).
- Player studies a leader's mapped skill profile through that lens — the evidence, not a label.
- Player reasons about **what that profile enables and what it costs** — trade-offs, comparatively, against the other leaders.
- The teaching lands when the player can predict capacity from profile: high Communication enables mobilization but can outrun substance; high Critical Thinking enables sound judgment but can stall decisive action.
- Guess-who identification is an available *mode*, not the spine. The spine is comparative capacity.

**Even-handedness is load-bearing here (Satirist condition, stricter):** the comparative engine must show every profile's strengths AND costs evenly. No profile reads as simply "capable" or "incapable." Trade-offs, never rankings.

---

## 4. The agent pipeline (five-stage chain, now three coordinated corpora)

Question → Generate → Human gate → Play → Feed back.

What was a single-corpus test is now **three coordinated corpora feeding one game with comparative architecture across them** — a truer stress test of the pipeline, and a bigger first bite. Chosen deliberately: the truer version over the faster one, consistent with the living-system thesis.

### Phase 1 — Corpus Assembly (three parallel agent teams)
- **Team A — Rhetoric:** quotes across all six leaders, full-range (sharpest to muddiest, most persuasive to most evasive), across the whole career, with *when they said it*. Output JSON: `quote`, `date`, `source_url`, `leader`, `context_note`.
- **Team B — Visual:** campaign imagery, signage, design and body-language strategy. Every item carries **rhetoric-bearing alt-text** — the rhetorical move, not "campaign poster." Output JSON: `image_ref`, `date`, `source_url`, `leader`, `rhetorical_move`, `alt_text`, `context_note`.
- **Team C — Socioeconomic:** spending and policy per administration, tied to the communication record. Output JSON: `policy_or_spend`, `period`, `source_url`, `leader`, `comms_link`, `context_note`. Heaviest job; highest even-handedness exposure.

**Sourcing rule (Satirist condition), all three teams:** the full-range / "worst" bar is applied **evenly** to all six leaders. No favorites, no protected figures.

### Phase 2 — Scoring, Tagging & Capacity-Mapping (Agent Team D)
Pull the three AAC&U rubrics. Score every artifact. Tag across the epistemic frames. Build the **comparative capacity map** — what each leader's profile enables and costs, per rubric dimension. Flag patterns and drift over time.
- **AI-Skeptic condition (binding):** scoring notes stay in **evidence language** — what the artifact *does*, not a finished-sounding verdict. No wrapped-bow rubric prose.

### Phase 3 — Human Gate (founder; faculty board governs policy)
Founder is the final gate before anything ships to the deck: evidence-language discipline, even-handedness audit (do scores cluster by party?), trade-off-not-ranking check, taste. The **faculty advisory board** governs the policy layer around this gate (see §7).

### Phase 4 — Play
Three-view game with two meta-toggles. Instrumented so play generates research data.

### Phase 5 — Feed Back
Play data feeds validation (are capacity mappings holding up?) and gap-filling. More play = more data = better games. The living loop.

---

## 5. Binding conditions (from full-panel review)

1. **Evidence-language scoring** — describe what an artifact does; no verdict prose. (AI-Skeptic HALT)
2. **Capacity as trade-off, never ranking** — every profile shows strengths and costs evenly. (Satirist)
3. **Even-handed sourcing** — full-range bar applied equally to all six. (Satirist)
4. **Rhetoric-bearing alt-text** on every image. (Accessibility/ADA HALT — now live in v1, Visual view ships)
5. **Trauma-informed framing** — rhetoric/capacity analysis, not partisan endorsement; no graphic war imagery. (Trauma-Informed HALT)
6. **Ships portable** — single link, no accounts, college-laptop safe. (Skeptical Faculty Adopter)
7. **FERPA wall** — public figures only. Steward's HALT does not fire on public statements. The moment the game ingests student writing, HALT. Wall is absolute.
8. **Visual Critic HALT through founder's eyes** — the art table is seated live for the Visual view; the AI maker cannot see the render, so the founder is the eyes.

---

## 6. Faculty Advisory Board — DECISION POINT (open)

The board is granted **governing capacity** (policy, rubric-instrumentation approval, expansion decisions beyond the six), not merely operator capacity at the Phase 3 gate. Founder maintains **coherence of vision**.

**Unresolved tension (logged, not decided):** how governing authority coexists with founder-held vision coherence — the advisory-board failure mode (rubber-stamp vs. seize-the-wheel) in the OS's own terms. Candidate mechanisms for a later call:
- Vision held as a **constitutional layer** the board operates within but cannot amend without supermajority; or
- Founder retains a narrow set of **locked, non-votable principles** (TI / choice / play / joy + the living-system thesis), everything else governable.

Resolving this is a two-seat convening: Skeptical Faculty Adopter (wants real faculty ownership) vs. Project Manager (wants the ship on course). The mechanism above is what they'd argue.

**Board training beyond content (the gap):** they are trained on VALUE principles, TI/choice/play/joy, interdisciplinary design, assessment tools, and Confluence/Tight Spiral capacity. To work meaningfully in the pipeline they additionally need training in:
- **The gate as a skill** — calibration to tell evidence-language scoring from wrapped-bow verdict prose (same inter-rater discipline as Confluence, rehearsed here where there's no student data).
- **Even-handedness under political pressure** — blind-score-before-reveal; check whether their own scores cluster by party.
- **HALT vs. pass-with-conditions** — which hat they wear; a HALT means stop, not deliberate.
- **Reading the loop, not just the artifact** — aggregate pattern review (is the deck teaching the rubric, or teaching students to game the guess?).
- **The limits, trained as hard as the capabilities** — FERPA wall, no-branching, never-optimize-ahead-of-data. A board that knows capability but not the stop signs will, well-meaningly, propose the pipeline that ships student writing to an external API.

---

## 7. Decision points surface in the demo — DECISION POINT (logged)

Governance decision points **render in the demo** as visible, operational moments — consistent with the standing principle that the demo shows choice points and pipeline stages as playable, not as diagrams. The human gate and the board's role become a visible beat, not backstage machinery.

---

## 8. Open decisions still needing founder calls

- **Faculty board governance mechanism** — constitutional layer vs. locked-principles set (§6).
- **Exact Leadership rubric instrument** — confirm which AAC&U VALUE rubric is the leadership reference.
- **Capacity evidence basis for v1** — does "what they can DO" run on rhetoric-predicted-outcome, or require real policy-outcome data from day one? (All-three-views decision pushes toward the latter; confirm depth Team C must reach for v1.)
