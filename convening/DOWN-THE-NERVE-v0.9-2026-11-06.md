# DOWN THE NERVE v0.9 — rulings and build record (2026-11-06)

Base: canon v0.8 (repo lab/down-the-nerve.html at d4ff3e1, artifact 1793982729-954d, sha256
cd66bbac...32710; spec claude/SPEC-DOWN-THE-NERVE-v0.8-AUDIO-2026-11-06.md). v0.9 sha256
6c2359e6...70aac, 1,039,117 B, artifact version 1794010052-539c (hash matched). Repo lane:
NOT PUSHED from this session (no write credential); the v0.8 session or the Mac should land it.
Playtest findings this build answers: convening/DOWN-THE-NERVE-PLAYTEST-2026-11-06.md.

## Founder rulings

- 18:52 ET: "No pop up cards. Only frayed bands and blocks. But as you advance blocks can add up.
  Like 2-4 together depending on your week. We need more audio clues about what's happening.
  Critical: pop up messages cover the player ball frequently."
- 18:53 ET: "Take recs on combining" — the session's combined landing (D15) and its other
  recommendations (one replay after the ride, D17; claim fixes).
- D14 settled by the 18:52 ruling: week cards no longer pop up during the ride; only frayed
  bands and blocks act on the spark.

## What v0.9 does

| Area | Change |
|---|---|
| Pop-ups | None during the ride. The week decides which blocks appear and how many. |
| Block clusters | Four clusters per leg. Reds come as a wall of 1-4 side by side; greens as a line of 1-4 to ride along. Size grows each leg and with the reds or greens in the week. Red share 25-75% by week. Every cluster sits at least 8 units clear of a frayed band (measured: closest 9-10 units). |
| The Leap | The tube ends in a cleft. The spark leaps (arc, steer in the air), bursts into 10 messengers at the next neuron, and a threshold ring fills. Relays 1-3 always fire. Thinking cortex under a hard week: fewer spines, wider cleft, each landing counts for less (weight = spines/5), so it can take more than one spark; what landed carries over, fading 20% (summation). The thorny alarm face beside it has 7 easy spines; if its messengers win, the ride ends "The alarm road fired first" (an arrival, not a failure). No rewind-and-scold; a fresh spark fires from 7 units back. |
| Leg 4 blocks | Under a hard week, a green grows a spine back on the face ahead (+weight); a red dims one (minimum 2). |
| Audio | Pre-cue about 1.4 s ahead for every band (double buzz if in your path, soft tick if not), every red wall (low saws, one per block, louder if in your path) and every green line (rising notes, one per block), all panned to where the thing is on screen. Synapse beacon: a tone that rises and centers when you are lined up with a lit spine. Leap whoosh, messenger sparkles, fizzle when not enough lands, alarm buzz. After the second hit: two-tone warning and "One hit left." Alarm-road heartbeat while the pull is on. |
| Messages | Banner, toast and steer hint live in one stack that moves to wherever the ball is not: top band, bottom band, left column, right column; if none fits, the toast (also spoken) steps aside. The floating "+ / - speed" text over the ball is removed. Replay caption moved to the top. |
| Replays | No replays at checkpoints. One optional "Replay the last red and green" button at the end. |
| Claims | Banner fiber lines cut; night and phone captions now say "a long run of hard weeks thins the landing places"; warm-up lines match what the warm-up shows (bands); fade card adds "damaged insulation can stop a signal." |

## Checks run

- Messages vs ball: 6 screens (390x844, 375x667, 844x390, 1280x800, 1024x1366, 320x568) x both
  views x 24 ball positions = 288 samples, heaviest message load: 0 overlaps.
- Relay 1 fires with no aim. Hard week, no steering at the thinking cortex: alarm road fires
  first. Hard week, aimed at a spine: fired on the second spark (fill 4.3 of 3, weight 0.6).
- Contrast gate SHIP. No page errors. Audio not heard; the founder's phone is the test.

## Founder ruling 19:08 ET — D16 settled (v0.9.1)

"You have to steer into greens just like you steer away from reds and damaged bands."
Already true in play (greens collect only within 0.42 rad of the spark, the same reach as
reds). v0.9.1 makes it legible: tray line, legend and Library now say "steer into greens";
a soft falling note plays, panned to its side, when a green passes uncollected. v0.9.1
sha256 d6c3648c...85b4bb, artifact version 1794014657-a7d2. Gate SHIP; gameplay checks
unchanged.

