# SPEC — Headwaters (working title) · 2026-11-10

Status: **LAB**, v0.3 (v0.1 and v0.2 built same day). Build: `lab/headwaters.html`.
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
- Sound: v0.1 has quiet synth cues scaled to the event (crack small, smash larger, bloom chime, win largest) per the win-state research.

## v0.2, founder playtest 2026-11-10
Founder: *"The messages obscure gameplay 95% of time, graphics are mid, dying is too easy."*
- **Messages:** one short line at the top under the status bar, gone in under two seconds; no message for checkpoints; camera puts the marble a third of the way down so the slope ahead is clear.
- **Dying:** paths 18% wider; a banked lip on every edge; a soft bumper that soaks up sideways speed near a drop unless you are really flying; a small overhang before you fall; three gondola cabins per line and a wider catch. Measured with a scripted random player over 3 minutes, 3 seeds: v0.1 lost all three marbles in about 22 s; v0.2 lost none. A full-speed charge at an edge still goes over.
- **Graphics:** smooth path edges (marching squares) with cliffs painted behind the ground; rivers painted as one continuous ribbon with banks, and moving glints once a river is freed; grass blades, tree shadows, scrub patches so the damaged slopes are not one flat brown; treelines on the far hills; valley mist and a soft vignette.

## Founder rulings, voice session 2026-11-10 (primary source)

| # | Ruling | Founder words |
|---|---|---|
| H12 | Falling must stay a threat for reckless play, occasionally. Agreed target: reckless play loses a marble about once a minute; careful play stays safe. | *"Falling should be a threat for a reckless player occasionally ... There should be some element of danger."* |
| H13 | Audience: everybody. The game shows systems properties. | *"I kind of want it to be for everybody ... To show systems properties."* |
| H14 | A working ecosystem with causal chains, including the machinery (magnets and so on). | *"I want it to be a working ecosystem with causal chain based on ... Magnets and all kinds. So yeah, causal chain for sure."* |
| H15 | Ecology from MassBay EV 103 and EV 104: college-level principles, playable at any age. | *"I like to use principles from college level courses so the game should be illustrative of those principles but it should be playable by somebody ... of all ages"* |
| H16 | Five mountains for now. | *"Maybe five for now."* |
| H17 | All mountains interconnected and all reachable; access limited at first and grows. Healing the mountain you are on opens more gondola lines out of it (the founder caught the circular version: a mountain cannot be healthy before you can reach it). | *"there has to be at least a way to get to all of them ... maybe it's limited at first. Maybe you have to grow."* / *"they should all be interconnected."* |
| H18 | Title: Headwaters. | *"Headwaters."* |

## v0.3, built from H12 to H18
- **Five mountains:** Kettle Ridge (dam, power plant, pylon), Ash Fork (dam, coal plant, pump jack), Wren Hollow (sawmill, road culvert; logging truck crosses the path), Fallow Lake (fertilizer silo behind a bridge that a lever lowers, runoff pipe), Larch Crown (highway wall across the main path, diversion pump up a magnet spur; snowplow crosses lower down). 12 targets, 5 rivers.
- **Network:** every mountain has one line out from the start (a ring A to B to C to D to E to A, so all five are reachable). At half healed a second line opens; fully healed opens lines to every mountain. Edge catches and the bottom station use the same network; with more than one line open, the Watershed map asks where to ride.
- **Watershed map** (Map button, bottom rail): the five mountains, how healed each is, whether its river runs, lines open and closed, cross-mountain chains drawn as threads, and every chain found with a one-line why.
- **Chains (11):** river herring run (dam out), herons (one run later), beavers as keystone species (Kettle Ridge whole), clear water below the pump jack (pollution travels downstream), clean rain on Wren Hollow from Ash Fork's coal plant (acid deposition downwind, cross-mountain), brook trout pass (culvert out), forest returns by succession (mill out + clean air), Fallow Lake clears (nutrient runoff and eutrophication), deer cross the ridge (habitat fragmentation and corridors), snowmelt reaches Fallow Lake from Larch Crown (headwaters feed the watershed, cross-mountain), songbirds carry seeds (three healthy mountains). Each shows in the world: fish in the river, herons on the banks, a beaver lodge, deer, birds, the haze lifting, the lake filling and clearing.
- **Win:** all 12 targets down and all 5 rivers running free.
- **Danger, measured:** scripted reckless player (random two-key steering) and careful player (steers back from edges), 60 s per mountain: reckless loses 1.2 marbles a minute on average (Kettle Ridge 0, Ash Fork 3, Wren Hollow 0, Fallow Lake 2, Larch Crown 1); careful loses none.

## EV 103 / EV 104 source status
Confirmed: EV 103 Environmental Studies I and EV 104 Environmental Studies II, 4 credits each, a two-semester lab sequence (MassBay curriculum sheets; WPI's 2025 transfer map counts the pair as BB 1002 Environmental Biology). **Not yet read: the catalog descriptions.** catalog.massbay.edu blocks automated reading and the PDF catalogs reached did not include the course descriptions. The chains above use the standard principles of a two-semester intro environmental science sequence (watershed connectivity, food webs and trophic levels, keystone species, point-source pollution, acid deposition, succession, eutrophication, habitat fragmentation). PENDING: check each chain against the real EV 103 / EV 104 descriptions (paste them in, or open the catalog page in a browser session). The *why* lines are machine fallback for the founder to edit.
