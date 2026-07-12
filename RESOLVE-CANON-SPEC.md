# RESOLVE_CANON — BUILD SPEC
**The one automation. Build this before anything else.**
**2026-07-11. Written after a session spent editing a nine-version-stale file.**

---

## WHAT IT IS

**One Zapier code action.** Given a filename, it answers: *which copy is real, where does it
live, and does the copy in my hand match?*

It is a **lookup, not an inference.** Nothing about it is clever. That is the point.

## WHY IT IS THE ONE THING

On 2026-07-11 six studio rules should have caught a nine-version version drift. **One did** —
the byte-check, because it is **arithmetic, not memory.** Every rule that required *remembering*
failed: the pointer file (never opened), the fork-diff rule, the source-first lock, OS §12.

The studio wrote the diagnosis itself on **2026-06-29**, twelve days earlier, and never acted:

> **"Rich in rules, thin in enforcers. A written floor without an enforcer fails."**

**`resolve_canon` is the enforcer.** It is not a rule. It is a refusal.

---

## THE FOUR LANES (it must know all of them)

| Lane | How to read it | Authority |
|---|---|---|
| **GitHub repo** `walshero/TIGHT-SPIRAL-STUDIOS` | `git clone` + md5, or raw.githubusercontent.com | **CANON for anything deployed. Content-addressed — cannot lie.** |
| **Netlify** `relaxed-gaufre-a0c223.netlify.app` | HTTP GET. **Container egress BLOCKS `*.netlify.app`** — must be allowlisted, or resolved via `web_fetch` | Canon for what lives only here (Dad Energy v2.1) |
| **Google Drive** `Claude_files` (walshero) | Zapier `list_all_drive_files` | Canon for **addresses**, not files |
| **Project shelf** `/mnt/project` | direct read | **NEVER canon. It is a cache and it lags.** |

**`outputs/` is not a lane.** It is a staging bench that evaporates. Every loss this studio has
suffered came from a file that stopped there.

---

## SIGNATURE

```
resolve_canon(name) →
  {
    found_in:    ["repo", "shelf"],        // every lane where a copy exists
    canon_lane:  "repo",
    address:     "raw.githubusercontent.com/walshero/TIGHT-SPIRAL-STUDIOS/main/<name>",
    bytes:       598114,
    md5:         "8dcf990336eb1c0ffa600cae3b689539",
    fossils:     ["shelf: 528886 B (v34) — STALE"],
    single_lane: false,                    // true = NO BACKUP, warn loudly
    verdict:     "OK" | "STALE_COPY" | "SINGLE_LANE" | "NOT_FOUND"
  }
```

## PRECEDENCE (when lanes disagree)

1. **repo** wins. It is content-addressed; it cannot lie about what it contains.
2. **netlify** wins only if the file exists *nowhere else* (then flag `single_lane`).
3. **drive** never holds files, only addresses. Treat a Drive pointer as a **cache to verify,
   never an oracle to trust** — `confluence-TRUNK-POINTER.md` went stale in under 24 hours.
4. **shelf** never wins. Ever. If the shelf differs from the repo, **the shelf is wrong** —
   *unless* the file is shelf-only, in which case it is an **orphan and must be pushed.**

**Exception, learned the hard way:** if the shelf copy is *larger and has more code* than the
repo copy, **STOP and diff.** The repo held a 2,277 B empty stub of `warriors-fantasy-arcade.html`
while the shelf held the real 19,577 B game. **Never auto-default to the smaller or newer file.**

---

## THE GATE (this is the part that matters)

> **No file may be edited until `resolve_canon` has returned for it in the current session,
> across ALL FOUR LANES, and the working copy's md5 matches canon.**
>
> - **hash mismatch → HALT.** You are holding a fossil.
> - **`NOT_FOUND` → HALT** until all four lanes are confirmed checked. *"Not in three lanes"*
>   is not *"does not exist"* — that is exactly how a finished game (Dad Energy) got declared lost.
> - **`SINGLE_LANE` → WARN LOUDLY.** One account change and it is gone.

A HALT here carries the **same force as a failed contrast check**. It is not advisory.

---

## IMPLEMENTATION NOTES (real constraints, learned 2026-07-11)

- **Drive queries lie.** `name contains 'onfluence'` returned **ZERO** while two matching files
  sat in the folder. **Do not trust filtered Drive queries. List the folder (scoped by folder ID
  — unscoped overflows the payload) and filter locally.**
- **Netlify is unreachable from the container.** Egress blocks `*.netlify.app`. Either allowlist
  the host or resolve that lane through `web_fetch` and treat it read-only.
- **Version banners lie.** Confluence v44's in-file banner still reads "v43" — the commit changed
  content without bumping the banner. **The md5 is authoritative. The banner is decoration.**
- **A zero-result search is not evidence of absence.** It lied twice in one session (Drive files,
  Dad Energy). **When a search comes back empty, list the container and look.**

---

## COMPANION: AUTO-PUSH AT CREATION (TICK 5)

`resolve_canon` stops you **editing** the wrong file. This stops you **losing** the right one.

> **Every file lands in a real lane in the same turn it is created, byte-verified.**
> Small → Drive bus. Large → git-push (no size limit, proven). Standalone game → Netlify.
> **Un-pushable → flagged LOUDLY as un-backed-up, never silently.**

The shape of every loss this studio has suffered:

> **built → landed in `outputs` → never pushed → chat closed → gone**

The Gatekeeper charter already says *"Outputs is a staging bench, nothing lives there."*
**Written. Never enforced.** That sentence is the studio's disease in eight words.

---

## WHAT NOT TO BUILD

- **No new belt beat, tick, or rule.** There are ~30 already. If a rule cannot be a check,
  it is a wish.
- **No agent framework.** An autonomous agent would have read the stale shelf, applied 145 edits,
  pushed, clobbered v43, and reported success — *every step would have "succeeded."* The failure
  was **judgment about which file was real.** That is what agents are worst at, and adding
  autonomy to an unresolved-canon problem multiplies the blast radius.
- **No nightly lane-reconciler — YET.** Good idea, wrong time. Do not add a second scheduled
  agent until the Integrity Guard is fixed, or two bots will push noise to the founder's phone
  and he will stop reading both.

---

## OPEN ITEM — THE INTEGRITY GUARD

Scheduled task `trig_01FQqXXXHr5mFBUt1JGWK3n4` ("Studio Integrity Guard — weekly sweep") has
cron `0 * * * *` — **hourly, not weekly.** It has fired six times and returned
`PROVENANCE_REQUIRED` / **BLOCKED** every time. It has **never once completed a check**, because
it cannot fetch `walshero.github.io` (host not authorized for WebFetch).

**It is not a guard that fires too often. It is a guard that has never worked, alarming hourly
about its own inability to work.**

**RECOMMENDATION: DELETE IT.** Fixing the cron makes it fail weekly instead of hourly — a
quieter broken thing, not a fix. **Rebuild it as a GitHub Action**, which runs *inside* the repo,
needs no WebFetch authorization, and can actually read the files. `floor.yml` is the pattern.

**An alarm that fires constantly and says nothing new teaches you to ignore alarms.** That is the
same failure that made the founder distrust Studio Eyes for six days. Do not let a guard become
the thing it guards against.
