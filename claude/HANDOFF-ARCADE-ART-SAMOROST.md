# HANDOFF — Arcade art expansion, Samorost grade

Written 2026-08-09 at the tail of the playtest session that landed v5.1 through v6 on
`en195-arcade.html`. This is the piece deliberately NOT built that night: new art takes
a fresh session, not the last tokens of a long one.

## THE RULING (founder, verbatim, 2026-08-09)

> "The graphics should be much larger cs text. Like 3x current. I want to see genre
> related games located near the four current workshops, which players will use a week
> or 15 weeks from entry into this platform. This is for practice and playing so
> workshops should be for real. Feed those animated beings!!!! And more zany art like
> samarost"

## WHAT v6 ALREADY LANDED (do not redo)

Four genre districts on the hub, each led by its guardian banner (injected from VM_ART,
idle rigs running), practice cabinet above the real workshop, tags "Practice, any week"
and "For real", cabinet icons 40px -> 120px (96px under 480px), workshop copy trimmed,
two "in the shop" practice slots (Play district, Story district).

## WHAT THIS HANDOFF IS: the zany pass

Reference: Samorost / Amanita Design - organic surrealism, small creatures living in
found textures, machines grown rather than built, everything slightly alive. The studio
translation is NOT painterly rendering (no image model in this file); it is hand-cut
SVG shadow-puppetry with more joints, more moss, more nonsense that moves:

- Give each guardian an ENVIRONMENT, not just a ground line: Funes under a tree that
  drops one leaf on a loop; the Aleph's rings orbiting debris (a chair, a fish, a
  comma); the marionette's strings running up past the frame to something unseen; the
  golem's book-rows sprouting tiny mushroom bookmarks.
- Small secondary beings, one per district, that react on tap (a snail on Funes's knee
  that retreats; a moth circling the Aleph). Decorative, aria-hidden, 44px if tappable.
- The coin on scene0 gets company: something small watching from behind a cabinet.
- Cabinet icons at 120px deserve 3-4 more cut shapes each - they were drawn for 40px.

## FLOORS THAT BIND THE ART (all mechanically checked, no exceptions)

No emoji ever. All art hand-cut SVG, own work, in-file, offline. The puppet stage and
scene0 stay fixed-dark (#262019 family) per the standing ruling - comfort governs the
chrome around them. Every animation obeys the two-rule motion pair already in the file
(never merge an @media into a selector list). Tap targets 44px+. Every rendered text
node 18px+. Run `bash studio-belt.sh en195-arcade.html` before and after; push through
the connector in verified ops (replace_substring_in_repo_file / append_chunk, unique
match + expect_total_bytes every time).

## STILL OPEN ELSEWHERE (inherited, not this handoff's job)

Dusk propagation to comfort-v3.html and comfort-gate MODES. Practice cabinets for the
Play and Story districts (game design, not just art). workshop_tokens retention -
founder call, still open.
