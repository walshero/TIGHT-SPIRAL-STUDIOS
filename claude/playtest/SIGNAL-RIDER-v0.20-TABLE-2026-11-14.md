# Signal Rider v0.20 — Playtest Table, 2026-11-14
<!-- source: Matt directive 2026-11-14 "Signal rider. Use playtesting agent suite to look for improvements based on research. Gameplay and learning and engagement are top priorities." | build: lab/down-the-nerve.html v0.20 (repo 15a8047) | owner: mwalsh | status: filed, awaiting founder ruling -->

Four seats played v0.20 at 390x844 in headless Chrome, driven by scripted players (warm-up, full rides, fades, checkpoint return, end card, replay, all-stress week, reduced motion). Seat reports sit beside this file: `signal-rider-v0.20-{gameplay,learning,engagement,trauma-access}.md`. Anything about how hard the game feels to a real human is UNPROVEN until founder or student play. Nothing in the build was changed.

The chair checked the two biggest claims in the code before filing:
- Steering: keys and hold add to `run.theta` (line ~965), while drag subtracts (`run.theta-=dx*0.012`, line ~619). The two input modes disagree, so this is confirmed. The gameplay seat saw hold-Right move the spark left with "Tube stays still" on.
- Greens on the last leg: a grown spine is placed at `last pad + 0.55` (line ~993). `landingBeat` tests `onAlarm` before `full`, so a match on a grown spine near the alarm face counts toward the survival shortcut. This is confirmed: the learning seat lost 4 of 4 hard-week runs after matching every beat.

## The convergent ruling (single blocking check for v0.21)
**Make the game's rules true.** Three of the four seats, working independently, found the game saying one thing and doing another:
- Effort and support can lose the last leg.
- The speedometer drops on a bad night.
- The calm road deals rent and loneliness cubes.
- The tray and Library still say "greens do not change your speed."
- Damage the Library says recovers never recovers in the ride.

When the system contradicts its own text, the player learns helplessness. That is the opposite of the resilience goal. Fix the truth layer before adding anything new.

## Tier 1 — bugs and contradictions (all S, do first)
| # | Fix | Seats | Owner · date |
|---|---|---|---|
| 1 | Make hold and keys steer the same way as drag (one sign) | gameplay | fix · build v0.21 · 2026-11-15 |
| 2 | Grown spines are placed away from the alarm face; a match always counts as a match; add a regression check | learning | fix + test · v0.21 · 2026-11-15 |
| 3 | One hit per red block group (the gap between two blocks currently touches both hit zones, so one mistake can cost 2 of 3) | engagement | fix · v0.21 · 2026-11-15 |
| 4 | Calm road and support-only weeks: no named stress cubes (use a blank "hard moment" or none) | trauma-access, learning | fix · v0.21 · 2026-11-15 |
| 5 | Rewrite stale text: greens surge; landing is shape-match, not "line up"; remove old deck and pop-up references (tray legend, Library lines ~104 and ~148) | all three | copy · v0.21 · 2026-11-15 |
| 6 | Stressed final face: spines hidden behind the key disc on beat 0 | gameplay | fix · v0.21 · 2026-11-15 |

## Tier 2 — learning truth (S to M)
| # | Fix | Research |
|---|---|---|
| 7 | Speedometer m/s moves only on frayed bands (demyelination really slows conduction). Greens and pinks keep their feel ruling but don't change the science readout | Horvath item 3, still open since 11-06 |
| 8 | Keep the week's effects to leg 4 (cortex). Relays 1–3 carry touch regardless, matching the end card | Learning seat F3 |
| 9 | Science wording table (in the learning report): sleep evidence is hippocampus (Havekes 2016); spine changes take days to weeks (Radley 2005, Vyas 2002); "Missed the bus" is about control, not predictability (Maier & Seligman); swap the mortality statistic for Liu 2012 (isolation thins prefrontal myelin) | Learning seat |
| 10 | Frayed bands slowly knit back after a few clean seconds, so recovery is a mechanic and not just a sentence | Radley 2005; trauma-access |

