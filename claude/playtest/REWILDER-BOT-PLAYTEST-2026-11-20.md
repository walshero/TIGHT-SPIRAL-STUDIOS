---
title: Rewilder bot playtest — v0.84
date: 2026-11-20
build: lab/rewilder.html, repo main 9c06a28, 606,890 B, sha256 ab81f7a6…f42e6f
method: headless Chrome, fixed-step simulation, seeded, 258 runs, 15 game-minutes each
harness: claude/playtest/rewilder-bots/ (bot.js, run.py, analyze.py, README.md)
status: findings only — no change made to the build
---

# Rewilder bot playtest — v0.84

## What ran
- 258 runs in total, about 60 game-hours, in about 25 minutes of machine time.
- Level 1: 210 runs with three personas. Rampager smashes the nearest block. Climber goes up the buildings. Novice flails 35% of the time and picks choice cards at random.
- Levels 2 and 3: 48 runs, started from the playtest level menu.
- Not covered, because the bots can't do these: swimming, the salmon gate to TAR CO, the underground dam in level 3, and the tower quest.

## Findings, ranked

### 1. Bug: you can't smash the block you're standing on (one-row sites)
- Standing on the paved lot's last asphalt blocks, Smash hits nothing. `target()` checks the chest row and one row above and below it. On a 26 px row the chest sits 2 rows up, so row 0 is never checked.
- In 22 of 24 Climber runs in level 2, the bot stood on the last two lot blocks and mashed for ten minutes.
- Fix (one line): add the row under the player's feet to the candidate list in `target()`.

### 2. Losing both animals wipes the level
- When both animals are knocked out, the game shows BOTH DOWN and restarts the level after 1.6 s, wiping everything planted.
- Level 1 restarts: 20 restarts across 15 of 60 competent-bot runs (25%), at 40–290 s. Each one wiped up to 3 grown or growing sites.
- Novice bot: 16 restarts in 9 of 30 runs.
- No founder ruling covers what happens when both animals are down. This is a call for Matt (see the end).

### 3. Half the damage is self-inflicted while climbing
- About 50% of all damage comes from blocks and cars falling onto a climbing animal. The rest is trucks and tar barrels.
- Knockouts per level 1 run: median 3.

### 4. A flailing player never clears level 1
- Competent bots clear level 1 in a median of 5 min 15 s. The fastest 10% take under 4 min, the slowest 10% about 10 min.
- The Novice bot cleared 0 of 70 runs in 15 minutes.
- Two causes:
  - Smashing a growing site sets it back.
  - Random card picks leave needs unmet, which brings the Baron (69 power-need spawns, against 15 for the Rampager).
- This is the needs system working as designed. For a young or first-time player, though, the gap between failing and succeeding is very steep.

### 5. Repaving spiral
- Crews repave a median of 6 sites per level 1 run. The lot takes about half of the repaving (it's cleared first and grows longest).
- Tipped trucks don't count toward the truck cap, so they pile up. One run had 7 tipped trucks stacked on the lot.

### 6. Dead air is fine
- From the last site falling to everything grown: median 42 s. The long growth timers aren't creating a boredom gap in level 1.

### 7. Level 2
- Cleared in 17 of 24 runs, median about 2 min 40 s.
- The stalls were finding 1 (lot top) and Rampager knockout loops (12–14 knockouts in a run).

### 8. Level 3
- Cleared in 0 of 24 runs. The bots can't reach the underground dam (every run parked at x = 2854). This shows the gating works. It doesn't measure difficulty.

### 9. No errors
- Zero script errors and zero page errors in 258 runs.

## Calls for Matt
- **Finding 1** is a straight bug. It goes first in the next build.
- **Finding 2** needs a ruling. When both animals are down: (a) restart the level, as now; (b) hold progress and revive both at the left edge after a beat; or (c) the Baron repaves one site as the cost.
- **Finding 4** is about audience. If young players are the target, consider making the setback on growing sites smaller for the first few minutes.
