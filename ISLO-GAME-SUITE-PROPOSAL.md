# The iSLO Game Suite — proposal & coverage map

**A hub of games for MassBay students that both _build_ and _measure_ the college's
Institutional Student Learning Objectives.**

- **Deliverable shipped:** `islo-hub.html` — single-file, offline, contrast-gated (SHIP on preship-gate-v4).
- **Client anchor:** this is the student-facing sibling of `confluence-TRUNK.html` (the faculty
  assessment instrument) and the `islo-switcher` demo (rubric viewer). Same outcomes, same rubrics,
  three surfaces: faculty norm on Confluence, the switcher proves the spine, the hub is where students play.
- **Date:** 2026-07-19 · **Source of truth for outcomes:** MassBay Graduation Competencies,
  Spring 2026 ISLO #5 workshop deck (verbatim), plus the ISLO #1 and #5 rubrics (verbatim from Drive).

---

## 1. What the college actually asks for (verbatim)

MassBay expects every associate-degree graduate to become proficient in **seven** dimensions —
the Graduation Competencies, a.k.a. the Institutional Student Learning Objectives (iSLOs):

| # | Competency | The college's words |
|---|---|---|
| 1 | **Written & oral communication** | explain, persuade, advocate, and argue effectively when engaged with a variety of audiences |
| 2 | **Quantitative skills** | use a variety of mathematical tools and quantitative reasoning to solve problems and analyze complex challenges |
| 3 | **Technological / computer / information-science facility** | understand and use appropriately a variety of technological tools |
| 4 | **Knowledge about the natural world** | use scientific knowledge and methodology to test, validate, and update knowledge about the natural world |
| 5 | **Diversity, Equity, and Inclusion** | analyze systems of power and the ways group and individual interactions impact self, community, and society; identify skills and strategies for promoting equity, inclusion, and cultural sensitivity |
| 6 | **Critical thinking & informed decision-making** | ethical reasoning, integrative/systems thinking, and creative thinking to analyze and solve problems from multiple perspectives |
| 7 | **Personal, social, and civic responsibility** | take responsibility, self-assess, self-advocate, collaborate, and develop community and civic awareness |

**Rubric status (the measure side):**

- **iSLO 1** — AAC&U Written Communication VALUE, modified for MassBay. **Live**, 5 dimensions, verbatim in repo.
- **iSLO 5** — MassBay ISLO #5 Rubric. **Live**, 3 dimensions (Systems of Power · Group/Individual · Advocacy), 0–4, verbatim.
- **iSLO 6** — Critical Thinking. **In development** (criteria pulled from existing essay rubrics).
- **iSLO 2, 3, 4, 7** — **no locally-normed rubric yet.** AAC&U VALUE frameworks are the natural donors.

---

## 2. The design principle — measure **and** build

The task said the games must *measure and help build* iSLO skills. Those are two instruments, not one:

- **BUILD** = the game. You develop the skill by running into the constraint — no tutorial, no account.
  This is the studio's whole method: make the invisible constraint visible, let the student find it.
- **MEASURE** = the rubric. The *same* instrument faculty use on the graduation portfolio, reproduced
  verbatim. Ipsative and criterion-based: a starting point is never a verdict; you are scored against the
  college's levels and your own earlier draft, never ranked against classmates. (Criterion-based grading is
  what keeps minoritized students in STEM rooms — Hogan & Sathy, cited in the ISLO #5 workshop.)

The hub puts both on screen per outcome, side by side. It is itself an instrument: it **shows the dry cells** —
the outcomes the college measures that the suite does not yet build. Same move as Confluence showing faculty
"the dry cells — the places nobody is teaching what everybody is measuring."

---

## 3. Coverage map — existing shelf → the seven outcomes

Nineteen existing builds map onto the seven outcomes — a **finishing** play, not a building spree: most of
the suite already existed and only needed pointing at the framework. A twentieth, **Sticker Price**, was then
built this pass to close the quantitative gap.

| iSLO | Coverage | Games that BUILD it (live now) | Measure |
|---|---|---|---|
| **1 · Written/Oral Comm** | 🟢 **Built** (strongest lane) | The Tell · Sandbags · Cliché Cowpaths · Flash Ballast · Workshop Wall · Review Bench · EN195 Hub | WC VALUE (live) |
| **2 · Quantitative** | 🟢 **Built** | **Sticker Price** · The Tension Bar (client engine) · Warriors Fantasy Arcade | QL VALUE (not normed) |
| **3 · Tech / Info-Sci** | 🟢 **Built** | The Console · Funny Boney's Factory · How an Idea Travels | suite-proposed criteria |
| **4 · Natural World** | 🟢 **Built** | **Update the Model** | Scientific reasoning (not normed) |
| **5 · DEI** | 🟢 **Built** | **Who Holds the Room** · Choose Your Leader | **ISLO #5 (live)** |
| **6 · Critical Thinking** | 🟢 **Built** (deepest lane) | Choose Your Leader · The Console · The Viscosity · The Compound Capstone · Warriors · Behind This Door | ISLO #6 (in development) |
| **7 · Personal/Civic** | 🟢 **Built** | Play the Semester · The Course River · Workshop Wall · FYS Treasure Trove | suite-proposed reflective rubric |

**Net:** all 7 outcomes built. What remains open is the *measure* side — four outcomes (2, 3, 4, 7) have no locally-normed MassBay rubric yet; iSLO 6's rubric is still in development.

