# CONVENING — SANDBAGS (a flash fiction climb)

Convened 2026-09-20 under OS §6 0.5-A and `claude/INVOKING-THE-STUDIO.md`.
Invocation (founder): *"Who is composing the scenes? Those aren't Japanese houses
or a village. In others the street lights look alien. Why are houses in the city?
We need an art director. Give this game the full TSP treatment. Conjure funds and
aleph and run the timing belt."*

SENTENCE: The player drops the words a piece of flash fiction can live without and learns by feel which ones were holding it up — and that the difference is not length, it is load.

Instruments of record, all run this session:
- **art-gate.py** — HALT.
- **studio-belt.sh** — HALT (tick 11 intent; tick 12 registries stale).
- **preship-gate-v4** — HALT (dark palette, type floor).
- **studio-voice-gate** — HALT. **comfort-gate** — pass. **retired-lines** — pass.
  **studio-fingers** — pass.
- **funes-tendrils** — 3 loose ends, 5 lanes blind.
- **aleph** — `aleph-runs/2026-09-20-sandbags`, **4 blockers, 1 major, 2 minor**,
  ledger committed, 54 findings tracked.

**Two gates were blind and are not any more.** `art-execution-gate.py` and the
belt's image-floor tick both reported *"SKIPPED LOUD — playwright absent, this
gate is BLIND. Not a pass."* Python Playwright is now installed and pointed at
the container's existing Chromium, so both see. A gate that cannot run is a gate
that cannot HALT, and this session spent eight versions under two of them.

---

## THE HEADLINE, BEFORE THE SEATS

**Every version of this scenery was composed in a lane that was abolished on
2026-08-01.**

`art-department/CHARTER.md`, opening line: *"Founder ruling, 2026-08-01. Recorded
the day the founder saw hand-drawn SVG scene art one time too many: 'I never want
to again.'"* Then: **"Hand-authored SVG scene art is dead. The check is
`art-gate.py` — wired into safe-push, exit 1 does not ship."**

`art-gate.py` has been in this repo the entire time. Nobody ran it, including me.
It takes four seconds and it says:

```
HALT  sandbags.html
      line 613: 4779 bytes of unprovenance'd inline SVG - hand-authored scene art
```

So the answer to *"who is composing the scenes"* is: a lens with no art brief,
working from memory, in a lane that does not exist. That is also the answer to
why the Japanese village is not Japanese, why there are houses in front of a
downtown skyline, and why the streetlamps match no fixture anyone has stood
under. None of it was referenced. The founder saw in one glance what seven
versions of polish never fixed, because polish was never the missing thing.

---

## UNION REP ROLL CALL

Caucus ran against the OS benches, `art-department/CHARTER.md`, the ledger and
the belt. The Rep's finding is that this build has been running without the
bench that owns its largest surface.

- **Coordinator (learning science)** — method: constructive alignment. Scrub-in:
  whether the build names its spec and its player.
- **Stranger (comprehension + RP cold-read)** — method: the floor as arithmetic.
  Scrub-in: the dark-palette promise, and the type floor in dead CSS.
- **Osterweil (freedom of play)** — method: the Four Freedoms. Scrub-in: the
  keep-cutting change shipped this session.
- **Aleph (one view of all lanes)** — method: five-lens sweep, plus every gate in
  the belt run literally. Scrub-in: the two blind gates.
- **Studio Voice (founder corpus)** — method: MW corpus as source. Scrub-in: the
  why-cards and the voice gate.
- **Conductor (anything seen)** — method: screen contract, DARK HOST LAW.
  Scrub-in: image share and the comfort ladder.
- **ART DIRECTOR (FIRST SEATING on any build — the role is canon in
  `art-department/CHARTER.md` and has never been seated in a convening)** —
  method: owns the shot list; reads the beats, decides what each screen needs,
  writes the brief. **Never draws.** Scrub-in: the shot list this build has
  never had.
- **Period Librarian (art bench)** — method: legal-photo lane, licence verified
  on the source page. Scrub-in: reference for four real places.
- **Colour & Palette Lead (canon, CLAUDE.md — palette is per game)** — method:
  the game's palette serves the game. Scrub-in: the paper drawer.
