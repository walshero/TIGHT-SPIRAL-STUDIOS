# THE FORKING PATHS PROTOCOL — TSP standing rule

Ratified by the founder 2026-08-03. Repo-lane copy (canon FILES home).
Twin lives in Confluence project canon memory as `claude/forking-paths-protocol.md`.
Read before computing canon in ANY session. If this protocol can't run, say BLIND — loudly.

## The sentence that is the rule
TSP is wired like the GARDEN OF FORKING PATHS: hold ALL PATHS AT ONCE,
through BABEL (every lane), via the ALEPH (one view of all lanes simultaneously),
with FUNES (hash-perfect memory of everything seen).

## What each figure means operationally — a check, not a mood
- BABEL = the full lane list. No lane silently skipped:
  git repo · Netlify · Google Drive (walshero) · Google Drive (post.massbay) ·
  Dropbox (ns:6905321) · project shelf · code sessions · chats · cowork ·
  iOS Notes · OneDrive · founder canon (Matt's word on working vocabulary).
  A zero-result search in one lane is NOT absence. Unreachable lane -> verdict BLIND, named.
- ALEPH = one simultaneous view. Canon is never declared from a single lane.
  The oracle's output is the whole garden: every copy, every lane, every hash, at once.
  `single_lane` is itself a defect (NO BACKUP), never a proof of canon.
- FUNES = the ledger of hashes. Canon is the content hash, never the filename or the
  eyebrow (both lie — proven: a "v43" label on an Aug-2 file). Every new hash seen
  gets recorded the same session. Funes is NOT omniscient: he remembers only what the
  Aleph showed him. Ledger rows older than the last Aleph pass are stale by default.
- FORKING PATHS = forks are data, not errors. When lanes disagree, do not collapse
  prematurely to newest/biggest/oldest. Enumerate all forks with verdicts:
  AGREE / DIVERGED / STRANDED / BLIND — then the founder (or the gate) picks the path.
  Proven necessary 2026-08-03: newest bytes (repo, Aug-2) and canonical bytes
  (v43, Drive Build Versions) had silently come apart; only the all-paths view saw it.

## VOICE runs under the same protocol
- The founder's own pre-machine words are PRIMARY SOURCE. Machine prose is fallback,
  HITL-edited by the founder.
- Founder words are TAGGED to the principle they express (provenance-bound quote -> principle).
- Authorship is claimed from content + naming signals, never from storage location.
- Excluded as source text: copyrighted collected material (reference only) and
  student work (FERPA-quarantined).
- Voice baseline lane: Dropbox 1998–2021 (machine-writing-free).
  Anchor: /mwalsh/All I wanna do is crawl.docx (2014).
- TRUTH (provenance) precedes REPAIR (fixing machine prose "unlike him"). Always.

## Session obligations (the runnable form)
1. Before editing any named file: run the Aleph pass across all reachable lanes; hash everything found.
2. Record new hashes in the FUNES ledger the same session they are seen.
3. Declare every unreachable lane BLIND by name. Silence must never read as agreement.
4. Nothing survives a chat unless pushed to a real lane, byte-verified, same turn.
5. When the founder pushes back on a machine-produced fact, the machine is the suspect. Re-derive from source.
6. ENFORCEMENT GAP (open): extend resolve-canon.py from repo-only to lane-aware —
   emit AGREE/DIVERGED/STRANDED/BLIND across the Babel list. Until it lands, this
   protocol runs by hand at session start. A rule that can't be a check is a wish;
   this file is the spec for the check.

---

## LANE RULING 2026-08-09 — this path is now the repo-lane canon

**Founder: "Make this write lane. I auth."**

Everything ABOVE this line is the ratified protocol text, byte-for-byte as it stood at
repo root `FORKING-PATHS-PROTOCOL.md` (3430 B, md5 `a731c5c34d5b65292c3d4309bf403c59`,
blob `26db9524`, commit `c11ee6a`). It is not retyped and it is not edited. Ratified
founder text does not get quietly improved.

**What changed is the address, and the reason is arithmetic.** The standing instructions
order every session, unprompted, to run the Aleph pass *per this path*. Until today no file
existed here, in any lane the repo can reach. `scope-gate.py` (belt tick 8, armed
2026-08-09) measured it: the instruction named three files at `claude/` paths and **none of
the three resolved in the trunk.** A rule that points at a file nobody can fetch fails
silently and forever — the session reads the instruction, finds nothing, and proceeds. That
is exactly how `claude/FERPA-SCOPE-RULING.md` went unread twice in one day by the agent
whose enforcement clause names it.

So the canon moves to where the instruction points, rather than the instruction being bent
toward the canon. **Root `FORKING-PATHS-PROTOCOL.md` is now a POINTER to this file, not a
copy.** One canon writes; others read. Two copies of a protocol is the failure this
protocol exists to name.

**Decided from CONTENT, not from preference.** The root copy still carried obligation 6 as
an open enforcement gap. That gap closed 2026-08-06 when `resolve-canon.py` went
lane-aware. The text carried below has been the fuller and more current record since then
and lived only on the project shelf — a lane the studio instructions call a cache that
lags and is never canon. The stale copy was the one at the addressable path. That is the
whole finding.

## AMENDMENTS — carried in from the shelf lane, never previously in the repo

**Founder ruling, 2026-08-06.** The protocol header above says the twin "lives in
Confluence project canon memory." Asked who owns it, Matt: *"we don't build confluence but
we inform and live in the same universe."* Applied reading, per ONE CANON WRITES / OTHERS
READ: **TSP writes this file; Confluence reads it.** TSP does not write into Confluence's
canon. The protocol had claimed two homes since ratification and had zero until 08-06.

**Obligation 6 is CLOSED as of 2026-08-06.** `resolve-canon.py` at repo root is lane-aware.
It emits the BABEL roll call over nine lanes, per-file AGREE / DIVERGED / STRANDED / BLIND /
UNWITNESSED, and exit 3 = INCOMPLETE when any lane was blind. Run it at session start:

    python3 resolve-canon.py --aleph --watch index.html,en195-arcade.html,FUNES-LEDGER.md

It must be run **from a clone of the repo** — the repo probe is `git ls-tree origin/main`.
Lanes with no machine path (Drive, Dropbox, OneDrive, iOS Notes) stay BLIND until an agent
supplies `--evidence <file.json>`; a lane closed by evidence prints LIVE and is named in the
roll call as evidence-supplied, never as directly probed.

Two things the resolver taught us on its first real run, both enforced in code:

A **lane check** asks whether the copies agree. A **ledger check** asks whether the record
still describes the bytes. Two of the four findings from the 2026-08-06 Aleph pass were
ledger failures, not lane failures, and no code existed for them at all.

A cross-lane finding needs two lanes. Run the resolver with one lane live and every file in
the repo comes back STRANDED — 533 lines, all arithmetically true, all noise. Single-lane
holdings now report UNWITNESSED (backup status *unknown*, not *absent*), and STRANDED /
DIVERGED print NOT COMPUTABLE rather than "(clean)". A pass the run did not earn must never
print as a pass.

### LANDED IDENTITY — resolve-canon.py

Canon for the resolver is **38353 B**, md5 `58d3a8fa2a0f63dd0da783b08a1e832d`, blob
`34d58994`, commit `abb98f6d` — the basename-collision fix of 2026-08-08. Two earlier rows
named 36271 B / blob `3d3b5d9f` and 36272 B / blob `5e42e244`; both are **superseded**. Any
session holding either is holding a fossil.

Why the corrections exist, because it is the whole lesson: the file could only reach the
repo as hand-copied base64 chunks (no push credential for this repo from the sandbox; gists
and public file-drops are proxy-blocked). **Two of the first five landed wrong.** The seed
carried bytes from a stale draft. Chunk three gained a byte because the agent silently
normalized an irregular 23-space continuation indent to 24 while transcribing — source
indentation outside the string literal, so zero behavioral change and a different file.
Both wrong writes returned `success: true`. Only the byte count caught them, both times.

The rule that follows is arithmetic, not prose: **after any chunked push, fetch the file
back and diff it.** The tool's byte count is the check; its success flag is decoration.
Where the two disagreed, the landed bytes were adopted as canon and the local copy resynced
down to match — canon is computed from what is actually in the lane, never from what the
agent believes it sent. That discipline now has a tool: `stage-push.py`.

### WHAT STILL HAS NO CHECK

Obligation 6 is closed; obligation 3 is not. Declaring an unreachable lane BLIND by name is
still a thing a session does by hand, and a session that simply forgets produces silence
that reads as agreement. `scope-gate.py` closed the adjacent gap — a governance doc may no
longer name a file the trunk cannot reach — but it reads artifacts, not runs. Naming that
here so the next session inherits the gap instead of rediscovering it.
