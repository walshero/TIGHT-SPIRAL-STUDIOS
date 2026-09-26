# KIREJI POND — SENSES PASS, 2026-09-26

Build `kireji-pond.html` · md5 `0a6f41fbb6a5c9a3ce43c1749b6b8358` · sha256 `a71cfaf44c03fa46...`

Findings are blocking checks filed for the founder. No seat vetoes a ship; the founder rules.

## Studio Ears Layer 1 (arithmetic)
Verdict: **HALT**
- HALT E1 GESTURE-FIRST  1 source(s) started before the first gesture; speaker reached -36.2 dBFS before any touch. [LAW] OS §2: the first tap unlocks audio, ambush-free.
- WARN E5 SIGHT ALONE  18 of 32 state changes carry no sound, vibration or announcement: step 3 "a child’s paper boat, 5 syll"; step 5 "a temple bell, cold, 5 sylla"; step 7 "Mother Nature’s gentle touch"; step 11 "April showers fall, 5 syllab"; step 14 "Pause streamP"; step 15 "Resume streamP" .... [CITED] XAG 103.

## Founder ruling needed: sound before the first tap

- **Against:** line 2126 starts the waterfall at load; measured -36 dBFS before any touch. OS §2 (2026-06-27): the first tap unlocks audio, ambush-free.
- **For:** it is quiet and fades in, the mute is the first Tab stop and works (-83 dBFS), and a living pond is scene-first.
- **Middle path (Murch):** delete only the load-time `Snd.wake()`; the existing first-touch listeners already start the pond on the first tap.

## Seat halts (blocking checks for the founder)

- **Ear persona:** GESTURE-FIRST audio (Studio Ears Layer 1 E1) — evidence: ear.md verdict: 1 source started before the first gesture; the speaker reached -36.2 dBFS before any touch. This talks over VoiceOver's first announcement on load.
- **Ear persona:** Core verb is not reachable by ear: phrase activation neither announces nor moves focus to its actions — evidence: State 3/5/7/11/17/20/25/27: phrase gets [expanded] with 'nothing announced'. Catch line/Smash cliche/Let it go are appended after 'Still water', last in DOM order, while the phrase keeps moving (steps 19, 35-37 show phrases leaving or toggling). Step 4 shows a tap on one phrase judging a different phrase.
- **Fingers:** Slot controls under the 44px founder floor — evidence: Move to bottom 183x39, Move to top 144x39, Remove 103x39 in every slot-filled state (6-12, 18-21, 30); Skip to the stream 182x39 in states 0-1. Static controls, so this is a true floor miss, fixable with min-height: 44px.
- **Fingers:** Core-verb target spawns at 15-16px tall while moving, at the top screen edge — evidence: New phrases measure 77x15 (state 6), 48x15 (state 10), 52x16 (state 15), 77x15 (state 28) centered at y=53-59, above the thumb arc and near the top edge, in low contrast against the mountain. For a reduced-field, low-vision player this is the first thing to tap. Pause stream exists but sits at the bottom edge, partly below the fold.
- **Hitchcock:** confirm that a tap aimed at a second phrase while the action menu is open cannot fire Smash on the held phrase — evidence: state 3 -> state 4: menu open on 'a child's paper boat', crawler tapped 'the carp flips' phrase (y=77); result was a fresh-line smash of the paper boat and Clear water dropped 3 to 2. The menu buttons sit on top of the drifting phrases (screenshot states/03.png).
- **Horvath:** Target concept is practiced: at least one player choice changes its outcome based on where the cut sits — evidence: None of the 43 steps has an outcome that depends on a cut. Show turn marks changed no on-screen text (steps 16, 27, 42). Every scored outcome comes from syllable fit (automatic) or the cliché call (smash, states 4, 8, 26). The build names the kireji as its lesson and only displays it at state 1.
- **Murch:** E1 GESTURE-FIRST: sound before the first tap (founder rules) — evidence: Line 2126 calls Snd.wake() at load ('where the browser allows it, sound starts before any touch at all'); Layer 1 measured the waterfall at -36.2 dBFS before any touch. Against: studio OS section 2 says the first tap unlocks audio, permission-clean and ambush-free, and for a screen-reader player an unasked noise bed arrives before the first spoken word. For: the level is low, fades in over about 1.5 s, the mute is the first Tab stop and drops output to -85.5 dBFS (WCAG 1.4.2 is met: a stop mechanism exists at the top), the choice persists in localStorage, and the pond being already alive is the scene-first opening the studio also asks for. The code path conflicts with a stated law, so it is filed as blocking; the founder decides whether the law or the scene wins, or whether a middle path (bed starts on the first tap anywhere, which the capture listeners already do) is enough.
- **Sighted persona:** Action menu overlays neighboring stream phrases, so a tap aimed at another phrase lands on Smash cliche and costs clear water — evidence: Step 4 tapped 'the carp flips' label while the paper-boat menu was open; result state 4 reads 'a child's paper boat is fresh, not a cliché... the water clouds' and Clear water drops 3 to 2; screenshot 03 shows Smash cliche at y~240 covering the carp card
- **Sighted persona:** Show turn marks produces no text change and only a small visual mark, reading as a dead control to a first player — evidence: Steps 16, 27, 42 all logged 'screen text did not change'; screenshot 32 shows only a small red 切 tile near one card

## Where seats converged (independent channels, same finding)

- The Catch / Smash / Let it go menu overlays other drifting phrases; a thumb aimed at one phrase acted on another (Hitchcock, Sighted, Ear, Fingers).
- Show turn marks changes no text on screen and no announcement (Hitchcock, Horvath, Sighted, Murch).
- The cut is explained once on card 2 and never practiced; Skip bypasses it (Horvath, Hitchcock).
- A screen-reader player cannot reach the action menu from a phrase: nothing announced, focus does not move (Ear, Horvath).

## Predictions filed

- Ear persona: 6
- Fingers: 6
- Hitchcock: 6
- Horvath: 6
- Murch: 6
- Sighted persona: 7

Graded by `studio-senses/grade.py` against sessions from `playtest-room.html?build=kireji-pond.html`. None yet: no human has played.
