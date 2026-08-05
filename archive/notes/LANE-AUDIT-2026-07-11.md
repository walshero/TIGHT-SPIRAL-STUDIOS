# LANE AUDIT — what the machine can reach, and what it cannot
*2026-07-11 · Tight Spiral Productions · run on founder request*

**The question:** where can Claude actually look, where is it blind, and what workflow
makes work lossless given both?

---

## PART 1 — WHAT I CAN REACH (verified this session, not assumed)

| Lane | Access | Method | Notes |
|---|---|---|---|
| **GitHub repo** | **FULL — read + write, any size** | container `git clone` with PAT | The only lane with **no size limit.** Moved 598KB byte-exact. Authoritative. |
| **Drive — walshero** | **FULL — read + write** | Zapier `GoogleDriveCLIAPI` | Write is a **tool parameter** → hard ceiling ~30–50KB. Read has no such limit. |
| **Drive — post-owned files inside walshero folders** | **READABLE** ✓ | same | **Tested and confirmed.** Your sharing works. Post-owned files in `Confluence/` and `Leeder/` read fine. |
| **Project shelf** (`/mnt/project`) | **READ ONLY** | filesystem | A **cache. It lags.** Never canon. |
| **Chat uploads** | **FULL** | filesystem | Anything you attach. |
| **Container** (`/home/claude`) | **FULL** | filesystem | **Resets between sessions.** Nothing survives here. |
| **Past chats** | **SEARCHABLE** | `conversation_search` | A miss is **not** proof of absence. |

**Net: I can read essentially everything you have.** The blindness is not about permission.

---

## PART 2 — WHERE I AM BLIND (the honest list)

### 1. YOUR PHONE AND MAC — total blindness
I cannot see local files. Not Downloads, not Files.app, not iCloud, not the Desktop.
**If a file exists only on a device, it is one lost device away from gone.**
→ *Fix:* attach it to a chat, or Drive-save it. There is no third way.

### 2. GOOGLE-NATIVE DOCS — partial
`.docx` / `.xlsx` / `.pptx` read as **base64 only** — decodable but expensive, and each
one burns a turn. Google Docs need `export_gdoc_as_text`, a different action.
→ *Consequence:* the **Writerly Moves master canon** (`.docx`) is readable but slow.
Word/Excel are the worst format to hold canon in.

### 3. THE DRIVE WRITE CEILING — the one that actually cost you
The Zapier Drive write takes **file content as a tool parameter** (~30–50KB).
**598KB will never fit.** This single fact — unnoticed — froze the Confluence trunk at
v33 while **ten versions** shipped elsewhere. It was never neglect. **The lane was never
wide enough.**
→ *Fix, already law:* files **>50KB → canon in the REPO**, pointer in Drive.

### 4. ZIP ARCHIVES — unopened
`File_008` (11.5MB), `Matt's Claude Builds…zip` (15.7MB), `Matt's Writing…zip` (11.8MB),
`confluence-project-export.zip`, `File_003`, `File_077`, `leeder-redesign.zip`.
**I have not opened any of them.** They may contain originals that exist nowhere else,
or they may be pure backup. **Unknown is not the same as safe.**

### 5. IMAGES — no OCR pass
`en195_arcade_bb_banner.png` (1.8MB), `..._square_tile.png` (3MB), a `Screenshots`
folder. I can *see* images if you attach them; I have not swept them.

---

## PART 3 — THE ACTUAL PROBLEM (it isn't access)

### ⚠ YOU HAVE AT LEAST THREE PARALLEL COPIES OF YOUR ENTIRE KNOWLEDGE TREE

```
Claude_files/
├── _MW KNOWLEDGE BASE_/          ← tree A
│     ├── Confluence — Build Versions/
│     ├── Matt_s Claude Builds/
│     ├── Matt_s Writing/
│     └── Writerly Moves Card Deck/
│
├── Matt_s Claude Builds/         ← tree B  (DIFFERENT folder IDs)
│     ├── Confluence — Build Versions/
│     ├── Confluence — Chat Logs/
│     └── Writerly Moves Card Deck/
│
└── (root)                        ← tree C — ~230 loose files
```

