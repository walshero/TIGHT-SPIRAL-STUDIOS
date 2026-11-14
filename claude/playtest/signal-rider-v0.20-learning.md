# Signal Rider v0.20: Learning seat (learning science and neuroscience accuracy)

Played at 390x844 with an autopilot on an instrumented copy (`learning/instrumented.html`, which adds only a read hook; the build itself is untouched). Runs: one calm road, four hard weeks (night, phone, pile, food, alone, loud), and one deliberate fail followed by a checkpoint restore. Screenshots and logs are in `sr-table/learning/shots/`. I read the replay clips in the code but did not play them.

## 1. What works (keep)

- **No reading while steering.** In the ride, banners show a title only, and teaching lines wait for the calm stretch after a relay fires (`lesson()`/`flushLesson()`). Horvath item 6 is fixed. This follows Mayer's segmenting and modality principles.
- **Threshold and summation are real mechanics.** Too little input means "Did not fire." Part of a partial fill carries over (`missLanding`: `fill*=0.5`). This is the biology of a neuron firing (OpenStax A&P 2e, 12.5), taught through play.
- **The cortex has fewer spines under a hard week, and the alarm neuron fires first.** This matches the direction of Radley et al. 2006 (Cerebral Cortex: repeated stress causes spine loss in rat mPFC) and Arnsten 2009. The "protecting you, not failing" line is good trauma-informed framing.
- **Claims fixed since the Horvath seat:** the friend card is now sourced (Heinrichs 2003), the meal card is gone, Practice now means only the fulcrum, and the fade card reads "damaged insulation can stop a signal."
- **"Words for what you felt" comes after the experience.** The vocabulary arrives after the player has felt it. Keep it.

## 2. Top findings, ranked

**F1. Collecting greens on leg 4 makes the thinking cortex lose (bug, wrong lesson). Size S.**
- **Evidence:** in 4 of 4 hard-week runs, an autopilot that matched every beat ("10 matches, 0 wrong") still ended "The survival shortcut fired first." `hard4.out` logs the cause:
  - Each green grows a spine at `pads[last]+0.55` (line ~989). The grown spines land at -1.09 and -0.54 rad from the alarm, inside the alarm face (±1.0).
  - `landingBeat` records the beat as a MATCH (green flash, screenshot `hard-34-leg3-land.png`) and then counts it as an alarm landing, because the `onAlarm` check runs first.
- **Why it matters:** the player does the right thing, is told "Match," and loses anyway. Maier and Seligman (2016, Psychological Review) show that perceived control is what protects against stress. This bug teaches the opposite: effort and support do not matter. It also makes the end card's advice ("steer against the pull and leap at the thinking spines") false.
- **Fix:**
  - Place grown spines only in the arc away from the alarm, at least 0.4 rad from any alarm spine.
  - Check `onAlarm` before the verdict is recorded.
  - Add a regression check: a perfect aimer wins a hard week at least 1 time in 3.

**F2. The speedometer says stress slows a touch signal. Size S.**
- **Evidence:** on the fingertip leg, a "Short nights" hit drops the readout from 74 to 22 m/s (`fail-effect-82.png`). After a green the readout climbs to 92. `vReal` scales `run.v` directly.
- **Why it matters:** a short night does not change conduction velocity in a peripheral touch fiber. Myelin and axon diameter set that velocity (OpenStax 12.4). Horvath flagged this (item 3), and it is still open. The founder ruled that greens accelerate and reds slow (v0.16), and that ruling can stand as game feel. The problem is the number in meters per second, which presents the game's momentum as physiology.
- **Fix:**
  - Keep the speed changes, but the m/s readout moves only on frayed bands. That is true: demyelination slows or blocks conduction.
  - Otherwise the readout holds the fiber's real value.
  - Optional: show the real value per leg, falling to about 10-30 m/s for central pathways. The tray and end-card lines that say "each a speed surge" stay as game language.