---

## 4. Proposed new builds — three, to fill the dry cells

Ranked by value-to-effort (the studio's standing ranking rule). Each reuses a proven engine.

### 4.1 `Sticker Price` — iSLO 2 (Quantitative) · **SHIPPED 2026-07-19** (`sticker-price.html`)
A headline number — a student loan, a tuition sticker, a statistic in an argument, a small monthly charge —
gets pulled apart into what it actually means over time. **Reuses the Tension Bar cost-decomposition engine**
and its dignity framing (the number asks — never "you are short"). Four cases, each guess-first then reveal:
1. **The Loan** — a real fixed-rate amortization; principal vs. interest bar; the sticker is the amount
   borrowed, the price is the amount repaid.
2. **The Sticker** — published price minus gift aid = net price; what the sticker leaves out (books, housing,
   loans-vs-grants).
3. **The Statistic** — a percentage change with the counts and denominator put back; *a percentage with no
   denominator is a rumour.*
4. **The Small Charge** — a `/mo` multiplied out over a degree; small-times-often is not small.

Teaches all four AAC&U QL dimensions — Interpretation, Calculation, Assumptions, Communication. Every headline
is an **editable example** the student sets (dignity floor: a starting point is never a verdict), so no market
number is fabricated — provenance names the *method* (amortization formula; federal net-price definition;
base-rate pedagogy). **Verified end-to-end in a headless browser** (all four cases, no console errors, correct
arithmetic); preship-gate-v4: SHIP (worst pair 5.57:1). **Still open on the measure side:** norming a local QL
rubric — the game now produces the work samples for it.

### 4.2 `Who Holds the Room` — iSLO 5 (DEI) · **SHIPPED 2026-07-19** (`who-holds-the-room.html`)
One scene, several positions. You map who holds power, trace how a group and an individual read the same
moment differently, and choose an advocacy move — then see it scored on the college's **live ISLO #5 rubric**,
whose three dimensions become the three rounds:
1. **Systems of Power** — who holds power/privilege in this scene, and where are you in it?
2. **Group / Individual Interactions** — how does the same moment land differently across positions?
3. **Advocacy** — pick a communication move that promotes equity/inclusion; the rubric names its level.

The only station with a live rubric and no purpose-built game. Choose Your Leader feeds in (systems of power,
who sits in the chair) but is history/judgment, not DEI-advocacy. **Effort: medium.** Dignity-first framing,
MassBay's verbatim language, attributed — non-negotiable given the outcome.

> Note from the workshop deck: *"What else do we lose when we lose DEI?"* This build keeps the college's own
> normed instrument in students' hands, which is the durable answer.

### 4.3 `Update the Model` — iSLO 4 (Natural World) · **SHIPPED 2026-07-19** (`update-the-model.html`)
You hold a belief about how something in the natural world works. Evidence arrives. You decide whether to
test it, state in advance *what would change your mind*, and how much to revise. Hypothesis → test → update —
**the tight-spiral feedback loop the whole studio is named after** (Xenos-ISLE / Learning Games Network, 2012),
finally pointed at the science outcome. Nearest existing relative is The Viscosity (models a scientific
framework — Maslow — as a walkable space); the reveal pattern is proven, only the domain is new.
**Effort: medium.** AAC&U Inquiry & Analysis / Scientific Reasoning map cleanly; both a build and a norming
pass are open here — the strongest single opportunity for a brand-new instrument.

---

## 5. What shipped

**2026-07-19 (pass 3):** `who-holds-the-room.html` (iSLO 5) + `update-the-model.html` (iSLO 4) — the last two dry cells filled. **All seven outcomes now have a build.** Hub: iSLO 4 Dry→Built, iSLO 5 Thin→Built; counts 22 games mapped / 0 dry cells. Both browser-verified end-to-end; ratchet 0 regressions.

**2026-07-19 (pass 2):** `sticker-price.html` — the iSLO 2 build, above. Hub updated: iSLO 2 flips Thin→Built, Sticker Price card goes live, counts re-read (20 games mapped, 2 dry cells left).

**2026-07-19 (pass 1):**

- **`islo-hub.html`** — the hub. Seven stations, verbatim definitions, 19 live games mapped, 2 live rubrics
  reproduced, 3 dry cells marked, 3 proposed builds shown as dashed "Proposed" cards. Standing Home/Back nav,
  4.5:1 contrast floor, single-file, offline, zero network calls. **preship-gate-v4: SHIP** (worst pair 5.57:1).
- **This proposal** — the research trail and the build ranking.

## 6. Open decisions for the founder

1. **Build order** — recommend `Sticker Price` first (engine exists, lowest effort, unblocks QL norming).
2. **iSLO 6 rubric** — the deepest game lane sits over an unnormed rubric; worth closing that loop next term.
3. **Naming** — hub currently titled "The iSLO Suite." If it should read to students as a course requirement
   vs. an optional arcade, the framing on the stage copy can shift.

---

**Sources.** MassBay Graduation Competencies / iSLOs (Spring 2026 ISLO #5 workshop deck, verbatim) ·
AAC&U Written Communication VALUE rubric © 2017, modified for MassBay (verbatim) · MassBay ISLO #5 Rubric
(verbatim) · ISLO #6 criteria from existing MassBay essay rubrics (rubric in development) · existing TSP shelf
(`index.html`, counted from the repo, not remembered). CC BY-NC-ND 4.0.
