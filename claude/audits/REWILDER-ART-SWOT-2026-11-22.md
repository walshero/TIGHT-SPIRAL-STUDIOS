---
title: Rewilder art SWOT, game-wide (v0.87)
date: 2026-11-22
asked: founder, 2026-11-22, "Then I want a full SwOT report on art game wide"
evidence: 18 scenes captured at phone landscape 844x390, contact sheets in rewilder-art-swot/sheet1-3.png
bar: the ocean salmon scene (founder's 10/10 for built things) and Lumino City (founder's bar for papercraft)
seats: Claude reading the screenshots against the founder's rulings; no outside reviewer, no senses-seats agent (cost)
---

# Rewilder art SWOT (v0.87)

## The scenes

| # | Scene | Read against the bar |
|---|---|---|
| 01 | Title | Strong. Hanging letters, grey to green, read as the game's story. |
| 02-03 | Level 1 street: garage, I-93, coal plant, triple-deckers | Strong. Layered card, faces on the cars, the most finished stretch. |
| 04 | Lot and dam | Weak. The dam is a stack of flat grey slabs with no card edge, grain or shadow. |
| 05 | Tar works approach | Weak. A wall of flat grey-green fills half the screen. |
| 06 | Level 1 restored | Good. Tree, playground, wind turbines, blue sky. The ground stays flat. |
| 07 | Restored dam and waterfall | Mixed. The waterfall is flat polygons next to papercut trees. |
| 08-10 | Level 2-3 dystopia: billboards, scaffolds, data center | Good mood: dark sky, OBEY/CONSUME eyes, hazard stripes. Buildings are flat window grids, simpler than level 1. |
| 11 | The Eye sphere | Strong. The single most memorable image in the game. |
| 12 | Level 3 restored: eco tower | Good. Busy and joyful, though detail is small at phone size. |
| 13 | Underwater river | Weak. Muddy, low contrast, small junk shapes, floating word signs. |
| 14 | Ocean salmon | The 10/10 reference: light shafts, depth, kelp, one clear subject. |
| 15 | Island arrival | Weak. Many small parts, purple lair blob, low read at phone size. |
| 16 | Island tower (v0.87) | Better. Hotel face, big pool, cold pipes. The drone line is the strongest shape. |
| 17 | Island roof | Mixed. Penthouse, blimp and post are small; the top of the scene crowds the bar. |
| 18 | Vacation | Clean and bright, but plain: flat sand and sea. |

## SWOT

| Strengths | Weaknesses |
|---|---|
| Level 1's street is real papercraft: layered card, grain, cast shadows, characterful cars. | **Three materials in one game.** Papercut (level 1 street, salmon ocean), flat vector slabs (dam, tar works, waterfall), and flat window grids (level 2-3 buildings). |
| Clear before-and-after: grey and brown dystopia against green and blue repair, with sky colour carrying the change. | **The big structures are the flattest.** The dam and the tar works are where the player spends the most time per site, and they have the least art. |
| Icons with meaning: the Eye, OBEY and CONSUME, the frowning sun. | **Words in the world**: DIVE, TAG, TOLL signs, "Floor 40 of 40", toasts over the top. Small text against your "icons, not words" rule and hard to read with RP. |
| One clear subject in the ocean scene: light, depth, the salmon. | **Small detail at phone size.** The eco tower, island arrival and roof hold dozens of 10-20 px parts. On a phone they become texture, not story. |
| HUD is one icon bar, high contrast (10.17:1 worst text pair). | **Controls take about a third of landscape.** The d-pad and Smash are dark and heavy and sit over the ground band. |
| | Underwater reads as murk, not water. |

| Opportunities | Threats |
|---|---|
| **One material rule** (your award list item 1): every built thing as layered card with an edge, grain and a shadow. The dam and the tar works are the two biggest wins. | **The finishing problem.** Art passes keep going 3/10 to 6/10 one object at a time while new features arrive as line art. Every new system adds art debt. |
| **The transformation as showpiece**: each site's fall and regrowth staged like the 93 collapse, the one moment players will remember. | **File weight.** 616 KB and climbing toward the studio's 1 MB ceiling. More procedural art adds bytes and draw time. |
| Swap in-world words for icons (dive ladder icon, tag hand, toll coin). Cheaper than any art pass and helps RP reading. | **Phone draw cost.** The island scene renders slowly even headless. Richer art on a mid-range phone risks dropped frames. |
| Reuse the ocean scene's recipe (light shafts, depth layers, one subject) for the underwater river. | **Clutter versus reading.** More detail at phone size works against your accessibility rule unless each scene keeps one clear subject. |
| Lighter, smaller controls in landscape (outline d-pad, translucent at rest). | |

## Ranked next moves

| Rank | Move | Why first | Cost |
|---|---|---|---|
| 1 | Dam and tar works to papercut (layered card, grain, shadow, a face or two) | Biggest flat surfaces, longest time on screen | One build |
| 2 | Words in the world to icons | Cheap, helps RP, matches your standing rule | Small |
| 3 | Underwater river with the ocean recipe | Turns the weakest scene into a sibling of the best one | One build |
| 4 | Island arrival: one subject (the tower), fewer small parts | The final act should read at a glance | One build |
| 5 | Level 2-3 buildings get card depth instead of window grids | Brings the dystopia up to the level 1 street | One build, after 1 |

**Recommendation:** do 1 and 2 together in the next build. They fix the two things a first-time player sees most (the dam is the first big structure after the street) at the lowest cost.
- **Tradeoff:** the dam pass adds bytes. Budget it, and check draw time on the phone.
- **Simpler:** just 2 (icons), this afternoon.
- **More advanced:** the one-material rule as a shared card renderer that every structure calls, so new features arrive papercut by default and the art debt stops growing.

## Not covered
Motion and sound (Murch and Ear seats), human play, and the art at the end of the island sequence (fireworks and village), which needs the full quest run to capture.
