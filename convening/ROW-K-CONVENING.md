# CONVENING — ROW K: DRESS REHEARSAL (review of the shipped build, v16)

Convened 2026-09-19 under OS §6 0.5-A and `claude/INVOKING-THE-STUDIO.md`.
Invocation (founder): *"Conjure all staff with aleph to convene a review session
and SWOT report on this game as is."*

**Out of process until now, and the file says so.** Row K shipped through v16
without a findings file. It predates the 2026-09-17 Convening ruling, so this is
not a grievance against a session — but the gate has been red on this build
since the ruling landed and nobody looked. This file closes that.

SENTENCE: The player stages another character's secret in three moves — an object, a move, a line — and notices that the audience only ever knows what it can see or hear.

Aleph pass of record: run dir `aleph-runs/2026-09-19-row-k-review`, all five
lenses seated inline (no fleet — CLAUDE.md cost discipline, and the 2026-08-07
precedent that an inline panel beats a parallel one). Ledger committed:
**2 blockers, 8 major, 5 minor · 15 new, 0 regressed**. Surface assessed:
`row-k-dress-rehearsal.html` @ v16.

---

## UNION REP ROLL CALL

Caucus ran against the OS benches, the ledger, the convening folder, and the
six standing craft games. Every seat names its method and its scrub-in, or it
does not sit.

- **Coordinator (learning science)** — method: constructive alignment; Mayer on
  load. Scrub-in: whether a hidden rubric can still teach.
- **Stranger (comprehension + RP cold-read)** — method: the accessibility floor
  as arithmetic, first-touch cold read. Scrub-in: keyboard and voice traversal,
  measured not assumed.
- **Osterweil (freedom of play)** — method: the Four Freedoms. Scrub-in: the
  cost of experimenting after v14's scoring change.
- **Aleph (one view of all lanes)** — method: five-lens sweep against
  `aleph-taxonomy.json`, agreement by count. Scrub-in: the ledger commit and
  the harness itself.
- **Studio Voice (founder corpus)** — method: MW corpus as source. Scrub-in:
  the critics' voices and the provenance line.
- **Conductor (anything seen)** — method: screen contract, DARK HOST LAW,
  BACKDROP-AS-ELEMENT, founder canon C7. Scrub-in: image share, measured per
  screen at 390px.
- **Mamet (standing advisory; seated 2026-09-17 in the Row K session — Registrar:
  still not in the OS §5.6 table, carry it at next OS edit)** — method: drama is
  what the character does; evidence at body scale. Scrub-in: whether the card
  bank still honours its own rule.
- **Magpie (seated 2026-09-18 on Reading Lamp)** — method: comparative mechanics
  from shipped commercial games. Scrub-in: the reward loop.
- **Saunders (standing anchor)** — method: the reader's mind steered line by
  line. Scrub-in: the critics as instruction.

GRIEVANCE: none this run. Every seated seat scrubbed in and produced a finding
or an explicit pass.

---

## SEAT: Coordinator

The teaching here is genuinely good and I want to say that before I say the rest.
Three scenes in three emotional registers — fear, bluff, love — running the same
three-slot structure is textbook varied practice, and the INVISIBLE cards are the
common misconception surfaced deliberately rather than stumbled into. Feedback is
immediate from Fran, deferred and reasoned from the critics, and it always says
why. Eight of my twelve keys pass clean.

Two things are wrong and one is contested. SPLIT-ATTENTION is not contested: the
secret is shown on one screen and then judged across three others, so the player
carries the only load-bearing sentence in the game in working memory while doing
the work. That is the founder's own profile taxed at exactly the wrong moment.
Put the fact back on every choice screen.

OUTCOME-UNMAPPED: the competency lives in an HTML comment. EN195 Workshop 3,
Lens 3 is named where only a developer will ever read it, no iSLO is named at
all, and this build sits one join away from the ISLO suite that already owns the
instruments. That join is free and nobody has made it.

Contested: RUBRIC-UNLINKED. I hold that a scored activity must let the learner
know the criteria. I am overruled on the wording and I accept that — see my
dissent below — but I will not sign a claim that hiding the rubric is costless.

