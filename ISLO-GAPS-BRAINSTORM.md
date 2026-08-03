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
| ~~**Placement Skill-Scorer**~~ **PARKED** | ~~EN placement~~ → co-req support diagnostic? iSLO 1 | Norming Table scorer + Close the Loop export | **Premise void:** MassBay offers **no EN90/98** developmental courses — it's a **co-req pioneer**, no place-out gate. The engine + the founder's skill rubric still stand; the *use* must be re-framed (e.g. a co-req support-targeting diagnostic, not a placement). **Awaiting founder's co-req detail** ("ask me later"). |
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
- **CONFIRMED by the founder (2026-07-30) — the placement premise is void.** MassBay offers **no EN90 or
  EN98** developmental courses; it is a **co-requisite pioneer** (students enter EN101 with co-req support,
  not placed out). So "EN98-vs-EN101 placement" is not a live mechanism, and any reference to it — including
  the founder's own reflection — is describing a prior or mis-stated model. The Registrar's caution was right.
  The Placement Skill-Scorer is **parked**; if it returns it will be a **co-req support diagnostic**, not a
  placement gate. **Now documented** in the department's own annual reports (2025): *"as a result of long-term
  data on the efficacy of our co-req model, EN090 and EN098 have been officially retired"* — EN101X + EN101L
  co-req lab. **Now fully documented** in the **Title III co-req grant summary (Katie McGrath, Aug 2024)**, seated
  in `claude_seat-english-assessment.md`: placement is **multiple measures** (HS GPA ≥ 2.7 → EN101, else Accuplacer →
  co-req/college-level/ESL); co-req passes college English at **80-83% vs 38-50%** developmental; the named open
  target is the **EN102 + Hispanic/Latina-female equity gap**, and Title III's support models (embedded learning
  specialists, coaches, PEEPS, Persistence Project) are the scaffolding a **co-req support diagnostic** would route
  students toward. Buildable once the founder greenlights the co-req vision.
- **Delivery fit is verified:** MassBay is **~69% part-time / commuter** (Fact Book) — single-file, offline,
  no-account, phone-first is exactly the right vehicle for who MassBay actually is. This is a strength, not a
  gap; it just confirms the studio's whole delivery model.
- **Dignity guardrail (Studio-Eyes):** the oral and multilingual builds must stay **private and ipsative** —
  the moment a recording or a register-choice becomes comparable to a peer's, the asset-framing collapses into
  a deficit score.

## Recommended first move (the studio's synthesis) — revised after the co-req correction
The placement flagship is parked, so lead with builds that stand on their own:
1. **Score the Room** — opens the unbuilt oral lane at the lowest cost, on the AAC&U Oral Communication rubric.
2. **Real-Cost Case Pack** — nearly-free underserved-population reach on the shipped Sticker Price rail.
3. Then **Rubric Forge** (unblocks the un-normed outcomes) or the prosody **Dry Run** (the deliberate oral flagship).
4. **Held for founder briefing:** the co-req support diagnostic (the re-framed ex-"placement" build) and the
   career/workforce iSLO lane.

## Shipped since — the GenAI lane (2026-07-30, built while the founder was away)
Not on the original tier list, but the strongest unblocked signal from the **Assessor seat**: the English annual
reports name AI-use guidance and AI-resistant assignment design as active department needs (30/60/75% of students
got no class/syllabus/assignment guidance). Two tools shipped, both gated + ratchet-clean + browser-verified:
- **Whose Draft** (student, iSLO 1 & 3) — decide how much of an essay to hand to AI at each step; leave with a
  usable disclosure statement. Grounded in the dept's own integrity indicators.
- **AI-Resilient Assignment** (faculty, iSLO 1 & 3) — a 7-check assignment audit + redesign moves + a syllabus
  GenAI policy builder. Answers the reports' action items directly.
This did **not** touch the parked builds below.

## Open decisions for the founder
- Green-light which Tier-1 build(s) first?
- The **career/workforce iSLO** question — is that a lane the studio wants to open? (Biggest strategic gap.)
- Oral comm: cheap-first (**Score the Room**, described delivery) or straight to the **prosody** builds?
- Should I verify the current EN placement mechanism (via the Registrar corpus / Catalogue) before building the placement tool?
