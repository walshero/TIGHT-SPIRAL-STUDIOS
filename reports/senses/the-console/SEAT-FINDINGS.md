# FLOK v31 — SENSES PASS, 2026-10-13

Build `the-console.html` ("v31 Tess’s Tuesday") · md5 `6b07e110befb60faa26b1bad15701c4f` · sha256 `35c60a17b2727b56` (16) · bundle from `senses-crawl.py v2` (signature v2.1) · coverage FULL 5/5 · 0 page errors · 0 external requests.

The seats file blocking checks for the founder. No seat vetoes a ship; the founder rules.

## Pre-checks
| check | result |
|---|---|
| Tool | senses-crawl.py v2 (the version string was not bumped to v2.1) |
| Coverage | FULL: sc-hire, sc-train, sc-rank, sc-flip-seat, sc-about |
| md5 match | manifest = `md5sum the-console.html` = 6b07e110… |

## Layer 1 (arithmetic)
- **Ears:** PASS. The mute works on the first press: -25.6, then -180, then -25.5 dBFS. WARN: 3 sight-only changes (steps 26, 32, 40).
- **Fingers play:** PASS. 0 controls under 44 px in all 20 states.
- **Eyes:** 0 HALT (as reported by the run; it reads first paint).

## Halt (1)
| # | Seat | What | Evidence |
|---|---|---|---|
| 1 | Hitchcock, Sighted | The lever-1 burst "Quinn viewed" (step 5, 10:53 PM) never clears. It covers Priya's "best friend · 64-day streak" on lever 5 and sits on the streak banner on lever 3. | Sighted text in states 7, 10–13, 15–17. In the state 15 and 7 pngs it is at about y=310–350 CSS px. Absent from the accessibility tree (ear.md: 0). |

## The world, graded
| Beat | Verdict | Evidence |
|---|---|---|
| Clock, 10:52 PM to 12:09 AM | Continuous | 10:53, 11:06, 11:07, 11:21, 11:22, 11:37, 11:38, 11:52, 11:53, 12:06 (step 37), 12:09 (state 18) |
| Lever 1 time | Contradicts | The return times on her cards add up to about 26 minutes after 10:53 (state 2); the card says 11:06 |
| Two photo posts, then replies and text | Contradicts | Lake, mushroom, then a third photo: "one more before bed", the nightstand (states 10–13) |
| Streak with Priya | Contradicts | 64 (state 7), then 67 after three sends, all in one minute (state 8), then "64-day streak" again at 11:53 (state 15) |
| Memories card | Likely misread | "the night before she moved", a year ago (state 11), against "moved in August" (state 15) |
| Three Seens | Holds, one break | Three people, three weights (state 15). Switching receipts off takes the replies back (state 16 to 17) |
| tidepool | Small contradiction | "posted for the first time in a while" (state 11) after a sunset at 21m (state 4) |
| 12:06 list on the last card | Spoken; not photographed | Announced at step 37. The card was folded into state 14, whose png shows the 11:52 card |
| Reveal Rosa line | Pays "for rosa." | State 18; set up by state 0 and Rosa's post in state 4 |
| Lever 1 ratio | Reads | "You tapped Boost 6 / It paid off 3 / About one in 2" |
| "Pulled her back fastest" | In teal, as the machine's measurement | State 18 png. The player's counts are in white |

## Per chair
- **Hitchcock.** Setups paid: the clock, "for rosa.", past midnight. Still unpaid: the "on flok 4:13" meter. 7 continuity breaks (table above). Evidence gap: the Shift-over card has no screenshot.
- **Horvath.** No decoys on levers 1–4. Lever 5's feed was kept on purpose (v29 ruling). Risk: "q.ramos viewed your story" sits on the card marked "back after 9m", and the 40s return is one card up (state 2). Telemetry reads "Alerts 10" and "Screens 10" against 4 presses each.
- **Fingers.** P1 and P2 PASS. At the win frame the bell is still out of frame on lever 4 (state 11, same as v29), and the streak banner is scrolled out on lever 3 (state 8). Next is at y=1217 after a bell tap after the win (state 13).
- **Murch.** One sound, on the interrupt only, under the floors, and the mute works. No ask.
- **Sighted persona.** The relationships read in lever 5's DM lines, "Suggested for you" and tidepool's 2341. They come late for Mom (named at 11:53) and Rosa (named as sister at 12:06). Hank is never identified.
- **Ear persona.** The three payouts and the 12:06 beat are spoken. Unpaid Boosts are silent, and the return times are never spoken.

11 gradeable predictions in `predictions.json`. They grade when the founder plays v31 cold on a phone.


## Resolved after seating (same day, carried to md5 6eaa4b42fca4dd622664c3f176dd777f)
- **HALT (Hitchcock, Sighted): the payout pop-up never cleared** under reduced motion and covered Priya's line on lever 5. It now clears after 1.2 s in both modes (measured: opacity 1, then 0 at 1.6 s).
- **Timeline:** the streak stays at 64 on a save; lever 1 return times add up inside 10:53-11:06 and name what they follow ("back 90s after Mom's comment"); Memories is "movie night at the old place" (Quinn moved in August); "first time in a while" is cvx, not tidepool; Tess's older posts read "earlier".
- **Two photos, then text:** the bedside photo is gone; the bed photo is labelled "sent to daily.loaf" (a streak save, not a post).
- **Receipts off** hides Seen and no longer takes replies back.
- **Ear persona:** an unpaid Boost now says "No payout. She posts again."
- **Kept, noted for the founder:** the opening's "on flok 4:13" meter does not return later; Hank is never named in the feed (real feeds show handles, not relationships; the DMs carry the ties).
