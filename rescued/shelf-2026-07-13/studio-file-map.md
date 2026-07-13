# Tight Spiral Productions — Studio File Map & Save Architecture

*Built 2026-07-05 from live tool probes, not memory. Every capability below was tested this session — where it says "verified," a tool call proved it. Where it says "unverified," it has NOT been tested and should not be trusted yet. This document exists because the studio's save lanes had drifted from what memory claimed, and guessing was costing real time.*

*Amended 2026-07-11: canonical `Claude_files` folder resolved (§2B). NEEDS PHONE-CANONIZATION.*

---

## 0. The core problem this map fixes

Memory carried assumptions that live probes proved wrong:

- **Memory said** one `Claude_files` folder (ID `1WJh7jRrIfVE9MNydjyKjYlErIQq7gRwC`).
  **Drive actually has THREE** folders named `Claude_files`, owned by two accounts. That ambiguity is why saves felt like guesswork.
- **Memory said** v34 was the current Confluence trunk (528,886 bytes).
  **Drive's newest is v33** (`confluence-TRUNK.html`, 522,533 bytes). v34 is not in Drive — it exists only in a chat's outputs, or never saved.
- **Memory said** "native Drive write is down."
  **Native Drive READ is fully working** (deep, folder-aware, real IDs). Write was not tested this session — status genuinely unknown, don't assume either way.

**The rule going forward: probe before trust.** This map is only as good as its last verification date. Re-verify the lanes when a save fails, don't re-guess.

---

## 1. Verified tool capabilities (tested this session)

| Lane | Capability | Status | Evidence |
|---|---|---|---|
| **Native Google Drive** | READ / search / list folders | VERIFIED working | Pulled full Confluence history w/ IDs |
| **Native Google Drive** | WRITE (create/replace) | UNVERIFIED | Not tested this session |
| **Zapier → Google Drive** | READ inside named folders | VERIFIED working | Listed "Tight Spiral Studios" contents |
| **Zapier → Google Drive** | Upload File (from URL) | EXISTS, untested | Action present on account |
| **Zapier → Google Drive** | Replace File (in place) | EXISTS, untested | Action present — kills "Drive can't replace" myth |
| **Zapier → GitHub** | 21 actions live | EXISTS, untested | Connector enabled |
| **iPhone Shortcut** | Save file to Project shelf | Known-good (prior) | Historically the phone lane to the shelf |
| **Claude Project shelf** | Auto-loads into every chat | Working | Files visible in context |
| **Claude `project_write`** | Write direct to the Project shelf | VERIFIED working 2026-07-11 | Charter, guard, live-map, this file all written directly — no phone hop |

**The single most important finding:** the connector addresses Drive by **named folder**, not by folder-ID. It sees: *Shared with Me, Tight Spiral Studios, MW KNOWLEDGE BASE, Creative Writing Club, HOME/FAMILY, BHCC External Eval, LUMIERE everything, MASSBAY: COURSE DOCS, Matt's Projects.* Save targets should be named folders from that list.

---

## 2. The three save destinations (and what each is FOR)

The studio has three places a file can live. They are not interchangeable. Confusing them is the drift.

### A. Claude Project shelf — CANON
- **What it is:** the files that auto-load into every chat in this Project.
- **What lives here:** the OS, the Constitution, patterns, pipeline, active specs, active game files.
- **How a file gets here:** **`project_write` (Claude, direct — verified 2026-07-11)** OR the iPhone Shortcut. The old "iPhone Shortcut only" rule is retired: Claude can now canonize to the shelf directly. Phone-save remains the lane for files Matt edits on his phone.
- **Truth status:** THIS is canon. If it's not on the shelf, I can't read it next session.

### B. Google Drive — ARCHIVE + WORKING STORE
- **What it is:** your real Drive, where the trunk versions, chat logs, and knowledge base live.
- **Verified structure (real folders, real IDs):**
  - `MW Knowledge Base` — `1HgCt7LgM88cexg90tjVh0844eYfo0oOq` (parent of Confluence work)
  - `Confluence — Build Versions` — `1ylU3uDeC16UZtYo-mqeSGyXFHyGEkztM` (all trunk .html versions)
  - `Confluence — Chat Logs` — `1BkV0yYmJSSJfibyyJz03WIqPqPHHTSFb`
  - `Tight Spiral Studios` — `1_dFyRQxdHs_Cb7PiqZCIh3Arb3L0owrc` (owner: mwalsh@post)
  - `MassBay Course Docs` — `1YY997nYBGFxwBHU782D_qajO2e76uauB`
  - `Creative Writing Club` — `1k76RjBSS2i1Sqd7g3sC1L_Oi55ClE2X6`
