# SPEC: Dunk-O-Rama (Lab) - 2026-11-06

Build: `lab/dunk-o-rama.html`. Status: LAB. Single file, offline.

## Founder words (primary source, verbatim)

v0.1, session of 2026-11-06:
> "I'd like to create a simulation of the carnival dunk tank game. You should he able to pick a cartoon version of a politician etc."
> "Ok, build. Make it fun and make physics a blast. Works like angry birds but you are facing ahead not to right"

v0.2, same session:
> "Instead of a slingshot, let's have a Mickey Mouse hand that you pull back like you're touching the hand and the invisible elbow is the pivot so it snaps forward. The game is too easy, so make the target hanging on two wires and blowing in the breeze. Also, add a breathing rhythm to the player so that the shot line-up indicator fluctuates. Like in metal gear where you need to be calm to snipe."

## Rulings made in the session

- **No real people.** The founder asked to start with a real politician, but the build does not draw real, identifiable people. The cast is four original political archetypes, none tied to a party: The Filibusterer (Sen. Lyle Droneon), The Spin Doctor (Skip Twirl), The Pork-Barrel Mayor (Mayor Bunting), The Lobbyist (Chet Ledger).
- **No licensed characters.** The throwing hand is an original cartoon glove: a cream glove with a striped red carnival cuff on a blue sleeve. It is not a character's glove.

## What v0.2 does

| Element | Behaviour |
|---|---|
| Throw | First-person view facing the tank. Touch anywhere, pull back, let go. The forearm pivots on an elbow below the screen. On release the arm snaps forward, lets go of the ball as it passes rest, then follows through. |
| Aim | Pull right to throw left. Pull down to throw higher and harder. White dots show the first part of the flight. |
| Breath | Aim sways on a 3.6 s breathing cycle. Holding still builds calm, which shrinks the sway; moving the finger costs calm. After 5 s of holding, tremor sets in (SHAKY). A ring around the ball fills as calm builds, with a label: BREATHE, STEADY or SHAKY. |
| Target | Disc hung on two wires from a crossbar. A forced pendulum swings it side to side, and the wires let it twist, which narrows the disc. Breeze is a mix of sines plus random gusts, shown on a wind sock on top of the tank. A hit or a rim clip knocks it swinging. |
| Difficulty | Breeze strength and twist vary by character: Filibusterer 0.5, Spin Doctor 0.7 (twist x2.1), Mayor 0.8 plus wind that also pushes the ball, Lobbyist 1.15 with a smaller disc. |
| Modes | One icon button cycles Dark, Light, Sharp (CLAUDE.md, three modes, one button). Sound is a separate icon toggle. Reduced motion follows the OS setting. |
| Chrome | Studio and Cabinet in the top bar, Back and Home in the bottom rail. Version and LAB chips sit in the h1. |

## Measured in the session (aim bot, perfect solver, held steady before each throw)

- v0.1: every pull was reachable, and the founder called it too easy.
- v0.2, before the breeze bump: Filibusterer 10/10, Lobbyist 4/10. The Filibusterer's breeze was then raised from 0.35 to 0.5. A human has no perfect solver, so human rates run lower.

## Open (founder's call)

- Whether the human hit rate feels right after a phone playtest.
- The carnival scene could later take studio-cut art; the current art is canvas-drawn.

## v0.3 (2026-11-06): the levels teach rhetorical cheats

Founder: "Each level of dunk o Rama should teach a set of critical thinking skills by demonstrating political rhetorical moves, especially the cheats like straw man ad hominem etc. This should be funny but very sharp. Mark Twain is on set writing these characters. Convene political science messaging alephs as needed."

Full record, with seats and sources: `convening/DUNK-O-RAMA-CONVENING.md`. In short: three moves per level (12 in all); every throw opens with a heckle that commits one; from the second throw on, "Call the move" offers three choices. A right call locks the breath steady and makes the target 22% bigger for that throw. A wrong call shows the answer and how to spot it. The round card is a field guide (what it does, spot it, fair version) and closes with a Twain maxim verified in Following the Equator (1897). Test run: 9 calls, 6 right as scripted; no page errors.

## v0.4 (2026-11-06): bigger curriculum, exchanges, no repeats

Founder: "Increase the curriculum and cut the repeats. Make the dialogue richer." Five levels, 20 cheats, 60 crowd-then-politician exchanges, 65 reactions, shuffle bags reset each round. Details in the convening file.

## v0.8 (2026-11-07): the runoff for mayor

Founder: "there should be two politicians in the dunk tank. You can aim at a target to the left of tank, right, and above will dunk both politicians. There can still be double no cheat but usually it's one or the other. Make candidates answer consistently so that this presents a kind of run off. Dryest candidate wins mayor."

Five runoffs (Senator v Skip, Skip v Mayor, Mayor v Chet, Chet v Dale, Dale v Senator), each teaching its level's four moves. 50 questions, 200 answers; each candidate holds one platform throughout. Three targets: left, right, top (both). Driest candidate wins; the card reports cheat counts. Full record: `convening/DUNK-O-RAMA-CONVENING.md`.
