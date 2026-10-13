# STUDIO SENSES SWOT — Flok as the test case, 2026-10-13
<!-- source: Matt, 2026-10-13: "utilize studio eyes and studio fingers and studio ears to review latest build, use a SWOT to examine the work of those TSP agents, then update the agents/workflow to include SWOT results. Target FLOK for this exercise with studio improvements persisting in studio protocol" | owner: mwalsh | status: LANDED -->

**One sentence:** the senses were judging the wrong thing. They read first paint, they crawled out of the build on the first tap, and nothing played the game, so three Flok builds shipped green with the core verb below the fold on every phone.

The SWOT is of the AGENTS (Eyes, Fingers, Ears, the crawl, the seats, the belt, and the session running them), not of Flok. Flok is the specimen.

## The evidence (all measured on Flok v27 as shipped, md5 fa04cec3)

| # | What happened | Which agent | Caught by |
|---|---|---|---|
| E1 | The senses crawl's first tap was the studio's own "Studio" link. The bundle became the studio home and the EN195 arcade. Personas reported "0 under-floor targets across 4 states" about a game they never saw. | senses-crawl v1 | this SWOT, by reading `sighted.md` |
| E2 | Core verb (Boost, Send, Release, 'Seen' receipts) at y=930 on every phone from 375x667 to 430x932. Bisected to v25 (60c40dd, "photo-first training screen"). | static Fingers, all 12 belt ticks | crawl v2 + new fingers-play |
| E3 | On a win, Next landed 250-320px below the fold. A player who won saw nothing happen where they were looking. | nothing | crawl v2 (197 Boost taps, no progress) |
| E4 | Wordmark dot inside the phone: amber on light, 1.8:1. Present on the training screen since v24, never seen because Eyes reads first paint. v27 put a phone on the first screen and Eyes HALTed. | Eyes (caught it), the session (did not run Eyes) | studio-eyes.py |
| E5 | v27 shipped on "all gates green" from a HAND-PICKED list of three gates. Studio Eyes was not on it. The belt also passed (tick 10 carried the dot as old debt). | the session; the belt's baseline | this SWOT |
| E6 | `studio-fingers-play.py`, reported built and committed in September, is in neither repo's history. | the session that reported it | this SWOT (git log, both repos) |
| E7 | Belt printed "BELT: PASS — all ticks clear" under tick 12's "REPORTED, NOT ARMED … This is NOT a pass." | studio-belt.sh | this SWOT |
| E9 | Built during this SWOT and caught by the belt the same day: `senses-run.sh` v1 began with `rm -rf` on the bundle and wiped the seats' predictions; an `.sr-only` line, absolutely placed in a flex column, sat at the top of the screen and tick 5 counted its 13 words as an instruction wall. Both fixed (preserve seat files; `aria-describedby` to a `hidden` target). | this session | belt tick 13, belt tick 5 |
| E8 | The two defects the founder found by eye this week (photos that made no sense; an underwhelming opening) were found by no agent. No seat has ever been run on Flok; the seat ledger holds 0 graded sessions. | the seats | the founder |

## S — Strengths
- **Eyes is real.** 25/25 canaries, and it caught E4 that three other contrast gates passed. It reads pixels, not tokens.
- **Ears is honest.** Flok reads SILENT, never PASS. That word did its job: it is a fact the seats can use, not a green light.
- **Arithmetic beats prose when it exists.** `flok-feed-check.py` (v26) took the founder's "the photos make no sense" from 21 HALTs to 0 and now guards it on every build.
- **md5 stamping works.** Every bundle, prediction and verdict names the bytes it judged.

## W — Weaknesses
- **W1 First paint only.** Static Fingers, Eyes, tick 5 and tick 10 all judge the screen you load on. Flok's game lives on four other screens.
- **W2 The crawl could not play.** v1 left the build, could not scroll a feed, quit any button after 3 taps, and read boxes mid-scroll. No coverage measure, so shallow read as clean.
- **W3 Seats exist on paper.** Six seats, one pilot (Kireji), zero graded sessions. Judgment defects (meaning, compelling, setup/payoff) have no instrument and fall to the founder's phone.
- **W4 Hand-picked gate lists.** A session chose which gates "counted". Eyes was left out and the release note said green.
- **W5 Baselines hide new instances.** A carried selector absorbed a new element with the same selector on a new screen.

