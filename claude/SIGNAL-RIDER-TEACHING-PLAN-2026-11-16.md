# Signal Rider: teaching plan, 2026-11-16
<!-- source: founder 2026-11-16 21:05 "Let's get back to teaching more. What do Horvath Osterweil and other suggest?" | inputs: claude/playtest/horvath-2026-11-06.md, osterweil-2026-11-06.md, signal-rider-v0.20-learning.md | build at time: v0.22 (c06b279f) | status: PENDING founder pick -->

## The panel's shared diagnosis
Signal Rider teaches mostly through words: captions, flashes, the Library. The mechanics teach "steer and match." When text and mechanics disagree, players learn the mechanic (Habgood & Ainsworth 2011, intrinsic integration). So the fix is to make the science the action and let the words name what was just felt (Gee; Schwartz & Bransford 1998, "A Time for Telling").

## Already built from their lists
- Alarm spines and the alarm ending
- Spines sprout and dim on the last leg
- Only frayed bands count as hits (load ruling)
- The week reaches the last leg only
- No sentences while steering
- Wording fixes
- A prediction before ride 2

## Not yet built, ranked by teaching return
| # | Move | Seat | Teaches | Size |
|---|---|---|---|---|
| 1 | **Live balance and spine preview.** Each cube tips the bottom-left beam the moment it lands, and a row of spine dots beside it gains or loses one. You carry that row into the cortex face. | Horvath #2, Osterweil #3 | One cause, one visible effect: the week sets how many places the thinking cortex has to land | M |
| 2 | **Fill the next neuron.** The landing ring is a threshold that leaks between beats. Relays 1-3 fill on the first matches. The stressed cortex fills slowly while the alarm fills on its first touch. | Horvath #1 | Summation and threshold; "same effort, less answer" under stress (Arnsten 2009) | M |
| 3 | **Bare stretch.** One stretch of uninsulated fiber where the spark crawls (readout near 1 m/s), then the insulation begins and the spark hops ring to ring. Name it "myelin" only after. | Horvath #5 | Why insulation matters, felt before it is named (OpenStax 12.4) | M |
| 4 | **Ghost spark.** "Change the week" replays your last ride's spark alongside you. | Osterweil #6 | Experiment: two weeks side by side, ungraded | M |
| 5 | **Misconception card.** "Will a hard week slow your touch?" asked before the ride and flipped after it. | Horvath #4 | Targets the top wrong belief (refutation; Schroeder & Kucera 2022) | S |

## Chair recommendation
Build #1 first, then #3. Hold #2 until the founder has played v0.22's three-match landing.

## Founder pick, 2026-11-16 21:07: "5."
Read as option 5 of the reply: the advanced set (the plan's moves #2, #3 and #4). All three are built as v0.23 (`claude/signal-rider-build-v23.py`, checks in `claude/signal-rider-v23-checks.py`):
- **Bare stretch:** the first ride of each visit opens on 13 units of fiber with no insulation. The spark creeps at 0.4x and the readout says 1 m/s. Then the myelin wraps on, with a flash and full speed. A caption and the voice name it afterwards. The crawl does not count toward travel time.
- **Leaky ring:** a beat with no match drains the charge (relays -0.5, the thinking cortex -0.4). The alarm's charge never leaks. The relay ring shows the live charge.
- **Ghost spark:** the next ride shows a dashed ring where your last spark was.

**Verified:** the readout fell to 1 in the bare stretch and returned to 75 after it. Both captions appeared. The charge went 1, 0.5, 0 across two missed beats. Ride 2 had no bare stretch and a 98-sample ghost. No page errors. Contrast gate SHIP.

**Still open:** the live balance and spine preview (#1) and the misconception card (#5).
