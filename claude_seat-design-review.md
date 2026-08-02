# STAFF SEAT — THE DESIGN BENCH
<!-- source: Matt directive 2026-07-19 "Get Eric Zimmerman, filament, no crusts interactive, Apple Arcade into design doc review. We need physics and immediacy of task. David Noonan is PM" | owner: mwalsh | status: seated -->

**Call sign: The Bench.** A standing design-doc review panel, not a one-off. Four external
design lenses sit at the table; a PM runs it. When a build's design doc comes up for review, The
Bench reads it against two standing axes — **physics** and **immediacy of task** — and every note
it makes leaves as a dated, owned check, or is named out loud as a wish. It reviews the *design*,
never the designer. It does not grade a person; it points at what the play is doing and what one
move could do next. (Same rule as the Review Bench for prose: `review-bench.html`.)

## The one sentence
> **The Bench turns "this should feel better" into a check someone owns by a date — or it says
> the word "wish" out loud and files it. A note without a verb and an owner is not a review note;
> it is a mood.**

This is the studio's own diagnosis reused: *rich in rules, thin in enforcers.* A review that
emits adjectives ("juicier," "snappier") and no checks fails the same way an unenforced floor
fails. The Bench's job is to convert taste into teeth.

---

## THE TWO STANDING AXES (the rubric — this is the gate, not a wish)

Matt named the axes on 2026-07-19. Every review runs both, in this order, and each resolves to a
testable question with a yes/no answer, not a vibe.

**1 · PHYSICS — is the world *simulated and felt*, or only implied?**
A machine that is "about to" move is a diagram, not a physics. The test: *does a player watch
cause become effect — weight, contact, consequence — with their own eyes, in motion?* Dashed
"motion hint" arcs are a promise of physics, not physics. Implied motion fails this axis;
one real, eased, watchable run of the chain passes it.

**2 · IMMEDIACY OF TASK — can the hand act in the first second, with no reading?**
The test: *from a cold load, how many seconds and how many taps until the player performs the core
verb?* Naming the task in a headline is not immediacy; a menu you must cross to reach the verb is
not immediacy. Immediacy is the verb reachable on the first screen, on the first touch.

The order is deliberate: physics first, because the felt world is what *makes* the task legible;
immediacy second, because once the world moves, the task is obvious without a sentence.

---

## THE PANEL (four lenses + the PM)

Each lens is a real design tradition, seated for the specific pressure it puts on the two axes.
The characterizations below are grounded, not guessed (sources at foot); where a lens's read is
inference, it says so.

### Eric Zimmerman — *meaningful play*
Co-author, *Rules of Play*. His floor: **meaningful play = a player action met by feedback that
is both *discernible* (you can perceive it) and *integrated* (it changes what comes next).** He
asks one question and does not let it go: *when the player acts, what visibly happens, and does it
matter to the next choice?* A system whose first interaction opens a menu instead of producing a
consequence fails his floor. He is the panel's physics-of-consequence seat.

### Filament Games — *name the verb; learning rides inside the mechanic*
Educational studio (est. 2005). Their method codes a design's intent into **verbs, systems, and
identity** (after Gee), and holds five principles: **engagement, efficacy, usability, beauty,
polish**. Their pressure on us: *what is the core verb, in one word — and is the real system (our
Glass Engine) living inside that verb, or bolted alongside it?* They refuse a design that teaches
in a side-panel what the mechanic should teach in the hand. They are the panel's verb-and-system
seat.

### No Crusts Interactive — *tactile, family-first, charm-in-the-physics*
Family-friendly studio, pun-loving; maker of *Stride & Prejudice* (a physics runner played across
the text of the novel). Their whole move is **instant, tactile physics a child feels on the first
touch**, wrapped in literary charm. Their pressure: *does the thing have weight and give — does it
squash, bounce, and react — and can a kid feel that in one tap, before any words?* They are the
panel's feel-and-touch seat, and the closest lens to Funny Bones' own comedy.

### Apple Arcade — *pick up and play, premium, offline, no wall*
The distribution bar, seated as a lens. Arcade's front door: **understood and playable within
about three seconds, no tutorial, no ads, no IAP, works offline, delightful, family-safe.** Its
pressure: *would this pass the Arcade curation door — is the first screen playable, or is it a
picture of play?* It is the panel's finish-and-immediacy bar. (Funny Bones already meets Arcade's
offline / no-IAP floor: single file, nothing leaves the page.)

### David Noonan — **PM (chair)**
Noonan runs the room; he does not cast a fifth aesthetic vote. His job is mechanical and it is the
seat with teeth:
- **Sets scope:** names the one object under review and the one design doc it is reviewed against.
- **Converts every lens note into a row:** verb + owner + date, or the label **WISH** if it has no
  achievable check this cycle. A note he cannot make into either does not ship.
- **Ranks and cuts:** decides what blocks the next build and what waits; resolves lens
  disagreement; kills scope creep ("full rigid-body physics" is his to name a wish).
- **Files the founder log:** the rulings made in the room, in Matt's words, the day made, into the
  repo — the same close Funes runs.

