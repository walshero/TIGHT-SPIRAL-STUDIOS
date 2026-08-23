# FINDING: stored state cannot tell when it has gone stale (2026-08-17)

*Founder question: how do we fix the problem that created "canon-manifest.json is
itself stale"? The answer is that the manifest is not the problem. It is one
instance of a class the studio has 18 of.*

## THE MEASUREMENT

Every JSON in the repo root that stores state a gate later reads:

| | |
|---|---|
| Stored-state files | **18** |
| Files carrying a fingerprint of the inputs they were derived from | **0** |
| Files carrying anything version-like at all | 1 (`aleph-taxonomy.json`, a bare `version` int, not an input digest) |

`aleph-blindspots`, `aleph-ledger`, `attribution-baseline`, `canon-manifest`,
`canon-vocab`, `comfort-baseline`, `contrast-baseline`, `fingers-baseline`,
`floor-baseline`, `gate-baseline`, `intent-baseline`, `lane-tendrils`,
`one-thing-baseline`, `retired-lines`, `scope-baseline`, `type-baseline`,
`voice-baseline`. Not one of them can answer "is the corpus I describe still the
corpus that exists?"

## THE ROOT CAUSE

**Canon is asserted in a side file instead of derived from the artifact, and the
side file carries no fuse.** Two independent faults, and both have to be fixed:

1. **Asserted, not derived.** `canon-manifest.json` says `preship-gate-v4.py` is
   canonical for the pre-ship role. `preship-gate-v5.py` exists in main and its own
   docstring says it supersedes v4. The truth was written in the artifact; the
   manifest was never told. A registry maintained separately from the thing it
   registers will always drift, because the update is a second action someone has
   to remember after the real work is done.
2. **No fuse.** Even a correct manifest goes wrong the moment the corpus moves. A
   file that is read as current but has no way to know it is stale will answer
   confidently with old data forever. That is precisely the failure mode
   `canon-guard.py` was built to catch, which is why it is worth saying plainly:
   **the guard against stale files was itself stale.**

This is the same shape as the git error retracted earlier this session
(`claude/FINDING-UNRELATED-HISTORIES-2026-08-12.md`): a stale ref read as current,
with numbers computed off it that looked like evidence. Different substrate,
identical failure. **Anything that can go stale must carry the means to detect its
own staleness.**

## WHY "JUST UPDATE THE MANIFEST" IS NOT THE FIX

It restores the same trap with fresher data. The manifest was accurate on
2026-07-26 and rotted in three weeks without anyone doing anything wrong. Updating
it buys another three weeks and teaches the studio that these files are
trustworthy, which is the belief that made this expensive.

## THE FIX, THREE LAYERS

**Layer 1, the fuse (universal, cheap, do this first).** Every stored-state file
carries a `_fuse` block: the glob of inputs it was derived from, a digest of those
inputs, and when it was generated. On read, the digest is recomputed; a mismatch
means the file reports **STALE, regenerate me** instead of answering. This does not
make anything correct, it makes wrongness *loud*, which is the whole difference
between the arcade quietly violating its own gate for eight days and the gate
saying so on day one. It generalises to all 18 files without knowing what any of
them mean.

**Layer 2, derive where derivation is possible.** `canon-manifest.json` should be
computed, not written. The correct source is a small machine-readable stanza in
each tool's own header, next to the code, authored in the same edit as the change:

```
# TSP-ROLE: pre-ship gate (manual, render-proof)
# TSP-SUPERSEDES: preship-gate-v4.py, preship-gate-v3.py, preship-contrast-gate.py
```

Then canon for a role is derived: the file nothing supersedes wins. Drift becomes
structurally impossible, because declaring the lineage *is* the act of shipping the
replacement.

**The blocker, measured:** exactly **one** file in the corpus currently declares
its lineage in any form (`preship-gate-v5.py`, in prose). So layer 2 cannot be
derived today; the convention has to be established across roughly thirty tools
first. That is a real cost and it is why layer 1 comes first.

**Layer 3, fix the false positive that will otherwise discredit layer 2.**
`canon-guard.py --refs` reads `preship-gate-v5.py`'s line *"Supersedes
preship-contrast-gate.py, preship-gate-v3.py"* as a live dependency on superseded
files and HALTs. Supersession and dependency are opposites; a machine-readable
`TSP-SUPERSEDES` header fixes this as a side effect, because a declaration in a
known field cannot be confused with a call.

## RECOMMENDED ORDER

1. **Build the fuse** (`stale-fuse.py`: `--stamp`, `--verify`, canaries), stamp all
   18 files, wire `--verify` into the belt as a WARN first and a HALT once the
   noise is known to be zero.
2. **Establish the `TSP-ROLE` / `TSP-SUPERSEDES` header convention**, starting with
   the gates that actually have lineage.
3. **Regenerate `canon-manifest.json` from the headers**, retire the hand-edited
   version, and fix the supersession false positive.
4. Only then wire `canon-guard.py` into the belt. Wiring it now would wire a gate
   that is both stale and crying wolf.

## STANDING RULE THIS EARNS

**Stored state without a fuse is a claim with no expiry date.** Any file a gate
reads as truth carries, from now on, the digest of what it was derived from. A
number computed from an unfused input is not evidence; it is a guess with decimal
places.