- **Continuity, the Mad Men seat (art bench)** — method: adversarial audit, names
  each object and dates it. Scrub-in: the anachronism pass nobody has run.
- **Refuter (art bench)** — method: breaks every claim the others make, re-runs
  the gates. Scrub-in: the two gates that were blind.

GRIEVANCE: `ART DIRECTOR seated eleven versions late — the role existed in canon
from 2026-08-01 and no convening had ever seated it.` Recorded against the
process, not a session.

---

## SEAT: Coordinator

The game itself is sound and I want that on the record before the art findings
bury it. A player drops words and learns by feel which ones carry load; the
strike does not shame, the why-card explains, and the piece rewrites itself under
them as they trim. Eleven of my twelve keys pass. The session also fixed the two
real ones — the secret now rides the choice screens, and flying no longer freezes
the draft.

My one open finding is that this build does not know what it is for.
`intent-gate` HALTs: no `spec-source`, no `audience`. That tick exists because
seven wrong Funnybonies builds passed every artifact-quality gate while being the
wrong game for the wrong player, with a reviewed spec sitting unopened in the
trunk the whole time. Sandbags is EN195 Creative Writing and maps to iSLO 1,
Written and Oral Communication — Content Development, the same cell Row K took
yesterday. Neither fact is in the file. Two meta tags close it.

SIGNED 2026-09-20

## SEAT: Stranger

Clean on my floors and I checked them twice, by two different instruments.
Contrast holds at day, dusk and night. Targets pass. Focus is restored on every
tap since this session's accessibility pass, headings exist, nothing renders
under 18px.

Two things the runtime audit could not see and the studio's own gate could.
First, `preship-gate-v4` finds six CSS declarations under the 18px floor — 10,
11, 12, 13, 14 and 16px — every one belonging to the Studio Eyes comfort panel
whose markup was removed under the no-walls ruling and whose stylesheet was
never removed with it. Nothing renders at those sizes. They are a trap for
whoever reuses this sheet, not a live defect, and they should go.

Second and worse: the dark palette is applied by JavaScript. The file declares
`color-scheme: light dark`, which tells the OS not to force-darken, and then
hands over the night tokens only if a script runs. There is no
`@media (prefers-color-scheme: dark)` block at all, so the belt cannot see the
palette and a reader whose script fails gets light tokens on a dark surface.
That is the DARK HOST LAW failure with the promise still attached, which is worse
than not promising. Move it into CSS; keep the attribute as an override.

SIGNED 2026-09-20

## SEAT: Osterweil

Satisfied, and this is the one seat with nothing to add. Liftoff used to freeze
every word the moment the balloon crossed the line, so a piece that flew at eight
bags with six still hanging on it could not be trimmed — the game stopped the
player mid-lesson to tell them they had won. Flying is a state you can enter,
keep trimming inside, and fall back out of. A strut still tears, and tearing one
while up drops you below the line with the words still live so you can climb
back. Undo works at every point. Nothing is timed.

The freedoms are in good order here. My only note is a watching brief: if the
Art Director's shot list turns out to need a longer scene-load, do not let it buy
that time out of the player's first tap.

SIGNED 2026-09-20

## SEAT: Aleph

Seven findings, four of them blockers, and three of the four are the same
failure wearing different clothes: the art lane, the missing provenance, and the
compositions. Full run at `aleph-runs/2026-09-20-sandbags`, ledger committed,
54 findings now tracked.

The part I have to report is about the instruments, not the build. **Two gates
were blind.** `art-execution-gate.py` and the belt's image-floor tick both
printed *"SKIPPED LOUD — playwright absent, this gate is BLIND. Not a pass."* The
belt is honest about it, which is to its credit, but honest blindness is still
blindness and this session ran eight versions of art past two silent gates.
Python Playwright is now installed and pointed at the Chromium already in this
container. Both gates see. `art-execution-gate` reports `no scene marked, not
this gate's business` — which is itself the finding, because a scene that never
declares itself a scene is a scene no art gate will ever grade.