- **THE Claude_files CANONICAL PICK — RESOLVED 2026-07-11 (Matt's call: walshero):**
  - **CANONICAL → `1WJh7jRrIfVE9MNydjyKjYlErIQq7gRwC`** — walshero@gmail, shared-with-me, created 2026-07-01. Chosen: newest, and the folder memory already used (least disruption).
  - ARCHIVE → `1f85Siq2AXHXvpUZc33MpjOKToehhKoec` — walshero, created 2026-06-25.
  - ARCHIVE → `1A32a09_G3XSHECqpg1DxJWrmAZAyH1G8` — walshero, created 2026-06-25.
  - **Note:** all three are walshero-owned (the "post-owned" one was a memory error). If Matt meant a directly-owned rather than shared-in folder, swap canonical to `1f85...`.
  - **Execution:** archiving the two non-canonical folders is queued for the **Studio Archive Zap** — Drive write is still untested, so the move waits on that automation being built/tested. The decision itself is now canon.
- **How a file gets here:** native Drive create (untested), OR Zapier Upload/Replace (untested but present), OR manual.
- **Truth status:** archive and backup. Reachable by tools for READ. NOT the Project shelf.

### C. GitHub Pages — PUBLIC LIVE WEB
- **What it is:** `walshero.github.io/TIGHT-SPIRAL-STUDIOS/` — the public arcade.
- **What lives here:** only files meant for the public web (index, published games). Verified live 2026-07-11 — see `studio-live-links-2026-07-11.md`.
- **How a file gets here:** Zapier GitHub lane (present, one-time browser auth pending per memory).
- **Truth status:** public. Never put student data or institutional drafts here.

---

## 3. How a file SHOULD flow (the canonical path)

```
        BUILT IN CHAT (outputs/scratch)
                 │
      ┌──────────┼───────────────┐
      │          │               │
   [project_    [native Drive    [Zapier GitHub
   write /       or Zapier]       lane]
   phone]        │               │
      │          ▼               ▼
      ▼       DRIVE           GITHUB PAGES
  PROJECT     ARCHIVE         PUBLIC WEB
  SHELF       (backup)        (published games only)
  (canon)
```

**Rules that keep it clean:**
1. **Canonical filename, no dates in living names.** `sandbags-joy.html`, not `sandbags-2026-07-05.html`. Dates belong in changelogs inside the file, not in filenames.
2. **Replace, don't add.** New version overwrites the canonical name. Old copies get deleted, not accumulated.
3. **Two-lane ship:** durable builds land on the **shelf** AND in **Drive** (archive). Public games also go to **GitHub**.
4. **Verify every save.** "created:true" is never proof. Byte-count and content-head check after every save.
5. **FERPA floor:** student names/data never leave to GitHub, never persist in archive. Strip before save.

---

## 4. What to Zap NOW (clear, low-risk automation)

### CLEAR TO BUILD — Drive archive automation
- **Zapier "Replace File"** pointed at a canonical Drive file, triggered on demand. Low risk: it replaces one known file by ID. Reversible (Drive keeps version history).
- **Voice-first payoff:** "Hey Siri, run Confluence archive" → Shortcut → Zap → Drive updated. No menu hunting.

### CLEAR TO BUILD — Duplicate cleanup list (delegate to automation, not Josh)
- Drive has ~9 Confluence duplicates and the two non-canonical Claude_files folders. Route to the Studio Archive Zap (Ruling 10: not a Josh task).

### TEST FIRST — GitHub deploy Zap
- The 21 GitHub actions are live but the deploy lane has an untested one-time auth. Test with ONE small file before trusting it for real deploys.

### DON'T ZAP — the trunk phone-save
- v34/v33-class files (>500K) go by **Shortcut** or `project_write`. The Zap can archive to Drive; it cannot replace a hand-edited phone copy.

---

## 5. The recurring failure this map ends

Every "which lane / can Zap do it / is it saved" spiral traces to one missing thing: **a verified map that says where files live and how they move.** That's this document. When a save question comes up: check §2 for the destination, §1 for whether the lane works, §4 for whether to automate. Don't re-derive it live.

**Re-verify trigger:** any time a save fails, or monthly, re-run the §1 probes and update the dates. Portability rule: this map is plain Markdown, survives any tool change.

---

## 6. Immediate next actions (from this map)

1. **Resolve v33-vs-v34** — confirm which is the real current trunk; if v34 exists only in a chat, get it to Drive and the shelf. (Still open — founder gate.)
2. **Claude_files canonical — DONE 2026-07-11:** walshero `1WJh...` is canonical; archive `1f85...` and `1A32...` via the Studio Archive Zap (execution queued behind untested Drive write).
3. **Build the Replace-File Drive Zap** (the one clear automation).
4. **Delegate the Drive duplicate cleanup** to the Studio Archive Zap with an explicit ID list (not Josh).

*End of map. Verified 2026-07-05, amended 2026-07-11. Re-verify on any save failure.*
