# THE LANE REGISTRY — canon across FOUR lanes
**2026-07-11. Written after declaring a finished game "lost" that was live on a lane I never checked.**

---

## THE FAILURE THAT PRODUCED THIS FILE

I told the founder **Dad Energy was lost.** Searched the repo. Searched the shelf. Searched Drive.
Not there. Declared it gone.

He replied with a URL. **It is live on Netlify at v2.1** — a version *later* than anything in any chat.

**I asserted absence after searching three of four lanes.** Earlier the same session I had written
the rule *"a zero-result search is not evidence of absence"* — and then broke it within the hour.

**A resolver that only knows some lanes is not a resolver. It is a fourth silo with better manners.**

---

## THE FOUR LANES

| Lane | What it is | Authority | Knows about the others? |
|---|---|---|---|
| **GitHub repo** `walshero/TIGHT-SPIRAL-STUDIOS` | Live site + canon files. **Content-addressed — cannot lie.** | **CANON for anything deployed** | No |
| **Netlify** `relaxed-gaufre-a0c223.netlify.app` | **Standalone game deploys.** Dad Energy v2.1 lives here. | Canon for what only lives here | No |
| **Google Drive** `Claude_files` (walshero) | The **zipper** — Command Center, pointers, OS blocks | Canon for *addresses*, not files | No |
| **Project shelf** `/mnt/project` | A **CACHE. It lags. It is never canon.** | **NEVER canon** | No |

Plus one non-lane: **`outputs/` is a staging bench. Nothing lives there.** It evaporates when the
chat closes. Every loss this studio has suffered came from a file that stopped here.

---

## `resolve_canon(name)` — THE SPEC

**One action. Reads all four lanes. Refuses to guess.**

```
resolve_canon("dad-energy")
  → found_in:   [netlify]
    canon_lane: netlify
    address:    https://relaxed-gaufre-a0c223.netlify.app/
    version:    v2.1
    md5:        <computed live>
    absent_in:  [repo, drive, shelf]
    warning:    SINGLE-LANE — no backup. One Netlify account change and this is gone.

resolve_canon("confluence-TRUNK")
  → found_in:   [repo, shelf]
    canon_lane: repo
    address:    raw.githubusercontent.com/walshero/TIGHT-SPIRAL-STUDIOS/main/confluence-TRUNK.html
    version:    v44   bytes: 598114   md5: 8dcf990336eb1c0ffa600cae3b689539
    fossils:    [shelf v34 — DELETED 2026-07-11]
```

### THE GATE

> **No file may be edited until `resolve_canon` has returned for it in this session, across
> ALL FOUR LANES, and the working copy's md5 matches canon.**
>
> **A hash mismatch is a HALT. "Not found" is a HALT until all four lanes are checked.**

### Implementation notes (real constraints, learned today)

- **Repo:** `git clone` + md5. Trivial. Content-addressed, authoritative.
- **Drive:** Zapier `list_all_drive_files` — **MUST scope by folder ID**; unscoped overflows.
  **A `name contains` query silently returned ZERO today while two matching files sat in the
  folder.** Do not trust filtered Drive queries. **List the folder and filter locally.**
- **Shelf:** direct read. Fast. **Always suspect.**
- **Netlify:** the container **cannot reach it** (egress allowlist blocks
  `*.netlify.app`). `web_fetch` **can**. Either add the host to egress, or resolve Netlify
  via `web_fetch` and treat it as read-only.

---

## SILOED RIGHT NOW — shelf-only, not in any deploy lane

**Twenty-five files exist ONLY on the shelf.** If the shelf is a cache, these have no home.

**Big and probably real:**
```
claude_cliche-cabinet-suite.html      113,355 B
confluence-TRUNK-v43-2026-07-10.html  597,191 B   (superseded by v44 — DELETE)
fys_fys-treasure-trove.html            63,325 B
funny-boneys-factory.html              42,709 B
behind-this-door.html                  42,400 B   (the "known dead link" — IT EXISTS)
en195-what-counts-now.html             40,508 B
claude_cliche-field.html               27,591 B
claude_tsp-home.html                   25,503 B
claude_cliche-line.html                21,472 B
recursion-ledger.html                  20,906 B
laughter-foundry-spec-and-log.html     20,968 B
claude_cliche-city.html                20,503 B
group-foreman.html                     17,801 B
founder-compass.html                   17,349 B
studio-river.html                      15,781 B
open-house-strategic-plan.html         15,142 B
paper-craft-ceiling.html               14,868 B
convergence-card-engine.html           13,593 B
play-tight-spiral.html                 13,040 B
timing-belt.html                       11,490 B
session-tree.html                      11,293 B
legibility-optimizer.html               9,899 B
claude_cliche-cabinet.html              9,242 B
dark-stop-lab.html                      7,404 B
```

**`behind-this-door.html` is the sharpest finding.** It was recorded as a **dead link** in the
404-Forward-Guard block. **It is not dead — it is 42 KB of real file that was never pushed.**
The guard correctly found a broken door and the studio pruned the link instead of shipping the
room behind it.

---

## FIXED THIS SESSION

- **`en195-hub.html`** — was **shelf-only** while students 404'd on it. Swept (0-HALT),
  404-guard green (all six doors live), **pushed and byte-verified.**
  Live: `walshero.github.io/TIGHT-SPIRAL-STUDIOS/en195-hub.html`
- **`warriors-fantasy-arcade.html`** — repo held a **2,277 B empty stub**; the shelf held the
  **real 19,577 B game**. Pushed the real one. *Fork-diff rule: never default to the smaller file.*
- **All dated handoffs → one `HANDOFF.md`.** No dates in filenames. History lives in git.

---

## THE RULE THIS ALL POINTS AT

**Every loss in this studio has the same shape:**

> **built → landed in `outputs` → never pushed → chat closed → gone**

The Gatekeeper charter already says *"Outputs folder is a staging bench, nothing lives there."*
**Written, never enforced.** Three weeks of work sat in dead chats because saving depended on
*remembering*.

**TICK 5 — AUTO-PUSH AT CREATION.** Every file lands in a real lane **in the same turn it is
made**, byte-verified. Small → Drive bus. Large → git-push (no size limit, proven). Standalone
game → Netlify. **Un-pushable → flagged LOUDLY as un-backed-up, never silently.**

**And the standing lesson, twice-earned today:**

> **A zero-result search is not evidence of absence. When a search comes back empty,
> LIST THE CONTAINER AND LOOK.** It lied about Drive files. It lied about Dad Energy.
> Both times I believed it.