And `art-gate.py` was never blind. It was never run. Four seconds, sitting in the
repo, ready to HALT from the first version. The lesson is not "add a gate"; the
lesson is that a gate nobody invokes is prose.

Funes: three loose ends — one uncommitted tree, nine unmerged commits on the Row
K branch, two orphan pages unlinked from index. Five lanes blind to the sweep.

SIGNED 2026-09-20

## SEAT: Studio Voice

The writing is the founder's own and it is why this game works. Four verbatim
excerpts, used by the author, attributed in-file. The heap copy — "weight this
flight didn't need (it may fly another day)" — and the dignity floor around the
crash are the founder's register exactly.

One HALT in my lane: `studio-voice-gate` catches `H-VOICE-DASH` at line 764, in a
why-card. Those cards are studio craft notes written at the 70 percent tier for
the founder to finish, which is an explanation and not an excuse — a voice ban is
a ban whether or not the line is a placeholder. Either the line loses the
punctuation or the founder finishes the card.

SIGNED 2026-09-20

## SEAT: Conductor

Image share is no longer the problem here; the sky and the manifest carry the
screen. The comfort ladder measures clean at all three stops. My contract holds.

What does not hold is that the largest thing on my screen has no provenance and
no brief. I sign for what is SEEN, and what is seen in this build is four
compositions nobody directed. I defer to the Art Director on the remedy and note
only that whatever replaces them has to survive the same measurement the rest of
the screen does — including on the black stop, where a photographic plate behaves
very differently from flat card.

SIGNED 2026-09-20

## SEAT: Art Director (first seating)

I should have been seated eleven versions ago. Taking the founder's three
questions in order, because each one is a different failure:

**"Those aren't Japanese houses or a village."** Correct. Echigo-Kawaguchi is
deep snow country in Niigata — among the heaviest snowfall of any inhabited place
on earth. That fact determines the architecture entirely: steep gassho or irimoya
pitches to shed load, deep eaves, snow guards, dark stained timber against cream
plaster, often a raised ground floor and a second-storey entrance for winter.
What is on screen is four generic gabled boxes that would sit as comfortably in
Surrey. The torii is worse than wrong — it is placed as decoration in open
ground, when a torii marks an approach and means nothing standing in a field.

**"The street lights look alien."** Also correct, and this is the tell that
nothing was referenced. They are invented shapes. A real fixture is a specific
object with a specific era — a Boston cobrahead on a bracket arm is not a globe
on a post, and neither is what I am looking at.

**"Why are houses in the city?"** Because two settings were composed into one
frame. The piece is a father and child at a neighbourhood curb; the frame has
pitched-roof houses standing in front of a downtown skyline. That is not a style
error, it is a failure to decide what the place is.

The root cause is not skill, it is process: **there was no shot list.** My job is
to read the beats, decide what each screen needs, and write the brief. I never
draw. Nothing further should be drawn on this build until there is a shot list
per scene naming the real place, the era, the light, and the specific objects
that must be in frame — and until the Period Librarian has sourced reference for
all four. Dead Ants is the easiest: Sparr's and the 39 bus are real, in
Roslindale and Jamaica Plain, and the Library of Congress and Boston's own
collections are the first stop.

I am not proposing a lane. That is the founder's ruling and it is in the
decisions section below.

SIGNED 2026-09-20

## SEAT: Colour & Palette Lead

The paper drawer is the one part of the art work I would keep. Eleven fixed
stocks with a face and a shade each, held outside the page tokens so the art does
not repaint when the page does, is the correct structure and it is per-game as
canon requires. The haze-between-layers model for depth is also right: aerial
perspective is haze added, never colour replaced.

My caution for whatever lane wins: a photographic plate does not take a token
palette. If the scenes become photography or traces, the drawer stops governing
the scene and starts governing only the chrome around it, and the per-game
palette ruling will need re-reading for a build whose art is sourced rather than
authored. That is worth deciding before assets land, not after.

SIGNED 2026-09-20

## SEAT: Continuity (the Mad Men seat)

I have nothing to audit yet, and that is my finding. An anachronism pass names
every visible object, dates it, and kills what does not belong. I cannot date an
invented streetlamp. I cannot date a house that is from nowhere.