## Tier 3 — gameplay and engagement (M)
| # | Change | Why |
|---|---|---|
| 11 | Landing puzzle as real work: show the next messenger ahead, allow targets two spines away, and put the stressed target on the far spine against the pull. One messenger per synapse; the player finds the matching spine they can reach | Today it's a left/right guess, and stress makes it easier (67% of stressed beats target the spine you're on). Hick 1952, Fitts 1954; Dale's principle |
| 12 | Pace each leg as dense sets followed by about 4 s rests that carry the curves, timed to the music | The tube is straight about 90% of the ride; curves run only in clear stretches (founder ruling). Smith et al. 2009 rhythm-based level design |
| 13 | Travel time becomes the headline score: last ride and best this visit (in memory, nothing saved) | Ride 2 plays like ride 1. Mastery goal framing (Ames 1992); competence (Ryan, Rigby & Przybylski 2006) |
| 14 | Chained greens rise in pitch and stack the surge; speak a name only the first time it appears | An attentive scripted player had zero hits on the hardest week (UNPROVEN for humans). Juice: Jonasson & Purho 2012 |
| 15 | "Try next" becomes one button that adds the block and starts the ride | Removes a wall; turns feedback into the next attempt (Hattie & Timperley 2007) |
| 16 | Inventory: cut the opening paragraph, fold research lines behind a "Why?" toggle; Ride button visible without scrolling (now about 2.8 screens down) | Expertise reversal (Kalyuga 2003); founder no-walls floor |
| 17 | First green earlier; a one-beat landing with no fail state in the warm-up | First landing now arrives 45 s or more in (inferred from timing) |
| 18 | "Rose to it": a stress hit right after a green becomes a labeled surge | Stress reappraisal (Jamieson 2010/2012; Crum 2013). Teaches through play what the tray only tells |

## Access (S, fold into v0.21)
- Draw cube icons on a dark disc. They measure 1.02:1 on green and 2.33:1 on pink today; on a disc they measure 10.9–11.9:1. The outside-event pictures are the whole trauma-informed hook, and right now nobody can read them at speed.
- Change the "Wrong shape" and "Missed" labels to #ff8fc4 (8.3–9.7:1; currently 5.8–6.7:1).
- Alarm and thinking spines differ by only 1.04:1 luminance, so shape alone separates them. Add a value difference.
- Lightning: obey reduced motion, cap at 3 per second, add a setting.
- Move "Skip replay" into the thumb arc. The Studio link mid-ride needs a confirm.

## Founder rulings (2026-11-14 14:00: "1 idk. 2. Y. 3 y. And implement advised changes")
1. Week stress: founder declined to choose, so the chair ruled per standing preference. **Week stress is LOAD, not hits.** Pink cubes slow you and widen frayed bands but never end the ride. Hits come from frayed bands and gaps that do not fire. Stress raises risk without being scored as the player's fault (SAMHSA 2014). Founder may reverse.
2. Speedometer shows the science: **yes**. Built in v0.21.
3. One-tap prediction before ride 2+: **yes**. Built in v0.21.

Built as v0.21: `claude/signal-rider-build-v21.py`, notes in `claude/SIGNAL-RIDER-v0.21-BUILD-2026-11-14.md`.

## What already passed (keep)
- Scene-first opening with one instruction; passes the 3-second test.
- Hands-on warm-up; cheap checkpoints (about 18 s at most); crisp Match / Wrong shape / Missed verdicts.
- Week blocks from real student life ("Closing shift, then class").
- Non-blaming copy ("the body protecting you, not a failure"); supports appear even in an all-stress week.
- HUD text at 11.9:1 or better; full-screen flashes pass WCAG 2.3.1 by arithmetic.
- Horvath fixes since 11-06: no reading while steering, friend card sourced, meal card cut, fade card reworded.

## Wishes (no honest check this cycle)
- A shareable "my week" end card.
- The ghost spark from the 11-06 panel.
- A real student playtest. Only that can prove Tier 3.