## O — Opportunities
- **O1 One evidence spine.** The crawl bundle already holds screenshots and boxes for every state. Fingers now judges it; Eyes, Hitchcock and Horvath can read the same play-through instead of first paint.
- **O2 Flok's interrupt lever is silent.** A single notification tick on Release (gesture-first, mutable, under the Ears floors) would let the player feel the trick they are pulling. Founder call.
- **O3 Pay the midnight off.** The cold open plants "keep her here past midnight" and 10:52 PM. Nothing in the game says what time it is at the end. One clock line on the promotion card or the reveal pays the setup. Founder call.
- **O4 Decoys on lever 1.** The bell and the feed are live, labelled controls that do nothing on lever 1; the crawl tapped both before Boost. Cheap Horvath fix once the founder rules.

## T — Threats
- **T1 Rule sprawl.** ~30 rules already. Every fix below is a check or a command, not a paragraph (project instruction: "if a rule can't be a check, it's a wish").
- **T2 Cost.** A full crawl is about a minute per build. Tick 13 runs only on changed game builds, never the corpus.
- **T3 The founder as the only judgment instrument.** Until seats are graded against real play, they drift toward plausible.
- **T4 Claims without bytes.** E6 is the fourth "it shipped" that did not (TSP_Ledger 2026-08-27). Only `git log` settles it.

## What changed, as checks (all landed 2026-10-13)

| Weakness | Fix | Proof it discriminates |
|---|---|---|
| W2 | `senses-crawl.py` v2: stays in the build (no cross-document links, no studio chrome), retires a control after 3 taps that change nothing (not 3 taps), scrolls scrollable controls, scrolls before tapping off-screen controls and logs `needs_scroll`, skips inert controls (`pointer-events:none`), waits for scroll to settle, records each state's screen and prints **coverage FULL / SHALLOW** | Flok: v1 reached 0 of 5 game screens; v2 reaches 5 of 5 and plays all five levers |
| W1 | `studio-senses/fingers-play.py` (rebuilt, E6): P1 verb in view, P2 path in view on first pass, P3 shallow crawl HALTs, P4 dead taps. Builds mark credit screens `data-secondary` | self-test 4/4; Flok v27 HALT (5 verbs), v28 PASS |
| W4 | `studio-senses/senses-run.sh <build>`: crawl + ears + fingers-play + Eyes + personas, exit 1 on any HALT. One command is the senses; there is no list to pick from | v27 HALT, v28 PASS |
| W4, W1 | Belt **tick 13**: senses-run on every changed game build (screen census). SKIPS LOUD without a browser | belt HALTed v28 on first run until P2 learned "first pass" |
| E7 | Belt verdict now reads "every ARMED tick clears; N REPORTED, NOT ARMED" when tick 12 or 13 cannot speak | belt run 2026-10-13 |
| W3 | `.claude/agents/senses-seats.md`: ONE agent seats all six chairs on a bundle, with the SWOT's three standing questions (setup paid off, verb in view, decoys). Predictions must be gradeable or go to notes | Flok v28: 11 gradeable predictions filed, `reports/senses/the-console/predictions.json` |

## Flok fixes this SWOT shipped (v28)
- The verb is on screen at every lever on every phone tested (fitTrain: the brief-to-verb span fits the viewport; feed and photo shrink to floors 220/110px; short phones drop the role line, which repeats the rank pill).
- Next scrolls into view on the win.
- Wordmark dot 4.6:1 on the phone (was 1.8:1).
- The opening tells a screen reader the clock: "It is 10:52 PM. She has been on flok for about four minutes."

## Pending, for the founder (seat calls, not defects)
- O2 a notification tick on Release. O3 a clock on the reveal. O4 make the lever-1 decoys inert or part of the lesson.
- The entry gate still carries two old debts on the opening: the photo is 17% of the entry against the >50% image rule, and Studio / Cabinet / Start your shift read as three co-equal invitations. Both pre-date v27 and ride the ratchet; growing the photo trades against fitting the button above the fold on an SE.
- Grade the seats: play Flok v28 cold on the phone. The 11 predictions in `reports/senses/the-console/predictions.json` are the first ever filed on Flok.
