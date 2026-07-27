# FUNNY BONES v7 — POST-REBUILD REVIEW: Aleph · Funes · Playtesters
<!-- convened 2026-07-27 · reviews the v7 rebuild on branch claude/funny-bones-cold-opening-pn51ay -->

## ALEPH (founder-canon)
**Verdict:** honors the canon in craft — the game finally has a game in it — but it spent the session *rebuilding*, the one thing the finishing finding says the studio does not need.
- **Upholds:** the moat (calibration) is now in the hand — the player owns the bet; "a fact about this room, not a fail" is the Dignity floor (§3.1) transposed into play; one decision per screen (screens replace, not append); offline law enforced on the front door (Supabase POST + shipped key removed).
- **The flag Matt would raise:** *the meta-machine and the social score are still gone* — "the whole reason the idea was exciting" (founder-canon #5) — and v7 now also files away the Glass Engine. The loop is real; the reason you cared is still homeless. Rebuilding was the right call (you can't finish a game that never became a game), but it displaced the finishing list (the Tell cards, the Borges paper, Diagnose mode — "they need a push, not design").

## FUNES (memory)
**Verdict:** CLEAN. All gates pass, canon held, branch pushed, nothing stale, nothing re-litigated.
- ratchet **0 regressions** (known debt 22); studio-eyes **funny-boneys CLEAN**; preship **SHIP** (6.64).
- The comfort control stayed the canonical **five stops** (the toggle misstep was reverted within the session); the text-size axis was folded into `comfort-control.html` canon, not bolted on.
- Offline law clean: index ships **0 fetch/keys**; the rebuilt game makes **zero network calls**.
- **One standing caveat (not a flag):** the 15 commits are pushed to origin but **not merged to main** — canon (main) does not yet carry the rebuild. That is a push, not a merge; the merge is Matt's/Josh's hand.
- **Finished this session:** the Funny Bones rebuild (a homeless shelf-only silo got a push), the offline-clean front door, the canonized size axis.

## PLAYTESTERS (three played the loop; two questions: does it do its job / what surprised me)
**Cold first-timer:** "Got it" by ~second 8, made a real guess, felt the gap, went again *twice* to crack the grown-ups room. But: the intro auto-advances and can't be skipped; "Call it" is disabled with no explanation; no score/streak, so after 4–5 rounds he'd memorized the answers and had nothing to chase. Would send to a friend "as a neat little thing," not a must-play.

**Kid / casual:** the machine tap is the **star** (real Rube Goldberg giggle) — "but I only get to do it *once*. The one thing that felt like a toy is a doorbell, not a toy." The game it drops into reads as "homework" (a slider prediction quiz), and the payoff usually *doesn't* laugh — the cat only cracks up at 6+/10, so most calls earn "a polite half-smile and a gentle lecture." One-line fix: **let me tap the machine again, and let the cat actually cackle on a good call instead of grading me.**

**Educator / assessment:** it teaches **calibration/norming** convincingly and is genuinely **learnable** (deterministic `base×taste`; Chicken→kids = 8 vs Chicken→grown-ups = 4 is the money moment). Two real gaps: (1) it measures *predicting the room*, not *discovering your own bias* — "my taste ≠ theirs" is a **caption, not a mechanic** (the game never captures what *you* find funny); (2) **no memory is surfaced** — `lastmiss` is a bare "4 off" with no gag/room label and it carries across a room switch, so it can advise about a room you already left. Also the rounding compresses the scale (floor 2, ceiling ~8 — the top third of the slider is dead).

---

## THE PUNCH-LIST (what all five converge on, ranked)

**P1 — cheap, high-value, said by multiple players:**
1. **Make the machine replayable + skippable.** It's the best thing in the build and you get it once. Let a tap replay the chain; let a tap skip the intro on the way in. *(kid, first-timer)*
2. **Let a good call feel like a win.** The cat should crack up on an accurate/close call — reward *calibration*, not just a high actual. Right now most plays earn a graded half-smile. *(kid)*
3. **Explain the disabled "Call it"** ("pick a bit and a room first"), and nudge the slider so it doesn't read as a pre-filled answer. *(first-timer)*
4. **Fix `lastmiss`:** label it with the gag+room, and scope it to the room (don't carry a miss across a room switch). *(educator, first-timer)*

**P2 — the progression gap (the "nothing to chase past round 5"):**
5. **Surface memory:** a small per-room history ("this room so far: chicken 4, boing 6…") so calibration is *legible* and improvement is *seen*, not just felt. *(all three)*
6. **Capture the player's own taste** (rank what *you* find funniest) so "my taste ≠ theirs" becomes the mechanic, not a caption — the sharper assessment point. *(educator)*

**P3 — canon / the reason Matt cared / into the world:**
7. **The meta-machine + social score** — connect players' machines into one story. Aleph: the heart of why the idea was exciting; still homeless (filed as a Bench wish). Decide if v8 is where it returns.
8. **Deploy:** merge branch → main so canon carries the rebuild (Funes); and weigh the finishing list the rebuild displaced (Tell cards, Borges, Diagnose — pushes, not builds).

<!-- MANIFEST: P1 is a short, safe pass (replay/skip the machine, celebrate a win,
explain the disabled CTA, fix lastmiss). P2 is the progression layer that makes it
sticky and teaches better. P3 is founder-level: the meta-machine, and merge-to-main.
Re-run the two standing axes after P1+P2 land. -->
