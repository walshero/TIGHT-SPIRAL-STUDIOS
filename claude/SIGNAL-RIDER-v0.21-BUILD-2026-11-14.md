# Signal Rider v0.21 — build notes, 2026-11-14
<!-- source: founder 2026-11-14 14:00 "1 idk. 2. Y. 3 y. And implement advised changes" | base canon v0.20 303844ec | script claude/signal-rider-build-v21.py | status: LAB, awaiting founder phone play -->

This build implements the Playtest Table report (`claude/playtest/SIGNAL-RIDER-v0.20-TABLE-2026-11-14.md`).

## What changed
**Rulings**
- **Week stress is load, not hits.** Pink cubes slow you and widen frayed bands. The HUD shows "Load n" beside Hits, and load never ends a ride. Hits come from frayed bands and gaps that do not fire.
- **The speedometer shows the science.** It reads 75 m/s and drops only in a frayed band. Greens still surge the ride.
- **Predict first.** On ride 2 and later, the tray asks "more, the same, or fewer landing spines than last ride?" before showing the effects panel. One tap reveals the panel, and the Ride button is never blocked.

**Tier 1 fixes**
- Hold and arrow keys now steer the same way as drag.
- Grown spines are re-laid evenly on the thinking face, away from the alarm face, and a match always counts as a match.
- A red group adds load once.
- The calm road and support-only weeks deal plain "A hard moment" cubes, never named stresses the player did not pick.
- Stale rule text is rewritten in the legend, Library and fade card.
- On the stressed face, spines are drawn above the key disc, so none is hidden on beat 0.

**Tier 2: learning truth**
- The week's frayed-band width applies on the last leg only.
- Bands knit back at 0.05 per second after 4 clean seconds.
- Wording fixes:
  - The sleep line now cites hippocampus evidence (Havekes 2016).
  - Spine changes are said to take days to weeks (Radley 2005, Vyas 2002).
  - "Missed the bus" now cites control, not predictability.
  - "Feeling alone" uses Liu 2012 (isolation thins prefrontal myelin) in place of the mortality statistic.

**Tier 3: gameplay and engagement**
- **Landing:** a target can be up to two spines away. On the stressed face, 60% of targets are the spine farthest from the pull. The next shape shows above the tube, labeled "next".
- **Pacing:** blocks come in two sets per leg (at 6/20% and 58/72% of the leg). Frayed bands skip the rests, so curves have room.
- **Leg 1** opens with a green group, then a red.
- **Chained greens** rise two semitones each, and the surge stacks up to 1.7x.
- **Spoken names:** a card's name is spoken the first time only.
- **End card:** travel time is the headline, with best this visit (held in memory only).
- **Try next** is a button: "Add <category> and ride".
- **Tray:** the intro is cut to one line, research sits behind "Why?", and the Ride row stays pinned to the bottom of the tray.
- **Warm-up:** adds one practice gap (2 beats, needs 1 match, no fail state).
- **Rose to it:** hitting the test cube within 2.5 s of a green becomes a surge (stress reappraisal, Jamieson 2012).

**Access**
- Cube icons sit on a dark disc.
- The Wrong shape and Missed labels are #ff8fc4.
- Thinking spines are #ff9ed2 and alarm stars #d1003f with a light outline.
- Lightning has a setting, follows reduced motion, and is capped at 3 per second.
- Skip replay sits at the bottom, in thumb reach.
- Leaving mid-ride asks first.
- A mute button is always in the top bar (Senses E2/E3, WCAG 1.4.2).

## Verified (scripted, 390x844, headless Chrome)
- **Steering:** hold Right moves the spark right on screen in tube-still mode (cos theta 0.00 to 0.75).
- **Hard week, bot matching every beat:** reached the thinking cortex, grew 2 spines, 0 hits, travel time 17.3 ms. On v0.20 the same scenario lost 4 out of 4.
- **Red group:** crossing between two blocks of one group gave load 1, hits 0.
- **Calm road:** only "moment" pink cubes.
- **Prediction:** hidden on the first visit; after a ride it shows and hides the panel; a tap gives "Right: 2 spines this week, 5 last ride."
- **Contrast gate:** SHIP (every text token clears 4.5).
- No page errors in any run.

## Held, with reasons
- **Dale's principle landing** (one messenger shape per synapse; learning seat F4) is not built. It would replace the founder-approved shape-match mechanic, so it waits for a founder ruling.
- **Ghost spark, shareable week card, student playtest:** wishes, unchanged.
- **Human difficulty is UNPROVEN.** The bots are perfect players. Only phone play can tell whether load-not-hits made the game too easy. If it did, the first lever is frayed-band density inside the sets.
