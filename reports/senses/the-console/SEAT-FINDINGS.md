# FLOK v29 — SENSES PASS, 2026-10-13

Build `the-console.html` ("v29 past midnight") · md5 `1aeb4521a881d8981457eec23747eaed` · sha256 `cb47e8117180904d` (16) · bundle from `senses-crawl.py v2` · coverage FULL 5/5 · 0 page errors · 0 external requests.

The seats file blocking checks for the founder. No seat vetoes a ship; the founder rules.

## Pre-checks
| check | result |
|---|---|
| Tool | senses-crawl.py v2 |
| Coverage | FULL: sc-hire, sc-train, sc-rank, sc-flip-seat, sc-about |
| md5 match | manifest = `md5sum the-console.html` |

## Layer 1 (arithmetic)
- **Ears:** PASS. Mute works on the first press: -25.6 dBFS, then -180, then -25.5. WARN: 7 of 18 state changes carry no sound or announcement.
- **Fingers play:** PASS. WARN: About the photos needs a scroll (secondary screen).
- **Eyes:** 0 HALT (as reported by the run).

## The four v29 changes, graded
| Change | Seat | Verdict | Evidence |
|---|---|---|---|
| O3 midnight payoff | Hitchcock | Paid | The clock advances on every lever (10:53, 11:07, 11:22, 11:38, 11:53). The reveal opens "12:09 AM ... You kept her past midnight." (state 17) |
| O4 lever-1 decoys | Horvath | Gone | State 1 controls: Boost plus chrome only. The crawl's lever-1 taps were Boost only (steps 1 to 4) |
| O2 sound | Murch, Ear | Felt by the crawl, mutable | 6 oscillators per Release (about 0.29 s), RMS -25.5 dBFS, lever 4 only, none before a gesture |
| Story opening | Sighted | Reads as a post | Segment bars, avatar, handle, clock, and the headline over the photo. The photo is about half the 400x840 frame (eyeball read). Footer under the fold |

## Seat findings (no halts)
- **Hitchcock.** One setup is unpaid: the opening meter "on flok 4:13" never returns. Evidence gap: the crawl's signature ignores text, so only the first promotion card (11:06 PM, Junior) was captured. Cards 2 to 4 are unchecked. The phone's clock row scrolls out of frame at every win.
- **Horvath.** One decoy remains: "Simulated feed" is a live control on the inbox lever (state 12) and changes nothing (steps 31, 33). The lever-4 brief asks "clear, then release", but Release alone won on passes 2 to 4 (steps 59 to 67).
- **Fingers.** At the lever-4 win frame, the bell (the winning tap, step 20) is out of frame at y=-128.
- **Murch.** The only sound is the interrupt, on the interrupt lever. Nothing more is asked.
- **Sighted persona.** Studio and Cabinet still sit above the post: three invitations on the first screen.
- **Ear persona.** The 12:09 AM payoff and the promotion card are not announced (steps 36, 6). On lever 1 the tree lists Next before the win (state 1).

11 gradeable predictions in `predictions.json`. They grade when the founder plays v29 cold on a phone.


## Resolved after seating (same day, carried to md5 1f59f6939ce42e08d48e00afc2656d09)
- **Ear persona:** promotion cards and the 12:09 AM reveal are now spoken once, politely ("Promoted: Junior. 11:06 PM. She is still on flok." ... "12:09 AM. She is still on flok. You kept her past midnight."). Verified in the crawl's live log.
- **Ear persona:** Next carries `aria-disabled="true"` until the target is hit.
- **Horvath:** lever 4 Release now waits for the red dot to be cleared, as the brief says; a press before that says "Clear the red dot first."
- **Hitchcock:** crawl v2.1 separates states by heading, so all four promotion cards are in the bundle; the fifth card reads "Shift over" at 12:09 AM instead of repeating "Head of Growth".
- **Kept on purpose:** the inbox lever's feed stays keyboard-focusable. It is a scrollable message list, and a scroll region must be reachable by keyboard (WCAG 2.1.1), even when scrolling is not the verb.
