---
title: Choreographed Chaos — Art Handoff Spec ("The Spilled Shaker")
date: 2026-09-29
owner: Matt Walsh (TSP founder) — HITL on every visual
lane: business (not EN195, not edu)
applies_to: table-four.html reskin, and every future Choreographed Chaos build
source_of_truth: DAM_225222_ChoreographedChaos_Cover_v6 (Damianos Publishing, InDesign, mod 2026-06-27)
permission: Wallers approved 2026-09-29 (founder report, in chat). Record the written reply in the repo next to this file.
supersedes: the cream "paper" palette in table-four.html (commit d847f1d3 lineage)
status: SPEC — no pixels yet
---

# Choreographed Chaos — Art Handoff Spec

## 1. The direction in one sentence
The game looks like the book cover came to life: real tabletop objects shot from above on the cover's red, where chaos is things tipping, sliding, and spilling on a visible rhythm, and every word sits on a kitchen ticket.

## 2. Why this and not the studio look
- The buyers are the Wallers, Damianos, and restaurant groups. They are paying for their brand, not ours.
- Restaurant people spot fake food and fake rooms at once. Real objects carry credibility.
- The shots are reusable: book-launch trailer, social loops, trade-show screen.
- House rules that still apply: accessibility floors, single file, offline, no emoji, scene first. House rules that do NOT apply here: paper-house / Lumino cut-paper look.

## 3. Brand tokens (sampled from the cover PDF, contrast computed)

Each token is ATMOSPHERE or TEXT, never both.

| Token | Hex | Role | Notes |
|---|---|---|---|
| --cc-red | #F70201 | ATMOSPHERE | The field. Never carries text. |
| --cc-oxblood | #680202 | TEXT accent / dark field | Cover shadow red. |
| --cc-ink | #231F20 | TEXT | Cover black. |
| --cc-ticket | #FBF7F0 | TEXT ground | Kitchen-ticket paper. |
| --cc-kraft | #E0C1A3 | ATMOSPHERE | Tabletop/linen warm fill. |
| --cc-wood | #8C5842 | ATMOSPHERE | Tabletop wood. |
| --cc-yellow | #FFF066 | ACCENT fill | The cover pull-quote yellow. Highlight, focus, "win" fill only. |
| --cc-white | #FFFFFF | ATMOSPHERE | Title outline, porcelain. |

Contrast (WCAG ratio, computed):

| Pair | Ratio | Verdict |
|---|---|---|
| ink on ticket | 15.26 | body text — use |
| oxblood on ticket | 12.30 | accent text — use |
| ink on yellow | 13.90 | highlighted text — use |
| ink on kraft | 9.57 | label text — use |
| white on oxblood | 13.14 | dark-field text — use |
| white on red | 4.23 | FAIL body. Display type 36px+ bold only |
| ink on red | 3.85 | FAIL body. Never |
| red on ticket | 3.96 | FAIL body. Red is never a text color |
| yellow on red | 3.61 | decorative only |

Rule of thumb for the builder: if a word is readable, it is on a ticket, kraft, yellow, or oxblood surface. The red is where the objects live.

## 4. Comfort ladder (live corner control, no opening wall)

Light stops (ticket surface; luminance gap >= 0.12):

| Stop | Ticket | Luminance | ink contrast |
|---|---|---|---|
| 1 Bright | #FBF7F0 | 0.933 | 15.26 |
| 2 Soft | #EBE1D0 | 0.761 | 12.58 |
| 3 Dim | #D9CBB5 | 0.608 | 10.21 |

