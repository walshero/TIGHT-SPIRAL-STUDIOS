# EXTERNAL ASSESSOR BRIEF — how to read this studio without grading a ghost
*For any outside consultant: an independent model, a human reviewer, an accreditor.
Written 2026-08-08, after the first external assessment (OpenAI lane) proved both
valuable and partly stale — it graded July's studio in August because nothing told
it where truth lives. This brief exists so that never happens again.*

---

## 0. FRESHNESS CHECK — do this before reading anything else

This brief describes HOW to read, not WHAT is currently true. State goes stale;
method doesn't. Verify freshness mechanically, never by trusting a document's
self-description (including this one):

1. **Canon is the repo:** `github.com/walshero/TIGHT-SPIRAL-STUDIOS`, branch `main`.
   Nothing else is canon. Not Google Drive, not a Claude project shelf, not a file
   someone pasted you, not an export with a version-suffixed filename.
2. **Check the last-commit date** on any file before citing it (`git log -1 --
   format=%cd -- <file>`, or the file's History tab on GitHub). A status claim in a
   file untouched for weeks is a claim about the past.
3. **The live site is the repo's GitHub Pages deploy.** A version.json stamp at
   the site root (generated at deploy, not committed) carries the deployed SHA and
   build timestamp — compare it to `main`'s HEAD to know whether live matches canon.
4. **CI is public.** The repo's Actions tab shows every run of "Studio Eyes —
   Accessibility Floor." Deploy is hard-coupled to the gates: a green deploy means
   the belt actually passed, not that someone said it did.

## 1. THE IGNORE LIST — files that will mislead you

The first external assessment cited these; all are stale caches or gone from canon:

- Any file named like "STUDIO-COMMAND-CENTER-v5.3-2026-07-13" (a Drive export;
  canon is `STUDIO-COMMAND-CENTER.md`, unversioned filename, versioned inside).
- "tight-spiral-kernel", "session-tree", "studio-file-map",
  "tight-spiral-production-pipeline", "tight-spiral-visual-constitution" as
  standalone files — superseded or living only under `rescued/` as historical
  record. Their surviving content is in the OS.
- Anything under `rescued/` or `archive/` — preserved history, never current law.
- The repo copy of the Confluence trunk (`confluence-TRUNK.html`) — known-stale
  v43; the newer v48 lives in Drive and is an OPEN reconciliation item, tracked in
  `cross-lane-manifest.md`. Cite the manifest, not either copy.

If a claim matters, cite the file AND its last-commit date. If you cannot reach
something, say so plainly — the studio's own precedent for this is
`CYL_Harvest__Access_Boundary_Findings_and_Re-Run_Instructions.md`, an assessor
refusing to fabricate about chats it could not open. That refusal is the standard.

## 2. READING ORDER — eight files, then stop

1. `STUDIO-COMMAND-CENTER.md` — live state: what's closed, open, owed. The one doc
   that changes every session.
2. `BUILD-DEBT.md` — the ratio rule (governance rate-limited by shipping), the
   session log, and the FAC instrument (founder judgment calls per session,
   logged per line since 2026-08-08).
3. `tight-spiral-studio-os.md` — the law. Long; skim by section headers. §5 holds
   the panel doctrine including "Lenses, not authorities" and the Panelist Union
   Rep; §9 the project roster.
4. `TSP_Ledger.md` — the decision record. Chats defer to it; so should you.
5. `CLAUDE.md` — standing operating preferences, including cost discipline (the
   founder pays out of pocket; this constrains every recommendation you make).
6. `studio-belt.sh` — enforcement, not documentation: 6 blocking ticks, each a
   founder ruling with a gate. Read the header comment; it is kept current.
7. `lane-tendrils.json` — every lane work can strand in, with honest reach
   classes. The lanes no machine can walk are named, not hidden.
8. `cross-lane-manifest.md` — what is canonical where, including the open
   Confluence-trunk gap.

Supporting instruments, read on demand: `canon-freshness.py` (doc claims vs live
reality), `retired-lines-gate.py` + `retired-lines.json` (founder objections as
mechanical checks), `one-thing-gate.py` / `comfort-gate.py` / `preship-gate-v4.py`
/ `studio-voice-gate.py` (the ticks' teeth), `funes-tendrils.py` (loose-end sweep,
prints its own blind spots), `INSTRUCTION-WALL-QUEUE.md` (measured UX debt,
worst-first).

## 3. DELTA SINCE THE JULY SNAPSHOT — so you don't re-litigate the fixed

The first assessment's grades, against current state. Verify each via §0 before
relying on it — this table is itself dated 2026-08-08:

- **Governance enforceability (was C+):** deploy was decoupled from the gates in
  July; re-coupled 2026-08-08 (`floor.yml` — a failing belt now blocks deploy,
  verified live). Two parallel disagreeing CI systems merged to one. "Documented
  governance ≠ enforced governance" was the correct diagnosis; it is also the
  studio's own law ("if a rule can't be a check, it's a wish"), and the week's
  work was converting the remaining wishes: canon-freshness (stale status headers
  caught mechanically), retired-lines (a founder objection that sat unenforced in
  the ledger for three weeks while the objected line kept shipping is now belt
  tick 6, zero tolerance).
- **Canon/state management (was C):** the "three OS versions behind seven
  filenames" problem was reconciled 2026-08-08 — all 13 os-block files merged
  into the OS, collisions found and fixed, headers corrected. Repo-is-canon is
  settled, and the one carrier doc that inverted it was fixed. Still genuinely
  open: the Confluence trunk v43/v48 gap and the lane-count doctrine (three docs,
  three answers; founder has not ruled).
- **Cognitive independence (was C-):** stands, and is now law rather than a
  hope — "Lenses, not authorities" (OS §5) says a simulated panel routes
  attention but cannot disagree independently, with the 2026-08-07 proof cited
  (an inline panel missed a voided premise that five blind parallel agents
  caught). External assessors like you exist to be the disagreement surface.
  Cost constraint applies: cross-model runs are spent from a teacher's pocket.
- **Founder-load reduction (was Unproven):** now instrumented, not proven. FAC
  (Founder Attention Cost) is logged per session line in `BUILD-DEBT.md` as of
  2026-08-08. Judge the trend once there is one.
- **Policy entropy / pruning (their §5):** stands, partially. Real pruning
  happened (a whole CI workflow deleted; two auditors retired from CI), and the
  Union Rep's grievance log now gives the panel layer a pruning signal that
  fires on evidence. But rule-generation still outpaces burial; no
  governance-attic interment has actually occurred yet. Keep testing this.
- **FERPA incident (their §6):** the July command center's FERPA-LIVE item
  predates this brief's window; what is verifiable today is the control that
  answers it — `matt-eyes-lane-check.py` runs first in CI, blocking, fail-fast
  ("no private material on the public street"). Incident → control is the
  pattern; test whether it holds, not whether the incident happened.

## 4. WHAT THE STUDIO WANTS FROM YOU

1. **Independence, not agreement.** You are valuable where you disagree with the
   resident model and can show why. A finding both models reach independently is
   worth more than either alone; a finding only you reach is the reason you were
   hired.
2. **Test enforcement, not documentation.** For any rule you evaluate, find its
   check (a gate, a tick, a baseline, a CI step). No check = a wish; say so. The
   Actions tab and the gates' own self-tests (`--selftest` flags) are public.
3. **Cite or decline.** File + date for every claim; an explicit "cannot reach"
   for everything else. Confident fabrication about unreachable lanes is the one
   unforgivable assessor failure here.
4. **Respect the founder gate.** Voice, pedagogy content, lane doctrine, and
   anything listed under "OPEN — FOUNDER ONLY" in the command center are his
   calls. Recommend; never assert his answer.
5. **Weigh cost.** Every recommendation that costs tokens, subscriptions, or
   founder hours competes with a teacher's out-of-pocket budget. "More process"
   loses to "same assurance, cheaper" every time — see the ratio rule.

*This brief is registered with `canon-freshness.py` (pointer checks run in CI).
If you are reading a copy of it outside the repo, you are already violating §0 —
go get the canonical one.*
