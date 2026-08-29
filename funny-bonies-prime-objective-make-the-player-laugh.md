# PRIME OBJECTIVE — make the PLAYER laugh (a design advisory)
<!-- 2026-08-02 · design lane · founder: "My objective is to get player to laugh. Advise design with that as prime objective." A strategic reframe. Panel convened with agency: Cleese (open mode), the humor model (benign violation), Saunders (character), the Green Room (did they ACTUALLY laugh). This supersedes the calibration-first emphasis where the two conflict. -->

## THE HARD TRUTH (say it first)
We have been building a game **about** funny. The prime objective needs a game that **is** funny — one that produces the laugh, not the understanding of it. **Understanding humor and feeling humor are different faculties, and they fight.** E.B. White: "Humor can be dissected, as a frog can, but the thing dies in the process." Cleese says the same in his terms: analysis is *closed mode*, laughter is *open mode* — the instant a player is rating, being graded, or being taught, the laugh is gone.

So the sharp diagnosis: **the read-the-room loop makes the CAT laugh. The prime objective is to make the PLAYER laugh. Those are different games — and we've mostly built the first one.** The good news is the second game is already hiding inside this one.

## WHERE A PLAYER ACTUALLY LAUGHS HERE (there's exactly one place — study it)
The **Sisyphus cold open.** Drop the boulder → it flattens the pointing boss → Sisyphus throws his arms up → tap again, the boss pops back and gets flattened again. If anything in this game earns a real exhale-laugh, it's that. Why it works is the whole answer:
- **You caused it.** Self-authored absurdity is funnier than watching. Your tap made the boss get squashed.
- **It's physical, not verbal.** No reading. Universal. Immediate.
- **It's a surprise you *experience*, not a fact you're told.** The flatten happens *to* you, in time.
- **It escalates / repeats with variation.** The eternal loop is a running gag — and running gags are how games get the *second* laugh.
- **It's benign and deserved.** Superiority + safety = the clean laugh.
- **There's a character to be fond of.** You're on Sisyphus's side.

That is not the intro to the game. **That is the game** — the rest hasn't noticed yet.

## THE LAUGH LEVERS (the framework — design to these)
A player laughs when:
1. **Surprise, experienced not explained.** The payoff must *happen*, with timing, never be reported as a number.
2. **They caused it.** Put the absurd consequence downstream of the player's own action.
3. **Escalation + the callback.** Gag two is bigger; gag three calls back to gag one. Games live on the running gag.
4. **Timing — the beat.** Comedy is the pause before the payoff. The game controls that pause; use it (anticipation → release).
5. **Physical over verbal.** Slapstick is the universal floor (the humor model's own finding). Sight-gags beat wordplay for a first laugh.
6. **Variation so it doesn't die.** The third identical flatten stops being funny; randomize the *how* (different squash, different overreaction).
7. **Benign + character.** Safe, deserved, and starring someone you like.
8. **No grade in the moment.** Any scoring/quiz/teaching must be OUT of the joke's path, or it kills open mode.

## AUDIT — the current design against the prime objective
| Piece | Serves "player laughs"? |
|---|---|
| **Sisyphus cold open** | **HIGH** — the template. The one real laugh. |
| **Read-the-room loop** (pick bit → pick room → bet a number → reveal a gap) | **LOW** — it's a *calibration quiz*. The player reasons; they don't laugh. The v2 playtest already caught this ("screen 1 is a toy, screen 2 is a quiz"). |
| **The hunch + teaching reveal** ("you called it / here the body carried it") | **LOW→NEGATIVE** — it's analysis at the exact moment a payoff should land. Closed mode by construction. |
| **The humor model** (universal/cultural, benign violation) | **INVISIBLE (good) as an ENGINE; bad if foregrounded.** It should *decide what's funny under the hood*, never be shown to the player. |
| **Reply loop / duet** | **SIDEWAYS** — it's connection, not laughter. Shared laughter is great, but the duet compares *numbers*, not jokes. |

The pattern is stark: **one piece targets the laugh; the spine targets the rating.**

## THE REORIENTATION (the recommendation)
**Move the player's verb from RATING funny to CAUSING funny — and turn every payoff from a score into a staged gag the player watches happen.** Keep the humor model as the hidden engine; kill it as the visible experience.

Concretely:
1. **The reveal becomes a gag, not a number.** Right now "pick The Chicken for the kids" pays off as *"6/10, you were 2 off."* Instead: **the bit gets performed to the room, physically, and lands or bombs in a visibly funny way** — the chicken actually launches, the room reacts as slapstick, a bomb is its own joke (crickets, one slow clap, a tumbleweed). The humor model still decides the outcome; the *player experiences comedy instead of a grade.* This salvages the whole read-the-room investment by pointing it at the laugh.
2. **Make "you caused it" the core.** The player's action should trigger an absurd, physical, surprising consequence every single round — the Sisyphus relationship, generalized.
3. **Build the running gag + variation.** Recurring characters (Buster, Sisyphus, the boss) with escalating, varying bits and callbacks. The second laugh comes from "oh no, him again."
4. **Demote the number to a whisper, or cut it.** Calibration can survive as a quiet undertone ("you're getting a feel for this room"), never as the payoff. If it fights the laugh, it loses.
5. **Use timing.** Add the *beat* — the wind-up and the pause — before every payoff. This is nearly free and it's most of comedy.
6. **Bombing must be funny too.** The studio floor ("a flat gag is a fact, not a failure") becomes a comedy asset: a bomb is a *different* joke (the awkward silence), not a red X. Never punish; always pay off with a laugh of some kind.

## KEEP THE FLOORS — and note the honest twist
The studio's anti-hollow-claim rule *helps* here: **the player's laugh is the one signal you cannot fake, and don't have to** — it happens in their own body, self-verified. You are not claiming a laugh landed; you're trying to cause a real one. That's the honest version of a laugh-first game.

## THE ONLY METRIC THAT MATTERS NOW
Stop measuring comprehension. **Measure the laugh.** The v2 instrument already has the right probes — *"Something moved in me"* and *"Show-someone-this."* Make those the scoreboard: did they exhale/smile/laugh, where, and did they show someone. The Green Room's job flips from "did you understand it" to **"did you laugh — and when."** A build that teaches perfectly and gets zero laughs has failed the prime objective.

## SET EXPECTATIONS (honest)
Real laughs are hard; most comedy games earn a *smile* and an occasional *"heh,"* and the true peak is the **"show someone this"** shared laugh. Aim there. Surprise and timing carry the first laugh; character and the running gag carry the rest; variation keeps them alive. Plan for the exhale, treasure the laugh, engineer the share.

## RECOMMENDED FIRST MOVE
Prototype **one round of the reoriented loop**: pick a bit → a short *beat* → the bit **performs to the room as a physical gag** with a surprising, varying outcome (kill / smile / bomb, each its own joke) → a whisper of feedback, no grade. Reuse the Matter.js physics we just proved. If that round makes a playtester exhale, it's the new spine and the calibration quiz retires to a footnote.

<!-- MANIFEST: prime objective is the PLAYER's laugh, not the player's calibration. The Sisyphus cold open is the only piece that serves it and is the template; the read-the-room loop serves the wrong objective. Recommendation: move the verb from rating to causing, turn every reveal into a staged physical gag (humor model as hidden engine), build running gags + timing + variation, measure the actual laugh. Next: prototype one reoriented round. Awaiting founder greenlight on direction. -->