Dark stops (DARK HOST LAW; L* gaps >= 8; ink flips to #F4EEE6; field becomes oxblood #3A0706):

| Stop | Ticket | L* | text contrast |
|---|---|---|---|
| 1 | #2A2422 | 14.8 | 13.26 |
| 2 | #3E3532 | 23.0 | 10.35 |
| 3 | #544946 | 32.0 | 7.53 |

Build on comfort-kernel-v2 v4 (backdrop element, both dark axes, paint-contract guard). Run preship-contrast-gate.py and studio-mismatch-audit.py; exit 1 = does not ship.

## 5. Typography
- Title lockup: the cover's condensed, outlined, drop-shadowed "CHOREOGRAPHED CHAOS" plus script "Every Table in the Restaurant Counts". Ask Damianos for the vector lockup (PDF/SVG). Embed as inline SVG. Do not imitate it with a web font.
- Game text: one system stack, no external host. Suggested: `"Helvetica Neue", Arial, system-ui, sans-serif`, bold condensed feel via weight 700 and tight tracking on headings only.
- Ticket text may use a monospace stack (`ui-monospace, Menlo, Consolas, monospace`) to read as a kitchen printer. Body size stays 20px+; nothing under 18px, including ticket fine print.
- Script font: title lockup only. Never for instructions.

## 6. The cast (objects are the characters)

| Object | Role in play | Chaos state |
|---|---|---|
| Salt + pepper shakers | The couple / the pair that must stay matched | Pepper tipped and spilling (cover image) |
| Kitchen ticket | Every instruction, order, and feedback card | Crumpled, stabbed on the spike |
| Water glass | Guest patience / refills | Sweating ring, then empty |
| Candle | Ambience cost; the anniversary table | Out, or wax dripped |
| Check presenter | End of turn, the till, the score | Open, overflowing receipts |
| Folded napkin | A seated guest | Dropped on the floor |
| Plates (3 sizes) | Courses, timing | Stacked wrong, one chipped |
| Bread basket | "The usual" — regulars' memory | Empty when it shouldn't be |
| Reservation book | The pacing puzzle | Pages full of cross-outs |

Rule: an object earns its place by being used in play (Mamet seat). Nothing on the table is set dressing only.

## 7. Photography shot list

Kit: phone on overhead arm or step stool, red matte poster-board sweep (match --cc-red on screen, check in the build, not by eye), one window or single soft light from upper left, white foam-board fill on the right. No flash.

Match the cover: hard-ish single shadow falling down-right, high saturation, clean edges.

| # | Shot | Angle | Notes |
|---|---|---|---|
| 1 | Each cast object alone, upright | straight overhead | Clean for cut-out |
| 2 | Each object in its chaos state | straight overhead | Same light, same height |
| 3 | Pepper tip sequence, 8 frames | overhead | Upright → spilled; stop-motion ready |
| 4 | Glass drain sequence, 5 frames | overhead | Full → empty |
| 5 | Candle lit / out | 3/4 low | Trailer use |
| 6 | Full two-top set, calm | overhead | The "choreographed" state |
| 7 | Full two-top set, chaos | overhead | Same framing as 6 |
| 8 | Hand resetting the table, 6 frames | overhead | Staff presence without faces |
| 9 | Ticket spike, full and empty | 3/4 | Menu / pause screen |
| 10 | Wood tabletop and linen plates | overhead | Backgrounds, no objects |

Hands only, no faces (no releases needed, keeps it universal). Use the Wallers' own props if available; ask. Label every file with shot number.

## 8. Asset production
- Capture: RAW or HEIC max resolution; keep originals in Drive Claude_files/choreographed-chaos/raw/.
- Cut-outs: background removed (Adobe image_remove_background is wired), keep the natural shadow as a separate soft layer.
- Delivery format for the game: WebP, embedded base64 (single file, offline). Budget: 1.5 MB total images for table-four; object sprites <= 60 KB each; one backdrop <= 250 KB.
- Sizes: objects at 2x their largest on-screen size; backdrop 1600px wide.
- Naming: `cc-<object>-<state>-<frame>.webp` e.g. `cc-pepper-tip-05.webp`.
- Screen composition: image/scene >= 50% of every screen.

## 9. Motion (the "choreography")
- Choreographed state: objects sit on an invisible grid, aligned, still.
- Chaos: the ripple. One tip causes the next, with a visible 120–200 ms stagger so the player sees cause and effect (Everything's Connected).
- Frame sequences from shots 3, 4, 8 play at 12 fps (stop-motion feel, not smooth tween).
- Reset: the hand (shot 8) sweeps in and restores the table. This is the win beat.
- Win sound and feel: follow topics/win-states-and-juice studio canon; one confident beat, no confetti.
- prefers-reduced-motion: swap sequences for the before/after pair with a 200 ms crossfade.

## 10. UI components
- Ticket card: cream paper, torn top edge, monospace order line, 44px minimum tap targets as stamped buttons.
- Check presenter: the score/summary screen (Carol Index reads here).
- Spike: pause/menu.
- Nav: back + home on every screen, drawn as ticket tabs.
- Focus ring: 3px --cc-ink on light, --cc-yellow on oxblood (11.21 contrast).

## 11. Do not
- No cartoon servers or chefs (Overcooked territory).
- No isometric tycoon look.
- No AI-generated food, rooms, or people.
- No stock restaurant photos.
- No text on --cc-red. No red text.
- No lollipop anything, no emoji, no external fonts or hosts.
- No opening instruction wall; the table is the first screen.

## 12. Acceptance gate (all must pass)
1. preship-contrast-gate.py exit 0
2. studio-mismatch-audit.py: light / dark / mismatch x every comfort stop
3. Studio Eyes uncanny audit: no AI tells, cut-out edges clean at 2x
4. Image floor >= 50% per screen; font floor 18/20; 44px targets
5. File size and single-file check; no external requests
6. Founder cold play on phone (GATE 1)
7. Side-by-side with the cover: would the Wallers recognize it as their book?

## 13. Open items (founder)
- Save the Wallers' written approval (email) next to this spec; confirm it covers the cover's visual language, or get Damianos' yes for the lockup and palette.
- Ask Damianos for the vector title lockup.
- Ask the Wallers whether they have restaurant props or photos to lend.
- Book the one-afternoon shoot (shot list section 7).
