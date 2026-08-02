# BONKYARD → FUNNY BONIES — transferable mechanics (reference read)
<!-- 2026-08-02 · the agentic-playtester seat's first REFERENCE report (claude_seat-agentic-playtester.md output contract). Sourced from ONE founder-supplied screenshot of "Bonkyard Hub" (r/Bonkyard, a Reddit/Devvit post: 40 up, 26 comments). Full play pending a local bundle — reddit.com is egress-blocked in-studio. Named "Bonkyard" per the in-game title + the TheOnoir/bonkyard-releases repo; the founder also calls it "Boneyard". -->

## WHAT IT IS (from the frame)
A **physics contraption puzzle** — the *Incredible Machine / Brain It On / Crayon Physics / Bad Piggies* lineage, embedded as a Reddit post. A yellow sticky states the **objective** ("Get the tennis ball into the goal zone"). The player has a **scarce parts inventory** (tray: 1 peg, 1 plank, each count-badged), **places** them on a gridded board, hits the green **PLAY**, and a real **rigid-body simulation** resolves — the ball rolls, ramps tilt, pegs topple — into the **goal zone** (an orange ring) or not. The verb is **build → run → observe → undo → retry.**

## HOW IT WAS (almost certainly) MADE
Evidence + sourced inference (source code not yet readable — repo not enabled in-session):
- **Shell:** Reddit **Devvit Web** — it's a fullscreen interactive Reddit post with native up/downvote + comments as the social layer (no custom scoreboard). Reddit's official game stack is **Devvit + Phaser** (Reddit×Phaser "Games with a Hook" hackathon; the Phaser+Devvit starter template).
- **Physics:** NOT Phaser Arcade (that's axis-aligned, no rotation). The frame shows **arbitrarily-rotated rigid bodies** (a ~30° tilted ramp, a seesaw/lever), **rolling balls**, and **standing pegs that topple** — that requires a **Box2D-family 2D engine**, i.e. **Matter.js** (most likely, pairs natively with Phaser) or planck.js/Rapier.
- **Material-differentiated bodies:** a light **tennis ball** and a separate **bowling ball** glyph imply per-body mass/restitution/friction — the sim models materials, not just shapes.
- **Editor:** place-from-tray, undo, eraser, marquee-select, a palette (theme) and gear (settings) — a lightweight in-post level editor. The **"Hub"** title + Reddit thread imply **UGC**: players build contraption levels and share them as posts; others solve, upvote, discuss.

## THE TRANSFER — what to carry into Funny Bonies

### A. AESTHETIC (this is the fix for "failing on sight")
Funny Bonies fails the splash test; Bonkyard passes it in half a second because of five moves:
1. **Blueprint navy + dotted grid.** The background alone says "buildable sandbox / engineering toy" before a word is read. Instant genre legibility.
2. **Hand-drawn hatched fills** (diagonal pencil-shading on every rigid body). This is the signature: it takes a cold physics sim and makes it a **napkin doodle** — warmth over sterility. Our amber line-art is close; the missing ingredient is the *hatched-fill sketch texture.*
3. **A handwritten objective on a yellow sticky** — one sentence, human, low-intimidation ("someone left you a note"). Contrast our text-dense setup screen. One sticky, one sentence.
4. **One hot accent (orange) against the cool field** — the start arrow, the goal ring, the alert dot. Cool everywhere, warm at the one thing you should look at. Ruthless focal hierarchy.
5. **Affordance hierarchy by colour:** PLAY is the only green (go); tools are quiet translucent grey; parts are colour-coded by type (brown peg / purple plank). The eye is never lost.

### B. PHYSICS & VERB (the "lots here for physics")
6. **Real rigid-body physics** — gravity, rolling, inclines, levers/seesaws, toppling dominoes, collision, material mass. **Funny Bonies' chain-fire is scripted CSS keyframes — a puppet, not a sim.** This is the single biggest steal: make the marble *obey gravity.* It directly answers the Zimmerman/Filament design note ("physics and immediacy of task").
7. **Build → PLAY → observe** as the core loop — tactile, wordless, self-explaining. A player learns the rules by *watching the sim*, not by reading. Funny Bonies could let you **place a gag-element into the machine and watch it physically fire** instead of pick-from-menu.
8. **Scarcity as the difficulty knob.** A fixed, tiny inventory (1 + 1) makes placement a real puzzle. Cheap, elegant, infinitely tunable.
9. **Forgiving iteration** — undo, eraser, instant retry. Low cost to experiment = Cleese's **open mode** (the exact thing our advisory said the Maker score endangered). The physics toy IS open mode; keep it primary.
10. **A clear payoff target** — the orange goal ring. Unambiguous win condition, always on screen.

### C. SOCIAL (a lesson by contrast, not a copy)
11. Bonkyard offloads its entire social layer onto **Reddit's native rails** — upvotes are the score, comments are the discussion, the post is the level. It builds *no* custom scoreboard. **We can't copy this** (Funny Bonies is single-file, offline, no-network), but the lesson is the one our own advisory reached: **don't invent a scoreboard.** Their answer is "let the platform carry it"; our honest answer is the **Ticket / duet** (a human carries it). Same refusal, different wire.

## THE FLOOR CHECK (what fits our studio, what doesn't)
- **Aesthetic (A): all of it applies**, zero conflict. Highest-ROI, lowest-risk borrow — do this first to beat the splash failure.
- **Physics (B): applies, with a feasibility note.** A Box2D-family engine can be **inlined** into our single file: **Matter.js is ~150 KB minified and has zero runtime network needs** — it can live in an inline `<script>`, preserving single-file / offline / nothing-stored. So "real physics" does NOT break our floors. It DOES raise the build cost and the accessibility bar (a physics canvas needs a reduced-motion path + a non-canvas fallback for Clear Reader). Worth a scoped spike, not a blind rewrite.
- **Devvit shell / Reddit social (C): does NOT apply.** We are standalone and offline. Take the engine, leave the platform.

## RECOMMENDED NEXT INCREMENTS (for the founder to rank)
1. **Aesthetic pass (cheap, big):** blueprint-grid background, hatched-fill sketch texture on the machine, a single handwritten sticky objective, one-orange-accent focal discipline. This is the fastest answer to "failing on sight."
2. **Physics spike (medium, transformative):** inline Matter.js, make the existing marble a real gravity body, let the chain fire as a *sim*. Prototype behind a flag; keep the scripted version until the sim clears the reduced-motion + Clear-Reader floors.
3. **Verb shift (later):** place-a-part-and-run, borrowing the build→PLAY→observe loop, if the physics spike earns it.

<!-- MANIFEST: first reference read from the agentic-playtester seat, off one screenshot. Confidence: HIGH on aesthetic + verb (visible directly); HIGH on "real rigid-body engine" (rotated bodies + topple are visible); MEDIUM on the exact engine (Matter.js most likely, unconfirmed until the repo/source is readable). To deepen: enable TheOnoir/bonkyard-releases (read the physics params + confirm the engine) and/or send the Hub, a mid-solve, and a post-solve frame so the playtester can trace the full loop. -->
