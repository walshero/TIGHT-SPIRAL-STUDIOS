# Funnybonies v7 PRD · Samorost-register animated storytelling

Tight Spiral Studios · 2026-08-10 · For Claude Design / any Claude build session.
Founder assessment of v6: 3/10, making progress. This PRD defines what 8/10 looks like.
Style register: Samorost (Amanita Design). Learn the register, copy nothing. Same rule as Bonkyard.

## 1. Vision (one sentence)

A small, mostly wordless place where you bat a ball of yarn through a contraption,
trying to amuse a cat who has seen everything, and the room itself feels alive
enough that failing is still worth watching.

## 2. What Samorost does that v6 does not (the gap, named)

v6 is a functional diagram: flat shapes on a blank card, motion by straight-line
transform, story told by caption. Samorost-register means:

1. A PLACE, not a diagram. Ground with texture, a back wall, a window, depth in
   three layers. Props exist because the room is lived in, not because the
   mechanic needs them.
2. AMBIENT LIFE. Something is always moving, quietly: the fish circles its bowl,
   the cat's tail ticks, dust drifts in window light, the yarn shivers when
   touched. The scene breathes even when the player does nothing.
3. CHARACTER ACTING. The cat is the protagonist of every outcome. His eyes track
   the yarn. He has poses, not opacity swaps: asleep, bored, judging, perked,
   delighted, victorious. Reactions have anticipation and follow-through.
4. WORDLESS CAUSALITY. The animation tells the story completely; the caption is
   garnish. A stranger with the sound off and the text hidden should understand
   every outcome.
5. POKE THE WORLD. Tapping things that are not the button does something small
   and funny. Curiosity is always rewarded.
6. CONSEQUENCE THAT LINGERS. Chaos leaves the room changed until the next throw.
   The boom stays fallen. The cat looks at it, then at you.

## 3. Fixed floors (non-negotiable, the belt enforces them)

- Palette: cream, ink, gold, plum, rust, slate-blue water. NO GREEN anywhere.
- No emoji. All art original inline SVG, CC0, hand-drawn in-file.
- Single file, offline, in-memory only, stores nothing.
- Dark kernel: body.dusk and body.night variable flips, plus OS dark media query.
- SVG text renders at 18px or larger on a 390px phone (20+ units at viewBox 360).
- Exactly ONE invitation above the fold. Secondary controls live below the stage.
- 44px+ touch targets, keyboard reachable, visible focus.
- Reduced motion: complete still-state storytelling with full text description.
- No em dashes anywhere in the file, including comments and strings.
- The machine and scene occupy more than half the phone viewport.
- Nothing gets wet. The fish is fine, in every outcome, visibly.

## 4. The scene (three layers, portrait 360x640 or taller)

BACK: interior wall in a deep warm tone. One window, high left, with soft gold
light falling as a visible beam. Outside the window one leaf on a branch,
idly bobbing (the leaf the quips mention: it is doing better than you).
Wall texture: sparse hand-drawn grain lines, a crooked small picture frame.

MID: the contraption. Shelf with paw and yarn, adjustable ramp with visible
pivot hinge and wear marks, boom on its post with a counterweight, stool with
the fishbowl. Every adjustable part looks adjustable: hinges, bolts, a faint
arc showing its travel.

FRONT: floorboards with gaps and a rug edge. Sisyphus on the rug, bottom left.
The humor book face-down near the stool, one page corner lifted, occasionally
fluttering as if a draft touches it.

## 5. Sisyphus rig (the star)

Build the cat as a rigged group: body, head, two ears (independent), two upper
eyelids, two pupils, whiskers, tail in three segments. Named states:

- ASLEEP: eyes closed, tail still, slow 3s breathing loop. Entry state before
  the demo throw wakes him.
- BORED: half lids, pupils follow the yarn wherever it is. Tail tip ticks about
  once per 2.5s. This is the default and the joke; hold it long.
- JUDGING: after a miss. One ear rotates back, lids lower a fraction more,
  a single slow blink. Then back to bored.
- PERKED: on a funny thing. Anticipation dip first (head lowers 2px, 120ms),
  then ears snap up, lids open round, pupils wide, tail curls high. Overshoot
  and settle. Red spark lines beside the head.
- DELIGHTED: perked plus a small front-paw lift and a 4px hop. Used for funny
  things two and three.
- VICTORIOUS: the finale walk. He rises (weight shift back first), walks with a
  4-step gait cycle to the wreckage, bats the yarn ONCE with a real wind-up,
  then sits, wraps his tail around his feet, and slow-blinks at the player.

Pupil tracking rule: pupils lag the yarn position by 80ms and clamp inside the
eye. This single behavior does more acting than any caption.

## 6. Interaction

- One invitation above the fold: the Bat the yarn button.
- Ramp and Boom adjust below the stage, three settings each, as in v6. Each
  adjustment animates the part with a mechanical clunk-settle (rotate past the
  target 3 degrees, return). The part's travel arc flashes faintly so the
  player sees what moving bit by bit means.
- Poke gags (tap targets inside the scene, each 44px+, each idempotent):
  - Fish: darts once around the bowl, one bubble. Cat's pupils flick to it.
  - Cat: one ear swivels toward the tap. He does not otherwise dignify it.
  - Book: opens the humor book overlay (same as the button below the stage).
  - Window leaf: it waves. The cat watches the leaf with more interest than he
    has ever shown the machine. This is a joke about the meter.
  - Yarn at rest: shivers, one strand lifts and settles.
