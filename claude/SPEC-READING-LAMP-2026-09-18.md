# SPEC — READING LAMP (working title) — DRAFT, AWAITING CALIBRATOR

Status: DRAFT built against `convening/READING-LAMP-CONVENING.md` (2026-09-18).
Five decisions (D1–D5) sit with the founder; this spec carries the convening's
recommendations and changes wherever he rules otherwise. No build starts from
this file until the rulings land.

## One sentence

The player trades tired phrases for one of three offered rewrites and notices
which choice actually puts a picture in a reader's head — and that the trap is
not the cliché next door, it is the abstraction that sounds like writing.

## Where it lives (D5)

EN195 arcade, flash-fiction unit; cross-listed in the Cliché Cowpaths hub as
the fourth movement. The suite reads: Field notices, Line cuts, City recycles,
Reading Lamp rebuilds. Course target: the concrete-imagery lesson — the
difference between concrete, specific writing and cliché, taught by
replacement, per the founder's phone ruling of 2026-09-18.

## The scene

A room at night holds one Listener in a chair and one lamp. The player's page
sits inside the scene as an object, not as floating UI. Image carries over 50%
of the paint. Entry is scene-first: no instruction wall, the Listener already
seated, one invitation on screen. The Medium Gate has not run; the art lane is
undecided on purpose and gets chosen at build convening (§3.2).

## The loop

1. A short passage appears on the page — founder prose with machine-planted
   clichés (D3). Planted phrases carry a quiet mark; nothing else is tappable.
2. The player taps one phrase. The screen holds one decision: three rewrite
   cards plus KEEP IT. The cards never label themselves.
   - The CONCRETE option is the founder's original phrase — evidence a
     stranger could see or hear from across the room.
   - The ABSTRACTION reports a feeling in dressed-up language and shows
     nothing. It is written sincerely; it should tempt.
   - The LATERAL CLICHÉ swaps the tired phrase for a different tired phrase
     wearing a new coat.
3. The chosen text re-typesets live, in place, inside the sentence. The changed
   span announces itself via aria-live. No verdict appears anywhere.
4. The Listener answers with behavior only (D2): an image lands and the cup
   stops turning; the prose goes abstract and the eyes drift to the window.
   Behavior is the primary channel; the lamp may support it but never a color
   tint alone, and never any meter.
5. Every choice stays re-swappable at zero cost until the player calls the
   reading. Auditioning all three options is the game working as designed.
6. THE READING: the player's assembled paragraph performs itself line by line
   against the Listener's attention. Endings land as states of the room, not
   scores — the fog (abstraction-heavy), fresh paint (lateral clichés), or the
   lit room (the images hold and the Listener stays). The player returns to
   revise from the reading with everything still open.

## Anti-quiz laws (the convening's spine — each names its check)

- LIVE SUBSTITUTION: text rewrites where it stands; no answer screens.
  Check: no DOM state in which a choice renders outside the passage.
- ACCUMULATION: choices compose one performed paragraph; questions remember
  each other. Check: the reading renders only player-assembled text.
- WITNESS, NOT METER: consequence arrives as one person's behavior.
  Check: no numeric or bar-shaped element on the play screen; grep the build.
- NOTHING LOCKS: free re-swap before the reading; no timer, lives, or fail
  state. Check: every choice control remains enabled until the reading.
- NO LECTURE: the game never states that concrete beats abstract; KEEP IT is
  always present, and at least one planted phrase per late passage is best
  left alone. Check: copy audit against the word list (concrete, abstract,
  cliché as instruction); one KEEP-IT-correct phrase in the final passage.
- NO SCORES OR TICKS ANYWHERE: no percent, no green flash, no checkmarks.

## Passages (D3)

Five passages rotate, Sandbags-style. Load-bearing prose comes from
games-text-bank.md and the walshero corpus; the machine plants the clichés and
writes the two trap options per phrase, sincerely. Escalation per the
Coordinator: passage one plants smellable clichés; by passage four the traps
dress better; the final passage includes the phrase that should be kept.
Provenance line on the game screen: "Prose: Matt Walsh, from the studio text
bank. The clichés are the machine's; the images are his." Any non-founder
passage enters as attributed open-license text under the sourcing rule.
Founder approves the piece list before authoring (HITL).

## Floors (hard, all inherited)

- Accessibility is arithmetic: 44px targets, 18px floor / 20px body, back +
  home on every screen, one decision per screen.
- DARK HOST LAW: comfort ladder forks under prefers-color-scheme: dark;
  dark-side stops spaced by CIE L* gaps of 8+; color-scheme: dark at every
  stop.
- BACKDROP-AS-ELEMENT: the room paints on a real fixed div at z-index 0;
  content rides z-index 1; body background is never the floor.
- aria-live on the rewritten span; Listener behavior never color-only.
- No emoji. Single file, offline, no external hosts. No opening wall.
- Preship: one-thing-gate, preship contrast at every stop in both emulations,
  comfort-gate, tableau floor, hostile-viewer repro.

## Win state

The lit room: the paragraph holds its images, the Listener stays to the end,
and the lamp is still on when the last line lands on an object. The fogged
reading stays interesting and free to revisit — it is a draft, not a death.

## Deferred, logged, not built

- D4 City hand-off: swapped-out clichés shipping to Cliché City as prefab
  slabs. A true suite loop; breaks single-file law without a design the Medium
  Gate should see. Revisit after first ship.
- Listener animation count beyond the six named states.
- Cowpaths hub card (one new cartridge card when this ships).

## Open with the Calibrator

D1 name (rec: Reading Lamp) · D2 Listener (rec: person, behavior-only) ·
D3 source (rec: founder prose, Sandbags precedent) · D4 City hand-off (rec:
defer) · D5 home (rec: EN195 flash unit + Cowpaths fourth movement).