SIGNED 2026-09-19

## SEAT: Stranger

I came to this cold with a keyboard and I could not keep my place in it.

Every screen change clears `main` by innerHTML, which destroys the focused
element, and focus falls to `BODY`. Measured twice: entering a scene, and
advancing to Choice 1. Both times `document.activeElement` is BODY. In a
seven-step game that means a keyboard or voice user re-tabs from the top of the
document at every step — past HOME, past BACK, past COMFORT — to get back to
where they already were. This is the single worst thing in the build and it is
about four lines to fix.

Second: there is no authored focus style anywhere on the page. A stylesheet scan
for `:focus` returns nothing. What you get is the UA default, measured at
`outline 1px rgb(16,16,16)` — a one-pixel near-black hairline sitting next to
2px near-black ink borders. The comfort ladder measures every other colour on
this page and does not measure this one.

Third, and smaller: no screen carries a heading. The only `h1` is the persistent
title, so assistive tech gets an empty outline exactly where the player is
standing. `.stepline` already says the right words; it is just a `<p>`.

Everything else in my lane is clean and genuinely well done — contrast at every
stop, the 18px floor, 44px targets, no sideways scroll at 390px, the dark fork.
That is what makes the focus gap conspicuous rather than excusable: this build
is careful everywhere the gate looks, and the gate does not look here.

SIGNED 2026-09-19

## SEAT: Osterweil

Freedom to experiment took a hit in v14 and I do not think it was noticed.

Scoring changed to the most recent staging of a scene rather than the best, and
a TELL now removes three seats. Put those together: a curious student who has a
full house and replays Scene 3 to see what the announced version looks like
loses the 24 seats that scene had earned and nine more on top. Measured in the
gate: 96 to 63. The game punishes the exact behaviour it exists to encourage,
and it does so silently, and the only undo is HOME, which wipes everything.

I am not asking to revert the founder's instruction. Letting performance move
the room live is right and it is the best feel in the build. I am asking for a
floor: score each scene at its best run, keep the live response, and the player
can show the room the bad version without paying for the lesson. One `Math.max`.

Freedom to fail, freedom of effort, freedom of interpretation are otherwise in
good shape. Replay is never blocked, nothing is timed, and the three "wrong"
answers are interesting rather than punished — the critics make being wrong the
funniest part of the game, which is the correct instinct.

SIGNED 2026-09-19

## SEAT: Aleph

Fifteen findings, two blockers, both in the same place: focus. Full ranking is in
`aleph-runs/2026-09-19-row-k-review`, ledger committed, 45 findings now tracked.

Agreement is worth reading. L3 named TEXT-WALL on the choice screens and L4 named
IMAGE-FLOOR across all four; they are the same defect seen from two lenses and
they point at one fix. The choice screens measure **1.6% image**. The verdict
measures 8.7%. Founder canon C7 asks for over 50%. Not one screen clears it. The
hand-drawn pass made the art that exists excellent, and that has been hiding how
little of it there is — three rounds of polish on the seats and the spiral, and
the screen where the player spends most of the game is a paragraph with a hat on.

I also have to report on myself. Synthesising this run marked **30 open findings
on `the-tell.html` as FIXED** — a file nobody opened today. `fixed` was computed
as every ledger entry absent from the run, unscoped by surface, so assessing one
build retired every other build's findings. Committing that would have told the
next session that a surface it never looked at was clean. Funes' rule is that the
ledger forgets nothing; silence about a surface is not evidence about it. Patched
before commit, self-test green, re-run recorded **0 fixed**. The harness has been
wrong in this direction since it was written, which means earlier runs may have
retired findings they had no business retiring — the ledger's `fixed_on` history
is worth an audit that I am not doing in this session.

SIGNED 2026-09-19

## SEAT: Studio Voice

