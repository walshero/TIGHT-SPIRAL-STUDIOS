# PLAYTEST INSTRUMENT — v2 signal layer (optimize)
<!-- 2026-07-27 · founder: "the two questions seem very weak. Review. Optimize." · upgrades os-block-playtest-instrument.md §3 (reactions) + §4 (closing). The six floors are unchanged and correct. -->

## THE REVIEW — why the current questions are weak

The standing default (os-block §4) is: **(a) did the core loop do its job · (b) what surprised you · (c) one thing to fix first.** All three are weak, and Funny Bones itself already told us why:

> *"the way you poll decides what you learn. Ask a lazy question and you get a comforting number that isn't true."*

The instrument is the lazy question. Point by point:

1. **"Did the core loop do its job?"** — leading, binary, and framed in the *designer's* intent. It asks the tester to ratify the thing you hoped for; the honest answer is almost always a polite "yeah, mostly." It measures your hope, not their experience. This is the "was that funny? — yes/no" poll the game mocks.
2. **"What surprised you?"** — one-shot and undifferentiated. Surprise is not signal until you know *where*, and *what they expected instead*. The instrument stops exactly where the value starts. The game's own thesis is *ask, then follow up on the surprised ones* — the instrument never follows up.
3. **"One thing to fix first?"** — asks the tester to be the designer. You get a **solution** and lose the **problem** it was solving. Testers are experts in what they felt, novices at what to change.

Underneath all three: **they are single-shot self-report at the end of play** — memory-biased, opinion-weighted, and blind to the strongest signal in any playtest, which is *behavior*: where the thumb hovered, re-tapped, stalled, or quit. And none of them checks the loudest thing of all — **whether the player even knows what the game is.**

## THE PRINCIPLE (the spine of v2)

> **Never ask a question whose answer confirms the designer. Capture what the player DID and what they MODELED; follow every surprise exactly once; keep the problem (data) apart from the tester's fix (a hunch). A signal without its rater's context is noise.**

That last clause is the studio's own situated-humour lesson pointed at its own instrument: who played changes what the signal means, so every report is stamped with the rater.

## v2 — IN-PLAY REACTIONS (replaces §3)

Five one-tap reactions, **behaviour- and feeling-anchored, not verdicts, and not positive-skewed** (the old set skewed to praise: "This landed / Delight / I snagged / Confused me / I'd cut this"). New set:

| tap | the signal it captures |
|---|---|
| **Lost — didn't know what to do** | the friction/comprehension break (the strongest, most under-reported signal) |
| **Re-read / re-tapped** | silent hesitation made visible — where the design made them work |
| **Something moved in me** (tester flicks +/−) | the felt beat, good or bad, located in play |
| **Went dead here** | disengagement — the signal testers never volunteer at the end |
| **Show-someone-this** | the shareable spike — the moment worth a text to a friend |

Plus the free-text box. Dropped: "I'd cut this" (asks them to design) and the praise-heavy pair. Kept the phase auto-tag — every tap still stamps itself with the screen it happened on.

## v2 — CLOSING PROTOCOL (replaces §4's three questions)

Not three opinions — a short **adaptive** sequence. Ask, then follow the surprised.

1. **Comprehension first (non-leading):** *"In one line — what is this, and what were you trying to do?"* Compare to the designed intent. A wrong or blank answer is the loudest, least-biased signal there is, and it never mentions your hopes.
2. **The behaviour trace (not opinion):** *"Walk me through what you actually did — where did you stall, re-read, mis-tap, or almost quit?"* The friction map, reconstructed from action, not sentiment.
3. **Adaptive surprise (the follow-up IS the instrument):** *"What did it do that you didn't expect?"* → immediately: *"Where exactly, and what did you expect instead?"* This is the studio's adaptive polling, turned on itself.
4. **The felt map:** *"Where did you feel the most — good or bad? Where did you feel nothing?"* Peaks and dead zones, located.
5. **Retention as behaviour, not intention:** *"Did you go again? How many rounds before you stopped — and what made you stop?"* ("Would you play again?" is a wish; "did you, and why'd you stop?" is data.)
6. **Worst moment — the problem, not the fix:** *"The single worst moment: what happened, and what did you feel?"* If the tester offers a fix, capture it under a separate tag, **"tester's hunch — not the data,"** so it never gets mistaken for the finding.

The report stamps **who played** (from the Who-Are-You panel) at the top, because the same build lands differently for a cold first-timer and a target user — the signal is only readable next to its rater.

## WHAT DOESN'T CHANGE
The six floors (rides on top / phase auto-tag / clipboard-only, no network / accessibility / provenance / the founder cold-plays the wrapper first) are correct and stay. This is a swap of the **signal design**, not the rig.

## MIGRATION
- Fold v2 §3/§4 into `os-block-playtest-instrument.md` (it is locked; founder ratifies before re-lock).
- The recent v7 playtest used the *weak* two-question frame. Its findings still hold (behaviour leaked through — "it's a doorbell not a toy," "the cat should cackle"), but re-running the three v7 personas through the v2 protocol would sharpen the comprehension-gap and dead-zone data specifically.

<!-- MANIFEST: this optimizes the SIGNAL layer only. Next: (1) founder ratify; (2) fold into the os-block; (3) optional re-run of the v7 playtest through v2. -->
