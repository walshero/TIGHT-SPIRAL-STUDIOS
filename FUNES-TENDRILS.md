# FUNES TENDRILS — the post-stall walk down every forking path
*2026-08-04. Founder: "execute new function — Funes tendrils down all forking paths. this runs on all chats after stalls of all kinds."*

## The loss shape this ends
Every loss this studio has suffered has one shape:

> **built → landed on a branch / worktree / `outputs/` → STALL → never merged → gone.**

A **stall** is any interruption: context compaction, a session resume, an MCP
connector flap, a user interrupt, a chat that simply ended. Work strands on a
fork and nobody walks back down it. Funes (the studio's memory discipline)
forgets nothing — but memory without a **walk** is just a pile.

This is the walk. After every stall, tendrils go down all forking paths and
surface what did not land.

## It proved itself the day it was written
The first run flagged the **entire studio-wide governance lane sitting 194
commits behind main** on a stale handoff branch, **19 stranded branches**
(one 32 commits deep), the orphan pages, and the live worktrees — none of it
visible until the walk ran.

## What it walks (`funes-tendrils.py`)
1. **Working tree** — uncommitted changes (the freshest loose end).
2. **Current branch** — commits ahead of upstream (built, not pushed).
3. **All branches** (local + remote) — ahead/behind main. Ahead = unmerged /
   stranded; far-behind = **stale base** (the handoff-branch trap — flagged
   "do not fast-merge", because merging it reverts main).
4. **Worktrees** — extra checkouts that can hide uncommitted work.
5. **Staging dirs** — `outputs/`, `scratch/`, `tmp/` with files. Nothing lives
   in a staging dir.
6. **Orphan pages** — `*.html` the face (`index.html`) does not link. "No
   orphans anywhere." (Gate fixtures are excluded, as the eyes exclude them.)

It **never guesses and never deletes.** It reports.

## How it runs on all chats
Wired as a **SessionStart hook** in `.claude/settings.json`
(`matcher: startup|resume|clear|compact`) — so it fires at the start of every
chat and after every compaction/resume/clear, exactly "on all chats after
stalls of all kinds." Advisory there: it reports loose ends into the session so
the next chat inherits the map, never the silent stall.

## Modes
- `python3 funes-tendrils.py .` — advisory (always exits 0). Session-start + the
  `floor.yml` report step use this.
- `python3 funes-tendrils.py --gate .` — CI teeth (exits 1 on any loose end).
- Not a git repo → exits 2 in gate mode, 0 advisory.

## The standing rule
> A stall must never be inherited silently. Before the next fork, walk the last
> one. Funes forgets nothing; the tendrils make sure someone looks.
