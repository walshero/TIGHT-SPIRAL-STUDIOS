# TSP Ledger
*Single decision log for all Tight Spiral Studios projects. Append via KD! at session close. This file is truth; chats are archive.*

---

## 2026-07-03 — Strategic decisions (logged, binding)

**DECIDED — Open by default.** Backstage assets go public on the studio face. Hub and face become ONE site. No more design friction invented for IP security. Build in stealth with trusted parties; lock down later if ever needed.

**DECIDED — Timing belt protocol.** Before any synced execution run engages, all hub PMs (panel seats / project leads) get briefed so the right gears engage and disengage. Belt is NOT yet engaged — briefing (Aleph session) comes first.

**DECIDED — Aleph session.** Full-panel 360° review of TSP pipeline + operating system. Scheduled as the next project-side panel session, before v32 build.

**DECIDED — This ledger exists.** One portable markdown file, all TSP projects, KD! appends at session close. Mirrors the Confluence Source/Tributaries pattern.

**DECIDED — v32 = nodes-and-arrows.** ESL norming scaffold slots to v33. (Called 2026-07-02.)

**VERIFIED — True v31 located.** Uploaded trunk = 513,436 bytes, md5 a18283bc — exact match to canonical record. The 522,533-byte "confluence-TRUNK.html" in Drive is NOT v31; treat as suspect until project-side Steward audit.

**SHIPPED — TSP Village landing page** (tsp-village.html). Five buildings: Assessment Hall, Craft Arcade, Card House, EN195 Game Hub (in build), Lumière office. Links need URLs pasted into SITES block. Not yet deployed to GitHub Pages.

---

## Asset inventory (from Aleph sweep #1, chats June 19 – July 3)

| Asset | Status | Where |
|---|---|---|
| Confluence trunk v31 | Canonical, verified | Project knowledge + this chat's upload |
| TSP Village landing | Built, undeployed | Claude outputs (tsp-village.html) |
| Writerly Moves Craft Arcade v2 | Shipped | 33 KB HTML, in hand |
| Writerly Moves Card Game | Shipped | 19.8 MB HTML, in hand |
| WhisperGreen Gone Wrong | Shipped, UNTRACKED until now | Drive (TSP-branded micro-game, July 2) |
| Kintsugi instructional-design brief | Written, loose | Markdown, June 30 chat — Studio OS philosophy doc |
| BHCC Convergence SWOT | Delivered May 2025 | Archive |

---

## Loose ends (found by sweep, need a call or a close)

1. **EN195 Game Hub — deadline passed.** Course ended July 2. The async peer-workshop tool for Workshop Four was gated on the Writerly Moves file transfer and never shipped. Status change needed: post-mortem the proof-of-concept term OR re-scope for next term. Not a failure of the concept — the instrumentation goal was never resourced. Decide at Aleph.
2. **Kintsugi brief is homeless.** It belongs in the Studio OS corpus (visible-repair = TSP design principle, connects to SNAP/Pivot). One action: file it.
3. **Two dead stubs:** "President game" and "corpus builder" threads opened, never scoped. Recommend: eliminate both unless one resurfaces on its own.
4. **FLC trauma-informed handbook** — still gated on Matt's notebook photo + sources.
5. **Drive stub cleanup** — inert junk, bottom of parking lot, nothing breaks if never done.

---

## Sweep limits (honest)

Aleph sweeps from a non-project chat can only see non-project chats. Decisions made INSIDE Claude projects (Confluence build sessions) are invisible to the sweep — those must flow into this ledger via KD! inside the project. Two rivers, one ledger.

---

## 2026-07-11 — Zone B harvest reconciliation (KD!)
*Lifted from six archive/handoff files into this ledger so decisions stop living only in dated handoffs. Full provenance in `claude/omnibus-studio-memory.md` (ideas table). These update, not replace, the 07-03 entries above.*

