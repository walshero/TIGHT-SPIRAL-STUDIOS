# BUILD: CLICHÉ HUNTER (temp name) · 2026-08-27

**Status: LAB.** Playable end to end, gates green, no human has played it. Under
the ladder set today (`claude/RULING-LAB-STATUS-2026-08-27.md`) that is Lab, not
Live, and the build says so on its own face.

## The brief, in the founder's words

> "Kill blocking. It's too light on specs. Poetry game. Let's develop a new game
> called cliche hunter (temp) that has players discover real poems that have some
> lines replaced by cliches. Players must ID. All kinds of license able poems."

Amended the same session:

> "This will not be an action game like previous cliche cowpaths but includes
> substitution like in lure of the labyrinth arcade games. And we want art."

Both rulings are the design, not context for it.

## The move that made the game: the etymology is the mechanic

A cliché is a printing term before it is a criticism. French printers cast a whole
common phrase as one solid plate, so it could be dropped into any form without
setting the letters again, and named it for the sound the matrix made striking the
metal. The English word for the same object is **stereotype**.

That is the entire charge against a worn phrase, and it is not that the phrase is
untrue. It is that the phrase arrived pre-cast, and **would have fit anywhere**.

Once that was the setting, the mechanic stopped needing to be invented:

| the object | the move |
|---|---|
| a stereotype plate in the form | find it |
| pull the plate | you now have an empty channel |
| set type into the channel | choose what belongs **in this poem** |
| take the impression | the press tells you what you set |

The room is a composing shop and the clichés are literally plates in a drawer that
fills as you play. **When a build's subject has a literal object behind it, the
object is usually a better mechanic than anything designed on top of the subject.**

## Not an action game, and the substitution is why

The founder ruled this out of the cowpath family explicitly, and the two halves of
that ruling are one thing. There is no clock, no reflex test, and no fail state.
Every choice is a toggle you can take back until you print.

Identifying a plate is the cheap half. It gets you an empty channel and nothing
else. **The question that teaches is the second one:** of these three lines, which
was written for *this* poem? All three scan. In Teasdale's couplets all three
rhyme. The ear will not settle it, which is the point.

That is the Lure of the Labyrinth shape: you slot values into a system, the system
reacts, and you reason from the reaction rather than from being told.

## Four verdicts, and only one is an error

| what you did | what the press does |
|---|---|
| pulled the plate, set the poet's type back | prints clean |
| pulled the plate, set another plate in | prints in dead grey, and names the real line |
| left the plate in | prints in dead grey: it could have gone in any poem |
| pulled a line that was never a plate | prints struck through, and names what you removed |

Putting a poet's own line straight back where you found it **costs nothing**. The
game is a reading test, not a trap.

## The coined verdict

Two of the real lines in this set are worn to the point of sounding pre-cast:

- Sandburg, *Fog*: "on little cat feet."
- Dickinson: '"Hope" is the thing with feathers'

A student who flags either of those is **right about the wear and wrong about the
source**, and marking that as an error would teach something false. So the game
says the poem is where the phrase comes from, in its own panel, and does not count
it against them. Before 1916 fog did not come on little cat feet. After 1916
everybody's did.

This is the beat the build is proudest of and the one most likely to be wrong in
the room. It is first in the founder-open list for that reason.

## The specimens

Six United States public domain poems, published 1895 to 1923, set exactly as
published and attributed in-file.

| poem | poet | year | why it is in the set |
|---|---|---|---|
| The Red Wheelbarrow | William Carlos Williams | 1923 | the tutorial. Nothing in it is decorated, so a plate is loud |
| Fog | Carl Sandburg | 1916 | one metaphor held for six lines, and the first coined line |
| There Will Come Soft Rains | Sara Teasdale | 1920 | rhymed couplets, so form cannot be the tell |
| In the Desert | Stephen Crane | 1895 | the plate is a sentiment, not a phrase: it tidies the horror up |
| "Hope" is the thing with feathers | Emily Dickinson | 1891 | the hard one, and the second coined line |
| If We Must Die | Claude McKay | 1919 | a sonnet octave. Two plates, both keeping rhyme and meter |

**Poem accuracy was treated as a hard requirement, not a nicety.** A poetry game
that misquotes a poem teaches the misquotation. Short poems were chosen
specifically so they could be carried whole rather than paraphrased, and the
playthrough asserts on exact strings.

