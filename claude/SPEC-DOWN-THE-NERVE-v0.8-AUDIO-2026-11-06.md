# SPEC: Down the Nerve v0.8 — warm-up, voiced callouts, neon audio, checkpoint replay (2026-11-06)

Build: `lab/down-the-nerve.html` (LAB). First landing of this game in the repo.
Base: v0.7 as published to the claude.ai artifact "Down the Nerve v0.7"
(sha256 0570fe05...29fc3, 1,016,632 B). v0.1 to v0.7 were built in the chat "Neuroscience
teaching game spec" and lived only on the artifact and the project shelf.

**Owed to canon:** the full spec (`claude/SPEC-DOWN-THE-NERVE-2026-11-05.md`) and the
convening (`convening/DOWN-THE-NERVE-CONVENING.md`, rulings D1 to D13, v0.1 to v0.7) are on
the project shelf only. Copying them means retyping about 25 KB through a tool call, which is
the PLACEHOLDER risk (CLAUDE.md, "CHECKED IS NOT SHIPPED"). They should be harvested with a
byte-moving lane from a session that holds the files on disk.

## Founder words (voice call, 2026-11-06, primary source, lightly cleaned)

On onboarding, after the session proposed teach-by-playing with a warm-up ride:
> "How in the one after the warm-up game when they're really playing, how are they experiencing or learning ... the red boxes and the green boxes? This is a fast-moving game ... Do we pause the game when one of these things happens, to show them why? I don't love that, but I need options."

After the options (in-ride word flashes plus a checkpoint replay, recommended; bullet time as the more ambitious option):
> "I like this direction, but the one thing I want to add is audio ... since they're going to be moving, we really need to leverage audio. So if it says like bad night's sleep ... we need that to come with the flashing. The message."

> "I want you to build in your own audio, make it ... like Tron ... let's get the audio clips into the next build, and you are authorized to go."

Build order, text chat: "Build".

## What v0.8 does

| Element | Behavior |
|---|---|
| Warm-up | The page opens on the moving tube, with no tray or wall. One green ("A friend on the steps") comes straight at the spark, then one red ("Short night"). Each is flashed, voiced and followed by one line: "Supports clear the path." / "Stress takes away places to land." A dodged cube gets its own line. The warm-up red does not count as a hit. About 10 s, then the week tray opens. |
| Callouts | Every banner (green, red, frayed band) is voiced with a short label under a second: the card label ("Short night", "A friend"), "Frayed band", "Checkpoint", "Landed". Uses the device's own speech, tuned low and quick (pitch 0.55, rate 1.18), so it stays offline. Captions stay on screen. |
| Red sound | Two detuned low saws falling 100 to 42 Hz through a closing filter, plus a muffled noise thud. No echo. |
| Green sound | Rising square arpeggio C5-E5-G5-C6 through an opening resonant filter, a sine sub sweep, and the grid echo (190 ms delay, 0.38 feedback). |
| Checkpoint | Neon two-note chime. If anything happened since the last checkpoint, a slow-motion replay (0.35x) of the last red and the last green, letterboxed and tagged REPLAY. The cause-and-effect sentence is spoken and captioned. "Skip replay" button. About 5 to 10 s, then the ride resumes exactly where it was. |
| Fade | "The signal faded." is spoken. |
| Sound off | Silences the synth and cancels speech. |

Replay sentences (studio voice, flat, no wellness claims, for founder edit):
- Short night: "A short night. The bands widened and you slowed. In the brain, short nights thin the landing places in the thinking cortex. They come back."
- Test tomorrow: "A test tomorrow. One hard moment dims the thinking road for a while. It relights when the moment passes."
- Phone at 2 a.m.: "A phone at 2 a.m. means broken sleep. Short nights thin the landing places. They come back."
- Missed bus: "A missed bus. Stress stacks, and the alarm road gets louder. That is the body protecting you."
- Loud room: "A loud room. The alarm road fires. It is built to protect you, and it quiets when things calm down."
- Real sleep: "Real sleep. Landing places relight overnight, so the bands narrowed."
- A walk: "A walk. Moving helps new landing places grow, so the bands narrowed."
- A friend: "A friend. The alarm road calms and the thinking road relights, so the bands narrowed." (source still owed for social buffering, per the v0.1 spec)
- A good meal: "A good meal. Support the world gives you, so the bands narrowed."
- Practice: "Practice. A road you ride again grows more landing places."
- Frayed band: "A frayed band. That is damaged insulation, and the signal crawls through it."

## Not built (founder's call)

- Bullet time on the first sighting of each box type (the more ambitious option).
- A recorded human voice. Device speech sounds robotic and varies by phone. The voice-call trade-off: a recorded voice, even the founder's, means one clip per card.

## Measured

Headless run on a 390x844 screen: the warm-up ended and the tray opened at 10.0 s. On a
ride, the first checkpoint replay fired with its sentence, ended after about 5 s, and the
ride resumed from its live position. No page errors. Speech and audio were not heard; the
founder's phone is the test.