**OPEN — Drive round-trip is the recurring #1 friction (accountability flag).** The "save to Drive" half of the build round-trip has silently failed the entire v34→v42 arc; Drive Build Versions is stuck at v33, nine builds behind. This same drift has recurred across 3+ belt runs. It is a *systems* failure, not a to-do — a manual save closes today's gap and the gap reopens next build. Recommended fix: stop relying on the manual/Shortcut save; make the durable-save automatic (walshero Drive as the single shelf + a verified write, not a hoped-for Zap). Owner: Matt to authorize the mechanism; then delegatable.

**DECIDED — v40 is the canonical Confluence base.** 560,609 b, md5 `06868d7fefed82d11e3dbc7ae58342d4`, eyebrow "Department · v40". v42 (576,444 b) is real but lives only on a flickering project mount and could not be captured to a file — treat as unrecoverable. Next build: rebuild the SLO#3 paste seam onto v40, ship as v41 (numbers free to reuse). One stage per ship, one ship per round-trip.

**OPEN — OS is forked, not just duplicated.** Three generations (152,750 / 147,663 / 151,450 b; a fourth figure 161,666 appears in the 07-05 belt), each missing rules the others hold. **FERPA strip-before-save (§13.1, 34 CFR 99.31) exists ONLY in the 147,663 copy.** Do NOT canonize the newest as truth until the three-way merge ships. Merge is blocked on uploading the phone's 151,450 copy. The "duplicate OS" line in Zone A is really this fork.

**DECIDED — Studio is Tight Spiral Productions (TSP)**, renamed from Tight Spiral Studios 2026-07-02; propagate as-opened, never bulk. (Note: this Claude project is still titled "TIGHT SPIRAL STUDIOS" — rename is incomplete.)

**APPROVED — Assessment build roadmap (3 stages).** (1) Course/roster refresh + Supabase post seam + cycle-management form; (2) data aggregation with historical backfill to ~2002 (the differentiator most colleges lose) + forward intake from division coordinators; (3) reporting engine — outcome attainment, trend, program synthesis, action-plan tracker (NECHE-facing) + optional scheduled email hook. **FERPA scope locked: instructor syllabi/prompts ONLY** (instructor IP, not FERPA records); this clears both the FERPA-Steward and Build-Integrity-Warden HALTs. Student work would require a Nina + Provost conversation FIRST, never a build. Division of labor: Claude builds UI/schema/RLS SQL; Matt provisions Supabase (project, table, anon key, RLS) ~20 min one-time.

**VERIFIED — Real course list + faculty roster (live MassBay site, 2026-07-10).** Courses: EN101, EN102, EN120, EN195, EN202, EN210, ES100/ES150. 9 FT faculty (Codrington chair … Walsh). Wire into Confluence dropdown; verify two email spellings before shipping: `kmcgrath` (site typo "kmcgath"), `jdonato@massbay` (site typo "massby").

**OPEN — Repo IP exposure (HALT, stuck 3+ belts, highest-decay).** Whole IP tier is public on GitHub Pages. Good-enough-today fix: delete the 5 most sensitive files via the GitHub web editor (~10 min; exact click-path in `site-sweep-2026-07-02.md`). Exposure compounds daily; nothing else on the list does.

**STANDING RULE (reaffirmed today) — walshero is the durable shelf.** The studio archive is walshero-owned only; the post/MassBay account is never the durable shelf (institutional access can vanish). Current drift: TSP OS-blocks + STUDIO-COMMAND-CENTER + cross-lane-manifest are physically sitting in the *post* Drive right now. Reconcile to walshero.

**OPEN — Still-lost files:** `semester-arcade.html`, `en195-syllabus-game.html` (rebuild or hunt Drive). **Eliminate:** "President game" + "corpus builder" stubs. **Correctness:** Mode 3 scale bug — score 5 AND 6 both = EN102 (Sean/July-6 ruling); Trunk mislabels 6 as "Upper-Level Ready" — fix before next norming.

