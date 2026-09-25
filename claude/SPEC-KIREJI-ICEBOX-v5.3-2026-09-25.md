# SPEC — Kireji Pond v5.3: the Icebox reorganized

Date: 2026-09-25
Canon base: `kireji-pond.html` (repo root), v5.2, sha256 `8cead420e327345b17d4174f45d73975d2c803c90b6ec46d342965591bf12b01`, trunk `e8a6471`. Shelf copy `builds/kireji-pond-v5.2.html` is byte-identical.
Owner: TSP. Build target: `kireji-pond.html` v5.3.

## Founder words (primary source, 2026-09-25, voice)

- "I like how you can see your own poems there. But then when you save poems or phrases to the top of the fridge, it gets a little messy."
- "If they're in the freezer, then I should be able to hit a button that's like copy text, or email them to myself, or both."
- "I was trying to make a poem in the freezer door and it wouldn't let me because they're all sloppy. Maybe that just means I have to move them down, but it wasn't intuitive."
- "I like how you can just tap and move things around."
- "I'd rather see the ones you built actually inside the freezer."

## What the code does now (why it feels wrong)

1. Two physics one inch apart. `.fzsaved` is a flex-wrap list (reflows on every add, tilted 8 to 17 degrees, no placement). `.door` is absolute-positioned (magnets stay where dropped). Nothing on screen says which is which.
2. The freezer is invisible to Send. `readPoems()` reads only `mags` on the door. Anything composed or parked in the freezer never reaches Copy or Email. This is the concrete bug behind the founder's ask.
3. Send guesses structure. `readPoems()` splits poems by row height and a 96px gap. The player never declares where a poem ends.
4. The player's three finished poems sit somewhere in a 1600px door with no fixed home.
5. The dashed border on the tray reads as a drop zone, not a shelf.

## The build (v5.3)

### A. The freezer becomes the poem board (founder ruling: built poems live in the freezer)
- `.fzsaved` changes from flex list to an absolute-positioned field, same drag physics as the door. A magnet dropped in the freezer stays where dropped.
- Magnets land straight in the freezer (no tilt). Retire the v5.1 crooked tilt for the tray; keep the straighten animation only for door landings from above.
- Persist x, y per saved magnet in the existing localStorage key (add `x`, `y` to each `keep` entry; missing coordinates get auto-placed in reading order so v5.2 saves still load).
- Freezer min-height grows to fit its lowest magnet plus 80px. No internal scroll.
- The player's three finished poems are placed in the freezer on first open, as three stacked clusters, lines in order. (They already are "own" work; this gives them a fixed home.)
- Drag between freezer and door works both directions. Arrow keys move a focused magnet within whichever field it sits in; a menu item "Move to freezer" / "Move to door" crosses fields for keyboard and voice users.

### B. Copy and Email live on the freezer
- Two buttons in the freezer brand row, right of "The Icebox": `Copy poems` and `Email poems`. Min 44px, same `.fzb` style, real text labels.
- They read the freezer only, top to bottom. Poem breaks = the same row/gap reader, applied to freezer magnets. Because the freezer is small and deliberate, the guess is reliable.
- Copy: clipboard write, fallback select-and-copy (reuse v5.2 code). Live-region confirmation: "Copied 2 poems."
- Email: reuse the existing `fzMail` dialog (editable text, optional To field, mailto). Prefill from the freezer, not the door.
- Top-bar `Send haiku` stays for the door. Rename it `Send the door` so the two are distinguishable by voice.
- Empty freezer: buttons stay visible but announce "Nothing in the freezer yet. Drag magnets up to build a poem."

### C. Labels and cues
- Replace the dashed tray border with a thin wire-rack line (two 2px rules, `#4A463E`), no dashes.
- Subtitle under "The Icebox" changes from "Saved for later" to "Build and keep poems here".
- `fzEmpty` text: "Drag magnets up here to build a poem. Copy or email it when it's done."
- Door aria-label adds: "Phrase magnets. Drag up to the freezer to build a poem."

### D. The seal turns over (founder, 2026-09-25: "Keep it, but make it tappable and it turns around for translation")
- The red 句箱 seal becomes a `<button>` (min 44px target; the seal art stays the same size, padding carries the target).
- Tap, click, Enter or Space flips it like a card on its vertical axis (0.45s). The back is the same red seal, reading top to bottom: `verse` / `box`, and a small third line `ku · hako`.
- Tap again flips it back. It stays on whichever face the player left it.
- `aria-label` on the front: "Seal, 句箱, ku hako. Tap to translate." After the flip, the live region says "verse box. The kanji say verse and box, a pun on icebox." `aria-pressed` tracks the face.
- Reduced motion: crossfade, no rotation.
- Contrast: the back text uses the same cream-on-red pair as the front (`#F8E9DC` on `#B23A2A`); the gate must pass at the smaller English size.
- Honesty note in the back face's title attribute or live text: coined for the game, not a dictionary word.

## Out of scope for v5.3
- Cross-device saving (stays this-device; Copy and Email are the escape hatch, stated in the freezer hint).
- Door endless-scroll changes and a separate phrase drawer. Revisit after founder plays v5.3.

## Gates before it reaches Matt
- `preship-contrast-gate.py kireji-pond.html` exit 0 (new buttons, new rack line).
- No emoji. Single file, offline, no external hosts.
- Byte-verify after push: fetch back via git, match sha256.
- Playtest checks: drag freezer to freezer holds position; drag door to freezer and back; reload keeps freezer layout; v5.2 localStorage loads without error; Copy and Email output equals freezer poems only, in order; keyboard-only path moves a magnet into the freezer and emails it.
