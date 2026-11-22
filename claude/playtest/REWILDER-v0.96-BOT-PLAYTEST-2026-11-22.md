---
title: Rewilder v0.96 bot playtest
date: 2026-11-22
build: lab/rewilder.html v0.96 (canon f86187b, 657,225 B)
harness: claude/playtest/rewilder-bots (run.py personas, l3batch.py level-3 agent; l3bot.js now plays the pool-party bonus)
runs: 56 (36 persona runs on levels 1-3, 20 level-3 agent runs through the island)
---

# Rewilder v0.96 bot playtest

Founder: "Test current version with agents"

## Method
- Headless Chrome, fixed 1/30 s step, seeded, 15 game-minutes per run. The bots only press the player's inputs and taps.
- **Persona bots (run.py):** rampager, climber and novice. 6 seeds each on level 1; 3 seeds each on levels 2 and 3.
- **Level-3 agent (l3batch.py):** careful, rush and clumsy styles. It plays the mainland, the swim, the island tower quest and, with `bonus:true`, the new pool party: water back on, salmon up the pipe, then both animals into the pool.
- **Correction during the run:** the first batch silently tested v0.85. The scripts pointed at a stale clone. Both scripts now load the repo's own `lab/rewilder.html`, and every number below is from v0.96.

## Results

| Test | Result | v0.85 / v0.84 baseline |
|---|---|---|
| Level 1, rampager + climber | 11 of 12 cleared, median about 4:30 | median 5:15 |
| Level 1, novice (flails 35%) | 3 of 6 cleared | 0 of 70 |
| Knockouts per level 1 run | median 1 | median 3 |
| Level 2, all personas | 8 of 9 cleared, median about 2:50 | 17 of 24, about 2:40 |
| Level 3, persona bots | 0 of 9 (they can't swim to the underground dam, by design) | 0 of 24 |
| Level 3 + island, careful | 8 of 8 finished, 3:50 to 4:55 | 4 of 4 |
| Level 3 + island, rush | 8 of 8 finished | 4 of 4 |
| Level 3 + island, clumsy | 1 of 4 finished, 9:12 | 1 of 4 |
| Pool party bonus (agent tried it) | 13 of 13 got the party | new |
| Script or page errors | 0 in 56 runs | 0 |

**Pool party timing:** the takeover to the party takes 23 s for an agent that knows the route. Valve, salmon up the pipe, nearer animal, last animal, each switch automatic. The finish screen follows 9 s after the party.

## Findings
1. **The new island chain works end to end.** Pads, padlock, refill valve, salmon past the drain, the automatic hand-offs and the party all fired in every bonus run. No stalls.
2. **Level 1 got easier for every persona.** Two things drive it: v0.85's revive-with-progress (no level wipes) and no setback from smashing growing lots. Even the flailing novice clears half the time now.
3. **The fortress wires are still the wall for a careless player.** Clumsy agents took 21 to 72 shocks. Two of four never brought the fortress down in 15 minutes. This is unchanged since v0.85.
4. **One clumsy run stalled at the junk plug at x 1023 on the swim to the island.** This is the known agent gap: the game says Smash it; the agent doesn't.
5. **A climber bot spent 12 minutes pressing Up on the 93 between its legs (x 1316).** This is the founder's poles-only rule working; a player can walk to a leg. If a human hits the same thing, a small leg cue could help. Not a bug.
6. **Bot fix, not a game fix.** The agent first stalled 2 px under the floor-24 landing while climbing down, because it let go of Down too early. The game was right; the agent was fixed.

## Not covered
- Feel, sound and art; the phone touch layout (checked separately by screenshots this session).
- A human reading the island cold: the agent knows the route. The founder's play is the real test.