**Canon pointers (per 07-05 belt, verify against Drive):** OS = 161,666 b, CYL = v5 67,049 b, both in Drive > Claude_files > Tight Spiral Studio. Note the OS byte-count conflict with the OS-fork item above — resolve during the merge.

*End of 2026-07-11 append. Next append: KD! at close of next session.*

---

## 2026-07-11 — Integrity Guard run (scheduled, read-only)
**BLOCKED — first scheduled sweep could not probe.** WebFetch requires interactive per-URL approval; unattended run got `PROVENANCE_REQUIRED` on all URLs, so no live page was verified (FERPA floor unchecked, not cleared). NEW HIGH: guard cannot run unattended as designed — Matt to pre-authorize the public domain for WebFetch, or run it interactively. CYL-live-while-parked and the repo-exposure-vs-404 canon contradiction remain open founder gates. Detail in `claude/studio-guard-report.md`.

## 2026-07-11 16:05 UTC — Integrity Guard run #2 (scheduled, read-only)
**BLOCKED AGAIN — same `PROVENANCE_REQUIRED` wall on WebFetch; confirms the block is structural, not a first-run hiccup.** No live URL verified; FERPA floor still unchecked, not cleared. The guard will fail every scheduled run until the fetch path is fixed. Sharpened finding: the FERPA canon contradicts itself (live-links map + Command Center say trunk = 404/RESOLVED; Ledger Zone B HALT says IP tier still public) and the guard structurally cannot break the tie without a working probe. Decision owed by Matt: pre-authorize `walshero.github.io/TIGHT-SPIRAL-STUDIOS/` for WebFetch (recommended), run interactively, or commit a GitHub Actions link-checker. Detail in `claude/studio-guard-report.md`.

## 2026-07-11 17:05 UTC — Integrity Guard run #3 (scheduled, read-only)
**BLOCKED — third consecutive `PROVENANCE_REQUIRED` wall; no live URL verified.** Nothing new observed about the site (nothing could be observed); the only fresh fact is the third strike, which makes the fetch-path decision overdue. FERPA floor still unchecked-not-cleared; the trunk-404-vs-still-exposed canon contradiction stands unresolved. One decision unblocks the guard: pre-authorize `walshero.github.io/TIGHT-SPIRAL-STUDIOS/` for WebFetch (recommended), run it interactively, or commit a GitHub Actions link-checker. Detail in `claude/studio-guard-report.md`.

## 2026-07-11 18:05 UTC — Integrity Guard run #4 (scheduled, read-only)
**BLOCKED — fourth consecutive `PROVENANCE_REQUIRED` wall; both root and `confluence-TRUNK.html` probes refused. No live URL verified.** Four-for-four confirms the guard cannot run unattended by design; every future scheduled run will produce this same report until the fetch path is fixed. FERPA floor still unchecked-not-cleared; the trunk-404-vs-still-exposed canon contradiction stands. The fetch-path decision is now well overdue and is the single thing that unblocks the guard: pre-authorize `walshero.github.io/TIGHT-SPIRAL-STUDIOS/` for WebFetch (recommended), run it interactively, or commit a GitHub Actions link-checker. Detail in `claude/studio-guard-report.md`.

## 2026-07-11 19:05 UTC — Integrity Guard run #5 (scheduled, read-only)
**BLOCKED — fifth consecutive `PROVENANCE_REQUIRED` wall; no live URL verified.** NEW finding: the runs are one hour apart, not weekly — the scheduled task is misconfigured to fire hourly, so it churns an identical BLOCKED report and phone push every hour. Two fixes now owed, not one: (a) the fetch path — pre-authorize `walshero.github.io/TIGHT-SPIRAL-STUDIOS/` for WebFetch (recommended), run interactively, or commit a GitHub Actions link-checker; and (b) reset the cadence to weekly to stop the hourly churn. FERPA floor still unchecked-not-cleared; trunk-404-vs-still-exposed contradiction stands. Detail in `claude/studio-guard-report.md`.