The writing is the best thing here and it is not close. Marge, Dev and Paul are
three actual people — "there are no seats inside a memory," "I gasped at a book,
and I would do it again," "he gave the cat an extension and called it a forecast."
Fran's headset voice carries the whole tutorial without ever sounding like one.
VOICE-NOT-FOUNDER passes with room to spare; nothing in the copy reads machine-
generic, and the v13 Fran edits landed exactly where the founder put them.

Two small things in my lane. The closing craft claim is attributed to "the
workshop" and nothing else — the real lineage (EN195 W3 L3, and the Mamet and
Saunders benches that rebuilt Scene 3) is in an HTML comment the player will
never open. A claim with no source is a rumour; this one is true and deserves its
line.

And the teal. The studio colour appears exactly once in the entire game, as the
registration shadow under the footer spiral. Everywhere else is amber, the three
scene tints, and the curtain rose. The mark reads like a sticker from another
studio. Either drop teal from this build or give it a job — the focus ring the
Stranger is asking for wants a colour and has none, and that would be a tidy
place for it.

SIGNED 2026-09-19

## SEAT: Conductor

I measured instead of looking, and the numbers are the finding. Image share at
390px: choice **1.6%**, verdict **8.7%**, lobby **25.0%**, scene **34.8%**.
Canon C7 is 50%. This build fails its own studio floor on every screen it has.

The reward is also in the wrong place. On the verdict the housebox sits at
`top: 1432px` in an 844px viewport with `scrollY` at 0 — the house updates 1.7
screens below the fold, at the exact instant it changes. The player does not see
the seats arrive. Two rounds of work went into that meter and the moment it pays
is off-camera. Lift it above the critic reactions and the whole loop closes.

The curtain: correct, researched, and now a toll. About three seconds before the
scene is readable, paid again on every entry and every NEXT SCENE, with no way
past. Meaningful the first time, furniture by the fourth. Full performance once
per scene per session, fast haul after — the reduced-motion path already proves
the instant-open state is legible.

Screen contract otherwise holds: DARK HOST LAW forked, BACKDROP-AS-ELEMENT in
place, no sideways scroll, one hand drawing the whole page since v15. The
composition on the scene screen is right since v16 put the curtain first.

SIGNED 2026-09-19

## SEAT: Mamet (advisory)

The cards still obey the rule, which is the main thing. The wedge, the stairwell
door held open, the empty cup, the wrench in the boiler-room door — every SHOW
card is a thing a body does with an object, at a scale the back row can read.
Scene 3 earned its rebuild. "There's weather coming Friday" is the best line in
the game because the man never says the thing and the house knows anyway.

My objection is the form the choice arrives in. The player chooses between three
paragraphs of prose about staging. A game whose entire argument is *show it, do
not announce it* asks the student to read three announcements and pick one. The
cards should carry the staging, not describe it — a small drawing of the wedge,
of the propped door, of the cup. You have a drawing hand now. Use it on the one
screen that is still all telling.

SIGNED 2026-09-19

## SEAT: Magpie (comparative mechanics)

The reward loop is under-built next to what shipped games do with the same idea.
The house is a single accumulator that moves between screens; the player never
watches a seat arrive. Any crowd-sim or approval-meter game — the thing this most
resembles is a stadium filling in a sports management title — makes the arrival
the whole pleasure: seats land one at a time, with a beat, where you are looking.

Cheap version of the same trick, already available here: when the verdict's house
enters view, fill the newly-earned seats in sequence over about 600ms rather than
painting them pre-filled. Nothing new to invent, no new state, and it turns a
static chart into the payoff the game has been building to for three screens. It
also lets a loss be witnessed — people standing up and leaving after a seminar is
a better teacher than any sentence the studio could write.

SIGNED 2026-09-19

## SEAT: Saunders (standing anchor)

The critics are the instruction and they work because they are specific. "The good
can opener. For his own lunch he uses the church key. For the cat, the good one."
That is a reader's mind being steered a line at a time, and a student who reads it
learns more about concrete detail than a rubric would teach them in a semester.

One note in my lane. The three critics always respond in the same order, in the
same slots, with the same structure, and by the third scene the shape is
predictable. Predictable is not fatal — it is a form, and forms help. But the
game has nine reaction slots per scene and uses them identically every time. A
single break in the pattern, once, at the full house, would land hard.

