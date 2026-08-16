# CONFLUENCE PLAYTEST TEAM — the seating
*v1 · 2026-07-23 · A diversity-of-users playtest corps that works through*
*Confluence as real people do. Confluence-lane artifact.*

---

## WHAT THIS IS (and how it differs from the Panel)

The **Panel** (`collapse-panel-spec.md`, seven seats incl. Aleph) governs whether
an artifact is *correct, sourced, and accessible-by-floor* before it ships. It is
the maker's convening.

The **Playtest Team** is the opposite lens: it is the **audience**, seated to
work *through* the shipped thing the way real users would — and to break it the
way real users do. The Panel asks "is this right?"; the team asks "does a real,
varied human actually get through it?"

**The rule of this team — diversity is coverage, not decoration.** Each named
role (student, faculty evaluator, chair/admin, coordinator, reviewer) is seated
with several **template characters**. They are **composite archetypes**, not real
individuals — no real MassBay person is named. Each character exists because they
carry a *distinct failure mode*: a device, an access need, a literacy level, a
disposition, or a life-context that surfaces a problem the others can't see. If a
character doesn't surface a failure the roster otherwise misses, they don't earn
a seat.

The functional diversity axes each character is built from:
**life-context · device & bandwidth · accessibility · digital literacy ·
disposition toward assessment · the lens they bring.**

---

## THE SEATING

### 1 · STUDENTS `STU` — the people whose work is assessed
> They meet outcomes, artifacts, and the "where student work meets the world"
> companion. Community-college reality: commuter, working, first-gen, multilingual,
> many phone-first.

- **STU-1 · Returning parent** — works full-time, first-gen, evenings only.
  *Phone-first, low data, 5 spare minutes.* Disposition: time-starved, needs it
  obvious. **Lens:** can this be understood on a phone between shifts? **Breaks
  on:** mobile layout, hidden nav, anything that assumes a desktop or patience.
- **STU-2 · Recent grad, multilingual** — English is a second language; high
  phone fluency, low academic-English confidence. **Lens:** is the language
  *plain*? **Breaks on:** unexplained jargon (ISLO, rubric, calibration, artifact),
  reading level, idiom.
- **STU-3 · Low-vision** — retinitis pigmentosa; screen magnifier + high-contrast
  + occasional screen reader; commuter, mid literacy. **Lens:** the live
  accessibility floor. **Breaks on:** contrast under 4.5, missing focus, no zoom
  reflow, unlabeled controls, `color-scheme` gaps (C1) on a real phone. *(This
  character is the Stranger seat, walking around in the wild.)*
- **STU-4 · Veteran, older returner** — skeptical of being "tracked," moderate
  tech. **Lens:** trust & transparency. **Breaks on:** unclear what's collected /
  who sees my work / why; FERPA anxiety; assessment that feels like surveillance.

### 2 · FACULTY EVALUATORS `FAC` — the raters who score and calibrate
- **FAC-1 · Adjunct, five sections, two colleges** — no office, phone + borrowed
  laptop, zero spare time. **Lens:** can I score a batch fast with no training?
  **Breaks on:** onboarding friction, no save/resume, slow per-artifact flow.
- **FAC-2 · Tenured veteran** — skeptical of assessment-as-compliance, tech-
  cautious. **Lens:** does this respect my judgment or reduce me to a number?
  **Breaks on:** punitive tone, over-automation, calibration framed as a gotcha.
- **FAC-3 · New full-timer** — enthusiastic, high digital literacy, wants data.
  **Lens:** depth — can I see my agreement, my discrepancies, and drill in?
  **Breaks on:** shallow feedback, missing analytics, dead ends.
- **FAC-4 · Cross-discipline rater w/ dyslexia** — asked to score outside a home
  discipline. **Lens:** rubric clarity & cognitive load. **Breaks on:** dense
  rubric text, no anchor examples, small fonts, walls of prose.

### 3 · CHAIR / PROGRAM LEAD `LEAD`
- **LEAD-1 · Overloaded chair** — admin-heavy, glances on a phone between
  meetings. **Lens:** 30-second status — is my program on track? **Breaks on:**
  buried KPIs, no at-a-glance reliability, reports that need a desktop.
- **LEAD-2 · Faculty-advocate chair** — wary of top-down metrics harming faculty.
  **Lens:** does this show a *fair process* and protect individuals? **Breaks on:**
  individual raters exposed/ranked, punitive framing, metrics without context.
- **LEAD-3 · Interim lead, new to role** — data-minded but unfamiliar. **Lens:**
  can I learn it fast and trust the numbers' provenance? **Breaks on:**
  unexplained metrics, no methodology, no onboarding.

### 4 · ASSESSMENT COORDINATOR / ADMIN `ADM`
- **ADM-1 · Power user** — expert, desktop, owns the whole workflow. **Lens:**
  end-to-end — create session → invite → monitor → norm → publish → export.
  **Breaks on:** workflow gaps, missing export, unhandled edge cases.
- **ADM-2 · Rotating / part-time coordinator** — moderate tech, inherits
  half-built sessions. **Lens:** recoverability & error-proofing. **Breaks on:**
  destructive actions without guards, ambiguous states, bad defaults.

### 5 · EXTERNAL / ACCREDITATION REVIEWER `REV`
- **REV-1 · Accreditation reviewer (NECHE-type)** — skeptical outsider, read-only,
  needs an evidence trail. **Lens:** is the evidence credible, sourced,
  reproducible? **Breaks on:** unattributed claims, missing provenance/as-of
  dates. *(Mirrors the Registrar seat from the outside.)*
- **REV-2 · Transfer / articulation officer** — cares about outcome comparability.
  **Lens:** are outcomes legible to an outsider? **Breaks on:** internal jargon,
  no plain outcome definitions, results that don't travel.

---

## HOW A PLAYTEST RUNS

1. **Assign journeys.** Each character walks their real path (e.g. STU-3 opens the
   companion on a magnified phone; FAC-1 scores a full session cold; REV-1 opens a
   published report and hunts for the source of every number).
2. **Capture findings** in one shape:
   `character · screen · what happened · expected · severity · failure-axis`.
   Severity: **blocker** (can't proceed) · **friction** (proceeds, frustrated) ·
   **trust** (proceeds, but confidence/credibility damaged).
3. **Dedup by failure, not by character.** Two characters hitting the same wall =
   one finding with a wider blast radius (fix once, higher priority).
4. **Route to the floor.** Anything STU-3 hits is a live instance of the Stranger
   seat's accessibility floor — it should already be a gate tooth (C1, contrast,
   font floor). If it isn't, that's the gap.

---

## ALEPH TIE — the anti-silo rule for this team

Per the studio's law (*a rule that can't be a check is a wish*): a finding that
**recurs** across playtests should stop being a note and become a **gate**. The
team's job isn't to file the same bug forever — it's to convert repeat human
failures into arithmetic the CI enforces, so the next build can't reintroduce
them. Aleph's standing question applies: *did we relearn something a gate should
already catch?*

---

## NOTE ON THE CHARACTERS

Every character above is a **composite archetype** representing the diversity of a
real population — assembled from functional axes to maximize failure-mode
coverage. **None is a real person, and none should be given a real individual's
name.** They are lenses, not biographies.
