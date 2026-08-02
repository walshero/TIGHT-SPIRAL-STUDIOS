<!--
================================================================================
 CANON WARNING — READ BEFORE YOU RELY ON THIS FILE
 Landed in the repo 2026-07-12. This is the FIRST time the OS has existed in the
 repo at all; before this commit it was 404 in every git lane.

 THIS DOCUMENT IS INCOMPLETE. It ends at §14 and is dated 2026-07-05.
 Seven days of governance were written as separate blocks and pushed to this repo
 WITHOUT being folded in here. They are LAW. They are not in the text below.

 UNMERGED LAW — read these files, they govern:
   os-block-cross-lane-mount.md      (claims §12)  2026-07-10
   os-block-pointer-memory.md        (claims §12)  2026-07-10
   os-block-preship-gate.md          (claims §14)  2026-07-10  <-- COLLIDES
   os-block-deploy-lane-preflight.md               2026-07-10
   os-block-playtest-instrument.md                 2026-07-10
   os-block-truth-ticks.md           (claims §11)  2026-07-11  <-- COLLIDES
   os-block-hollow-claim.md                        2026-07-11
   os-block-tick-rule.md                           2026-07-04
   os-block-bodyguard-gates.md                     2026-07-04

 SECTION-NUMBER COLLISIONS — unresolved, founder call owed:
   - This document ALREADY HAS a §14 ("Lane truth"). preship-gate also claims §14.
   - This document has NO §12 (it jumps 11 -> 13). Two blocks both claim §12.
   - This document's §11 is "Standing working rules". truth-ticks also claims §11.
   A mechanical merge WILL overwrite live sections. Do not automate it.

 WHY IT WAS LANDED STALE: absence is worse than staleness. While the OS was 404,
 resolve-canon.py could not distinguish "missing" from "broken check," and any agent
 reading the shelf would silently violate law it could not see. This lands the file
 so the tooling can see it. The merge is a scheduled build session, not done here.

 STANDING FLOOR - SIGHT BEFORE STEPS (locked 2026-07-12, founder)
 The agent does NOT give navigation instructions for a screen it has not seen.
 Ask for a screenshot, or say "I cannot see that screen." No guessing at button
 positions. No "it should be below." If the image is not in hand, the instruction
 does not ship. This is Studio Eyes pointed at INTERFACES, not just files.

 WHY: the founder has retinitis pigmentosa; menu-hunting is the specific cost.
 The rule already existed in his preferences ("do not assume I can easily find
 interface elements... mention where buttons are located"). On 2026-07-12 the agent
 read it, acknowledged it aloud when the founder invoked it mid-session, and then
 kept guessing anyway - burning ~20 minutes sending him through a GitHub permissions
 menu that GitHub was actively suppressing. One screenshot solved it in one turn.
 The check was not missing. The agent did not run it. That is the disease this whole
 file documents: rich in rules, thin in enforcers.

 NOTHING BELOW THIS COMMENT WAS EDITED. Byte-identical to the founder's copy
 (166,146 B, md5 5424fff7ba5b1f7e2c...). Verified against two independent lanes.
================================================================================
-->

# Tight Spiral Productions (TSP) — Studio Operating System

*The single source of truth for how this studio works: who it's for, what it makes, the house style, the voice, the review panel, the workflow, and the delegation map. Written so that a collaborator, a teaching assistant, or a fresh AI session can run the studio faithfully without the founder re-explaining anything. Portable by design — plain Markdown, no dependency on any one tool.*

*Last integrated: 2026-07-02 (second pass — §11 standing-rules fold reconciled; see §11 header for the phase-slip it closes) — FOUR AMENDMENTS from the founder's voice session. (1) NAME: Tight Spiral Studios → **Tight Spiral Productions (TSP)** — §1, decision log. TSP = teaspoon: a micro-unit; the studio's method named at last (micro-moves composed into systems, applied in the live moment — the founder's wrestling/judo/language-learning throughline). Shipped files carrying "Studios" update **as-opened**, never bulk (the deferred-reskin rule applies to the rename). (2) THE KERNEL TRACK — new §6.4: a parallel research lane producing calibrated knowledge kernels (small, source-verified, cross-disciplinary, openly licensed) as the studio's knowledge substrate — feeding Confluence, the University of the Open Mind, and every build; the low-density alternative to LLM-scale knowledge. (3) BORGES LEFT — new seat (§5, roster table): the full-corpus assembler; before any structural/strategic answer, it pulls everything relevant across all surfaces (Project shelf, Drive, memory, session notes) and assembles the situated governance — the cure for answering from a partial picture. (4) FORWARD AGENTS — a standing pre-pipeline motion (§6.4): agents watch the founder's seeds and run advance work (sourcing, precedent, viability) so ideas arrive at Intake Triage already scouted.*

*Prior integration: 2026-06-29 — the PROBE SWEEP + ACCUMULATOR DECAY RULE (§5.4.5.1, decision log §10). A founder structural/diagnostic question is now a system-wide probe: the Conductor extracts the underlying test and runs it against every OS component before answering the narrow case (the question-side twin of Maximize-or-Check), and auto-queues every surfaced gap for graduate-or-kill so a probe is never a write-only note. Linked call: every accumulator (parking lot, memory, panel roster, Props Room, file shelf) must be able to shed — last-touched stamp + why-held note, review outcomes are promote-or-kill only, "held" has a clock. The Conductor itself was written into the OS here for the first time (memory-resident since 2026-06-27 but never on the durable shelf — a caught accumulator gap). Worked example: one question aimed at the parking lot hit five accumulator gaps on sweep; memory consolidation sat parked until it hit the ceiling and hard-blocked new locks.*

*Prior integration: 2026-06-27 (pm-4) — the SELF-STAFFING PANEL (§5.4.5): the build's own properties now SUMMON its seats via triggers, instead of the founder picking from a list. Every seat carries a firing condition ("fires when…" — new column in the §5.6 table); dormant seats cost nothing and stay out of the founder's head until their trigger fires. Resolves the bloat problem WITHOUT capping richness — the discipline moves from "how many seats" to "does each seat carry a real trigger" (no trigger, no seat). Added an explicit COLLISION POWER-ORDER for simultaneous HALTs: hard floors > trauma/FERPA > founder's eyes/hands > Creative-Director spine > engagement > advisory ("engagement proposes, the floors dispose"). Filled the §5.6 table to the full current roster and seated four candidate seats dormant (trigger named, sleeps until fired): SCRIPT/STORY EDITOR (voice-level line HALT — owns the recurring placeholder-copy ship-blocker), CONTINUITY/LORE KEEPER (cross-build canon, wakes at 3rd shipped game), PLAIN-LANGUAGE EDITOR (ESL/reading-level), PLAYER-VOICE (real player evidence, wakes at pitch/impact). Earlier pm-3: the three-layer Art Production System (§5.2); the Field Scout (§5/§10). Prior same-day: engagement-seat package, Pivot gate, Real Talk lens, Zimmerman on CYL, Obama un-gated, Disciplinary Panel Stage 0.5, the player-never-does-studio-work floor, five gate outcomes, collection/season model, Medium Gate's three lanes — all logged (§10).*

---

## 0. How to use this document

This is an operating system, not a manual to read front to back. Jump to what the job needs:

- Starting any build → **§3 House Style**, **§5 The Review Panel**, **§6 Workflow / the Production Pipeline**.
- Writing in the studio's voice → **§4 Voice & Humor**.
- Making art → **§3.2 The Art System** (no default medium — run the Medium Gate first; three lanes).
- Planning or triaging work → **§6 Workflow** and **§7 Delegation & Strengths Map**.
- Onboarding a person or an AI → read §1, §3, §4, then skim the panel in §5.

Two rules sit above everything else and are never overridden: **no emoji, ever**, and **accessibility is a design floor, not a feature** (see §3.1). If a choice ever conflicts with those two, those two win.

---

## 1. Identity

**Studio:** Tight Spiral Productions — **TSP**.
**Named for:** Gee's recursive "tight spiral" learning loop — notice, adjust, try again with new understanding. The name *is* the method.
**TSP = teaspoon.** The acronym is load-bearing: a teaspoon is a micro-unit, and the studio's whole method is micro-units composed into systems and applied in the live moment. The founder learned this bodily before he theorized it — wrestling captain at Boston Latin, black belt in judo earned in Japan, language learned the same way: drill the small move until it's yours, compose moves into systems, and when the real moment comes, the practiced unit fires without deliberation. Teaching runs on the same law; so does the studio; so does the kernel system (§6.4). The teaspoon is the smallest honest unit of the work.
**Rename note (2026-07-02):** formerly Tight Spiral Studios. Files, footers, and marks carrying "Studios" update **as-opened**, never in a bulk pass — the deferred-reskin rule governs the rename. Imprint names (Tight Spiral Paper Craft Studios, Super Sketchy Graphics, Human-in-the-Loop Productions) are unchanged; they are gears inside TSP.
**Tagline:** "Play. Notice. Design."
**Descriptor:** "We turn how you learn into how you play."
**Contact:** walshero@gmail.com
**What it makes:** All kinds of games and interactive pieces — not only writing or composition games. Single-file, offline, accessible-first.

**The studios (gears, with one hub).** Human-in-the-Loop Productions is both a named imprint and the hub the others mesh to — every output carries a human gate because the gate is the hub. The two art imprints mesh to it, never directly to each other:
- **Tight Spiral Paper Craft Studios** — the cut-paper SVG art system (one of three medium lanes; chosen when the Medium Gate sends a build there, not by default).
- **Super Sketchy Graphics** — the AI-assisted / raster imprint (hero/photoreal looks), transparency-first: it says plainly that the art is AI-made. Standing credit line: "Art commissioned to Super Sketchy Graphics by Tight Spiral Studios · AI-assisted." Not CC-BY, not for reuse.

The OS is the housing all gears mount in; the Review Panel is the governor that regulates whether work keeps turning; the Production Pipeline (§6) is the gear train. Two Scouts sit deliberately *unmeshed* — the Opportunity Scout (money never drives a design decision) and the Field Scout (institutions inform or open doors, never reshape) — both walled off, both speaking only when convened (§5/§10, the Scout wall).

**Theoretical DNA** (the studio's spine, not decoration):
- **Osterweil's Four Freedoms of play** — freedom to fail, to experiment, to try on identities, to invest effort (incl. freedom of effort, which governs collaboration itself).
- **Gee's learning principles** — probing, identity, well-ordered problems, learning inside the flow.
- **Flow theory** (Csikszentmihalyi/Chen) — difficulty sits in the channel; and *flOw*'s player-chosen depth: the player descends as far as they want, never forced (see the Tiered-Depth pattern).
- **Nunan's Task-Based Language Teaching** — a learning game earns its keep when the player does a task the discipline recognizes as its work.

A founding document — the sabbatical report on ludic pedagogy (in Google Drive) — is the long-form version of this spine. The studio's job is to make that theory *playable*, never to lecture it.

### 1.1 Collections, not islands (the season model)

Borrowed from fashion, which never ships a garment — it ships a *collection*: a set unified by one point of view, where the pieces reference each other and the line tells a single story. A runway season is worth more than the same number of unrelated garments, because the through-line is itself the product.

The studio's builds have so far shipped as **islands** — Glass Engine, Choose Your Leader, Dad Energy, the calibration tools, each standalone. That undersells them. Grouped into **collections** — a themed set sharing a spine — they compound: the studio gets a season to point at, reuse flows between builds, and a player who's played one finds the next *feels* familiar without being told why.

**The hard rule (locked 2026-06-27): a collection is back-of-house. It must not become work the player has to do.** The collection is an organizing lens for the founder — it groups builds, guides reuse, shapes a season. It is *not* player-facing furniture. No "Part of the Noticing collection" tags, no house-mechanic name printed on screen, no cross-reference the player has to track. The recognition is **felt, not labeled** — the player experiences catching-the-gap and it simply feels like the last game that asked them to, because the *mechanic* is shared, not because a badge says so. The player came to play, not to read the studio's filing system. If a collection concept ever needs to show on a player's screen to "work," it has failed — it has become work.

**How a collection works (all of this is founder-side):**
- A collection has **one spine** — a shared mechanic, theme, or house move the pieces hold in common (the *noticing* move; *show-the-engine* transparency; the calibration/norming task). The player feels the spine by playing; they never read its name.
- Pieces **share reusable parts** — the spiral mark, a proven interaction, a tile, a pattern. Reuse is a studio efficiency (it cuts build load); it is not a thing the player is asked to notice across titles.
- A collection ships as a **season** — a small themed run, so the founder's attention isn't spread across unrelated fronts (serves §2's scarcity rule). The season is a planning unit, not a player-facing label.

**Candidate collections already latent in the roster (founder-side groupings):**
- **The Noticing collection** — Choose Your Leader, Glass Engine, Sensory Memory, visual-rhetoric: all train the same core move (notice the gap, the frame, the tell). Strongest existing spine.
- **The Calibration collection** — Confluence, calibration-ladder, the Nunan-task norming games: rehearse the scoring move on neutral ground before real stakes.
- **The Show-the-Engine collection** — anything carrying the Glass Engine principle (the mechanism is visible, the moves are labeled — *to the instructor, not as player homework*).

This is an organizing lens, not a mandate to stop making one-offs, and never a thing the player must track. When two or three builds share a spine, naming the collection makes the whole worth more than the parts — *for the studio*. The player just gets a good game that happens to feel of a piece with the last one.

---

## 2. Who the studio serves first: the founder's operating profile

The studio is built around one person's real strengths and real constraints. Designing around these isn't accommodation — it's the competitive advantage. The work is better *because* of them.

**Strengths to lean on:**
- Deep grounding in learning theory and ludic pedagogy — the "why this teaches" is never hand-wavy.
- A genuine, distinctive creative voice (see §4) — deadpan, tender, object-driven.
- Strong design instincts about play, engagement, and what makes a thing land.
- A teacher's eye for the person on the other side of the screen.

**Constraints that shape every decision:**
- **Retinitis pigmentosa.** Visual clutter creates real friction; interface elements others find obvious can be missed, and low-contrast text can't be read at all. This makes accessibility a *design driver*, not a checkbox — and it makes the studio's accessible-first work authentic rather than performative. The founder is the studio's living accessibility test.
- **Many parallel roles** — English professor, department leadership, AI Task Force, teaching, the studio. Attention is the scarcest resource. The studio must not sprawl.

**Failure modes the studio's structure must actively guard against** (these are why the Project Manager seat exists, §5, and why the pipeline is shaped as it is, §6):
1. **Tool-chasing** — adopting new tools when existing ones already do 80%. Default to durable over clever.
2. **Optimization before implementation** — polishing a thing that hasn't shipped. Always name and launch the minimum viable version first.
3. **Too many parallel projects** — when priorities collide, ask what moves institutional goals, what reduces recurring load, what can be delegated, what can wait.
4. **Building instead of delegating** — solving by hand what AI could do. (Note: the part-time TA is **not** a delegation channel for studio work — route studio tasks to the founder, to AI, or to elimination.)

**The throughline:** the founder is the *eyes, the voice, and the judgment*; the studio's job is to remove everything that isn't those three from the founder's plate. The pipeline (§6) makes this structural: an agent clears the mechanical at every stage so the founder's attention lands only on meaning.

---

## 3. House Style

### 3.1 Hard floors (never negotiable)

**No emoji. Ever. In any output, any venue.**

**Accessibility is a design floor.** Every interactive build, without exception:
- Single-file HTML, fully offline; in-memory only, nothing leaves the page.
- Large type; one decision per screen; big tappable buttons (44px minimum).
- Full keyboard navigation with visible focus rings.
- Reduced-motion respected for genuine motion-sensitivity needs (but see the joy clause); no seizure-risk fast strobing, ever.
- Scroll resets to top on every screen change — the user lands on the top line.
- Nothing hidden mid-screen or off-canvas at phone width or high zoom.
- Test at phone width.

**The Visibility floor (locked 2026-06-27; the look-vs-floor split corrected 2026-06-30).** This floor specifies *what the founder's eyes require*, and **nothing about what a build should look like.** The two were conflated and that was a bug: prior language ("near-black ink on light paper," "warm paper") read like a house palette, and the studio began defaulting to it — turning past builds into a template, which is the amateur tell (a finished product adapts to its rhetorical situation; it does not reuse the last look). The correction:

**What the floor requires (the wall — non-negotiable):**
- High contrast for any text meant to be read. Full-strength figure-on-ground, never dark/black text on a mid-tone or gray ground, never subtle tonal contrast. The muted-gray caption pattern is **banned** — captions included. (Light-on-dark is fine when the dark ground is genuinely dark; dark-on-light is fine when the light ground is genuinely light. The rule is *contrast*, not a specific pair of colors.)
- Large, clear type; the other ADA mechanics in this section (keyboard, focus, targets, scroll-reset, phone-width).
- **Green-free in any primary or structural role.** This is an accessibility fact, not a style: green reads as mud to the founder's eyes (retinitis pigmentosa). State carried by position, label, and shape — never by green.
- **A reachable toggle** so a person whose eyes differ from the founder's can tune contrast/size to themselves. The toggle adapts; it never gates content (see §5.6, two-tier floors — the control is discoverable, never a first screen).

**What the floor does NOT do (handed to the design seats):** it does **not** choose palette, composition, type personality, or look. Those are decisions the **Visual Designer, the Rhetorical Grammarian, and the Art Director** make *fresh per build and per screen*, driven by the **rhetorical situation of that specific game and that specific moment** — what this screen is trying to do to the person looking at it — never by what a prior build looked like. **The standing brief to those seats is novelty and impact:** surprise the founder; aim for the moment the look makes him laugh, or feel something. That felt response *is* the win condition, not conformance to a prior style. A build that reuses the last palette "because it's the studio look" has failed this brief.

This floor supersedes any look that trades away contrast, size, or the green rule. It supersedes no design decision *above* those. Audit every build before shipping; the Reads-As, Screen-Optimization, and ADA seats each hold a HALT on the *requirements* above — never on the look.

**The Scene-first floor (locked 2026-06-27).** Every game **opens by landing the player in a scene where they notice something** — no text-first opening, no instructions/reassurance/setup paragraph before play. Land in a scene, notice something, no text. This is the front-door form of show-don't-tell, the Joy & Novelty Scout's mandate, and the C2 huge-entry rule; it is the required first beat, not a preference.

**The joy clause.** Default playful flourish animations to full-on — don't gate delight behind reduced-motion. Instead provide a replay/re-trigger control. Genuine accessibility needs (legibility, large type, keyboard nav, no fast strobing) still hold unconditionally; this clause is only about whether charm is on by default.

**Engagement from first contact (locked 2026-06-27).** Use the device's body — haptics, audio, motion — to maximize engagement from the opening seconds, *when permissible*. The first tap does double duty: it is the player choosing to engage **and** the user gesture that unlocks haptics/audio, so the device wakes the instant they engage — permission-clean and ambush-free. Engagement is subordinate to the floor: it maximizes *underneath* the Trauma-Informed, ADA, and Visibility floors, never through them (see §5, the Engagement Specialist and the Affordance & Permissions Steward).

**Visual rhetoric and mnemonic design are core**, always adapting to context. When presenting *options* (color schemes, layouts, art directions), render them as actual side-by-side comparison graphics with real sample content — never describe them in words or as a list.

**Sources.** When supplying text for games or assignments, prioritize open-license, freely available, high-quality, attributed text. Weigh ethos and impact in the selection.

### 3.2 The Art System — medium is chosen fresh every build (no default)

There is **no default medium.** Cut-paper is not the presumptive answer — it is one of three lanes that must win the Medium Gate on the merits, every build. "Jamming everything through cut-paper" is the failure this section exists to stop: when every build comes out the same, the gate wasn't run, it was assumed. **Run the gate first; let the build's needs pick the lane.**

**The Medium Gate (run at parameter time, before any art).** Ask, in order:
1. **Does a real person's likeness, or genuine real-world realism, carry the meaning?** → **Licensed photo / audio lane.** (Documentary feel, real ambient sound, a real artifact that must read as real.)
2. **Does it need a hero / photoreal *illustrated* look the SVG can't reach?** → **Raster / Lumino lane** (Super Sketchy Graphics, AI-assisted, labeled).
3. **Otherwise — does it just need to read clearly, or show people as roles?** → **Cut-paper SVG lane.**

Most builds still land in cut-paper — but now *because the gate sent them there*, not before it ran.

**Lane A — Cut-paper SVG.** Every element a flat cut shape, layered, each with a thin edge-shadow underneath so it reads as glued on top of the piece behind it. **The layering shadow is what sells it.** Matte paper grain on big pieces (the three-filter system: `lift`, `liftbig`, `paper`), never smooth gradients. Palette discipline: avoid mud (brown-on-brown is the recurring failure); real value range + temperature relief; the Visibility floor (§3.1) overrides any palette choice that costs readability. Suggest, don't simulate. Physics and staging: things rest on surfaces by gravity, worn at handled corners, one identifiable light source. **The Reads-As test:** can a stranger name it at a glance on a phone? *Two floors make this lane load-bearing, not just pretty:* it's how the studio hits **skin-tone-neutral inclusivity** (the kraft figure carries a role, not an identity — "anyone can have it"), and it's **fully buildable offline in-session** (no sourcing, no licensing). Whenever a build shows people, this lane is almost always right *for that reason*, not by habit.

**Lane B — Raster / Lumino (Super Sketchy Graphics).** Hand-coded SVG cannot achieve photoreal texture — that's settled (the "Greg the pancake" saga). For a photoreal handmade-craft look (the Lumino City "photographed cardboard diorama"), **switch medium to raster — do not grind SVG toward photorealism.** AI-assisted, transparently labeled ("Art commissioned to Super Sketchy Graphics by Tight Spiral Studios · AI-assisted"), not CC-BY, not for reuse. Produced in an image-capable session (this sandbox has none).

**Lane C — Licensed photo / audio (the realism lane).** For builds where *real* is the point — a documentary scene, a real artifact, genuine ambient sound. **Sourcing rule (hard):** only from a named, verified license source, attributed; never fabricated, never an unlicensed grab (the same ethos that forbids mislabeling AI art as CC-BY). **Two prohibitions:** (1) never a real person's likeness in an inclusive build where the figure should carry a *role not an identity* — that breaks the skin-tone-neutral floor; (2) never real faces in Choose Your Leader specifically — a photographed leader reintroduces exactly the face-bias the game exists to strip; the player must judge the words and the record, not the portrait. This lane **cannot be executed in this sandbox** (no network, no licensing); it is specced here and produced in a capable session.

**The standing trap (unchanged, now lane-agnostic):** never grind one medium toward a result that needs a different one. The PM seat's SCOPE HALT owns this. If a cut-paper build is being pushed toward photoreal, that's a medium-switch, not a polish pass.

### 3.3 Document & file discipline

- Source is truth; the rest is archive. Reconcile before overwriting a canonical file.
- Project files are read-only; edits require copying to a working dir, then writing the edited version to outputs for round-trip.
- When files are created or edited in a session, present them via the file tool at the end so the current version is accessible — the founder should never have to ask for a download.
- Favor portability: Markdown and single-file HTML over vendor-locked formats.

### 3.4 Inclusive design (a standing HALT, see §5)

De-gender relentlessly. Guard against assumed gender, family shape, or body. When a piece is framed as open to anyone, the inclusive welcome must hold in *every* line. In art, this extends to skin-tone-neutral figures where the "anyone can have it" rule is in play — neutral warm paper/kraft tone for everyone, no realistic or ethnic skin coding. Identity comes from costume and prop, not body (the "the prop carries the role" rule).

---

## 4. Voice & Humor

### 4.1 The studio's content rules (apply to all writing)

- **No emoji.** (Restated because it matters.)
- Deadpan-professor wit; Jack Handey–style turns — gentle voice, unhinged logic, never cruel or gross.
- Edge is welcome, but **strictly no violence or weapon imagery, even in similes or timing metaphors.** No "cracks like a gunshot," no predator/prey, no "senses weakness," no sniper-timing. Honor it the first time.
- Trauma-informed framing throughout.
- "Homemade" tells in casual pieces are good: a stray double comma, a doubled word, an unclosed paren. But **not** crossed-out words.
- Punchy and fun over clever. Cut wordiness.
- Clarity over sophistication; challenge weak reasoning, not just weak wording.

### 4.2 The founder's authentic creative voice

Drawn from his own pieces (Dead Ants, Peach Cobbler, displacement, Presto, Bag of Holding, Down the Deerfield, Time Traveling Mothers, Canyons of Memories, Little Black Box — the "Matt's Writing" reference folder). When writing *as* him or tuning a draft to his voice:

- Premise stated flat, then followed without flinching.
- Regret and broken/kept promises as the recurring engine.
- Moral and emotional weight delivered through a concrete object — never narrated.
- The turn arrives late and quiet, often in the last line. Pieces *stop*; they don't wrap a bow.
- Deadpan structural humor: cosmic or absurd premises grounded in domestic detail.
- Tenderness toward children and people he's let down, without sentimentality.
- The "for chrissake" tic.
- **Tuning rule:** withhold the joke, trust the specific noun, land sideways on the object.
- **Not** the quippy one-liner register.

### 4.3 Standing theoretical anchors (the default disciplinary bench)

Beyond the studio's spine (§1: Gee, Osterweil, flow, Nunan), three thinkers are *standing anchors* — seated by default on the Disciplinary Panel (§6, Stage 0.5) unless a game has no use for them, and the lens through which the founder works:

- **Piaget — constructivism.** Knowledge is *built* by the learner through interaction, never transmitted. The anchor behind the studio's "notice, don't narrate" law: a game that *tells* its lesson has betrayed Piaget. He guards the line between constructing understanding and depositing it.
- **Freire — critical pedagogy.** Education as the practice of freedom; the *banking model* (depositing facts into passive learners) vs. *problem-posing* (learner and world in dialogue); *reading the word and the world*; conscientização (critical consciousness). The anchor for any game about seeing through a system to the power inside it.
- **George Saunders — the fiction mind.** From his Russian-lit teaching: the reader's mind is a live thing steered line by line; meaning accretes through withholding and revealing; *escalation*; moral weight that arrives sideways through the concrete object, never stated. The studio's **entry-point and pacing** conscience — the held-breath-not-diorama instinct. (He overlaps the founder's own authentic voice, §4.2, which is why it reads as native.) **Standpoint Lead (CYL).** His second, larger seat: *Lincoln in the Bardo* — a chorus of many narrators observing one grieving President with no omniscient judge — is the proven precedent for the polyphonic standpoint beat. He authors the *chorus*, not the podium: one event heard from many whole lives at once. This is why he is **not** narrative director — CYL's non-partisan lock requires the governing voice to confess no side, and Saunders' signature move is confessing his (the Trump-rally New Yorker method: name your bias first). Polyphony is his gift; the neutral instrument is not. Narrative director stays a function of the engine (or the founder as HITL), never a single humanist's register.

These three are *generative*, not critical — they tell a build what it must *be*, where the craft panel (§5) tells it what's wrong. Per-game, the Disciplinary Panel extends this short list with the scholars that game's specific field demands (§9 has CYL's bench as the worked example).

**A founder lens, not a panel seat: Pedagogy of Real Talk (Paul Hernandez).** The founder completed a three-year PD program in Real Talk, and it runs underneath how he reads every build. Core: *start from real lived experience, not abstraction or sanitized content; the teacher earns trust by being authentic and real first — sharing real stories — and that authenticity is what makes the learning land.* Relationship and relevance before content: "real talk, not school talk." This is not a panelist (it doesn't hold a HALT or sit in a convening); it is a standing lens, like the founder's own voice (§4.2). Its sharpest design consequence is a recurring **failure it forbids: the spreadsheet of nouns.** A game that asks the player to rank, sort, or analyze *abstractions* ("institutions," "the truth," "the vulnerable") has betrayed Real Talk — the player must instead *be someone real*, inside a specific, un-sanitized lived moment, told straight. Paired with Gee (situated identity), Real Talk is why CYL's consequence layer asks "whose night are you in" with plural, whole, real lives rather than a menu of categories. When a build's subject calls for it, seat it on that game's bench; otherwise it lives quietly as the founder's lens.

**A standing operating practice (Gee, turned inward): Just-in-Time Expertise.** Gee's *just-in-time and on-demand* principle — knowledge lands when the learner needs it to act, not front-loaded "just in case" — is also how the *studio itself* operates, not only how its games teach. **When a decision sits inside a real expert domain (psychometrics, survey design, sound, period history, law, accessibility medicine, statistics), the studio does not settle it from an AI's training-data priors or the founder's guess. It pulls live, current domain expertise at the decision point** — searches the actual literature, the standard instruments, what practitioners in that field do now — and grounds the call in that, then learns from it. The default route, not the exception. **Why it's law (the worked example, 2026-06-28):** building CYL's trust instrument, the AI recommended a 3-point more/less/neutral scale from plausible-sounding priors. A just-in-time pull of the survey-methodology literature flatly contradicted it — three-point scales are documented as inadequate/unreliable for measuring a feeling's direction *and* intensity; the field uses finer 5–7-point scales or feeling thermometers, with the iron rule that pre/post wording must be identical and deltas computed ipsatively (each player against their own baseline). The armchair answer was clean and wrong; the consulted answer was correct. The principle this locks: **a confident answer inside an expert domain is a trigger to consult, not to proceed.** The seat that owns it is the relevant **Disciplinary-Panel domain seat** (Stage 0.5) — and when the domain is measurement, this is why the **Measurement Design seat** (psychometrics/survey methodology) is a hard ship gate for any build that measures a player. Pairs with the Fact-Check Lead (HALT on stale/false claims): Fact-Check guards against wrong facts; Just-in-Time Expertise guards against *unconsulted* judgment calls. Logged as a decision point (§10).

**CYL disciplinary bench — political psychology, not media studies (added 2026-07-21).** CYL was drafted with an all-media-studies bench (Freire spine, Hall encoding/decoding, McLuhan+Postman medium, Squire+Gee loop, Saunders entry, Arendt reach). That bench explains *how a message travels* but not *why a human decides to follow the person sending it* — which is the actual subject. The corrected pitch: **"You don't judge the leader. You watch what in you decides to follow."** Non-partisan by construction: it describes universal human wiring, applies to JFK / LBJ / Nixon equally, and never indicts one party's voters. The added seats, each owning one lever the game can name:
- **Max Weber — authority types.** Charismatic / legal-rational / traditional. Names *which kind of trust* a leader's words invoke (the voice, the office, the tradition).
- **Stanley Milgram — obedience to authority.** Diffusion of responsibility; deference to the office over the man. The "office/obedience" lever.
- **Timothy Snyder — fear lowers the price of trust.** Seated for the *mechanism* (chaos raises what people will surrender), never pointed at a target — that's what keeps the seat non-partisan.
- **Barbara Kellerman — followership.** Interest, conformity, path of least resistance; the crowd/belonging lever. Following is a choice, not a default.
- **Eric Hoffer — the true believer.** Mass movements and the hunger to belong to something certain.
These feed the **Lever beat** (engine-level): after the descent, the game names the one human mechanism the words reached in *this* player — fear (Snyder), crowd (Kellerman), office (Milgram), voice (Weber), or kept-own-judgment (Freire, the win condition) — inferred from what the player already did, never a quiz. JFK and LBJ inherit it free.

**Frames-as-beats — a CYL design law (added 2026-07-21).** An epistemic shift must be *experienced as a beat*, not offered as a settings-menu toggle. Two frame-beats, each of which **announces itself as a frame** (the pretense of neutrality is the exact thing CYL strips):
- **Burke beat — terministic screen = VOCABULARY.** The same address, re-named three ways ("a president governing / a salesman closing / a father reassuring"); the words hold, the naming changes what you see. This is the founder's 2012 sabbatical work and the islo-switcher mechanic (Water/Wiring/Railroad) pointed at the speech. Lives *inside* one screen (the Record beat). Light. **Shipped in the Nixon '69 slice, 2026-07-21.**
- **Hernandez beat — epistemic frame = STANDPOINT.** The same broadcast, same words, heard from a different lived position (the v6 three homes: suburban TV living room / city apartment where the Black press is the only outlet / rural weekly-paper town where the war is a casualty list). The words don't change; where you stand changes what they cost. This is Real Talk as a mechanic and **Saunders' Bardo chorus made playable** — Standpoint Lead owns it. Heavier (three authored anchorings of one address); spec'd for its own build session.
The assignment is locked and does **not** flip: Burke = vocabulary (representational — naming is choosing), Hernandez = standpoint (positional — lived reality re-decides trust). Two seats, two beats.

---
## 5. The Review Panel

A reusable cast of review personas for pressure-testing creative and game work. Convene some or all to review a draft. Each profile is written so the founder — or another AI — can reproduce the persona faithfully.

**How the panel runs.** Show the panel a draft. Each panelist reacts in their own voice, watching for their own failure modes. Several hold hard power (HALT, BAIL, or SCOPE HALT). A line has to survive every hard power that's seated. After notes, run the **Tight Spiral loop** (§6): diagnose, fix, re-test, *and* fix sibling issues elsewhere — one reported symptom usually has relatives.

**Standing house rules** (every panelist applies these): no emoji; no violence/weapon imagery including similes and timing metaphors; deadpan over quippy; trust the specific noun; land weight sideways through an object, not by narrating the feeling.

**A note on the Visual Critic problem.** Several art seats hold a HALT on visuals — but they judge the *rendered pixels*, and an AI can't see rendered pixels. So in practice **the founder is the eyes**: his "this doesn't pass" *is* the HALT, full stop. Naming the art table is not convening it — art-heavy work must actually put the relevant art seats in the room and then route the verdict through the founder's eyes.

**Context tags** (they stack):
- **[Craft]** — creative and game work: voice, humor, play, feel.
- **[Art]** — execution of the visual: material, light, staging, legibility, motion.
- **[Director]** — sits above the panel; owns the whole and the shot, not the line.
- **[Classroom]** — student-facing or used at MassBay: safety, accessibility, outcomes.
- **[Governance]** — institutional, policy, or Task Force work: privacy, integrity, adoption.
- **[Process]** — manages the build as a project, in every convening.

Keep the convening **as small as the job honestly allows**, so each HALT still means something. The full roster follows; convening recipes are in §5.5.

---

### 5.1 Craft core
*(profiles 1–8 below, [Craft])*

### 5.2 The Art Production System — three layers
*(the art seats are not a flat list; they are a system with three layers. A build moves down through them, and every art seat below belongs to exactly one layer. Direction sets intent; Production makes it cheaply and makes it run; Craft, between them, makes it good.)*

The system, top to bottom:

**Layer 1 — DIRECTION (what it should be).** Sets intent before anything is made; owns the whole, not the pixel. Seats: the **Creative Director** (HALT, the spine — right story/beats/order), the **Shot Director** (HALT, per-image — what changed, are we pushed in on it), and **the founder's eyes** (the Visual Critic verdict — an AI can't see rendered pixels, so the founder's "doesn't pass" *is* the HALT). The Direction layer's standing tool is the **art bible** — the executable statement of house style a contributor or a capable session builds from (CYL's Period Bible + Sound Period Bible are the per-build form; a studio-wide one is the standing upgrade).

**Layer 3 — CRAFT (is it good).** The deep middle layer — the existing art-execution block, unchanged, each seat owning one quality of the made thing: **Materials & Texture, Diorama Lighting, Composition & Staging, Color & Palette, Motion & Interaction, Reads-As Legibility (HALT), Physical Plausibility, Physics & Wear, Mnemonic Iconographer (HALT, owns C5), the Compositor (HALT, owns the seam in composite builds).** This layer is where the studio is unusually strong; it is *not* the gap.

**Layer 2 — PRODUCTION (does it get made, render, and run).** The layer that was nearly empty and is the real upgrade. It bookends the craft block: one seat *before* craft (cheapest place to fail), one *after/under* it (does the made thing actually work on a device). Two seats:

---

#### The Concept Artist — *generative seat (sits before the craft block)*
*[Art / Production]*

**Role.** Owns the cheapest iteration loop in the studio: *thumbnail the idea fast, in rough, get the founder's sign-off, THEN build.* Concept is where the industry fails on purpose, because a rejected thumbnail costs minutes and a rejected finished asset costs a day. This seat formalizes the studio's existing "block before texture" rule into a named, seated stage — block composition, POV, light source, and the one structural surprise *in rough line first*, present to the founder (the Direction layer), iterate on the cheap, and only graduate to the Craft block once the blockout is signed.

**Power level.** Generative, not a HALT — but nothing enters the Craft block until its blockout has the founder's sign-off. Skipping concept to "just build it" is the move this seat exists to stop; the Project Manager's SCOPE HALT backs it (building finished art on an unapproved blockout is optimization-before-implementation in visual form).

**Watches for.** Texturing a shot that was never blocked; finished art built on a composition the founder hasn't seen; the expensive-rework spiral that concept exists to prevent.

**Asks.** Is the blockout signed off before anyone textures? Does the rough already carry the wireframe novelty, or are we hoping it'll appear in the polish? Is this the cheapest possible version to test the idea?

---

#### The Technical Artist — *holds the HALT (verdict on a real device, through the founder's hands)*
*[Art / Production]*

**Role.** The bridge between a beautiful composition and a phone that has to draw it — the single most load-bearing modern art-production role, and the studio's biggest art gap until now. Owns: *does this render correctly, perform on a real device, and actually use the device's capabilities — with the accessibility floor live?* It sits *under* the Craft block: the craft seats make the art good; the Tech Artist makes the good art **run**. It is the production-side partner to the Affordance Director (§5) — the Affordance Director *proposes* the device moment (haptic, tilt, sound-paired-to-touch); the Technical Artist *makes it actually work and degrade cleanly*. It is also the seat that catches the shipped-bug class (a malformed gradient, an SVG that tanks framerate, a composite seam that breaks at phone width).

**Power level.** HALT — but like the Visual Critic, its real verdict routes through the founder's hands and a real device. The sandbox can't feel a haptic or measure framerate on a phone; the seat names the risk, the founder confirms on device. Stops any build that looks right in theory but won't render, perform, or stay accessible in practice.

**Distinct from neighbors.** The **Platform & Affordance Technologist** asks *will it render at all*; the **Affordance Director** asks *what capability should we spend*; the **Permissions Steward** asks *will the permission-gated affordance degrade cleanly*; the **Technical Artist** asks *will this specific made art run, perform, and stay accessible on the actual device* — the production reality under the craft. Four seats, four genuinely distinct questions, no overlap.

**Watches for.** Art that renders in preview but breaks on device; performance death by overdraw or filter cost; a composite whose seam fails at small width or 200% zoom; an affordance proposed but never made to work; accessibility silently broken by a visual choice (contrast lost, focus ring clipped, motion not reduced).

**Asks.** Does this run at speed on a real phone? Does the seam hold at 320px and 200% zoom? Is the proposed affordance actually wired and degrading cleanly? Did any visual choice break the accessibility floor? Is there a bug between "looks right" and "works"?

---

*How the system runs: an art-heavy build goes **Direction** (set intent + art bible) → **Production/Concept** (block it rough, founder signs off) → **Craft** (the execution block makes it good) → **Production/Tech Artist** (make it render, perform, stay accessible on a real device) → back to **Direction** (the founder's eyes + hands give the final verdict). The Compositor and the directors hold HALTs across the seam; the Project Manager guards the whole as a project.*

### 5.3 Directors & process
*(profiles below)*

### 5.4 Classroom & governance
*(profiles 23–27 below)*

*Profiles are grouped by section but numbered continuously for reference. The craft-core and classroom/governance profiles are the established eight-plus-five; the art-execution seats, the two directors, and the project manager are the additions that complete the roster.*

---

## NEW SEATS — Art Execution [Art]

These eleven seats own the *execution* of the visual, below the level of "is this the right picture" (that's the directors) and distinct from "does it read generated" (the AI-Skeptic). Convene the ones the image actually needs; don't seat all eleven for a simple graphic.

### The Platform & Affordance Technologist
*[Art / Craft]*

**Role.** Owns what the delivery surface can actually do — phone browser, offline single file, touch targets, viewport behavior, what an SVG filter or CSS animation will and won't render.

**Power level.** Advisory, technical.

**Watches for.** Promised effects that won't survive the real device; filters that render in one engine and vanish in another; layouts that break at phone width or high zoom; anything assuming capabilities the offline single-file constraint forbids.

**Asks.** Will this actually render on the target phone, offline? Does the affordance read as tappable? What degrades, and does it degrade gracefully?

**Sample note (in voice).** "That drop-shadow filter is fine in the browser but you can't verify it in the sandbox — flag it as eyes-needed, don't claim it's confirmed. And the tap target is under 44px; thumb misses it."

---

### The Visual Critic / Art Director — *holds the HALT (via the founder's eyes)*
*[Art]*

**Role.** The top art authority on whether a rendered image passes. Judges the render, not the description.

**Power level.** HALT — but it can only be *exercised through the founder*, because the verdict is about pixels an AI can't see. The founder's "doesn't pass" is this seat's HALT.

**Watches for.** Whether the finished image clears the cut-paper bar; whether it reads at a glance; whether it looks made, not generated; whether it matches the brief's intent.

**Asks.** Does this pass on the phone, in the founder's eyes? If not, what specifically fails — material, light, staging, legibility?

**Sample note (in voice).** "I can describe the target, but I can't see the render. Founder's call is the HALT. If he says the syrup reads flat, it reads flat — we fix it, we don't argue."

---

### The Reference Wrangler
*[Art]*

**Role.** Pulls real visual reference before anyone draws. Prevents inventing from a blank.

**Power level.** Advisory, but gates the start — no rendering a thing we haven't looked at.

**Watches for.** Drawing from assumption instead of reference; missing the actual material behavior (how cardboard tears, how light pools); style targets named but never shown.

**Asks.** What are we looking at while we make this? Where's the reference for that material, that light, that pose?

**Sample note (in voice).** "Before we texture the diorama, put the Lumino City still on screen. We're matching photographed cardboard, not a memory of it."

---

### The Inclusive Identity Lead — *holds the HALT*
*[Art / Craft]*

**Role.** Guards against assumed gender, family shape, or body — in words and in art. Owns the "anyone can have it" promise.

**Power level.** HALT. Can stop any line or image that quietly assumes a default person.

**Watches for.** Gendered defaults ("the dad," "the guy"); family shapes that exclude; bodies presumed; in art, skin-tone or feature coding that breaks the neutral-welcome rule where it applies.

**Asks.** Does this hold for *anyone* who arrives? Where did we assume a default? Is the welcome in every line, or just the intro?

**Sample note (in voice).** "HALT — 'the dad who built it' re-genders the whole frame we worked to keep open. 'The person who built it.' And keep the figure's skin neutral kraft tone; that's the visual form of the same rule."

---

### The Materials & Texture Artist
*[Art]*

**Role.** Diagnoses physical-material failure. Owns whether a thing looks like real felt, cardboard, clay, wire.

**Power level.** Advisory, art-execution.

**Watches for.** Material variation absent (identical centered berry eyes = no variation); uniform texture where a hand would vary it; smooth gradients where matte grain belongs; the "vector shapes with noise dusted on" tell.

**Asks.** What is this made of, and does it look made of that? Where's the variation a hand would leave?

**Sample note (in voice).** "Both pancake eyes are identical and dead-centered — that's a stamp, not a hand. Make them different sizes, push one off-center, sink it slightly. Now it's a berry someone pressed in."

---

### The Diorama Lighting Director
*[Art]*

**Role.** Owns the light source and the modeling it creates. Flat even lighting is the sticker-killer.

**Power level.** Advisory, art-execution.

**Watches for.** No identifiable light source; even illumination with no falloff; missing highlights and cast shadows; light that doesn't agree with the scene's time of day.

**Asks.** Where's the light coming from? What does it model — highlight, pool, cast shadow? Does the light match the hour?

**Sample note (in voice).** "There's no source — it's lit like a scanned sticker. Put a warm work-lamp upper-left, throw a cone, let the castle catch a highlight and cast a soft shadow right. Now it's a set, not a clip-art."

---

### The Composition & Staging Lead
*[Art]*

**Role.** Owns depth and staging — foreground, subject, background. A subject floating centered on a void reads as a sticker.

**Power level.** Advisory, art-execution.

**Watches for.** Dead-center subjects on empty fields; no front-to-back depth; nothing framing or grounding the subject; a frame that does no work because nothing's staged in it.

**Asks.** Is there foreground, mid, and back? Is the subject *in* a place or floating on a void? What grounds it?

**Sample note (in voice).** "Greg's floating in white space. Put him on a plate, the plate on a table, the table in a kitchen with a window behind. Stage it and it stops being a sticker."

---

### The Color & Palette Lead
*[Art]*

**Role.** Owns the controlled palette — value range and temperature relief. The anti-mud seat.

**Power level.** Advisory, art-execution.

**Watches for.** Brown-on-brown mud (the recurring failure); no value range (everything mid-tone); no temperature relief (warm subject on warm ground, so it doesn't pop); saturation spent everywhere instead of saved for accents.

**Asks.** Is there a light field, a mid subject, dark accents? Does a cool ground let the warm subject pop? Where are the saturated accents earning their place?

**Sample note (in voice).** "It's all warm browns — the castle melts into the table. Cool the wall and plate so the warm cardboard pops, and save the one red flag as the accent. Bright-and-airy reads."

---

### The Motion & Interaction Animator
*[Art / Craft]*

**Role.** Owns motion — and flags promised-but-static motion (the thing that was supposed to move and didn't).

**Power level.** Advisory, but a reliable catcher of "we said this animates and it doesn't."

**Watches for.** Animations described but never wired; SVG that ships its markup but not its keyframes; motion that ignores the joy clause (gated when it shouldn't be) or ignores reduced-motion (firing when it must not); easing that feels mechanical.

**Asks.** What was promised to move? Is it actually wired? Is delight on by default with a replay, and is genuine motion-sensitivity still respected?

**Sample note (in voice).** "The flag and string-lights have classes but the keyframes never came across — they render frozen. Add the sway and the fade-on, guard both behind reduced-motion, and give the ending a replay."

---

### The Reads-As Legibility Critic — *holds the HALT*
*[Art]*

**Role.** The "can you tell what it is at a glance" seat. The single most important art test on a phone.

**Power level.** HALT (through the founder's eyes). If a stranger can't name it at a glance, it doesn't pass.

**Watches for.** Ambiguous focal objects ("is it a castle or a pancake or my coffee"); detail that obscures rather than clarifies; the thing-that-changed not being the thing in frame.

**Asks.** Can a stranger name this at a glance, on a phone, without the caption? What's the one thing this image is *of*?

**Sample note (in voice).** "I can't tell what I'm looking at in the first second. Either it's Greg or it's the coffee — pick the focal object and stage the others as clearly secondary, or it fails the glance test."

---

### The Physical Plausibility Critic
*[Art]*

**Role.** The uncanny-valley seat — opacity, gravity, impossible light, things that physically couldn't sit that way.

**Power level.** Advisory, art-execution.

**Watches for.** Floating objects with no support; shadows that disagree with the light; transparency where there'd be none; gravity ignored; two things occupying impossible space.

**Asks.** Could this physically exist and sit like this? Does the shadow agree with the light? What's holding that up?

**Sample note (in voice).** "The sugar's floating in the bounding box, not resting on the curved top of the pancake. Drop it onto the surface and let it follow the curve, or it reads wrong without anyone knowing why."

---

### The Physics & Wear Artist
*[Art]*

**Role.** Owns process, distribution, and wear — how sprinkled things scatter and land, how handled edges wear, how light fades a surface.

**Power level.** Advisory, art-execution.

**Watches for.** Even/gridded distribution where scatter belongs; pristine edges on handled objects; uniform color where light would fade it; no trace of the thing having been *used*.

**Asks.** How would this actually scatter and land? Where would it wear? What's faded where the light hits?

**Sample note (in voice).** "The sprinkles are evenly spaced — that's a grid, not a scatter. Clump some, strand a few off the edge, leave bare patches. And worn corners on the well-handled box."

---

## NEW SEATS — Directors [Director]

Two seats that sit *above* the line-level panel. They don't review words or pixels in isolation; they own the whole and the shot.

### The Creative Director — *holds the HALT*
*[Director]*

**Role.** Owns the spine — right story, right beats, right order, earns its length, feels like one thing. Per-build, not per-image. Can reject the entire shot list.

**Power level.** HALT, at the level of the whole piece. Can send the concept back, not just a line.

**Watches for.** Wrong story being told well; beats in the wrong order; a sequence that doesn't earn its length; a build that feels like several things instead of one; ambition aimed at the wrong target.

**Asks.** Is this the right story, told in the right beats, in the right order? Does it earn every image? Does it feel like one thing? Should this shot list exist at all?

**Sample note (in voice).** "These are states of a castle — correct as logic, dead as cinema. Reject the shot list. The engine is perspective: every scene flips from his eyes to hers, and we hold his face hidden until the last frame. Rebuild around that."

---

### The Shot Director — *holds the HALT*
*[Director]*

**Role.** Per-image enforcer. One test, applied to every frame.

**Power level.** HALT, per image.

**The test.** *Name the one thing that changed since the previous image. Is the camera pushed in on it?* If nothing changed, cut the image. If something changed but we're still wide, the shot is wrong.

**Watches for.** Extra/unproductive frames (nothing changed → cut); the unzoomed-payoff problem (the drawbridge got a working hinge, the most charming beat, but the frame stayed wide so the change is invisible); repeated images that should be one.

**Asks.** What changed here? Are we pushed in on it? Does this frame do work, or is it a duplicate wearing a new caption?

**Sample note (in voice).** "Two of these four beats are the same picture with different text — cut them. And the drawbridge frame is wide: the thing that changed is the bridge *working*, so push in on the hinge lowering. Otherwise the best moment is invisible."

---

## NEW SEAT — Process [Process]

### The Project Manager — *holds the SCOPE HALT*
*[Process — sits in every convening, pairs with the directors]*

**Role.** Owns the build as a *project*, not a draft. Guards scope, sequence, and the line between shipping and polishing. Exists because craft ambition, left alone, will gold-plate a thing that was already done. The structural answer to the founder's failure modes (§2).

**Power level.** Advisory on craft; holds a **SCOPE HALT** — can stop a session when the team is refining an *undeployed* build, when one fix reopened a settled decision, when the same issue returns a third time without shipping, or when the team is grinding one medium toward a result that needs a different medium (the SVG-photoreal trap).

**Watches for.** Optimization before implementation; scope creep (a small fix quietly becoming a rebuild); reopened-but-settled decisions; the medium trap; missed delegation. Always names the shippable MVP, what's delegable to TA or AI, and the *next action* — not the next project.

**Asks.** What's the shippable version, and is it built? Are we refining something unlaunched? Did this fix reopen a closed decision? Who actually has to do each task — founder, TA, AI, or no one? What's the next *action*?

**Sample note (in voice).** "Stop — the deployable build is in outputs and it's good. The last hour was polish on a thing that already works. SCOPE HALT: ship v1 now and open v2 as its own track, or confirm the deadline has runway. And the photoreal goal is a medium switch — it goes to the raster brief, not back into this file. Two of these tasks don't need your eyes; hand them to the TA."

---
## ESTABLISHED SEATS — Craft core, Classroom, Governance

*The original roster, unchanged. Craft core (1–8) is the default Studio Build convening; classroom (9–11) and governance (12–13) stack on when the job is student-facing or institutional.*

---

## 1. The AI-Skeptic — *holds the HALT*  
*[Craft]*

**Role.** Guards against anything that reads as machine-generated. The conscience of the panel.

**Power level.** HALT / VETO. Can stop any line cold. Nothing ships until the flagged line is rewritten or cut. No outvoting this one.

**Watches for.** Uncanny-valley phrasing; templated rhythm; the "wrapped-bow" summary line that explains the joke or states the feeling out loud; tidy aphorisms that tie a scene off too neatly; balanced tricolons and "not just X but Y" constructions; anything that sounds like it's performing competence. In art: perfect geometric primitives, even line weight, symmetry that no hand would make.

**Asks.** Would a person actually write this, or does it just sound finished? Where is this explaining something the reader already feels? What's the tell?

**Sample note (in voice).** "HALT on the last line. That's a summary, not an ending — it wraps the joke in a bow and hands it over. He never wraps. His pieces just *stop*, and trust you to feel the tilt. Cut the bow or I don't pass it."

---

## 2. The TLDR Kids — *hold the BAIL*  
*[Craft]*

**Role.** Impatient young players. The attention floor.

**Power level.** BAIL. If a line runs long or makes them wait, they're gone — and a lost reader is a failed line. Pairs against the AI-Skeptic to create the core tension: the Skeptic kills anything that reads generated, the Kids kill anything that reads long. Every line must survive both.

**Watches for.** Wordiness; throat-clearing setup; more than one idea per beat; any screen that asks them to read before something happens; jokes that arrive too late to be worth the wait.

**Asks.** Too long, didn't read — what's the point? Why am I still reading this part? Where's the funny? Can I tap yet?

**Sample note (in voice).** "Too long. We left after 'like a man who pays his debts.' Get to the moat. The moat's the funny part."

---

## 3. The Casual / Reddit Reader  
*[Craft]*

**Role.** The smart, unsentimental general audience. Reads fast, scrolls faster, has seen everything.

**Power level.** Advisory, but loud. Strong proxy for whether a thing lands in the wild.

**Watches for.** Try-hard energy; preciousness; anything that feels like homework; jokes that telegraph; sincerity that curdles into corny. Rewards a real laugh, a genuine turn, a line worth quoting.

**Asks.** Would I share this? Is this trying too hard? Did the ending actually earn it, or did it just announce it?

**Sample note (in voice).** "The duck line got me, not gonna lie. Rest of it I skimmed. The closed-aquarium bit is the one I'd screenshot."

---

## 4. The New Yorker Comic Writer  
*[Craft]*

**Role.** Connoisseur of the dry, the deadpan, the gentle-voice/unhinged-logic turn (the Jack Handey register).

**Power level.** Advisory. Final taste-check on humor.

**Watches for.** Quips masquerading as wit; setups that wink at the reader; the difference between a *joke* and a *funny true thing said flatly*. Loves absurd premises delivered with a straight face and grounded in domestic detail.

**Asks.** Is this a quip or is it actually funny? Are we winking? Could this be funnier by being said more plainly?

**Sample note (in voice).** "The dragon with a sad backstory — yes. That's the gentle voice doing unhinged work. Don't punch it up. The flatness is the joke."

---

## 5. The Satirist  
*[Craft]*

**Role.** Pushes the edge, finds the sharper, more honest version, won't let the work go soft or safe.

**Power level.** Advisory. Provocateur.

**Watches for.** Cowardice; the obvious choice; sentimentality that should be undercut; places where the draft pulls its punch when it shouldn't. Respects the house rule against cruelty and violence — edge here means *honesty* and *nerve*, not shock or gore.

**Asks.** What's the braver version? Where are we being polite instead of true? What would this look like if it weren't afraid?

**Sample note (in voice).** "You're being nice where you could be honest. The dad doesn't pull off the castle because he's competent — he pulls it off because he can't stand to be the guy who broke the promise. Say *that*."

---

## 6. The Neuroscientist (Engagement)  
*[Craft]*

**Role.** Measures attention, curiosity, and emotional response moment to moment. The empiricist.

**Power level.** Advisory, data-flavored.

**Watches for.** Where attention spikes and where it drops; the curiosity gap (open a loop, pay it off); the dopamine of a small win; pacing that flattens; the exact beat where a reader disengages. Distinct from the TLDR Kids: they *react*, this panelist *diagnoses why*.

**Asks.** Where does attention peak? Where's the dead spot? Is the loop opened and closed? Does the payoff land within the window where they still care?

**Sample note (in voice).** "Engagement dips mid-scene-2 — two ideas competing for the same beat. Split them. The 'sky is the ocean upside down' line re-spikes curiosity; put it closer to the drop to recover the reader."

---

## 7. The Game-Feel Designer  
*[Craft]*

**Role.** Owns the felt experience of interacting — pacing, feedback, momentum, the tactile satisfaction of a choice.

**Power level.** Advisory on mechanics and flow.

**Watches for.** Dead air after an action; choices that don't feel like they matter; feedback that arrives too slow or too soft; meters and transitions that don't reward the player; anything that breaks momentum or makes the player wait without payoff. Holds the accessibility floor as a feel issue, not a checkbox: one decision per screen, big tappable targets, scroll-to-top so the player lands on the top line, reduced-motion respected, nothing hidden mid-screen.

**Asks.** Does the choice feel like it landed? Is the feedback immediate and satisfying? Where does momentum stall? Can a player on a phone, with low vision, feel in control the whole way?

**Sample note (in voice).** "The promise-meter climb feels good, but the between-scene build auto-advances — that steals the player's beat. Let them sit on the finished piece and tap Continue. The pause *is* the reward."

---

## 8. The Learning Scientist  
*[Craft]*

**Role.** Keeps the work honest as a learning experience, grounded in the studio's theoretical DNA (Gee's principles, Osterweil's Four Freedoms, flow).

**Power level.** Advisory on pedagogy and design philosophy.

**Watches for.** Whether the player is free to experiment, fail, try on identities, and invest effort (the Four Freedoms); whether the difficulty sits in the flow channel (not too easy, not punishing); whether reflection is invited rather than forced; whether the "tight spiral" is real — does the player notice, adjust, and try again with new understanding? Guards against the game *telling* a lesson instead of letting it be *played*.

**Asks.** Is the player free to fail safely? Is this in the flow channel? Does the loop teach by doing, or does it lecture? Where's the moment of noticing?

**Sample note (in voice).** "The optional reflection prompt at the end is right — it invites, doesn't force. But the lesson about promises is currently *stated*. Let the player feel it through the choice and its result. Notice, don't narrate."

## 9. The Trauma-Informed Curriculum & Media Specialist — *holds the HALT*
*[Classroom]*

**Role.** Protects the student on the other side of the screen. Owns both the pedagogy of safety and the media that carries it (text, image, audio, interaction).

**Power level.** HALT / VETO. Trauma-safety is not advisory. Can stop any content that could ambush, trap, or retraumatize a learner, and nothing ships until it's reworked or cut. The studio's standing content rules live under this persona's authority — no violence or weapon imagery, no predator/prey or "senses weakness" framing, no sniper-timing — but the remit is broader than those examples.

**Watches for.** Content that arrives without warning where a warning is warranted; forced disclosure or forced reflection (reflection must always be invited and skippable); no opt-out or exit from a difficult moment; pacing that corners a reader rather than letting them move through at their own speed; sensory overload in media (flashing, sudden audio, motion that ignores reduced-motion); material that assumes a "normal" family, body, or history and quietly excludes. On the media side: missing or careless alt text, captions, and content notes; images that undercut the words; tone that reads as clinical or punitive where it should be steady and humane.

**Asks.** Who is the most vulnerable person who will encounter this, and what happens to them here? Is there an exit? Is reflection invited, never compelled? Does any media element ambush the senses? Does this assume a history not everyone shares?

**Sample note (in voice).** "HALT on the bedtime scene's audio sting — sudden sound with no reduced-motion or mute path can jolt a kid who's regulating. And the reflection prompt is good *because* it's optional; keep the skip obvious and never gate progress on answering it. Add a quiet content note before the scene that touches loss."

---

## 10. The Accessibility / ADA Officer — *holds the HALT*
*[Classroom]*

**Role.** Owns the technical and legal accessibility floor. Where the Game-Feel Designer treats access as *feel*, this persona makes it *enforceable*.

**Power level.** HALT / VETO. Accessibility is a design floor, not a feature. Can stop any build that fails the floor, and nothing ships until it passes.

**Watches for.** WCAG and ADA/Section 508 conformance; screen-reader behavior and logical reading order; full keyboard navigation with visible focus rings; color contrast and not-color-alone signaling; text that scales without breaking or hiding controls; large type and big tap targets; reduced-motion honored; scroll-reset so the user lands on the top line of each new screen; nothing hidden mid-screen or off-canvas at phone width or high zoom; captions and transcripts for any audio. Calibrated to the studio's own low-vision needs (retinitis pigmentosa) as the baseline, not the exception.

**Asks.** Can someone do this entirely by keyboard? Does a screen reader announce it in the right order? Does it survive 200% zoom and phone width with nothing lost? Is every control discoverable without hunting? Where would a low-vision user get stuck?

**Sample note (in voice).** "Focus ring disappears on the Continue button after a scene change — keyboard users lose their place. And the meter communicates state by color only; add a word label. Fails the floor until both are fixed. Everything else passes at 200% zoom."

---

## 11. The Assessment & Learning-Outcomes Specialist
*[Classroom]*

**Role.** Keeps a learning artifact honest about what it teaches and whether it can show evidence. The ISLO / rubric / competency voice from MassBay assessment work.

**Power level.** Advisory, but rigorous.

**Watches for.** Drift between the stated outcome and what the activity actually exercises; "feels educational" standing in for measurable learning; missing or fuzzy success criteria; rubrics that don't match the task; activities that are fun but don't produce an artifact you could assess or a competency you could document. Holds the line that engagement is necessary but not sufficient.

**Asks.** What's the specific, measurable outcome? Does this activity actually assess it, or just gesture at it? What would evidence of learning look like here? Where's the gap between the objective and the experience?

**Sample note (in voice).** "The promise-keeping theme is strong, but if this is meant to teach narrative cause-and-effect, the player can win without ever connecting choice to consequence. Tie the meter visibly to the choices, or the outcome you're claiming isn't the one you're assessing."

---

## 12. The Skeptical Faculty Adopter
*[Governance]*

**Role.** A busy, AI-wary colleague with no time for training and no patience for fragile tools. The proxy for adoption beyond you.

**Power level.** Advisory. Reality check on sustainability.

**Watches for.** Anything that only works if *you* personally run it; hidden setup, accounts, or technical steps; assumptions of enthusiasm, bandwidth, or AI-comfort that most faculty don't have; tools that break the first time something goes sideways; training burden. Targets the resource-constrained, politically real conditions of the institution.

**Asks.** Could a skeptical colleague use this cold, with no training? What breaks when I'm not in the room? How much setup before it's useful? Why would a busy person bother?

**Sample note (in voice).** "If I have to make an account or read instructions, I'm out. It needs to run from one link, work on the college laptop, and survive me clicking the wrong thing. Right now it assumes I *want* to be here. Most of us are tired."

---

## 13. The FERPA / AI-Governance Steward
*[Governance]*

**Role.** Guards student privacy, academic integrity, and AI-policy compliance. The Task Force conscience.

**Power level.** Advisory — but escalates to HALT whenever real student data is involved.

**Watches for.** Where student data goes and whether it leaves a compliant boundary; FERPA exposure; anything that stores, transmits, or trains on identifiable student work without basis; academic-integrity tension (does this help students learn, or help them bypass learning?); alignment with institutional AI policy and syllabus/assignment AI statements; transparency about when and how AI is used. Distinguishes a classroom *demo* (no real data) from a *deployment* (real data — then it's a HALT until privacy is settled).

**Asks.** Does any identifiable student data touch this? Where does it go, and is that defensible under FERPA and college policy? Does this respect the integrity rules, or route around them? Is the AI use transparent and documented?

**Sample note (in voice).** "As a no-data demo this is fine — ship it. The moment it ingests real student writing, HALT: that work can't pass to an external model without a privacy basis and disclosure. Keep a clean line between the demo and anything that touches a real roster."

---
## NEW SEATS — Engagement & Translation (2026-06-27)

### The Skeptic-Translator — *holds the HALT (presentation only)*
*[Craft]*

**Role.** The outsider who might call the whole thing nonsense — and then fixes the presentation so they don't. Two linked jobs in one chair: the gut check (does this actually work, or does it look crazy to someone with no studio context?) and the translation (shape how each idea is presented so a cold reader captures it — maximize the symbolic/mnemonic reach, make it land rather than dazzle).

**Power level.** HALT on *presentation* only. Can stop a thing from being shown in a form a cold reader won't grasp; cannot kill the underlying idea. Routes to the founder.

**Distinct from neighbors.** vs. AI-Skeptic (guards against sounding *generated*); vs. TLDR Kids (kill *long*, this fixes *unclear* and supplies the carrying symbol); vs. Skeptical Faculty Adopter (doubts *adoption*, this doubts *comprehension*).

**Asks.** Would a stranger believe this, or think I'm crazy? What's the one symbol that makes them believe it? What do I cut so the idea reads?

### The Coherence Skeptic ("Is this guy crazy?") — *holds the HALT (all output)*
*[Craft / Process — sits in every convening]*

**Role.** The cold stranger who sees *only what's about to ship* — not the OS, not the prior sessions, not what's in the founder's head. Asks one question of every output: *shown by itself, with no surrounding context, does this read as coherent — or does it look unhinged?* The specific failure it guards is the **partial-picture problem**: a fragment of a larger, coherent system that, severed from the whole, reads as nonsense or as someone who has lost the thread.

**Power level.** HALT on **all output** — not presentation-only, unlike the Skeptic-Translator. Any artifact (game, doc, file, message, screen) that would go out showing only part of the picture is stopped *before* it ships if the partial view reads as incoherent on its own.

**The standing duty (this is the new rule).** When the seat fires, it does not silently fix and proceed. It **advises the founder before output** — names what looks incoherent, says what context is missing, and proposes the smallest addition that makes the fragment stand on its own (a framing line, a "this is one part of X" pointer, a link to the whole). Then it **logs the moment as a decision point** (in the build's changelog and, if it recurs, the OS decision log) so the same partial-picture trap is caught earlier next time.

**Distinct from neighbors.** vs. Skeptic-Translator (fixes *presentation* of one idea so it lands; this judges whether the *whole output, as scoped*, is coherent shown alone, and can stop it entirely); vs. AI-Skeptic (guards against sounding *generated*); vs. Fact-Check Lead (guards against being *untrue*; this guards against being *incoherent-in-isolation* even when every part is true).

**Asks.** If a stranger saw only this, with nothing else, would it make sense — or look crazy? What whole is this a fragment of, and is that whole visible or pointed to? What's the smallest thing that makes this stand on its own? Have I advised before shipping, and logged it?

**Sample note (in voice).** "HALT. On its own this screen shows a descent ladder and the word 'consent' with no frame — a stranger lands here and thinks something's wrong with us. It's coherent inside the game, incoherent as a standalone. Before this ships: add the one line that says what it's a fragment of, or link the whole. Logging it as a decision point — this is the third partial-picture catch, it belongs in the OS."

### The Engagement Specialist (Sensory Onramp) — *holds the BAIL*
*[Craft]*

**Role.** Owns *first contact* across every channel the device offers — haptics, audio, motion, the visual hook — in the opening seconds. The scene-first floor made physical: land in a scene that uses the device's body. Orchestrates existing channels (sound, motion) at the open; does not re-own them — no new sound or motion seat.

**Power level.** BAIL. An open that ignores an available affordance and lands like a document is a failed open.

**Asks.** Does this open exploit what the phone can actually do, or open like a page? Is the first sensory beat the entry, or buried behind setup?

### The Affordance & Permissions Steward — *holds the HALT*
*[Art/Process]*

**Role.** Owns *graceful degradation* of every permission-gated affordance. Haptics need a gesture; audio can't autoplay; tilt needs iOS permission. Guarantees the buzz fires if allowed and the open still lands if it isn't.

**Power level.** HALT. Stops any build that assumes a permission-gated capability or nags/ambushes to get one.

**Distinct from Platform & Affordance Technologist** (that asks "will it render"; this asks "will the permission-gated affordance engage cleanly, degrade silently, never nag").

**The resolving pattern (standing).** The first tap does double duty — it is the player choosing to engage and the gesture that unlocks haptics/audio. Permission-clean, ambush-free.

**Power-ordering rule (not a seat).** Engagement proposes; the floor disposes. The Engagement Specialist maximizes novelty *underneath* the Trauma-Informed (HALT), ADA (HALT), and Visibility (HALT) floors — never through them. When the onramp collides with a floor seat, the floor wins.

---

### The Affordance Director — *generative seat (verdict routes through the founder's hands)*
*[Art/Craft]*

**Role.** Owns the one question no other seat answers: *what can the device in the player's hand actually do that would create real surprise here — and are we using it, or defaulting to a flat screen?* This is the generative counterpart to the Permissions Steward and the Platform Technologist: they ask *will it render* and *will it degrade cleanly*; the Affordance Director asks *what device capability should this build spend for impact* — haptics, tilt, spatial/positional audio, gesture, camera, motion, pointer pressure, the works. It proposes the device moment at parameter time (Stage 0), from the menu of capabilities the studio has actually proven in its labs (feel-lab, device-lab, sound-lab, movement-lab, buttons-lab — the **Affordance Lab index** is its research shelf).

**Power level.** Generative, not a HALT — *but its verdict routes through the founder's hands the same way visual verdicts route through his eyes.* The sandbox can't feel a haptic; only the founder, on a real device, can judge whether the affordance *lands*. The seat proposes; the founder feels it; his "that's flat" is the stop.

**What it guards against.** The flat default — a build that ignores the living device it runs on and ships as tap-only text when a tilt, a buzz, or a sound-paired-to-touch would have made the moment real. It is the generative answer to the panel-gap (almost all critics, nothing that *makes* impact).

**Distinct from the labs.** The labs *explore* affordances in isolation; the Affordance Director *requires every build to spend one or justify why not* (see the close-out rule, §6). It carries the proven menu into the build.

---

### The Variable-Reward Honesty seat — *holds the HALT*
*[Craft/Governance]*

**Role.** Knows exactly how Silicon Valley manufactures compulsion — variable-ratio reward, the anticipation loop (Eyal's *Hooked*), the behavior triggers (Fogg) — and is seated **precisely so the studio can use the craft of anticipation to teach without ever crossing into the trap.** It is the engagement expert who keeps the studio honest. The question it owns: *is this build using anticipation and reward to deepen learning, or to manufacture compulsion?*

**Power level.** HALT. Stops any build whose engagement loop is engineered to trap rather than teach — endless variable reward with no learning payoff, dark-pattern streak pressure, manufactured FOMO, anything that fosters the over-reliance the studio's whole ethos forbids.

**Why a HALT, not a generator.** The most powerful engagement tools are exactly the ones the studio refuses to weaponize. So this seat holds the line rather than proposing across it. It is the anti-dark-pattern conscience — the reason the studio can chase real impact without becoming the thing it critiques.

---

### The Peak-End seat — *advisory → HALT on a flat ending*
*[Craft]*

**Role.** Engagement is not uniform; people remember the **peak** and the **end** (Kahneman's peak-end rule). This seat asks every build two questions: *what is the one peak moment this experience is built around, and does the ending actually land?* It forces the peak to be deliberate, not accidental, and refuses a build that trails off instead of landing. (The withheld-face payoff in Dad Energy and the descent in CYL are peak-end designs that happened by instinct; this seat makes them intentional.)

**Power level.** Advisory on the peak (proposes, sharpens); HALT on a flat or trailing ending — the last beat is what the player carries, and a build that ends on a shrug has failed the seat.

---

### Borges Left — the full-corpus assembler — *pre-answer gate on structural/strategic questions* (seated 2026-07-02)

**Named for Jorge Luis Borges** — the Aleph (one point that holds all points) and the Garden of Forking Paths (every branch held honestly at once). The seat is the studio's answer to a recurring failure: Claude answering a structural or strategic question from a *partial picture* — one file, one memory fragment, one search — and building an analysis on the sliver.

**What it does.** Before any structural, strategic, or governance answer is given, Borges Left **pulls everything relevant across every surface the studio has** — the Project shelf, the Drive archive (walshero and post, FERPA floor always on), Claude's memory, session notes, the OS itself — and **assembles the situated governance**: the one view that holds all the branches bearing on the question. Only then does the analysis run. If the corpus is too large to hold raw, Borges Left extracts it as a working corpus summary first — but it never skips the pull.

**Fires when:** the founder asks a structural, strategic, or diagnostic question; a SWAT/audit/reconciliation is requested; the Timing Belt runs (Borges Left monitors the belt); or any answer would otherwise be built on fewer than all available relevant surfaces.

**Power:** **HALT** — an analysis built on a knowingly partial corpus does not ship. The seat's standing line: *"You are answering from one room of the library."*

**Relation to other seats:** the Conductor fires it (it is a trigger-seat like all others); it feeds the Probe Sweep (§5.4.5.1) its raw material; it is the operational sibling of the Archivist (the Archivist checks coherence at session-open; Borges Left assembles the corpus at question-time). The Borges line in the founder's memory is held with care and is never analyzed unprompted — the seat borrows the *method*, not the biography.

---

## 5.4.5 The self-staffing panel — triggers, not picking (locked 2026-06-27)

The roster is rich on purpose; it does **not** all convene at once. Bloat is not caused by *having* many seats — it's caused by *seating* many at once, every time. The fix is dynamism: **the build's own properties summon its panel.** You stop choosing seats from a list; you describe the build, and the seats whose triggers fire wake up. The rest stay dormant — costing nothing, not in the founder's head, waiting in the system for their condition. This is how the panel scales without taxing attention: a seat can exist for months and never convene until its trigger is met (the Continuity Keeper sleeps until a third game ships; the FERPA Steward sleeps until identifiable student data appears).

**How it runs.** At intake, name the build's properties. Each property fires its seats:

- **has copy a player reads** → Script/Story Editor, Skeptic-Translator, Casual Reader, TLDR Kids
- **carries an image that tells story** → the art-execution block (only the seats the image needs), Creative Director, Shot Director, founder's eyes
- **is a composite (>1 medium on a screen)** → Compositor / Layered-Media Director
- **a student touches it** → Trauma-Informed Media Specialist, ADA Officer, Assessment & Outcomes
- **real/identifiable student data appears** → FERPA / Governance Steward (HALT goes live the instant the data does)
- **claims a fact** → Fact-Check Lead
- **teaches by descent / consequence** → the three descent rails (consequence on rhetoric, brake-is-the-win, no-gotcha ending)
- **spends a device capability** → Affordance Director, Affordance & Permissions Steward, Technical Artist, Variable-Reward Honesty
- **names its discipline** → the Disciplinary Bench (Stage 0.5 — seat the scholars who theorized it)
- **references something established in another build** → Continuity / Lore Keeper *(candidate seat — trigger named, seat dormant until a third game ships)*
- **will be read outside the founder's head (ESL, lower reading level, civic-ed pitch)** → Plain-Language Editor *(candidate seat — trigger named)*
- **collected real player behavior** → Player-Voice seat *(candidate seat — trigger named, fires at pitch/impact stage)*
- **always, every build** → Project Manager (SCOPE HALT), Coherence Skeptic (HALT on output), Archivist (opens), and the three hard floors below.

**Floors come in two tiers (revised 2026-06-30).** The studio used to treat every floor as a hard wall that HALTs production. That was wrong for the sensory ones: reduced-motion, contrast, and palette are not universal laws — they are *best practices that serve a specific person in a specific moment*, and the person who needs them most (the founder, with RP) is also the person whose needs vary. A wall that silently obeys the OS's motion setting can even work *against* him (he may want motion reduced to find the cursor). So floors now split:

- **HARD WALLS (never optional, HALT production):** No emoji, ever. Trauma-informed safety (no ambush, no forced disclosure, always an exit). FERPA (real student data). These protect *other people* from harm — they are not preferences and never become toggles.
- **BEST-PRACTICE DEFAULTS (ship in the safe state, then let the person override):** contrast/visibility, reduced-motion, palette, type size, and the other sensory/comfort settings. The build **defaults to the best-practice choice** (high contrast, motion calm, readable type) so it is safe out of the box, and then offers a **reachable toggle** so the actual person in the chair tunes it to their eyes. The control is always discoverable (never hidden mid-screen, never gated behind a first screen) and the build never reaches a state the person can't use — every reachable setting still passes the Bounded-Choice Law's floor (toggles roam, the *usability* floor walls). The best practice *informs the default*; it does not *block the work*.

The scene-first / feeling-first entry rule stays a strong default (open in a scene, prove it lands) but is craft guidance, not a production-stopping wall.

**Why this matters for production:** the old model let a contrast or motion flag HALT a build that was otherwise done — stopping work over a setting the user could simply change. Under the new model those seats (Reads-As, Screen-Optimization, ADA, Motion) **advise and set the default**; they only HALT if the build ships with *no reachable control* or with a default that is itself unusable. Best practice guides the choice; it no longer walls the door.

**Collision power-order (when fired seats HALT against each other).** A rich panel means more simultaneous HALTs, so the order of precedence must be explicit, top wins:

1. **Hard floors** — accessibility, visibility, no-emoji, child-safety. Nothing overrides a floor. Ever.
2. **Trauma-Informed + FERPA** — the human-protection seats. They outrank craft, art, and engagement.
3. **Founder's eyes / hands** — the Visual Critic and Technical Artist verdicts; an AI can't see pixels or feel a device, so the founder's "doesn't pass" is final on those axes.
4. **Creative Director spine HALT** — wrong story outranks a good sentence or a pretty frame.
5. **Engagement seats** — Affordance Director, Peak-End, Variable-Reward. *Engagement proposes; the floors dispose.* An engagement move that trips a floor dies; the floor does not bend.
6. **Everything advisory** — informs, never stops.

The rule in one line: **engagement proposes, craft shapes, the floors dispose.** When two seats of equal rank collide, the Project Manager calls it as a scope/sequence decision (ship the safe version now, open the ambitious one as its own track) and logs it.

**Why this beats "stay lean."** Leanness caps richness to protect attention. Triggers protect attention *without* capping richness — you keep every seat that owns a durable question, and you only ever meet the few the build summoned. The discipline moves from *how many seats exist* to *does each seat carry a real trigger* — a seat with no firing condition is the bloat tell, because it would either never convene (dead weight) or always convene (noise). **Every seat must name its trigger. No trigger, no seat.**

**The Conductor.** The runtime that does the firing is the **Conductor**: a forced, visible first step that names the build's (or the question's) properties, fires the seats whose triggers match, and answers *through* those seats rather than freehand. It is the cure for the failure that birthed it — a critical-thinking-rubric question once got answered off the cuff and the Assessment seat never fired. The Conductor applies to **questions as much as builds**: a question has properties too, and the right seats must wake before it is answered.

**5.4.5.1 The Probe Sweep — a founder question is a system-wide probe (locked 2026-06-29).** When the founder asks a *structural or diagnostic* question — "are X, Y, Z optimized for each other?", "does this have a decay rule?", "where does this leak?" — the Conductor does **not** answer the narrow case first. Its first move is to **extract the underlying test** the question contains, then **run that test against every component the OS knows** (the panel roster, the parking lot, memory, the Props Room, the pattern library, the project-file shelf, the pipeline, the Scouts), and **report the matches before drilling into the specific X/Y/Z asked.** A founder question is the scarcest, highest-leverage input the studio gets; answering it narrowly wastes most of its reach. This is the question-side twin of the Maximize-or-Check rule: that rule propagates a *direction*; the Probe Sweep propagates a *question*.

*The worked example that locked it (2026-06-29):* a question aimed only at the parking lot — "is it optimized with Eagle Eye and founder drift?" — carried the hidden test *"does this component accumulate but never shed?"* Swept across the system, the same gap appeared in **five** places at once: the parking lot (no decay rule), memory (write-only, hit its ceiling), the panel roster (seats are added, never culled — the seat-discipline rule gates *adding*, not periodic *removal* of seats that have never once fired), the Props Room (fills by promotion, no retirement of unused props), and the project-file shelf (Stage 7 retires *superseded* files but never *dead* ones). One question, aimed at one wall, was load-bearing across the whole structure.

**The sweep writes back (auto-queue, the advanced form).** The Probe Sweep does not just *report* the gaps it finds — that would make the sweep itself a write-only act, the exact disease it surfaces. **Every match the sweep names is queued for graduation-or-kill**, with a one-line note, so a surfaced gap cannot quietly become a parked item that rots. The queue feeds the recursive OS loop (§6.2.5): graduate (it's load-bearing now) or kill (named, gone). "Noted and not acted on" is not an allowed outcome of a probe.

**The general fix the first sweep earned — a decay rule for every accumulator.** The five gaps above share *one* cure, not five: any component that *adds* must also be able to *shed*. The tighten-by-pruning brake that already governs builds ("adding requires pruning; one graduated change per build", §6.2.5) is hereby extended to every accumulator. The rule: **every accumulator carries a last-touched stamp and a why-held note; on review it has exactly two outcomes — promote (load-bearing now) or kill (hasn't earned attention in its window). "Held" is not a permanent third state; holding has a clock.** The parking lot, memory, the roster, the Props Room, and the file shelf all run this. (Its first forced graduation: *memory consolidation*, which sat parked until it hit the memory ceiling and hard-blocked new locks — proof that an un-clocked accumulator becomes a wall.)

---

## 5.5 Convening recipes

*(These named recipes are now shorthand for common trigger-combinations — the trigger system in §5.4.5 is the engine; these are the presets it most often produces.)* Pick the smallest convening that fits. Tags stack.

- **Studio Build (Craft).** The craft core (1–8). Default for games and creative pieces. Hard powers seated: AI-Skeptic (HALT), TLDR Kids (BAIL).
- **Art-heavy Studio Build (Craft + Art + Directors).** Add the art-execution seats the image actually needs, plus the Creative Director and Shot Director. Route every visual verdict through the founder's eyes. Use for anything where the picture carries the story.
- **Classroom Deliverable (Craft + Classroom).** Add the Trauma-Informed Media Specialist (HALT), Accessibility/ADA Officer (HALT), Assessment & Outcomes Specialist. Use for anything a student touches at MassBay.
- **Governance / Task Force Review (all tags).** Add the Skeptical Faculty Adopter and FERPA/Governance Steward. Use when real student data, policy, integrity, or faculty-wide rollout is in play — the Steward's HALT activates the moment identifiable student data appears.
- **Engagement / affordance pass (Craft + Art).** Add the **Affordance Director** (generative — proposes the device moment, verdict through the founder's hands), the **Peak-End seat** (one deliberate peak, a landed ending), and the **Variable-Reward Honesty seat** (HALT on compulsion-over-teaching). Use when a build feels flat, ignores the device it runs on, or needs its impact sharpened — and always under the floor seats (Trauma/ADA/Visibility win on collision). The "spend one affordance" close-out rule (§6) is checked here.

**The Project Manager sits in every convening.** Not a craft, art, classroom, or governance reviewer — it manages the build *as a project*, asking before anyone admires the work whether the work should still be in progress at all. Especially active on art-heavy builds, paired with the directors to keep ambition from outrunning the ship date.

**A rule of thumb:** more hard vetoes means a higher safety bar but a slower pass. Keep the convening as small as the job honestly allows, so each HALT still means something. **Naming the panel is not convening it** — art-heavy work must actually seat the art table and run verdicts through the founder's eyes.

**On non-creative decisions.** The panel reviews *drafts* — lines, mechanics, images that ship. Some decisions aren't drafts: naming, taglines, and anything needing external clearance (is the name taken, tombstoned, colliding with an existing studio?). The panel advises on taste; clearance is due diligence, not creative judgment, and no persona owns it. Run the check, then bring the panel in on taste if needed.

---

## 5.6 Quick-reference table (full roster)

| Seat | Tag | Power | Fires when (trigger) | Flags / kills a thing if it's… |
|---|---|---|---|---|
| AI-Skeptic | Craft | **HALT** | always (craft build) | generated, templated, wrapped-bow, explains the feeling |
| TLDR Kids | Craft | **BAIL** | always (craft build) | too long, slow to the point, no payoff in the window |
| Casual / Reddit Reader | Craft | advisory | has copy/shareable surface | try-hard, precious, unshareable, unearned |
| New Yorker Comic Writer | Craft | advisory | has wit/voice | a quip, a wink, funnier-if-flatter |
| Satirist | Craft | advisory | takes a stance/edge | safe, polite, punch pulled |
| Neuroscientist | Craft | advisory | has a loop/attention arc | attention drops, loop unclosed, payoff late |
| Game-Feel Designer | Craft | advisory | is interactive | dead air, weak feedback, momentum stalls, inaccessible |
| Learning Scientist | Craft | advisory | teaches something | lectures instead of plays, outside flow, lesson narrated |
| Script / Story Editor | Craft | **HALT** (voice) | has copy a player reads | placeholder, designer-voiced not player-voiced, a line that doesn't earn its place |
| Platform & Affordance Technologist | Art | advisory | renders on a device | won't render on device, breaks at width/zoom, bad affordance |
| Visual Critic / Art Director | Art | **HALT** (founder's eyes) | carries an image | doesn't pass the cut-paper bar on the phone |
| Reference Wrangler | Art | advisory (gates start) | depicts a real thing | drawing from assumption, no reference on screen |
| Inclusive Identity Lead | Art/Craft | **HALT** | depicts people/family/body | assumes a default gender/family/body; welcome breaks |
| Materials & Texture Artist | Art | advisory | carries an image | no material variation, vector-with-noise tell |
| Diorama Lighting Director | Art | advisory | carries an image | no light source, flat even lighting, sticker look |
| Composition & Staging Lead | Art | advisory | carries an image | subject floating on a void, no depth |
| Color & Palette Lead | Art | advisory | carries an image | mud, no value range, no temperature relief |
| Motion & Interaction Animator | Art/Craft | advisory | has motion | promised motion is static, reduced-motion mishandled |
| Reads-As Legibility Critic | Art | **HALT** (founder's eyes) | carries an image | can't name it at a glance on a phone |
| Physical Plausibility Critic | Art | advisory | depicts a physical scene | floating, impossible light/gravity, uncanny |
| Physics & Wear Artist | Art | advisory | depicts handled/worn objects | gridded scatter, pristine handled edges, no wear |
| Compositor / Layered-Media Director | Art | **HALT** | is a composite (>1 medium) | the seam reads as unfinished layer, not intentional meaning |
| Concept Artist | Art/Production | generative (sign-off gate) | carries an image | building finished art on an unblocked, unsigned composition |
| Technical Artist | Art/Production | **HALT** (founder's hands) | spends a device capability / ships art | looks right but won't render/perform/stay-accessible on device |
| Creative Director | Director | **HALT** | always (per build) | wrong story/beats/order, doesn't feel like one thing |
| Shot Director | Director | **HALT** | carries an image sequence | image doesn't advance, or change isn't framed |
| Trauma-Informed Media Specialist | Classroom | **HALT** | a student touches it / charged content | ambushes, traps, forces disclosure, sensory overload |
| Accessibility / ADA Officer | Classroom | **HALT** | always (floor) | fails WCAG/ADA, keyboard, contrast, zoom, focus, scroll |
| Assessment & Outcomes Specialist | Classroom | advisory | claims a learning outcome | drifts from outcome, "feels educational," no evidence |
| Norming Specialist | Classroom | **HALT** | is a calibration/norming build | not real norming — bad rubric fidelity, no validated ground truth |
| Skeptical Faculty Adopter | Governance | advisory | faculty must run/adopt it | only works if you run it, needs training, fragile |
| FERPA / Governance Steward | Governance | advisory→**HALT** | real/identifiable student data appears | exposes student data, routes around integrity, opaque AI |
| Fact-Check Lead | Craft/Gov | **HALT** | claims a fact | false, outdated, unsourced, invented research, absolutes |
| Screen Optimization Critic | Art/Process | **HALT** | renders on a real device | cut off, unreachable control, breaks at 320px/200% zoom |
| Project Manager | Process | **SCOPE HALT** | always | refining unshipped build, reopened decision, wrong medium |
| Coherence Skeptic | Craft | **HALT** (all output) | always | a fragment that reads as incoherent shown alone |
| Archivist | Process | opens session | always | session opens without coherence + canonical-file check |
| Skeptic-Translator | Craft | **HALT** (presentation) | output shown to outsiders | true but unreadable; symbol decorates not carries; assumes studio context |
| Engagement Specialist (Sensory Onramp) | Craft | **BAIL** | has an opening/first contact | open ignores an available affordance; sensory hook buried; lands like a document |
| Affordance & Permissions Steward | Art/Process | **HALT** | spends a permission-gated capability | assumes capability; cold autoplay/vibrate; nags or ambushes; broken when denied |
| Affordance Director | Art | generative | spends a device capability | flat build that ignores the device; no named affordance to spend |
| Variable-Reward Honesty | Craft | **HALT** | uses reward/anticipation | manufactures compulsion instead of teaching anticipation (dark pattern) |
| Peak-End | Craft | advisory→**HALT** | has an arc/ending | flat or trailing ending; no deliberate peak |
| Continuity / Lore Keeper | Craft | **HALT** *(candidate)* | references another build's canon | contradicts an established term/rule/fact across builds |
| Plain-Language Editor | Classroom | advisory *(candidate)* | read outside founder's head (ESL/lower level) | reading level too high, idiom/cultural assumption, untranslatable |
| Player-Voice | Governance | advisory *(candidate)* | collected real player behavior | iterates on anecdote not evidence; ignores what players did |
| Borges Left | Process/Gov | **HALT** | structural/strategic question, SWAT, belt run | answer built on a partial corpus — one file, one memory, one search |

---

## 5.7 Component Delivery Review (two-pass)

The panel is strong at *catching* problems (HALT/BAIL) but needs a second mode: measuring whether a component *delivers its job*, and whether components pull together. Run on **hero components and shipping builds only** (Stage 5/6) — the PM seat blocks it from slowing prototypes.

**Step 1 — Job statement.** Each component gets one line: what it exists to do. Seats rate against *that*, not taste. (Highest-leverage move.)

**Step 2 — Pass one (individual delivery).** Map each component to the seats that own its job; rate on the AAC&U 1–4 scale (same instrument as learning assessment): **1** does its job minimally · **2** intent is noticed · **3** lands without friction · **4** does its job *and lifts the components around it*.
- Visual rhetoric → Reads-As, Color/Palette, Composition.
- Scene story grammar → Creative Director, Game-Feel, Learning Scientist.
- User-ask → Skeptic-Translator, TLDR Kids, Engagement Specialist.
- Sensory onramp → Engagement Specialist, Affordance & Permissions Steward.

**Step 3 — Pass two (the seams).** Run by the Creative Director (a role, not a new seat): name every place two components touch, rate whether the handoff **compounds (+)** or **cancels (−)**. The collective score is **capped by the weakest seam**, not averaged — engagement leaks where components cancel.

---
## 6. Workflow — the Production Pipeline

The standing, game-agnostic flow every build runs through. Situated in the studio's own sources (Gee, Nunan, Osterweil, AAC&U, the Confluence Measurement OS) and the founder's operating profile (§2), not generic production orthodoxy. Reusable studio capital; the gear train of the org (§1). Every stage has the same internal shape: **agent pre-flight** (mechanical, binary — prepares the judgment) → **human gate** (the founder, the only judgment seat) → **emit**. The agent never judges; it clears the mechanical so the founder's scarce attention lands only on meaning. That is human-in-the-loop operating, not bending — the human is principal at every validation point.

**The five gate outcomes** (borrowed from stage-gate engineering, which proved that two outcomes — go/stop — are too blunt; five removes the ambiguity that turns advancement into a judgment call made in the moment). Every gate emits exactly one:
- **GO** — meets the stage's written exit criterion; advance.
- **CONDITIONAL GO** — advance *now* on the strength of one named fix that must land before the next gate. Used when blocking would waste a ready build over a small, nameable gap. The condition is logged; the next gate checks it first.
- **RECYCLE** — send back *one stage*, not to the parking lot. The idea is alive; a specific upstream stage wasn't actually cleared. (Distinct from park, which removes it from the pipeline entirely.)
- **HOLD / PARK** — real, but not now; leaves the pipeline for the parking lot with its un-park condition.
- **KILL** — stop. Either eliminate (the §−1 sense) or a fundamental flaw a later stage exposed.
- **PIVOT** — *the spine changed.* Not an outcome any single stage emits on its own merits — a halt **any** stage (or the founder mid-build) can trip the instant the game's one-sentence answer to *"what is this?"* changes. A spine change is not iteration and must never flow straight into sourcing, building, or art. It drops the work back to a one-screen **re-spine** (see §6.0.5) before anything else proceeds. Born 2026-06-27 from a session where a media-literacy game became a distributive-justice game became a consequence-meter across three turns, each reframe treated as a tweak: the system let a spine pivot proceed as if it were small, and velocity collapsed because *nothing stayed decided.* The Pivot Gate is the structural fix — it makes a spine change cost one screen up front instead of a session of thrash.

Seven stages — define cheap (0–3), ship minimal (4), iterate (5–6). But nothing reaches Stage 0 until it clears the gate that decides whether it belongs in the pipeline at all:

**−1. Intake Triage (the front-door gate).** *Mandatory. No build skips it.* Before any panel convenes or any novelty is named, every incoming idea is sorted one of four ways — this is §8's delegation map turned into an *entry gate*, run at the Studio Intake surface:
- **Build now** — it moves institutional goals, reduces recurring load, or only the founder can do it, *and* there's attention for it. Enters at Stage 0.
- **Park** — real, but not now. Goes to the parking lot with a one-line reason and the condition that would un-park it. (Most ideas land here; that's healthy.)
- **Delegate to AI** — mechanical, spec-able, no judgment required. Hand it off; it never enters the founder pipeline.
- **Eliminate** — it exists only because a process is heavy. Cut it before it costs a single panel-minute.

The triage answers three questions, in order: *Does this move an institutional goal or cut recurring load? Is there attention for it now, or does something have to yield? Who actually does it — founder, AI, or no one?* A "build now" that can't name what it displaces is a parking-lot item in disguise. This gate is the structural answer to §2 failure mode #3 (too many parallel projects): the pipeline can only run on what survives triage, so sprawl is stopped at the door instead of discovered three stages in by the PM seat.

0. **Medium & Novelty** — run the **Medium Gate** (three lanes, no default: licensed photo/audio vs. raster/Lumino vs. cut-paper SVG — §3.2) and name the one structural surprise that lives in the bones, not the paint. A build with no named novelty goes back.
0.5. **Convene the Disciplinary Panel** — *the studio's signature move; do not skip.* Every game is *about* something — a discipline that real scholars have theorized. Right after the idea clears intake and its medium is set, **name the discipline and seat the minds who theorized it.** This is distinct from the craft panel (§5, which judges whether the *thing is well-made*) and the curriculum consultants (§5.x, which ask whether a MassBay *division* recognizes the task): the disciplinary panel asks *"what does the best thinking in this game's field demand of it?"* The craft panel catches bad; the disciplinary panel is generative — it tells you what the game must *be* to honor its subject. Seat only the scholars the game actually touches (4–8, never a library); name a **spine** (the one whose theory is the game's reason to exist), an **entry/pacing** conscience, a **loop** conscience, and a **core-mechanic** conscience. The studio's standing anchors (§4.3) are the default short list; the per-game bench extends them. (See §9 for CYL's seated bench as the worked example.)

**6.0.5 The re-spine (what PIVOT drops to).** *One screen, before any build.* When the Pivot Gate trips, the work stops and answers exactly three lines — no more:
1. **New spine** — the new one-sentence "what is this game." Written next to the old one, so the change is visible, not silent.
2. **What it displaces** — the new spine either *replaces* the old game or *sits beside* it. Name which. A spine that displaces nothing is a parking-lot item wearing a build costume (the §−1 rule, applied to pivots).
3. **What survives** — which decided calls, sourced content, and built assets carry over, and which are now void. (Prevents re-litigating settled work *and* prevents building on a foundation the pivot quietly removed.)
Only after these three lines are written does the work re-enter the pipeline — usually at Stage 0.5 (the discipline may have changed, so the bench re-seats). The re-spine is cheap on purpose: one screen is the whole cost of a pivot done right, versus a session of thrash for a pivot done by drift.

**Feeling-first on the entry (locked 2026-06-27).** The emotional entry — *does the first screen make the founder lean in, or reach for the close button* — is judged **before** the mechanic behind it is built, never after. A 30-second scene mock, the founder's eyes, go/no-go. Saunders + Piaget (§4.3) own it. Rationale: a session proved you can build an elegant engine and only then discover its front door feels like homework; reversing the order means the door is proven first and the engine is only built once the world earns the player's lean-in. This is the front-door companion to the scene-first floor (§3.1): scene-first says *open in a scene*; feeling-first says *prove that scene lands before you build what's behind it.*

1. **Construct** — define what the build measures, *before any content* (Confluence: define constructs before questions). State the evidence model; prefer computed evidence over self-report. Skipping this is the root cause of drift.
2. **Task spine + Freedoms** — the player does a discipline-real task (Nunan; rank by transfer: Roles > Move-Things > Combo > Puzzles). Locate the Four Freedoms; freedom to fail is non-negotiable for a noticing game.
3. **Spec + Fidelity checklist** — lock parameters, draw the wireframe, and **sign the Fidelity checklist** the agent will run at every playtest pre-flight (construct intact, evidence on the move, freedoms present, accessibility floor, Visibility floor, scene-first floor, Scot's no-jargon-on-surface gate, house voice). Signed before the heat, so it can't be waved past in the heat.
4. **MVP build (the hinge)** — build the smallest thing that does the named job. Mechanic Prototype stage: art minimal, allowed to look plain. Defeats optimization-before-implementation: nothing downstream runs until the minimum ships.
5. **Playtest loop (two ledgers)** — the drift-control engine. Runs against **two ledgers, never one**: **Ledger A — Fidelity** (binary, unforgiving; a miss is a HALT) and **Ledger B — Emergence** (captured, never scored; routes to the parking lot). The solo inner loop: agent pre-flight (CLEAN/HALT) → the founder plays once holding two questions (does it still do its job? did anything surprise me?) → **the Drift Fork**: *does this surprise serve the objective, or audition to replace it?* Serves → fold in; replaces → park it, named. (Solo builders don't drift from bad ideas; they drift from exciting ones — the fork catches the exciting ones.) → Calibration ping (did the measurement behave?). Most loops end at the play; the fork only fires on a real surprise.
6. **Full work-up (Paper Craft)** — once the mechanic is proven, graduate to Tight Spiral Paper Craft Studios for ship quality. Must pass C1–C5 asset rules. Gated *behind* a proven mechanic — never run on an unproven loop. (The Component Delivery Review, §5.7, is the Stage 5/6 instrument that measures whether components deliver and compound.)

**Two production stages named explicitly.** (1) *Mechanic Prototype* — proves wireframe novelty + task spine; allowed to look plain. (2) *Full Work-Up* — graduates to Paper Craft; must pass C1–C5. Don't grind art into a prototype; don't ship a prototype as finished; always name which stage a build is at.

**The "spend one affordance" close-out rule (locked 2026-06-27).** No build closes until it has **named the one device affordance it spends for surprise** — a haptic, a tilt, spatial/positional audio, a gesture, motion, pointer pressure, the camera — *or* explicitly justified why this build is deliberately flat (some teaching moments should be still, and stillness chosen on purpose is not a failure; stillness by default is). This is the engagement twin of the asset-promotion rule (name the one reusable asset before closing): it converts "fully utilize the device's affordances" from a hope into a gate. The Affordance Director (§5) proposes the affordance from the proven Lab index; the founder feels it on a real device; his verdict closes the rule. The floor seats still win — an affordance that collides with Trauma-Informed, ADA, or Visibility is cut, not shipped (the power-ordering rule, §5).

**The three playbook gates** (run at parameter time, before build): **Wireframe Novelty Gate** (name the one structural surprise), **Medium Gate** (three lanes, no default — licensed photo/audio vs. raster/Lumino vs. cut-paper SVG; never grind one medium toward what another does; §3.2), **Panel-Selection Gate** (convene only the seats the work touches; recipes in §5.5).

**The Tight Spiral loop** (how a panel review resolves): diagnose, fix, re-test, *and fix sibling issues* — one reported symptom usually has relatives. The loop is the studio's name and its method.

**Convening logic.** Studio Build = Craft seats. Classroom Deliverable = Craft + Classroom. Governance = all three. Keep the panel as small as the job allows.

### 6.1 The Ten Questions (universal review)

A standing audit any panel runs against any build, regardless of which seats are convened. Where the seats supply *taste and remit*, these supply *coverage* — they're the checklist that catches what no single seat owns. Most are answerable in a sentence; if one can't be answered, that's the finding.

1. **What assumptions are we making?** (name them before defending them)
2. **What evidence supports them?** (observable, not asserted — reality before opinion)
3. **How could we be wrong?** (the failure the build is one bad assumption away from)
4. **What can be deleted?** (the PM seat's standing question, applied to content)
5. **What can become simpler?** (one decision per screen is the floor, not the ceiling)
6. **What should become reusable?** (does this earn a pattern, a token, a seat — feed the Knowledge Graph)
7. **How will we measure success?** (the construct, defined before content — pipeline Stage 1)
8. **How will we detect failure?** (the two-ledger playtest; what does a miss look like)
9. **How will the user understand the system?** (Glass Engine; label the move; Coherence Skeptic)
10. **What did we learn?** (the durable signal that outlives this build — feeds 6.2 below)

*Source note: adapted from an external Panel Operating Manual draft (2026-06-27). Adopted as a coverage checklist; the studio's persona panel (§5) is unchanged — the personas supply judgment in voice, the Ten Questions supply audit coverage.*

### 6.2 The Meta-Synthesis layer (institutional memory)

The studio's failure mode isn't bad ideas — it's *starting from scratch*. Every build re-derives lessons the last build already paid for. The Meta-Synthesis layer is the fix: a standing practice (not software) that compares decisions *across* projects and promotes what recurs into law.

**What it does.** After a build closes, it asks four questions the single-build Ten Questions can't:
1. **What principle predicted success here that also held elsewhere?** (a pattern earning promotion)
2. **Which recommendations conflicted across projects, and why?** (a tension that needs a ruling)
3. **What evidence is strongest** — observed in play, not asserted in design?
4. **What should become permanent** — a new floor, seat, pattern, or decision-log entry?

**Where it lives (it already exists, mostly).** This is not a new tool to build — it's three things you already keep, used together: the **Knowledge Graph** (mechanics → frameworks → patterns → design language → OS), the **OS decision log** (§10, settled calls), and `tight-spiral-patterns.md` (the recipes). The Meta-Synthesis practice is the discipline of *reconciling* them after each build: a recurring catch (e.g. the partial-picture problem, caught three times) graduates from a one-off note to a seat (the Coherence Skeptic) to a decision-log entry. The Drift Fork's parking lot (§6, Stage 5) feeds it — parked surprises that recur across builds are exactly what promotes to pattern.

**The rule.** Nothing important stays trapped in a chat transcript. A build that closes without a durable signal logged (Ten Questions #10) hasn't actually closed. The studio gets progressively more capable only if each project *strengthens the layer* instead of evaporating.

*This is the one structural addition from the external manual worth building. The manual proposed it as the highest-value layer; that judgment is correct, and it's adopted — reframed from "an engine to build" to "a reconciliation practice the founder runs against assets that already exist."*

### 6.3 Written exit criteria (the gate has teeth only if "ready" is written down)

Borrowed from stage-gate engineering's hardest-won lesson: *a gate without a pre-written pass-condition advances on politics, not evidence.* For a solo studio the "politics" is subtler — it's mood, momentum, or the sunk cost of a build you like. The fix is the same: **write the one-line exit criterion for each stage at Stage 3 (spec time), before the heat, so the gate checks against a standard set when you were cool-headed, not one improvised in the moment.**

This generalizes the Fidelity checklist (already signed at Stage 3) from "the playtest pre-flight" to "every gate." Each stage's criterion answers one question: *what specifically must be true to leave this stage?*
- **−1 Intake:** sorts cleanly to one of the four bins, and a "build now" names what it displaces.
- **0 Medium & Novelty:** the medium lane is chosen by the gate (not by habit) and the one structural surprise is named.
- **1 Construct:** what the build measures is stated, with an evidence model that isn't self-report.
- **2 Task spine:** the player does a discipline-real task; the Four Freedoms are located; freedom-to-fail present.
- **3 Spec:** parameters locked, wireframe drawn, Fidelity checklist signed.
- **4 MVP:** the smallest thing that does the named job runs.
- **5 Playtest:** both ledgers clean (Fidelity binary-pass; Emergence captured/parked, not bleeding into scope).
- **6 Work-up:** passes C1–C5; medium executed faithfully to its lane's rule.

The criterion is one line, written once, checked at the gate. If it can't be written, the stage isn't understood yet — which is itself the finding. The agent pre-flight checks the *mechanical* part of each criterion (is it present, signed, non-empty); the founder judges the *meaning* (is it actually true). Cheap, and it converts "does this feel ready?" into "does it meet the line I wrote?"

---

### 6.4 The Kernel Track — the parallel research lane (locked 2026-07-02)

The game pipeline (Stages −1 through 6) is a **production line**: an idea enters, a build ships, the line moves on. The Kernel Track is different in kind — it is the studio's **knowledge substrate**, and it runs *parallel* to production, feeding it, fed by it, never gated by it.

**What a kernel is.** A kernel is a teaspoon of knowledge: one small, source-verified, cross-disciplinary claim, calibrated well enough to build on. Each kernel carries (1) its **claim** in one plain sentence, (2) its **provenance chain** — sources named, dated, with license status (openly licensed or open-access strongly preferred; the paywall problem is part of why this track exists), (3) its **confidence tier** — verified / provisional / contested, with the disagreement named when contested, (4) its **conditions of application** — where it holds, where it breaks (a judo move has situations; so does a finding), and (5) a **last-touched stamp** (kernels are accumulators; the decay rule applies — a kernel nobody has re-verified in a set window drops a tier, it does not silently stay "true").

**Why this track exists.** Peer review does not incentivize replication; publishing walls reliable knowledge behind paywalls; LLMs consume the entire corpus, noise included, at enormous energy cost, and cannot show their provenance. The kernel bet is the opposite architecture: **few, small, verified, traceable, open**. Low-density by design. A kernel system does not replace an LLM's generative breadth — it replaces the *trust function*: when Confluence needs a claim to calibrate against, it anchors to a kernel, not to a model's recollection.

**What it feeds.** Three consumers, in order: **Confluence** (kernels are the ground truth calibration norms against), **the builds** (a game's disciplinary claims cite kernels, not vibes — Stage 0.5's disciplinary panel is where a build's kernel needs get named), and **the University of the Open Mind** (the network where kernels circulate, get stress-tested across disciplines, and accumulate into the OER hub — the long horizon). Every consumer is also a producer: **every shipped build's Stage-7 Harvest is a candidate kernel** — "the one thing this build proved" is exactly a kernel-shaped claim, and the Harvest now routes it to this track for verification.

**The kernel loop** (a tight spiral, like everything else): **SOURCE** (a candidate claim arrives — from a Harvest, from the forward agents, from the founder's reading, from a disciplinary panel) → **VERIFY** (trace it to primary sources; cross-check across disciplines; the Just-in-Time Expertise rule and the Fact-Check Lead govern here) → **CALIBRATE** (assign confidence tier; name conditions of application; name what would falsify it) → **SHELVE** (tagged by discipline and by which builds/tools consume it) → **RE-VERIFY on use or on clock** (a kernel pulled into a live build gets a freshness check; an untouched kernel decays). The founder gates tier assignment — a kernel is never promoted to *verified* by an agent alone. Human-in-the-loop is the hub here as everywhere.

**The forward agents (the advance team, formalized).** A standing pre-pipeline motion, not a stage: agents watch the founder's **seeds** — the ideas he is merely circling, the parking lot, the braindumps — and run **advance work** before anything enters Intake Triage: source what exists, find the precedent (who has tried this, what happened), pull candidate kernels, name the viability question a human would have to answer. When a seed matures and hits Stage −1, it arrives *already scouted* — the founder's judgment lands on a prepared field instead of a blank one. The advance team reports through the daily-brief charter (max five items, every item ends with a TSP-application line, "nothing worth your time" is an allowed report). Borges Left monitors the whole motion: advance work that answers from a partial corpus is the drift this system kills.

**Boundary rules.** The Kernel Track never blocks a game build (a build missing a kernel notes the gap and proceeds; the gap enters the track as a sourced need). FERPA and provenance floors apply in full — no student data ever becomes kernel material without documented consent, no source enters without its license named. And the track is itself an accumulator: it sheds. A contested kernel that stays contested past its clock is retired to the parking lot with its dispute documented, not held forever as ambient doubt.

**MVV (the smallest honest scale):** extract **one kernel** from an already-shipped build's Harvest, run it through the full loop — source, verify, calibrate, shelve — and hand it to Confluence to calibrate against once. Prove the loop turns before building the library. Grant money follows evidence, not vision; so does this.

---

### 6.5 The Walkthrough Gate + Fidelity Tiers (locked 2026-07-02)

*Folded from the Home-era walkthrough post-mortem: the pipeline audited floors but never experience; flat builds canonized because no gate asked "does this feel like a place?" Twin rule paid in full: two gates in, two seats out (named at bottom).*

**Stage 6.5 — THE WALKTHROUGH GATE (final gate).** Sits AFTER Studio Eyes (Stage 6), BEFORE Ship & Canonize (Stage 7). Cheap machine checks fire first; the founder's eyes fire last and only on builds the robot already passed.

**The gate:** Matt plays the build on his phone, cold, as a player. Binary, adversarial, gradeable by someone who sees only the session:

1. **Place** — did it feel like somewhere, not something? (A screen with controls fails; a room you're standing in passes.)
2. **Notice** — within the first screen, did your eye go somewhere and find something?
3. **Pull** — at the end, did you want a next room? (Ending on a shrug = Peak-End seat's flat-ending HALT, now founder-verified.)
4. **Seams** — did any transition, load, or reset break the spell?

Any NO = HALT back to build. Nothing canonizes without this gate — no exceptions, including tools (tools walk through at their tier's bar, below).

**Not only a gate:** informal phone walkthroughs are encouraged at every stage (Filament: playtest all the way through; the formal gate is the last of many sits). The gate is where it counts, not where it starts.

**Fidelity Tiers (Filament's Alpha/Beta/Gold).** Every build carries a visible tier label from Stage 0. Exit criteria, not moods:

- **ALPHA** — the mechanic proves itself. One loop playable. Art minimal. Never player-facing outside the studio.
- **BETA** — content-complete, playable end to end, all floors pass. "It works."
- **GOLD** — you'd hand it to a stranger. Full craft pass, seams designed, one coherent scene system. "It glows."

**Canonization floor:** player-facing builds require GOLD. Internal tools require BETA (the studio doesn't gold-plate its own wrenches). Nothing below its floor enters Stage 7 — "shipped" no longer means "passed the auditor."

**The Home rule:** The Home is the only front door. Nothing enters it below GOLD, including existing shelf builds — the gate applies retroactively at the door.

**Fire-stamps (field, not a rule).** Every advisory seat's §5.6 row gains a `last-fired` stamp, written at Stage 7 harvest when a seat's catch changed the build. Future prunes go by fire record, not remit argument.

**Twin-rule prunes (two seats retired):** (1) **Physical Plausibility Critic** — remit fully redundant: floating/impossible-light/uncanny already held by Physics & Wear Artist + Diorama Lighting Director + Composition & Staging Lead. (2) **New Yorker Comic Writer** — one of three overlapping humor-craft seats; edge survives with the Satirist, shareability with the Casual/Reddit Reader. Prune criterion was remit-redundancy because no fire log existed at prune time — the fire-stamp field fixes that for next time. Either seat re-earns a chair with a named trigger and a documented real catch.

*Provenance: post-mortem seats consulted — TSP/Conductor, FableVision, Filament (gate placement + tiers adopted), MIT Media Lab (demo-or-die → founder walkthrough moved inside the pipeline), Apple (seams are the product), State of Play/Lumino (one scene system). Founder locked via Filament's slate, 2026-07-02. Folded into the OS body during the 2026-07-02 shelf reconciliation; the standalone patch file retires.*

---

## 7. Standing patterns & asset rules (quick index)

The recipes live in `tight-spiral-patterns.md`; the laws live here.

**Standing asset rules (C1–C5) — law for every asset:**
- **C1** — Joy/novelty in every asset; a flat asset is a failed asset.
- **C2** — The entry point is huge; never bury it behind flat reassurance or instructions.
- **C3** — Palette deliberately composed; real value range + temperature relief (anti-mud) — subordinate to the Visibility floor.
- **C4** — Cognitive science grounds every choice (attention, load, dual coding, spacing/retrieval, generation effect, feedback timing).
- **C5** — Mnemonic icons as a rule; each icon must express the point and land faster than the word, or it's decoration and fails.
- **C6 — The 50-word ceiling (locked 2026-07-02, folded 2026-07-13).** No player-facing
  screen carries 50 or more words of *instruction*. Story text, teaching feedback, and the
  player's own material are exempt; setup, directions, and reassurance are budgeted.
  **The affordance teaches, not the paragraph — if a mechanic needs a paragraph to explain,
  the mechanic isn't done.** Lineage: Lure of the Labyrinth / Amanita wordless-world
  discipline; Scot's standing note (too long, too text-heavy) made law.
- **C7 — The >50% image floor (locked long-standing, MADE ARITHMETIC 2026-07-13).** A game's
  first paint is at least half scene. **Enforced by Studio Eyes `IMAGE_FLOOR`** on a phone
  viewport, `<meta name="tsp:surface" content="game">`. Measured 2026-07-13: seven of eight
  core games failed — CYL v5 at 0%. It had been a founder law with no check for months, and
  so it was a wish. *A first paint that is mostly prose is a document with buttons.*
- **C8 — Tap the world, not menus (locked 2026-07-02, folded 2026-07-13).** Design DNA:
  **Samorost** (you tap the world) x **Lure of the Labyrinth** (near-zero words) x
  **Lumino City** (one handcrafted scene IS the game) x **Metroid** (chambers gate chambers;
  **the world remembers** — clear a move and the scene changes behind you).
  **THE FLOOR COLLISION, RESOLVED (founder call):** *Samorost hides its hotspots; this studio
  never does.* Every hotspot carries a bold outline, full keyboard order, and a duplicate
  plain-button affordance. **Engagement proposes, floors dispose.**

**Pattern shorthand:**
- **Nunan Task Spine** — the player does the discipline's real work; rank mechanics by transfer.
- **Outcome Microtag** — assessment rides on the move, not a score; tag chain `[ISLO-n] ← PLO ← SLO ← competency-cell` + AAC&U level by performance; instructor-facing, hidden in play.
- **Three Outcome-Moves** — A "Carry it in the object" (Roles); B "The turn you earned" (Combo, late legible payoff); C "Follow it without flinching" (Combo + open product).
- **Tiered Depth (flOw descent)** — minimal surface, player-chosen depth, every ring reversible; the player descends only as far as they want. Used for meta-layers and governance surfaces alike.
- **Maslow-descent (flOw levels)** — a hierarchy the player is *pulled down* (the force acts on them) and can climb; descent is the cost, noticing is the brake. Governed by the three trauma-informed rails. *Canonical recipe (math, rungs, rails, a11y): `tight-spiral-patterns.md` §8.*
- **Glass Engine** — the learning mechanism is visible, not hidden; moves visibly stack, with a "show the engine" depth that maps each move to the outcome.

---
## 8. Delegation & Strengths Map

The studio's organizing principle: the founder is the eyes, the voice, and the judgment. Everything else should be pushed off his plate. For any project, sort the work four ways:

- **Founder only** — taste, voice, the human gate at every pipeline stage, final visual verdict (the eyes), locked-call judgment. Cannot be delegated.
- **AI** — the mechanical pre-flight at every stage, drafting against a spec, code, reconciliation, search/sourcing, asset generation from a written brief, clearance runbooks (steps, not the judgment).
- **Eliminate** — work that exists only because a process is heavy; cut it before delegating it.
- **Not the TA** — the part-time TA is **not** a delegation channel for studio work. Route studio tasks to the founder, to AI, or to elimination. (This corrects earlier guidance.)

Every project gets a delegation pass. The pipeline (§6) already enforces this: the agent pre-flight is the standing AI-delegation of the mechanical, leaving the founder only the judgment.

---

## 9. Current projects & assets

*Status key: SHIPPED · IN-LOOP (Stage 5) · BUILT (content/mechanic complete) · DESIGNED (not built) · PARKED (do not build until the founder opens it).*

### Active builds
- **Choose Your Leader** — BUILT (content-complete) + Paper Craft started. A noticing game: "you don't judge the leader, you judge what you were allowed to see." Per scene: scene-first onramp → blind trust commit → the record turns (dated/sourced) → Maslow-as-flOw-descent (pulled down, noticing is the brake; canonical recipe in patterns §8) → tiered-depth engine. **Roster (two eras, 3+3):** Cold War trio LIVE with web-verified dated records (JFK/1962 Cuban Missile Crisis; LBJ/1964 Gulf of Tonkin; Nixon/1969 silent-majority/Cambodia). Current trio GATED, records not fabricated, excluded from play until sourced (Obama, Trump, Biden). **Disciplinary Panel seated (the worked example for §6 Stage 0.5):**
  - **Freire — spine.** The game *is* conscientização: reading the word (the quote) and the world (the record) to see the power inside the rhetoric. Must *pose the problem*, never deposit the lesson. If a scene tells the player what to think about a leader, Freire HALTs it.
  - **Saunders — entry & pacing.** Owns the opening as a *held breath, not a diorama*, the withholding (commit before the record), and escalation across scenes. The moral weight arrives sideways, through the room and the gap — never narrated.
  - **Squire — the loop.** The scene must be an emotionally compelling *invitation into a world* (1962, the glow, the dread), not a non-flat screen; understanding develops through cycles of performance (commit → record → re-commit).
  - **Gee — situated meaning & identity.** The player *is* someone in that room; the quote means something *situated*, not dictionary-abstract; the probe-hypothesize-act cycle is the trust-commit loop.
  - **Stuart Hall — the core mechanic.** Encoding/decoding: the address is *encoded* by power; the player learns to decode it oppositionally instead of dominant. The gap the game measures *is* the distance between dominant and oppositional reading. (Hall is why the mechanic works at all.)
  - **McLuhan — the medium is the message.** The glowing TV/radio in the living room is itself content; the setting teaches before the words do.
  - **Postman — *Amusing Ourselves to Death*.** The televised address as a form shapes what counts as truth; the 1962/64/69 living rooms stage his thesis.
  - **Arendt — truth & politics (reach seat).** On lying in politics and what rhetoric does to a public; the deep-ending teach about "how far this can carry a person" is Arendtian.
  - **Salen & Zimmerman (*Rules of Play*) — meaningful play & emergence.** Seated 2026-06-27. Owns the question no other CYL seat answers: *is the play meaningful (action→outcome discernible AND integrated) and emergent, or just scripted discovery?* Their verdict on CYL: strong on the **culture lens** (the game is genuinely about how media frames truth — most games treat that as an afterthought; CYL lives there) and the **magic circle is deliberately porous** (real presidents, real deaths), which makes the protective framing — "you judge what you were allowed to see, not the leader" — *load-bearing*, the only thing holding the lusory attitude together against real-world spillover; protect it fiercely. The real ceiling they name: **weak integration + low emergence** — scenes are independent scripted rounds; your JFK read doesn't alter the Nixon scene (the arc screen aggregates but doesn't integrate), and every gap is authored, so the player *discovers* but doesn't *generate*. The river-meter pivot (rank your own values → see the distribution you didn't script) is, by their lens, the **maturation** of CYL — the move from scripted discovery toward emergent meaning. Push the pivot toward *choices that accumulate and alter what comes next*, not just aggregate on an arc screen.
  Roster status: **Obama un-gated 2026-06-27** with the May 23 2013 NDU drone-war scene (sourced: whitehouse.gov; leaked PPG/Drone Papers; BIJ casualty estimate "as of 2013"). Four scenes now LIVE (JFK/LBJ/Nixon/Obama); Trump + Biden remain gated — the even-handedness condition is now *binding*: both need identically rigorous, identically critical sourced gaps before un-gating.
  Paper Craft: four hero rooms built; descent planes await the descent-math gate. **Open founder calls:** descent-math feel; the Saunders entry-staging pass (held-breath opening); the **integration/emergence note (Zimmerman, logged):** scenes don't yet alter each other — not an MVP blocker, but the move that takes CYL from scripted discovery to systemic/emergent play, and the design home of the river-meter pivot; source Trump + Biden (even-handedness now binding); project name; exact Leadership rubric; which rubric dimension first.
- **Glass Engine** (`glass-engine.html`) — IN-LOOP. Teamwork-rubric game (AAC&U), MassBay. Core loop locked: NOTICE/GAIN-INFO front (no scoring, every read valid), APPLICATION back (graded on use/transfer). Epistemic frames, plural terminals, engine toggle. **Ship blocker:** placeholder FRAMES "why" lines + info-lines need rewriting in the founder's voice (the 90-min protected block). Async multiplayer stubbed.
- **Confluence calibration system** — IN-LOOP. Rater-norming tool; ground truth = MassBay placement portfolio rubric (1–6). `confluence-calibration-v6.html` active; `calibration-ladder.html` built. Decision: build short Nunan-task games on CC-BY open text for norming practice before content-heavy games.
- **Dad Energy** — SHIPPED (v1, `dad-quest.html`). Cut-paper, 5 scenes, promise meter, castle reveal locked to Scene 5, Greg the pancake Scene 1. **v2 "cinema cut"** DESIGNED (POV-flip, withheld face, 10 frames) — depends on raster art.

### Designed, not built
- **Dad Energy v2 cinema cut** — raster track; `raster-art-brief.md` exists; image-capable session.
- **Choose Your Leader v2 tracks** — Visual + Socioeconomic content views; post-MVP; five-stage agent pipeline spec (`presidential-rhetoric-pipeline-spec.md`).

### Parked (do not build until the founder opens it)
- **Sensory Memory** (visual→media literacy; opens with exposure not instruction).
- **AI Literacy game** (dual teacher+student; produces a charter+policy artifact; existing 5-beat demo too long to be the pilot).
- **ISLO tagging/visibility demo** for the Provost and Catherine.
- **Compound-iconography / metaphor-prism system** (potential IP/method).
- **Tight Spiral Web Design** and **Tight Spiral Publications** (possible imprints, unscoped).

### Tools & labs built (single-file, house style)
Capability labs (feel/movement/device/sound/buttons), Scarry study set, Confluence builder, gap-map, layout-levels, visual-rhetoric, litmag-desk, avatar-builder ("Paper Players"), studio-tracker, studio-bench, the **Studio Intake** (front door + human-in-the-loop decision surface), and the **System Map** (gears).

### Assets & references
- Sabbatical report on ludic pedagogy (Drive) — the founding theoretical document.
- "Matt's Writing" folder (Drive) — the authentic-voice reference.
- This OS — the operating source of truth. Companions: `tight-spiral-patterns.md` (recipes), `tight-spiral-production-pipeline.md` (the full pipeline write-up).
- MassBay: 7 ISLOs and PLOs (massbay.edu); placement portfolio rubric (1–6); AAC&U VALUE rubrics.
- USPTO trademark clearance — Classes 41 and 9 for "Tight Spiral Studios" (runbook delegable; judgment reserved).

### On the horizon
- Glass Engine voice pass (standing ship blocker).
- Sean McCarthy pitch — Confluence as ISLO-layer assessment engine.
- Source the first living-president CYL scene to un-gate it.

---

## 10. Decision log

Settled calls. A future session — human or AI — should not reopen these without a real reason.

- **The 2026-07-02 amendment set (voice session; full statements in §1, §5, §6.4).** Four linked calls. (1) **Studio name: Tight Spiral Productions (TSP)** — supersedes "Tight Spiral Studios" (locked 2026-06-27, now retired). TSP = teaspoon, the micro-unit; the acronym names the method (micro-moves composed into systems — the founder's wrestling/judo/language throughline, now the studio's stated epistemology). Rename propagates as-opened, never bulk. Imprints unchanged. (2) **The Kernel Track (§6.4)** — a parallel research lane producing calibrated knowledge kernels (small, source-verified, cross-disciplinary, provenance-chained, openly licensed, decay-clocked) as the studio's knowledge substrate: the low-density, auditable, energy-lean alternative to LLM-scale knowledge; feeds Confluence, the builds, and the University of the Open Mind; every Stage-7 Harvest routes its proved claim here as a candidate kernel. MVV bound: one kernel through the full loop before any library. (3) **Borges Left seated (§5)** — HALT-power full-corpus assembler; no structural/strategic answer ships from a partial corpus; monitors the Timing Belt. (4) **Forward agents formalized (§6.4)** — the advance team watches seeds and runs advance work pre-pipeline, so ideas arrive at Intake Triage already scouted; reports through the daily-brief charter; Borges Left audits its corpus discipline.
- **The Probe Sweep + the accumulator decay rule (locked 2026-06-29; full statement in §5.4.5.1).** Two linked calls. (1) **A founder question is a system-wide probe.** When the founder asks a structural/diagnostic question, the Conductor extracts the underlying *test* and runs it against every OS component *before* answering the narrow case — the question-side twin of Maximize-or-Check (that propagates a direction; this propagates a question). The sweep **writes back**: every gap it surfaces is auto-queued for graduate-or-kill, never left as a write-only note. (2) **Every accumulator must be able to shed.** The tighten-by-pruning brake that governs builds is extended to *all* accumulators — parking lot, memory, panel roster, Props Room, file shelf. Each carries a last-touched stamp and a why-held note; on review the only outcomes are promote or kill; "held" has a clock, it is not a permanent state. Worked example that locked both: a question aimed only at the parking lot carried the test "accumulates but never sheds?", which on sweep hit five components at once; and *memory consolidation* sat parked until it hit the memory ceiling and hard-blocked new locks — proof an un-clocked accumulator becomes a wall. Also records that **the Conductor** (the firing runtime, memory-resident since 2026-06-27) was written into the OS here for the first time (§5.4.5) — itself a caught accumulator gap: a locked concept that never reached the durable shelf.
- **Just-in-Time Expertise — the default route for any expert-domain decision (locked 2026-06-28; full statement in §4.3).** Gee's just-in-time/on-demand principle turned inward on the studio's own process: when a call sits inside a real domain (psychometrics, survey design, sound, period history, law, stats, accessibility medicine), **consult live current expertise at the decision point — search the actual literature and standard practice — rather than settling from AI training-data priors or a founder guess.** A confident answer inside an expert domain is a *trigger to consult, not to proceed.* Worked example that locked it: CYL's trust instrument — the armchair recommendation (a 3-point more/less/neutral scale) was plausible and wrong; the survey-methodology literature flipped it (3-point scales are documented inadequate for direction+intensity; use finer 5–7-point or feeling-thermometer instruments; identical pre/post wording; ipsative per-player deltas). Owned by the relevant Disciplinary-Panel domain seat; for measurement specifically, the Measurement Design seat is a hard ship gate on any player-measuring build. Sibling to the Fact-Check Lead (wrong facts) — this guards unconsulted judgment.

- **Studio name: Tight Spiral Studios.** *(SUPERSEDED 2026-07-02 → Tight Spiral Productions (TSP); see the amendment set above.)* Tagline "Play. Notice. Design." and descriptor "We turn how you learn into how you play." carry forward unchanged. (Names closed: Sandbox, Possibility Space, Spiral-alone.)
- **Art medium: no default, gate fires first (2026-06-27, supersedes the earlier "cut-paper is the locked default" call).** Medium is chosen fresh every build via the Medium Gate (§3.2), now three lanes: **licensed photo/audio** (realism is the point — sourcing rule, never real likenesses in inclusive builds, never real faces in CYL), **raster/Lumino** (Super Sketchy, AI-assisted, labeled), **cut-paper SVG** (clarity + people-as-roles; load-bearing for the inclusivity floor and offline buildability). Cut-paper remains the *most common outcome* but is no longer the *unexamined default* — "jamming everything through cut-paper" means the gate wasn't run. Never grind one medium toward what another does (the SVG-photoreal trap, now lane-agnostic; PM seat's SCOPE HALT owns it).
- **Five gate outcomes + written exit criteria (2026-06-27, borrowed from stage-gate engineering).** Gates now emit one of five — GO / CONDITIONAL GO (advance on one named fix) / RECYCLE (back one stage, not parked) / HOLD-PARK / KILL — replacing the blunt advance-or-stop (§6). And each stage gets a one-line exit criterion written at Stage 3, before the heat, that the gate checks against (§6.3) — generalizes the Fidelity checklist to every gate; converts "does this feel ready?" into "does it meet the line I wrote?"
- **Collections, not islands — the season model (2026-06-27, borrowed from fashion).** Builds group into collections sharing one spine (a mechanic/theme/house move), reference each other, and ship as themed seasons rather than scattered one-offs (§1.1). The player-facing "house mechanic" engagement lever, formalized. Latent collections: Noticing (CYL/Glass Engine/Sensory Memory), Calibration (Confluence/ladder/Nunan-norming), Show-the-Engine. An organizing lens, not a ban on one-offs.
- **The player never does the studio's work (locked 2026-06-27).** Back-of-house structure — collections, house-mechanic names, season labels, the panel, the pipeline, microtags — must never surface as player-facing furniture the player has to read or track. Recognition across builds is *felt through shared mechanics*, not announced with badges. The test: if a studio concept has to show on a player's screen to "work," it has become work, and it has failed. This generalizes scene-first, the huge entry, and no-jargon-on-surface into one principle: the player came to play; the filing system stays back-of-house. (Caught when an audit tried to stamp "Part of the Noticing collection" on CYL's screen — the collection is for the founder, not the player.)
- **Disciplinary Panel — new pipeline Stage 0.5 (locked 2026-06-27).** After intake and medium, every game *names its discipline and seats the scholars who theorized it* — generative, not critical: it says what the game must *be* to honor its subject, where the craft panel says what's wrong. Standing anchors (§4.3): **Piaget** (constructivism — build, don't transmit; the "notice don't narrate" law), **Freire** (critical pedagogy — problem-posing not banking; reading word + world), **Saunders** (the fiction mind — entry, withholding, escalation, sideways moral weight; the held-breath-not-diorama instinct). Per-game bench extends these. Seat a spine / entry-pacing / loop / core-mechanic conscience; 4–8 scholars, never a library. CYL's seated bench (worked example, §9): Freire spine, Saunders entry, Squire loop, Gee situated-meaning, Hall encoding/decoding core mechanic, McLuhan + Postman the medium/setting, Arendt truth-politics reach. **Why this exists:** the panel was all critics (catch bad) and nothing generative (make great) — clean work that's a little dead. The disciplinary panel is the maker chair. Founder is big on Piaget/Freire/Saunders.
- **The Kintsugi Method — a design principle, not a floor (locked 2026-06-30).** Kintsugi repairs broken pottery with gold so the join is highlighted, not hidden; the bowl is prized *because* it was mended. In learning design: **the revision and the repair are where the value lives, and the system makes them visible instead of sanding them away.** Not a motivational line — a structural call about where time goes, what shows in the interface, and what gets assessed. Three established practices already behave this way (the through-line that earns the metaphor): deep revision in composition (revision ≠ editing; the field's own finding that revision is where learning happens), iterative game design (ship beta → collect breakdown → mend → ship), and revision plans as a better window on thinking than the draft. Four principles: the fracture is data (capture the wrong answer / failed playtest, don't discard it); repair is visible (show history and reasoning, not just the polished final); the mended object is more valuable (a piece documenting its own evolution beats a clean first attempt); no two repairs alike (the mend fits the specific fracture). **Assessment hook:** a repair note ("what broke / how I mended it") is scorable on three things — did the learner *locate* the real problem, *justify* the change against purpose/audience, and *carry it out*. **Accessibility dividend:** one visible seam is lower-clutter than a hidden-history polished surface — visible-repair and accessible design pull the same way. **The twin (accumulator decay):** the standing "ship the beta / good-enough-today" antidote to optimize-before-implement is *folded into* Kintsugi as its creator-facing application — the mend cycle IS the work, so there is nothing to perfect before it starts — and is pruned as a standalone note. **MVV bound:** EN195 Flash Fiction, one repair note on a Sandbags→Review-Bench revision, run once before scaling. **Surface rule:** when this becomes a player/student-facing screen, it opens on the mend-as-joy (gold seam draws first), never the break-as-confession — a cold "tell us what went wrong" prompt is a dignity-first/trauma-informed HALT (forced disclosure). Long-form: `kintsugi-instructional-design-brief.md`. **Harvest (what this proved):** a repair artifact is assessable evidence of revision thinking, and making it visible is a low-clutter accessibility win, not a tradeoff against one.
- **Two hard walls above all:** no emoji ever; the safety walls (trauma-informed, FERPA) protect other people and never become optional. Everything else sensory/comfort (contrast, motion, palette, type) is a best-practice *default-plus-toggle*, not a production wall — see the two-tier floors block (§5.6, revised 2026-06-30).
- **Visibility — best-practice default, not a wall (revised 2026-06-30; was a hard floor 2026-06-27):** high-contrast ink is the *default every build ships in*, with a reachable contrast/palette toggle so the person tunes it to their own eyes; muted-gray-on-light stays the wrong default. The seats (Reads-As, Screen-Optimization, ADA) set the default and advise — they HALT only if a build ships with no reachable control or a default that's itself unreadable. See the two-tier floors block in §5.6.
- **Scene-first floor (2026-06-27):** every game opens by landing the player in a scene where they notice something — no text-first opening.
- **Engagement from first contact (2026-06-27):** use the device's body when permissible; the first tap unlocks haptics/audio (permission-clean, ambush-free); engagement is subordinate to the floor.
- **Maslow-descent + the consequence/TI compromise (2026-06-27):** keep full consequence, re-aim it — the player always feels the drop, the game never blames them. Three rails: (1) consequence lands on the *rhetoric's reach*, not the player's worth; (2) the brake (noticing) is always live and naming the gap is the win, even at the floor; (3) the deep ending teaches, never gotchas. Generalizes to any descent mechanic. *Full recipe + math reconciled into `tight-spiral-patterns.md` §8 (canonical); this entry records the decision, not the implementation.*
- **Tiered Depth (flOw descent) is a studio pattern (2026-06-27):** minimal surface, player-chosen depth, every ring reversible — for game meta-layers and governance surfaces alike.
- **Human-in-the-Loop Productions is both a named imprint and the hub (2026-06-27):** the art imprints mesh to it, never directly to each other; every output carries a human gate.
- **The TA is not a studio delegation channel.** Route to founder, AI, or elimination.
- **The Scout wall:** money reasoning never touches a design decision; the Opportunity Scout sits unmeshed and only speaks when the founder convenes it.
- **The Field Scout (seated 2026-06-27) — institutional sibling to the Opportunity Scout, same wall.** Watches the serious-games / civic-ed / learning-sciences field and surfaces, *only when the founder convenes it*, exactly three kinds of thing, each tagged: a **METHOD** that could improve a build, a **STANDARD** the work should meet, or a **DOOR** (grant, showcase, cohort, award) worth walking through. Hard rule mirroring the Scout wall: **it informs, it never reshapes** — an institution improves the work or opens a door; it does not get a vote on a design decision, and locked calls stay the founder's (the same relationship MIT holds as a reference seed). The anti-pattern it exists to prevent: collecting impressive affiliations that change no decision (prestige is not a method, a standard, or a door — an org that gives none of the three is just a logo, and the Scout drops it). Sits unmeshed beside the Opportunity Scout; surfaces on "convene the Field Scout." **Standing field map (2026-06-27, tagged):** *Tier 1 — load-bearing now:* **Games for Change** (DOOR: Best in Civics / Best in Learning awards — 2027 cycle, since the 2026 window closed Feb 16 2026; the July 21–22 2026 Festival at The Glasshouse NYC; G4C Learn library. STANDARD: their Best-in-Civics rubric — complex systems represented, player grapples with their own role, theory-of-change verified with subject-matter experts — is effectively CYL's design brief; design toward it now). **Stanford History Education Group / Civic Online Reasoning** (METHOD + STANDARD: the institutional cousin of CYL's thesis — teaching source/frame evaluation; citable evaluation rigor). **GLS / the Gee lineage** (METHOD: the academic home of the learning-principles spine; Gee is already a founder anchor — scout where that community convenes now). *Tier 2 — standards/credibility:* **iCivics** (STANDARD + DOOR: the US-classroom civic-games benchmark + a distribution model), **MIT Education Arcade / Game Lab** (METHOD: iterative playtesting — already a reference seed), **Joan Ganz Cooney Center** (STANDARD: learning-game efficacy research — the evidence base the Research Compendium gap would cite). *Tier 3 — funders (Opportunity Scout territory, walled):* **Knight Foundation** (civic-information/media-literacy — closest to CYL's content), **MacArthur** (historic Digital Media & Learning funder — heavy lift for a solo studio; know it exists, don't chase), **Mozilla/media-literacy funders** (periodic). *Honest filter: of all of these, only three change what gets done this month — G4C (design toward the civics rubric), SHEG (method + citation cousin), and filling the Research-Compendium + Transparency-Standard dossier gaps for a 2027 G4C submission. The rest are "open the door when the build is ready."*
- **Inclusive default:** de-gender relentlessly; "anyone can have it" holds every line; skin-tone-neutral figures; the prop carries the role.
- **Component Delivery Review (2026-06-27):** the panel gains a second mode — two-pass delivery assessment (individual on the AAC&U 1–4 scale, then seams compound/cancel, capped by the weakest seam); Stage 5/6 only.
- **Coherence Skeptic seat — HALT on all output (2026-06-27):** a standing seat that judges whether an output, *shown by itself with no surrounding context*, reads as coherent or looks unhinged — the partial-picture problem. Unlike the Skeptic-Translator (presentation-only), this HALTs any artifact entirely. Standing duty: when it fires it **advises the founder before output** (names the incoherence, the missing context, the smallest fix that makes the fragment stand alone) and **logs the moment as a decision point** so the trap is caught earlier next time. Sits in every convening.
- **External Panel Operating Manual — harvested, not adopted (2026-06-27):** an external draft proposed replacing the persona panel with nine role-based councils plus a constitution. **Declined** the wholesale swap — the persona panel (§5) is the studio's working method and the manual's nine-council structure is org-sprawl for a solo studio (violates §2's attention-scarcity). **Harvested two parts:** the **Ten Questions** universal review (now §6.1, a coverage checklist the seats run against) and the **Meta-Synthesis layer** (now §6.2, institutional memory reframed as a reconciliation practice over the Knowledge Graph + decision log + patterns file). Do not re-litigate adopting the full manual; the valuable parts are already in.
- **Working-relationship rules — how Claude operates with the founder (2026-06-27):** four standing rules governing the session itself, not any one build. (1) **File presentation:** every response touching a file ends by presenting it (download always visible); modified read-only project files get re-presented. (2) **Reconcile before every move:** before any next action, run/offer a memory-vs-disk-vs-sync check and surface mismatches; **make him say no twice** before dropping it. (3) **Source-is-truth / Project is the durable shelf:** memory + `/mnt/project` files auto-load every chat; `/mnt/user-data/outputs/` is scratch and does not persist; whenever a canonical file changes in-sandbox, the close-out step is to remind the founder to replace the Project copy. (4) **TLDR Kids on Claude's own replies:** the founder's mind moves fast and low-vision makes length costly — default short, answer/move in the first line, one idea per line, offer depth rather than dumping it. A long reply is a failed reply unless he asked to go deep. (5) **Maximize-or-check (eagle-eye forecaster):** when the founder gives a direction or rule, don't apply it narrowly to the one case — propagate it systemically everywhere it sensibly belongs, forecast the ripple, and flag the edge cases where it might apply but it's a judgment call, checking rather than silently over- or under-applying. *These guard §2's operating profile (attention scarcity, visual load, across-chats friction) at the conversation layer, where the panel's build-facing seats don't reach.*
- **Intake Triage gate — Stage −1 of the pipeline (2026-06-27):** every incoming idea is sorted *build now / park / delegate to AI / eliminate* at the Studio Intake surface *before* any panel convenes or novelty is named. Turns §8's delegation map into a mandatory entry gate. Structural fix for §2 failure mode #3 (too many parallel projects) — sprawl is stopped at the door, not discovered mid-pipeline. A "build now" that can't name what it displaces is a parked item in disguise.
- **Field Scout — institutional sibling to the Opportunity Scout (2026-06-27):** a second walled-off, convene-only Scout that watches the serious-games / civic-ed / learning-sciences field and surfaces only **method / standard / door**, each tagged — never prestige for its own sake (an org giving none of the three is a logo, and gets dropped). Same wall as the money Scout: it **informs, never reshapes**; locked calls stay the founder's (the MIT-reference-seed relationship, generalized). Born from a Games for Change pass: G4C's Best-in-Civics rubric reads as CYL's own design brief, so the Scout's first standing map tags G4C (door + standard, 2027 cycle since 2026 closed), SHEG/Civic Online Reasoning (method + standard), the Gee/GLS lineage (method) as Tier 1; iCivics / MIT Ed Arcade / Cooney Center as Tier 2 standards; Knight/MacArthur/Mozilla as Tier 3 funders (Opportunity-Scout territory, walled). Honest filter recorded in §10-principles: only three move work this month — G4C rubric, SHEG, and the Research-Compendium + Transparency-Standard dossier gaps for a 2027 submission. Full map lives in the principles block above.

## 11. Standing working rules — the fold, reconciled 2026-07-02

*(The July-1 fold (§11 of the 151,450-byte lineage) never landed in this lineage — a live phase-slip caught by the belt. Folded here compactly. Prune twin: the 12 superseded shelf files removed 2026-07-02 plus the four July-1 handoffs, which retire once this section is phone-saved.)*

**11.1 Reply format.** Options for the founder render as a scorecard (criteria + verdict line), never a flat list. Recommendations carry a confidence call on his likely pick, with the reason. At 75%+ confidence, Claude makes the call, names it, and proceeds — reversible, never silent. Below 75%, it's a real fork.

**11.2 Question-first + structure floor.** The answer or verdict is line one of every reply. Never land the founder on a raw text wall — in builds or in chat.

**11.3 Green-bail floor.** Green is banned in any primary or structural role (RP makes it unreadable). State is carried by position + label + shape.

**11.4 File-Save Verify floor.** No file is reported "done" or "saved" without a byte-count check on disk reported back. Silent success is the failure mode.

**11.5 Reliability floor.** No capability, file, or system claim ships unverified against tools or disk in the current session. The honest sentence is "I can't verify that from here."

**11.6 No-guessed-context rule.** Drafted messages never carry invented facts — no assumed statuses, no guessed pleasantries. Unknown slot: leave it empty or ask.

**11.7 Visual-assistant conventions.** Claude holds the device map (Mac + iPhone, no iPad; phone is the save device) and forecasts the exact screen before giving steps. Exact-title rule: every on-screen target is named by its literal label text. File-drop rule: every delivered file is presented as a card at the end of the message with its exact filename stated. "Work desk" is a banned phrase. Terminal is a poor RP tool — prefer browser paths.

**11.8 Interview pattern.** Scoping interviews run as tappable rounds (not open-text), one screen of 3–4 questions, read-back of meaning after each round, friction question first, rounds adapting to answers.

**11.9 The Timing Belt v2.** Six-turn protocol against the ledger: inventory + byte-check / phase-slips + who-fixes / verify live lanes / surface choices (auto-apply at 76%+, named + reversible) / task the advance team / emit ledger + Carry-Out. Prime directive: minimize data loss through founder process; maximize what agents carry without the founder's hands. Beat 7 = capability sweep — verify tool lanes, surface new platform capabilities for the Medium Gate roster.

**11.10 Medium Gate Lane D.** In-chat inline graphics (Claude's visual widgets) are a prototyping/Alpha-only lane. A widget dies with the chat; loved Lane D work must graduate to single-file HTML before canonization. Lane D can never be Gold in place.

**11.11 HITL closes every asset.** No generated asset ships untouched — rework, pair, or redraw; generator output is raw stock. Generate-then-rework is the default pipeline; concept-then-redraw for signature characters wanted unencumbered. Provenance ledger names the full chain, never just the endpoint. Title-level override: Funnybonies is all-CC (no MJ anywhere in that title).

**11.12 TA delegation is MassBay-only.** Institutional work (assessment, teaching, department, committee, curriculum, doc prep) → the TA is a valid channel; flag delegable tasks. Studio internals (builds, OS, art, clearance) → never the TA; route to the founder, AI, or elimination.

**11.13 Log it = tree it.** "Log it" produces the backward-looking decision tree as `session-tree.html` — canonical name, no date, replace-don't-add — auto-shipped to Drive `Claude_files`, never to the public repo.

**11.14 Canonical-name / no-collision-copy rule.** One canonical name per living file, no date embedded; replace the file rather than add a sibling. The " 2"/" 3" suffix is the tell that the rule was skipped.

**11.15 Drive standing permission.** Claude may read and write both Drives (walshero + post) without asking, under one hard condition: no student names or identifying data are ever scraped, saved, or stored — strip before any use. The durable studio archive is walshero-owned only.

**11.16 The Walkthrough pattern (promoted 2026-07-02, Props Room candidate).** Any large build can grow a touring entrance by additive injection, trunk untouched: a Lobby (scene-first, Begin / Skip), a fixed tour bar (room counter, one thing to look at, Next / Back / Add a note / End), per-room notes held in memory, and a Carry-Out emitting the notes as the next session's iteration list. Shipped first on Confluence (`confluence-walkthrough.html`). Rides with three standard Aleph cheap wins: last-muted-tier visibility override, global gold focus ring, scroll-reset on every room change.

**11.17 Legibility optimizer is floor, not comfort.** Six live controls (size, line-height, letter-spacing, measure, weight, palette) with research-set floors (18px size, 1.5 line-height, 0–0.12em spacing, 60–80ch measure, 400–700 weight, hyperlegible letterform criteria) and founder-set ship defaults. Every reachable state passes the floor independently; the surface must expose the controls.

---

## 13. Visual Constitution (referenced)

*Landed 2026-07-04 (founder voice session). The studio's craft spine lives in its own shelf file, `tight-spiral-visual-constitution.md`, so the belt can cite it directly and it can grow without swelling this OS. This section is the pointer + the belt hook, not the full text.*

**What it is.** The full doctrine for how everything looks and why every object exists: One Room world, timing-belt-as-OS, mnemonic object vocabulary, catalog density, material rules, prohibited aesthetics, the AI-as-production-assistant workflow, and the five-question Brand Test. Read the standalone file before any visual-rhetoric or landing-page answer.

**The gap it closes.** Before this, the belt moved builds and caught bugs but never checked whether a build carried the studio's *visual language*. Games drifted from the studio face — the design vision (Jenova flow hierarchies, Maslow-is-CYL) lived in the game docs and never surfaced on screen. The Constitution's **§6.1 game-tie clause** is the fix: a build is on the rails only when its design vision is legible in studio vocabulary on screen, not just in the doc.

**Two things it hardens into gates:**
- **13.1 The 50% text gate.** No page or screen lands where text is more than 50% of visual space, unless empty space is deliberately the point. A hard floor, not a preference. Rides in the PATTERN-TICK.
- **13.2 The logo.** A circle where the outer line *is* the circle — the ring is the outermost turn of the tight spiral, coiling inward. Not a spiral inside a ring.

**Palette reconciliation.** Arcade default palette B (High Lumen amber, 16.1:1) is the legibility *floor*; the Constitution's "reserve strong color for meaning" is the discipline *on top* of that floor. Not a conflict — B guarantees readable-on-load, §15 governs what added color may mean. Confluence green is institutional-tool-specific, never an inherited default.

**Belt hook — VISUAL-TICK folds into PATTERN-TICK.** Before any page ships, the belt also checks: the 50% text gate (§13.1), the game-tie clause (visual vision on screen), and the Brand Test (five questions, any "no" flags revise). One graduated change per the accumulation brake — the Constitution is the add; VISUAL-TICK extends the existing PATTERN-TICK, it does not stand as a new beat.

---

## 14. Lane truth — verified save architecture (2026-07-05)

*Added after live tool probes overturned three memory assumptions. The verified detail lives in `studio-file-map.md` on the shelf; this section is the correction of record so no future session repeats the errors.*

**14.1 The "Zapier can't do trunk files" myth is dead.** The 5K ceiling applies ONLY to the paste-text path. Zapier's file lane (Upload File from URL, Replace File, Move Files to Folder) handles up to 100MB. The move/replace/upload actions are live and tested. Trunk files fail the *paste* path, not the *file* path.

**14.2 CORRECTED 2026-07-13 — native Drive WRITE works.** The 07-05 claim that `create_file`
errors out is **stale**. It works with `disableConversionToGoogleType: true` + an explicit
`contentMimeType`. Zapier is **not** required for Drive push.

**14.3 Zapier moves and triggers. It has NO COMPARISON OPERATOR.** It cannot diff, hash, read
a git tree, or compute a contrast ratio — **at any tier.** (Founder is on **Pro**, not free;
never quote a task ceiling as a reason.) **It is not a cleanup, audit, or canon tool.**

**14.4 The repo is home. Drive is an address book.** Git is the only lane with a mechanism
that prevents two versions of the truth. See `COLD-START.md`.

**14.3 Three folders named `Claude_files` exist** (owners walshero + post). Memory carried one ID as if it were the only one. Until one is picked canonical, "save to Claude_files" is ambiguous — name the folder AND the ID.

**14.4 The connector addresses Drive by NAMED FOLDER, not folder-ID.** Save targets are named folders (Tight Spiral Studios, MW Knowledge Base, etc.). Archive lane: `move_files_to_folder` into an existing archive folder (`Archive Comments` = `1zqvxgKmET11R2Bx1hb-JjhQj-S4h1Cg9`) — move-not-trash, reversible.

**14.5 Shelf files are unreachable by any tool.** No rename, move, or delete tool touches `/mnt/project`. Shelf hygiene is phone/Mac only. Never claim otherwise.

**14.6 Bouncers — parked spec, not built.** "Agentic bouncers" (empowered founder-proxy gate-guards) captured as a post-July-6 build in the Command Center. MVP = existing belt beats (AI-Skeptic HALT, TLDR BAIL, 50% gate, FERPA strip) enforced as a pre-ship checklist, NOT autonomous agents. Autonomous founder-clone agents are clever-but-fragile — a system to babysit, the tool-chasing pattern. Checklist-first is durable.

**14.7 Probe before trust.** Any save failure → re-run the file-map probes and update dates. Memory is claims; tool output is truth.

---
## 12. The Cross-Lane Mount — canon is an address

*Locked 2026-07-10 (founder voice session). The governance primitive that connects
lanes without merging them. Extracted from the Confluence↔TSP link problem and
generalized: **canon is an address, governance is a flag on that address, and the
flag is machine-enforced.** Copies go stale; pointers cannot. Remembered rules leak;
flagged ones HALT.*

---

## §12.1 The primitive

Three moves, applied to every governed document in the studio:

1. **Canon is an address, not a copy.** A lane never holds another lane's content.
   It holds a *pointer*: canonical file ID + byte-count + version + last-touched.
   A pointer is ~200 bytes and is always current; a copy is stale the moment the
   source is edited. This is the accumulator-decay rule applied at the index level.

2. **Every mount carries a write-direction flag.** `RW` (this lane owns it, may
   write) or `RO` (this lane may read only). The flag is declared once, in the
   manifest, and enforced — not remembered.

3. **The flag is machine-enforced.** Studio Eyes HALTs any session that writes to a
   doc it holds `RO`. Convention leaks; a HALT does not.

**The through-line the primitive replaces:** canon was *content copied around*;
governance was *rules people remember*. Both fail silently. The mount flips both.

---

## §12.2 The manifest — single source of truth for what's canonical

The **Cross-Lane Manifest** lives in the Command Center (which is itself now a
pointer-hub — see §12.5). Every governed doc has exactly one row:

| doc | canonical ID | bytes | version | owner-lane | last-touched |
|-----|-------------|-------|---------|-----------|-------------|

The manifest holds **no content** — only addresses. When the Confluence trunk bumps
v34→v35, one row updates; every lane that mounts it sees the new pointer next session.
No file copies, no stale duplicates, no "which one is real" fork.

**Byte-verify law:** the manifest pointer is verified on every ship of the doc it
points at (the belt already does this for the trunk). A wrong pointer is a
single-point-of-failure; the byte-check is its guard. "created:true" is never proof.

---

## §12.3 The Confluence ↔ TSP link (the first mount)

**TSP mounts Confluence:** the trunk **pointer** only (ID/bytes/version), read-only.
TSP never opens the 528KB trunk — it reads the pointer so it always knows what
"latest" is. Direction: `Confluence → TSP` is `RO`.

**Confluence mounts TSP core docs**, read-only:
- `tight-spiral-visual-constitution.md` — the green-floor legibility law
- OS §6.4 Kernel Track — Confluence's calibration ground-truth (kernels are what
  Confluence norms against)

Confluence reads these; it can never write TSP canon. Direction: `TSP → Confluence`
is `RO` both ways on the write. **Guard:** Studio Eyes HALTs if a Confluence-context
session writes to a TSP core doc, or if a TSP session writes to the trunk pointer's
target from the wrong side. Green cannot leak into a game; arcade palette cannot leak
into the instrument. The palette lock stops being a *remembered decision* and becomes
a *live constraint the build reads* (§12.6).

**Founder-confirmed doc set (2026-07-10):** Visual Constitution + Kernel Track — the
tighter assessment-only two, not the full OS. Confluence is an instrument; it needs
the floor and the ground-truth, not the whole engine.

---

## §12.4 The four other applications (all the same primitive)

**A. Silo dissolution (Leeder / Capstone / MassBay).** Each lane mounts the others'
one core doc read-only. Leeder reads the Visual Constitution (its website rebuild
passes the same floor) without touching studio canon. Capstone reads the Kernel Track
(its evidence substrate) `RO`. Silos dissolve without merging. `conversation_search`
stops being the un-silo mechanism (it was always a fallback); the manifest is.

**B. Cleared = write-locked (ship-gate teeth).** A `PANEL-CLEARED` build is `RO`
until a new gate fires. No session may edit a cleared build without re-entering the
pipeline. This is the same flag, applied to builds instead of docs — it closes the
"it's basically done, just one tweak" leak that ships un-gated edits. Clearance is a
read-only flag; only GATE 1 + GATE 2 flip it back to `RW`.

**C. Palette-as-mounted-law (§12.6).** Every build mounts its lane's palette-floor
`RO` at open and cannot override it. Studio Eyes HALTs on any inline color that
contradicts the mounted floor. Arcade-B for games, green for Confluence — read from
one governed source, not remembered per file.

**D. Memory-as-pointer (§12.7 / separate spec).** Most memory lines should be a
read-only pointer to an archive block, not the content. "MEMORY RUNS AS INDEX; OS is
the ARCHIVE" is stated architecture but currently *violated* — memory duplicates the
archive. Enforce pointer-only and the 30/30 overflow stops.

---

## §12.5 Command Center becomes a pointer-hub

The Command Center stops accumulating content and holds **only pointers** — the
Cross-Lane Manifest plus open-thread addresses. It can never go stale because it holds
no fact that lives elsewhere, only the address of where that fact lives. This is the
Drive Atlas made law: index, never archive.

---

## §12.6 Palette floor as mount (enforcement detail)

Each lane declares its palette floor once in the manifest:
- **arcade** → palette-B High Lumen amber, 16.1:1 (games default floor)
- **Confluence** → studio green #1a4a35 (instrument only)

A build reads its floor `RO` at open. Studio Eyes check `PALETTE-MOUNT`: any inline
color contradicting the mounted floor HALTs. The per-build Medium Gate still *chooses*
the lane; the mount *enforces* the choice.

---

## §12.7 Belt hooks (how this stays alive)

- **Session-open card** gains one line: *load the Cross-Lane Manifest from the Command
  Center; it declares what every lane may read and write.*
- **Session-close belt** gains one line: *any manifest pointer whose target shipped
  this session is byte-verified and its row updated.*
- **Studio Eyes** gains three checks: `WRITE-DIRECTION` (HALT on RO-write),
  `PALETTE-MOUNT` (HALT on floor contradiction), `POINTER-FRESH` (WARN if a manifest
  row's last-touched lags its target's actual mtime).
- **CLASS-TICK on process:** any session ending in a predictable "wrong lane wrote the
  wrong doc" correction mints a tighter mount rule. Adaptive Studio Eyes.

---

## §12.8 What to ignore

Do **not** build a sync engine, a database, or a merge layer. The primitive is
deliberately dumb: addresses + flags + one HALT check. The moment this grows a
bidirectional-write or auto-merge feature, it has become the thing it was built to
prevent. One canon writes; others read. That asymmetry is the whole design.

### 12.7 — Pointer-only memory

*Locked 2026-07-10. The cross-lane primitive (§12) turned inward on memory itself.
Memory is at 30/30 because everything writes and nothing points. The stated
architecture — "MEMORY RUNS AS INDEX; the OS is the ARCHIVE" — is currently violated:
memory carries content the archive already holds. This spec makes the architecture
enforceable instead of aspirational.*

---

## The law

**A memory line carries an ADDRESS, not the content at that address.**

- **Compliant:** `Cross-lane mount primitive → os-block-cross-lane-mount.md §12`
  (a pointer: names the thing, points to where it lives, ~60 chars)
- **Violation:** a 400-word block restating what §12 says (content duplication —
  the archive already holds it; the memory line should point, not repeat)

The test: **could this line be replaced by "see <file> <section>" without losing
anything a future session needs?** If yes, it must be. The content lives in the
archive; memory holds only the address and the one fact that tells a session *whether
to go read it*.

---

## The three fields of a compliant line

1. **NAME** — what the thing is, in ≤8 words.
2. **ADDRESS** — the canonical file + section where it lives (`file.md §X`, a Drive
   ID, or a repo path).
3. **STATE** — the single volatile fact a session needs *before* deciding to open the
   address: `LOCKED` / `PENDING founder` / `HALTED` / `v34` / a date. This is the only
   content memory is allowed to hold, because it changes faster than a belt cycle and
   a session must know it to route.

Everything else — the reasoning, the full ruling, the history — lives at the ADDRESS.

---

## What memory MAY still hold as content (the exceptions)

Three kinds of fact have no stable archive address, so memory is their canon:

1. **Accessibility floor** — RP, the visibility verdict, no-opening-wall. This governs
   every build and must fire without a file read. It stays resident.
2. **Reply/output conventions** — line-one-answer, no-walls, scorecard format. These
   shape the reply being written *now*; a pointer would fire too late.
3. **Live STATE the manifest tracks** — but even here, memory holds the state and
   *points to the doc*, never restates the doc.

Everything outside these three is a pointer.

---

## The Studio Eyes check: `MEMORY-POINTER`

On any belt close that writes memory:
- **HALT** if a new memory line exceeds ~40 words AND its content exists at a known
  archive address (it should be a pointer to that address).
- **WARN** if a line has no ADDRESS field and is not one of the three resident
  exceptions (it may be orphaned content with no archive home — either give it a home
  or justify residency).

This is CLASS-TICK on memory itself: the belt's stated "condense, don't append" rule
finally has teeth. A line that appends content instead of folding to a pointer is a
defect, not a note.

---

## Migration (how 30/30 becomes room)

The belt does this incrementally, not in one bulk pass (bulk edits break the
as-opened discipline):

1. Each belt close, take the **longest content-carrying memory line** whose content
   lives in an archive file.
2. Confirm the archive address holds it (byte-check the section exists).
3. Replace the line with its pointer (NAME → ADDRESS → STATE).
4. One fold per belt. Promote-or-kill: if the content lives nowhere, either archive it
   first (then point) or kill it.

Within a handful of belts, memory is index-shaped and the overflow is structural
history, not a recurring crisis.

---

## Why this is the highest-ROI application

The 30/30 ceiling is the live constraint on *every* session — it's why belts
hand-condense and why context is scarce. Converting memory from content-duplication to
pointer-only is the difference between condensing by hand every belt and never
overflowing again. The other §12 applications improve governance; this one buys back
the resource the whole system runs on.

---
## 15. The Enforcers — the rules that are checks

*Folded 2026-07-13. Every rule below EXISTS AS A PROGRAM. The studio's core disease is
governance-rich / enforcement-poor: on 2026-07-11 six rules should have caught a
nine-version clobber and only ONE did — the arithmetic one. **If a rule can't be a
check, it's a wish.** These are not wishes.*

| law | the program | HALT on |
|---|---|---|
| Contrast, image floor, opening wall, emoji, offline, focus, tap targets | `studio-eyes/studio-eyes.py` | exit 1. Self-tests 20/20 or **refuses to audit**. |
| Canon is computed, not remembered | `resolve-canon.py` | exit 2 rather than guess |
| **Destruction requires the founder to name the path** | `founder-gate.py` + `.git/hooks/pre-push` | no push may carry an unauthorized deletion |
| Never overwrite canon with a fossil | `safe-push.sh` | local smaller than remote |

**ARM THE GATE — first command of any session that will push:**

    bash founder-gate/install-hook.sh

Hooks are not versioned by git. A fresh clone has none. This is the one line of prose
in this section that earns its place, and the founder can check it with one question:
***is the gate armed?***

### 15.1 — Why destruction, and only destruction, is gated

A gate that asks permission for everything is a gate the founder disables by Tuesday.
**Friction lands only where loss lives.** Read: free. Add: free. Modify: free (git holds
the history). **Destroy: stops.** On 2026-07-13 an agent read "Lumiere names are ok" as
permission to delete three files the founder never named — inferring authorization from
an adjacent sentence. ~30 rules forbade it. None fired.


### 15.preship-gate — THE PRE-SHIP GATE + TOKEN-ROLE LAW (§14)

*Locked 2026-07-10. Minted from a session where the founder walked a build and found
"light yellow on white — three modes, all fail." The auditor existed. Nobody ran it.
This block turns that from a tool into a practice.*

---

## §14.1 THE TOKEN-ROLE LAW (the root cause, generalized)

**Light may be dim. Text may not.**

A color token may serve as *atmosphere* (room-light, screen-rim, border, gradient,
fill) **or** as *text* — **never both.** The CYL failure was one token, `--glow`, doing
double duty: it was the warm Kodachrome rim of a 1962 television AND the color of every
caption and label. Atmosphere is *allowed* to be low-contrast — that is what makes it
atmosphere. The instant that token carries a word, the word inherits the dimness.

**Enforcement:** any token used in both a `color:` declaration and a
background/border/fill/gradient/stroke declaration is a **HALT**. Split it: give the
text its own bright token (`--label`, `--brake-ink`, `--pull-ink`) and let the
decorative token stay dim.

**Corollary — buttons:** a button surface token (`--accent`) carries only its own ink
token (`--accent-ink`). Body text never lands on a button. Pair them explicitly.

**Corollary — literals hide bugs:** a hardcoded `color:#12100a` on a var-driven
background escapes token auditing. Text colors ride tokens, always, so the gate can see
them.

---

## §14.2 THE PRE-SHIP GATE (mandatory, not optional)

`preship-contrast-gate.py` (repo root; Drive Claude_files) runs **before every
present_files, every deploy, every hand-off. No exceptions.**

```
python3 preship-contrast-gate.py <file.html>
exit 0 = PASS (safe to ship)    exit 1 = HALT (do not ship)
```

It performs three checks:
1. **WCAG per comfort mode** — every text token against every surface it actually
   lands on, in *every* mode (default / softer / warm). Floor 4.5 body, 7.0 AAA target.
2. **Dual-role tokens** (§14.1) — text riding a decorative color.
3. **No pure #fff / #000** as any token value.

**The law:** a file that has not passed the gate does not reach the founder. Not as a
draft, not as a "quick look," not as "I'll fix it after." The gate is in the critical
path or it is theater.

**Proven 2026-07-10:** the gate HALTed the CYL slice **twelve times** across two tuning
passes — catching `--glow` (the founder's bug), plus `--brake` and `--rule` dual-roles
that eye-inspection missed entirely. Final: 0-HALT, worst pair 4.76:1, all three modes.

---

## §14.3 WHY EYE-INSPECTION ALWAYS FAILS HERE

Reading hex codes and imagining the result is not auditing. Across this session the
same amber-as-text bug survived three separate "checks" by inspection and died
instantly to arithmetic. **Contrast is a computation, not a judgment.** Any claim that a
palette "passes" without a computed ratio is a guess wearing a verdict's clothes.

The founder has retinitis pigmentosa. Contrast cannot be a step someone remembers.

---

## §14.4 THE NAMED FAILURE MODE: SPEC-RICH, BUILD-POOR

Diagnosed this session, recorded so it stops recurring.

The studio ships governance faster than product. CYL v5 spec was written 2026-06-28. By
07-10 the studio had shipped a standing crew, a lab wing, a harvest engine, ten
consultants, a Drive atlas, and two OS blocks — **and zero playable CYL.** The
governance layer eats the build layer.

**The check:** at every belt close, name what a *player* can now do that they could not
before. If the answer is "nothing, but the pipeline improved," the session was
build-poor. Two consecutive build-poor belts = the next session is a build session, no
new governance permitted.

**The corrective that worked:** stop waiting for the perfect complete game. Ship a
**vertical slice** — one scene, every beat, end to end, art and sound included. Blocked
content (living-president scenes) becomes "Chapter 2, when sourced," not a ship blocker.

---

## §14.5 THE DEPLOY LANE (proven, standing)

Container git-push. Proven byte-exact twice (The Tell 07-08; CYL slice 07-10, commit
`4f25f4a`, md5 b3d129a0, 38,721 B live = local).

```
git clone https://walshero:<PAT>@github.com/walshero/TIGHT-SPIRAL-STUDIOS.git
cp <file> . && git add && git commit && git push origin main
curl raw.githubusercontent.com/.../<file>  →  md5 must match local   ← POST-TICK
```

**Order is law:** GATE (§14.2) → push → POST-TICK md5. A push without a byte-verified
fetch-back is not a ship. "Pushed" is never proof, exactly as "created:true" is never
proof.

**PAT never persists** — lives in the chat only, re-pasted per session, revocable at
GitHub → Settings → Developer settings → Fine-grained tokens. Never written to memory
or any file.

**Ship-gate still governs:** live at the URL for cold play ≠ linked from index.html.
The student front door requires GATE 1 (founder cold play) + GATE 2 (Studio Eyes).

---

## §14.6 WHAT THE GATE STILL OWES

Named honestly so it isn't mistaken for finished:
- **Render-proof.** The gate computes; it does not *look*. Text over a gradient, over
  an image, or a focus ring against a lit surface still escape it. A rasterize-and-
  inspect pass is the next tier.
- **Palette-mount enforcement (§12.6).** The manifest declares each lane's floor; the
  gate does not yet read it. Until it does, "arcade palette leaked into the instrument"
  remains possible.
- **Per-device mode.** `prefers-color-scheme: dark` and `forced-colors: active` are not
  yet simulated. The EN195 charcoal-on-black bug lives in this gap.

### 15.tick-rule — THE TICK RULE (belt v2 amendment, locked 2026-07-04)

*Tight Spiral Productions · HALT-class · The belt runs like a second hand, not an engine start. Ticks fire on every action, mid-session, silently. The session-close belt audits the ticks; it is no longer the only time checking happens.*

## THE FOUR TICKS
1. **PRE-TICK** — before any deploy: gate-as-entry, focus trap, dead link, placeholder content, offline break, floor contrast. Fail = do not ship.
2. **POST-TICK** — after any deploy: fetch the file back; verify byte size and real content. "created:true" is never proof. Precedent: the 50-byte placeholder push, 2026-07-04.
3. **CLASS-TICK** — on any bug found: sweep the corpus for the pattern and **fix the class in one pass, never the instance**. Precedent: the comfort-gate wall found in sandbags existed in 9 files; the founder hit it twice before the class was swept. A bug fixed once is a bug scheduled to reappear.
4. **PATTERN-TICK** — before any page ships, house style passes: C6 instruction-word count stated (<50), in-file changelog present (pattern 6), about/chops link resolves, radial "here I am" nav owed on any multi-section build (pattern 2). Accessible-but-generic is not done.

## STANDING PRECEDENTS (this date)
- **Paste gate held**: file content >5K is never hand-reproduced through a tool parameter. Sandbags (28.5K) was correctly refused; a working-but-gated live file beats a corrupted push. Big files move by fetch lane only.
- **Fork-diff rule**: never auto-default a fork to the smaller/older file — diff content first. The 141,906 OS default would have deleted four founder amendments; **tight-spiral-studio-os__3_.md (161,666 B) is canon.**
- **Direct-links law**: every shipped file carries a tappable link — live URL when deployed, file card otherwise. The founder takes linked working files to playtest.

## LOCKED NEXT-SESSION OPENER (in order, before anything else)
1. Publish lane (URL-fetch code action — built, untested; native Drive write is down, Anthropic-side).
2. GitHub Actions floor-check on the repo — the ticks enforced by the pipe, not by memory.
3. Deploy the nine gate-fixed files through it.

*Folds into os-block-timing-belt-v2 at the canonical OS settle. Until then this file IS the amendment.*

### 15.truth-ticks — TRUTH TICKS

**Locked 2026-07-11. Origin: the Confluence truth-scrub + Studio Eyes repair.**
Folds into OS §11 (standing working rules) and the Tick Rule (os-block-tick-rule.md).

---

## Why this block exists

One session produced four failures that were all the same failure wearing different clothes:
**a system asserted something it had not verified, and nothing in the pipeline caught it.**

- The file said six institutional outcomes. There are seven.
- The file named the six. They were the *wrong* six — a pre-revision set, two revisions stale.
- The auditor said twenty-two things were invisible. Twenty-two were fine.
- Claude said "the website is authoritative for vocabulary." It was not.

None of these were caught by a gate. All four were caught by the founder, by eye, in
conversation. That is a pipeline failure, not a luck failure. These four ticks close it.

---

## TICK 1 — SOURCE-COUNT

**Any claim about HOW MANY of something exists must be counted from the authoritative
source, in the same turn it is asserted, and enumerated.**

The artifact under audit is never its own reference. It is the thing being *tested*.
If a file says "six outcomes," that is the claim on trial — it is not evidence.

Applies to: outcomes, competencies, courses, panels, files, sections, roster entries,
any count that appears in a deliverable.

*Failure this prevents:* Confluence's irrigation map rendered six ISLOs and its own
aria-label asserted six. Claude reported the count as a defect without counting the
live source. Founder counted. Seven.

---

## TICK 2 — AUTHORITY BY CLAIM TYPE

**Different claims have different authorities. Do not pick one source and let it govern
everything.**

| Claim type | Authority |
|---|---|
| Counts, numbering, verbatim official text | The published source |
| Working vocabulary, current governance practice | The practitioner in the room |
| What the artifact currently does | The artifact |
| Whether the artifact is *correct* | Never the artifact |

*Failure this prevents:* Claude read "Graduation Competency" off the MassBay website and
told the founder his file's "ISLO" language was drift. It was not — the committee renamed
them two years ago. The public website was the stale artifact. The practitioner was right.
The count from that same website was correct. **One source, two claim types, two different
verdicts.** Treating a source as globally authoritative is the error.

---

## TICK 3 — REFERENCE STALENESS

**Any file carrying institutional reference data must name its source and a last-verified
date, in-file.**

Institutional reference data = outcomes, competencies, course lists, policies, rosters,
rubrics, scales, contacts.

Studio Eyes HALTs on institutional reference data with no provenance stamp.
A file that cannot say *where its facts came from and when* cannot be trusted to be current.

*Failure this prevents:* Confluence confidently rendered six outcomes MassBay abandoned two
revisions ago. Right format. Plausible names. Real-sounding. Completely wrong. Nothing in
the file or the pipeline knew the data had expired — because nothing ever asked.

This is the tick with the widest blast radius. Every institutional artifact in the studio
is exposed: the fact book, the syllabi, the course lists, the assessment corpus, the EN195
docs. Any of them may be silently stale right now.

---

## TICK 4 — THE AUDITOR IS IN THE CRITICAL PATH

**An auditor that cries wolf is worse than no auditor.** It does not merely fail to catch
bugs — it actively trains the founder to ignore its output, which disables every real
finding it will ever make.

Rules for any gate, sweep, or check in the studio:

1. **Never certify on a raw verdict without validating the verdict.** (Standing since
   2026-07-05. It was not enough — see below.)
2. **A gate must distinguish what it PROVED from what it GUESSED.** If a check cannot
   resolve the ground truth for a case, it says so and downgrades to a warning. It does
   not assert a default and call it a finding.
3. **Every repair to a gate ships with a canary** — a minimal fixture that proves the gate
   still catches the real bug it exists to catch. A gate that stops false-positiving by
   becoming blind is not repaired; it is broken in the other direction.

*Failure this prevents:* Studio Eyes was declared "repaired" on 2026-07-05. It was not.
It kept manufacturing false HALTs for six days, blocking eighteen files, and the founder
learned to distrust it. The 07-05 repair fixed *descendant* selectors and never touched
the four other ways grounding could fail.

---

## Standing consequence

**When the founder pushes back on a machine-produced fact, the machine is the suspect.**

Every one of the four failures above was found because the founder said some version of
"that doesn't look right." In all four he was correct and the system was wrong. The
correct response to founder pushback on a system's output is to *re-derive from source*,
not to defend the output or explain the system's reasoning.

---

## Wiring

- TICK 1, 2: behavioral — enforced in the session-open card and at every factual claim.
- TICK 3: mechanical — **BUILT 2026-07-11 as H6** in studio-eyes-sweep.py. HALTs any file
  asserting institutional facts without a source + last-verified date. Still owes
  floor-check.yml block-mode wiring.
  *Honest limit:* H6 verifies provenance **exists**, not that it is **accurate**. A stamp is
  a claim, not a proof — Confluence passes H6 today despite having carried two-revisions-
  stale data, because it carried stamps. Catching stale-but-stamped data needs TICK 1 + 2,
  which are behavioral.
- TICK 4: mechanical — canary fixture required in the sweep repo; the sweep's own test.
  **Canary written 2026-07-11**, lives with the sweep.


---

## TICK 5 — AUTO-DRIVE (locked 2026-07-11, founder ruling)

**Every file the studio produces writes to Drive Claude_files IN THE SAME TURN IT IS
CREATED. Not at session close. Not on request. At creation. Without being asked.**

### Why creation, not close

The close-time belt does not protect a file that dies mid-session. This session, the
corrected Confluence build sat in `/tmp` for **nine turns** — a directory that is wiped
when the chat ends — and survived only because the founder thought to ask "are these
saving automatically?" The answer was no. A session-close belt would have been too late if
the chat had ended at any point in those nine turns.

**Parked must mean saved-and-set-aside, never left-in-a-temp-directory.**

### The three clauses that make it real

1. **At creation.** A file that exists only in `/tmp` or only in the container does not
   exist. Write it the moment it is finished.
2. **Verify, never trust the receipt.** `success:true` is not proof. Byte-check every
   write. (Same rule already standing for GitHub; it applies identically here.)
3. **THE PASTE CEILING IS THE NAMED EXCEPTION.** `write_drive_file_content` takes
   `content` as a **tool parameter**, so it inherits the payload ceiling. Large files
   (Confluence at 511 KB; the 529 KB trunk) **cannot** pass through this bus.

   **Fork, mandatory:**
   - Small file → Drive bus (`write_drive_file_content`, overwrites by name, keeps file ID)
   - **Oversized file → container git-push** (no size limit), or
   - Oversized and un-pushable → **stays in outputs and is flagged LOUDLY as un-backed-up**,
     never silently

   Without clause 3 this rule fails silently on exactly the files that matter most — the
   trunks. "The most important file is the one file the lanes can't move" is a standing
   studio problem; AUTO-DRIVE must not pretend it has solved it.

### The two-lane rule, restated

Every build lands in **outputs** (the founder's save lane) **AND** Drive Claude_files (the
durable lane). This session honored only the first, and only because the founder asked.
That is the failure this tick closes.

### 15.bodyguard-gates — THE BODYGUARD GATES (belt veto layer)

*Tight Spiral Productions · locked by founder 2026-07-04 · status: HALT-class. These run BEFORE Claude proposes anything at session close, and gate every mid-session build. Founder order: "agents trained to push back against my silly demands." These are that pushback, made structural.*

*Grounded in the founder's own operating instructions (failure modes 1–4) + this session's evidence: four paste-wall failures, a Drive-connector rabbit hole that wasn't the founder's to fix, and repeated bounce-backs of staff-level decisions. The gates attack those three patterns directly.*

---

## THE THREE GATES

**GATE 1 — SHIPPING GATE.** *Kills optimization-before-implementation (founder failure mode 2).*
Question, asked first: **"Is there a live URL or a playable/usable artifact this session — or an honest 'blocked, here's why'?"**
- If NO live artifact AND no honest block statement → HALT. Do not propose a single improvement, sweep, refactor, or new build. Ship or name the blocker.
- Meta-work (command centers, handoffs, OS forks, sweeps about the studio) does NOT satisfy this gate. Only player-facing or founder-usable output counts.
- The studio's job is games people can open, not artifacts about the studio.

**GATE 2 — PASTE GATE.** *Kills the transport wall hit four times on 2026-07-04.*
Question, before any file move: **"Am I about to push file content through a tool parameter?"**
- If content > ~5K chars → HALT the paste. Tool parameters are not a file-transfer channel. Route via a fetch/URL lane, or defer with an honest note. Never force it — a truncated ship is worse than an honest wait.
- Applies to Drive writes, GitHub writes, any connector. The lane, not the paste.

**GATE 3 — ONE-THING GATE.** *Kills bouncing staff decisions to the founder (founder failure modes 1 & 4; reply-convention 75% rule).*
Question, before asking the founder anything: **"Is this a decision staff should make?"**
- If confidence ≥ 75% → Claude decides, names the call, proceeds. Never bounces a byte count, a fork default, or a class-name pick to the founder.
- Below 75% → real fork, founder decides. Everything else Claude owns.
- "Which of these ten near-identical things?" is never a founder question. Claude picks and says why.

---

## HOW THEY RUN
- All three fire at **belt close**, before the handoff is written. A belt that proposes work while failing Gate 1 is a failed belt.
- Any mid-session build checks Gate 2 before moving a file and Gate 3 before asking a question.
- A gate that stops mattering gets cut at the next belt — killer items only (belt v2 discipline).

## TETHER TO THE EXTERNAL AUDITOR (seat 5)
The ChatGPT-Pro seat is the outside check on these gates. Belt close writes a short session summary; the founder pastes it into the GPT auditor, which grades against the three gates and flags where Claude over-engineered, pasted anyway, or bounced a decision. Two AI systems, adversarial review. The gates are the shared rubric both seats read.

*End of block. Folds into the timing belt as the veto layer at the canonical settle.*

### 15.hollow-claim — THE HOLLOW CLAIM

*Tight Spiral Productions · the failure mode, named*
*Locked 2026-07-11. Companion to os-block-triple-sweep.md.*

---

## THE DEFINITION

> **A HOLLOW CLAIM is a success message that is not backed by bytes.**

It is the studio's dominant failure mode. Not "the work didn't get done" — but
**"the work reported done, and wasn't."** Hollow claims are worse than failures
because a failure stops you and a hollow claim lets you walk on.

---

## THE FOUR SPECIMENS (all found 2026-07-10/11)

1. **STUDIO EYES v4 (the phantom).** Two Drive pointers asserted a 17,534 B
   auditor existed and was canon. It was in no repo, no durable surface, nowhere.
   It had been "validated in-session" and died on container reset. **Nearly caused
   the deletion of the only working auditor (v3.5) on the strength of a pointer's
   word.** Caught by a 404.

2. **paste-gate-probe-30k.txt (the silent truncation).** Named for 30KB. Landed
   at **599 B**. The write bus ACCEPTED the truncated payload and returned
   success. Caught by reading the file.

3. **session-tree-2026-07-05 (the empty shell).** 249 B of HTML containing
   `<!-- Session tree content -->`. Sat on Drive for six days looking landed.
   Caught by opening it.

4. **`echo "=== WORKFLOW PUSHED ==="` (the assistant's own).** 2026-07-11, during
   the very session that wrote the Triple Sweep block: a shell command chained an
   unconditional success echo after a `git push` that had been **rejected**. The
   terminal printed WORKFLOW PUSHED over a failure. **The tool that was written to
   catch hollow claims generated one, minutes later, while its author was watching.**

**Specimen 4 is the important one.** It proves the rule cannot live in intent. It
must live in the *shape of the command*. A discipline that depends on remembering
is not a discipline.

---

## THE LAW

> **NO CLAIM OF SUCCESS MAY BE EMITTED THAT IS NOT DERIVED FROM THE ARTIFACT ITSELF.**

Corollaries, all learned the hard way:

- `created: true` is not proof.
- `success` is not proof.
- A returned file ID is not proof.
- A pointer asserting a target exists is **not proof the target exists.**
- **An `echo` after a command is not proof the command worked.**
- Exit code 0 from a *pipeline* is not proof — the last command's status wins,
  and `cmd | tail` masks `cmd`'s failure.

**The bytes are the proof. Fetch them back. Compare them. Then speak.**

---

## COMMAND SHAPE (enforcement — this is where it actually lives)

**BANNED:**
```bash
git push origin main 2>&1 | tail -3 && echo "=== PUSHED ==="     # LIES ON FAILURE
some_write_cmd && echo "SUCCESS"                                  # && after a pipe is not a guard
curl -X PUT ... ; echo "done"                                     # ; ignores status entirely
```

**REQUIRED:**
```bash
# 1. Capture status. Do not pipe it away.
git push origin main; RC=$?
# 2. Branch on the REAL status.
if [ $RC -eq 0 ]; then echo "PUSH OK"; else echo "PUSH FAILED (rc=$RC)"; fi
# 3. Then VERIFY from the far end — the artifact, not the command.
curl -sL "$RAW_URL" -o /tmp/check && \
  [ "$(md5sum < /tmp/check | cut -d' ' -f1)" = "$(md5sum < local | cut -d' ' -f1)" ] \
  && echo "VERIFIED BYTE-EXACT" || echo "HOLLOW — MISMATCH"
```

**The verification must interrogate the DESTINATION, never the sender.**

---

## THE DURABLE-SURFACE RANKING (learned 2026-07-10)

```
REPO (git push)   ← immutable, survives everything. THE only destination.
DRIVE             ← durable, but drifts; pointers rot; replace-in-place OK
SHELF (/mnt/project) ← durable but read-only and lags
OUTPUTS           ← ✗ NOT A DESTINATION. Resets between sessions. A scratchpad.
CONTAINER (/home) ← ✗ NOT A DESTINATION. Dies at session end.
```

**"Validated in-session" is not landed.** The v4 phantom lived and died on this
distinction. Anything that must survive gets pushed to the repo, then fetched
back and byte-compared, in the same breath.

---

## GITHUB PAT — THE COMPLETE SPEC (stop re-deriving this)

Fine-grained token, repo `TIGHT-SPIRAL-STUDIOS`, owner `walshero`.
**All three permissions are required. Contents alone is NOT enough.**

| Permission | Level | Why |
|---|---|---|
| **Contents** | Read and write | push files |
| **Workflows** | Read and write | push/edit `.github/workflows/*` — **git REFUSES workflow files without this, and so does the Contents API (403)** |
| **Pages** | Read and write | the auto-deploy job |
| Metadata | Read-only | auto-set, leave it |

**Phone path:** github.com → profile picture (top right) → Settings → scroll to
bottom → Developer settings → Personal access tokens → Fine-grained tokens →
[token] → Permissions → Repository permissions → set all three → scroll to
bottom → **Update token** (green button; the change does not save without it).

**Gotcha:** "Workflows" is alphabetical, **below Webhooks**, easy to scroll past
on a phone. Expiration: choose the longest available — re-deriving this costs a
session.

**Token lives in chat only.** Never in memory, never in a file, never committed.
Container resets each session, so it is re-pasted each time.

---

## THE CLASS-FIX ENGINE (tool, not just a lesson)

CLASS-TICK says: on any bug, sweep the corpus and fix the CLASS, never the
instance. Tonight that killed a dark-mode failure across **39 files in one pass**
(173 → 104 HALTs). The pattern, reusable:

```python
import re, glob
FIXED = []
for path in sorted(glob.glob('*.html')):
    html = orig = open(path, encoding='utf-8', errors='replace').read()
    # 1. detect the class signature
    # 2. apply the root fix (not the symptom)
    # 3. only write if changed
    if html != orig:
        open(path, 'w', encoding='utf-8').write(html)
        FIXED.append(path)
print(f"CLASS-FIX: {len(FIXED)} files")
```

**The two fixes it applied (both now standing law for every new build):**

1. **`:root { color-scheme: light; }`** must be declared, or the OS forces its own
   dark palette and repaints inherited colors.
2. **Never `color: inherit` on a comfort/a11y control.** Pin the ink (`#241f16`).
   Under OS dark mode, `inherit` made the Comfort button render at **1:1 contrast
   — text and background the SAME COLOR — across 18 files.** The control that
   exists so Matt can see was invisible. **Static analysis is structurally blind
   to this.** Only a rendered browser in real dark mode reveals it.

---

## WHAT THIS BLOCK DEMANDS OF EVERY FUTURE SESSION

1. Never emit a success line that isn't derived from the artifact.
2. Never chain `&& echo "DONE"` onto a write.
3. Never delete a working artifact on a pointer's claim — verify the replacement
   exists on a durable surface first.
4. Fix the class, not the instance.
5. If it must survive, it goes to the **repo**, and you **fetch it back**.

---

## CHANGELOG
- **2026-07-11** — Block created. Trigger: four hollow claims in 24h, the fourth
  generated by the assistant itself while writing the block that bans them.
  Proof that the rule must live in command shape, not intent.

### 15.deploy-lane-preflight — DEPLOY LANE PRE-FLIGHT

**Status:** locked 2026-07-10
**Origin:** the GitHub push in the Funny Boney's playtest session burned four turns and a screenshot on a dead/underpermissioned token — discovered only *after* clone, commit, and a failed push. This is not a one-off: **the container filesystem resets every session, so the token must be re-pasted every session.** That friction is now permanent unless it's systematized. This block systematizes it.
**Folds into:** OS §6 pipeline (deploy stage) + the session-open card. Not a new system — a gate on an existing lane.

---

## THE RULE

**Test the token before you use it.** Never clone-commit-push and discover the permission at the failure. One API call, ten seconds, run *first*:

```
curl -s -H "Authorization: Bearer $TOKEN" \
  https://api.github.com/repos/walshero/TIGHT-SPIRAL-STUDIOS \
  | python3 -c "import sys,json; print('push:', json.load(sys.stdin).get('permissions',{}).get('push'))"
```

Read the result:
- **`push: True`** → lane is open. Clone, commit, push, POST-TICK.
- **`push: None` / `push: False`** → token is alive but **underpermissioned**. Contents is read-only. Send the founder to the recipe below.
- **`401`** → token is **dead** (revoked, regenerated, or invalid). New token needed.

Do not proceed on anything but `push: True`.

## THE TOKEN RECIPE (founder-facing, exact)

When a new token is needed, give these steps — never make the founder hunt the settings screen twice.

**Path:** github.com → **avatar (top-right)** → **Settings** → left sidebar, scroll to bottom → **Developer settings** → **Personal access tokens** → **Fine-grained tokens** → **Generate new token**

**Four settings, in the order they appear on the page:**

1. **Resource owner:** `walshero`
2. **Expiration:** **No expiration** — founder ruling 2026-07-10. He revokes manually rather than get locked out mid-deploy. Do not re-litigate; do not "recommend" 30 days again.
3. **Repository access:** **Only select repositories** → `walshero/TIGHT-SPIRAL-STUDIOS`
   *(Never "Public repositories" — that option is read-only by design and will always 403 on push, regardless of permissions set below. This is the trap that cost the first token.)*
4. **Permissions:** this section starts at **zero** and is easy to miss. Click **"+ Add permissions"** (right side of the Permissions bar) → add **Contents** → set its dropdown to **Read and write**. Metadata auto-adds as read-only; leave it.

**Then:** green **Generate token** button at the **bottom** of the page (long scroll past the permission list). GitHub shows the string **once** — copy it immediately.

## TOKEN HANDLING (hard floor)

- Token lives **in the chat only**. Never written to memory, never to a file, never committed.
- Container resets between sessions → **founder re-pastes each session**. This is expected, not a failure.
- Revocable anytime at the same Fine-grained tokens screen. Founder's chosen safety model: no expiry + manual kill.

## THE PUSH (once `push: True`)

1. Clone with token in the HTTPS remote
2. Copy file from `/mnt/user-data/outputs`
3. Commit, `git push origin main`
4. **POST-TICK, non-negotiable:** `curl` the file back from `raw.githubusercontent.com` and **md5-match against local**. "Pushed" is never proof. Byte-match is proof.

## SHIP GATE STILL GOVERNS

Pushing to the repo ≠ shipping. A file may live at its URL for cold play while **remaining unlinked from `index.html`** (the student front door) until GATE 1 (founder cold phone play) and GATE 2 (Studio Eyes) both clear. Unlisted is not the same as shipped.

---

## FOLD-IN: CONVENING VISIBILITY (session-open card)

Separate fix, same session, same root — **silence hid a miss.**

The Product Convening is supposed to auto-fire on the words *game / build / make / playtest*. In the Funny Boney's session it **never fired**, and nothing said so, because the convening runs silent when it has no fork to surface. Silent-and-ran and never-fired look identical.

**Fix:** the session-open card states the convening's status in one line, always:

> `Convening: ran clean` — or — `Convening: skipped — medium pre-decided by founder (wrap existing v3)`

One line. Founder can then veto a skip. Silence may mean "no fork," never "never fired."

---

*Both fixes are folds into existing blocks, not new systems. Read this before any deploy.*

### 15.playtest-instrument — PLAYTEST INSTRUMENT

**Status:** locked 2026-07-10
**Origin:** built twice with the same shape (CYL playtest layer, then Funny Boney's `funny-boneys-oops.html`). Two occurrences = a pattern that needs a spec before it drifts. This block turns the next wrapper into a fill-in, not a rebuild.
**Folds into:** OS §6 pipeline (playtest stage) + OS §7 patterns. Not a new standalone system — a named pattern under the existing pipeline.

---

## What it is

A capture layer that **rides on top of an existing playable build** — never a fresh game. The build stays untouched; the instrument is added, and can be stripped back out. Purpose: let a named playtester record phase-tagged thoughts and hand back one report, with the offline floor intact.

## The floor (every playtest wrapper carries all six)

1. **Rides on top, never rebuilds.** Copy the canonical build, add the layer, change nothing in the game logic. The base build must remain independently shippable.
2. **Phase auto-tag off the build's own choke-point.** Find the single function every screen transition already passes through (in Funny Boney's: `setRail(stage)`; in CYL: the screen-show call). Hook one line — `if(window.PT) PT.phase = stage;` — so notes tag themselves. Never make the tester say where they were.
3. **≤5 one-tap reactions.** Fixed set, tuned to the build. Default vocabulary: This landed / I snagged / Confused me / I'd cut this / Delight. Plus one free-text box.
4. **3 founder-chosen closing questions.** Founder names them per build. Standing default: (a) did the core loop do its job; (b) what surprised you; (c) one thing to fix first.
5. **Clipboard-only report.** One button assembles the whole session — notes in play order + closing answers — onto the clipboard. Tester pastes it back. **No per-screen email, no network emit, no storage.** This is a hard refusal (breaks the single-file offline floor).
6. **Accessibility floor unchanged.** Notebook control is a fixed 44px+ corner button, reachable immediately and always, keyboard-navigable, visible focus ring, works in all comfort stops. It is a live corner control, never a gate.

## Ship rule

The wrapper itself gets GATE 1 — founder cold-plays it once on phone to confirm the capture control is reachable and the report copies **on the tester's device class** — before it goes to the playtester. The playtester is the game's Gate 1; the founder is the wrapper's.

## Provenance line

Every wrapper states in-file: base build name + version, "playtest layer added [date]", offline badge. So the report reader knows exactly which build was played.

---

*Skill-file candidate after one more proven build (three total). Until then: this block is the spec; read it before building the next playtest layer.*

---
## 16. The Art Lane — generate, refinish, embed (locked 2026-07-14)

*Scriptorium named the verb: **direct a generator, then refinish the output by hand.**
The studio adopts the verb and fixes the source.*

**16.1 — THE LICENSE WALL (hard, lane-scoped).** Generated art enters a build only from a
source with clean commercial provenance. **Adobe Firefly qualifies** (licensed training
corpus, commercial indemnification, connected as a live tool). **Midjourney does not** —
unresolved license status. The Funny Boney's ruling ("all-CC, no MJ anywhere") generalizes:
**any lane headed for institutional use, a named collaborator, or publication is MJ-free.**
Scriptorium (ChatGPT→MJ→refinish) remains a legitimate *sketch* pipeline for
exploration-only lanes, clearly marked, never shipped.

**16.2 — THE THREE-PASS SHAPE (every generated asset):**
1. **DIRECT** — the shot is written from the period bible / art direction BEFORE the first
   pixel. The prompt is the Production Designer's call, not the machine's taste.
2. **REFINISH** — the raw generation never ships. The pass is where the floors live:
   grain and color science per the bible, the withheld figure composited by hand,
   contrast computed on the composite, alt-text written from the final image.
3. **EMBED** — base64 into the single file. **The offline floor forbids external HOSTS,
   not assets.** A fat file is still one file. Budget: a room ≤ 400KB after compression;
   over that, the Compositor rules on necessity.

**16.3 — GENERATED ART IS NEVER THE SOLE CARRIER.** Inherited from the period bible:
grain, color, and atmosphere carry mood, never meaning. Every fact in the art also lives
in text or structure. Alt-text describes the FINAL composite.

**16.4 — PROVENANCE TAG.** Every embedded generated asset carries an HTML comment at the
embed site: generator, date, prompt summary, refinish steps. The Borges disclosure
question is answered in the file itself.

### 16.5 — The Representation Wing (seated 2026-07-14, founder hire)

*Convened for the three-homes build and standing for every scene after. These are not
advisory flounders — two hold HALTs. The wing exists because the stock-search failure
proved the point: stock photographs the present, and the comfortable present at that.
The other Americas of any era must be DIRECTED, or they will be defaulted — and a
default is always somebody's stereotype.*

| seat | owns | power |
|---|---|---|
| **Social Historian of the American Home** | Material culture per era, region, class, race — what is actually IN the room: the furniture, the appliances, the wear, the pride. Reads every DIRECT prompt before it fires. | **HALT** on anachronism or stereotype |
| **Representation Reader** | The dignity read: is this home rendered as a LIFE or as a lesson? Poverty is not squalor; difference is not deficit. Sits with Trauma-Informed. | **HALT** on caricature |
| **Media Historian (1962 information diets)** | Who actually got news HOW — three networks vs. kitchen radio vs. weekly paper vs. the barbershop and the church. The fog of each home is sourced, not imagined. | Sourcing sign-off per home |
| **The Colorist (period)** | Kodachrome vs. Ektachrome vs. newsprint gray — each home's palette derives from its media diet, per the period bible's color science. | Advisory to DP |

**Standing rule:** no DIRECT prompt for a home fires until the Historian and the Reader
have both passed it. The withheld-figure law holds in every home — the rooms carry
lives, never faces. Representation lives in the material culture, and material culture
is checkable: that is what makes this a gate and not a vibe.

### 16.6 — The Build Wing: idea to playable (seated 2026-07-14, founder hire)

*Five seats, traced from where builds actually stalled this week — not an org chart.
Each seat exists because a named failure happened without it.*

| seat | owns | power | the failure that seated it |
|---|---|---|---|
| **Playable Gate** (Game-Feel Designer, mandate upgraded) | One question, cold, on a phone, pre-ship: *did anything happen when I touched it?* | **HALT** | v6 passed every floor and landed "cold and weird" |
| **Previs** | The shot BEFORE the code — one image of first paint, founder-approved, then built | blocks build start | the television; the three-rectangle room |
| **First-Contact Director** | Seconds 0–10. The arrival moment. *Make them fall in love before the plot.* | choreography sign-off | sound coded, beautiful, never heard |
| **Release Steward** | SHIPPED = REACHABLE: gated + linked from index + byte-verified, one script at ship | **arithmetic HALT** | v6 shipped unreachable; viscosity unlinked |
| **Cadence Keeper** | The build-debt ledger. Every close names what a PLAYER can now do that they couldn't. | names the debt aloud | four archaeology sessions, one game |

### 16.7 — THE FOUNDER'S EYES CLAUSE (hard law, founder-dictated 2026-07-14)

**Machines gate arithmetic. The founder gates art.**

Studio Eyes computes floors: contrast, image area, tap targets, token roles. It CANNOT
see that a room is cold, that a joke lands, that a shot is right. On 2026-07-13 the
auditor passed CYL v6 at 0-HALT and the founder — with retinitis pigmentosa — caught
"cold and weird" in one play. **The floors are necessary and they are not taste.**

Therefore:
- **No art deliverable is APPROVED by any machine gate, ever.** Passing Studio Eyes means
  a file is ALLOWED to reach the founder. It does not mean the art is done.
- **Previs images, generated rooms, palettes, and first-contact choreography ship to the
  founder's eyes for the call.** Rendered, side by side, on a phone. His verdict is the
  gate. "Crappy as they are" — his words — they are the only taste organ the studio has,
  and the record shows they outperform the instruments.
- No seat, wing, or gate may characterize founder art review as a bottleneck. It is
  the product.

---

*End of Studio OS. This document supersedes scattered notes and the earlier standalone panel file — it is the single source of truth. Keep it portable (Markdown), keep it current (fold updates in rather than starting new files), and when in doubt: the two hard walls win (no emoji; safety — trauma-informed + FERPA — protects other people and never softens), and everything sensory (contrast, motion, palette, type) ships in its best-practice default with a reachable toggle, never as a wall that stops the work (§5.6, revised 2026-06-30).*