SIGNED 2026-09-19

---

## DISSENTS PRESERVED

**Coordinator dissents on RUBRIC-UNLINKED.** The founder ruled on 2026-09-19 that
the house shows nothing — no count, no key, no note. I agree the ruling produced
the best screen in the build and I would not undo it. My dissent is narrow: the
house *is* the gradebook, and a player who reads the drawing as atmosphere will
never learn that announcing the secret cost them seats, which is the lesson. The
Magpie's fix resolves this without a word of text — let the seats *leave*
visibly, and cause and effect are witnessed instead of explained. I withdraw the
objection if that lands. Studio Voice and Osterweil side with the founder as
written. Recorded, not resolved.

**Osterweil dissents on the v14 most-recent scoring.** Founder instruction was
"let player performance impact gradually," which most-recent scoring serves. The
seat's position is that the instruction is satisfied equally well by a
best-run floor, at no cost to the feel, and that the current rule taxes
curiosity. Founder is the Calibrator; the tie-break is his.

---

## SWOT — ROW K: DRESS REHEARSAL, v16, as it stands

### Strengths
- **The craft argument is airtight and the game never states it.** Three
  registers, one structure, the common misconception (writing interiority for a
  stage) built in as a playable wrong answer rather than a warning. Eight of
  twelve learning keys pass clean.
- **The writing.** Three critics who are three people, and a stage manager who
  teaches without instructing. This is the asset that cannot be copied and it is
  the founder's own hand.
- **The house.** A wordless gradebook that shows instead of telling, in a game
  about showing instead of telling. The form argues the thesis.
- **One drawing hand, page-wide.** Seeded, deterministic, size-scaled, and
  wrapped so a failure degrades to clean geometry rather than a missing icon.
- **A curtain built on physics rather than easing presets.** Stick-slip travel,
  damped hem, no elastic rebound — and a preship gate that asserts it.
- **A real gate.** ~90 checks across two widths, both schemes, and reduced
  motion, which caught two live regressions during this week's work alone.

### Weaknesses
- **Keyboard and voice traversal is broken.** Focus drops to BODY on every
  screen change; no authored focus ring anywhere; no per-screen heading. Two
  blockers and a major, all in one small area, on a build whose founder is
  voice-first. *This is the top of the list.*
- **The build fails its own image floor on all four screens** (1.6 / 8.7 / 25.0 /
  34.8 vs canon 50%). The choice screens — most of the playtime — are prose.
- **The payoff is off-camera.** The house updates 1.7 screens below the fold.
- **Curiosity is taxed.** Most-recent scoring plus a TELL penalty means replaying
  to explore costs earned ground, silently.
- **The competency is in a code comment.** No iSLO, no link to the ISLO suite's
  existing instruments.
- **A COMFORT button that standing canon abolished** (2026-08-29: no walls, no
  comfort button). Row K still asks the player a preference question.

### Opportunities
- **One fix closes three findings.** Card thumbnails on the choice screens
  answer TEXT-WALL, IMAGE-FLOOR and Mamet's objection at once, and the drawing
  hand to make them already exists and is already canon.
- **Seat-arrival animation closes two more** — the Magpie's fix resolves
  GAME-FEEL-DISPLACED and dissolves the Coordinator's rubric dissent without
  adding a word of text.
- **The focus fix is four lines and makes this the studio's reference build for
  keyboard traversal** — then harden the gate with focus tests and every
  surface in the trunk inherits the tooth.
- **The join to the ISLO suite is free.** Row K teaches a competency the suite
  already has an instrument for; naming it makes this assessable, which makes it
  institutionally useful rather than merely good.
- **A harness bug just got fixed that was silently retiring findings across the
  whole corpus.** The ledger's `fixed_on` history is now worth an audit — there
  may be live defects on other surfaces marked clean by earlier runs.

### Threats
- **The gate's blind spot is the real risk, not any single defect.** A ~90-check
  suite that passes everything creates justified confidence, and it does not
  look at focus at all. The build felt finished because the gate said so.