Same names. **Different folder IDs. Different contents.** Nested, recursive, and
unresolvable by name alone.

**This — not permission — is why work gets lost.** Not because I can't see it, but
because *nothing declares which copy is real.*

### The duplicate census (root folder alone)
- **Confluence trunk: 19 copies** — v33, `(1)`–`(10)`, `v9fork DONOTSHIP`, `v10`–`v13 SHIP`. ~6 MB of the same file.
- **Studio OS: 8 copies** — 86KB to 165KB. **They differ.** Name tells you nothing.
- **Choose Your Leader: 9 copies** — 67,049 / 67,128 / 47,769 B under near-identical names.
- **studio-eyes-sweep.py: 5 copies** · **review-panel: 3** · **pipeline: 2 (different sizes)**

**290 MB of GitHub Desktop installer** is also sitting in your knowledge folder.

---

## PART 4 — THE LOSSLESS WORKFLOW

The primitive that solves this is one you already have (**OS §12**): **canon is an
ADDRESS, not a copy.** Applied to the lanes:

### THE FOUR-LANE LAW

| What | Where canon lives | Why |
|---|---|---|
| **Any file >50KB** | **REPO** (git). Drive gets a **pointer**. | Git has no size limit. Drive's write bus does. |
| **Any file <50KB** | **REPO** (git). Drive optional mirror. | Git versions it. Drive doesn't. |
| **Binary source** (docx/xlsx/png) | **DRIVE** — it's the only lane that holds it well | But **never** hold canon *text* in a `.docx`. |
| **Live state** (what's in flight) | **Command Center** (Drive) | The one doc that changes every session. |

**Nothing is canon in two places. Ever.** One writes; the rest point.

### THE THREE RULES THAT MAKE IT HOLD

1. **NOTHING SURVIVES A CHAT UNLESS IT'S PUSHED.** Same turn it's made. Byte-verified.
   `outputs/` is a bench — it evaporates. *"success: true" is never proof.*

2. **RUN `resolve-canon.py` BEFORE EDITING ANY NAMED FILE.** It hashes every lane and
   **HALTs on divergence.** This is the tool that ends the "which copy is real" question
   permanently — it does not ask you to remember, it computes.

3. **ONE OWNER PER FILE.** The manifest declares RW/RO. TSP does not write Confluence.
   Two sessions editing one file is **structural, not careless** — it happened twice today.

---

## PART 5 — WHAT I NEED FROM YOU (only you can do these)

| # | Action | Why only you |
|---|---|---|
| **1** | **Paste the coherence block into all four Projects' instructions** | It is the only carrier that fires *before* a session's first word. Everything else is downstream. |
| **2** | **Decide which knowledge tree is real** — `_MW KNOWLEDGE BASE_`, `Matt_s Claude Builds`, or root | Three parallel trees with the same names. I can diff them; I cannot choose. |
| **3** | **Say whether the zips are backups or originals** | 40MB unopened. If backups → I ignore them. If originals → I open them now. |
| **4** | **Move `GitHubDesktop-arm64.zip` (290MB) out** | It's an installer in a knowledge folder. |

---

## PART 6 — WHAT I'D DO NEXT, IN ORDER

1. **Open the zips** (once you say they're not just backups) — highest chance of a file
   that exists nowhere else.
2. **Diff the 8 Studio OS copies** — they differ, and one is canon. Name it; kill seven.
3. **Kill the 19 Confluence trunk copies** — canon is v44 in the repo. Every Drive copy
   is a fossil. (~6 MB freed, and the "which trunk?" question dies.)
4. **Land the Writerly Moves originals** byte-exact (8 files, IDs in
   `writerly-moves/PENDING-LANDING.md`).

---

## THE ONE-LINE ANSWER

**I am not blind. Your archive is ambiguous.**

I can reach everything — repo, Drive, post-owned files, past chats. What I cannot do is
**tell which of three identically-named trees is the real one**, and no amount of access
fixes that.

**A lossless workflow is not more storage. It is fewer copies and one address for each.**
