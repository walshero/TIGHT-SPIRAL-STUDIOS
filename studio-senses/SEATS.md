# STUDIO SENSES — THE SEATS AND THE PREDICTION LEDGER
<!-- source: Matt, 2026-09-26: "we convene Studio Eyes and Studio Fingers ... never from the panelists I've placed like Alfred Hitchcock for scene coherence and Jared Horvath for assessment ... now I want studio ears ... research based agentic assistance that resists drift" ; option 5 chosen same day | owner: mwalsh | status: PILOT on kireji-pond -->

**One sentence:** every sense seat reads one evidence bundle of the rendered game, files predictions about what the first human players will do, and is graded when they play, so a seat that is wrong loses standing instead of being ignored.

## Why the panelists were silent

Contrast talked because it is arithmetic on the belt and exits 1. Hitchcock and Horvath existed only as prose that signed a findings file before the build existed (`convening-gate.py` checks 120 characters and a signature). Nothing ever showed them the rendered game, and nothing ever checked whether they were right. A seat nobody grades drifts toward saying something plausible.

## The pipeline (runs in this order, per build)

```
senses-crawl.py   plays once, writes the evidence bundle (md5-stamped)
      |
ears.py           Studio Ears Layer 1, arithmetic, exit 1 on HALT
personas.py       splits the bundle: sighted.md | ear.md | fingers-states.json
      |
SEATS (agents)    each reads ONLY its channel, files predictions.json entries
      |
archive/playtest-room.html   SHELVED 2026-09-26 (founder: one main link for playtesting); records taps, text seen, sound, questions
      |
grade.py          outcome per prediction per session; Brier score per seat
```

The seats never veto a ship. Their HALTs are blocking checks filed for the founder (Playtest Table rule, `claude_seat-playtesting-agents.md`). What they gain is a scorecard.

## The six seats

| Seat | Reads | Owns | Research anchor |
|---|---|---|---|
| **Hitchcock** (Eyes Layer 2) | sighted.md + screenshots | scene coherence: does each touch change the scene, what the player knows and when | his own July check: every scene reads as a 3-frame board, room / glow / turn |
| **Fingers** | fingers-states.json + screenshots | hit area at every state, reach, taps to the core verb | `studio-eyes/studio-fingers.py` floors (44px founder floor, 60% reach arc) |
| **Horvath** (Coordinator) | sighted.md + ear.md | the cognitive work asked versus the work the build names; which taps are decisions and which are decoration | Gee's well-ordered problems; the studio's measurement ruling (5-point scales, identical wording) |
| **Murch** (Ears Layer 2) | ear.md + ears.json | whether sound carries meaning, sits under the scene, and never competes with reading | XAG 103/104; ASWG-R001 loudness; WCAG 1.4.2 |
| **Sighted persona** | sighted.md + screenshots | a cold first player who can see | the Playtest Table ENTRY axis |
| **Ear persona** | ear.md only, no pixels | a cold first player using a screen reader and sound | Can I Play That low-vision guide; AFB |

## A prediction is only a prediction if the recorder can grade it

Every entry names one observable the human instrument records. Opinions without an observable go in `notes`, which are read by the founder and never scored.

**Observables** (per human session, recorded by `archive/playtest-room.html`, shelved 2026-09-26; it fails the belt's night-mode, image and intent checks and needs that pass before any return):

| measure | meaning | fields |
|---|---|---|
| `time_to_tap` | ms from load to first tap on `target` | op, value (ms) |
| `taps_before` | taps before the first tap on `target` | op, value |
| `tapped` | did the player ever tap `target` | value true/false |
| `saw` | did `target` text ever appear in a heading, announcement or button | value true/false |
| `dead_taps` | taps that changed nothing in the page within 600 ms | op, value |
| `sound_off_at_end` | the sound control reads off when they finished | value true/false |
| `session_ms` | load to "I'm done" | op, value |
| `answer:knew_next` | 1 to 5, "I knew what to do next" | op, value |
| `answer:recall` | the build's own recall question (what the intro says) | value = one choice |
| `answer:notice` | a question that tests the practiced skill, not the intro sentence (Horvath owns it) | value = one choice |
| `answer:sound_felt` | helped / got in the way / I had it off / I didn't notice it | value = one choice |
| `answer:played_by` | looking / a screen reader / both | value = one choice; the grader uses it to route `cohort` |

**Target syntax:** `#id`, `.class`, `tag`, `tag.class`, or `name:words` (accessible name or label contains the words, case ignored). For `saw`, target is `text:words`.

**Entry shape:**
```json
{"id": "H1", "seat": "Hitchcock", "claim": "plain words", "measure": "tapped",
 "target": "name:catch line", "op": "==", "value": true, "p": 0.8,
 "cohort": "any"}
```
`cohort` is `any` or `screen_reader`; a screen_reader prediction is graded only on sessions that answered played_by = a screen reader or both.
```
```
`p` is the seat's confidence the claim comes true for a typical first player. The grader scores it with a Brier score (0 is perfect, 0.25 is a coin flip), so confidence is priced.

## Anti-drift, as checks

- Every predictions file carries the build md5 and sha256. A session recorded against different bytes grades **STALE**, never pass or fail.
- A seat that files zero gradeable predictions is recorded as **SILENT**, not agreeing.
- Seat scorecards accumulate across builds in `reports/senses/SEAT-LEDGER.md`. A seat whose Brier score is worse than 0.25 over ten or more graded predictions is flagged to the founder for re-grounding.

## Run it

```
python3 studio-senses/senses-crawl.py kireji-pond.html --out reports/senses/kireji-pond
python3 studio-senses/ears.py reports/senses/kireji-pond        # exit 1 on HALT
python3 studio-senses/personas.py reports/senses/kireji-pond
# seats: one agent per seat, each reading only its channel, writes pred-<seat>.json; merge into predictions.json
# humans: play the game directly (founder, 2026-09-26); the recorded room is shelved in archive/
python3 studio-senses/grade.py reports/senses/kireji-pond/predictions.json playtest-*.json
python3 studio-senses/ears.py --self-test && python3 studio-senses/grade.py --self-test
```
