# Flok phone playtest, 2026-11-06 (founder, voice, live on his phone) -> v36

Source: founder's spoken notes while playing v35 at the playtest URL. Founder words quoted where they set a rule.

## Shipped in v36
| Screen | Note | Fix |
|---|---|---|
| Opening | Clock cut off ("ten something PM"); "a big pile of text, different sizes of white text"; "the opening does not land"; keep "Start your shift" above the fold | Photo carries only story chrome + caption; all game text in one panel at two sizes; clock nowrap |
| All | "The text in general needs to be smaller" | Headlines, buttons, rank, playbook, ending scaled down; 18px floor untouched |
| Assignment | "1 of 5" broke across two lines | nbsp + nowrap |
| Boost | "If mom commented, that's not me as an engineer giving a boost" | Each result names the operator's move first ("you put it first in Mom's feed"), then what came back |
| Result / Your move | "There should never be extra lines of space" inside boxes | Reserved min-heights removed; boxes fit their text |
| Every assignment | Button "right underneath the flock interface... then result, because that's causal" | Order: phone, verb, result, meter, your move |
| Playbook 2 (infinite scroll) | Animation implied an infinite top | Cards now travel up; new posts arrive from below |
| Assignment 2 feed | Post slid left/right, text went off screen | Feed overflow-x hidden, pan-y only |
| Order | Notifications "so critical part of infrastructure... even before a streak you'd see a notification" | Order now: surprise likes, red-dot alerts, infinite scroll, streak, seen receipts |
| Streak level | "The first two messages don't seem to make sense" | Streak level shows streak posts; alerts level follows the lake post and Mom's comment |
| Seen receipts | Copy: "Once they know she saw it, not answering carries weight." | Founder words, verbatim |
| Seen receipts | "Replied just now" on every row; "show a mixture" | 5 rows: 2 replied, 1 started a reply and stopped, 1 seen no reply, 1 delivered not opened |
| Rank / every screen | "The page should load at the top... especially if there's an animation" | go() scrolls to top instantly; rank card no longer scrolls itself |
| Ending | Metrics "not appealing graphically"; text too big | Boosts as a dot row (paid lit), stat tiles |
| Ending | New line per question; question and answer in different colors | Each on its own line, amber question, ink answer |
| Ending | "At 12:06, her sister liked the lake photo. That was the post that would have meant the most to her. She didn't see it." Founder: do NOT give the last sentence its own line | Verbatim, one paragraph |
| Ending | Cut "The cohort was people like you." | Cut |
| Ending | Neutral, high-quality reading links | National Academies 2023, APA advisory 2023, Surgeon General advisory 2023, Pew 2025 |

## Founder rulings made in this session
- **Live links: exception approved on Flok's ending screen only** ("Approve live links as an exception"). Offline rule holds everywhere else.
- **Result below the verb, shipped Lab with feedback-floor F2 HALT on short screens** ("Ship 1"). On 393x660 (Safari toolbar showing) and iPhone SE the result lands below the fold after a Boost; on 393x760 and Android it passes. Alternative not chosen: result above the verb on short screens only.
- **Studio-wide: every new screen loads at the top, especially with an animation** (same as the Kireji Pond fix). NOT YET A CHECK. No current gate tests scroll position on screen entry; build one into fingers-play (screen entry -> scrollY == 0).

## PENDING
- Feed photos look like stock ("a National Geographic cover, not something I expect to see 11:07 PM"; e.g. rosa.out.west mountains). Needs phone-real photos. Blocked: the session sandbox cannot reach upload.wikimedia.org / commons.wikimedia.org. Founder can allow them at claude.ai > Settings > Capabilities.
- No way to go back to a previous screen. Asked; founder did not answer.
- Pre-existing Studio Eyes HALT (on v35 too): LAB chip leaves the top bar by 42px at 200% zoom.

## v37, the opening (same day, founder screenshot of v36: "needs cohesion and energy as well as clarity", Horvath leads; founder chose option 1)
One story, one column, one clock. Photo brightened, scrims only behind text; caption on the photo with no box; small avatar, full name; a live heart count and one "2 people viewed your story" notification; panel left-aligned at two sizes ("She opened flok to post one photo." / "Your job: keep her here past midnight."); the meter is the clock (10:52 PM ticking toward the midnight tick; the "on flok" timer is gone); button "Clock in". tsp-routes.json updated to the new button text.