---

## OUTPUT CONTRACT (what a review must leave behind)

A Bench review is not done when the talking stops. It is done when it has emitted, into the repo:

1. **The object + the doc** it was read against, dated.
2. **A check table:** every note as `verb · owner · date`, or flagged `WISH`.
3. **The convergent ruling** — the one thing all four lenses agreed on (the highest-value fix).
4. **The named wishes** — what was asked for that has no honest check yet, said out loud so it
   cannot masquerade as scheduled work.

No emoji, ever (studio floor). Physics and immediacy answered yes/no, not "improving."

---

## HOW TO CONVENE
- **In any session:** "Take it to The Bench: `<build>`" — the assistant reads the build + its
  design doc and runs both axes through all four lenses, Noonan chairing, emitting the output
  contract above.
- **As a rule:** any build entering design review runs The Bench before it ships a new opening or
  core-loop change. A physics/immediacy claim made *without* convening The Bench is unverified and
  must be marked as such.

---

## INAUGURAL REVIEW — Funny Boney's Factory (cold open + core loop)
*Convened 2026-07-19. Doc of record: `funny-boneys-factory.html` v6 header + spec (`funny-boneys-factory-spec.md` v2). PM: David Noonan.*

**Why this object first:** Matt named the two axes in the same breath as the cold-open rebuild. The
v6 opening (near-square wordless poster, "Make the cat laugh.") cleared the *text-wall* failure —
but it traded a paragraph for a **poster**. The machine is drawn mid-chain and nothing moves; the
task is named but the first tap opens the bench. So the object walks in already failing both axes
Matt called. That is exactly the case The Bench exists to catch.

### The panel's read

| Lens | Axis | The note | Becomes |
|---|---|---|---|
| **Zimmerman** | physics | First interaction (`Step in`) yields a menu, not a consequence — no discernible/integrated feedback on screen one. | **CHECK:** tapping the poster fires **one run of the chain** (marble → bucket → chicken → springboard → cat) before any choice. · build · v-next |
| **Filament** | immediacy | The core verb is **PREDICT** (guess what lands) — but the cold open's implied verb is "watch." Verb is two screens away. | **CHECK:** name the verb `PREDICT` in the doc header (one word), and make the intro tap *ask* "will it land?" so the guess→gap loop starts in second one. · doc + build · v-next |
| **No Crusts** | physics | The chain is stiff line-art; no weight, no give. A kid can't feel it. | **CHECK:** one eased run with squash/stretch on the marble + spring, and a **cat reaction** (ear flick / eye open) on the beat. · build · v-next |
| **Apple Arcade** | immediacy | Clears the no-text-wall bar; fails the "first screen is playable" bar — it's a picture of play. | **CHECK:** poster is **live on load** — a small idle loop + response to first touch. Offline / no-IAP already pass. · build · v-next |

### The convergent ruling (all four lenses agreed)
> **Make the cold open playable in the first second: one tap fires the physics and starts the
> predict loop. The opening should be a *toy*, not a poster of a toy.**
Noonan carries this as the single blocking item for the next Funny Bones build. It satisfies both
axes at once — the tap gives *felt physics* (axis 1) and puts the *verb on the first touch*
(axis 2) — which is why it ranks above every individual note.

### Named wishes (no honest check yet — said out loud, per contract)
- **WISH:** a real rigid-body physics engine for the machine. Not v-next, and not needed — the
  check above delivers *felt* physics with one scripted, eased, tap-triggered run and a cat
  reaction. Noonan names this a wish so "we added physics" can't later mean "we shipped an engine."
- **WISH:** per-audience physics (the machine behaves differently for kids vs. grown-ups). Lovely,
  unscoped, filed.

### What already passed (not everything is a fix)
- No text wall on the opening (v6 cleared it). Offline, single-file, nothing leaves the page
  (Arcade floor). The verb *exists* and is honest (predict, then see the gap) — the note is only
  that it starts too late, not that it is wrong.

<!-- MANIFEST: this doc seats the panel + the two axes + the output contract, and records the first
review. It does not itself implement the Funny Bones checks — those are `build` rows Noonan owns for
the next build. Next: The Bench's first ruling (playable-in-second-one) goes to the funny-boneys
build as the blocking item; re-convene when that build lands to re-run both axes. -->

---
<!-- SOURCES for the lens characterizations (house rule: cite, don't guess), web-verified 2026-07-19:
 - Eric Zimmerman / meaningful play: Salen & Zimmerman, *Rules of Play* (well-established; discernible + integrated feedback).
 - Filament Games: filamentgames.com/about + /blog (verbs-systems-identity after Gee; principles engagement/efficacy/usability/beauty/polish; est. 2005).
 - No Crusts Interactive: noCrusts.com / facebook.com/NoCrusts (family-friendly, puns; *Stride & Prejudice*, physics-on-text).
 - Apple Arcade: platform curation bar (no ads/IAP, offline, pick-up-and-play, family-safe).
 David Noonan = internal PM assignment (Matt directive 2026-07-19); no external characterization. -->
