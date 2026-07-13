# SHELF DELETE LIST — 2026-07-11
**Read top to bottom. Delete in this order. Do not group by category — this is shelf order,
which is how you scan it.**

Every file below is **superseded by canon in the repo.** Nothing here is unique.

---

## THE RULE THAT PREVENTS THIS

> **ONE handoff file. Canonical name: `HANDOFF.md`. No date in the filename.
> Replace, never add. Dates go INSIDE the file. History lives in git — that is what git is for.**

Fifteen files whose names differ only by a date or a `_2` suffix is **not a filing system**.
Three of them (`session-handoff-2026-07-01`, `_2`, `_3`, `_4`, `-close`, `-close_2`) differ by
a single character. **A file whose name you cannot distinguish from fourteen others is a file
you cannot use.**

This is an accessibility defect in the studio's own conventions, and the studio produced three
more of them today while diagnosing it.

**Already done in the repo:** all dated handoffs collapsed into `HANDOFF.md`.

---

## DELETE — shelf order, top to bottom

```
[ ]  1. HANDOFF-the-zipper-2026-07-11.md
[ ]  2. NEXT-SESSION-OPENER.md            (if present on shelf)
[ ]  3. READ-ME-FIRST-handoff.md
[ ]  4. belt-run-2026-07-05.md
[ ]  5. confluence-TRUNK.html             <-- v34 FOSSIL. Canon is v44 in repo.
[ ]  6. confluence-walkthrough.html       <-- v29. Five versions stale.
[ ]  7. funny-boney-session-kernel-2026-06-30.md
[ ]  8. handoff-arcade-praxis-2026-07-02.md
[ ]  9. new-chat-handoff-2026-06-28.md    (if present on shelf)
[ ] 10. os-block-truth-ticks.md           <-- incomplete draft. Repo has final (has TICK 5).
[ ] 11. reconciled-ledger-2026-07-02.md
[ ] 12. session-decisions-2026-06-28.html
[ ] 13. session-handoff-2026-07-01-close.md
[ ] 14. session-handoff-2026-07-01-close_2.md
[ ] 15. session-handoff-2026-07-01_2.md
[ ] 16. session-handoff-2026-07-01_3.md
[ ] 17. session-handoff-2026-07-01_4.md
[ ] 18. session-handoff-2026-07-02-belt.md
[ ] 19. session-handoff-2026-07-11.md
[ ] 20. session-roundup-2026-06-29-evening.md
[ ] 21. session-roundup-2026-06-29.md
[ ] 22. studio-eyes-sweep.py              <-- THE BROKEN AUDITOR. Repo has the repaired one.
```

**Then save the replacements** (from outputs or the repo):
- `HANDOFF.md` — the one handoff
- `studio-eyes-sweep.py` — the repaired auditor (448 lines)
- `studio-eyes-canary.html` — mandatory test fixture
- `os-block-truth-ticks.md` — final version

---

## KEEP — these are NOT handoffs. Do not delete.

| File | What it actually is |
|---|---|
| `TSP_Ledger.md` | **The decision log.** *"This file is truth; chats are archive."* |
| `belt-ledger.md` | Belt runs. Canonical name, replace-don't-add. |
| `provenance-ledger.html` | A **build** — enforces the provenance floor. |
| `recursion-ledger.html` | A **build** — OS governance made executable. |
| `session-tree.html` | A **build**, not a document. |
| `confluence-HANDOFF-2026-07-10.md` | **Confluence's own roadmap.** Moves to the Confluence Project — not deleted. |

---

## DO NOT DELETE — and this one needs a push, not a delete

**`warriors-fantasy-arcade.html`** — shelf **19,577 B** · repo **2,277 B**

**The shelf copy is the REAL GAME. The repo has the broken placeholder stub.**

This is the one file where the shelf is right and canon is wrong. **Push it to the repo before
touching anything else.** The fork-diff rule caught this — *never auto-default to the smaller
file; diff content first.*

---

## WHY A HAND CLEANUP ROTS AGAIN BY TUESDAY

This list is a symptom, not a cure. The shelf drifted because **nothing computes canon** — it
is a thing to be remembered, and remembering fails.

**The cure is `resolve_canon` + the edit gate** (see `HANDOFF.md`):

> No file may be edited until `resolve_canon` returns AND the working copy's md5 matches
> canon. A mismatch is a **HALT**.

Build that first. Then this list never needs writing again.