## 2026-07-11 20:05 UTC — Integrity Guard run #6 (scheduled, read-only) — CLOSING the hourly series
**BLOCKED (sixth consecutive `PROVENANCE_REQUIRED`); root cause of the hourly churn now pinpointed.** The scheduled task `trig_01FQqXXXHr5mFBUt1JGWK3n4` ("Studio Integrity Guard — weekly sweep") has cron `0 * * * *` = hourly, not weekly. Two-step fix owed: (a) reset that trigger's cron to weekly, e.g. `0 13 * * 1`; (b) authorize `walshero.github.io/TIGHT-SPIRAL-STUDIOS/` for WebFetch so the weekly run can actually probe. FERPA floor still unchecked-not-cleared; trunk-404-vs-still-exposed contradiction stands. **To stop the fatigue this guard exists to prevent, this is the last hourly Ledger line and phone push: future runs that are still blocked AND still hourly should replace the report in place but NOT append here or push, until the cadence/fetch path is fixed.** Detail in `claude/studio-guard-report.md`.

---

# HARVEST — PRE-GIT DECISIONS (2026-06-23 → 2026-07-10)
**Landed 2026-07-11. Source: `session-tree.html`, `decision-tree-2026-06-29-evening.html`,
`decision-tree-2026-06-30.html` — three HTML logs that were the ONLY record of this period.**

**Why this section exists:** git's history begins 2026-07-11. Everything before that date is
invisible to git. These decisions lived only in dated HTML files with near-identical names —
unnavigable, unenforced, and one shelf-purge from gone. Harvested here so the source files can die.

## Method
- **Adaptive publishing is the method** — the artifact reshapes to the reader (interest /
  expertise / semiotic domain / use) instead of the reader adapting to the artifact.
- **Know a metaphor that travels from a model earned with data.** The capstone's MBTA is a
  metaphor; a physics-accurate transit model is a different project. Do not confuse them.
- **Confluence as player-prep engine** — calibrate the PLAYER before a game the way Confluence
  norms RATERS before scoring. (Still unbuilt. Still a good idea.)
- **A structural question is a system-wide probe** — run it across every component, not just the
  one that raised it.

## Floor
- **Muted `--ink2` text and green-on-paper text are BANNED.** Green is structural only —
  bars, borders, fills behind content. Never text.
- *(SUPERSEDED 2026-07-06: the "Comfort Gate as screen zero" ruling from this period is RETIRED
  as a WALL. No opening gate. Games open scene-first; comfort is a live corner control.)*

## The finding that should have been acted on and wasn't
**Probe Sweep, 2026-06-29: "rich in rules, thin in enforcers."**
**"A written floor without an enforcer fails — proven by tonight's bail."**

That was written **twelve days before** the 2026-07-11 session independently rediscovered the
same thing and named it *governance-rich, enforcement-poor*. The studio diagnosed its own core
disease, wrote it down in a dated HTML file nobody re-read, and then kept minting rules.

**This is the strongest possible argument for `resolve_canon` and for ONE ledger.** A finding
that lives in a file nobody opens is a finding that has to be made twice.

## Pipeline
- **The pipeline audited floors, never experience.** Flat builds passed because no gate asked
  *"does this feel like anything?"*
- **Fidelity tiers (Filament):** Alpha / Beta / Gold with exit criteria. Player-facing canonizes
  at **Gold**; tools at **Beta**.
- **Stage 6.5** — founder plays it on a phone before anything canonizes. *(This became GATE 1.)*
- **Depth beats breadth.** One world file, one front door. Builds freeze.

## Housekeeping decided then, still true
- **"Log it" produces a tree** — canonical file, no date, replace-don't-add.
  *(2026-07-11: superseded. The tree is retired. Git is the log from today forward; this ledger
  holds everything before it. See `LANE-REGISTRY.md`.)*
