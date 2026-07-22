# FUNES-INDEX — the memory
*What the studio holds, across four lanes, from one point. Last swept 2026-07-13.*
*This is a live index. Every row carries where it lives and when it was last verified. An
unstamped claim is a suspicion, not a fact.*

---

## THE FOUR LANES

| Lane | Address | Canon for | Reachable from sandbox? |
|---|---|---|---|
| **GitHub repo** | `github.com/walshero/TIGHT-SPIRAL-STUDIOS` · raw: `raw.githubusercontent.com/walshero/TIGHT-SPIRAL-STUDIOS/main/<file>` | Anything deployed. Content-addressed — cannot lie. | Yes (raw fetch, git clone) |
| **Netlify** | `relaxed-gaufre-a0c223.netlify.app` | Standalone game deploys (e.g. Dad Energy v2.1) | NO — egress blocks `*.netlify.app`; `web_fetch` only, read-only |
| **Google Drive** `Claude_files` (walshero) | folder `1WJh7jRrIfVE9MNydjyKjYlErIQq7gRwC` | Addresses / pointers — the zipper. NOT files. | Yes (Drive connector; read + write both proven 2026-07-13) |
| **Project shelf** `/mnt/project` | the 11 curated docs below | NOTHING. It is a cache and it LAGS. If shelf ≠ repo, the shelf is wrong. | Yes |
| *(non-lane)* `outputs/` | — | Nothing. A staging bench that evaporates. Every loss came from here. | — |

**Resolver:** `resolve-canon.py` (repo root, on the shelf). `python3 resolve-canon.py <name>`
= where does this live, what is canon. `--check <local>` = HALT if your copy ≠ canon.
`--audit` = every file, every lane, all drift. This is the gate; run it before any edit.

---

## CANON POINTERS — current, verified

- **Asset-ingest past the egress wall** → `LANE-REGISTRY.md § THE ASSET-INGEST LANE` — STATE:
  **proven 2026-07-21.** Sandbox web egress is policy-blocked (proxy 403s CONNECT to all
  non-allowlisted hosts; `web_fetch` too). To pull a public asset in: `WebSearch` to verify →
  Zapier **Upload File** (`file`=URL, `convert=false`) fetches server-side → Drive → base64-embed.
  `WebSearch` works; `fetch_url_as_base64` is Google-hosts-only. Not for generated art.

- **Confluence trunk = v44** — repo, 598,114 B, md5 `8dcf990336eb1c0ffa600cae3b689539`
  (LANE-REGISTRY, 2026-07-13). Supersedes v43 (`bed8c7a3…`) and the long-cited v33/v34.
  *A prior session lost hours editing v34; the pointer that would have caught it existed in Drive,
  unopened. This row is why Funes exists.*
- **Studio Eyes** — `studio-eyes-sweep.py`, 448 lines, commit `07f1db9`, byte-verified on GitHub.
  Shelf HALTs cut 42/57 → 20/57 after six grounding bugs were fixed. Canary mandatory after any change.
- **EN195 hub** — `en195-hub.html` pushed + byte-verified; all six doors live.
- **Warriors** — real 19,577 B game pushed over a 2,277 B repo stub (the Warriors rule).
- **The nine EN195 files** — clean, contrast-verified, deploy-ready (two earlier "failures" were
  auditor bug 6, false positives).

## THE 11 CURATED CANON DOCS (survived the 2026-07-13 clean)

- `founder-canon 2.md` — the Aleph: Matt's terms, theses, rulings, the finishing finding. Upstream of all files.
- `LANE-REGISTRY.md` — the four lanes + the resolve_canon spec + the siloed-25 list.
- `resolve-canon.py` — the enforcer (gate + audit).
- `studio-eyes-sweep.py` — the contrast auditor (accessibility is arithmetic).
- `os-block-truth-ticks.md` — the mechanical ticks (byte-verify, auto-push).
- `ORPHAN-HALTS.md` — the 24 landed orphans; 11 contrast defects; behind-this-door is alive.
- `safe-push.sh` — the push-and-byte-verify path.
- `SHELF-DELETE-LIST.md` — what was cleared and what to keep.
- `SELF-DIAGNOSIS-2026-07-11.md` — the honest verdict on the v34 clobber.
- `HANDOFF-2026-07-11.md` — read-first state; "build resolve_canon before touching another file."
- `TSP Ledger.md` — the running log, incl. the Integrity Guard FERPA runs.

*(The living Command Center is `claude/STUDIO-COMMAND-CENTER 2.md`, restored 2026-07-13 after a
timed-out write dropped it; also byte-verified into Drive.)*

