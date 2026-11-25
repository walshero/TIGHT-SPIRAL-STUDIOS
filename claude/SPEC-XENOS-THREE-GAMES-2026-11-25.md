# Xenos rebuild: the three kept games (2026-11-25)

founder ruling 2026-11-25 13:47: keep only Mail Drop, Triangulate and Loteria. Mail Drop and Triangulate were functional in Xenos 2013; Loteria was Matt's paper prototype (concept to paper, 2012). Every player, NPCs included, spawns in the central Marketplace to maximize contact. Improve the map into cohesive spaces.
name collision: the studio already ships a different Mail Drop (EN195 Lab, cliche sorting, mail-drop.html in the repo). The Xenos game ships as xenos-mail-drop.html.

## Sources read (Drive, walshero)
| Game | Doc | Id | What it gives |
|---|---|---|---|
| Loteria | Loteria for Xenos (2012-04 to 11) | 1JdVX6rbb_75dBZuQ3QFj3ZtxNXMKXHth2PN9B5uLGjQ | Full design: 4x4 board, caller, clues, timing, X pattern, action cards, rubber band, listening standards |
| Loteria | Loteria MW notes (2012-09) | 1N3PW_AImys-pyvrhZsI5JTeQpUXVdx38UXp7ZVm0UE0 | Matt's notes; variations 2 (Reversi) and 3 (deduction) |
| Loteria | DECK 1 | 1qCKDby3aVZKmhGfsWxSxa-jRMn0PLxAcugytjK74shw | 16 pictograms with 17 shared clue attributes: complete level 1 content |
| Loteria | LOTERIA ACTION CARDS | 1KG49U9VSpWlgjw762AernydqiEh5OLd95p5LmPYHsb8 | 26-card action deck mix |
| Triangulate | Triangulate Enhancements | 1VLUNnsh4EBgsxXBNQohrUBt8lERCNA4UoXMWDkLY3v8 | Rules, levels 1-2, datasets A-C, 3.3 fixes, playtest bugs |
| Triangulate | Triangulate_Modifications | 1F4ddB6117mhMdbWyo9xZuZOHo7Hanu3slcgq84tvyyg | Level 2 definitions; tool tip; slow belt |
| Triangulate | Triangulate Deck (2012-08) | 1bblJVQWexk6uWZ3-k2HPIOTTBUlJLpOndLLhlg2ypZw | ~520 level-1 nouns (GLO template) |
| Triangulate | Triangulate Word Set Spreadsheet (2013) | 1gsE369DPT-SMhcnScjyYJA8N2pHceauDElB3ODS6y_8 | not yet read |
| Mail Drop | Mail Drop 2014-2016 Version | 1sK2w1r7qFwTBWAT2wC8pfB1eNU-DY4gvRV-dvWSdVxE | Complete spec: roles, timing, penalties, AI profiles, scoring, translation delay, input, sound, music |
| Mail Drop | Maildrop content (2012) | 1cBl-ICJIRG6uwEY1TVdc5CtHpQe18tIF_0o40O9w0uc | ~90-110 messages per role, 8 roles, writing rules (most funny, some tricky, some with two right answers) |
| Mail Drop | Mail Drop improvements | 12FB6xijti9TKZ0pNR29XjNaIkI1FyVKqiOGDYjd5h9Q | Playtest fixes and tutorial wording |
| All three | Tutorial videos ch3-triangulate, ch3-maildrop | Drive folder 1bssnnrvJvIP9fMSVkk_nQURTUwSUbe7t | How the 2013 screens looked and moved |

## Mail Drop (build first: fully specified, content exists)
- Messages fall into your inbox. Send each to the role that can help. Wrong send: the message bounces back, the role says "Don't spam me!", and 2 penalty messages drop in. A full inbox knocks you out; last inbox standing wins.
- Roles. Level 1: Employment Agency, Crazy Chef, Doctor, Superstore Customer Service. Level 2: Dog Walker, Cab Driver, Pizza Parlor, Animal Nutritionist. You hold one role; NPC players hold the others.
- Pace: about 4 s between messages at the start, 10% faster every 30 s.
- Players: you plus 3 AI players from the 2014 profiles (steady; saves 3 then bulk-forwards; 40% mistakes; mistakes on purpose then bulk). Their inbox meters are visible; knock them out by flooding them.
- Scoring: messages correctly forwarded x place multiplier (10, 6, 4, 2), plus 500 per knockout.
- Translation: tap a message for Spanish. A short delay from level 2 up keeps players reading English first.
- Input: tap a message, then tap a role (or drag). Keyboard: arrow keys select, 1-4 send, space translates.
- Fix: Spanish translations are empty in the 2012 sheet. Draft them in-studio and flag them for Matt to review.

## Triangulate
- 3 rows of stone triangles hide a photo. Tap a triangle to hear a word. Catch its match on the moving belt (tap, no drag). Clearing 3 or more touching triangles reveals the picture beneath.
- Level 1: spoken word to picture or written word. Level 2: spoken definition to word. Spanish tool tip on belt items.
- Timer: 10 minutes; 20 was "really long" in playtests. The belt slows while you hover or touch.
- Datasets: A (community, transport, time, food), B (medical, body, clothes, colors, shapes, school), C (sports, leisure, holidays, weather).
- Audio: the browser's own speech voice, offline. No recorded files.
- Art gap: every word needs a picture. Recommended: one consistent hand-drawn pictogram set, shared with Loteria.
- The reveal photo should be island art (enhancements doc: "tied back to the world").

## Loteria (Matt's design; first digital build)
- You and up to 3 NPCs from the Marketplace sit at the Loteria table under the big Market tree. Each gets a 4x4 board of 16 pictograms.
- The caller (an island character) gives up to 4 clues. The first 3 come in random order; the 4th is specific to that picture. Replay any clue; 60 s per picture.
- Right on the first guess: chip placed plus an action card. Wrong: new clues for a different picture with your remaining time. Missed pictures come back later. The called picture is always on your board.
- Win: the X pattern calls Loteria.
- Action cards (hold one at a time): swap two pictograms, wipe out any square, wipe out a random square, rebuild a missing square, randomize opponent's board, randomize own board. Rubber band: the leader draws weaker cards.
- Early finishers flip earned cards for bonus facts.
- Deck 1 (level 1): canoe, chef, duck, bridge, taxi cab, fisherman, horse, cafe, bicycle, farmer, monkey, pilot, tractor, skateboarder, plumber, airplane, with 17 shared attributes ("uses tools", "found near water", "has wheels"...). The deck already notes clue orders that would give away a picture in 2 clues; keep those rules.
- Listening standards: L3, L4, L5 (idioms), L6, L7.

## Build order
1. Mail Drop: no art gap; 2013 rules plus 2014 refinements; NPC opponents come from the Marketplace crowd.
2. Loteria: content complete in Deck 1; needs 16 pictograms and a caller.
3. Triangulate: needs a word-picture set (100+ pictures) or starts with word-to-word at level 1.

## Open question for Matt
Pictogram art for Loteria and Triangulate. Recommendation: one in-studio pictogram set in the Xenos painted style, built once and used by both games.
