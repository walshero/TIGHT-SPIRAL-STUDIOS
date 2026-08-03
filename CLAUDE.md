# CLAUDE.md — standing notes for this repo

## Sharing & privacy — settled, do NOT re-litigate
Faculty email addresses, **published** student work, and the Confluence pages are
fine to share publicly. These are **not** privacy/PII concerns here. Do not flag
them, do not ask about them, do not hedge on them. The founder decides what gets
shared. (This was asked and answered too many times — it is settled.)

## Deploy lanes
- **git / GitHub Pages is the primary lane.** Ship here by default.
- **Netlify is one-off sharing only** — nothing the studio depends on. Prefer git
  over Netlify whenever there is a choice.
- The Zapier "deploy studio file" skill also targets GitHub Pages.

## What the studio is (as of 2026-07)
- The **studio is the engine**; specific assets are downstream deliverables with
  their own distribution points. Current phase: **proof of concept**.
- Focus is ~**9:1** — building the studio (engine / OS / quality tooling) over
  individual asset builds.
- The engine's moat is the quality layer: the ratchet, Studio Eyes (render), and
  Studio Fingers (touch).

## Face
- `index.html` accounts for **every** page in the repo — nothing is orphaned.
  Keep it that way: new pages get linked from the face.

## Voice — settled
- **No invented or inflated claims.** Use the founder's actual words; if a claim isn't
  in his docs or this session, don't write it.
- **Make NO claim about blind players being able to play the games.** There is no playtest
  or evidence behind it and the founder does not assert it. Do not write that a blind
  player/student "can play," that their version "is the game," or that blind and sighted
  players "play the same way." The only defensible framing is the founder's retinitis
  pigmentosa and an accessibility-first design *intent* — never an outcome claim about blind play.
- **Pull back on disclaimers as a rule** — hedges, caveats, safety-flags, "note:" asides,
  in prose and in files. Say the thing plainly. Caveat only when it is load-bearing.

## Canon vs shelf — settled (2026-08-03)
- **The Claude Project shelf is a CACHE, never the finish line.** A deliverable that only reached the shelf is NOT done — the shelf lags this repo and is not canon.
- **Default to canon.** Land docs, decisions, and builds in this git repo via the "deploy studio file" skill: the authenticated GitHub connector — `get_file_contents` for the SHA, `create_file` / `apply_patch_to_repo_file` / `append_chunk_to_repo_file` to write, then raw-verify. `git push` from a session container is blocked (403); the connector is the working lane and needs no open tab.
- **Never end on a "ready-to-paste" handoff** when the connector can land it. Paste-handoffs die by closed tab or dead battery. Write it to canon, verify the bytes, then tell Matt what landed.