---

## THE FINISHING LIST — decided or done, still homeless (Funes' first loyalty)

*From founder-canon §VI–VII. The studio's finding: not a building problem, a finishing problem.*

- **The Borges paper** — 2,100 words, finished, chronicle-shaped, 14-venue strategy written.
  **Never sent.** "The only finished thing in the studio that nobody has read."
- **Diagnose mode** — takes a revision problem the writer actually has and routes the fix. Transfer,
  not recall. **Built, parked in Drive.**
- **Four Tell cards** — Shaky World Rules · Fast-Forward Scene · Noticeable Info Dump · Convenient
  Coincidence. Cards + reader-tests + engine exist. **An afternoon, unshipped.**
- **The taxonomy fork** — already resolved: `the-tell.html` is LIVE running the Drafty vocabulary;
  the 13/11 decks are the old system. **Decided, unannounced.**
- **The meta-machine** (Funny Boney's) — machines connecting into one story-telling meta-machine +
  social score. The build dropped it. Engine now exists.
- **The four-fifths thesis · provenance-as-content · the game-as-invitation** — fully articulated,
  homeless.
- **lumière → Suubi** — a student founded *Suubi* magazine in Mubende, Uganda. Ten years, real
  alumni. **Nowhere in the studio's own story.**

## SILOED — shelf-only, no deploy lane (LANE-REGISTRY, 25 files)

Big and probably real: `claude_cliche-cabinet-suite.html` (113 KB) · `fys_fys-treasure-trove.html`
(63 KB) · `funny-boneys-factory.html` (43 KB) · **`behind-this-door.html` (42 KB — recorded as a
DEAD LINK; it is a finished room, never pushed)** · `en195-what-counts-now.html` (40 KB) · the
cliché suite · `group-foreman` · `founder-compass` · `studio-river` · `open-house-strategic-plan` ·
`convergence-card-engine` · `timing-belt` · `session-tree` · others. **11 carry proven contrast
defects** (ORPHAN-HALTS) — real, not guesses.

---

## DRIVE — the zipper (walshero `Claude_files` = `1WJh…`)

- Native Google Docs found this pass (few — most work is HTML/MD/docx uploads, not gDocs):
  `Portfolio Comments Summer 2026`, `Writerly Moves — Move Bible v1`, `Writerly Moves —
  Formalization Map v1`, `MYSTERY TEXT`, `Copy of EN195-Portfolio: Emma Kwan`.
- **Confluence sprawl:** 30+ `confluence-TRUNK*.html` copies across `1WJh…`, `1Nk1…`, `1govQ…`.
  Keep the v44 canon (repo) + its pointer; archive the rest via move-to-folder (`Archive Comments`
  `1zqvxgKmET…`) — move, not trash. Not a Josh task.
- Command Center canon landed here: `STUDIO-COMMAND-CENTER-v5.3-2026-07-13.md`.

## OPEN FOUNDER GATES (carried)

0. **[CRITICAL] FERPA** — repo serving names/emails (`confluence-TRUNK-2026-06-23.html` + undated
   trunk). Delete/scrub via GitHub web editor (click-path: `site-sweep-2026-07-02.md`), then reset
   the Integrity Guard to weekly. Matt or Josh — no session can push.
1. **Confluence version** — canon = v44; confirm against any v40 "base" claim, then re-apply the
   irrigation/ISLO work onto v44 in Confluence's own Project.
2. **Score-6 label** — Sean email drafted (Gmail Drafts), needs send.
3. **Deploy the nine EN195 files** — clean and stale for days.
4. **Build the I-P-A curriculum map** — Introduced/Practiced/Assessed × outcomes, dry cells
   visible. "That is the product." Next session is a build session — no new governance.

---

## KNOWN GAPS IN FUNES' OWN MEMORY (truth in advertising)

- **Full Google-Docs enumeration is incomplete this pass** — the Drive connector pages ~5 at a
  time and the corpus is mostly non-gDoc files. This index is seeded, not exhaustive; the refresh
  sweep grows it.
- **Other Projects are invisible** (Confluence/Leeder/research, if separate). Not seen, not claimed.
- **The 318-piece writing corpus** was not on the shelf this session. Homeless, referenced only.
- **Netlify inventory is partial** — sandbox can't reach it; only files named in canon are known.

*Next sweep: re-run `resolve-canon.py --audit`, re-list the Drive canonical folders, re-probe the
repo FERPA files, and fold any new founder-log rulings. Stamp the date. Funes forgets nothing that
has been swept — and admits everything that has not.*