- The humor book: in-scene object opens a two-page spread overlay, paw-written,
  riddling the three funny things. Close control 44px+.

## 7. The three funny things (cutscene beats, wordless-first)

ONE · STRING THAT WALKS AWAY (ramp Medium, boom Level)
Yarn rolls off the ramp foot, lands soft (squash), rolls LEFT across the whole
floor unspooling a visible strand behind it, passes directly in front of the
cat at nose height, exits the rug. Cat: pupils track, head turns following it,
PERKED as the strand tightens and the tail end zips past. Meter rises visibly.

TWO · A FISH, MEETING A GUEST (ramp Steep, boom Up)
Yarn launches off the boom tip, arcs high (stretch on rise, squash at apex is
wrong: keep round at apex, stretch on fall), lands ON the bowl rim and balances
with two decreasing wobbles. Inside, the fish stops mid-circle. Beat of
stillness, THE PAUSE, one second. Fish and yarn face each other. One bubble
rises. Cat DELIGHTED. The fish resumes circling but keeps one eye turned.

THREE · EVERYTHING, FALLING OVER AT ONCE (ramp Steep, boom Down)
Yarn slams the lowered boom. Boom kicks its counterweight loose, rotates hard
past vertical, strikes the stool's front leg. Stool tips in two stages: lean
and hold for 400ms (the lie that it might survive), then commit. The bowl
slides, tips, and lands UPRIGHT on the rug with a bounce; water sloshes but
stays in; the fish spins once, unharmed, visibly fine. The book is knocked
open. Dust puffs at each impact. Cat stands up, DELIGHTED. The wreckage
persists until the next throw resets it, and until then the cat keeps looking
from the wreckage to the player.

FINALE (all three found, meter full)
No text needed until the last line. The room goes quiet, ambient loops pause
for one beat. The cat rises and crosses the floor in a real walk cycle,
bats the yarn once with full wind-up, sits in the middle of everything,
wraps his tail, slow-blinks. Then, and only then, the single closing caption.

## 8. Animation craft standards

- Every action: anticipation, action, overshoot, settle. No straight-line
  single-transform moves for story beats.
- Squash and stretch on the yarn at every landing.
- THE PAUSE before every punchline. The pause is the joke.
- Secondary motion: yarn strand, tail, water surface, dust.
- Ambient loops budget: fish circle 6s, tail tick 2.5s, leaf bob 4s, dust 12s,
  book flutter 9s. All CSS keyframes, all removed under reduced motion.
- Orchestration: JS timeline like v6 (setTimeout beats driving CSS transitions
  and keyframe classes). No external libraries. Target smooth on an iPhone.
- Captions remain in the hand font, one line, dry, and never required for
  comprehension.

## 9. Meter and pacing (unchanged rules, better clothes)

- Interest stays LOW a long time. Misses give 0, occasionally 1.
- Funny things give 20 / 30 / 50 once each. Full only when all three found.
- The meter is drawn in-scene if possible (a wooden gauge on the wall) rather
  than as a UI bar, but the HTML bar is an acceptable fallback and keeps its
  aria label either way.
- Repeat performances of a found funny thing: the cat gives a smaller, fond
  reaction (single ear, brief pupil widen). Never zero, comedy is rewatchable.

## 10. Out of scope for v7

- The kazoo / word / command mnemonic layer. Parked by founder ruling; the
  humor book is its future home. Do not build it. Do not remove the hooks.
- Sound. If added at all it is Web Audio synth, CC0, OFF by default, one
  toggle. Acceptable to ship v7 silent.
- More adjustable parts, scoring variety, levels. v8 candidates.

## 11. Acceptance criteria (ship gates)

1. All belt ticks pass locally before deploy: comfort-gate (day/dusk/night),
   preship-gate-v4 (contrast + 18px SVG render floor + dark promise),
   one-thing-gate (one invitation, control above fold), studio-voice-gate
   (no em dashes), retired-lines, studio-fingers (44px renders), scope-gate.
2. Studio Eyes screenshot checklist, phone 390x844, light and dark:
   entry scene (cat asleep), bored idle with pupils mid-track, each funny
   thing at its peak frame, chaos persistence frame, finale sit.
3. Wordless test: every outcome identifiable from screenshots alone.
4. Reduced-motion pass: every outcome fully told in still-state plus text.
5. The fish is visibly fine in every frame it appears in.
6. Deploy via the Zapier deploy lane to the stable URL, raw-verify bytes,
   confirm the live page serves the new build before reporting done.

## 12. Milestones

- v7.0 THE PLACE: three-layer scene, ambient loops, cat rig with pupil
  tracking, asleep-to-bored opening. Mechanic unchanged from v6.
- v7.1 THE ACTING: full cutscene beats for the three funny things, chaos
  persistence, judging state, poke gags for fish and leaf.
- v7.2 THE FINALE: walk cycle, finale staging, book as in-scene object,
  remaining poke gags, repeat-performance reactions.

Ship each milestone to the same URL. Founder reviews on phone between each.

## 13. Register references (learn, do not copy)

- Samorost / Amanita Design: place-first scenes, wordless causality, ambient
  life, curiosity rewarded. Do not copy their organic photo-collage textures;
  our register stays hand-drawn ink on cream.
- Tom and Jerry blueprint gag: legible schematic comedy.
- Bonkyard: player-arranged contraptions, dry feedback. Style reference only.
- Camus, for the cat.