**F3. The week decides whether touch reaches the brainstem. Size M.**
- **Evidence:** a hard week fades the signal at relay 1 (fail run: two "Short nights" hits plus one failed leap ended on the fingertip leg). The week widens the frayed bands from the first unit (`band0`), and since v0.12 relays 1-3 can fail.
- **Why it matters:** the end card claims "The touch itself got through the first three relays just the same." The mechanics say it did not. Horvath's core repair, "stress does not stop you feeling a touch" (Arnsten 2009: the effects fall on prefrontal circuits), is reversed by play. When text and mechanics disagree, players learn the mechanic (Habgood and Ainsworth 2011, intrinsic integration).
- **Fix:**
  - On legs 1-3, frayed bands start at the calm width whatever the week.
  - Pink hits there still cost speed and count toward the three hits (the founder's ruling), but the week loads its effects only onto leg 4.
  - A failed leap at relays 1-3 says "Missed the timing" with no reference to the week, and the relay fade line drops "Greens give you more landing spines" (relay 1 always has 5).

**F4. The landing teaches aiming and switching messengers. Size M.**
- **Evidence:** at relay 1, each of 5 spines carries a different receptor shape, and the messenger shape changes every beat (`calm-land-leg0.png`).
- **Why it matters:**
  - Real neurons do not aim. The presynaptic terminal already sits on its spine, and release is probabilistic.
  - One neuron releases the same main transmitter at all its terminals (Dale's principle); the touch relays use glutamate.
  - Receptor specificity is true and worth keeping, and so is the founder's "real work, slight puzzle."
- **Fix:**
  - One messenger shape per synapse.
  - Spines show mixed receptor shapes, which is true: dendrites carry receptors for several inputs.
  - Each beat, the matching spines that are within reach light up, so the puzzle becomes "which matching spine can I reach on this beat," and the beats must land inside a decay window (temporal summation).
  - Library line: "A real signal does not steer; the game lets you ride one."

**F5. The Library and legend contradict the build. Size S.** Wrong now:
- "Greens... do not change your speed" (legend) and "Nothing in the ride speeds you up" (Library). Both are false since v0.16.
- "Every bad that pops up." There have been no pop-ups since v0.9.
- "Each card you load shows up as a picture during the ride." Removed.
- The old five-card deck with "a meal."
- "Line up with a lit spine to land." The landing is now a shape match.

Rewrite these from the current DECK and CATS.

**F6. Science claims to reword. Size S.**

| Where | Now | Corrected wording |
|---|---|---|
| CATS sleep fx; Library "What's happening" | "Each sleep block takes one landing spine from the thinking cortex." "A long stretch of short nights thins the landing spines in the thinking cortex." | The sleep evidence is for the memory center: "In mice, 5 hours of lost sleep cut spines in the memory center (hippocampus)" (Havekes et al. 2016, eLife). For the cortex: "A long run of hard weeks thins spines in the thinking cortex (rats; Radley 2006)." |
| Replay WHY, sleep | "Landing places relight overnight." | "After practice, sleep helps new spines form (mice; Yang et al. 2014, Science)." |
| Legend; Library lights | "After a green, the thinking fibers light up and grow new tips." Alarm fibers "grow spiky cell bodies" after one bad. | Add the timescale: "Over days to weeks..." Spine regrowth (Radley 2005, Exp Neurol) and amygdala growth (Vyas et al. 2002, J Neurosci) both took repeated stress or recovery over days, not seconds. |
| Leg-4 pink "dims one spine" | Instant spine loss | Keep as a game beat, but the end-card line should say "the game's shorthand for weeks of load." |
| Missed bus | Predictability attributed to Maier and Seligman | Their paper is about control. Reword to "A surprise you cannot control..." and cut "predictable stress is easier." |
| Feeling alone | Mortality odds (Holt-Lunstad) | A mortality figure is a trauma-informed risk for this audience. Consider Liu et al. 2012 (Nat Neurosci): social isolation thinned myelin in the prefrontal cortex of adult mice. It is on-model and ties "alone" to insulation. |

**F7. No retrieval or prediction, and the choices do not match the ride. Size S.**
- **Choices vs ride:** a stress-only week shows 8 greens the player never chose ("A friend who listens" right after "Feeling alone"). The calm road shows stress and support blocks from the full deck (`bagDraw` fallback).
- **No retrieval:** nothing asks the player to recall or predict anything.
- **Fix:**
  - Empty pools spawn unlabeled blocks.
  - Before ride 2, add one tap: "Same week. Will your touch reach the brainstem slower?" Flip it on the end card. Retrieval beats restudy (Roediger and Karpicke 2006). Needs F2 and F3 first.

## What a player believes

**After one ride:**
- **Correct:** signals cross a gap, and enough must land to fire. Frayed insulation slows a signal.
- **Wrong:**
  - A bad night slows my touch nerve to 22 m/s.
  - Stress can stop me feeling a touch.
  - A signal aims at one landing spot, and neurons switch messengers every beat.

**After three rides:**
- Under a hard week, nothing I do saves the thinking cortex (F1).
- The ride's greens are not mine (F7).
- The causal model in the tray (spines, pull, band width) is the best teaching in the game, but play currently overrides it.

## 3. The one change first

F1: a two-line placement fix plus a check. Until it lands the game teaches helplessness to the students the ITAR framing protects.

## 4. Wishes

- **D18 bare stretch.** A short unmyelinated segment where the spark crawls before the ringed fiber. This is saltatory conduction felt by contrast. Still unbuilt (WISH).
- **Live spine preview in the HUD on leg 4.** Each green or pink visibly adds or removes a spine as you ride (Horvath item 2, partial).
- **A "weeks later" epilogue ride.** The same week with supports added, framed as recovery over time (Radley 2005).
- **Map receptor shapes to real families** (glutamate, GABA) in the Library only. UNPROVEN as a learning gain.