## Founder report 20:26 ET — five greens showed as four (v0.9.2)

"When I add 5 green blocks to the week it only shows 4." Cause: the week model left Practice
out of the green count (it only moved the balance point), so the tray drew 4 cubes; the HUD
drew one token cube regardless of count. Fix: Practice counts as a green block like the
others and still moves the balance point; the tray and the ride's balance both draw the real
number of red and green cubes. Checked: all five greens on, tray 5, ride balance 5, labels
read "5 support cubes." v0.9.2 sha256 d708b037...dcd81a, artifact 1794014900-9130. Gate SHIP;
landing and block checks unchanged.

## Founder notes 20:39 ET — onramp, reading while steering, the landing (v0.10)

"Everything is too fast at the beginning when onramping. Compare current speeds to industry
standard. Then during game, there are info tags but I'm trying to focus on steering so I read /
learn nothing. Also. The jump when you have to match the white dot it's anticlimactic and should
involve multiple maybe even slow motion moves to land it."

Research: endless runners start at a low base speed and raise it with distance up to a cap
(speed = min(max, base + distance x rate); Subway Surfers and peers speed up over time). v0.9.2
started at full cruise with no ramp. Mayer's modality principle: people learn more from pictures
plus spoken words than pictures plus printed words (17 of 17 tests, median d = 1.02), strongest
when the presentation is fast-paced. Looming sounds speed reactions (Gray 2011), which supports
the audio pre-cues.

Applied (v0.10):
- Onramp: warm-up at half speed; the first leg starts at half speed (about 3.3 units/s) and reaches
  cruise (6.5) after 180 units, about 45 s. Rings drawn one per unit (half the flicker: start 3.3
  rings/s, cruise 6.5/s, was 13/s from the first second). Warning at readable distance: 3.6 s at the
  start, 1.85 s at cruise. The speedometer still reads the fiber (75 m/s at cruise), not the ramp.
- No reading while steering: banners show the icon and a short title only (spoken too). Teaching
  sentences (nodes, frayed bands, synapse) wait in a queue and appear, spoken, in the calm stretch
  after a relay fires. Warm-up lines are spoken, not printed.
- The landing in slow motion: the tube ends, time slows, letterbox bars. A white target spine with
  a closing ring marks each beat (one per second); the target moves to a new spine each beat. On
  each beat the spark releases messengers where you are: on target lands fully, near lands half.
  Relays 1-3 fire after two landings (up to 6 beats, then fire late). The thinking cortex fills a
  ring (need 3; under a hard week each landing counts spines/5 and the alarm road pulls); two beats
  on the alarm face and the alarm road fires first. Metronome tick half a beat ahead, chord per
  landing rising with the ring, thud on a miss, fanfare on firing; the beacon follows the target.
- Measured: first 6 s at 3.5-3.7 units/s; relay 2 aimed fires in about 3 s (two beats); hard-week
  cortex aimed fires after five landings (about 5 s); no steering, the alarm road fires on the
  second beat. Messages vs ball still 0 of 288. Gate SHIP. v0.10 sha256 ec25339e...3ccff75,
  artifact 1794016241-362d.

## Still open

- D18 bare stretch for saltatory conduction. Friend card source (social buffering) still
  owed. Repo landing of v0.9.1.

## v0.11 — research-based categories (2026-11-07)

Ruling (founder, 11-07): the player can't see what good and bad effects are. Make the choices more nuanced, sort them into research-based categories of stress and resilience, let players drill down at the start, and give facts while they choose.

Build: artifact 93f72ea1 version 1794061212-f5ef, sha256 3483932cdfddc7467e7505233950fdf6b95012d50d3f27660546a1e6babe2cd1 (verified via list_files). Builder: build_v11.py over v0.10 (ec25339e). Landed in the repo 2026-11-07: tight-spiral-studios main b4a0934 (re-cloned; hash matches). Mirrored to tss-playtest main 1f23ba1.

**Stress categories (red):**
- Sleep: short nights, phone at night
- School: test tomorrow, work piling up
- Money and basics: skipped meals, rent due
- Time: work shifts, long bus ride
- Place: loud home
- People: feeling alone

**Builder categories (green):**
- Body: sleep 7+ hours, walk or workout
- Connection: a friend who listens, a professor who knows your name
- Skills: practice, slow breathing, if-then plan
- Belonging: time outside, a club or team
- Help: campus food pantry

