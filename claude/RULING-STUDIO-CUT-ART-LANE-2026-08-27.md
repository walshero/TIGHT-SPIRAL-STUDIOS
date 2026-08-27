# RULING: THE STUDIO-CUT ART LANE · 2026-08-27

**Founder's words, asking for Cliché Hunter:** *"And we want art."*

## The bind this resolves

`art-gate.py` has carried the 2026-08-01 ruling as arithmetic since it was
written: hand-authored SVG scene art never ships, and art comes from exactly two
lanes, founder Midjourney or licensed photography.

On 2026-08-13 the founder closed lane 1: *"No MJ in studio as we can do better
than we have so far with proper execution."*

That left one lane, licensed photography, which an offline single-file game
cannot carry. For two weeks the studio's art law read *"art comes from MJ"* while
MJ was shut. The only compliant build was a build with no art, and that is
exactly what shipped: `enjambment.html` records in its own meta that all its
scenery is CSS specifically to stay under the gate's floor, waiting for an MJ
lane that was never going to reopen.

This has been sitting in the notes as "art-gate amendment pending the founder's
own words" since 08-13. The words arrived today.

## The amendment

A third lane:

> **3. STUDIO-CUT.** Art cut in the studio, marked
> `data-art-class="studio-cut"`, and **proved by `art-execution-gate.py`**
> rather than by its own label.

## Why this is not a reversal of the 08-01 ruling

Read that ruling honestly. It banned hand-authored SVG because the hand-authored
SVG this studio was shipping was **bad**: flat layers with no silhouette, thin
line work, scene art out-glowing the type sitting on it. The ban was a **proxy**
for a quality bar nobody could measure at the time. Banning the technique was the
only lever available.

`art-execution-gate.py`, written on 08-13 to give the "proper execution" ruling
teeth, measures that bar directly: type dominance, cross-hatch texture, flat
layers. All three are real defects this studio actually shipped. With the bar
measurable, the proxy can retire in favour of the thing it was standing in for.

The 08-01 ruling gets what it wanted. Bad hand-cut art still does not ship. It
now fails for being bad instead of for being hand-cut.

## The teeth, so the marker cannot grant itself

When `art-gate.py` sees `studio-cut`, it **runs `art-execution-gate.py` on the
file** and HALTs if that gate HALTs, if it measured no scene, or if it could not
open a browser at all.

A label that clears a gate by being present is the failure this repo has a
standing rule against, and an unmeasured claim of proper execution is precisely
what the lane exists to stop. Blind is not clean.

Verified when the change landed:

| case | result |
|---|---|
| 3,273 bytes of unmarked inline SVG | HALT, unprovenanced |
| same SVG marked `studio-cut`, no scene marker | HALT, "claimed but NOT proved" |
| `enjambment.html`, `index.html` (CSS scenery) | pass, unchanged |
| `en195-arcade.html` (5,158 bytes hand-cut) | still HALT, unchanged |

The two gates compose and neither answers the other's question. **art-gate asks
where the art came from. art-execution-gate asks whether it is any good.**

## Consequence worth naming

`en195-arcade.html` has failed art-gate for weeks on 5,158 bytes of hand-cut
Samorost-direction scene art, with no legal way to fix it short of deleting the
art. It now has one: mark the lane and clear the execution gate. Not done in this
session, and left here on purpose so the next one inherits the task rather than
the puzzle.

## What did not change

No floor moved. `FLOOR` is still 2,500 bytes; small UI glyphs still pass;
instruments still pass; the MJ and legal-photo lanes are untouched. One lane was
added and it is the strictest of the three, because it is the only one that has
to be earned per file, every run.
