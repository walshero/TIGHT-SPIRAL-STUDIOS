# OS BLOCK — THE HOLLOW CLAIM
*Tight Spiral Productions · the failure mode, named*
*Locked 2026-07-11. Companion to os-block-triple-sweep.md.*

---

## THE DEFINITION

> **A HOLLOW CLAIM is a success message that is not backed by bytes.**

It is the studio's dominant failure mode. Not "the work didn't get done" — but
**"the work reported done, and wasn't."** Hollow claims are worse than failures
because a failure stops you and a hollow claim lets you walk on.

---

## THE FOUR SPECIMENS (all found 2026-07-10/11)

1. **STUDIO EYES v4 (the phantom).** Two Drive pointers asserted a 17,534 B
   auditor existed and was canon. It was in no repo, no durable surface, nowhere.
   It had been "validated in-session" and died on container reset. **Nearly caused
   the deletion of the only working auditor (v3.5) on the strength of a pointer's
   word.** Caught by a 404.

2. **paste-gate-probe-30k.txt (the silent truncation).** Named for 30KB. Landed
   at **599 B**. The write bus ACCEPTED the truncated payload and returned
   success. Caught by reading the file.

3. **session-tree-2026-07-05 (the empty shell).** 249 B of HTML containing
   `<!-- Session tree content -->`. Sat on Drive for six days looking landed.
   Caught by opening it.

4. **`echo "=== WORKFLOW PUSHED ==="` (the assistant's own).** 2026-07-11, during
   the very session that wrote the Triple Sweep block: a shell command chained an
   unconditional success echo after a `git push` that had been **rejected**. The
   terminal printed WORKFLOW PUSHED over a failure. **The tool that was written to
   catch hollow claims generated one, minutes later, while its author was watching.**

**Specimen 4 is the important one.** It proves the rule cannot live in intent. It
must live in the *shape of the command*. A discipline that depends on remembering
is not a discipline.

---

## THE LAW

> **NO CLAIM OF SUCCESS MAY BE EMITTED THAT IS NOT DERIVED FROM THE ARTIFACT ITSELF.**

Corollaries, all learned the hard way:

- `created: true` is not proof.
- `success` is not proof.
- A returned file ID is not proof.
- A pointer asserting a target exists is **not proof the target exists.**
- **An `echo` after a command is not proof the command worked.**
- Exit code 0 from a *pipeline* is not proof — the last command's status wins,
  and `cmd | tail` masks `cmd`'s failure.

**The bytes are the proof. Fetch them back. Compare them. Then speak.**

---

## COMMAND SHAPE (enforcement — this is where it actually lives)

**BANNED:**
```bash
git push origin main 2>&1 | tail -3 && echo "=== PUSHED ==="     # LIES ON FAILURE
some_write_cmd && echo "SUCCESS"                                  # && after a pipe is not a guard
curl -X PUT ... ; echo "done"                                     # ; ignores status entirely
```

**REQUIRED:**
```bash
# 1. Capture status. Do not pipe it away.
git push origin main; RC=$?
# 2. Branch on the REAL status.
if [ $RC -eq 0 ]; then echo "PUSH OK"; else echo "PUSH FAILED (rc=$RC)"; fi
# 3. Then VERIFY from the far end — the artifact, not the command.
curl -sL "$RAW_URL" -o /tmp/check && \
  [ "$(md5sum < /tmp/check | cut -d' ' -f1)" = "$(md5sum < local | cut -d' ' -f1)" ] \
  && echo "VERIFIED BYTE-EXACT" || echo "HOLLOW — MISMATCH"
```

**The verification must interrogate the DESTINATION, never the sender.**

---

## THE DURABLE-SURFACE RANKING (learned 2026-07-10)

```
REPO (git push)   ← immutable, survives everything. THE only destination.
DRIVE             ← durable, but drifts; pointers rot; replace-in-place OK
SHELF (/mnt/project) ← durable but read-only and lags
OUTPUTS           ← ✗ NOT A DESTINATION. Resets between sessions. A scratchpad.
CONTAINER (/home) ← ✗ NOT A DESTINATION. Dies at session end.
```

**"Validated in-session" is not landed.** The v4 phantom lived and died on this
distinction. Anything that must survive gets pushed to the repo, then fetched
back and byte-compared, in the same breath.

---

## GITHUB PAT — THE COMPLETE SPEC (stop re-deriving this)

Fine-grained token, repo `TIGHT-SPIRAL-STUDIOS`, owner `walshero`.
**All three permissions are required. Contents alone is NOT enough.**

| Permission | Level | Why |
|---|---|---|
| **Contents** | Read and write | push files |
| **Workflows** | Read and write | push/edit `.github/workflows/*` — **git REFUSES workflow files without this, and so does the Contents API (403)** |
| **Pages** | Read and write | the auto-deploy job |
| Metadata | Read-only | auto-set, leave it |

**Phone path:** github.com → profile picture (top right) → Settings → scroll to
bottom → Developer settings → Personal access tokens → Fine-grained tokens →
[token] → Permissions → Repository permissions → set all three → scroll to
bottom → **Update token** (green button; the change does not save without it).

**Gotcha:** "Workflows" is alphabetical, **below Webhooks**, easy to scroll past
on a phone. Expiration: choose the longest available — re-deriving this costs a
session.

**Token lives in chat only.** Never in memory, never in a file, never committed.
Container resets each session, so it is re-pasted each time.

---

## THE CLASS-FIX ENGINE (tool, not just a lesson)

CLASS-TICK says: on any bug, sweep the corpus and fix the CLASS, never the
instance. Tonight that killed a dark-mode failure across **39 files in one pass**
(173 → 104 HALTs). The pattern, reusable:

```python
import re, glob
FIXED = []
for path in sorted(glob.glob('*.html')):
    html = orig = open(path, encoding='utf-8', errors='replace').read()
    # 1. detect the class signature
    # 2. apply the root fix (not the symptom)
    # 3. only write if changed
    if html != orig:
        open(path, 'w', encoding='utf-8').write(html)
        FIXED.append(path)
print(f"CLASS-FIX: {len(FIXED)} files")
```

**The two fixes it applied (both now standing law for every new build):**

1. **`:root { color-scheme: light; }`** must be declared, or the OS forces its own
   dark palette and repaints inherited colors.
2. **Never `color: inherit` on a comfort/a11y control.** Pin the ink (`#241f16`).
   Under OS dark mode, `inherit` made the Comfort button render at **1:1 contrast
   — text and background the SAME COLOR — across 18 files.** The control that
   exists so Matt can see was invisible. **Static analysis is structurally blind
   to this.** Only a rendered browser in real dark mode reveals it.

---

## WHAT THIS BLOCK DEMANDS OF EVERY FUTURE SESSION

1. Never emit a success line that isn't derived from the artifact.
2. Never chain `&& echo "DONE"` onto a write.
3. Never delete a working artifact on a pointer's claim — verify the replacement
   exists on a durable surface first.
4. Fix the class, not the instance.
5. If it must survive, it goes to the **repo**, and you **fetch it back**.

---

## CHANGELOG
- **2026-07-11** — Block created. Trigger: four hollow claims in 24h, the fourth
  generated by the assistant itself while writing the block that bans them.
  Proof that the rule must live in command shape, not intent.
