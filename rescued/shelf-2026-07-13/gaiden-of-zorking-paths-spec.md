# THE GAIDEN OF ZORKING PATHS — spec seed
*Tight Spiral Productions · intake 2026-07-03 · stage 0–3 (spec lane; does NOT occupy a WIP slot)*
*The Script Engine First proof-of-concept: story logic ships as a playable scene graph before any art lane opens.*

## WHAT IT IS
A voice-only, blind-first, fully offline single-file HTML game. Seven scenes. A garden where paths fork; on replay, the garden remembers the paths not taken and says so aloud. Borges's conceit as the mechanic; Zork's architecture as the engine; gaiden scale — the smallest honest build that proves the house format.

## THE ENGINE RULE (the point of the build)
- World = data. One scene graph: scenes, choices, consequences, flags. No prose in the engine.
- Renderer = separate. This build's renderer speaks (`speechSynthesis`, on-device, offline) and listens via the OS (iOS Voice Control activates named buttons — the game never hears the player; the phone does).
- The graph is the canonical artifact. Edits happen in the graph, never in a renderer. A future visual renderer consumes the same graph — accessibility as birthright, not port.
- NO FREE PARSER. Zork's world model, not Zork's "I don't understand that." The game speaks 2–3 choices; the player taps a zone or says a button's name; the game echoes the pick before committing.

## FLOORS, TRANSLATED TO AUDIO
- Scene-first → SOUND-FIRST: opens with a sound the player notices, before any instruction.
- One decision per screen → one fork per utterance. Max 3 choices spoken per beat.
- C6 (50 words/screen) → ~10 seconds of speech per beat before the fork.
- 44px targets → whole-screen tap zones (left/right/bottom) + three large named buttons for Voice Control.
- Visible focus ring → SPOKEN FOCUS: "You're on: [name]" on every focus move.
- Scroll-reset → each scene starts audio-clean; standing button: "Again" (repeats the current beat).
- Comfort stops → three speech-rate stops + volume; live corner controls, never a gate (comfort is a knob).
- Joy flourishes ON with replay control → earcons: a short motif per path, recombined at forks.
- Keyboard nav, in-memory only, phone-width, offline: unchanged.

## PROVENANCE FLOOR
Borges is NOT public domain (d. 1986). The title is allusion; his prose never enters the file. All garden text = original founder/studio prose. Provenance ledger entry: original work, TSP, 2026.

## MVP (definition of done)
Seven scenes, two forks deep, one remembered-path reveal on replay. Engine and renderer in separate script blocks of one file. DONE = the founder plays start to finish, eyes closed, no sighted assist.

## OPEN FOUNDER CALLS
1. Garden text: founder-written or founder-voiced-then-transcribed? (Table Read either way.)
2. Earcon lane: synthesized tones (free, offline) vs. recorded motifs (base64, heavier). Recommend tones for MVP.
3. Does the Gaiden carry a discourse sub-deck later, or stay a pure mechanic proof? Recommend pure proof.
4. Build gate: cannot enter stage 4 until a WIP slot opens (BTD verdict or Warriors ships).

## LINEAGE
Zork (world-as-data, engine/presentation split) · Borges, "The Garden of Forking Paths" (all choices persist) · CYL v5 spec (scene inventory ready for the same graph format) · Script Engine First ruling (2026-07-03, KD! queue).
