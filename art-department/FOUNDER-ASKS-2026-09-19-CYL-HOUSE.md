# FOUNDER ART ASKS, 2026-09-19: Choose Your Leader, the house across the week

Founder, same day: *"The art in the kitchen doesn't match studio and the kids room doesn't look like one. Let's let art catch up. Remember mad men founder ask."*

The standard is the charter's: **Mad Men detail.** Every object in frame period-correct or it goes; a 1962 room contains nothing designed after 1962; the household reads its class register; wear and light match the film stock. The 1962 rung of the era ladder is **Kodachrome: saturated, slightly cool, orderly, hopeful.** No faces, no figures, ever.

What a session can and cannot do, measured today:
- **MJ lane:** closed by founder ruling 2026-08-13. The prompts below are for the founder's own subscription, paste verbatim.
- **Legal-photo lane (LOC, NARA):** blocked from the session sandbox. Verified 2026-09-19: the egress proxy refuses `www.loc.gov` and `tile.loc.gov` with 403, organization policy. Opening it is a founder job on claude.ai/code: the environment's network policy (see https://code.claude.com/docs/en/claude-code-on-the-web); allow `www.loc.gov`, `tile.loc.gov`, `catalog.archives.gov`. Once open, the Period Librarian brief in ASK 4 runs from any session.
- **Studio-cut lane:** cannot prove the house's room scenery. `art-execution-gate.py` measures first paint only, and every room plate in the house appears when the room is opened, mid-game. The porch SVG therefore stays an `art-gate` HALT until a plate replaces it.
- **Plates already on disk (`art/cyl/plates/`, founder MJ, 2026-07-30):** twelve. None is a kids' room. None is a porch. One is a kitchen, generated for 1969.

## What shipped today as interim, and needs your eye

**The kitchen** now carries `room.household.nixon69`, your own plate, cropped and re-graded in build: the calendar wall cropped out (the calendar face was generator mush and read December 1969), the amber pulled toward the Kodachrome rung, the window pane taken to night (it is seven in the evening in late October). What remains in frame: plywood slab cabinets, a white enamel range with a chrome dish rack, a Formica-top table, chrome-leg dinette chairs in red vinyl, a rounded-top refrigerator, cafe curtains, a wall clock. The Continuity seat's read: every object is at home in a 1962 suburban kitchen bought in the 1950s, which is the class register the retreat asked for. **RULING: keep as the 1962 kitchen, or hold for ASK 2.**

**The kids' room** still carries `prop.emptychair`, which you are right about: it is an armchair in a paneled room in raking light. Nothing on disk reads as a child's room. It stays until ASK 1 lands.

**The porch** is still the studio SVG stand-in. It stays until ASK 3 lands.

## ASK 1, primary: `room.kids.jfk62` (the kids' room at night)

Paste verbatim:

"Interior photograph, 1962 American suburban children's bedroom at night, seen from the doorway. Two twin beds with white chenille bedspreads, turned down, no one in them. A half-open door at frame left spills warm hall light across a braided oval rug and up one wall. Knotty-pine paneling on the far wall, a single window with a pull-down paper shade drawn, a small painted wooden bookcase holding a plastic model airplane, a stack of comic books, a tin transistor radio. A pair of canvas sneakers on the floor. No people, no faces, no toys with faces, no text legible anywhere. Shot on Kodachrome, 1962: saturated, slightly cool shadows, warm light only where the hall light falls, fine clean grain, orderly and cared for. Wide shot, eye level of an adult in the doorway. --ar 16:9 --style raw"

Object dates for the Continuity seat: chenille spreads (1930s to 1960s), braided rugs (period-neutral), knotty pine (1950s), pull-down paper shades (period-neutral), plastic model kits (Revell 1953 onward; keep the brand off), transistor radio (1954 onward), canvas sneakers (period-neutral). Kill on sight: any poster with a 1970s typeface, any plastic in a 1970s color, a digital clock, a nightlight of the plug-in kind (1960s exists but reads later).

## ASK 2, secondary: `room.kitchen.jfk62` (the kitchen at seven in the evening)

From the policy-gap bible's brief #1, cut for this house (a suburban family, not a Navy household; the suitcase stays out):

"Interior photograph, 1962 American suburban kitchen at seven in the evening, no daylight, one warm ceiling fixture. A chrome-leg Formica dinette table with a folded newspaper and one coffee cup on it, four vinyl chairs. Open shelves over the counter with canned goods and glass jars, a few gaps on the shelf. A white enamel gas range, a rounded-top refrigerator, a window over the sink gone black with the cafe curtains open, a wall clock reading seven. No people, no faces, no legible text on the paper or the cans. Shot on Kodachrome, 1962: saturated, slightly cool, fine clean grain, everything orderly and still believed in. Wide shot from the doorway. --ar 16:9 --style raw"

## ASK 3, secondary: `porch.jfk62` (the porch at night)

"Exterior photograph, 1962 American suburban front porch at night, seen from just inside the screen door looking out. A wooden screen door with a spring, a single porch light in a frosted glass shade, two concrete steps down to a walk, a cast-iron railing. Across the street, a similar house with its own porch light on and a television glow in one curtained window. A street lamp on a wooden pole. A 1950s sedan at the curb, no plates legible. No people anywhere. Shot on Kodachrome pushed for night, 1962: deep cool shadows, warm pools of light, fine grain. --ar 16:9 --style raw"

## ASK 4: the Period Librarian brief, once the LOC lane is open

Search the Library of Congress Prints and Photographs catalog, license read on the item page, never the search page. Collections that carry 1950s to 1962 domestic interiors with **no known restrictions**: Gottscho-Schleisner (interiors, 1935 to 1965), the Historic American Buildings Survey (HABS, federal work, public domain), the U.S. News and World Report magazine collection (1950s to 1980s, most items no known restrictions). Terms in the era's own vocabulary: "kitchen interior 1960", "dinette", "children's bedroom 1958", "front porch night", "suburban house Levittown interior". Record for every candidate: item URL, the rights statement verbatim, the date, and whether a person is in frame (if yes, it does not ship). Minimum 1600px on the long edge.

## Not asked for

The living room, the den and the hall are on `room.scene.jfk62` and its crops, and the founder has not flagged them. The set at seven is `insert.leader.jfk62`. Leave them.
