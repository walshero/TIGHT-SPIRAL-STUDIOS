# Funnybonies v8 - spec link and re-spine

Tight Spiral Studios · 2026-08-22 · Written before the build, not after.

## Spec this build is made against

`rescued/shelf-2026-07-13/funny-boneys-factory-spec.md` (Funny Boney's Factory, GDD v2,
2026-06-30, panel reviewed). This file exists in the repo. Every claim below cites a
section of it.

## Audience

**Kids, roughly grades 3 to 6, with at least one other real person in the room.**
Not a solo adult reviewer on a phone. That substitution is the named cause of the seven
failed builds (see `STOCK-TAKE-2026-08-12.md` section 3).

## Re-spine

**Old spine (v5 through v7, mine):** bat a ball of yarn through a contraption to amuse a
cat who has seen everything.

**New spine (the GDD's, restored):** kids build Rube Goldberg machines to make people
laugh, survey real people on what landed, and use the gap to redesign.

**What it displaces:** v7 at `/funnybonies/` is replaced, not shelved beside. The stock
take recommended KILL and the founder halted the build. v7 remains in git history at
commit ead9ec0.

**What survives:** the deploy lane, the belt, the animation craft standards from
`PRD-v7.md` section 8, and the three layer scene method. The cat rig survives as a
component in history, not in this build. Nothing else carries.

## What this build is, and is not

This is **Stage 4, the MVP hinge**: the smallest thing that does the named job. It is the
GDD core loop (section 2) with **step 1 moved off the screen and into the room**.

| GDD section 2 loop step | Where it happens in v8 |
|---|---|
| 1. Build a machine, for an audience, never in silence | **On a table, out of household objects.** No editor. |
| 2. Test on people | The kid runs the machine in front of real watchers. |
| 3. Survey what landed | Each watcher takes the phone and marks the beats that got them. |
| 4. Recalibrate | Round two: same machine, changed, new prediction. |
| 5. Share and stack | **Out of scope for v8.** Carry-Out is v9. |

The editor is the expensive half and it is not the construct. Cutting it tests the
construct in an evening instead of weeks.

## Construct (GDD section 3, unchanged and honored)

**Calibration, and only calibration.** The measure is the **delta between the player's
predicted laugh rating and the surveyed actual**. Computed by the app, never typed as a
feeling.

The one distinction the seven failed builds got wrong, stated plainly:

- The **builder's prediction is self report by design.** That is the claim under test.
- The **actual must come from someone else.** Watchers report their own laughs. The
  builder never rates their own machine's success.

There is no hidden correct answer and no oracle. The app knows nothing about what is
funny. It only holds up two numbers the humans produced and shows the distance.

The math: each beat carries a predicted value 0 to 3. Each beat's actual is the fraction
of watchers who marked it, scaled to the same 0 to 3 axis. The gap is the mean absolute
difference across beats. Round two is comparable to round one on that same axis, so
"did you read them better this time" is answerable.

## Floors carried (GDD section 4)

Tier 1 hard walls: no emoji; no dirty data; opt in; trauma informed (a watcher can hand
the phone back having marked nothing, and the app says out loud that this is a real
answer); human in the loop visible. **Nothing is stored.** In memory only, no backend,
no accounts, no analytics. Closing the tab ends it, and the app says so on the entry
screen.

Tier 2 defaults: high contrast shipped on, green free in any structural role, reduced
motion respected, 44px targets, type at 20px with an 18px absolute floor.

## Look (GDD section 4, the deliberate silence)

The GDD forbids inheriting a prior build's look. v8 does not reuse the cream and ink
register from v1 through v7.

**Register: butcher paper and grease pencil, with one hot accent.** The metaphor carries
the teaching: **your guess is drawn in pencil, the real laugh burns in.** On the gap
screen the pencil outline is what you predicted and the hot fill is what actually landed,
so the lesson is a shape before it is a number. Dark mode is the same idea in chalk on
slate.

The entry scene states the thesis wordlessly: a machine sits on a table, and the person
beside it is the one laughing. The laugh belongs to a person, never to the app.

## Out of scope for v8

Carry-Out and stacking (section 2.5), the real world problem layer (section 5), the four
dashboards (section 6), collaboration scoring. All park until the calibration signal
reads clean, per the GDD's own construct discipline.

## Acceptance

1. Belt clean: all mounted ticks pass. **Status: PASS, all 10 ticks, 2026-08-22.**
2. A kid can go from empty screen to a computed gap without an adult reading anything
   aloud to them.
3. The app never claims to know what is funny.
4. Round two is comparable to round one on the same axis.

## The open question v8 exists to answer

Does calibration play work? Put it in front of one kid with three watchers and see
whether the gap screen produces the moment the whole design is betting on: the part they
were proudest of is not the one that landed, and they want to run it again.

If that moment does not happen, no amount of editor solves it, and the four founder
calls in GDD section 6.6 should be made with that knowledge in hand.
