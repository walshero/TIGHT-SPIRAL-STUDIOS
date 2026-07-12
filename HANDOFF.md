# HANDOFF — 2026-07-11
**Read this first. It supersedes `session-handoff-2026-07-11.md` and
`HANDOFF-the-zipper-2026-07-11.md`, which were written mid-session before the diagnosis landed.**

---

## THE ONE THING

**Build `resolve_canon` — ACROSS ALL FOUR LANES — before touching another file.**

**FOUR lanes, not three:** GitHub repo · **Netlify** · Google Drive · Project shelf.
I declared a finished game (Dad Energy) LOST after searching three of them. It is **live on
Netlify at v2.1**. A resolver that knows only some lanes is a fourth silo with better manners.
See `LANE-REGISTRY.md`.

I spent this entire session doing good work on `confluence-TRUNK.html` **v34**.
Canon was **v43** — nine versions ahead, in the repo.

The file that would have told me — `confluence-TRUNK-POINTER.md` — **already existed in
Drive Claude_files.** It already said *canon is v43, here is the md5, here are the fossils
by ID*, and it **named the exact v34 file I was editing as superseded.** Four tool calls
away. Never opened.

**The system was not broken. There was no gate forcing me through it.**

---

## THE FIX (one action, one gate)

### `resolve_canon(name)` — a Zapier code action

Reads the `*-POINTER.md` files that **already exist** in Drive Claude_files. A lookup, not
an inference. An afternoon to build.

```
resolve_canon("confluence-TRUNK")
  → canon_lane: repo
    address:    raw.githubusercontent.com/walshero/TIGHT-SPIRAL-STUDIOS/main/confluence-TRUNK.html
    version:    v43   bytes: 597191   md5: bed8c7a3c3546fdab0efc08f1fef6930
    fossils:    [Drive 1ndz… v33 · Drive 1fZR… v34 · shelf mount v34]
    owner_lane: Confluence (RW)
```

### THE GATE — this is the part that matters

> **No file may be edited until `resolve_canon` has returned for it in the current session
> AND the working copy's md5 matches what canon claims. A hash mismatch is a HALT — same
> force as a failed contrast check.**

That gate would have stopped this session at minute two. Not with a reminder. **With a refusal.**

### Why a gate and not a rule

Six rules should have caught today's failure. **One did.**

| Rule that existed | Fired? |
|---|---|
| OS §12 — "canon is an ADDRESS, not a copy" | No |
| `confluence-TRUNK-POINTER.md` (md5 + fossil list) | No — never opened |
| Fork-diff rule — "never default to the older file" | No |
| SOURCE-FIRST LOCK — "open the actual file first" | No |
| Session-open card — "mount is fallback only" | Partially |
| **POST-TICK byte-verify** | **YES** |

The only rule that fired was the **mechanical** one — a byte-check that either matches or
does not. Every rule that required *remembering* failed.

The studio already proved this principle and wrote it down:
*"Contrast is a COMPUTATION, not a judgment… Matt has RP, contrast cannot be a step someone
remembers."*

**Canon is a computation too.** It cannot be a step someone remembers either.

**STOP MINTING BEHAVIORAL TICKS.** I responded to an enforcement failure by writing four
more rules. That is the disease treating itself as the cure. **If a rule cannot be a check,
it is a wish.**

---

## SUPPORTS (all already half-built)

1. **Pointers for every trunk.** `confluence-TRUNK-POINTER.md` is the working template —
   version · bytes · md5 · address · owner-lane (RW/RO) · fossils by ID · gate status.
   Clone for: CYL, studio-os, studio-eyes, Leeder.
   **Pointers are small → they pass the Drive bus. Trunks are big → they live in the repo,
   which has no size limit.** Already correct, already proven.

2. **THE ZIPPER (founder ruling).** Walshero Drive `Claude_files` = the junction where every
   lane's canon **address** lives. Not a backup folder.
   **Confluence gets its own Claude Project** — off the TSP shelf, which is over-full and is
   itself a drift generator.

3. **AUTO-DRIVE / AUTO-PUSH AT CREATION (TICK 5).** Small → Drive bus. Oversized → git-push
   (**proven byte-exact today**). Un-pushable → flagged **LOUDLY** as un-backed-up, never
   silently. *The corrected Confluence build sat in `/tmp` for nine turns today and would
   have evaporated if the founder hadn't asked.*

---

## STATE — WHAT IS TRUE RIGHT NOW

### Studio Eyes: REPAIRED, PUSHED, VERIFIED ✓
`studio-eyes-sweep.py` — 448 lines, commit `07f1db9`, byte-verified on GitHub.
**Shelf HALTs 42/57 → 20/57.** Twenty-two files were blocked by an auditor that was wrong.

Six grounding bugs, all live, all fixed:
1. **CSS comments glued onto selectors** (ROOT CAUSE) — `/* MASTHEAD */ .mh {}` parsed as a
   selector named *"comment plus .mh"*. Any selector after a comment was unfindable.
