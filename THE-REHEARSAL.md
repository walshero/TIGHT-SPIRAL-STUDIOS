# THE REHEARSAL

**Test the Cold Start without deleting anything.**

You are not ready to wipe 220 files on my word. Correct. I already got a count wrong
today, and a filename classifier of mine nearly destroyed `funnyboneysfactoryspec.pdf`.
**Don't delete on a promise. Delete on a proof.**

There are two proofs, and they answer different questions.

---

## PROOF 1 — DOES ANYTHING DIE?  (arithmetic, done)

`shelf-safe-to-delete.py`, in the repo. Run it any time, from a clone:

```
python3 shelf-safe-to-delete.py
```

It hashes **every blob in `origin/main`** and matches your shelf files **by content,
not by filename**. That distinction is the whole point — my classifier reasoned about
names and was wrong. This reasons about bytes.

- **exit 0** — every shelf file has a twin in git. Nothing dies.
- **exit 1** — names the files that would die. Do not delete.
- **exit 2** — HALT. Cannot read git. Never guesses.

**Current verdict: exit 0.** All 163 shelf files have a twin. 120 byte-identical,
2 identical under a different path, 41 drifted (repo version is canon).

Re-run it before you delete. Re-run it tomorrow. It cannot go stale, because it
recomputes.

---

## PROOF 2 — CAN A COLD CLAUDE ACTUALLY WORK?  (the real bet)

File safety is the easy question. The one you're actually betting on is:

> *With only five files resident, does the machine still know what it's doing —
> or does it get slower, dumber, and start asking me things it should know?*

**You cannot answer that by reading. You answer it by running one.**

### The rehearsal

**1. Do not touch this project.** Leave all 220 files where they are.

**2. Open a NEW project.** Call it `TSP — COLD`.

**3. Upload only the five files** in `STAGING/cold-shelf/`:

| file | size |
|---|---|
| `COLD-START.md` | 6,621 B |
| `STUDIO-COMMAND-CENTER.md` | 6,782 B |
| `tight-spiral-studio-os.md` | 169,275 B |
| `LANE-REGISTRY.md` | 6,419 B |
| `cross-lane-manifest.md` | 3,878 B |

**4. Paste the coherence block into that project's Instructions.** This is the piece
your own Command Center calls *"the one thing only the founder can do."* Instructions
fire before the session's first word. A shelf file does not.

**5. Give it a real task.** Not a test question — a real one. The build you actually
want. Watch what happens.

### What you are watching for

| signal | means |
|---|---|
| It fetches from git before editing a named file | **The pathway holds.** |
| It knows the law without being told | The OS is doing its job resident. |
| It knows what's gated and what's owed | The Command Center is doing its job. |
| It asks you something it should be able to compute | **Pathway leak. Tell me.** |
| It edits a file without fetching it first | **Pathway failure. Tell me.** |
| It claims a file doesn't exist without listing the container | **Old disease. Tell me.** |

### The honest failure mode

The thing most likely to go wrong is not that it *can't* find files. It's that it
**doesn't bother** — that it answers from the OS and memory when it should have gone
and looked. Warm habits in a cold room.

If that happens, the fix is not a bigger shelf. It's a louder instruction.

---

## THE DECISION GATE

Delete the 220 **only after all three are true**:

- [ ] `shelf-safe-to-delete.py` returns **exit 0** (it does, today)
- [ ] The complete zip is **downloaded and on your Mac** — 21 MB, 377 files, md5 `9e2a4607`
- [ ] You ran a **real task** in `TSP — COLD` and the machine held

Until then, this project stays exactly as it is. Nothing is lost by waiting. The repo
is already home; the shelf is now redundant, not load-bearing.

---

## WHY THIS IS WORTH THE TROUBLE

The 220-file shelf is not neutral. It is *actively harmful*, in a way that is now measured:

- `studio-eyes-sweep.py` on your shelf is **8,682 B**. In the repo it is **23,968 B**.
  The shelf is holding a badly truncated version of your own sweep tool — and nothing
  about looking at it would tell you that.
- `sandbags.html` is **bigger** on the shelf, which reads like "more game." It is more
  **wall** — the retired comfort gate you explicitly killed.
- Twenty-four files are each exactly **92 bytes** short of the repo version. One shared
  fix, applied repo-side, absent from every shelf copy. A uniform delta across unrelated
  files is a signature, not a coincidence.

A cold Claude holding five verified files is not a diminished Claude. It is one that
**cannot be handed a fossil and told it is canon** — which is what has been happening.

---

*The repo is home. Drive is an address book. The shelf is a cache and it lags.*
*Prove it, then delete it.*
