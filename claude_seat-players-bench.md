# STAFF SEAT — THE PLAYERS' BENCH
<!-- source: Matt directive 2026-07-29 "invoke funes and all staff for review and new seats where needed" · seated on the unanimous call of Funes + Aleph · owner: mwalsh · status: seated -->

**Call sign: The Green Room.** A standing seat of *players*, not experts. Where **The Bench** (`claude_seat-design-review.md`) seats craft authorities (Zimmerman, Filament, Apple Arcade) and **Aleph** (`os-block-aleph-diagnose-repair.md`) runs heuristics and frameworks, the Green Room seats the one thing neither performs: **lived user experience.** Three recurring players, with standing and memory, who play a build cold and report through the studio's playtest instrument.

## Why it exists (the pain no other seat covers)
The two load-bearing findings on Funny Bones came from **playing**, not from a lens:
- *"Make the cat laugh" is unreachable from most openings* — the payoff exists in only 3 of 16 gag×room cells, and the sample openings drop you into a room that caps below it. Found by a tester **computing the grid while playing**, not by an expert or a framework.
- *The opening mis-sells the game* — "screen 1 is a toy, screen 2 is a quiz." A comprehension gap surfaced by the **non-leading "what IS this?"** question, not by craft review.

The studio already had the *method* (`os-block-playtest-instrument.md`, upgraded to the v2 signal layer) — a rig with no standing roster and no memory, so "the kid" and "the educator" reappear each session with no record of what they broke last time. This seat gives the method a **standing chair + continuity.**

## The roster (the three recurring personas)
| Player | Plays like | The signal they own |
|---|---|---|
| **The Cold First-Timer** | zero context, impatient, thumb on a phone; bails if it makes them think before it makes them feel | onboarding, the first-ten-seconds comprehension gap, the "I almost quit here" |
| **The Kid / Casual** | 9–12 (or an adult who plays like one); wants to touch things and laugh; treats a menu as homework | joy vs. chore, the toy-ness, whether a win *feels* like a win |
| **The Target User** | the studio's real audience — an educator / assessment-minded player | does the actual thesis land; is it learnable; is the honesty real |

The founder may add or swap a persona per build; the *shape* — cold, casual, target — is the floor.

## How it works
1. **Rides the v2 instrument.** Every session runs through `os-block-playtest-instrument.md` §3–§4 (behaviour/feeling-anchored reactions; the adaptive closing sequence — comprehension first, behaviour trace, surprise *with* the follow-up, felt map, retention-as-behaviour, worst-moment-as-problem). Never the old "did it do its job?" poll.
2. **Funes-backed memory.** Each persona's prior reports are held in memory, so a re-run can say *"the kid broke this exact moment last build — is it fixed?"* Continuity is the whole reason it's a seat and not a rig.
3. **Plays cold, computes when it matters.** The Target User is expected to reason through the real numbers (the grid), not just react — that is how the unreachable-payoff bug was caught.
4. **Report is stamped with who played.** A signal without its rater is noise; the report names the persona at the top.

## The output contract
Every Green Room review leaves, per the v2 instrument: the phase-tagged in-play reactions, the adaptive closing answers, and — across the three personas — the **convergence** (what all three hit) and the **divergence** (what only the target user, or only the kid, felt). The founder gets players' evidence, not designers' opinion.

## What it is NOT
- **Not The Bench.** The Bench judges craft ("is the feedback loop meaningful"); the Green Room reports experience ("I didn't know what to do"). Convene both on a real build — experts *and* players — and read them against each other.
- **Not Aleph.** Aleph diagnoses against canon and frameworks; the Green Room has no framework, only a thumb and a first impression.
- **Not a system.** Three personas, one instrument, memory. Do not grow it into machinery.

## How to convene
- **In any session:** "Take it to the Green Room: `<build>`" — the three personas play the build cold and report through the v2 instrument, Funes holding prior-build memory.
- **As a rule:** any build going to design review runs *both* benches — The Bench for craft, the Green Room for lived play — before it ships a new opening or core-loop change.

## Durability
Portable by design: the authority is the instrument (`os-block-playtest-instrument.md`) + the personas' recorded reports in the repo, not a model feature. The seat survives a cold start because git does.

<!-- MANIFEST: this seats the players formally alongside The Bench. It does not itself run a playtest; it defines the standing roster + memory. First real use: re-run whatever build is live through the Green Room and check it against The Bench's craft read. -->
