---
title: Rewilder v0.85 + level 3 bot playtest
date: 2026-11-21
base: lab/rewilder.html, repo main 9c06a28 (v0.84, 606,890 B)
build: builds/rewilder-v0.85.html on the shelf (revised 2026-11-21 09:4x, electric shock restored)
patch: claude/playtest/rewilder-v0.84-to-v0.85.patch (git diff against 9c06a28)
gates: preship-contrast-gate SHIP (worst pair 10.17), preship-gate-v5 SHIP (0 halts). senses-run not run (2-CPU box).
status: NOT in the repo yet. This session's push and artifact-publish permissions were refused.
---

# Rewilder v0.85 + level 3 bot playtest

## v0.85: founder rulings of 2026-11-20

Founder: "1. revive both with progress kept. 2. Allow salmon to revive other players 3. Don't let players smashing good stuff have any effect. 4. Broken tractors disappear after 60 seconds. In a poof!"

Each change was checked with a scripted test in the game.

| # | Change | Check |
|---|---|---|
| 1 | When both animals are down, both stand up at the tag post with full energy. The city keeps its state; there is no level restart. | Growing garage still growing after both KO'd; both at 100 energy at x 3570 |
| 2 | The salmon's Smash revives a downed animal, from the nearest water she can reach. | Downed beaver up after one salmon smash |
| 3 | Smashing a growing lot does nothing: no growth setback. Revised 2026-11-21 (founder: "Trying to Smash electric stuff SHOULD shock you."): electric green sites (canopy, wind) and the tram still shock. | Growing lot: growth 0.500 then 0.503 after 6 smashes, energy 100, no shock. Wind farm: energy 100 then 66, shock on |
| 4 | A tipped pave truck vanishes at 60 s in a dust poof ("POOF"). It is no longer repaired. | Present at 59 s, gone at 61 s |
| + | Smash now reaches the block under your feet on one-row sites. This was the parking-lot dead spot from the first bot run. | target() returns row 0 when standing on the lot |
| + | Bug from this playtest: tagging right after landing on the island swapped you to the partner still on the mainland, sending you back across. The partner now catches up first. | v0.84 put the player at x 3570; v0.85 keeps them at x -2150 |

## Level 3 playtest

### Method
- The agent uses only the player's inputs: arrow keys, Up, Smash, the Dive and Tag buttons, and taps. It reads the screen (wires, drones, footings, walls) the way a player would.
- It swims under steel walls, breaks the dam's footings underwater, climbs the fortress, crosses the sea, and plays the island tower quest end to end.
- 12 runs, three styles:
  - **careful** reads the wires and waits out drone swoops.
  - **rush** reads the wires but never waits.
  - **clumsy** ignores the wires half the time and mashes the wrong key 20% of the time.

### Results

| Style | Finished (of 4) | Time to finish | Fortress shocks per run | KOs per run |
|---|---|---|---|---|
| careful | 4 | 3:51 – 4:30 | 0–4 | 1 |
| rush | 4 | 3:52 – 4:33 | 0–2 | 1 |
| clumsy | 1 | 8:55 | 12–53 | 3–14 |

Typical timeline for a careful run:
- Mainland sites cleared and the fortress started at about 1:40.
- The fortress falls and all five sites have grown by about 2:20–3:00.
- Landing on the island to the finish takes about 60 s: valve, salmon to the drain, drones drop, turtle to the plate, roof, rope, farmer.

### Findings
1. **Level 3 is finishable end to end.** Every careful and rush run completed the level and the island. No script errors in 12 runs.
2. **The fortress wires are the difficulty wall.**
   - A player who doesn't read the wires took 12–53 shocks and 3–14 knockouts.
   - Two of four clumsy runs never got the fortress down in 11.5 minutes.
   - With v0.85 nobody loses progress (7 both-down revives; no level wipes), but the wall is still steep.
   - If the audience is teens, the founder may want a softer fortress. The island tower got this treatment in v0.68 ("more spacing").
3. **The island quest runs clean and fast,** about 60 s for agents who know it. A human reading it cold will take longer. A cold founder play is the real test.
4. **The junk plug at x 1000 blocks the swim to the sea** if you dive at a ladder right of it. The game says "Smash it", and that works. The agent didn't, which is the agent's gap, not a game bug.
5. **The island ending logic runs inside drawIsle() (the render pass).** Play is unaffected, because render runs every frame. A headless test that skips render never reaches the end screen. Worth moving into update one day. No player-facing change.

### Not covered
- How the drones on the island tower feel to a human: the agent sees their state directly.
- Sound and art.
- The phone touch layout.
