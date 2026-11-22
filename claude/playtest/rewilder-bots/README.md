# Rewilder bot playtest harness (2026-11-20)
Headless Chrome via Playwright. Loads lab/rewilder.html, stops the rAF loop, and drives update() at a fixed 1/30 s
step with a seeded Math.random, so 15 game-minutes run in ~5-7 s. Personas live in bot.js (rampager, climber, novice).
  python3 run.py "$(cat plan.json)" out.json     # plan = [{"persona":"rampager","seed":1,"level":1,"secs":900}, ...]
  python3 analyze.py out.json
Both scripts load the repo's lab/rewilder.html (override with REWILDER_SRC=...). Level 3 + island: python3 l3batch.py plan.json out.json,
plan = [{"style":"careful|rush|clumsy","seed":1,"secs":900,"bonus":true}]; bonus:true also plays the v0.93-v0.95 pool party.
Limits (run.py personas): bots never swim, never do the salmon gate, the underground dam (L3) or the tower quest. setTimeout is
re-timed onto game time. jumpLevel() used to start L2/L3 counts as one RESTART per run (subtract it).
