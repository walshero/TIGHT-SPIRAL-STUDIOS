# SIGNAL REVIEW — Horvath + the Instrumentation Alephs
<!-- 2026-08-02 · design lane · convened by the founder BEFORE wiring the humor model into the game: "make sure we are emitting the clearest signals and receiving the richest data." Two lenses: the Instrumentation Alephs (Borges' Aleph — see the whole I/O at once, then ask one thing; grounded in os-block-playtest-instrument.md v2, os-block-hollow-claim, os-block-truth-ticks) and Agnes Horvath (liminality; permanent-liminal → trickster). Reads against funny-bonies-humor-model.md. -->

## THE FRAME — two channels, one picture
A game is an instrument with a **loop**: it **EMITS** signal to the player (the reveal, the teaching line, the gap) and **RECEIVES** signal back (the player's call). "Clearest signal / richest data" is a demand on *both* directions. The humor model changes both — so instrument it before wiring it.

Map the whole picture (the Aleph view):
- **EMIT (game → player):** the verdict + gap track; the NEW "why it landed" teaching line (filter, universal/cultural); the last-miss anchor; the duet (you · friend · room); the Maker whisper.
- **RECEIVE (game → its model):** the player's **call** — a single number 0–10. The duet adds a second number. That is the entire inbound channel.

## THE INSTRUMENTATION ALEPHS — total-view, one finding each

**Aleph‑1 · the whole I/O at once → THE ASYMMETRY.** The humor model makes the game able to *emit* rich, explainable signal (why a bit landed, universal vs cultural). But the game *receives* one scalar — a bet. **We are about to teach with a paragraph and listen with a thermometer.** The richest datum the model implies — *did the player understand why?* — is never captured. Clearest-emit without richest-receive is a lecture, not a loop.

**Aleph‑2 · the receive channel → A SCALAR CAN'T TELL A READ FROM A GUESS.** "7" that's right and "7" that's lucky are indistinguishable to the game; so is "the player gets the universal/cultural distinction" from "the player rolled a number." To train humor literacy (the whole point of the model) the inbound signal must carry the player's **model**, not just their **magnitude**. Fix: one cheap second signal that captures *reasoning* — a pre‑reveal prediction of *why* (see spec). This is the v2 instrument's own law imported into the game: *capture what the player DID and MODELED.*

**Aleph‑3 · the emit channel → ONE THING TO LOOK AT.** The v2 instrument floor is "one thing to look at" per screen. The reveal already carries a verdict + a two-marker gap; adding a filter name, a universal/cultural tag, and a benign-line note risks **four numbers and a paragraph**. Clearest-emit means the reveal names the gap (one thing) **and exactly one why** — attributing the miss to **context** (cultural — "no shared language here") *or* **tone** (benign line — "too edgy for this room"), in plain words, never jargon. Emit less, land it.

**Aleph‑4 · the honesty tick → THE "WHY" MUST BE COMPUTED, NEVER COMFORTING.** Studio law (os-block-hollow-claim, truth-ticks): never emit a claim the system didn't actually produce. The teaching line must be the model's *real* attribution, not a flattering post-hoc story. If the miss was genuinely mixed (both context and tone), emit "both mattered" — do **not** fabricate a clean single reason because it reads better. A humor trainer that lies about why a joke bombed is the hollow-claim failure wearing a lab coat.

## HORVATH — keep the liminal generative, not a trickster metric

- **The model's core is *already* a threshold — protect it.** Benign Violation is a *window* between too-safe and too-edgy: the funny lives in the in-between. That is Horvath's **generative liminal** made literal. Good. The instrumentation must keep that window **open** (a space the player explores) and never collapse it to a single "correct" number to hit.
- **Emit REVELATION, not GRADE.** "Why it landed" should open a door (a discovery about how humor works — generative); the moment it reads as a *report card*, the player flips to closed-mode optimisation — the trickster spiral the last advisory warned of. Keep the why a revelation and every score a whisper.
- **Instrument the player as a *player*, not a subject.** The richer receive-signal (Aleph‑2) is a trap if it becomes a *test the player can fail* — that manufactures the exact metric-gaming Horvath fears. It must be framed as **play** ("what do you think will carry?"), a guess, not an exam. Capture the model to **teach**, never to rank.
- **Never let the rich data become a leaderboard.** The whole reason to capture the player's reasoning is the teaching moment, not a new axis to score. The instant it's a rank, the liminal goes permanent and the game becomes the trickster it indicts.

## CONVERGENCE — the one instruction
> **Enrich the RECEIVE channel by capturing the player's *model* (a single cheap prediction of *why* a bit will land — universal vs. this-room), and keep the EMIT channel a *truthful revelation* — the gap plus exactly one plain-language reason (context vs. tone), computed by the model, phrased as discovery, never a grade.**

Both lenses land there from opposite doors: the Alephs (close the loop — listen as richly as you teach; emit one true thing) and Horvath (keep it play and generative — reveal, don't grade; model, don't rank). Clearest signal **and** richest data **and** it stays open.

## INSTRUMENTATION SPEC (folds into the humor-model wiring)
When `actualFor` is re-grounded (funny-bonies-humor-model.md §6), carry this:

**RECEIVE — add one signal that captures the model (not a second score):**
- Keep the bet slider (magnitude).
- Before the reveal, one lightweight **prediction of *why*** — a two-tap: *"Will this carry because it's **physical** (lands in any room) or because **this room gets it**?"* One tap. It's a guess, framed as play. That tap is the humor-literacy datum: it tells the game whether the player has the universal/cultural distinction — the thing the model exists to teach.

**EMIT — one thing + one true why:**
- Reveal shows the gap (the one thing to look at) **and one plain reason**, chosen by the model: **context** ("this room shares no language — only the physical beat landed") or **tone** ("the room's line is gentler than that — it read as too much"). If attribution is genuinely split, emit "both mattered" (Aleph‑4 honesty).
- Cross the prediction with the outcome for the teaching beat: *"You bet on the wordplay; the room had no language for it — the pratfall is what carried."* That single sentence is where humor literacy is actually trained — and it's a revelation, not a mark.

**GUARDS (standing):**
- Every score stays a whisper (Horvath).
- The why is always the model's real attribution (Aleph‑4 / hollow-claim).
- The prediction is play, never graded or ranked (Horvath).
- One thing to look at per screen (Aleph‑3 / v2 instrument floor).

<!-- MANIFEST: reviewed the humor model's signal I/O before wiring. Finding: the model makes EMIT rich but leaves RECEIVE a scalar; close the loop with ONE model-capturing prediction and ONE truthful reveal reason, kept as play, never a grade. This changes funny-bonies-humor-model.md §6 (add the why-prediction to RECEIVE; constrain the reveal to gap + one true reason). Next: founder ok on the spec, then wire the model + this instrumentation together. -->
