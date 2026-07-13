# The Sandbox Wing — Design Doc

*Tight Spiral Studios · a play-and-connect lab for cross-sector models · walshero@gmail.com*

*Status: design doc, not a build. Grounded in `tight-spiral-studio-os.md` (the OS), the Confluence calibration finding, and the one-engine-many-skins pattern. Nothing here ships until a model earns a spine.*

---

## 1. What the Sandbox Wing is

A wing of the studio where the founder builds **small working models of one engine**, points each at a **different sector**, and **connects them** — a place to play, not a place to ship. The rest of Tight Spiral is a production pipeline: intake, gates, ship, canonize. The Sandbox is deliberately *before* that pipeline. It is where a model is allowed to be half-formed, cross-wired, and wrong, so the founder can *see* it before deciding whether it graduates into the pipeline.

The one-sentence charter: **a bench for trying an engine in a new sector without committing to build it there.**

It is a wing, not a new studio. It mounts in the same OS housing, obeys the same floors, and is governed by the same panel. What is new is only the *permission to play* and the *front door for outside consultants*.

## 2. Why it exists (the pattern it serves)

Two findings from recent work force this wing into being:

**Finding one — the parking lot is smaller than it looks.** Half the parked ideas are the same engine wearing different clothes: the nursery, the model-trains paper, the MBTA model, the capstone-as-playable-trains. That is not four builds. It is one architecture and a skin-switcher, described four times. The Sandbox is where you prove that once.

**Finding two — Confluence is a horizontal, not an education tool.** Confluence is a *noise-removal machine for human judgment* — it calibrates two judges to the same call and strips the drift between them. Education is one skin. Clinical intake, grant review, content moderation, hiring, qualitative coding — each is the same machine pointed at a sector where two humans must agree and their disagreement is expensive. The Sandbox is where you point it at each and *play*, before betting a build.

The Sandbox exists so the founder can answer one question cheaply: **does this engine hold in that sector?** — without the cost of a full pipeline build to find out.

## 3. What lives in the Sandbox (the models)

A **model** in the Sandbox is a small, playable instance of a core engine, skinned for one sector. It is not a product. It is a probe you can touch.

The founder's two core engines, as of now:

- **The Calibration Engine (Confluence).** Norms two judges to the same score; names the order-of-concern; frames anchors as convergence not decree; closes the loop upstream. Removes noise *between judges*.
- **The Adaptive-Instrument Engine (CAT / the survey's missing half).** Shortens what has to be judged — picks the next most-informative question, stops when the score stabilizes, cuts 50–87% of items. Removes noise *in the instrument*.

The un-obvious product the research hub surfaced: **bolt them together.** One machine that norms the judges *and* shortens what they judge — noise stripped from both sides. The Sandbox is where that bolt-together gets tried first, in miniature, in more than one sector.

**Sector skins to try** (each a model on the bench):

| Model | Sector | The judgment being calibrated |
|---|---|---|
| Placement Calibrator | Higher ed (home) | Two faculty → same placement score |
| Intake Calibrator | Clinical / mental health | Two clinicians → same severity rating |
| Review Calibrator | Grant / peer review | Two reviewers → comparable scores |
| Moderation Calibrator | Trust & safety | Two moderators → same call |
| Coding Calibrator | Qualitative research | Two coders → same theme (kappa, made visible) |

Same engine. Different skin. That is the whole design.

## 4. How models connect (the sandbox floor plan)

The Sandbox is not a list of separate demos. Its whole point is that models **connect** — the founder can wire the output of one into another and watch what happens. Three connection types:

1. **Shared engine, swapped skin.** The same calibration core drives every model; changing the skin changes the sector, not the machine. Proving this once is the highest-leverage move in the wing.
2. **Chained engines.** The Adaptive-Instrument engine feeds the Calibration engine: shorten the instrument, *then* norm the judges on what's left. Output of one is input to the next.
3. **Shared substrate.** Every model writes to one calibration-data substrate (the ConfluenceFields pattern already scaffolded — timestamped variables, FERPA HALT on artifact text). Connecting models means they drain to one readable place, so the founder can *see* the whole bench at once, not scroll between demos.

This connection-first floor plan is why the Sandbox is a *wing* and not a folder of unrelated files. The models are meant to be plugged into each other.

## 5. Governance — the Sandbox obeys the studio

The Sandbox gets play-permission, not floor-exemption. Every OS floor still holds:

- **Accessibility floor** (green-free, full-contrast, 44px, one decision per screen, fit-first) — non-negotiable, the founder's eyes are the verdict.
- **The Scout wall** — money reasoning (Opportunity Scout) never meshes with a model's design. A sector's *market size* never decides whether a model is good.
- **Just-in-Time Expertise (the load-bearing one for this wing).** The OS already says: when a decision sits in an expert domain, do not settle it from AI priors or the founder's guess — pull live domain expertise at the decision point. **The Sandbox turns this from a principle into a front door: outside consultants ARE the just-in-time expertise, convened per model.** (See §6.)
- **The self-staffing panel** — a model summons its own seats by trigger; a clinical skin wakes the Trauma-Informed HALT, a measurement skin wakes the Measurement Design gate, and so on. Dormant seats cost nothing.
- **Collision order unchanged** — hard floors > trauma/FERPA > founder's eyes/hands > Creative-Director spine > engagement > advisory.

The one new rule the Sandbox needs: **a model on the bench is not a build.** It carries a `PLAY` stamp. It cannot claim pipeline status, cannot be pitched as shipped, cannot skip the gates if it later graduates. Playing is not shipping. When a model earns a spine — a one-line *what it proves* — it leaves the Sandbox and enters Stage −1 intake like anything else.

## 6. The consultant front door (the interdisciplinary layer)

This is the part the founder flagged as needing major outside help. The Sandbox is where **interdisciplinary consultants plug in** — because a calibration engine pointed at clinical intake needs a clinician, pointed at grant review needs a reviewer, pointed at qualitative coding needs a methodologist. The founder cannot and should not carry all of those domains.

The consultant layer is built on the OS's existing bones, not invented:

- **Consultants are just-in-time domain seats, convened per model.** They are not permanent staff. A model in the clinical skin convenes a clinician-consultant for that model's decisions and releases them after. This is the OS's Just-in-Time Expertise principle, staffed with real humans.
- **Consultants inform, they do not reshape** — the same wall the Field Scout obeys. A consultant tells the model what its sector actually requires (the standard instrument, the real practice, the failure modes). The consultant does not get to change the founder's engine or floors. *Advisory proposes; the floors dispose.*
- **Each consultant is briefed from one page, not the whole studio.** The OS is portable by design; a consultant reads a one-page model brief (what this model is, what judgment it calibrates, what you need from your field), not the entire OS. This respects their time and keeps the founder's IP layered.
- **Consultant contributions are provenance-tracked.** Same rule as any asset: who contributed what, in what capacity, credited. No un-attributed borrowing of a field's methods.

**Candidate consultant profiles the wing will need** (interdisciplinary by design):

| Domain | What they calibrate the model against | Named leads (from memory) |
|---|---|---|
| Psychometrics / survey methodology | The instrument is statistically sound (IRT, ipsative deltas, 5–7pt scales) | *to source — measurement seat* |
| Counseling / clinical | The clinical skin is safe and real | Dan (counseling-field practitioner) |
| Reading/writing assessment | The placement skin norms against real criteria | Sean McCarthy (MassBay learning specialist) |
| Consensus governance / tooling | The connect-and-govern layer | Jeanie (handoff doc needed first) |
| Learning-games network | Sector doors downstream of a shipped model | Paul Reynolds / Gary Goldberger (FableVision) |

The founder's job in this layer is **the eyes, the voice, the judgment** — deciding *which* model, *which* sector, *whether* it holds. The consultants clear the domain-expertise load so the founder's attention lands only on the meaning. That is the OS throughline, applied to collaboration.

## 7. What the founder plays with (the interaction)

The Sandbox front end is a **connect-and-play board**, not a dashboard of readouts. Design principles, drawn from the best-practice research:

- **Question-storming, not metric-storming.** Salesforce's own method starts with the questions a persona brings, mapped on sticky notes — which is exactly the founder's instinct. The board is spatial and movable: each model is a card you can pick up, edit in place, wire to another, resolve, or park.
- **Dynamic layers, not walls.** Drill into a model for detail; zoom out to see the whole bench. Never a scroll to read one screen (the fit-first floor).
- **5–7 at a time.** No more than a handful of models visible at once — cognitive-load science, and the founder's floor.
- **Persona-adaptive face.** The same Sandbox renders differently for the founder (build/connect), a consultant (their one model's brief), and a peer/grant reviewer (the proof). Same architecture, adaptive skin — the Salesforce persona principle.

## 8. The smallest honest first step

Per the OS's grant-money-follows-evidence rule and the mission-serving move (*one documented loop at the smallest honest scale*):

**Do not build the whole wing.** Build one model, connected to one substrate, with one consultant convened — the **Placement Calibrator** on the MassBay ESL norming session, because that is the live instrument with real ground truth and the nearest consultant (Sean). Prove the loop closes: two judges, calibrated, noise stripped, findings travel upstream. That single proven loop is what turns every other sector column into a reskin instead of a rebuild — and it is the evidence a grant or a network contact runs on.

The Sandbox Wing is the *frame* for that. The first model is the *proof*. Build the proof; let the frame fill in as models earn their spines.

## 9. Open founder calls (before any of this opens)

Each needs a decision from the founder — none is Claude's to make:

1. **Which model first?** (Recommended: Placement Calibrator — nearest ground truth + nearest consultant.)
2. **Which consultant to approach first, and with what one-page brief?**
3. **Does the Sandbox board persist across sessions, or emit-and-carry?** (The Carry-Out pattern vs. a stored board — a real architecture fork.)
4. **Jeanie handoff doc** — needed before any consensus-governance tooling is adapted.
5. **IP layering** — how much of the engine a consultant sees vs. the founder holds.

---

*Sandbox Wing · a play-and-connect lab mounted in the Tight Spiral OS · models are not builds until they earn a spine · consultants inform, never reshape · the founder is the eyes, the voice, the judgment.*
