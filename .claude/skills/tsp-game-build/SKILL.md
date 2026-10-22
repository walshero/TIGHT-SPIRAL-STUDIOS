---
name: tsp-game-build
description: >-
  Build, edit, or ship any Tight Spiral Studios (TSP) game or HTML surface. USE WHEN
  making a new game, changing an existing build (kireji-pond, arcade, en195-*, sandbags,
  funnybonies, any *.html in walshero/TIGHT-SPIRAL-STUDIOS), or when the user says
  "build", "ship", "push", "fix the game", or "tsp-game-build". Runs canon check before
  the edit and the studio gates after it, and refuses to report shipped until the live
  bytes match. DO NOT use for Confluence trunk files (Confluence lane owns them) or for
  prose docs with no HTML surface.
---

# TSP game build: canon in, gates out, bytes verified

This skill holds no rules of its own. Every rule already lives in the repo as a script
or as a section of CLAUDE.md. The skill is the ORDER they run in. If a step here and the
repo ever disagree, the repo wins: re-read it, don't defend this file.

## 0. Get the hub (any surface: chat, Code, Cowork)

    test -d ~/tsp/.git && git -C ~/tsp pull --ff-only \
      || git clone https://github.com/walshero/TIGHT-SPIRAL-STUDIOS.git ~/tsp

All scripts below run from `~/tsp`. Never run gates from a copy on the shelf; the shelf
is a cache and it lags.

## 1. Session start: the Aleph pass (once per session, before any edit)

    python3 resolve-canon.py --aleph

- Exit 3 or a BLIND list is normal from Python. Print the BLIND lanes BY NAME in the
  reply. Silence never reads as agreement.
- Standing HALTs in the output that you did not cause: report them in one line each,
  do not fix them unasked.

## 2. Before touching a named file: canon check

    python3 resolve-canon.py <file> --check <the-copy-you-are-holding>

Exit 1 = you hold a fossil. STOP and tell Matt which lanes disagree. Never pick the
newer, larger, or smaller copy by default. New files skip this step.

Also check `cross-lane-manifest.md` for the file's owner lane. TSP does not write
Confluence files.

## 3. Build

Floors that are checked by the gates in step 4 (do not restate them in the build,
just meet them): single file, offline, no external hosts, no emoji, scene first with no
opening wall, comfort as a live corner control, >50% image, 18px type floor, 44px touch.

Floors the gates cannot see, so you must do them by hand:
- Version chip in the `<h1>` plus the same version in `<title>` and the build banner
  (CLAUDE.md: "Version on the surface").
- Status chip (Lab / In build / Live) in the `<h1>` (CLAUDE.md: "Status ladder").
  Promotion to Live is earned by green gates and a play, never by editing the chip.
- Founder words are primary source; machine prose is fallback for Matt to edit.
  The SABBATICAL PILE is never studio-facing
  (claude/founder-voice-provenance-manifest.md).
- Win sounds or reward effects: read the win-state research first
  (claude/WIN-STATE-AND-JUICE-RESEARCH-2026-09-26.md).

## 4. Preship: one command

    bash .claude/skills/tsp-game-build/preship.sh <file.html>

It runs the belt in one-file mode (ticks 1-14: comfort, offline, emoji, image floor,
voice, entry paint, touch, contrast sweep, intent, top floor) and then
`preship-contrast-gate.py`, which the belt does not call. Exit 1 means it does not ship.
Paste the HALT lines to Matt as they are. Do not argue with the measured number; fix the
build or put it in Lab.

## 5. Push, then prove it arrived

- `./safe-push.sh <file> "<message>"` where git push works. Through a connector, pass
  `expect_total_bytes` with the local byte count.
- Then `./verify-push.sh <path>`. Say nothing about shipping until it prints clean.
  A green connector result is a claim, not proof (CLAUDE.md: "CHECKED IS NOT SHIPPED").
- Record the new hash: `python3 resolve-canon.py --row <file> <gate> <verdict> "<detail>"`
  and append the row to FUNES-LEDGER.md in the same push.

## 6. Close the turn

End with the live URL written out in full (CLAUDE.md: "Always say where to play it").
Play lane: https://walshero.github.io/tss-playtest/ unless the build names another.
Then one line each: version, status chip, gate verdict, BLIND lanes.

## What this skill will not do

- Write a new rule in response to a failure. If something slipped through, the fix is a
  check in a gate script, landed in the repo, not a sentence here.
- Clear a HALT by relabelling, lowering a baseline, or editing a gate.
- Push to a lane another project owns.