2. Only the **first `<style>` block** was read.
3. **`@media`/`@supports`** broke the flat parser the same way.
4. **Grouped selectors** never split.
5. **Ancestor walk was whitespace-only** — `.mh-name` has no space, so the loop never ran.
   Fixed with real DOM grounding + BEM-prefix fallback.
6. **Element's own background never checked** before walking to ancestors.

**The honesty rule:** proven failure → **HALT**; unresolvable ground → **WARN/UNGROUNDED**.
The auditor no longer asserts what it cannot verify. *An auditor that cries wolf is worse
than none.*

**TICK 3 built as H6** — HALTs institution-asserting files with no source + last-verified
date. *Honest limit: it verifies provenance **exists**, not that it is **accurate**. A stamp
is a claim, not a proof.*

**Canary is mandatory** (`studio-eyes-canary.html`) — white-on-white must HALT, white-on-dark
must pass. Run after ANY change to the sweep. *A gate that stops false-positiving by going
blind is not repaired.*

### CORRECTION ON RECORD
Mid-session I reported **two of the nine EN195 files** (`course-river`, `workshop-wall`) as
having **real warm-mode contrast failures on the founder's eyes.**
**That was wrong — BUG 6 talking.** Both were false positives.
**The nine are genuinely clean and deploy-ready.**

### Confluence: v43 INTACT. Session work must be RE-DONE on v43.
I pushed a v34-based file over v43. The POST-TICK byte-check caught it. **Reverted
(`2622a83`). Canon restored, md5 `bed8c7a3…`, pointer still true. Nothing lost.**

**The findings all transfer — the artifact does not:**
- **Loom → irrigation.** Correct and load-bearing: a loom renders dry cells as "woven,"
  which is a lie. Irrigation renders them **dry**, which is the truth. 145 tokens.
- **The ISLO set was STALE, not just miscounted.** The file carried a **pre-revision
  six-competency set** (Written Comm / Critical Thinking / DEI / Info Literacy / Quant /
  Personal-Social) — **wrong names, not just a wrong count** — including as visible chips in
  the course UI. Current set = **ISLO 1–7**.
- **Vocabulary ruling: "ISLO" is correct and current.** The MassBay *website* still says
  "Graduation Competency" — **the website is the stale artifact**; the committee renamed them
  ~2 years ago. The **count** from the website was right; the **vocabulary** was not.
  *(TICK 2: one source, two claim types, two verdicts.)*
- **Three open questions**, to re-place as inline notes:
  1. **ISLO #5's rubric carries a dimension that reads as ISLO #6.** Spring 2026 norming
     (Walsh, Codrington, McCarthy, Zakuta; 0–4+N/A) scored against the three-dimension
     version. **Do not re-cut the instrument** — that invalidates the record. **Committee rules.**
  2. **Scale collision** — three scales in one file. Fix is labeling at point of use.
  3. **2024/2025 norming gap** — records exist for Spring 2023 and Spring 2026 only.
- **Public/private split (decided):** public = **the instrument** (irrigation map, rubrics,
  training, methodology — no student data, **no gate needed**); private = **the intake**.
  *A client-side password on a static Pages file is NOT security — it ships in View Source.*

**Still unbuilt — and it is the actual product:** the **I-P-A curriculum map** —
Introduced / Practiced / Assessed, courses × outcomes, **dry cells visible**, plus the
faculty-training layer. Score + map + gap-find + train.

---

## NEXT SESSION — IN ORDER

1. **Build `resolve_canon` + wire the gate.** Nothing else until this exists.
2. **Write pointers** for CYL, studio-os, studio-eyes, Leeder.
3. **Re-apply Confluence work to v43**, in its own Claude Project.
4. **Deploy the nine EN195 files** — clean, verified, stale for days.
5. **Build the I-P-A map.** That is the product. *Two build-poor belts in a row means the
   next session is a BUILD session, no new governance.* **This is belt two.**

---

## STANDING

- **ROTATE THE GITHUB PAT.** It appears repeatedly in this transcript and it demonstrated
  today that it can overwrite canonical files.
- **A zero-result search is not evidence of absence.** It lied twice — Drive today
  (`name contains 'onfluence'` → 0 results while two matches sat in the folder), and
  historically `conversation_search` re: "phantom v42." **When a search returns nothing,
  list the container and look.**
- **The mount is a cache, not canon.** It lags. Reading it *feels* like diligence and is the
  most reliable way to do good work on a dead file.
- **When the founder pushes back on a machine-produced fact, the machine is the suspect.**
  Re-derive from source. Do not defend the output. **Every failure this session was caught by
  the founder, by eye. No gate caught any of them.**

---

## FILES

**Pushed + byte-verified** (commit `07f1db9`): `studio-eyes-sweep.py` ·
`studio-eyes-canary.html` · `os-block-truth-ticks.md` · `studio-eyes-repair-2026-07-11.md`

**In outputs, not yet landed:** `SELF-DIAGNOSIS-2026-07-11.md` (the research + the honest
verdict — read it) · this handoff · `confluence-TRUNK.html` (**v34-based — DO NOT USE. Kept
only so the irrigation/ISLO work can be lifted onto v43.**)