**Each category changes one thing the player can see** (weekModel):

| Category | Effect on the ride |
|---|---|
| Sleep | fewer landing spines |
| Body | +1 landing spine |
| People | alarm-road pull |
| Connection | less alarm-road pull |
| Place | wider frayed bands |
| Belonging | narrower frayed bands |
| Time | red groups one larger |
| Help | red groups one smaller |
| Skills | lowers the weight of red blocks (lever) |

**Tray:**
- Order: balance, then the live effects panel (spines, pull, band-width bar, group size), then categories.
- Inside a category: an intro, an "In the game:" line, and cards. Each card shows a research fact, its source, and what it does in the game.
- The legend is folded into "How the ride works".
- The Library lists the research behind every block.

**Sources:** Yoo 2007; Chang 2015; Arnsten 2009; Maier & Seligman 2016; Hope Center 2019; NCES 2022; Stansfeld 2005; Holt-Lunstad 2010; CDC; Liu & Nusslock 2018; Heinrichs 2003; Gallup-Purdue 2014; AFWI; Zaccaro 2018; Gollwitzer & Sheeran 2006; White 2019; Walton & Cohen 2011; Harvard Center on the Developing Child (stress types).

**Checks:**
- t11: categories, effects, and ride reflection all pass.
- t10/t09 regressions pass.
- tmsg: 0/288 message-ball overlaps.
- Contrast gate: SHIP, worst pair 18.10.
- No errors.

## v0.12 — the leap can fail (2026-11-08)

Founder, 13:19 ET: "In down the nerve, there is no fail state on the jumps and there should be. It should be slightly harder."

**Science.** A neuron fires only when enough input lands together to reach threshold. Below threshold there is no action potential (OpenStax A&P 12.5).

**Fail state.**
- Each gap has a closing window:
  - Relays: 2 landings in 5 beats. A half landing counts half.
  - Thinking cortex, ordinary week: 3 in 6.
  - Thinking cortex, hard week: each landing counts 0.5 (floor raised from 0.35), 8 beats.
- Missing the window shows "Did not fire", with a spoken line and a fizzle. It costs one of 3 hits, and a fresh spark retries from 7 units back.
- At the cortex, half of what landed carries over (summation).
- The third hit opens the fade card, which now names the gap when the gap was the cause.

**Slightly harder.**
- The beat quickens by leg: 1.0 / 0.92 / 0.85 / 0.8 s.
- Windows are tighter: a full landing is under 0.25 rad, a half under 0.5.
- Targets jump only as far as steering (2.7 rad/s) covers in 60% of a beat, so it's hard but never unreachable.
- On a two-spine cortex the target holds and jumps every third beat.

**Calibration** (simulated aimers at the game's steer speed; t12.py, 6 trials each):

| Gap | 250 ms reaction | 450 ms reaction | No steering |
|---|---|---|---|
| Default week, relay | 6/6 fire | 5/6 fire | 0/6 |
| Default week, cortex (first try) | 4/6 | 3/6 | 0/6 |
| Hard week, cortex (with carryover) | fires in 1-3 tries | fires in 1-2 tries | the alarm road fires first |

**Also in this build.**
- HUD text has solid backings, and the balance fulcrum is lighter. These were Studio Eyes contrast HALTs already present in v0.11.
- --ink and --bg are split into text tokens plus --inkfill and --ground fill tokens (Studio Eyes TOKEN_ROLE).
- The legend has a line on how the leap is won and lost.

**Gates.**
- Contrast gate: SHIP.
- Studio Eyes: PASS.
- Top floor: PASS.
- Messages vs ball: 0/288.
- Senses: HALT on fingers P3 "shallow". The crawl has no screen census and never enters the ride. The seat read (one agent) confirmed this and declined to seat. LAB status allows it.

**Open from the seat read.**
- Give the crawl a way into the ride (sc- screens for the ride, the "Did not fire" banner and the fade card, plus a held steer through one window).
- The crawler counts 0 of 0 screens as FULL (senses-crawl.py line 387).
- The top bar shows the word "Comfort", which the 2026-10-13 ruling bars.
- The Back button is announced as "Restart the ride".

**Names.** Brainstorm in progress; no ruling yet. "Threshold" and "Touch & Go" are taken by existing games.