What I can say now, so the shot list carries it: Dead Ants has real period
anchors and they must be got right rather than approximated. Payphones, the 39
bus, Sparr's — these are datable objects in a datable place, and the piece turns
on the narrator being a specific person on a specific corner. The withholding
rule also stands on every scene: no real faces, ever. Figures read by outline,
posture and prop.

SIGNED 2026-09-20

## SEAT: Refuter

I tried to break the claims above and two did not survive.

The session's own audit script reported "no text under 18px" and that reading was
true but incomplete — it walked rendered nodes only, and `preship-gate-v4` found
six declarations it could never have seen. A bespoke check that agrees with you
is not a second opinion. The studio's gates exist precisely so a session cannot
grade its own homework, and this session graded its own homework for eight
versions.

Second: "contrast is clean" held up under `comfort-gate` at all three stops, but
`preship-gate-v4` additionally flags three token PAIRS that are only safe on
`--card` — `--rust` on `--gold-br` at 2.76, `--slate` on `--accent-strong` at
1.30, `--slate` on `--gold-br` at 3.41. Nothing composes them today. They are
loaded guns in the sheet and the next edit can fire one.

I re-ran `art-gate.py` after the fix to confirm it was not a stale result. Still
HALT. The finding is real.

SIGNED 2026-09-20

---

## DISSENTS PRESERVED

**No dissent on the art findings.** Every seat that touched them agrees: the lane
was abolished, the gate was never run, the compositions were undirected.

**Colour & Palette Lead dissents, narrowly, on the remedy's scope.** If the lane
ruling sends this build to photography, the per-game palette ruling stops
governing the scene art and the seat's authority over this build shrinks to the
chrome. The seat does not object to that outcome; it objects to it happening
silently. Recorded so the next session does not discover it as a surprise.

---

## FOR THE CALIBRATOR — the decisions only you can make

Per `INVOKING-THE-STUDIO.md` step 4, nothing has been authored against these
findings. Four decisions, in the order they block:

1. **The lane, and it governs everything else.** `art-gate.py` names three:
   founder MJ generations (the charter says this lane closed 2026-08-13), verified
   legal photography, or a studio cut PROVED by `art-execution-gate.py`. The
   charter and the gate disagree about how many lanes are open, which is itself a
   canon repair. Which lane does Sandbags use?
2. **Does the hand-authored art come out now or stay until its replacement
   lands?** It ships today against a standing HALT. Leaving it is a known
   violation; pulling it leaves the game with an empty sky for a while.
3. **The Art Director seat** — first-seated here, and the Registrar will want it
   carried into the OS §5.6 table rather than living only in the art charter and
   this file.
4. **The why-card voice HALT** — you finish the card, or I strip the punctuation.

Cheap and unblocked whatever you decide on the art: the dark palette into a real
media query, the two intent meta tags, the dead comfort-panel CSS out. Say the
word and those three go in without touching a pixel.

---

## FOUNDER RULING, 2026-09-20: "No MJ."

That settles decision 1. The lane is **studio-cut, proved by
`art-execution-gate.py`**, which is the 2026-08-13 ruling's own lane: "we can do
better than we have so far with proper execution," made checkable. Hand-built
is permitted when it is MARKED and it EARNS the pass. It was never marked and
never graded. Now it is both: `data-art-class="studio-cut"` on the scenery and
the balloon, `data-scene` on the sky, and both gates run green.

Decision 4 was taken as the belt required: the voice gate is a flat em-dash ban
of 2026-08-05 and this file predates it. Seventy-three went, including the ones
this session added as `—` escapes that the gate could not see and the rule
still covered.

## THE SHOT LIST — Art Director, first deliverable

Each scene names the real place, the era, the light, and the objects that must
be in frame. Nothing below is from memory; the reference the Period Librarian
found is cited. Figures, where they appear, read by outline and posture only.
No faces, ever.

