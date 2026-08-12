# FINDING — `main` and the arcade branch are UNRELATED HISTORIES, and `main` is the stale one (2026-08-12)

*Recorded because the session-start tendrils hook prints a line about this every
run, and the line reads backwards. A session that trusts it will "fix" the wrong
branch.*

## What the hook says

```
[STRANDED] claude/en195-poetry-arcade-1aunsp: 50 commit(s) not in origin/main,
51 behind — STALE BASE, do not fast-merge
```

Read plainly, that says: *your branch is behind main, rebase onto main.* I acted on
that reading this session and told the founder the branch needed rebasing. **That is
wrong and would have destroyed six days of work.**

## What is actually true

The two refs have **no common ancestor at all**:

```
$ git merge-base HEAD origin/main   # no output, exit 1
$ git rev-list --max-parents=0 HEAD         → b5277d8   (branch root)
$ git rev-list --max-parents=0 origin/main  → 6e16918   (main root)
```

Two separate root commits. So "50 ahead / 51 behind" is **not divergence** — with no
merge base, every commit on each side counts against the other. The numbers are an
artifact of unrelated lineage, not a measure of staleness. `git rev-list --count` is
51 on each side: two independent 51-commit histories in one repo.

## Which one carries the current work

**The branch.** Not main.

| | branch tip | `origin/main` tip |
|---|---|---|
| newest commit | 2026-08-12 | **2026-08-06** |
| `en195-arcade.html` | **98,583 B** (v6.4) | 57,341 B (pre-v6) |

Tree diff branch → main is 195 files, **16,579 deletions against 1,792 insertions** —
main has strictly less. Present on the branch and absent from main: the whole
08-07 → 08-10 stream, including `SIX-MONTH-CONSULTATION-2026-08-07*.md`,
`aleph-fleet.py` and the aleph runs, `HITL-REVIEW-2026-08-08.md`,
`HANDOFF-2026-08-10-tick9.md`, `PRD-CHOOSE-YOUR-LEADER.md`, and both hired-in agent
seats (`.claude/agents/type-director.md`, `.claude/agents/union-rep.md`).

**Exactly one file exists on main and not on the branch:**
`en195-arcade-layout-preview.html` — and that file's own disposition is already
recorded in the branch's arcade TSP-META: *"Layout preview
(en195-arcade-layout-preview.html, 2026-08-06 v2) folded in same day and deleted."*
It was absorbed on purpose. **Nothing on main is at risk.**

## Why this happened (probable)

CLAUDE.md records that `git push` from a session container is 403-blocked and that
the GitHub connector is the working lane. `origin/main`'s history is the connector
lane's lineage; this container's repo is a separate lineage that was initialized
rather than cloned from that ref. Both are real; they simply never shared a root.

## Standing correction for future sessions

1. **Do not rebase this branch onto `origin/main`.** There is no base to rebase onto,
   and main is six days behind on content.
2. **Read the hook's "N behind" as unverified.** Before acting on it, run
   `git merge-base HEAD origin/main`. Exit 1 means the counts are meaningless as a
   staleness signal — compare **dates and tree content** instead.
3. **If the two lanes are ever to be reconciled**, the direction is branch → main
   (main takes the branch's content), and it is a founder call, not a mechanical
   fast-forward. `en195-arcade-layout-preview.html` is the only file needing an
   explicit keep/drop decision, and it is already ruled *drop* (folded in 08-06).

## Meta — how the error was caught

The founder's challenge was *"this is a fresh chat. what could be stale?"* The
container clone being fresh is not what the hook was measuring, and neither was the
chat — but the question forced a verification that the hook's own phrasing had
discouraged. **A mechanical signal that reports a number without reporting its
validity is a hollow claim.** `funes-tendrils.py` should either run the merge-base
check before printing "behind", or label the count as lineage-relative.
