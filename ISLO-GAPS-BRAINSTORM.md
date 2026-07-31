# iSLO gaps — full-staff brainstorm

> **Source:** Full-staff brainstorm convened 2026-07-30 — five studio lenses (Registrar/Cora, Learning
> Scientist, Studio-Eyes/accessibility-&-dignity, Assessment Lead, Reuse Engineer). Synthesis by the studio.
> A living planning doc to steer, not a commitment. **Last-verified:** 2026-07-30.

## The gaps on the table
1. **Oral communication** — iSLO 1 is "written **and oral**," but every build is writing. Genuinely unbuilt.
2. **Thin outcomes** — iSLO 4 (one game), iSLO 7 (self-report only), iSLO 3 (leans on "dark patterns").
3. **Measure side** — no locally-normed MassBay rubric for outcomes 2, 3, 4, 7; iSLO 6 rubric in development.
4. **EN placement portfolio** — records only EN98-vs-EN101, no skill-level data (founder's own reflection).
5. **Underserved populations** — multilingual/ESL, working/parenting/commuter, first-gen.

## What the staff converged on (the strong signals)

- **Oral comm is the #1 real gap** — every seat named it. The Registrar: "half of the most-assessed
  competency going unmeasured." Two build paths: a cheap one (score *described* delivery on a rubric) and a
  deliberate one (capture the mic, analyze **prosody only** — pace/pauses/energy — never transcribe, so it
  stays offline **and** never scores words/accent/dialect: the dignity move and the technical unlock at once).
- **The EN Placement Skill-Scorer is the flagship measure-side build** — Assessment Lead and Reuse Engineer
  landed on it independently, both ranked #1. It reuses the Norming Table scorer, loads the founder's own
  candidate skill list, derives the placement *from* the skill profile (never entered first), and exports
  per-skill data — the exact "insufficient means to review our curriculum" gap, answered.
- **One authoring tool unblocks four outcomes** — a "Rubric Forge" that helps faculty draft a normable rubric
  for the un-normed outcomes (2/3/4/7) feeds every other measure-side app.
- **Cheapest wins reuse a shipped engine outright** — new *case data* on the Sticker Price rail, or a new
  *rubric + samples* on the Norming Table scorer, is ~80% built already.

## The idea map, by value-to-effort tier

### Tier 1 — cheap, high value, reuse an engine, buildable now
| Build | Gap / iSLO | Engine reused | Note |
|---|---|---|---|
| **Placement Skill-Scorer** ("Placement Prism") | EN placement + measure, iSLO 1 | Norming Table scorer + Close the Loop export | Flagship. Founder's rubric + rationale on file. Verify the placement mechanism is current first (see flags). |
| **Score the Room** — oral comm | oral, iSLO 1 (unbuilt) | rubric-level scorer + case-rail | Scores *described* delivery on AAC&U Oral Communication VALUE. No audio. Opens the oral lane cheaply. |
| **Real-Cost Case Pack** | underserved populations, iSLO 2 | Sticker Price (case data only — no new engine) | Commuter transit, working-parent time-cost, ESL textbook, first-gen hidden fees. Nearly free. |
| **The Real Syllabus** | first-gen, iSLO 3 + 7 | predict-then-reveal | Decodes the hidden curriculum ("my door's open," "recommended reading"). Knowledge was *withheld, not missed.* |

### Tier 2 — medium effort, high leverage
| Build | Gap / iSLO | Engine reused | Note |
|---|---|---|---|
| **Rubric Forge** | measure, outcomes 2/3/4/7 | fillable-report (Close the Loop) | Faculty draft normable rubrics; output loads into every scorer/report. Unblocks the un-normed outcomes. |
| **Hold It Constant** | iSLO 4 depth | predict-then-reveal | Controlled-variable / confound isolation — the skill Update the Model assumes but never teaches. |
| **The Follow-Through** | iSLO 7 depth | logic + fillable report | Implementation intentions (if-then re-routes around a real bad Tuesday). Obstacles structural, never moral. |
| **The Load** | working/commuter, iSLO 2 + 7 | number-decomposition + report | Planner that starts from the immovable week and treats the hours you *have* as sufficient. |
| **Full Contrast** | accessibility, all iSLOs | shared include + extend preship gate | One drop-in file (focus rings, keyboard, ARIA live regions, text-size) + gate enforcement — lifts the whole shelf. |
| **Open Norming Table** | measure, 2/3/4/6/7 | Norming Table (generalized to load any rubric) | Makes every Rubric Forge output immediately normable. Mostly parameterization. |

### Tier 3 — deliberate builds / higher risk / blocked
| Build | Gap / iSLO | Note |
|---|---|---|
| **Dry Run** + prosody oral games (**Landing**, **Say It in Three**, **In Their Words**) | oral, iSLO 1 | The *real* oral builds — private rehearsal + prosody meters. Most new-mechanic risk; the flagship deliberate build. Must stay private + ipsative. |
| **Two Tongues** | multilingual, iSLO 1 + 6 | Multilingualism-as-asset: shows the rhetorical move a bilingual student already makes in both languages. Must never be cohort-comparable. |
| **The Commons** | iSLO 7 civic | Tragedy-of-the-commons over seasons; reuses the decomposition bar as a depletable pool. |
| **Prism Consensus** + **Loop Gaps** | measure meta-tools | Reader-agreement view for placement; a 7-row coverage scoreboard of the whole measure side. |
| **iSLO 6 CT rubric load** | measure, iSLO 6 | **Blocked** — the engine's ready; the cost is *finalizing the CT rubric* (faculty work), not code. |

## Strategic flags (the staff's cautions — decisions, not builds)
- **The unnamed gap (Registrar):** the whole suite speaks an English/writing/humanities idiom, but MassBay's
  largest enrollments are the **career/workforce divisions** — Health Sciences, Automotive, Business — plus
  transfer-STEM. Those students must still clear all seven iSLOs, yet almost nothing meets them *inside their
  own programs.* Biggest strategic gap. *Verify the enrollment-by-division ranking against the Fact Book
  before choosing which division to build for first.*
- **Verify before building the placement tool:** Massachusetts has pushed community colleges toward
  co-requisite / multiple-measures placement; the EN98→EN101 gate may be partly dissolved. Confirm the
  *current* English placement mechanism (Catalogue / English dept) before shipping — build for 2026's
  pipeline, not the portfolio's memory.
- **Delivery fit is verified:** MassBay is **~69% part-time / commuter** (Fact Book) — single-file, offline,
  no-account, phone-first is exactly the right vehicle for who MassBay actually is. This is a strength, not a
  gap; it just confirms the studio's whole delivery model.
- **Dignity guardrail (Studio-Eyes):** the oral and multilingual builds must stay **private and ipsative** —
  the moment a recording or a register-choice becomes comparable to a peer's, the asset-framing collapses into
  a deficit score.

## Recommended first move (the studio's synthesis)
Two Tier-1 builds that reuse shipped engines and answer named needs, then one flagship:
1. **Placement Skill-Scorer** — the founder's own named pain, primary-source rationale already on file, pure
   Norming Table reuse. *(Pending the placement-mechanism verification above.)*
2. **Score the Room** — opens the unbuilt oral lane at the lowest cost, on the AAC&U Oral Communication rubric.
3. Then **Rubric Forge** (unblocks the un-normed outcomes) or the prosody **Dry Run** (the deliberate oral flagship).

## Open decisions for the founder
- Green-light which Tier-1 build(s) first?
- The **career/workforce iSLO** question — is that a lane the studio wants to open? (Biggest strategic gap.)
- Oral comm: cheap-first (**Score the Room**, described delivery) or straight to the **prosody** builds?
- Should I verify the current EN placement mechanism (via the Registrar corpus / Catalogue) before building the placement tool?