- **Polish is outrunning structure.** Three consecutive rounds went into art
  (spiral, seats, one-hand pass) while two accessibility blockers sat
  unmeasured. The art is excellent; the sequencing was wrong.
- **Canon drift, documented.** COMFORT survives against a standing ruling, Mamet
  is seated in session canon but absent from the OS §5.6 table, and this build
  ran to v16 with no findings file. Each is small; together they are the pattern
  the Convening was created to stop.
- **Ledger trust.** Until the `fixed_on` audit runs, "FIXED" in the ledger means
  less than it should.

### The order the seats would work it
1. Focus: restore focus on transition, author a ring, promote `.stepline` to `h2`.
2. Harden the gate with focus and heading checks, so the trunk inherits it.
3. Card thumbnails on the choice screens.
4. Lift the house on the verdict and let seats arrive one at a time.
5. `Math.max` the per-scene score; the secret strip on choice screens.
6. Name the iSLO; add the provenance line.
7. Founder ruling needed on COMFORT, and on the teal.

---

## FOR THE CALIBRATOR

Nothing above has been authored into the build. Per `INVOKING-THE-STUDIO.md`
step 4, the findings come to the founder first and the tie-break is his — in
particular on the two dissents, on COMFORT, and on whether item 3 is worth the
authoring cost before the semester.

---

## WORKED — 2026-09-19, same session (founder: "Go")

Items 1–6 of the seats' order, authored against the findings above. Second aleph
run recorded at `aleph-runs/2026-09-19-row-k-v17`:
**2 blockers → 0 · 8 major → 1 · 12 fixed · 0 regressed.** Shipped as v17.

| # | Finding | State |
|---|---|---|
| 1 | FOCUS-LOST, FOCUS-INVISIBLE, OUTLINE-BROKEN | **closed** — h2 per screen takes focus on transition; card picks restore focus to the card; ring authored from the ink/paper pair; `aria-live` off `main` |
| 2 | gate blind spot | **closed** — the suite now asserts an authored focus style, a ≥3px ring, a heading per screen, focus never on BODY across the walkthrough, and prints image share |
| 3 | SPLIT-ATTENTION | **closed** — the scene strip carries plate + secret onto the choice and review screens |
| 4 | GAME-FEEL-DISPLACED | **closed** — house lifted under the banner, above the critics; seats arrive in sequence over ~620ms, and leave from the back |
| 5 | FAIL-STATE-PUNITIVE | **closed** — best-run floor per scene; a first bad staging still costs, a restage cannot take back won ground |
| 6 | OUTCOME-UNMAPPED, SOURCE-UNNAMED | **closed** — iSLO 1 / AAC&U Written Communication VALUE, dimension Content Development, named in the build header and here; footer carries the craft lineage |
| — | TEXT-WALL, IMAGE-FLOOR | **open, downgraded** — strip took choice 1.6→14.5% and review 0.9→12.4%; canon C7 is 50%. Remaining fix is Mamet's: a drawing on each of the 27 cards. Authoring job, quoted not guessed |
| — | RUBRIC-UNLINKED | **open at minor** — the Coordinator's condition was met (loss is now witnessed, not explained), criteria still unstated by ruling. Recorded so it is not rediscovered as new |
| 7 | COMFORT, teal | **founder call, untouched** — COMFORT stands against the 2026-08-29 no-walls ruling and the DARK HOST LAW ladder is built on it; teal has no job. The Studio Voice proposed the focus ring as teal's home and measurement killed it (#0F5F5A on the black stop is 2.6:1), so the ring was built from ink on paper |

**Harness note.** `aleph-fleet.py` was patched before the first commit: `fixed` was
every ledger entry absent from a run, unscoped by surface, so this review would
have retired 30 live `the-tell.html` findings it never opened. The ledger's
`fixed_on` history predating 2026-09-19 is therefore **not trustworthy** and
wants an audit — earlier runs may have marked defects clean on surfaces they
never assessed. Not done here; carried.