The plates are written for this game and have no author, which is the correct way
round: the game asks you to find pre-cast language among live lines, so the dead
language is the part that should not have been written for anything.

## Nothing was reused from the cliché cowpaths

Checked before building rather than after. `cliche-cabinet.html`,
`cliche-city.html`, `cliche-field.html`, `cliche-line.html` and
`cliche-cowpaths.html` all draw from a **business** cliché bank (low-hanging
fruit, move the needle, circle back, paradigm shift). Nothing in it is mountable
for poetry. Those five went to Lab today under the separate ruling.

## Art

Studio-cut, under the art-gate amendment made the same day
(`claude/RULING-STUDIO-CUT-ART-LANE-2026-08-27.md`) and **proved by
`art-execution-gate.py`, not by its own label**. Hand-cut inline SVG, no raster
plates, no generated art, no external hosts.

The composition is not cropped at any width, and that took three tries:

1. First cut sized the stage to a fixed height and sliced. On a phone it read as a
   header stripe at 20% of the frame.
2. Second cut anchored the slice to the bottom edge. Better on a phone, but a
   laptop stage is nearly three times as wide as it is tall, and the crop threw
   away the press, the lamp and the entire wall of cases. The entry read as an
   abstract band.
3. Shipped: the room takes the page's ratio on a phone and sits as a framed
   picture on its own dark ground on a laptop. Nothing is thrown away on any
   screen.

The type on the scene stays the brightest thing in it by construction, which is
what the execution gate measures: brightest paint in the room is the paper stack
at 0.40 relative luminance, and the type sits at 0.87.

## Two defects the build introduced, both caught by gates rather than by eye

Worth naming because the next lift will make them again.

- The comfort kernel was lifted out of `enjambment.html` **by line number**, and
  the slice stopped one line short of the comfort panel's closing `</div>`. The
  panel is `display:none`, so it swallowed the entire game and the page rendered
  as chrome over nothing. `one-thing-gate` caught it by reporting 0% image and no
  invitation on a page whose entry is a full-bleed scene. Lifting markup by line
  number is cheap and exact, and this is its one failure mode: **verify the render,
  never the slice.**
- The lifted chrome arrived wearing the other game's words: a bar labelled
  *Enjambment*, and a motion-stop note about silencing a belt this room does not
  have.

The one-time assembler is deliberately **not** kept in the repo. It splices by
line number, which breaks silently the moment `enjambment.html` moves a line, and
a build tool reading stale coordinates is the failure class documented in
`claude/FINDING-STALE-STATE-CLASS-2026-08-17.md`. The HTML is the canon artifact.

## No panel was convened

Stated rather than implied, per the Union Rep protocol. The founder gave two
rulings in one session and they were specific enough to build from; convening a
bench to re-decide what he had already decided would have spent credit to arrive
where the brief already was. The seats that would have argued this build (a
Poetry seat on the specimen set, a Legibility seat on the scene) were answered by
measurement instead: exact-string assertions on every poem, and the execution
gate on the art.

**Grievance record: none. No seat was seated, so no seat failed to scrub in.**

## Open, and written down rather than remembered

1. Is the substitution step doing the work, or does identifying the plate already
   feel like the whole game?
2. Six poems in one sitting, or a shorter run the student comes back to?
3. Does the coined verdict land as generous, or as a gotcha with a nice
   explanation?
4. Cliché Hunter is a temp name and the room in the build is the Stereotype Room.
   Does the game keep the temp name or take the room's?
5. Does this absorb the cliché cowpath games now that they are in Lab, or do they
   stand as their own bench?

## Verified before shipping

- Full headless playthrough, 44 assertions, all pass: the plate shows and the
  poet's line stays hidden until pulled; the pull is a reversible toggle; three
  slugs are offered per channel with the poet's line among them; the impression
  restores the poem; the tally counts; the drawer keeps the plate; the coined
  verdict fires and does not mark the reader wrong; stanza gaps are not controls;
  all six rounds run to the drawer; the game stays playable in warm dark with
  motion stop on; no page errors anywhere.
- `art-gate` (which runs `art-execution-gate` on the studio-cut claim),
  `preship-gate-v5`, `studio-voice-gate` v1.2: all pass.
- `one-thing-gate`: WARN, no block. One invitation, three controls, four words
  before the first action.
