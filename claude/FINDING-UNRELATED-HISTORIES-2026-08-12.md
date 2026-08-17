# RETRACTED : this finding was wrong. See the correction below.

> **RETRACTED 2026-08-14.** The claim in this document, that `origin/main` and
> `claude/en195-poetry-arcade-1aunsp` are unrelated histories and that main is the
> stale one, **was false**, and it was false because of my own error. The document
> is kept rather than deleted so the mistake stays legible, but **do not act on
> anything below the correction.**

---

## THE CORRECTION

**What actually happened.** This session never ran `git fetch`. Every judgement in
the original finding was computed against the container's **clone-time
remote-tracking ref**, which was stale and pointed at a different lineage
(root `6e16918`). One `git fetch origin` on 2026-08-14 replaced it with the real
`origin/main`, and every number changed:

| | Claimed (stale ref) | Actually true (after fetch) |
|---|---|---|
| Shared ancestor | none, `merge-base` exit 1 | **`d1bda1c`** |
| Root commit | different roots | **identical root `b5277d8`** |
| Branch position | 50 ahead, 51 behind, unrelated | **10 ahead, 25 behind** |
| `origin/main` tip | 2026-08-06, "stale" | current, carrying PRs #24, #25, #48, #49, #50 |
| Files only on main | 1 (`en195-arcade-layout-preview.html`) | **14**, including the whole `confluence-hub/` lane, `c1-check.py`, `the-break-room-v2.html`, and a GitHub Actions workflow |

So the branch was never stranded on an orphan lineage. It was an ordinary feature
branch that had fallen behind, and **50 of its 60 "unique" commits were already in
main.** The 10 genuinely unique ones were this session's ENJAMBMENT work.

**What the error would have cost.** The original document told the next session, in
bold, *"Do not rebase this branch onto `origin/main`"* and *"the direction is
branch → main (main takes the branch's content)."* Acting on that after the fetch
would have taken the branch's tree wholesale and **deleted 14 files of real work,
including a live CI workflow and an entire hub lane.** The advice was confidently
wrong in the destructive direction.

**Resolution.** `git merge origin/main` into the branch on 2026-08-14: clean, zero
conflicts, 20 files changed, all additions. Both sides verified present, gates
re-run green on the merged tree, and the game regression-tested in both modes.

## WHAT I GOT RIGHT, AND WHY IT STILL MISLED

The original finding was correct that the tendrils hook's "N behind" line is
unverified and should not be trusted on its own. It then made exactly the mistake
it was warning about: it *trusted a ref* instead of refreshing it, and dressed the
result in measurements. Numbers computed from a stale input are not evidence; they
are the same guess with more decimal places.

## THE RULE THAT REPLACES THIS DOCUMENT

1. **`git fetch origin` before any claim about a remote branch.** A
   remote-tracking ref in a fresh container is a snapshot from clone time and can
   be arbitrarily wrong. Nothing about `origin/*` is knowable without it.
2. **`git merge-base` exiting 1 is a claim about your refs, not about history.**
   Unrelated histories are rare; a stale ref is common. Suspect the ref first.
3. **Never propose "take one side's tree wholesale" across a divergence you have
   not fetched.** Enumerate what only the other side has, by name, and say what
   happens to each file.
4. The tendrils hook still computes against whatever ref it finds. Its "behind"
   count remains advisory. **Fetch, then judge.**

## ORIGINAL DOCUMENT (SUPERSEDED, DO NOT ACT ON)

The original text claimed unrelated roots (`b5277d8` vs `6e16918`), a 16,579-line
deletion delta against main, and that `en195-arcade-layout-preview.html` was the only
file at risk. The root pair was real for the stale ref; everything concluded from
it was not. It has been removed rather than left in place to be skimmed and acted
on by mistake.
