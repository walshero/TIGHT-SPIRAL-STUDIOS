# OS BLOCK — POINTER-ONLY MEMORY (§12.7 detail)

*Locked 2026-07-10. The cross-lane primitive (§12) turned inward on memory itself.
Memory is at 30/30 because everything writes and nothing points. The stated
architecture — "MEMORY RUNS AS INDEX; the OS is the ARCHIVE" — is currently violated:
memory carries content the archive already holds. This spec makes the architecture
enforceable instead of aspirational.*

---

## The law

**A memory line carries an ADDRESS, not the content at that address.**

- **Compliant:** `Cross-lane mount primitive → os-block-cross-lane-mount.md §12`
  (a pointer: names the thing, points to where it lives, ~60 chars)
- **Violation:** a 400-word block restating what §12 says (content duplication —
  the archive already holds it; the memory line should point, not repeat)

The test: **could this line be replaced by "see <file> <section>" without losing
anything a future session needs?** If yes, it must be. The content lives in the
archive; memory holds only the address and the one fact that tells a session *whether
to go read it*.

---

## The three fields of a compliant line

1. **NAME** — what the thing is, in ≤8 words.
2. **ADDRESS** — the canonical file + section where it lives (`file.md §X`, a Drive
   ID, or a repo path).
3. **STATE** — the single volatile fact a session needs *before* deciding to open the
   address: `LOCKED` / `PENDING founder` / `HALTED` / `v34` / a date. This is the only
   content memory is allowed to hold, because it changes faster than a belt cycle and
   a session must know it to route.

Everything else — the reasoning, the full ruling, the history — lives at the ADDRESS.

---

## What memory MAY still hold as content (the exceptions)

Three kinds of fact have no stable archive address, so memory is their canon:

1. **Accessibility floor** — RP, the visibility verdict, no-opening-wall. This governs
   every build and must fire without a file read. It stays resident.
2. **Reply/output conventions** — line-one-answer, no-walls, scorecard format. These
   shape the reply being written *now*; a pointer would fire too late.
3. **Live STATE the manifest tracks** — but even here, memory holds the state and
   *points to the doc*, never restates the doc.

Everything outside these three is a pointer.

---

## The Studio Eyes check: `MEMORY-POINTER`

On any belt close that writes memory:
- **HALT** if a new memory line exceeds ~40 words AND its content exists at a known
  archive address (it should be a pointer to that address).
- **WARN** if a line has no ADDRESS field and is not one of the three resident
  exceptions (it may be orphaned content with no archive home — either give it a home
  or justify residency).

This is CLASS-TICK on memory itself: the belt's stated "condense, don't append" rule
finally has teeth. A line that appends content instead of folding to a pointer is a
defect, not a note.

---

## Migration (how 30/30 becomes room)

The belt does this incrementally, not in one bulk pass (bulk edits break the
as-opened discipline):

1. Each belt close, take the **longest content-carrying memory line** whose content
   lives in an archive file.
2. Confirm the archive address holds it (byte-check the section exists).
3. Replace the line with its pointer (NAME → ADDRESS → STATE).
4. One fold per belt. Promote-or-kill: if the content lives nowhere, either archive it
   first (then point) or kill it.

Within a handful of belts, memory is index-shaped and the overflow is structural
history, not a recurring crisis.

---

## Why this is the highest-ROI application

The 30/30 ceiling is the live constraint on *every* session — it's why belts
hand-condense and why context is scarce. Converting memory from content-duplication to
pointer-only is the difference between condensing by hand every belt and never
overflowing again. The other §12 applications improve governance; this one buys back
the resource the whole system runs on.