### Scene 0 — Ramen at Echigo Kawaguchi
**Place.** A snow-country station town, Kawaguchi, Niigata. Among the heaviest
inhabited snowfall on earth, and the architecture is built for it whatever the
season. **Season/light.** Heavy rain, grey, mid-afternoon; the piece is rain from
first word to last. **Must be in frame.**
- Roofs pitched 60° and steeper, deep eaves, dark tile or thatch. Nothing shallower.
- Dark stained timber frame with pale plaster infill.
- A **gangi**: the covered wooden arcade that runs along the street front of a
  Niigata town so you can walk under three metres of snow. This is the single
  most Niigata object there is and it was absent.
- The noodle shop, with a noren over the door and one lit window holding the
  plastic ramen display, because that is the image the piece turns on.
- Villagers under umbrellas, by outline.
- Rain. Uonuma hills behind.
- **Not in frame:** a torii. It marks an approach and means nothing in a field.
*Reference:* [Snow Country Buildings, Tokamachi](https://snowrich-tokamachi.com/en/architecture.html); [Shirakawa Village, gassho architecture](https://www.vill.shirakawa.lg.jp/2687.htm); [Historic Villages of Shirakawa-go and Gokayama](https://en.wikipedia.org/wiki/Historic_Villages_of_Shirakawa-g%C5%8D_and_Gokayama).

### Scene 1 — Black Spots on the Crosswalk
**Place.** A Massachusetts residential street. **Era.** The narrator's
childhood, so late 1970s. **Light.** Ordinary bright morning. **Must be in frame.**
- **Triple-deckers**: three stacked porches, flat or low-hip roof, clapboard,
  bay windows. The Massachusetts vernacular, and the answer to "why are there
  houses in the city" is that this is not the city. It is Dorchester or Somerville.
- A wooden utility pole carrying a **cobrahead** on a bracket arm, and the wires.
- **Granite curb**, which is what Massachusetts curbs are made of.
- The crosswalk, ladder-style painted bars.
- The black spots, which are flattened gum.
- One period sedan, boxy, at the curb.
- **Not in frame:** a downtown skyline, shopfronts, awnings. Two settings in one
  frame was the error.
*Reference:* [Boston's triple-deckers, Boston Preservation Alliance](https://www.bostonpreservation.org/news-item/short-history-bostons-triple-deckers); [Three-decker house](https://en.wikipedia.org/wiki/Three-decker_(house)).

### Scene 2 — Peach Cobbler
**Place.** Two adjacent houses on a suburban Massachusetts street. **Era.**
Contemporary. **Light.** Late golden afternoon; the walk to the neighbour's door.
**Must be in frame.**
- Two New England houses: a **cape** (storey and a half, dormers) for the
  narrator, a **colonial** (two full storeys) for the neighbours. Clapboard,
  shutters, brick chimneys.
- The **bulkhead**: angled steel double doors over a stairwell at the foundation
  of his house. He was made to sleep beside it. It has to be a real bulkhead.
- The fence between them.
- The kids' toys in the yard, since the piece says they want them back.
- The neighbours' house lit, with a porch light. His dark.
- Lawn, a tree, a mailbox.
*Reference:* [Bulkhead and cellar door, Northeast New England](https://www.groundworks.com/resources/bulkhead-and-cellar-door-replacement-in-northeast-new-england/); [cellar door vs bulkhead](https://www.ecospect.com/faqs/whats-the-difference-between-cellar-door-and-bulkhead-door).

### Scene 3 — Dead Ants
**Place.** Centre Street, Jamaica Plain, at a 39 bus stop. **Era.** Payphones,
so the 1990s. **Light.** Night; sodium glow. **Must be in frame.**
- **Low-rise brick storefronts**, two and three storeys, cornices, shop windows.
  Centre Street is not a downtown and the tall blocks were wrong.
- Triple-deckers behind and beside.
- An MBTA bus stop sign on a pole.
- Two **payphones** of the 1990s pedestal kiosk type, not booths.
- A cobrahead streetlight on a pole.
- Brick sidewalk, which Jamaica Plain has.
- One ant on the pavement, small.
- **Open question for the founder:** "Sparr's." The Period Librarian could not
  verify a business by that name on Centre Street. Hardware City at 656 Centre
  is real and so is the 39. The name is the founder's memory and stays in the
  text untouched; the question is only whether a shopfront in frame should
  carry it, and that is his call.
*Reference:* [MBTA Route 39](https://www.mbtainfo.com/39); [Forest Hills station](https://en.wikipedia.org/wiki/Forest_Hills_station_(MBTA)); [Hardware City, 656 Centre St](https://www.yelp.com/biz/hardware-city-jamaica-plain-2).

## AUTHORED, 2026-09-20: the four scenes rebuilt to the shot list

**What was built.** The `SCENERY` array in `sandbags.html` was rebuilt from the
shot list above, object by object. Each object is a named generator in the
source (`decker`, `gangi`, `noren`, `brolly`, `pole`, `sedan`, `curb`,
`brickwalk`, `cape`, `colonial`, `bulkhead`, `shop`, `payphone`, `busstop`),
so the shot list can be checked against the code by name rather than by eye.

- **Scene 0, Kawaguchi.** Uonuma ridges with terrace lines; a gassho farmhouse
  and three 60-degree gables up the slope in dark timber over plaster with a
  koshi lattice on the lower wall; a gangi arcade the full width of the street
  with the noodle shop under it, noren over the door, one lit window holding
  three bowls of plastic ramen, a red lantern; four villagers under umbrellas,
  outline only; rain. No torii.
- **Scene 1, the crosswalk.** Four triple-deckers in the middle ground and two
  behind, each with three stacked porches, balusters, a projecting bay and a
  cornice; a wooden pole with crossarm and cobrahead; wires; a boxy sedan at
  the far curb; granite curbs, near and far, with joints; a ladder crosswalk
  with six flattened gum spots on its bars. Nothing downtown.
- **Scene 2, Peach Cobbler.** A cape with two dormers and a chimney, every
  window dark, shutters closed, a steel bulkhead at the foot of its wall; a
  colonial with eight lit windows, shutters, a door and a porch light; the
  picket fence between; a ball, a toy truck and a bat on his lawn; a mailbox
  with its flag up; a tree. Golden light from the sky tokens, not the paper.
- **Scene 3, Centre Street.** Six low-rise brick storefronts, one to three
  storeys, cornices, sign bands, lit shop windows, a few lit rooms above;
  triple-deckers behind; a cobrahead on a pole throwing a sodium pool on the
  road; wires; brick sidewalks with joint lines and granite curbs; two pedestal
  payphones; the MBTA stop sign as a white plate with a black roundel, no
  lettering; one ant. No Sparr's sign, per the open question.

**What else changed in the pass.** Aerial haze is now a vertical gradient
rather than a flat sheet, which removes the hard line the sheet drew across
the sky where the diorama began. Seven sheets were added to the paper drawer
(white, brick, granite, timber, indigo, gold, each with its shade). The OS dark
palette is now written to `:root` inside the media query, with an explicit
`html[data-light="day"]` rule repeating the day tokens so a player who picks
day on a dark phone gets day; preship-gate-v4 could not see the previous
`:not()` selector and was reporting the page as having no dark palette. The
Studio Eyes wordmark was 16px and is now 18px.

**Belt, on the rebuilt file.** art-gate pass; art-execution-gate SHIP;
preship-gate-v4 SHIP, worst pair 7.47; studio-voice-gate SHIP; intent-gate
clean; comfort-gate pass in day, dusk and night; convening-gate pass. Zero em
dashes, zero emoji. Rendered at 390 wide in both OS schemes; boot on a dark
phone lands on night tokens, an explicit day choice lands on day.

**Still open for the founder.** Whether a shopfront in scene 3 carries the
name Sparr's. The Art Director seat's line in the OS section 5.6 table. The
charter and art-gate disagreement over whether the Midjourney lane is closed.

SIGNED: Art Director, Compositor, Continuity, Refuter (measured the belt, not
the author's word for it), Studio Voice.

## AUTHORED, 2026-09-20, second pass: founder's Echigo notes

**Founder:** "Lines in Echigo houses overlap and look weird. Umbrellas are
nice touches, but Lumino would have kimonoed villagers."

**Root causes found.** Two, and only one of them was the gable.
1. The gable generator laid a second roof plane over the face of the gable,
   a band twelve units wide along each edge. Real gables show one receding
   slope and a pair of bargeboards. Rebuilt that way; the cape's dormers get
   the same fix for free.
2. The cut-edge rule in the stylesheet (`#scenery .ly3 *{stroke:...}`) beats
   any `stroke` attribute, so every line in every scene was being restyled
   into a translucent warm-white edge: the rain was invisible, the wires in
   the crosswalk and Centre Street scenes were ghosts, the bat on the lawn was
   white. Lines now set their stroke inline through one helper, `ln()`.
   Refuter's note: this was in the file for two passes and no gate measures
   it. A stroke-integrity tooth belongs in art-execution-gate.

**Villagers.** Four figures in kimono under wagasa, by outline and posture:
robe widening to the hem, hanging sleeves, obi, collar, head as a circle, a
shallow ribbed umbrella with a finial. Each in a different robe, obi and
umbrella from the paper drawer. Scaled to stand under the gangi rather than
over it, because a miniature is honest about height or it is not a miniature.
No faces. Wet-street reflection added under the noodle shop's window.

**Belt.** All six gates pass again; preship worst pair 7.47.
SIGNED: Art Director, Compositor, Refuter, Studio Voice.

## SHOT LIST, REVISED 2026-09-20: founder's corrections to scenes 1 and 3

**Founder:** "Black Spots is on the way to the hospital so it's urban.
Redesign for Longwood Avenue Boston feel. The Dead Ants one is too large for
the scene. We need a bus stop and a pay phone and bench."

### Scene 1, revised: Longwood Avenue
**Place.** Longwood Avenue, the Longwood Medical Area, on the walk to the
hospital. The Art Director's residential reading was wrong; the piece is
urban and institutional. **Era.** Late seventies. **Light.** Bright morning.
**Must be in frame.**
- Children's Hospital's 1914 pavilion at 300 Longwood: a columned classical
  front under a green dome on a drum, by Shepley, Rutan and Coolidge. This is
  the one object that says Longwood and nothing else.
- The seventies concrete hospital slab behind it, ribbon windows.
- Brick hospital blocks either side, dense window grids.
- A traffic signal on a mast arm, red showing. A cobrahead on a wooden pole.
- An ambulance at the far curb: white van, red stripe, light bar.
- The ladder crosswalk, the gum spots, granite curbs near and far.
- **Not in frame:** triple-deckers, which belong to the old reading.
*Reference:* [Children's Hospital, SAH Archipedia](https://sah-archipedia.org/buildings/MA-01-FL24); [Boston Children's Hospital](https://en.wikipedia.org/wiki/Boston_Children%27s_Hospital); [Harvard Medical School and the Longwood Medical Area](https://sah-archipedia.org/buildings/MA-01-FL21).

### Scene 3, revised: the near sidewalk
The first build put the storefronts at the front of the frame and the
narrator's props at the back, which is the opposite of where the piece
stands. We are on the near sidewalk waiting for the 39, so the near things
are the big things.
- A bus shelter: steel frame, flat roof, glass, with a slat bench inside.
- The 39 stop sign beside it.
- Two pedestal payphones, near and large.
- The ant on the brick by the payphones.
- Across the street, small: nine low-rise brick storefronts, lit, a cobrahead
  with its sodium pool, wires; the triple-deckers behind, smaller still.
Shelter form after the plain steel-and-glass MBTA shelters of the period;
the 2000s advertising shelters came later.
*Reference:* [Bus Stop Program, City of Boston](https://www.boston.gov/departments/transportation/bus-stop-program); [MBTA Route 39](https://www.mbtainfo.com/39).

## AUTHORED, 2026-09-20, third pass: both revisions built
Generators added: `pavilion`, `slab`, `signal`, `ambulance`, `shelter`,
`bench`. Scene 3 uses layer transforms to put the far rows at 0.6 and 0.68
scale and the payphones at 1.3, which is the first time the diorama has had
true near-far scale rather than three rows at one size. Belt run on the file;
verdicts recorded in the commit.
SIGNED: Art Director, Period Librarian, Compositor, Refuter, Studio Voice.
