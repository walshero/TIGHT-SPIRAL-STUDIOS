# SPEC — Headwaters (working title) · 2026-11-10

Status: **LAB**, v0.2 (v0.1 built same day). Build: `lab/headwaters.html`.
Source: founder spec given in chat, 2026-11-10. Founder words are quoted; everything else is machine fallback for Matt to edit.
Not Rewilder. Founder: *"It's a new game."* (Rewilder is the Rampage-style smash game, `convening/REWILDER-CONVENING.md`.)

## Founder rulings (primary source)

| # | Ruling | Founder words |
|---|---|---|
| H1 | Marble Madness feel: you are a ball rolling down a mountain. | *"it's like marbled madness, and you're a ball going down the mountain"* |
| H2 | Falling is not always doom: gondolas can catch you and carry you to the tops of other mountains. | *"instead of falling off at the end to your doom ... you have a chance to ... go into these gondolas that bring you back up to the tops of other mountains"* |
| H3 | Ecological purpose: smash power plants and other egregious things, break dams, let rivers flow, restore nature. | *"your job is to smash the power plants and other things on the mountain that are egregious ... allow the rivers to flow, break the dams ... Your job is to restore nature"* |
| H4 | Strategy is route-finding. Paths are not known the first time. Some lead to doom; a gondola catch is luck and does not always happen. | *"the strategy is in where you go, and you don't necessarily know the first time what the paths are ... you can't always fall into the gondola"* |
| H5 | Three balls. Falling without a gondola, the ball disappears. Checkpoints exist. | *"you just disappear ... you only get three balls. And there is there are checkpoints."* |
| H6 | Win a mountain: both conditions, every target smashed AND the landscape restored (river running free top to bottom). | *"Uh, both."* |
| H7 | The marble is always heavy; it never gains weight. Obstacles guard targets. | *"It's always a heavy marble, but sometimes there might be things in the way."* |
| H8 | Some targets take more than one roll down the hill. | *"It might take multiple rolls down a hill to get the target."* |
| H9 | Obstacles are machinery: moving things, triggering levers, turning things on, magnets. | *"it might take triggering levers and turning things on, turning on magnets. All kinds of things"* |
| H10 | Healing shows a little at once, and in full on the next run. | *"You only start to see it a little bit. And then the next run, when you come back, you see it and it's full stage."* |
| H11 | Strategy game, but super beautiful. Art: Studio Ghibli level of care, but distinct. | *"it has to be the same kind of care that goes into Studio Ghibli. But it has to be distinct."* |

## How v0.1 meets each ruling

- **H1** Oblique three-quarter view so downhill runs down a phone screen; the marble rolls under slope gravity; drag anywhere (virtual stick) or arrow keys push it.
- **H2 / H4** Gondola lines run beneath some edges only. Cabins move along the line; a fall is caught only if a cabin is under you when you drop. Elsewhere the drop is doom. Every gondola goes up to the top of the *other* mountain. The bottom station also rides you up.
- **H3** Six targets across two mountains: Kettle Ridge (pylon, power plant, Kettle Dam), Ash Fork (Ash Dam, coal plant, pump jack).
- **H5** Three marbles shown as pips; a lost marble respawns at the mountain's last checkpoint; zero marbles is a restart.
- **H6** Win screen only when all six are down; the final smash brings every slope to full bloom and both rivers run top to bottom. HUD tracks Broken x/6 and Rivers x/2.
- **H7 / H8** Contact always smashes, but each target takes only one hit per run; hit pips show runs remaining (dams 2 and 3, plants 2, pylon and pump jack 1).
- **H9** Kettle Ridge: a gate seals the left ridge (and its power plant) until you roll over a lever on the right ridge, so one run sets up the next. Ash Fork: the coal plant sits up a steep spur; a switch on the main path wakes a magnet that pulls you up it (a very fast run can make it without).
- **H10** A smash greens the ground near it a little and sends up leaves at once; on the next run (respawn or gondola arrival) it is in full bloom, trees leafed out, flowers in. Breaking a dam turns the dry bed below it into flowing water with a current you can ride.
- **H11** Painted terrain (brush dabs, slope lighting, fog-faded cliffs, living trees that grow from snags), layered sky, drifting cloud. Palette chosen for this game; no borrowed Ghibli imagery.

## Modes
One icon-only button, three modes: Light (day), Dark (dusk), Sharp (high contrast: path edges outlined in bright yellow on near-black void). Follows the 2026-10-13 three-modes ruling.

## PENDING (founder calls, not yet made)
- Final title (Headwaters is a working title).
- Audience (EN195? general? younger?).
- Number of mountains and how the gondola network branches beyond two.
- Sound: v0.1 has quiet synth cues scaled to the event (crack small, smash larger, bloom chime, win largest) per the win-state research.

## v0.2, founder playtest 2026-11-10
Founder: *"The messages obscure gameplay 95% of time, graphics are mid, dying is too easy."*
- **Messages:** one short line at the top under the status bar, gone in under two seconds; no message for checkpoints; camera puts the marble a third of the way down so the slope ahead is clear.
- **Dying:** paths 18% wider; a banked lip on every edge; a soft bumper that soaks up sideways speed near a drop unless you are really flying; a small overhang before you fall; three gondola cabins per line and a wider catch. Measured with a scripted random player over 3 minutes, 3 seeds: v0.1 lost all three marbles in about 22 s; v0.2 lost none. A full-speed charge at an edge still goes over.
- **Graphics:** smooth path edges (marching squares) with cliffs painted behind the ground; rivers painted as one continuous ribbon with banks, and moving glints once a river is freed; grass blades, tree shadows, scrub patches so the damaged slopes are not one flat brown; treelines on the far hills; valley mist and a soft vignette.
