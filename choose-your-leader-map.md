# Choose Your Leader — Project Map & Overview

*A single document that explains what this game is, why it's built the way it is, exactly what's in the file today, and what's left to decide. Written so someone who has never seen the project — a collaborator, a faculty reviewer, a new AI session — can understand it without anyone re-explaining.*

*Maps the build `choose-your-leader-full.html` (v2). Last mapped: 2026-06-27. Structure: two eras — a Cold War trio (live) and a current-era trio (gated).*

---

## 1. The one-sentence version

**You don't judge the leader. You judge what you were allowed to see.**

Choose Your Leader is a short, playable lesson in media literacy. It hands you a real quote from a U.S. president, asks how much you trust the person who said it, *then* shows you the facts the original audience couldn't see — and lets you feel how far the words pulled you before you knew the whole story.

It is not a game about who was a good or bad president. It is a game about **the gap between what gets said and what was true at the time**, and about training the reflex to notice that gap.

---

## 2. Why it exists (the teaching problem it solves)

Most "media literacy" instruction tells students *that* they should be skeptical. It rarely lets them **feel** themselves being moved by a message and only afterward see the frame they were inside.

Choose Your Leader closes that loop. It does three things a lecture can't:

1. **It makes you commit before you know.** You rate your trust with only the quote in front of you. That commitment is real, and it's on the record before the facts arrive.
2. **It shows you the cost.** Once the full record turns over, the game shows how far the rhetoric carried you — visually, as a descent.
3. **It rewards noticing, not cynicism.** The win condition is *catching the gap*, not distrusting everyone. One scene (Lincoln) deliberately has almost no gap — and noticing that there's no gap is also a win. The skill is calibration, not suspicion.

This is the studio's house method in miniature: **Play. Notice. Design.** The player plays, notices something real about how they were moved, and walks away with a transferable habit.

---

## 3. How a single scene plays (the core loop)

Every scene runs the same four beats. This repetition is the point — the player learns the *move*, then practices it across different presidents and eras.

**Beat 0 — Scene first.** You land inside a room. No instructions, no setup paragraph. A 1962 living room lit only by a television; a Depression-era parlor with a radio; a hearth with a folded newspaper. The prompt is simply: *tap whatever your eye goes to.* Whatever you tap, you "noticed" — every read is valid. Then the room speaks.

> *Design rule behind this:* every game in the studio must open by landing the player in a scene where they notice something — never a wall of text. (Scene-first floor, locked 2026-06-27.)

**Beat 1 — Blind trust.** You see the quote and a line about how it would have reached you ("Three networks. One message. This is all you get."). The game asks: *with only this, how much do you trust the leader saying it?* Four buttons, Not much → Fully. **You must commit before you can continue.** This commitment is the measurement the whole game depends on.

**Beat 2 — The record turns.** The facts the original audience couldn't see arrive — dated and sourced. (Kennedy's televised address was day eight of a six-day deliberation, not a first reaction. FDR's "fear itself" calm arrived alongside the most drastic emergency powers in the country's history.) Then the game asks again: *same words, but now you can see the frame — how much do you trust them?*

**Beat 3 — Where it pulled you (the descent).** The game compares your two trust ratings and shows you, on a five-rung ladder, how far the rhetoric pulled you down — and whether you braked it by noticing the gap. This is the emotional payload of the game, and it follows three strict safety rails (see §5).

After the last scene, an **arc screen** shows every moment at once: how high you held each time, and where you caught the gap versus missed it.

---

## 4. The descent — what the five rungs mean

The ladder is a Maslow hierarchy turned into a felt consequence. You start at the **top** (rung 5 — your own judgment) and rhetoric *pulls you down* toward the floor (rung 1 — where consent stops mattering). Noticing the gap is the brake that arrests the fall.

| Rung | Label in the game | What it represents |
|------|-------------------|--------------------|
| 5 | Your own judgment — becoming who you could be | You kept your footing; the message didn't override you |
| 4 | Standing, respect, a voice | Lightly moved, still mostly your own |
| 3 | A people, a side, a we | Pulled toward belonging — "us," one safe message |
| 2 | Safety — survive the threat | Pulled toward fear and protection |
| 1 | The floor — where consent stops mattering | Carried all the way; this is how far rhetoric *can* reach |

**How the rung is computed (the actual code):**

- `pull = (blind trust) − 1` — how much the quote alone moved you. More blind trust = more pull downward.
- `brake = max(0, blind trust − trust after the record)` — if you trusted *less* once you saw the facts, you noticed the gap, and that brakes the fall.
- `landing tier = clamp(5 − pull + brake, 1, 5)` — start at the top, subtract the pull, add back the brake.
- `noticed = (trust dropped after the record)` — a yes/no flag the arc screen reports.

The game **never asks you to rate yourself.** It only watches the distance between your two commitments. That distance *is* the measure of gap-noticing.

*(The reusable version of this mechanic — math, rails, and accessibility rule for any future game — is the canonical recipe in `tight-spiral-patterns.md` §8. This section is the player-facing explanation for this game; the pattern file is the source of truth for the implementation.)*

---

## 5. The three safety rails (why this isn't a "gotcha" game)

The descent could easily feel like punishment — "you got fooled, you're at the floor." The studio forbids that. Three rails are law (locked 2026-06-27, trauma-informed):

1. **The consequence lands on the rhetoric's reach, never on the player's worth.** The copy says *"This is how far rhetoric can carry a person,"* not *"you failed."* The thing being judged is the message's power, not you.
2. **The brake is always live, and naming the gap is the win — even at the floor.** If you land at the bottom but noticed the gap on the way, the game says so plainly: *"All the way down… but you named the gap on the way. That's the whole skill."* There is no dead end.
3. **The deep ending teaches; it never ambushes.** The lowest landing explains how far rhetoric can carry someone — it does not mock the player for getting there.

These rails are why the game can use *real* emotional stakes without harming anyone. They generalize to any future game with a descent mechanic.

---

## 6. What's actually in the file right now (honest build audit)

**Status: BUILT — content-complete for the four historical scenes, single-file, offline, accessible.**

### Plays today (three Cold War scenes, all with real dated/sourced records)
- **Kennedy, Oct 22 1962** — Cuban Missile Crisis address. Gap: the calm public address was day eight of six days of private deliberation.
- **Lyndon Johnson, Aug 4 1964** — Gulf of Tonkin address. Gap: the second attack the speech leaned on most likely never happened (later NSA study), and the ships supported covert raids the public wasn't told about; the war-powers resolution had been drafted months earlier.
- **Nixon, Nov 3 1969** — "Silent majority" / Vietnamization speech. Gap: while the speech asked for patience on a withdrawal, the same administration had been secretly bombing neutral Cambodia since March — a covert campaign hidden from the public for years.

### Built but gated (does not play until you source it)
- **Obama, Trump, Biden** — three current-era scenes are coded and waiting, but their quotes and records are placeholders (`[QUOTE PENDING]`, `[RECORD PENDING]`). The engine **deliberately excludes them from play** (`PLAY = SCENES.filter(not gated)`). Records are *not* fabricated. Each needs a real dated, sourced, founder-approved quote-and-record pair before it ships. This is the Bias-Auditor / Validation-Lab gate, and it is visible to the player in the deepest "for instructors" panel.

### The "show the engine" panel (end of game)
Three reversible depth rings let a curious player — or a skeptical faculty member — descend from *"what was this measuring?"* down to the raw measurement readout: constructs, instrument, scenes played, gaps noticed, mean landing tier, and the ship-gate status. This is the studio's **Glass Engine** principle: the learning mechanism is visible, not hidden.

### Accessibility (meets the studio's hard floor)
Single-file, offline, in-memory only. Large serif type, one decision per screen, 44px+ tap targets, full keyboard navigation with visible focus rings, scroll resets to top on every screen change, a working "leave the game" exit that clears state. Art is cut-paper SVG with real value range and warm/cool temperature relief so subjects read clearly.

### Art state
Four "hero rooms" are built as layered cut-paper SVG (the Kennedy night room is the most finished). The descent screen (Beat 3) is currently a clean typographic ladder — the cut-paper "descent planes" art is **not** built yet, and is waiting on your descent-math sign-off before anyone makes art for it.

---

## 7. How the studio's system runs this project

Choose Your Leader is one build inside Tight Spiral Studios, and it follows the studio's standing machinery:

- **The pipeline.** Every stage is *agent pre-flight (mechanical) → human gate (your judgment) → emit*. For CYL, the agent can draft scenes, write code, and assemble sourced records; **you** make every locked call. The living-president records are the clearest example: an agent can gather candidate quotes and facts, but only you approve a record as shippable.
- **The Review Panel.** Trauma-Informed and Accessibility seats hold a HALT on this game — they're why the three rails and the visibility floor exist. The Validation-Lab seat holds the gate on living-president records.
- **The measurement layer (Confluence).** Confluence is the studio's rater-norming and calibration system. CYL's measurement is built to speak its language: the game emits *gap-noticing* and *landing tier* as constructs, which can roll up as evidence at the assessment (ISLO) layer. In plain terms: **the game teaches what to notice; Confluence is the discipline for measuring whether the noticing actually happened and whether different raters would agree on it.**

---

## 8. Open decisions (what only you can settle)

These are the locked-call judgments the build is waiting on. None can be delegated.

1. **Descent-math feel.** Does the pull/brake formula *feel* right when you play it — is the drop dramatic enough, is the brake satisfying enough? Art for the descent planes waits on this sign-off.
2. **Project name.** "Choose Your Leader" is the working title.
3. **Brand placement.** Where the Tight Spiral / imprint credit sits in the finished piece.
4. **The exact Leadership rubric instrument.** Which formal rubric (if any) the measurement maps to.
5. **Which rubric dimension ships first.** The studio rule is: ship one dimension as the MVP before building the visual and socioeconomic content tracks. Don't widen before the first dimension is real.
6. **Source the first living-president scene.** Picking one (Obama, Trump, or Biden), finding the dated quote and the dated outside-the-frame record, and approving it — that un-gates the first modern scene and proves the gate works end to end.

---

## 9. Glossary (terms this project uses)

- **Scene-first** — the rule that every game opens inside a scene the player notices, never with text. CYL's Beat 0.
- **The gap** — the distance between what a leader said and what was true/happening at the time. The whole game trains noticing it.
- **The descent / Maslow-descent** — the five-rung ladder rhetoric pulls you down; noticing is the brake. The studio's name for this mechanic.
- **The brake** — noticing the gap, which arrests the fall. Measured as your trust dropping after the record turns.
- **Gated** — a scene that is coded but excluded from play until its record is real, dated, sourced, and founder-approved.
- **Glass Engine** — the principle that the learning mechanism is shown, not hidden. CYL's end-of-game depth rings.
- **Confluence** — the studio's calibration/rater-norming system; the measurement discipline CYL's evidence feeds.
- **Human gate** — the point in every pipeline stage where your judgment, and only yours, decides advance / halt / park.
- **The rails** — the three trauma-informed rules that keep the descent from blaming the player.

---

*This map describes the build as it stands in `choose-your-leader-full.html`. When the build changes, update this file rather than starting a new one. When in doubt, the studio floors win: no emoji, accessibility is a design floor, full-contrast text, scene-first openings.*
