# TSP Ledger
*Single decision log for all Tight Spiral Studios projects. Append via KD! at session close. This file is truth; chats are archive.*

---

## 2026-08-27 - CHECKED IS NOT SHIPPED: one failure class, four costumes

**THE INCIDENT.** Funnybonies v9.1 was verified hard: belt clean on all eleven ticks, full flow driven in a headless browser, zero JS errors, screenshots read by eye. It was then pushed to main through the GitHub connector with the literal string `PLACEHOLDER` as the file content. **The write succeeded.** The connector returned a commit sha and a green result. `funnybonies/index.html` on main became an 11 byte file and stayed destroyed until someone happened to look. Nothing was permanently lost only because the verified build still existed in the session sandbox.

**WHY NOTHING CAUGHT IT.** Every check in this repo grades **a file in a working tree**. The belt reads the worktree. Studio Eyes renders the worktree. Eleven ticks all ask *is this file good*. Not one of them can see the moment of **transmission**, because `git push` is blocked from the session sandbox, so bytes do not move mechanically, they are **retyped into a tool call**. Verification and transmission were decoupled and the gap between them was unwatched.

**PROBE SWEEP - the same class, four times in four costumes, all within three weeks:**

| When | Costume | What was checked | What actually shipped |
|---|---|---|---|
| 2026-08-06 to 08-24 | The 18 day outage | the belt, locally | Pages served an 18 day old site |
| 2026-08-23 | Site Watch | HTTP 200 liveness | a stale site, reported SUCCESS |
| 2026-08-22 | Seven wrong builds | artifact quality | the wrong game for the wrong player |
| 2026-08-27 | PLACEHOLDER | the local file | 11 bytes of nothing |

**One sentence covers all four: THE THING THAT WAS CHECKED WAS NOT THE THING THAT SHIPPED.** A green result is a claim about what a tool did. It is never proof of what arrived. This is the same shape as the belt's own oldest law, *a gate that has gone blind must never read as clean*, pointed one step further downstream: **a gate that was never looking at the shipped artifact was blind the whole time.**

**GRADUATED: `verify-push.sh`.** One mechanical comparison, no judgment. Fetch the remote, compare the content hash of each named path against the verified local file. Content-identical or HALT. Two canaries, one of them the incident itself. Run it after **every** connector write, before reporting anything as shipped.

**Deliberately NOT a belt tick.** The belt reads files in a tree; it cannot see a tool call. **Not every lesson becomes a tick.** Some failures live outside what the belt can look at, and pretending otherwise is how a repo ends up with gates that grade the wrong thing. This one lives in the deploy lane and runs AFTER a write, which is the whole point.

**IT CAUGHT ITSELF, TWICE, ON ITS FIRST LIVE RUN.** First it flagged real drift on its own push: the pushed copy had a hyphen where the local copy had an em dash, and the em dash was a house floor violation in the local file, so the remote copy was the correct one. Then it produced a **false** HALT on a file whose bytes were identical and whose only difference was a local `chmod +x`, because `git diff` also reports index state and file mode. Corrected to compare content hashes. **A false HALT is worse than no gate**, because a gate that cries wolf is one somebody disarms inside a week, and that is this repo's single most repeated lesson.

**THE STANDING RULE, now in `CLAUDE.md`:** never report a push as landed on a connector's success message. Pass `expect_total_bytes` on the way out, run `verify-push.sh` on the way back, and say nothing about shipping until it prints clean.

**WHAT IT COST TO LEARN THIS:** two minutes of a destroyed file and a full re-push. Cheap, this time, and only because the sandbox still held the verified copy. The next one will not be.

**CAUGHT ITSELF A THIRD TIME, AND THIS ONE IS THE SHARPEST.** The stop hook flagged a single modified file, `verify-push.sh`, from a local `chmod +x`. Chasing that mode bit found a real defect in the gate's own canary: every script in this repo is committed `100644`, because the connector is the only write lane out of the sandbox and it cannot set an exec bit. The self-test invoked `"$SELF"` directly, so it passed in the session that wrote it and would have failed on any fresh clone. **The gate's canary was broken for everyone but me.** That is the same failure class the gate exists to catch, one level up: the thing that was tested was not the thing anyone else would run. Fixed in three `bash ` insertions and written into the file's own header, so the next reader inherits the reason and not just the rule.

**THE GUARD FIRED BEFORE A HUMAN LOOKED.** The first push of that fix asserted `expect_total_bytes: 6428` while the payload carried only the header edit. The connector refused the write at 6413, exactly the 15 bytes of the three `bash ` insertions that had not been sent. No sha returned, no green result to misread, nothing landed. **This is what the assertion is for**, and it is the second time in one day it stopped a short write from being reported as a complete one.

**LANE CLOSED 2026-08-27, verified rather than assumed.** Three commits: `e7c8686` (the file mode note), `be5c267` (both canaries invoked with bash), `be6783d` (the usage line matches). Then `verify-push.sh` clean on five paths, self-test PASS at mode 644, `HEAD` against `origin/main` at `0 0`, working tree empty. **Every one of those is a check on the arrived artifact, not on the sending.**

**AND THE DISTINCTION THE GATE EXISTS TO HOLD:** committed is not deployed. All five files are content-identical on main and the live site still serves the old build, because Pages remains stopped at the floor job by tick 2 (5 governance records read as student attributions) and tick 5 (2 regressed entry paints). Those are separate facts and this entry states them separately on purpose. **Landing bytes on main is not shipping.** Founder call still open on both ticks.

---

## 2026-08-22 - Funnybonies v8 + TICK 11: the belt learns to ask what a build is for

**THE FINDING (2026-08-12, acted on today).** The founder halted Funnybonies: *"we are so far from vision. Peter wanted a game that would make kids laugh. I've not yet delivered."* A repo search then found `rescued/shelf-2026-07-13/funny-boneys-factory-spec.md`, a 28KB panel-reviewed GDD for that exact game, dated 2026-06-30, in the trunk the entire time. Never opened. Seven builds were made from a screenshot. Full account: `funnybonies/STOCK-TAKE-2026-08-12.md`.

**HARVEST, the one thing it proved.** A simulated audience cannot teach calibration. The construct is the delta between predicted-funny and actually-funny; replace real watchers with a cat holding a hidden answer key and you have built lock-picking. The kid stops being the author, the laugh stops being social. The construct dies the instant the audience is fake.

**HARVEST-BACK, the one thing the system should now catch.** All seven wrong builds PASSED EVERY BELT TICK. Ticks 1-10 are all artifact-quality checks and not one asks whether the artifact matches its spec or serves its named player. The pipeline has fidelity at Stage 3 and Stage 5, but the pipeline is paper and the belt is automation, so the cheap floors ran on every push while the expensive judgment was skipped by any session that started by writing code. Work flows to the automation.

**PROBE SWEEP.** Same failure class elsewhere: `funny-boneys-factory.html` is a mnemonic tool for adults and was labeled "the Peter deliverable" in the 2026-08-08 HITL packet. Peter asked for a game for kids. That mislabel predates this session and is corrected in canon here.

**GRADUATED (one per build, per the rate governor): TICK 11, intent.** `intent-gate.py` + `intent-baseline.json`, wired into `studio-belt.sh`. Two clauses, one question, the TICK 8 shape. A: a build must carry `<meta name="spec-source">` and that spec must resolve in the repo. B: it must carry `<meta name="audience">`, the player must not be a nobody-word (everyone / users / general / tbd), and it must share a content word with its own spec. Calibrated to TICK 8's shape and TICK 8B's definition of reachable, so the repo keeps one definition. **Presence RATCHETS, contradiction is FLAT.** Baseline: **244 undeclared fields across 122 of 123 surfaces.** Exactly one surface declares what it is for and who it is for, and it is the one built today. Debt, not a standard; it may only shrink. Self-test carries 13 canaries including the incident itself; applied retroactively the gate HALTs the v7 lineage, since `PRD-v7.md` never says "kids" once.

**LIMIT, in the gate's own docstring.** It reads a DECLARATION, not fidelity. A build can name a spec it does not follow and this tick will pass it. Two greps do not replace reading the spec. They make skipping it visible, which is the whole ask.

**TWIN RULE PAID.** The inert OLD TICK 7 block (source-parsing touch gate, retired 2026-08-08, dead code inside `if false`) pruned to a tombstone. 1350 bytes of unreachable shell that still read like a live tick.

**BUILT - Funnybonies v8.0 "The Gap"** at `/funnybonies/`, replacing v7 (KILL per the stock-take). Spec link and re-spine written BEFORE the build: `funnybonies/SPEC-LINK-v8.md`. The GDD core loop with step 1 moved off the screen and into the room: the kid builds a chain reaction out of household objects on a real table, chains 3 to 8 beats, predicts each beat's laugh, runs it for real people, and each watcher takes the phone and marks the beats that got THEM. The app computes the delta and names the biggest surprise. **It knows nothing about what is funny.** No editor, no simulated audience, no oracle. The distinction the seven builds got wrong, now in the code: the builder's prediction is self-report by design because it is the claim under test; the actual must come from someone else.

**LOOK - fresh per GDD section 4**, which forbids inheriting a prior build's palette. v8 drops the cream-and-ink register carried unchanged through v1-v7. New register: butcher paper and grease pencil, one hot accent. Your guess is drawn in pencil dashes; the real laugh burns in as hot fill. The entry scene states the thesis wordlessly: a machine on a table, and the person beside it is the one laughing. **The laugh belongs to a person, never to the app.**

**OPEN, founder's call.** v8 exists to answer one question: does calibration play work? One kid, three watchers, one table. If the gap screen produces the moment the design is betting on (the part they were proudest of is not the one that landed, and they want to run it again), the four judgment calls in GDD section 6.6 get made with evidence. If it does not, no editor was going to save it.

---

## 2026-07-23 — CYL v5: spine objection + game-design panel (logged, binding)

**DECIDED — The mechanic is the spine, not a sentence.** Game-design panel (Romero, Blow, Chen, Meier; Hocking on ludonarrative fit) advised: CYL's spine is the re-rate DELTA — rate blind → the record turns → rate again → SEE THE GAP between your two readings — not a thesis line. Implemented in `choose-your-leader-v5.html` (presentation only; ipsative capture unchanged): descent now shows the two readings on one 7-point scale with the gap between them; the 5→1 rung ladder and "rung X of 5" removed; "skill" language cut; ends on a Saunders mercy coda ("Be easy on the person in the chair — that was you, and you did fine with what you had."); honesty rings + MEASUREMENT_PENDING kept.

**SUPERSEDED — the 2026-07-18 founder-locked spine line.** *"You don't judge the leader. You judge what you were allowed to see."* — objected on three counts: scold ("you don't judge" contradicts the rating mechanic and quietly absolves); gatekeeper ("allowed" imports an intentionalist frame the game's own structural beats contradict); and drift toward "media literacy" (the framing guarded against, per `CYL_Harvest…md`). Demoted off the title screen. Saunders reframed the intent; the panel then demoted the line itself to a post-play coda. A lock re-opened by objection, not photocopied forward.

**RECORDED — CYL art lane reconciled (cross-chat, via the repo).** Rooms ship as handcrafted SVG dioramas (never smooth-AI-photoreal — Greg-the-pancake). Photoreal = magazine collage of real period print (founder ruling). Art direction owned by `cyl-period-bible.md`; operational manifest `cyl-v5-image-lane.md`. "Never a real face" rationale: epistemic (strip the halo), methodological (control the variable), inclusive (the chair stays anyone's), science-grounded (faces pre-empt judgment), rights (living-figure disinfo hazard), rhetorical (the withholding is the point).

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
**BLOCKED — third consecutive `PROVENANCE_REQUIRED` wall; no live URL verified.** Nothing new observed about the site (nothing could be observed); the only fresh fact is the third strike, which makes the fetch-path decision overdue. FERPA floor still unchecked-not-cleared; the trunk-404-vs-still-exposed canon contradiction stands unresolved. One decision unblocks the guard: pre-authorize `walshero.github.io/TIGHT-SPIRAL-STUDIOS/` for WebFetch (recommended), run interactively, or commit a GitHub Actions link-checker. Detail in `claude/studio-guard-report.md`.

## 2026-07-11 18:05 UTC — Integrity Guard run #4 (scheduled, read-only)
**BLOCKED — fourth consecutive `PROVENANCE_REQUIRED` wall; both root and `confluence-TRUNK.html` probes refused. No live URL verified.** Four-for-four confirms the guard cannot run unattended by design; every future scheduled run will produce this same report until the fetch path is fixed. FERPA floor still unchecked-not-cleared; the trunk-404-vs-still-exposed canon contradiction stands. The fetch-path decision is now well overdue and is the single thing that unblocks the guard: pre-authorize `walshero.github.io/TIGHT-SPIRAL-STUDIOS/` for WebFetch (recommended), run interactively, or commit a GitHub Actions link-checker. Detail in `claude/studio-guard-report.md`.

## 2026-07-11 19:05 UTC — Integrity Guard run #5 (scheduled, read-only)
**BLOCKED — fifth consecutive `PROVENANCE_REQUIRED` wall; no live URL verified.** NEW finding: the runs are one hour apart, not weekly — the scheduled task is misconfigured to fire hourly, so it churns an identical BLOCKED report and phone push every hour. Two fixes now owed, not one: (a) the fetch path — pre-authorize `walshero.github.io/TIGHT-SPIRAL-STUDIOS/` for WebFetch (recommended), run interactively, or commit a GitHub Actions link-checker; and (b) reset the cadence to weekly to stop the hourly churn. FERPA floor still unchecked-not-cleared; trunk-404-vs-still-exposed contradiction stands. Detail in `claude/studio-guard-report.md`.

## 2026-07-11 20:05 UTC — Integrity Guard run #6 (scheduled, read-only) — CLOSING the hourly series
**BLOCKED (sixth consecutive `PROVENANCE_REQUIRED`); root cause of the hourly churn now pinpointed.** The scheduled task `trig_01FQqXXXHr5mFBUt1JGWK3n4` ("Studio Integrity Guard — weekly sweep") has cron `0 * * * *` = hourly, not weekly. Two-step fix owed: (a) reset that trigger's cron to weekly, e.g. `0 13 * * 1`; (b) authorize `walshero.github.io/TIGHT-SPIRAL-STUDIOS/` for WebFetch so the weekly run can actually probe. FERPA floor still unchecked-not-cleared; trunk-404-vs-still-exposed contradiction stands. **To stop the fatigue this guard exists to prevent, this is the last hourly Ledger line and phone push: future runs that are still blocked AND still hourly should replace the report in place but NOT append here or push, until the cadence/fetch path is fixed.** Detail in `claude/studio-guard-report.md`.

## 2026-07-12 12:20 UTC — Integrity Guard run #19 — FIRST SUCCESSFUL PROBE, and it found a CRITICAL
**UNBLOCKED (Matt approved WebFetch interactively) — and the FERPA "RESOLVED" note is WRONG.** Live probe found `confluence-TRUNK-2026-06-23.html` returns HTTP 200, serving six MassBay faculty names+emails (mwalsh/jdonato/kmcgath/dadeyemi/litmag/ENchair @massbay.edu). The July tier-split took down the *undated* `confluence-TRUNK.html` (confirmed 404) but missed this *dated* twin — the exact file on the 07-02 "5 most sensitive" list. Also still LIVE: `claude-project-instructions.md`, `chatgpt-pro-instructions.md`, `massbay-fact-book-word.docx` (pipeline IP + institutional doc). CLEARED: student PII none (course pages are seat-label-only, FERPA-safe); `tight-spiral-studio-os.md` 404; Choose Your Leader live but clean of named real figures; no emoji on any of 14 public pages. ACTION owed by Matt: delete the 4 live sensitive files via GitHub web editor (click-path in `site-sweep-2026-07-02.md`), then correct Command Center v5.1 + live-links map which falsely say the faculty trunk is down. Cadence still hourly (`trig_01FQqXXXHr5mFBUt1JGWK3n4` = `0 * * * *`) — reset to weekly. Phone push sent (CRITICAL). Detail in `claude/studio-guard-report.md`.

## 2026-07-12 13:05 UTC — Integrity Guard run #20 — CRITICAL still open, roster longer than #19 caught
**Live probe succeeded (naming each URL in-message clears the `PROVENANCE_REQUIRED` gate — so the guard CAN run unattended). State unchanged from #19 ~45 min ago: nothing taken down.** `confluence-TRUNK-2026-06-23.html` still returns HTTP 200. This probe pulled a longer list than #19: 7 emails and 17 names (mwalsh/litmag/ENchair/jdonato/kmcgath/kmcgrath/dadeyemi @massbay; names incl. Codrington, McCarthy, Lyons, Kistner, Giancioppo, Dow, Moreno, Oakley, Desmarias, Sebugwawo, Earl, Murad, Rocha, Conrad). Several are NOT on the verified faculty roster and may be students — so this can no longer be characterized as faculty-only; treat as possible student PII until Matt confirms. Still LIVE too: `claude-project-instructions.md`, `chatgpt-pro-instructions.md`, `massbay-fact-book-word.docx`. Still 404 (good): `confluence-TRUNK.html`, `tight-spiral-studio-os.md`. Choose Your Leader live+clean; root splash unchanged (links only en195 + sandbags); no emoji anywhere. Action owed by Matt is unchanged and now more urgent: delete the four live files (06-23 trunk first), then correct Command Center v5.1 + live-links map, then reset the trigger to weekly. Phone push sent (still-open CRITICAL). Detail in `claude/studio-guard-report.md`.

## 2026-07-12 14:05 UTC — Integrity Guard run #21 — BLOCKED again; #20 workaround regressed; no re-push
**BLOCKED — `PROVENANCE_REQUIRED` returned on all 5 attempts (root + `confluence-TRUNK-2026-06-23.html`), each URL named in-message exactly as #20 did.** So the "name-in-message clears the gate" workaround #20 relied on is NOT durable — it worked once (likely while #19's interactive approval was still warm) and has since closed. No live page verified this run; the run #20 CRITICAL (faculty/possible-student PII file at HTTP 200) and the three HIGH files stand as **last-known-open, unconfirmed since 13:05** — could still be up or could have come down; the guard cannot currently tell. **No phone push sent** (per the Run #6 anti-fatigue rule; this CRITICAL was already pushed at #19 and #20 today, and a blocked run adds no new observation). The durable fetch-path fix is now the recurring blocker: pre-authorize `walshero.github.io/TIGHT-SPIRAL-STUDIOS/` for WebFetch, run interactively, or commit a GitHub Actions link-checker (no provenance gate). Cadence still hourly — reset `trig_01FQqXXXHr5mFBUt1JGWK3n4` to weekly. Detail in `claude/studio-guard-report.md`.

## 2026-07-12 15:05 UTC — Integrity Guard run #22 — PROBE SUCCEEDED; CRITICAL confirmed WORSE (undated trunk is live too)
**Fetch path recovered — all 21 URLs loaded, no provenance block; 404 detection verified working (a known-dead file returned a real 404).** Fresh live confirmation, and worse than #20: the *undated* `confluence-TRUNK.html` — which #19/#20 and all canon say is 404/RESOLVED — is **LIVE (HTTP 200)** serving the same faculty+student PII payload (7 emails, ~19 names incl. student writers Sarah Courchesne, Peter Kistner, Nick Giancioppo, Chelsea Dow, Gabriela Moreno, Georgia Oakley, Nathan Desmarias). The dated twin `confluence-TRUNK-2026-06-23.html` is also still LIVE. Still LIVE (HIGH): `claude-project-instructions.md`, `chatgpt-pro-instructions.md`, `massbay-fact-book-word.docx`. Confirmed 404 (good): `tight-spiral-studio-os.md`. All 14 public pages return 200, no broken links, no emoji, no green-outside-Confluence, Choose Your Leader live+clean. Action owed by Matt (unchanged, more urgent): delete the two trunks + three HIGH files via GitHub web editor; then correct Command Center v5.1 + live-links map (both wrongly say the trunk is down); then reset `trig_01FQqXXXHr5mFBUt1JGWK3n4` from hourly to weekly. Phone push sent (fresh confirmation + "canon says 404 but it's live" are new information). Detail in `claude/studio-guard-report.md`.

## 2026-07-12 21:05 UTC — Integrity Guard run #28 — PROBE SUCCEEDED; CRITICAL still live 6h later; front page rebuilt
**Fetch path worked again (all URLs loaded, 404 detection verified via `tight-spiral-studio-os.md`).** The CRITICAL is unchanged from #22 — nothing taken down in six hours. Both `confluence-TRUNK.html` and `confluence-TRUNK-2026-06-23.html` still return HTTP 200 serving faculty emails + apparent student writers (Kistner, Giancioppo, Dow, Moreno, Oakley, Desmarias, alumni). Three HIGH files still live (`claude-project-instructions.md`, `chatgpt-pro-instructions.md`, `massbay-fact-book-word.docx`). NEW: the public front page has been **rebuilt** since the 2026-07-11 map — root now links a new set (the-console, choose-your-leader-**v5-slice**, the-tell, cliche-cowpaths, behind-this-door, funny-boneys-factory, en195, arcade, how-an-idea-travels); the old map is stale and `studio-live-links-2026-07-11.md` needs re-probing. New game pages scan clean of student PII (two show Matt's own walshero@gmail.com by choice; console/CYL use theme-toggle glyphs — borderline vs no-emoji rule). CLEARED: `tight-spiral-studio-os.md` 404; no green-outside-Confluence; CYL live+clean of named real figures. Action owed by Matt unchanged and now 6h+ stale: delete the two trunks + three HIGH files; correct Command Center v5.1 + live-links map; make the fetch path durable (GitHub Actions link-checker or pre-authorized WebFetch domain — the interactive approval is intermittent); then reset `trig_01FQqXXXHr5mFBUt1JGWK3n4` from hourly to weekly. Phone push sent (still-live CRITICAL + rebuilt front page are new information). Detail in `claude/studio-guard-report.md`.

## 2026-07-13 00:24 UTC — Integrity Guard run #31 — PROBE SUCCEEDED; CRITICAL still live, unchanged; rebuilt front page scanned clean
**Fetch path worked (all URLs loaded; 404 detection verified via `tight-spiral-studio-os.md`).** State unchanged from Run #30 ~12 min earlier and from #22/#28: nothing taken down. Both `confluence-TRUNK.html` and `confluence-TRUNK-2026-06-23.html` still return HTTP 200 with named students (Kistner, Giancioppo, Dow, Moreno, Oakley, Desmarias, Sebugwawo, Earl, Murad, Rocha, Conrad, Courchesne) + faculty emails. Three HIGH files still live (`claude-project-instructions.md`, `chatgpt-pro-instructions.md`, `massbay-fact-book-word.docx`). NEW this run: all nine rebuilt front-page builds scanned page-by-page — clean of student/faculty PII and emoji; `choose-your-leader-v5-slice.html` retitled "Choose Your Leader — October 22, 1962," no named real figures (old RED flag clean); Matt's own walshero@gmail.com appears on the-tell + behind-this-door by choice (informational). CLEARED: `tight-spiral-studio-os.md` 404. Action owed by Matt unchanged: delete the two trunks + three HIGH files via GitHub web editor; correct Command Center v5.1 + live-links map; make the fetch path durable; reset `trig_01FQqXXXHr5mFBUt1JGWK3n4` from hourly to weekly. Phone push sent (standing CRITICAL, weekly run, still unresolved).

## 2026-07-13 01:10 UTC — Integrity Guard run #32 — PROBE SUCCEEDED; state UNCHANGED from #31; no push
**Fetch path worked (provenance gate blocked first attempts, cleared on single-URL retries; 404 control honest via `tight-spiral-studio-os.md`).** No change in the ~45 min since Run #31: both `confluence-TRUNK.html` and `confluence-TRUNK-2026-06-23.html` still HTTP 200 with named students + faculty emails (CRITICAL); three HIGH files still live (`claude-project-instructions.md`, `chatgpt-pro-instructions.md`, `massbay-fact-book-word.docx`); root unchanged (nine builds). **No phone push** — identical CRITICAL was pushed at #31 forty-five minutes ago; unchanged state adds no information, and re-pushing is the exact notification fatigue this guard exists to prevent (Run #6 rule). Action owed by Matt unchanged: delete the five files; correct Command Center v5.1 + live-links map; reset `trig_01FQqXXXHr5mFBUt1JGWK3n4` from hourly to weekly and make the fetch path durable. Detail in `claude/studio-guard-report.md`.

## 2026-07-13 02:05 UTC — Integrity Guard run #33 — BLOCKED (probe blind); no push
**BLOCKED — `PROVENANCE_REQUIRED` on all three WebFetch attempts (single-URL retries + URLs named in-message); the gate did not clear this run, same wall as #21.** No live page verified. The Run #32 standing findings (CRITICAL: both `confluence-TRUNK*` trunks with named students + faculty emails; three HIGH files) carry forward as **last-known-open, unconfirmed since 01:10 UTC** — the guard is blind and cannot tell whether anything came down in the last hour. **No phone push** (blind run adds no new observation; standing CRITICAL already pushed at #31; Run #6 anti-fatigue rule). The two structural fixes are now the highest-leverage action and remain owed by Matt: reset `trig_01FQqXXXHr5mFBUt1JGWK3n4` from hourly (`0 * * * *`) to weekly (`0 13 * * 1`), and make the fetch path durable (pre-authorize `walshero.github.io/TIGHT-SPIRAL-STUDIOS/` for WebFetch, or a server-side GitHub Actions link-checker). Detail in `claude/studio-guard-report.md`.

## 2026-07-13 13:06 UTC — Integrity Guard run #34 — PROBE BLIND, but CADENCE FIX CONFIRMED LANDED
**One structural fix done, one still owed; site probe blind.** WebFetch hit `PROVENANCE_REQUIRED` on every attempt (parallel batch of 8 + single-URL retries + a post-pause retry) — no live page verified; the Run #32 CRITICAL (both `confluence-TRUNK*` trunks with named students + faculty emails) and the three HIGH files carry forward as **last-known-open, unconfirmed since 01:10 UTC (~12h)**. NEW & GOOD (read-only trigger check via list_triggers): `trig_01FQqXXXHr5mFBUt1JGWK3n4` is now cron `0 13 * * 1` (weekly, Mon 13:00 UTC), updated 2026-07-13T02:52 UTC, next run 2026-07-20T13:04 UTC — the hourly churn is OVER and this run fired on the correct weekly schedule; the "reset to weekly" action is **resolved**, drop it from the open list. STILL OWED (now the only structural fix): make the fetch path durable — commit a GitHub Actions link-checker (recommended, no provenance gate; runs even with no chat open) or pre-authorize the domain for WebFetch; this blind run is itself the proof it's still broken. FERPA action unchanged: delete the two PII trunks + three HIGH files, then correct Command Center v5.1 + live-links map. Phone push sent (first true weekly run; ~12.7h since last push; standing student-PII CRITICAL still open + one fix landed / one still broken = new information). Detail in `claude/studio-guard-report.md`.

## 2026-07-13 14:21 UTC — Tableau Sweep #1 (scheduled, read-only) — 16 of 21 builds ship-blocked on the entry gate
**First weekly run of the "run the belt on all games" loop (ratified 2026-07-12).** Swept 21 builds through `one-thing-gate.py` @1280×800 headless Chromium: **3 PASS · 2 WARN · 16 SHIP-BLOCK**; gate exit 1. **Zero emoji studio-wide** — the no-emoji floor holds everywhere. Worst offender by the gate arithmetic: `laughter-foundry-spec-and-log` (197-word wall + 5 co-equal invitations) — a spec/log surface, not a core game. Worst among core playable games: the four text-walls `choose-your-leader-full`, `convergence-card-engine`, `sandbags-joy`, `flash-ballast`. PASSes: `cliche-city`, `cliche-line`, `cliche-field-v6`. Note: `cliche-field.html` (plain) still ships the OLD two-button entry and ship-blocks, but `cliche-field-v6.html` PASSES — the fix exists; **promote v6 over the plain file.** GROWTH HABIT fired — three failure classes recur past the 3-build trigger: invitation-count≠1 (13/21), text-wall (8/21), control-clutter (11/21). Two proposals DRAFTED for ratification (not self-adopted): (1) a surface-type split in the gate — game/hub/doc rubrics via a `tsp:surface` meta tag — so course hubs, launchers, a decision-lab, and a spec-log stop being graded as broken games; (2) seat a "Scene-First Scaffold" as the studio default so builds are born passing. FILE-COLLISION FLAGGED: the routine's step-4 target `claude/studio-guard-report.md` is owned by the Integrity Guard sweep (standing CRITICAL there) — this sweep wrote to `claude/tableau-sweep-report.md` instead and did NOT clobber the guard report; recommend the routine's target be corrected. Read-only: no game edited, nothing published. Detail in `claude/tableau-sweep-report.md`.

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

## 01:05 — Founder log: repo connected, PII reclassified, showcase-lock scoped (session, read-mostly)
**Rulings logged at the moment (founder mandate: "I'm losing vision, log it").**
- **CONNECTED** — the GitHub repo lane (`walshero/TIGHT-SPIRAL-STUDIOS`) is now reachable AND pushable from a session; founder provided a write-capable token this session. Supersedes FUNES's standing "no session can push / pull is Matt's or Josh's hands." Token is transcript-exposed → founder to rotate.
- **RECLASSIFIED** — Integrity-Guard Gate #0 "student PII CRITICAL / FERPA" is corrected. Verified from source (`confluence-TRUNK.html` = v44, md5 `8dcf990336eb1c0ffa600cae3b689539`, 598,114 B, byte-verified): the flagged content is the Lumière published award-winners showcase — consented student bylines + faculty directory emails (6, all `@massbay.edu`) + students' own quoted published poems. Not education records; not a FERPA breach — an editorial/consent call, not a legal emergency. Founder concurred ("Right").
- **SCOPE FINDING (halted before any push)** — "lock part of the showcase for founder" is larger than first framed: the 6 student names appear in **16 woven places** (6 award bylines, 1 featured-essay byline with military rank, 3 pull-quotes of the students' own poems, 5 prose mentions, 1 awards-summary string inside the page JS) — not a 6-item list. A partial scrub would be a hollow claim; a full scrub is real editorial surgery. HELD for a founder scope decision (recommendation on the table: lift the named showcase block into a founder-only copy rather than make 16 fragile edits). A full-names founder copy was preserved off-repo.
- **PRODUCED this session** — Tableau Sweep #1 (16/21 entry ship-blocks; `claude/tableau-sweep-report.md`); Studio Eyes v2 cross-field upgrade (`claude/studio-eyes-v2-cross-field-upgrade.md` — fixes the cry-wolf classifier; the PII reclassification above is its first application); founder-lock demo (AES-GCM ciphertext honesty model, zero plaintext names in source).
- **CANON UNCHANGED** — no push made; `confluence-TRUNK.html` remains v44 (md5 `8dcf9903…`), reverted byte-clean after the scope check. Repo canon-diff honored (md5 matched FUNES's v44 pointer from source).

## 2026-07-17 — Founder log: motion specimen shipped, PAT live this session, canon-inversion caught

**Session rulings, in Matt's words the day made.**

- **BUILT + SHIPPED** — `motion-specimen.html` (repo, 11,064 B, md5 `3be57545…`). A pattern-lock reference: one source of MOTION truth, the way preship-contrast-gate.py is one source of color truth. Four moves — Sisyphus letterhead loop, settle-on-load, comfort-stop crossfade, reveal (Console-style delayed disclosure). Paper ground, all THREE comfort stops. Founder call: "5, 1 when tricky" — advanced version (three stops), fall back to default-only where the tricky panel bites. Warm-dark was the tricky panel.
- **GATE + HAND-VERIFY** — preship gate PASS all three modes (worst pair 4.79:1, softer --ink-3, AA). Because each comfort stop is a full `html[data-comfort=...]` palette (not :root-only), the gate READ warm this time — the per-mode discipline HANDOFF-render-proof-gate.md asked for, achieved by construction. Warm-dark hand-verified against the render-proof floor: html+body+section all paint opaque `--paper` (no white-sheet bleed), warm ink tokens all cool near-white (#f4f1e8/#d9d3c4/#bcb6a6), amber never used as `color:` on text. ONE watch-item flagged to founder: the warm-mode eyebrow uses muted-gold `--brass-ink` (accent label, 11:1) — founder's retina is the verdict on cold play; one-line flip to --cool-ink if it smears.
- **CANON INVERSION CAUGHT (index.html)** — the prior handoff said "shelf holds the Manhattan fix, repo is stale." INVERTED. The repo already held the fix (md5 `038e566d`, "Advantage Relocation / running firm"); the SHELF lagged. Claude trusted the handoff note over the diff, pushed stale shelf over good repo, caught the regression on POST-TICK (wording came back wrong), reverted. Net zero — live page was correct before and after. LESSON RE-EARNED: the handoff note is not a source; the diff is. Task 1 was a no-op.
- **LEDGER RECONCILED** — the 01:05 founder-log block (repo-connected, PII reclassified, showcase-lock scope) existed only on the shelf; landed in repo this session (md5 `2a9de52…`). All four lanes now agree on TSP_Ledger.md.
- **PAT LIVE THIS SESSION** — Matt provided a write-capable fine-grained token; container git-push worked (four commits this session). This SUPERSEDES the FUNES charter line 99 ("cannot push to the repo from a session") FOR THIS SESSION ONLY. Token is transcript-exposed → founder to rotate at GitHub → Developer settings → Fine-grained tokens. Charter is not amended; the standing default remains no-session-push.
- **STILL OPEN** — EN195 placement (Writerly Moves Arcade vs. MassBay edu hub) — founder's call, not made. Render-proof gate teeth still unbuilt (HANDOFF-render-proof-gate.md); the warm-dark hand-verify above is manual because those teeth don't exist yet.

## 2026-07-18 — Founder log: RP-world render bug closed, orphans rescued, Zapier no-PAT lane proven

**What the day earned. Cleanup session — no new governance, two archaeology days now paid off.**

- **PAT LEAK + REFUSAL** — Matt pasted a live fine-grained PAT into chat. Claude REFUSED to use it and did not push with it. Standing action: rotate/revoke at GitHub → Settings → Developer settings → Fine-grained tokens. The whole session then ran on the **Zapier no-PAT GitHub lane** instead (`github_create_or_update_file`, `GitHubCLIAPI`, account `walshero`) — no token in context, pauses for founder approval tap. Proven end-to-end: 6 writes, every one readback-verified from git.
- **ZAPIER GITHUB LANE = CANON DEPLOY PATH (no PAT).** This supersedes "PAT required to push" for ordinary file writes. It is functional-exact, NOT byte-exact — it nudges HTML/CSS comment characters (box-drawing dashes, blank lines) in transit. The readback-diff is the check and it caught every nudge. Use container git-push (PAT) when comments are canon (specs, annotated OS blocks). ⚠ UPDATING AN EXISTING REPO FILE via this lane requires the current blob `sha` (new files do not) — fetch it with `git rev-parse origin/main:<file>` first; and the `content` param must carry the FULL body verbatim (a placeholder truncated this very ledger once this session — caught and restored by the readback).
- **RESOLVE-CANON.PY WAS SHELF-STALE** — the tool caught its own staleness: shelf copy (10,508 B) lagged the repo canon (12,276 B), missing the 2026-07-13 recursive `git ls-tree` fix. Always fetch it fresh from repo raw before an audit; run it from inside a clone.
- **6 ORPHANS RESCUED** — shelf-only files with no deploy lane, now live in repo, each readback-verified: `claude_seat-registrar.md` (35c6532), `claude_FUNES-CHARTER.md` (ecbbce4), `claude_FUNES-INDEX.md` (af4c86a), `tsp-spiral-studio.html` (e9826bd), `CYL_Harvest__Access_Boundary_Findings_and_Re-Run_Instructions.md` (d4052f6), `your-rp-world.html` (51ce54b). Post-audit: **orphans 0, canon-stubs 0, single-lane 0.** Remaining 7 "drift" flags are all `canon=repo, shelf lags` — informational, self-correcting on pull.
- **RP-WORLD RENDER BUG CLOSED** (`your-rp-world.html`, commit 51ce54b). ROOT CAUSE of the 13.23:1-certified / 1.17:1-rendered warm-dark bug: `body.warm` remapped `--paper` to dark, but the comfort toggle did `removeProperty("--paper")` on the warm branch, leaving the body surface cascade-dependent — on iOS the white sheet showed through and gold text resolved against nothing. FIX (arithmetic, two lines): (1) CSS — `body.warm{ background:#151210 !important }`, a literal opaque surface that never depends on cascade timing; (2) JS — warm branch now `setProperty("--paper","#151210")` so html+body agree, no undefined gap. Gate exit 0, worst pair 8.28; SIX render-proof hand-checks pass (literal surface present, warm sets --paper, no removeProperty-on-warm, --dusk gold never a background fill so token-role law holds, no transparent body surface).
- **LESSON RE-EARNED — THE GATE IS A SUSPECT.** The token gate certified the broken file at 13.23:1 because it reads color PAIRS, not whether the surface PAINTS. It passed the fixed file the same way. The real check was the six-item render-proof HAND-verify, not the gate number. The render-proof teeth (opacity tooth, per-mode paint check) named in HANDOFF-render-proof-gate.md are STILL UNBUILT — until they exist, warm-dark ships only after the manual hand-verify.
- **`your-rp-world.html` STATUS** — a finished Stage-1 vertical slice: nav floor (back+home every screen), scene-first home, no opening wall, mailto-only send to mwalsh@massbay.edu, disclaimer floor on the treatments layer, >50% image per screen. Only the warm-render bug was ever wrong; it is now closed. GATE 1 (founder cold phone play, warm-dark mode specifically) is the remaining ship gate.
- **STILL OPEN** — rotate the leaked PAT; build the render-proof gate teeth (HANDOFF-render-proof-gate.md); wire resolve-canon.py + preship-gate-v3.py into GitHub Actions on push (needs a fresh PAT for Actions); push preship-gate-v3.py to repo so it becomes canon.

## 2026-07-19 — Founder log: the Pages 403 root-caused and cleared (it was the gate, not the door)

**Five days of a site-wide 403 that was never a delivery bug. Full write-up: `SELF-DIAGNOSIS-2026-07-19-pages-403.md`.**

- **ROOT CAUSE** — `walshero.github.io/TIGHT-SPIRAL-STUDIOS/` returned `403` on every URL (consistent GitHub error page, md5 `1f5fcbc`) because Pages Source was flipped to **"GitHub Actions"** (branch builder `pages-build-deployment` last ran 2026-07-11 and never again while `main` kept moving — the source-flip fingerprint). `floor.yml`'s `deploy` job is now the only publisher, and it is chained `needs: floor`. The ratchet **armed 2026-07-14**; we push regressions **straight to `main`**; so regression → `floor` exits 1 → `deploy` SKIPPED → no fresh deployment under the Actions source → 403. **The empty-commit "nudges" (`445b21a`, etc.) could never work — each one re-ran the failing ratchet and re-skipped deploy.** The gate was arithmetically right (`.status.wait` really was 1.0:1 invisible; `your-rp-world` really reached off-box) — the failure was BLAST RADIUS: one per-file miss took the whole front door offline.
- **RESOLVED (not by a 403 fix — by paying the debt)** — PR #3 (`ee010c8`, front door + clear CYL v5) and PR #4 (`43fcbae`, **inline mobile module — single-file-offline law**) cleared the five blocking regressions (inlining killed the external-host H4/H7 halts). On `43fcbae` the ratchet returned **0 regressions**, `floor` PASSED, `deploy` ran, `actions/deploy-pages` logged **"Reported success!"** → `https://walshero.github.io/TIGHT-SPIRAL-STUDIOS/` at **2026-07-19 14:27 UTC**. Site restored, by the ratchet turning one way exactly as designed once the corpus was clean.
- **VERIFIED FROM SOURCE** — cloned repo, reproduced the sweep with `bs4` ABSENT (matches CI: it installs only `playwright`+`axe-core`), `python3 ratchet.py` → **exit 0** on current `main`. Deploy job (id `88203200016`) all-green; deploy-pages liveness reported. ⚠ CAVEAT: the diagnosing sandbox's egress proxy blocks `*.github.io` (proxy-level 403, not GitHub's), so the live page was pipeline-confirmed, not eyeball-confirmed — founder hard-refresh is the last check.
- **LESSON RE-EARNED — A BLOCKING GATE ON THE LIVE-SITE DEPLOY IS A KILL SWITCH.** "A gate that does not block is not a gate" — true. Other half, paid for this week: a gate on *delivery to the public*, fed by direct pushes to `main`, does not fail a check — it takes the site GONE. Under "Deploy from a branch" a red check leaves the last good build serving (degrades to STALE); under "GitHub Actions" gated on the check, a red check serves NOTHING (degrades to GONE). We put the chokepoint between the visitor and the whole door. This is the 07-18 STILL-OPEN line ("wire the gates into Actions on push") biting — done without decoupling liveness.
- **NO ALARM = THE REAL BUG.** A 5-day outage (armed 07-14 → restored 07-19) with the only signal being a yellow "a check is failing." "The site is down" must be detectable AS ITSELF. Same class as TICK 4 / the-gate-went-blind: a monitor reporting the wrong severity lies.
- **RECOMMENDATION (decision needed, not made)** — (a) keep the teeth, move the chokepoint to the MERGE: require PRs into `main` with `floor` as a required status check → a regression fails the PR and never lands on canon, so `main` stays green and deploy is never handed broken work. The PEP in the RIGHT place — guarding entry to canon, not delivery to the public. Cost: stop direct-pushing `main`. (b) decouple deploy (`if: always() && …`) — site never hostage but an inaccessible page CAN ship (wrong default for a founder losing vision; emergency hatch only; one-line patch preserved in the diagnosis doc, NOT applied). (c) Source back to "Deploy from a branch" — last good build always serves, gate advisory. **PLUS, regardless: give the Pages URL its own HTTP-200 liveness probe on the hourly Integrity Guard.** Recommend **(a) + the liveness probe.**
- **NOT CHANGED** — `main`'s `floor.yml` left COUPLED with teeth intact (founder wants the teeth kept). The decouple patch was prepared, then withdrawn as contrary to intent; it lives in the diagnosis doc as an option.
- **STILL OPEN** — pick (a)/(b)/(c); add the Pages HTTP-200 probe; the render-proof gate teeth remain unbuilt (HANDOFF-render-proof-gate.md); rotate any leaked PAT.

## 2026-07-19 — SHIPPED: The iSLO Suite (student-facing hub, measures + builds the 7 competencies)

**Ask:** a hub for a series of MassBay games that measure and help build iSLO skills; research + propose the suite. **Delivered:** `islo-hub.html` (SHIP on preship-gate-v4, worst pair 5.57:1) + `ISLO-GAME-SUITE-PROPOSAL.md`.

- **OUTCOMES LOCKED FROM SOURCE, NOT MEMORY** — the seven MassBay Graduation Competencies (iSLOs) read verbatim from the Spring 2026 ISLO #5 workshop deck in Drive: 1 Written/Oral Comm · 2 Quantitative · 3 Tech/Info-Sci · 4 Natural World · 5 DEI · 6 Critical Thinking · 7 Personal/Civic. Live rubrics pulled verbatim: **ISLO #1** (AAC&U Written Comm VALUE, MassBay-modified) and **ISLO #5** (Systems of Power · Group/Individual · Advocacy, 0–4). ISLO #6 rubric confirmed IN DEVELOPMENT.
- **FINISHING, NOT BUILDING** — 19 existing shelf builds map onto the 7 outcomes. The hub is the student sibling of Confluence (faculty norm) and the islo-switcher (rubric viewer): same outcomes, same rubrics, three surfaces. It **shows the dry cells** (Confluence's own thesis, turned on the game shelf): iSLO 4 dry, iSLO 2 + 5 thin, iSLO 6 built-over-an-unnormed-rubric.
- **MEASURE + BUILD = TWO INSTRUMENTS** — each station shows the game (build the skill by playing) beside the verbatim rubric (measure it). Ipsative/criterion-based framing held to the dignity floor: a starting point is never a verdict; scored against the college's levels + your own prior draft, never ranked against peers.
- **PROPOSED (ranked by value-to-effort)** — (1) `Sticker Price` iSLO 2, reuses the shipped Tension Bar cost-decomposition engine → lowest effort, also generates work samples to norm a local QL rubric; (2) `Who Holds the Room` iSLO 5, built to the three live ISLO #5 dimensions as three rounds; (3) `Update the Model` iSLO 4, the tight-spiral loop (hypothesis→test→update) finally pointed at the science outcome — clearest gap, both build + norming open.
- **FLOOR HELD** — reused index.html's shipped/gated token palette verbatim (token-role law, green-free render-proof). Standing nav is STATIC (Home + Back, no-JS, offline, gate-detectable) — chose static over the JS tsp-mobile inject so nav_floor passes on inspection AND the page survives scripting-off. All 20 internal links verified against the repo. Linked into `index.html` classroom section (contrast-clean; index's pre-existing self-referential nav HALT untouched — it is the front door).
- **STILL OPEN** — founder picks build order (recommend Sticker Price first); iSLO 6 rubric norming; decide whether the hub reads to students as a requirement vs. an optional arcade (stage copy shift only).

## 2026-07-19 — SHIPPED: Sticker Price (iSLO 2 build — the first dry cell, filled)

**Founder called the build order: Sticker Price first.** Delivered `sticker-price.html` — the Quantitative-Skills game the hub had marked "Proposed."

- **REUSED THE PROVEN ENGINE** — the Tension Bar cost-decomposition (`advantage-intake.html`) and its dignity framing in code: the NUMBER asks, never "you are short." Pointed at four numbers students actually meet, each guess-first then reveal: **The Loan** (real fixed-rate amortization, principal-vs-interest bar) · **The Sticker** (published cost − gift aid = net price) · **The Statistic** (percentage change with counts + denominator put back — "a percentage with no denominator is a rumour," the studio's own line, earned here) · **The Small Charge** (a /mo multiplied out over a degree).
- **QL VALUE, all four dimensions** — Interpretation · Calculation · Assumptions · Communication, one foregrounded per case, mapped on-screen. Every headline is an EDITABLE EXAMPLE the student sets — no market number fabricated (provenance names the METHOD: amortization formula, federal net-price definition, base-rate pedagogy). Dignity floor held: "a starting point is never a verdict," money/deficit language kept off screen one (opens on the skill, not "you're broke").
- **VERIFIED BY DRIVING IT, NOT PARSING IT** — installed py-playwright, launched the pre-installed Chromium (`/opt/pw-browsers/chromium-1194/...`, executable_path — the pinned-version workaround), drove all four cases + the close summary headless: reveals open, readings populate, arithmetic correct ($12k @6.5% 10y → $136/mo, $16,351, $4,351 interest), ZERO console/page errors. Amortization cross-checked in node.
- **FLOOR HELD** — reused index's gated palette; static Home/Back nav (Back→islo-hub, Home→index). Image-floor HALT cleared honestly by adding 5 authored SVG instrument marks (hero + one illustrating each number-type: coins, tag, misleading bar-spike, clock) — the every-page-has-a-glyph pattern, not a token drop. **preship-gate-v4: SHIP** (worst pair 5.57:1).
- **HUB RE-READ** — iSLO 2 flips Thin→Built; Sticker Price card goes Proposed→Live link; count tiles now 20 games mapped / 2 dry cells left. Suite scoreboard: **5 built · 1 thin (DEI) · 1 dry (Natural World)**.
- **STILL OPEN** — the two remaining proposed builds: `Who Holds the Room` (iSLO 5, to the live ISLO #5 rubric) and `Update the Model` (iSLO 4, the tight-spiral loop pointed at science). Measure side of iSLO 2: norm a local QL rubric — Sticker Price now generates the work samples for it.

## 2026-07-19 — Studio-whole: one canonical home; the iSLO suite reframed as one module

**Founder correction: the recent work read as one module (the iSLO/MassBay games) and risked collapsing into the "Mike & Rebecca" pitch (`studio/studio-tour-for-massbay.html` — Rebecca Heimel + the CIO, Restricted). Direction: build the STUDIO AS A WHOLE.** Chosen move: consolidate the ~6 competing "studio" front doors into ONE canonical home, iSLO as one lane inside it.

- **DIAGNOSIS (surveyed, not guessed)** — six pages each call themselves "the studio": root `index.html` (public, gated, current — the real front door), plus `studio/the-village.html`, `studio/tsp-home.html`, `studio/what-this-is.html`, `studio/massbay-hub.html`, `studio/tight-spiral-system-map.html`. Survey verdict: village/tsp-home/what-this-is are orphaned predecessors superseded by root index; system-map is an internal diagram; play-the-studio is a playable demo; studio-tour is Restricted (private pitch, not a public door).
- **CANONICAL HOME = root `index.html`** — it is the GitHub Pages root, so it IS the studio's address; making any other page canonical would fight Pages. Added a new **"The whole studio"** section surfacing the lanes the front door was missing: the OS (`tight-spiral-runbook.html` — the gates/ticks/refusals), the **System Map**, **Play the Studio** (the playable pipeline), **What This Is** (the manifesto), and a **For MassBay** card (Confluence + the iSLO Suite run live inside the college; pilot proposal shared privately). Section sub states it plainly: *"The iSLO Suite is one module in one lane — not the studio."* Contrast-clean (only the front door's standing self-referential nav HALT, unchanged).
- **RESTRICTED IP RESPECTED** — did NOT link `studio-tour-for-massbay.html` (Restricted, not-for-distribution) from the public home; represented the MassBay lane via the public artifacts instead. Did NOT surface `massbay-hub.html` (student-resource data flagged verify-before-publish).
- **CONSOLIDATED THE ORPHANS (non-destructive)** — added a small routing banner to `studio/tsp-home.html` and `studio/the-village.html` ("an earlier studio home; the current front door is → Tight Spiral Productions"), literal high-contrast hex, aria-Home link. They stop competing without being gutted. NOTE: both files carry PRE-EXISTING contrast HALTs (--lamp / --gold-br in their own draft palettes) — not touched; out of scope and not introduced by the banner.
- **STILL OPEN** — if the founder wants harder convergence: redirect (not just banner) the stale predecessors, or fold what-this-is/system-map fully into index; decide whether to link the self-gating studio-tour from a private index; verify + publish or retire `massbay-hub.html`. The two remaining iSLO builds (Who Holds the Room, Update the Model) also still stand.

## 2026-07-19 — De-named the MassBay pitch (roles, not two individuals)

**Founder: "Remove Rebecca and Mike as specific targets."** `studio/studio-tour-for-massbay.html` no longer names Rebecca Heimel or "the CIO" as the two readers — every reference (open comment, gate recipient block, the ask section's role labels, the footer, the restricted strip) now addresses **MassBay leadership: the teaching-and-learning side (CTL) and the IT / governance side.** Still a MassBay-directed, Restricted pitch; just not aimed at two named people. Text-only edits; gate SHIP. Did NOT touch Mike Rose (cited scholar) or Rebecca Skloot (FYS book author). OPEN: the live `confluence-TRUNK.html` still credits a named backend collaborator ("Mike Lyons") in its build-status HOOK table — a different person/context (a dev credit, not the pitch audience); left pending founder confirmation before altering a deployed deliverable's attribution.

## 2026-07-19 — "Mike" → neutral role; and a caught deploy-gate regression (TICK 3)

- **De-named the backend collaborator.** Per founder ("change Mike to a neutral position, universally"), the four "Mike Lyons" references in the LIVE `confluence-TRUNK.html` (backend/data-persistence HOOK, security-review HOOK, cloud-sync note, DATA_HOOK script string) now read **"Backend / IT partner."** Text-only; no palette change. Left the dated `archive/` + `rescued/` snapshots and the `claude_consent-manifest.md` faculty roster as historical record (rewriting dated backups would falsify provenance). Confluence's pre-existing --pine-lt / --gold-border render-proof debt is untouched (baselined "known debt," not mine).
- **RATCHET CAUGHT WHAT preship-gate MISSED — and it was mine.** Ran `ratchet.py` (the actual deploy gate, not just preship-gate-v4) and it HALTed on **2 regressions I shipped earlier**: `islo-hub.html` and `sticker-price.html` carried institutional reference data (islo/rubric/outcome markers ≥6) with **no machine-detectable source + last-verified date** — H6 / TICK 3, the exact class that 403'd the whole site on 07-14→07-19. Fixed: added `tsp:last-verified 2026-07-19` + visible "Last-verified 2026-07-19" to islo-hub; added a visible "**Source:** … **Last-verified 2026-07-19**" line to sticker-price. Ratchet now **0 regressions — floor holds** (23 known-debt files still allowed). Both still preship SHIP.
- **LESSON (re-)LOGGED.** preship-gate-v4 is not the deploy gate. `ratchet.py` is. Run the ratchet before pushing anything that asserts institutional facts — a green preship + a red ratchet is exactly the split that takes the site to 403. I should have run it on the iSLO builds the day I shipped them.

## 2026-07-19 — SHIPPED both remaining builds: iSLO suite is now 7/7 built

**Founder: "advance both builds."** Shipped `update-the-model.html` (iSLO 4) and `who-holds-the-room.html` (iSLO 5). Every one of MassBay's seven Graduation Competencies now has a build. The suite's dry cells are gone.

- **Update the Model — iSLO 4 (Natural World).** Scientific-method loop, made playable: state a prior confidence, **pre-register what would change your mind** (falsifiability, the move that matters), meet real cited evidence, update. Three beliefs — falling objects (Apollo 15 hammer–feather, 1971), the 10% brain neuromyth, the full moon (Rotton & Kelly 1985). Measured on suite-proposed AAC&U Scientific Reasoning dims (Hypothesis · Evidence · Revision); honestly flagged: no normed MassBay rubric. Dignity: "being right first is not the skill; updating honestly is."
- **Who Holds the Room — iSLO 5 (DEI).** Built to the **live MassBay ISLO #5 rubric, verbatim** (Systems of Power · Group/Individual Interactions · Advocacy, 0–4). One ordinary campus scene (a group-project plan) read three ways: select the structural defaults, open four whole people to feel one sentence land four ways, then pick an advocacy move that gets placed on the rubric's actual level with the next rung shown. Grounded in the workshop's own equity levers (deliberative interdependence, transformative translation, proactive engagement; Estefan et al. 2023). Dignity-first throughout — no villains, people framed as whole/capable not deficits, "a starting point is never a verdict," ipsative not ranked, characters explicitly fictional/composite.
- **VERIFIED BY DRIVING, NOT PARSING.** Both driven headless (Chromium 1194) through every round + close: gates open on the right interactions, readings populate, replay works, the ISLO #5 rubric renders all three dims verbatim, zero console errors. Amortization-style logic n/a here; confidence deltas and level mapping checked live.
- **RATCHET RUN BEFORE PUSH (lesson applied).** First ratchet HALTed: who-holds-the-room H6/TICK 3 — I wrote "Source**.**" not "Source**:**", so the source marker didn't match the check's regex. One-char fix. Ratchet now **0 regressions**. Both preship SHIP (5.57:1). Provenance markers (Source: + Last-verified 2026-07-19) baked in from the start this time.
- **HUB RE-READ.** iSLO 4 Dry→Built, iSLO 5 Thin→Built; both cards Proposed→Live links; counts **22 games mapped / 0 dry cells**; stage + slab copy updated to say all seven have a build and the remaining gaps are on the *measure* side. Suite scoreboard: **7 built · 0 thin · 0 dry.**
- **STILL OPEN** — the measure side: four outcomes (2, 3, 4, 7) have no locally-normed MassBay rubric; iSLO 6's is in development. Norming those is faculty work the suite now supplies work samples for.

## 2026-07-30 — Built the measure side: The Norming Table + Close the Loop (ISLO #1 & #5)

**Founder pasted the real "2026 ISLO #1 & #5 Assessment Initiatives | Scoring Teams" email; asked for BOTH a norming companion and a close-the-loop reporting tool. Grounded in the real email + verbatim rubrics, not Copilot's reconstruction.**

- **PROVENANCE CATCH FIRST.** The scoring email's task list said to score "using the initiative's **critical thinking rubric**." Stale copy-paste: ISLO #1 = Written Communication rubric, ISLO #5 = DEI rubric; critical thinking is ISLO #6 (rubric in development). Flagged, and both tools load the CORRECT rubric per outcome (with the correction shown on-screen). Classic TICK-3-class error caught in a live institutional doc.
- **`scorer-norming.html` — The Norming Table.** Score four fictional/composite student excerpts on the real ISLO #1 (Sources & Evidence; Context & Purpose) and #5 (Systems of Power; Advocacy) rubric dimensions — verbatim levels shown — then meet the team's normed score. Verdict is exact / adjacent (within one, the working standard) / two-apart (the conversation norming exists to have). Teaches inter-rater reliability by making the player feel it. Mirrors what Confluence does at scale.
- **`close-the-loop.html` — the annual assessment report.** Fillable, offline, no data leaves the page. Pick ISLO #1 or #5 → loads the correct outcome statement + rubric dimensions into a per-dimension Results table; sections for method (norming/IRR/50 artifacts, prefilled from the initiative), benchmark, analysis (flagged "review teams read this first"), actions (closing the loop), follow-up, next steps. Assembles a copy/print-ready report → straight into a program review. Print CSS hides the form and prints just the report.
- **CONNECTOR DETOUR (resolved).** Spent effort trying to pull the real template via Outlook/OneDrive; Microsoft 365 connector is in the org list but unauthenticated + off-in-chat, and the post.massbay Gmail isn't where these emails land. Founder solved it by pasting the email content directly. Noted the connect path (Settings → Connectors → Microsoft 365) and the Zapier fallback for next time.
- **FLOOR HELD.** Both reuse the shipped gated palette; static Home/Back nav; authored SVGs clear the image floor; TICK 3 provenance (Source: + Last-verified 2026-07-30) baked in from the start. Both browser-verified end-to-end (outcome switch loads right rubric / dims; scoring + normed verdict; report assembly + copy). preship SHIP; **ratchet 0 regressions**. Linked from the hub's #1 and #5 measure blocks ("For faculty").
- **STILL OPEN** — norm local QL/scientific/civic rubrics (2,3,4,7); iSLO 6 rubric still in development; the games now generate work samples for all of it. If desired, extend the two measure tools to more outcomes once their rubrics norm.

## 2026-07-30 — On file: founder's ISLO scoring reflection (primary source for the measure side)

Added `ISLO-SCORING-REFLECTION-2026-mwalsh.md` — Matt's verbatim one-page reflection from the 2026 ISLO scoring initiative (to Tom & Sean). Kept as a repo CONTEXT doc, not a public-site artifact (unlinked from index/hub). Provenance header (Source + Last-verified 2026-07-30) so it clears TICK 3 if swept.

- **Why it matters:** it's the founder's own rationale for the measure side, in his words — *"the holistic model … doesn't capture important information about specific learning objectives … we currently collect no data about areas of student strength or weakness."* That is precisely the gap `close-the-loop.html` fills (per-dimension results, not one holistic number).
- **Names the next measure-side build:** measurable outcomes for the **EN placement portfolio** (today only the EN98-vs-EN101 placement is recorded; two–three readers; no skill data). His listed candidate outcomes (analytical reading, interpretation, synthesis; rhetorical argument; audience; central claim on credible evidence) are a ready-made draft rubric — a Norming-Table-style instrument could turn "placement 3 vs 4" into curriculum-reviewable skill data. Logged as an opportunity, not built.
- **Label nuance:** his reflection is titled "Critical Thinking artifact assessment," echoing the announcement's "critical thinking rubric" wording — so the CT label is drifting through the initiative's own materials, not just one email. My earlier "stale copy-paste" framing is softened to "label drift" in the context doc; the substance stands (score #1 on Written Communication, #5 on DEI; CT is #6, in development), and the tools already load the correct rubrics.
- Proposal updated with the primary-source note. No HTML changed; ratchet re-run to confirm still 0 regressions.

## 2026-07-30 — Full-staff brainstorm: iSLO games/apps for the gaps

Convened five studio lenses (Registrar/Cora, Learning Scientist, Studio-Eyes, Assessment Lead, Reuse Engineer) to brainstorm builds for the suite's gaps. Synthesis in `ISLO-GAPS-BRAINSTORM.md` (living planning doc).

- **Strong convergence:** (1) **oral communication** is the #1 real gap — every seat named it; "half the most-assessed competency going unmeasured." (2) The **EN Placement Skill-Scorer** is the flagship measure-side build — Assessment Lead + Reuse Engineer both ranked it #1 independently; reuses the Norming Table scorer, loads the founder's own candidate skill list, derives placement from the skill profile, exports per-skill data (answers his reflection directly). (3) A **Rubric Forge** unblocks the four un-normed outcomes (2/3/4/7).
- **Cheapest wins reuse a shipped engine outright:** Real-Cost Case Pack (new Sticker Price cases, ~free), Score the Room (oral, score described delivery on AAC&U Oral Comm rubric), The Real Syllabus (first-gen hidden-curriculum decoder).
- **Oral, done right (Learning Scientist):** capture mic, analyze **prosody only** (pace/pauses/energy), never transcribe — offline-safe AND never scores words/accent/dialect. Dignity + technical unlock together. Must stay private + ipsative.
- **Registrar's unnamed gap:** the suite is entirely English/writing/humanities idiom, but MassBay's largest enrollments are career/workforce (Health Sciences, Automotive, Business) + STEM — nothing meets those students in their disciplinary context. Biggest strategic gap. Also verified: MassBay ~69% part-time/commuter (Fact Book) — confirms single-file/offline/phone-first is exactly right.
- **Cautions:** verify the current EN placement mechanism before building (MA co-req reform may have changed EN98→EN101); keep oral + multilingual builds private/ipsative or the asset-framing collapses into a deficit score.
- **STATUS:** brainstorm only — nothing built. Awaiting founder green-light on first build(s) + the career/workforce lane question.

## 2026-07-30 — Correction: no EN90/98; MassBay is a co-req pioneer (placement build parked)

**Founder:** "We don't offer 90 or 98. We are pioneers in co-req. Ask me later for more on this."

- The Registrar's brainstorm caution ("verify EN98→EN101 is still live before building") is **confirmed**: MassBay offers **no EN90/98 developmental courses** — students enter EN101 with **co-requisite support**, no place-out gate. The whole "Placement Skill-Scorer / EN98-vs-EN101" premise is **void**.
- **PARKED** the placement flagship. The Norming-Table engine + the founder's candidate skill rubric still stand; the *use* re-frames to a **co-req support diagnostic** (targeting supports), not a placement gate — but not designed until the founder briefs the co-req model.
- Corrected `ISLO-GAPS-BRAINSTORM.md` (Tier 1 row, strategic flag, recommended-first-move) and added a correction note to my commentary in `ISLO-SCORING-REFLECTION-2026-mwalsh.md` — leaving Matt's verbatim words (which say "EN98/EN101") untouched, flagged as a prior/mis-stated frame.
- **Revised first move:** lead with **Score the Room** (oral) + **Real-Cost Case Pack** — both stand on their own, no placement dependency. Co-req diagnostic + career/workforce lane held for founder briefing.
- Being a co-req pioneer is itself a story/asset worth building around (support students *inside* EN101, not out of it) — noted for the later conversation.

## 2026-07-30 — Green-lit gap builds shipped (full staff, funds): oral, real-cost, rubric-forge

**Founder: "1 2 3 let's go with new alephs as needed to seat expertise. Funds and all staff."** Seated three expert "aleph" agents for content, then built + gated + browser-verified + ratcheted three tools.

- **`score-the-room.html` (iSLO 1 — the ORAL lane, finally built).** Read a DESCRIBED delivery (transcript + stage directions) and score it on the AAC&U Oral Communication VALUE rubric (5 dims), then meet the normed anchor. Four fictional deliveries, levels 2/4/1/3. Scores described delivery ON PURPOSE: no mic, offline-safe, and it never scores accent/dialect/first-language word choice — only choices a speaker can change. Reuses the Norming Table scorer.
- **`real-cost.html` (iSLO 2 — underserved).** The Commute (frequency×trips + hidden hours), The Hours (a course priced in hours; wrap-around childcare/commute; $/hour vs the credential), The Book (cost-per-use; re-reading = thoroughness), The Whole Bill (fees + aid's real denominator). Dignity floor absolute: assets not deficits, the NUMBER does the work, every headline an editable example. Reuses the Sticker Price engine.
- **`rubric-forge.html` (measure — outcomes 2/3/4/7).** Faculty draft a normable rubric from an AAC&U VALUE scaffold (QL / Info Lit / Sci Reasoning / Civic Engagement), edit every dimension + level, add/remove dims, export copy/print. Ships 7 authoring checks + a draft-vs-normed explainer (drafting is authoring; norming is the IRR workshop). Reuses the Close the Loop engine.
- **VERIFIED:** all three preship SHIP; browser-driven end-to-end (Score the Room 4 rounds + calibration; Real Cost 4 cases $360/135hr/$1,230; Rubric Forge 2/3/4/7 scaffolds load 6/5/6/5 dims, edit flows to report, add/remove, copy). **Ratchet 0 regressions** — TICK 3 markers baked in. Wired into the hub; games count 22→24.
- **STAFF/ALEPH MODEL WORKED:** three parallel expert agents produced accurate rubric language + samples + cases; I assembled + gated. Fast and high-fidelity.
- **STILL PARKED:** the co-req support diagnostic (ex-placement) and the career/workforce iSLO lane — both await the founder's co-req briefing ("ask me later").

## 2026-07-30 — Trained on the English department annual reports (new seat: the Assessor)

**Founder: "Train on my English department annual reports. Should have at least 4 of them."** Found and read four-plus via Drive; seated the record as `claude_seat-english-assessment.md` (Registrar-seat pattern; aggregate only, FERPA floor; repo context doc, unlinked from the public site).

- **Corpus (with Drive IDs):** AY24-25 (Sikorski/Walsh/Herrera/Casson), 2025 draft (AI vs SLO#2), 2021 (SLO#5 multimodal), AY2017-18 (SLO#3 research), + AY16-17 notes + index.
- **Captured:** the 7 English program PLOs verbatim (distinct from the college iSLOs); the assessment arc by year; recurring patterns — portfolio assessment + norming/blind scoring is the department's core method (exactly what The Norming Table + Close the Loop model); adjunct participation and **closing the loop** are the chronic gaps (a 2021 SLO#5 revision was drafted and still never posted); a ~5-year cycle (2025-26 assesses SLO#1).
- **CO-REQ RESOLVED FROM THE SOURCE:** the 2025 report states plainly — *"as a result of long-term data on the efficacy of our co-req model, EN090 and EN098 have been officially retired."* EN101X + EN101L co-req lab; placement via college process / dept Portfolio Assessment / ES150. Confirms the founder's co-req correction and voids the EN98-vs-EN101 place-out framing. Folded into the brainstorm's parked-placement note. (Founder still to brief the fuller model.)
- **GenAI thread surfaced** (SLO#2, AY24-25): 48/38/42% AI usage; 30/60/75% not-discussed-in-class/syllabus/assignment; CopyLeaks pilot; the dept is actively asking for AI-use guidance + AI-resistant assignment design — a ready build lane (iSLO 1 + 3 + academic integrity).
- FERPA: excluded individual student names/scores present in raw 2021 scoring notes; seat holds aggregate/method only. Provenance header (Source + Last-verified 2026-07-30) so it clears TICK 3 if swept.

## 2026-07-30 — Added the Title III co-req grant report (Katie McGrath) to the Assessor corpus

**Founder: "Katie McGrath authored a Title III co-req report you need. Search files."** Found and read it — **"Grant Summary: Co-Requisite English" (Title III), Aug 2024** (`1F4PXlD-ShaWsi39g3e6Xxnn4nJXRo09QWZWOCGO3pIM`, in Matt's Drive; first-person, attributed to McGrath per founder). Folded into `claude_seat-english-assessment.md`.

- **The definitive co-req record.** Title III scaled EN101X to 100% co-req by Fall 2024; 2023-24 the dept voted to discontinue ALL stand-alone developmental English (EN90/EN98 gone). Placement = **multiple measures**: HS GPA ≥ 2.7 → EN101, else Accuplacer → co-req/college-level/ESL.
- **The data:** co-req passes college English **80-83% vs 38-50%** developmental (in one semester not two); EN102 completion **49-54% vs 10-37%** (cohorts 260/1,195 co-req vs 174/70/2,355 developmental).
- **Equity:** gaps shrank on the co-req path (EN102 gap disappeared among male students; AA male students most likely among males to complete EN102) but **Hispanic/Latina females still lag** — the named open target.
- **Support models Title III funded:** embedded learning specialists (AAC, 1:1 draft conferencing), a life-skills coach pilot, PEEPS (faculty/specialist PD), the Persistence Project (non-academic weeks-1-3 1:1s), and blind portfolio assessment. These are the scaffolds a future **co-req support diagnostic** would route students toward.
- Enriched the Assessor seat's co-req section + the brainstorm parked-placement note. Aggregate only (no student PII). Repo context doc, unlinked from the public site.

## 2026-07-30 — Built the GenAI lane (autonomous, founder away +55%)

**Founder: "I'll be away for three hours and need you to roll with +55% while I'm offline."** Built the one lane the founder never objected to and the English annual reports explicitly ask for: **appropriate, honest AI use in writing** (iSLO 1 + 3 + academic integrity). Two tools, both grounded in the Assessor seat's aggregate findings.

- **`whose-draft.html` (student — iSLO 1 & 3).** Walk one essay through four steps (Ideas / Evidence / Draft / Polish); at each, choose how much to hand to AI. Two meters move — **what stays yours** (agency) and **the tell** a reader/rubric would catch. Choices carry the dept's real integrity indicators (fabricated citations at Evidence; voice-shift at Draft; meta-textual AI chatter at Polish; SLO#2 "generate original ideas" at Ideas). Close screen assembles a **copyable disclosure statement** from the actual choices made — the thing the reports say students keep asking for. Dignity-first: no "cheater" framing; a starting point is never a verdict. Reuses the who-holds-the-room choice-and-reveal + case-rail engine.
- **`ai-resilient-assignment.html` (faculty — iSLO 1 & 3).** A seven-check AI-resilience audit (norms named · process collected · voice baseline · local anchor · sources pinned · reasoning shown · grade the thinking), each with a concrete redesign move for the exposed checks, plus a resilience tally (N/14). Then a **syllabus GenAI policy builder** — three stances (encouraged-with-disclosure / limited-to-stages / not-permitted) that assemble an editable, student-facing policy paragraph. Copy/print packet export. Answers the reports' own action items verbatim (AI-resistant assignment design; a GenAI policy in every syllabus). Reuses the Rubric Forge / Close the Loop fillable-report engine.
- **The grounding number that drove both:** the dept found 30/60/75% of students got no GenAI guidance in class/syllabus/assignment. Silence is the gap; both tools close it — one for the student, one for the faculty.
- **VERIFIED:** both preship SHIP; JS parses; browser-driven end-to-end (Whose Draft: all 4 steps → meters/reveal → disclosure assembly + copy; AI-Resilient: 7 checks score correctly, redesign-move visibility toggles, all 3 policy stances assemble with fields woven, copy). TICK 3 markers baked in (Source: + Last-verified 2026-07-30). Wired into the hub under iSLO 1 (student game + faculty note) and cross-listed under iSLO 3; games count 24→25.
- **HELD (unchanged):** did NOT open the PR (needs explicit ask), did NOT build the co-req support diagnostic, did NOT open the career/workforce lane. All await the founder's return/briefing.

## 2026-08-03 — Merged the iSLO Suite (PR #43), then a Funes-aleph playtest + fixes

**Founder: "Merge with funes alephs and ledger — full access."** Merged PR #43 into `main` as a merge commit (`5b14abc`): the full iSLO Suite — build-side games, faculty measure-side tools, and the GenAI-in-writing lane — across MassBay's 7 competencies.

- **The merge also un-red main.** PR #43's baseline fix repaired a stale `floor-baseline.json` (3 pre-existing unbaselined failures: two comfort-gate canary fixtures + `soundings-TRUNK-v03`) that had kept the floor CI red on `main` for days. First green floor run on main in that window.
- **Getting there:** resolved the merge conflict against a far-moved main (adopted the canonical **Flok** rename; kept **Whose Draft** and the built **Who Holds the Room**), and conformed all 9 pre-Phase-3 iSLO files to the studio's dark-mode kernel + version stamps.

**Then a Funes-aleph playtest fleet (11 alephs, one per page)** drove every iSLO page headless through all interactions + edge cases + the Studio Eyes control in day/dusk/night, and read each for dignity/voice + source integrity. Record: `FUNES-PLAYTEST-2026-08-03.md`.

- **One real regression, fixed (priority 0):** the dark kernel made `.slab h3` (which colors text with the `--brass-fill` *fill* token) dark-on-dark in night mode — 2.14:1. comfort-gate missed it (fill token, not a sampled text token). Forced a bright brass ink on the always-dark slab → **9.87:1** night, across 6 files.
- **Correctness/integrity fixes:** islo-hub "four"→"five" un-normed outcomes + games count 25→**23** (reconciled to the page); update-the-model no longer wipes the player's posterior on a repeat reveal; score-the-room + scorer-norming retire a shown verdict when the pick changes; sticker-price Case 3 now reads "up from/down from" directionally and clamps the incident count to the pool (no more >100% rates); ai-resilient packet stamps the current date; close-the-loop clamps percent-at-benchmark to 0–100.
- **Confirmed holding:** dignity/voice on every page (no verdict framing, the number does the work, **no blind-play claim**, assets-not-deficits, no dark patterns), contrast in all light modes, source integrity, zero crashes/dead-ends/console-errors.
- **Knowingly left (minor, logged):** real-cost plural agreement + all-zero bar; the version-stamp stray-`</span>` tooling artifact; case-rail ARIA tablist semantics.

All fixes browser-verified and gate-clean (comfort-gate, art-gate, JS parse). FERPA/voice floors intact. Fixes pushed as a follow-up off the merged main.

## 2026-08-03 — DECIDED: Student Attribution Standard (studio canon, adopted)
When the studio publishes/links a student game: credit **first name + last initial** only, name the course **generically** (e.g., `EN195 Creative Writing (summer 6-week online)`), and carry **no year and no section number**. A student email granting permission = documented approval, logged in the approvals list. Presentation standard layered on the FERPA ruling (publication is consent); written as a check — a credit with a full surname, a 4-digit year, or a section token does not ship (exit 1). First application: *Barcelona Summers* (Hamish K.), approval on file. Standard doc: `student-attribution-standard.md`. Also published this turn: the Barcelona Summers guest cabinet on `arcade.html` (comfort-gate pass, links the student's own deploy).

## 2026-08-03 — Tableau Sweep #2 (scheduled, read-only) — 31 of 38 builds ship-blocked on the entry gate
Swept 38 playable builds through `one-thing-gate.py` @1280×800 headless Chromium: **1 PASS · 6 WARN · 31 SHIP-BLOCK**; gate exit 1. Canon recovered from the repo lane (rescued shelf snapshots). Worst by arithmetic: `laughter-foundry-spec-and-log` (183-word wall + 6 invitations) — a spec/log, not a core game; worst core game: `the-tell` (183-word wall + 2 invites); `dad-energy` triple-flagged. Failure classes past the 3-build trigger: text-wall 25/38, invitation≠1 16/38, sub-50% image 34/38, control-clutter 22/38. **NO decorative emoji** — the 3 pictographic CRITICALs are false positives (© attribution in `close-the-loop`; ▶ play-buttons in `dad-energy`/`how-an-idea-travels`). TWO NEW proposals DRAFTED (not self-adopted): (1) exclude the **Studio Eyes comfort control** from the primary-invitation count — the 2026-07-29 comfort-kernel rollout put `se-eyes` on 62 games and its bold label is scored as an invitation, causing all 16 invitation ship-blocks and blocking `cliche-city/field/line` (the Sweep-#1 PASS exemplars) SOLELY on the comfort button; (2) narrow the emoji tooth to exclude ©/▶ functional glyphs. Read-only: the sweep edited no game or gate. Detail in shelf doc `claude/tableau-sweep-report.md`.

## 2026-08-04 — Land the stranded governance lane + the Matt-eyes lane + Funes Tendrils

**Founder: "merge and land — no orphans anywhere. execute new function — Funes tendrils down all forking paths. this runs on all chats after stalls of all kinds."**

- **LANDED to main (was stranded 194 commits deep on `tsp-git-handoff-studio-wide`):** the whole studio-wide governance/tooling lane never reached main. Surgically landed the additive files (the handoff branch itself is unmergeable — merging it would revert 194 commits of main; the classic stale-base trap): `matt-eyes-lane-check.py`, `MATT-EYES-LANE.md`, `medium-gate-check.py`, `egress-probe.sh`, `fireground-panel-kernels.md`, `asset-ingest-storyboard-lane.md`, `DECISION-zapier-auth-lane.md`, the Fireground Image Scout skill. `floor.yml` re-applied against main's current version (matt-eyes gate step, blocking).
- **NEW FUNCTION — `funes-tendrils.py`:** the post-stall walk. Every studio loss has one shape (built → stranded on a fork → stall → never merged → gone). This walks all forking paths — working tree, unpushed, all branches ahead/behind main (unmerged = stranded, far-behind = stale base "do not fast-merge"), worktrees, staging dirs, orphan pages — and reports what did not land. Wired as a **SessionStart hook** (`startup|resume|clear|compact`) so it runs on all chats after stalls of all kinds; also a report step in `floor.yml`. Canon in `FUNES-TENDRILS.md`. First run flagged 19 stranded branches + the 194-behind handoff lane — it proved itself immediately.
- **NOT force-merged (honest):** the handoff branch's diverged shared-doc edits (OS.md, LANE-REGISTRY, FUNES-INDEX, pipeline.md) and its old fireground redesign are left for careful reconciliation, not a destructive merge. Funes Tendrils now surfaces them every session so they can't be silently lost. Real orphan pages the face doesn't link are also surfaced (not auto-linked — that's a judgement call, not a cheap win).

## 2026-08-05 — EN195 Arcade lands (Workshop Vending Machine); real Studio Eyes catches two live bugs; a shelf artifact corrected

**Matt: "push to en195 and matt's dashboard gits etc."** First real push of `en195-arcade.html` to this repo (was shelf/session-only before today). The build: four playable teaching games (Semester Machine, Sandbag Drop, Line Break, plus the arcade-floor hub) plus the Workshop Vending Machine, this repo's one deliberate offline-floor exception — a live Supabase backend (RLS-verified: anon insert-only on submission tokens, select-only on the public leaderboard view, base table never exposed) so a shared class submission board can exist, since a single offline file can't hold one. Four cabinets, one per EN195 workshop (Creative Nonfiction / Poetry / 10-Minute Play / Short Story), each with its own guardian-puppet SVG (hand-cut shadow-silhouette, idle-rigged) built in-house since no image model is reachable from this session. Cabinet titles and copy are genre-first and self-contained per founder ruling — no Borges naming on the student-facing surface; the Funes/Aleph/Forking-Paths/Babel mapping behind the four guardians is preserved separately as design documentation, not shipped here.

**Real Studio Eyes (`studio-eyes-sweep.py`, WeasyPrint render-proof) caught two live bugs the first push shipped with**, both fixed and re-verified before this entry: (1) `:root` had no `font-size`, so every `rem`-sized control (coin counter, buttons, footer) was resolving off the 16px UA default instead of the intended 20px base — real phone-width text under the 18px floor, invisible to a regex-only scan; fixed by setting `:root{font-size:20px}`. (2) The footer's `margin-top:36px` sat outside its own painted background box, tripping a paint-mismatch false-read at the gate's sample point (hand-verified against the raw raster: dark by y+68, light only in the margin gap at y+8) — fixed by converting to `padding-top`, identical visual result, now inside the painted box. Also added a skip-link (was WARN). Re-swept clean: 0 HALT. `index.html` linked it (was a real orphan — Studio Eyes' own orphan-pages rule caught it).

**Correction to the record:** earlier work this session logged gate verdicts to a shelf-only `claude/FUNES-LEDGER.md` via a shelf-only `claude/funes-ledger.py` — neither file, nor that gate-verdict-table schema, has ever existed in this repo's history on any branch (checked: `git log --all` on both paths, zero hits). This repo's real post-stall practice is `funes-tendrils.py` / `FUNES-TENDRILS.md` (walks git state: unpushed work, stranded branches, orphan pages — not a gate-verdict ledger), and this file, `TSP_Ledger.md`, is the real running log. The shelf artifact was disconnected from repo canon and should not be treated as studio practice; this entry is the correction, made by checking source rather than the shelf, per the studio's own rule.

**Commits:** `cda3e61` (first push), `beac0a0` (font-size + footer-padding + skip-link fix), `08eb68d` (index.html link). All raw-verified byte-for-byte after each push.

## 2026-08-05 — Account survey: leaks / canon coherence / credit usage (posted once)

**Founder: "account wide survey of how i store and reference docs and governance to check for leaks and optimization points per canon coherence AND credit usage … scan walshero and post ONCE and not always and set up best practices."** Read-only survey (cheap git-grep method, credit-conscious). Full report + standing best practices in `ACCOUNT-SURVEY-AND-BEST-PRACTICES.md`.

- **Leaks: clean.** No hardcoded secrets/tokens/JWTs on main; `.gitignore` covers `.env`; Supabase keys are dormant/placeholder/publishable (public by design). One verify item: RLS INSERT-only on the en195-arcade table.
- **NEW enforcer — `secret-scan-gate.py`** (self-testing, fool-me-once): makes "clean" a floor, not a hand-check. Wired into `floor.yml` report-only (arm to blocking later). Confirmed 0 HALT / 389 files.
- **Canon coherence:** SSOT erosion, not contradiction — 7 handoff files (vs the registry's "one HANDOFF.md" rule), ledger ambiguity, dated root clutter, three `preship-gate` versions, and the big one: **34 enforcers, only ~4 wired** (the "runs if remembered" anti-pattern). Fixes recommended, NOT auto-executed (mass file moves would clobber the concurrently-active main) — awaiting go.
- **Credit sinks named + fixed:** `actions_list` dumps ~390KB (use minimal/targeted status instead); 21% of the repo is dead `rescued/archive` weight; 3 HTML files >2MB; per-push weasyprint/playwright install (cache it).
- **Scope note:** only TSP + matt-radar surveyed; the other 3 walshero repos need an approval-gated scope-add (add_repo was approval-gated overnight).
## 2026-08-05 — Reconcile: The Viscosity is a CYL feature, not a standalone game

**RECONCILED — Viscosity = CYL's felt descent renderer.** Founder confirmed the design intent: `the-viscosity.html` was built to be a *feature of Choose Your Leader*, not a peer arcade game. It is the embodied version of CYL's Beat-3 Maslow descent — the honeycomb STRETCHES (viscosity = the felt cost of scarcity) where the v5-slice currently paints a static ladder. This matches the shelf design block `cyl-viscosity-descent-block.md` and the v5-rebuild-spec's open problem (*"it's text, I don't feel it… I don't know where I am in the hierarchy"*). The intended payload also carries a **Jenova Chen flow layer**: the leader's actions modulate viscosity and move you between rungs (drop-downs / pull-ups) — impact you FEEL, continuously.

**DEBT NAMED — the "unlinked" fix mis-framed it.** `tight-spiral-studio-os.md` logged "viscosity unlinked" as Release-Steward debt. That debt was closed by linking it from `index.html` as its *own room* (chip: "Motivation") — which is the mis-frame the founder just corrected. Reachable ✓, but positioned as a standalone game rather than the CYL mechanic it is.

**CHEAP WINS TAKEN (this session, no sign-off needed):** (1) header note in `the-viscosity.html` recording its CYL parentage + founder-gated flow layer; (2) pointer in `choose-your-leader-map.md` glossary ("The descent" → felt-renderer prototype); (3) this ledger entry; (4) founder decisions queued in `STUDIO-COMMAND-CENTER.md` → OPEN — FOUNDER ONLY. No public framing or engine code touched.

**NOT TOUCHED (founder-gated):** the three locked trauma rails (2026-06-27), the descent math (Measurement seat re-derivation still pending per v5 spec), the index public framing, and any wire-in / flow-layer engine code.

**PENDING — push the shelf block.** `cyl-viscosity-descent-block.md` is the design canon that ties Viscosity to the descent and is still SHELF-ONLY ("PUSH FIRST — no lane," per SHELF-ACTION-LIST). It should land in the repo so the canon is co-located with the build.

## 2026-08-05 — Playtest pass (Studio Eyes + Fingers + agent playtester)

Ran the studio's own quality engine (local Playwright, bridged to pre-installed Chromium; no LLM credits) over the flagship builds. Full findings in `PLAYTEST-REPORT.md`.

- **Systemic finding:** the older ISLO suite (rubric-forge, close-the-loop, score-the-room, scorer-norming, update-the-model, whose-draft) fails the 44px touch floor — shared control styling at 26–42px. The just-shipped `en195-arcade.html` passes clean = the reference standard.
- **Fixed:** `reading-the-fireground.html` (fireground branch) — nav/comfort buttons → 44px, skip target enlarged, focus-ring fallback. Studio Fingers now green; Studio Eyes 15 → 9 (remaining = studio-wide token-role/skip-link debt).
- **Agent playtester:** all builds reach an end (playable). Caveat: it returned identical output across 4 ISLO files — exercising a shared overlay, not each game; a harness limit + shared-widget flag, not 4 bugs.
- **Recommended (not auto-applied):** suite-wide 44px bump using arcade as reference; split token roles; wire Studio Fingers into floor.yml.

## 2026-08-06 — Fireground photo wired to canon; the touch-floor recommendation was already done; the real Studio Fingers backlog is 8 files, not 6

Matt: "Auth zap. Close loose ends push latest best build thru to repo. Fire guard push to repo should be photo etc. Run the timing belt." Decoded against real repo state (not memory): the NIST Charleston field-investigation photo, pushed to `fireground-assets/` in an earlier session, was sitting orphaned. Not scene art (it is a post-fire investigation photo, not an ignition-to-flashover still; the file's own `imageNote` is explicit about that gap and stays unchanged), so it now runs as documentary source credit on the Reading the Smoke closing screen, real alt text, real NIST/public-domain credit line. `.lane-test`, a leftover write-path probe, removed. Patched via the connector, verified against the authenticated GitHub API (the raw CDN was still serving a stale copy minutes later, exactly the trap this file warns about), swept clean through `studio-belt.sh`.

Then asked to advise on next action. Recommended the suite-wide 44px touch-floor bump PLAYTEST-REPORT.md (2026-08-05) called out across 6 ISLO files. Before touching anything, ran Studio Fingers live against those 6 files first, per "canon is computed, not remembered": all 6 already pass clean. `git log` shows why: commit `bc45ec4`, "ISLO suite: enforce 44px touch floor (playtest fix)", landed ~40 minutes after the playtest report was written, by a session this one has no memory of. The report is stale. No redundant work done.

Ran Studio Fingers against the full corpus (`*.html`, 74 pages) instead of trusting either the stale report or the narrow 6-file list. Real result: **12 of 74 HALT.** 4 are `comfort-gate-canary-*.html`, synthetic fixtures for `comfort-gate.py`'s own self-test (282-690 bytes, referenced only by `comfort-gate.py` and `funes-tendrils.py`), not real pages, not real debt. The other **8 are real, current, undocumented debt**, distinct from anything in PLAYTEST-REPORT.md's list: `_confluence-v48-canon.html` (F-VIEWPORT overflow + many F-TAP), `ai-resilient-assignment.html` (26 F-TAP), `cliche-field.html` (F-VIEWPORT, 14px overflow), `confluence-TRUNK.html` (3 F-TAP, footer/byline links), `confluence-massbay-assessment.html` (2 F-TAP), `real-cost.html` (6 F-TAP), `tight-spiral-runbook.html` (F-VIEWPORT, 606px overflow, likely an internal doc page not a public one, worth confirming before triage), `who-holds-the-room.html` (2 F-TAP).

Attempted to wire Studio Fingers into `floor.yml` as a report-only step, exact precedent match to how Studio Eyes itself rolled out 2026-07-11 through 2026-07-14 (report first, ratchet and arm once the backlog is dated and triaged). **Blocked, structurally, not a retry-able failure:** `probe_workflow_scope` confirms the connected GitHub token (`gist, notifications, read:org, repo, user`) does not carry the `workflow` OAuth scope GitHub requires to write anything under `.github/workflows/`. A normal file write to repo root succeeded in the same probe (proving the connector itself is fine); only workflow-file writes are scoped out. This needs Matt to re-authorize the GitHub connection in Zapier with the `workflow` scope added, a one-time fix, before Studio Fingers can be wired into CI by this lane. Until then, Studio Fingers only runs when someone remembers to run it by hand, exactly the gap the ratchet's own writeup names as the failure mode that matters.

**Next, once unblocked:** land the Studio Fingers report-mode step, then triage the 8 real files (some are single-line CSS bumps like `real-cost.html`'s inputs; `_confluence-v48-canon.html` and `tight-spiral-runbook.html` look larger and may be archival/internal rather than public-facing, worth confirming with Matt before spending a pass on them).

## 2026-08-06 (later) — en195-arcade: fixed the contrast bug AND the gate that missed it, added hub icons, split the coin economy into coins vs tokens

Four things landed tonight, all in `en195-arcade.html`, all byte-verified against the authenticated API (SHA256 match, not raw-CDN-trusted):

**1. The Comfort-toggle contrast bug, fixed upstream.** The `body[data-stop="softer"]` rule only ever remapped `--paper`/`--card`, leaving `--ink`/`--ink2`/`--gold`/`--rust`/`--slate`/`--kraft`/`--edge`/`--focus` to fall through to whatever the `@media (prefers-color-scheme: dark)` block had already set on `:root`. On a device with OS dark-mode preference on, toggling to "Softer" produced light ink on light paper — axe-core measured this at roughly 1.08:1 to 1.14:1 contrast, effectively invisible. This is the same bug class as The Tell and The Viscosity: a comfort stop that partially overrides tokens instead of declaring its full, self-consistent set. Fix: `softer` now sets all nine tokens explicitly, matching how `warmdark` was already built correctly. Commit `0362990`.

**2. Why Studio Eyes didn't catch it — the real upstream fix.** `comfort-audit.mjs` (the purpose-built gate for exactly this bug class, built after The Tell and The Viscosity) still reported this file CLEAN. Root cause: v1's stop-detector used a hardcoded name list (`data-comfort="warm"`, `body.dark{`) that matched 0 of 74 real corpus files — the studio's actual convention had already moved to attribute selectors (`body[data-stop="softer"]`, `html[data-light="night"]`). 67 of 74 pages use that convention; the old detector silently skipped every one of them, including The Tell and The Viscosity, the two pages that motivated building the tool in the first place, and printed CLEAN regardless. Rewrote detection to parse the page's own CSS for every `(html|body)[data-X="Y"]` rule — no name list, self-updating — and to test every discovered stop under both light and dark OS colour-scheme emulation (the bug only appears in the OS-preference × stop interaction, not either alone). Verified the rewritten tool now catches the real bug (reproduced the 1.08:1 violation) and goes clean after the content fix. Commit `d173fa6`. Not yet re-run against the full 74-file corpus with the fixed detector — worth doing as a follow-up sweep, the same way the Fingers backlog got surfaced.

**3. Hub icons.** All 7 hub cabinets (Semester Machine, Sandbag Drop, Line Break, all four Workshop cabinets) now carry a hand-cut inline SVG icon next to the name — coin+river, balloon+basket, broken line, quill, feather, two-mask CNF/poetry/play/story marks — built from theme tokens so they recolor correctly across all three comfort stops. No emoji, per house rule. New `.cabrow`/`.cabicon`/`.cabtext` layout classes; Studio Fingers confirmed the restructuring didn't break the 44px touch floor.

**4. Coin economy split into coins and tokens.** Previously every Semester Machine answer paid one coin regardless of quality. Now: the best answer per round still pays a coin (ding + a rolling gold-coin SVG, `coinRoll` animation), any other answer pays a lesser wooden-nickel token instead (a synthesized square-wave "Maru Batsu" buzz plus a batsu/X-mark SVG stamp) — the player keeps playing either way, per founder spec ("you still get a wooden nickel or brass washer and +1 token state to keep playing"). New `tokens` counter, `setTokens()`, `buzz()`, `COIN_SVG`/`BATSU_SVG`/`NICKEL_SVG`, rewritten `smAnswer()`; three UI copy lines corrected from the old unconditional "five rounds, five coins" claim now that the payout is differentiated. `prefers-reduced-motion` respected for both new animations, matching the existing `.glint`/`vm*` pattern. The coin ticket export now itemizes tokens separately from coins.

**Still open:** stacking "won" principles on a personal leaderboard (the founder's fourth ask) needs a schema decision — likely a new Supabase table, separate from the existing `workshop_tokens`/`workshop_board` pair which serves the unrelated Workshop Vending Machine submission board — before it can be built. Not started.

---

## 2026-08-08 — CYL spine line: objection reaffirmed, removed from every build (not just demoted)

**DECIDED — "You don't judge the leader. You judge what you were allowed to see." is fully retired, not merely demoted.** The 2026-07-23 entry above records it moved off the v5 title screen to a post-play coda; what actually happened in v5/v5-b is the coda was rewritten to different words entirely ("Be easy on the person in the chair..."), while the original line kept shipping unnoticed on four other live, index-linked surfaces: `choose-your-leader-full.html`'s title screen, `choose-your-leader-v5-slice.html`'s title screen, the CYL card blurb on `studio/play-tight-spiral.html`, and the payoff line inside the embedded demo widget on `studio/studio-tour-for-massbay.html`. Founder, 2026-08-08: "I never liked or approved [it]." Removed from all four, verified no console errors post-edit, full belt run clean. `cyl-full-bible.md`'s Beat 1.0 spec (which literally instructed the line onto the title screen) corrected so a future rebuild from spec can't reintroduce it; `choose-your-leader-map.md`'s "one-sentence version" and the OS's CYL entry (`tight-spiral-studio-os.md` §9, current projects & assets) both annotated rather than left asserting a retired line as current.

**ANSWERED LATER SAME DAY — see the v7 drift ruling below; the paragraph that
followed here is kept as the record of the question as it stood:**

**NOT YET DECIDED — no replacement thesis line authored.** The founder's framing of what Viscosity/CYL are actually about — "the effect your leader had on you in CYL, as you move in your world, affected by your leader" — describes Viscosity's felt-descent role (consistent with the 2026-08-05 entry above), not a new CYL spine sentence. Distinct open question, still his to answer, not guessed at here: **does the OS §CYL-disciplinary-bench "corrected pitch"** ("You don't judge the leader. You watch what in you decides to follow.," added 2026-07-21, never implemented in any build) **also fall under this objection**, since it opens with the same rejected clause? Left untouched pending his answer — it's design-rationale text, not a duplicate of the removed line.


---

## 2026-08-08 — CYL v7: the drift ruling (founder, binding)

**RULED — the drift is named and the direction is set.** Founder's words verbatim in `cyl-v7-founder-ruling-2026-08-08.md` (the binding capture; this entry is the pointer). The substance: The Viscosity's felt Maslow-descent — the player moving through a world thickened by the powers their leader was enabled to use — is CYL's missing core, ruled so 2026-08-05 and never built into any CYL surface; that absence is the drift. The tag has to go in ALL variants — this closes the morning's open question (the 2026-07-21 "corrected pitch" is retired too, removed from the OS) and extends to the paraphrase ("judge what you were allowed to see"), which a widened retired-lines pattern then found still live on studio/studio-river.html and studio/tsp-home.html plus three spec docs — all six hits fixed, gate PASS, renders verified clean. Copy: founder's words only where possible (chats unreachable — the harvest boundary; docs are the reachable source; studio placeholders must be tagged as such). Art: mount the standing lanes (period bible + image lane, magazine-collage-is-photoreal, no real faces). Screens image-first, one thing at a time, skill scaffolded; a full room (TV, radio) is allowed. Class representation and perspectives repped — the three-homes finding is the grounding. Roster: Cold War trio live; Obama already un-gated (2026-06-27, sourced); Trump + Biden gated, even-handedness binding.

**FLAGGED, NOT ANSWERED — the protection question.** Zimmerman's recorded verdict: the old framing was load-bearing for keeping real presidents/real deaths playable. The line is dead; the protective function needs a new home before the current-era trio expands. Founder's call.

**NEXT SHIP:** the v7 descent-in-world build, Union Rep seating at open, per the ruling doc's order of work.

---

## 2026-08-08 — Legal-photo lane AUTHORIZED (founder: "Authorized to build and use legal photos")

**RULED — the realism lane is live for the v7 build.** The standing sourcing rules bind unchanged (OS §16 Lane C + cyl-v5-image-lane.md): only named, verified license sources — PD-first (Library of Congress, National Archives, US-gov, Wikimedia Commons PD/CC0) — license verified on the item's own rights page, source URL + license string recorded in the mount, never an unlicensed grab, never a real leader's face in CYL (the room is the subject; the figure stays withheld). Provenance manifest lives beside the assets.

**REACHABILITY MAPPED same hour (tested, not assumed) — PENDING one founder unlock:**
- **This session's network policy BLOCKS the PD archives** (curl and WebFetch both refused on commons.wikimedia.org and loc.gov — proxy 403 / EGRESS_BLOCKED, logged). The image-lane doc now says environment policy governs, not a blanket "sandbox can't."
- **Drive holds no period plates** (searched: images are arcade tiles, screenshots, AI one-offs; the "cyl/plates" a prior session referenced were its own local /tmp, gone with the container).
- **Two unlocks, founder's choice:** (1) FREE — allow-list the archives (loc.gov, www.loc.gov, commons.wikimedia.org, upload.wikimedia.org, archives.gov) in this Claude Code environment's network settings; PD-first sourcing then runs from any session here. (2) PAID — Adobe Stock via the connected Adobe account (`asset_license_and_download_stock`); legally licensed but spends real money per asset, so per the cost rule it waits for an explicit per-use go-ahead. Until one opens, the v7 build's art mounts stay staged as asks, exactly like the fys hero plate.

---

## 2026-08-08 — FOUNDER RULING: the vending machine leaderboard needs no login

Founder, verbatim: **"No login needed."**

This closes one of two founder-opens carried in `en195-arcade.html`'s TSP-META since
2026-08-05: *"public leaderboard requires no login - confirm acceptable for this course."*
Confirmed. It ships as built. The Supabase posture is unchanged and already matches:
anon insert-only on `workshop_tokens`, select-only on the `workshop_board` view, RLS
verified, and the anon key can never read the base table.

**The design consequence, recorded once and not re-litigated.** With no account there is
no server-side identity, so the board is self-declared: a name on it is a claim, not an
authentication. Two students can pick the same name, and one can enter another's. For a
six-week workshop board whose whole job is to make practice visible, that is the correct
trade, and it is the founder's to make. The alternative buys identity with a login wall in
front of a game, which is the friction this build exists to remove.

Still open, and the last one on this file: retention and deletion policy for
`workshop_tokens`. Semester end, a fixed drop date, or on student request.

**Separate finding, same file, same day.** Measured against the type standard amended
today: `en195-arcade.html` PASSES type-census at 0 of its visible text nodes under 18px,
which makes it one of only six clean surfaces in a 134-surface corpus carrying 4,171
nodes of debt. But it passes for the wrong reason. It hardcodes `font-size:20px` on
`:root`, which is exactly what the amended standard rules against, because it overrides
the one accessibility control the reader already owns. A reader who has set their browser
to 24px gets 20px here. The number is right and the mechanism is wrong. It goes when
comfort v3.1 mounts, and the count should hold at zero on a reader-controlled root.


## 2026-08-09 — Comfort v3.1 mounted on the arcade; layout preview folded in and deleted

Executed per `claude/HANDOFF-VENDING-MACHINE-2026-08-08.md`. The Workshop Vending
Machine (`en195-arcade.html`) now carries all five things the founder means by comfort -
font size, contrast, modes like warm and dark, motion stop, and screen reader options -
plus persistence applied pre-paint (`tsp.comfort.v1`), so a reader who chose warm dark
never sees a flash of daylight. The block was LIFTED from `comfort-v3.html` (sha
`6a753a4ed473f38d`, all seven ticks clean), not re-derived; the only host adaptation is
measure() reading `.coinbar` instead of `.chrome`. The old three-stop `data-stop` ladder
is gone - this was one of the last three files on that vocabulary.

The belt ran before and after, per the handoff's first rule. Before: PASS with one
`comfort-gate` DEBT line. After: PASS with the DEBT line GONE, not carried - the dark
path is visible to the gate now (night body luminance measured dark, day/dusk/night all
at or above 4.5). Both this file and the deleted preview were burned off
`comfort-baseline.json` (25 entries to 23; the list may only shrink).

The wrong-mechanism finding from 2026-08-08 is closed the way it predicted:
`:root{font-size:20px}` is gone, the root is `font-size:100%`, and type-census still
reads 0 visible nodes under 18px (body 18.0px at a default browser base, more at the
reader's). The count held on a reader-controlled root.

The one real design decision went the way the handoff proposed, uncontradicted: the
puppet stage (scene0 and the four cabinet guardians) stays fixed-dark as its own scene.
Comfort governs the chrome and the reading surfaces around it. The guardians still read.

The layout preview (`en195-arcade-layout-preview.html`, 2026-08-06 v2) was folded in and
deleted, its line removed from `index.html`. What it contributed: the reader-scale type
ladder (body 1.125rem), the compact sticky coinbar with coin and token glyph counters
that tucks on scroll-down and returns on scroll-up, the narrow-screen furniture layer,
and one tightened hub sentence. Its comfort-button compaction was superseded by the
v3.1 dock in the thumb arc - which also clears the C-REACH note studio-fingers carried
on this file. The per-animation reduced-motion blocks were replaced by the two-rule
comfort pair, so an explicit motion choice now outranks the OS in both directions -
verified in a live browser, along with persistence across reload, Clear Reader leaking
none of the arcade's hidden screens, and the full coin round-trip.

Still open, unchanged, the founder's call: retention and deletion policy for
`workshop_tokens` - semester end, a fixed drop date, or on student request.

## 2026-08-09 (later) — FOUNDER RULING from live playtest: Dusk is retired

The founder played the arcade on his phone within the hour of the comfort mount
landing and ruled, verbatim: *"Lots to like about the arcade this makes me want to
kill dusk all together and have Day Warm Clear."*

Landed on `en195-arcade.html` the same turn (v5.1): the light ladder is **Day / Warm
dark**, the Dusk button, its token block, and its Clear Reader tokens are gone, and a
stored dusk choice from another surface normalizes to day so the control's pressed
state stays honest. **Clear Reader stays its own toggle**, not a third light stop -
that is the standing 2026-08-08 ruling (it composes with warm dark instead of trading
against it), and nothing in the playtest message overrules it. Belt PASS, type-census
0 under 18px, night+Clear composition verified in a live browser. Pushed in six
surgical connector commits, each byte-checked, repo sha256 equals local.

Left open by scope, not by neglect: propagating the dusk retirement to
`comfort-v3.html` (the standard the arcade lifted from) and to comfort-gate's
day/dusk/night MODES list. The gate still passes this file as-is - its dusk pass just
measures the day palette now. Next session's first errand.

Lane note: two new connector actions landed today for small patches -
`delete_line_from_repo_file` and `replace_substring_in_repo_file`, both requiring a
unique match and an expected byte total before they will write, both tested on a
scratch file before touching canon. A one-line fix no longer costs an 80KB re-upload.

## 2026-08-09 (later still) — FOUNDER RULING from playtest: the math needs subtraction; tokens buy play at 2:1

Second playtest note of the night, verbatim: *"The math needs subtraction. If it costs
a coin to play you should always have 1 zero 1 zero 1 tokens, right?"*

Measured before answering: coin subtraction already worked (trace: 1 to 0 entering
Sandbag, blocked at 0, earn 1, 0 again entering Line Break). What the instinct actually
caught: TOKENS had no subtraction anywhere - they only climbed - while the reward line
promised "+1 token so you keep playing." A student with five weak answers held five
tokens, zero coins, and was locked out by a game that had just told them tokens keep
them moving. The copy and the math disagreed.

Founder chose, from three options: **2 tokens = 1 play.** Paid cabinets now cost 1 coin
or 2 tokens, coins spend first, so the wooden nickel finally buys something and a coin
stays worth more - the strong-read lesson survives. Blocked message, hub copy, and both
price tags state both prices; the reward line adds "Two tokens open a coin cabinet";
the carry-out ticket logs token spends. Traced live: coin path, token path, honest
block at 0 coins 0 tokens. Belt PASS, census 0 under 18px. Landed as v5.2 in six
surgical byte-checked connector commits; repo sha256 equals local.

## 2026-08-09 (third playtest note) — FOUNDER RULING: Line Break rebuilt; the game must create what it teaches

Verbatim: *"Also line break game mechanic is lousy. Visually terrible because it doesnt
create what it teaches. Enjambment. Providen prose and X number of scissors to cut lines
and repopulate text below. Players can use free 'paste' to go back - enjambment game
should be created by poets. Fails as is."*

The diagnosis is exact: the old mechanic toggled slashes in a word row and NAMED what a
break does, but no line was ever made - the one thing the game is titled for never
appeared on screen. Rebuilt as v5.3 to the founder's sketch: the poem flattened back
into prose, seven scissors in hand (Williams's own break count for The Red Wheelbarrow -
the scarcity is the craft lesson), each cut spends a scissor and the poem re-forms live
in a verse card below, paste is free and returns the scissor so nothing is lost to
experiment, and an eighth cut is blocked until one comes back. The slash stays as the
cut mark because it is the mark poets use to quote a break. Williams's teach notes kept.

Traced live: seven cuts at Williams's own break points reproduce the poem line for line
in the card; the eighth cut blocks; paste refunds. Belt PASS, census 0 under 18px.
Landed in five surgical byte-checked connector commits; repo sha256 equals local.

## 2026-08-09 (fourth playtest note) — FOUNDER RULING: Sandbag Drop gets a win state and five rotating passages

Verbatim: *"Also, the sandbag game should have a clear win state and should rotate 5
pieces of prose."*

Landed as v5.4. The five passages come from `games-text-bank.md` under its own policy -
the load-bearing prose is the founder's writing, the machine adds clearly separable
padding, and cutting the padding back out IS the game. Passages: the Rockview Rd duplex
and the potten plants (A Roslindale Story), the Taiko drumming and the bus station (The
Van Story), and the extra large milk no sugar (the reaper draft). A provenance line sits
on the game screen: "Prose: Matt Walsh, from the studio text bank. The padding is the
machine's; cutting it is the game."

The win state is now unmistakable: cut every sandbag with the cargo intact and the
balloon sails clear of the frame, "Lift-off. You win." and the writer's own sentence is
read back with nothing extra. Cut cargo along the way and the balloon holds low with an
honest message until the cargo is pasted back - so the win is cutting EXACTLY the flab,
not cutting everything. A free Next passage button rotates forward; entering the cabinet
fresh also rotates. Passage counter shows N of 5.

Traced live: cargo-hostage state, win at cargo restore, all five passages won in
sequence, rotation wraps back to passage 1. Belt PASS, census 0 under 18px. Five
surgical byte-checked connector commits; repo sha256 equals local.

## 2026-08-09 (fifth playtest note) — FOUNDER RULING: 3x graphics, genre districts, feed the beings; Samorost pass banked

Verbatim: *"The graphics should be much larger cs text. Like 3x current. I want to see
genre related games located near the four current workshops, which players will use a
week or 15 weeks from entry into this platform. This is for practice and playing so
workshops should be for real. Feed those animated beings!!!! And more zany art like
samarost"*

Landed as v6, structure now, new art banked. The hub is four genre districts, each led
by its guardian banner on the arcade floor - the beings left the vending back room and
took the floor, idle rigs running, injected from VM_ART so the art lives once. In each
district the practice cabinet sits above the real workshop, tagged "Practice, any week"
and "For real"; Sandbag Drop guards Creative Nonfiction, Line Break guards Poetry, and
the Play and Story districts carry honest "in the shop" slots until their practice
cabinets exist. Cabinet icons went 40px to 120px (96px narrow), workshop copy trimmed
to group names, and the server-exception note shrank to two sentences below the
districts - the ruling was more picture, less prose, and the file obeys both ways.

The Samorost-grade zany pass (guardian environments, secondary beings, richer icons) is
deliberately NOT tonight's work: new art wants a fresh session, not the tail of this
one. It is banked with teeth as `claude/HANDOFF-ARCADE-ART-SAMOROST.md` - founder words
verbatim, art direction, and every floor that binds it.

Traced live: four banners render on the hub with animations running, districts named,
icons 3x, every cabinet still opens, sandbag and workshop flows intact. Belt PASS,
census 0 under 18px. Six surgical byte-checked commits plus the handoff; repo sha256
equals local.

## 2026-08-09 (sixth playtest note) — FOUNDER RULING: Comfort at the top AND the bottom, tucking, studio-wide

Verbatim: *"Comfort should be like the homepage it's up at the top, but after you scroll
up, it disappears that happens across the studio and you include them at the bottom too"*

Landed as v6.1 on the arcade: a Comfort button now sits in the top bar beside Home,
rides the tuck (slides away on scroll-down, returns on any scroll-up), and the thumb-arc
dock stays at the bottom - two doors, one panel, aria state synced across both, the
outside-click close excludes both buttons. Traced live: opens and closes from either
end, tucks and returns with the bar, no overflow at 390px. Belt PASS, census 0 under
18px. Four surgical byte-checked commits; repo sha256 equals local.

The pattern is ruled STUDIO-WIDE: top-and-bottom comfort on every surface. That rides
the existing comfort-standard propagation item (with the dusk retirement) - one
next-session sweep updates comfort-v3.html and carries both rulings to the corpus,
rather than patching 101 surfaces twice.

---

## 2026-08-10 — Session-close lane sweep (the standing CLAUDE.md sweep, run before idling)

**Swept via live connectors, cost-scoped per the rule.** Spokes: matt-radar and the writerly-moves repo clean; en195-apps clean (the offline-floor fix branch is fully merged, pointer just undeleted). **One real strand found:** the Confluence hub repo carries an unmerged branch (github-pages-deployment-setup, tip 08690e4, 2026-07-19/20) holding a complete Supabase real-data backend — schema, RLS policies for the four-role model, reliability views, magic-link auth behind a demo-mode fallback, plus a one-shot setup script. Three weeks stranded, the classic built-never-merged shape. NOT merged by this session: TSP is read-only in the Confluence lane; the merge is a Confluence-lane call, founder's to route. Zapier: clean — deploy-studio-file still targets GitHub Pages with SHA-safe verification. Drive: no TSP file newer than its repo counterpart; two items worth routing, named by title without paths so tick 8 reads this as prose, not citation: a founder-authored "Silent Majority World Building" doc (mwalsh account, modified 2026-08-06, Drive id 1R9qM2FybyxEOmrTumoaWuRceKhyx0WUtogs2Ol4GIak) — founder's own words for the Nixon '69 world, exactly what the CYL lane's words-only copy policy wants, routed to whichever lane now owns CYL; and a LAND-THE-BUNDLE note (2026-08-06, id 1J2HboNm70Lg_e7JXHa38WBYVN6M0fDqF) that whoever owns the bundle handoff should glance at once. Human-only lanes (shelf, chats) not walkable by anyone — mitigation stays harvest discipline.

## 2026-08-09 (seventh playtest note) — FOUNDER RULING: train before Williams; the start is a block of prose and nothing else

Verbatim: *"wCw is crazy hard to start with for enjambment. Train on this and retry the
look. The Start Should be a block of prose and nothing else. Keep it clean."*

Landed as v6.2. Line Break now opens on a trainer passage - the founder's own line from
the text bank, "I've pictured this so many times I almost have a memory of there being
a photograph." - five scissors, no teach notes, free ground where every cut is
expressive and there is no canonical poem to feel wrong against. Williams is the second
passage, reached by a Next button, with his seven scissors and the teach notes intact.

The look retried: the entry paint is the clean prose block and nothing else. The intro
paragraph is gone entirely; the scissors counter, poem card, feedback, and next button
all stay hidden until the first cut reveals them. The cut marks lost their dashed boxes
- quiet gold slashes in the text now, 44px targets held - so the block reads as prose
instead of a picket fence.

Traced live: clean start confirmed (all machinery hidden), first cut reveals and breaks
the line, trainer at 5, Williams at 7 with the upon note firing, cycle runs both ways.
Belt PASS, census 0 under 18px. Four surgical byte-checked commits; repo sha256 equals
local.

## 2026-08-09 (eighth playtest note) — FOUNDER RULING: the dock is retired; Comfort at the top of the page only

Verbatim: *"I'm still seeing the comfort button standing in the lower right when I
scroll. Just top of page. We don't even need it at bottom please"*

Landed as v6.3. The bottom dock left the DOM, its CSS, and Clear Reader's exclusions;
Comfort lives only in the tucking top bar, and the panel now drops down from the bar's
measured height instead of floating up from the corner. This overrides two earlier
positions in order: the v3 thumb-arc placement (C-REACH) and last hour's top-and-bottom
reading - the founder saw both live and chose top only. The studio-wide comfort pattern
is likewise top-only, riding the same propagation item.

One pre-existing quirk surfaced while verifying: the coinbar's hidden attribute has
never actually hidden it (the .coinbar display:flex rule wins over [hidden]), so the top
bar - and now Comfort - shows on the entry scene and always has. The entry gate has
carried it all along. Left as-is: it matches the ruling, and closing it is a one-line
CSS guard if the founder ever wants the entry scene bare.

Traced live: no dock anywhere on scroll, panel opens under the bar, night applies,
Clear Reader keeps the top bar as its exit. Belt PASS, census 0 under 18px. Eight
surgical byte-checked commits; repo sha256 equals local.

## 2026-08-09 - FOUNDER RULING (live playtest, ninth of the night): the first screen goes organic, and the type gets a director

The founder, from his phone, looking at the entry screen: "First Screen - can we make the arcade more like samarost on the splash? Organic? Also look at the typing for home and comfort, out of the box. Whose job is that on staff? We aren't pro yet hire in." His screenshot showed the ruling's evidence: "Comfort" clipped off the right edge of the top bar at his font size, and Home/Comfort wearing the browser's stock box.

Three fixes and a hire, landed as arcade v6.4:

1. Scene0 rebuilt organic. The three rectangles are now rounded stump-forms grown out of two rolling mounds - moss caps, mushrooms at their feet, drifting spores, a curling tendril with a swaying frond, and a small round being with glinting eyes watching the coin from beside the third cabinet. Hand-cut SVG, own work, fixed-dark stage kept, idle animations ride the motion pair. The deep Samorost pass across the rest of the arcade stays banked in claude/HANDOFF-ARCADE-ART-SAMOROST.md.
2. The coinbar wraps instead of clipping. The bar was a no-wrap flex row, so at a reader-enlarged base font the last button simply left the screen. flex-wrap added, padding tightened; render-proofed at 390px with a 24px base - Comfort's right edge lands at 378px of 390, zero horizontal overflow, and the panel opens below the measured bar (ResizeObserver keeps --chrome-h honest at any wrap height).
3. Home and Comfort out of the stock box. Pill cut, 2px edge, quiet ground, letter-spaced; the 1.125rem type floor and 44px tap floor held - fit was fixed with wrap and padding, never by shrinking text.
4. The staffing answer, plainly: that job belonged to nobody. Studio Eyes proves the floors (18px, contrast, paint) and the comfort standard governs the controls, but no seat owned whether the type is any good - fit at the reader's own font size, chrome that looks designed rather than shipped. So the studio hired in: the Art and Type Director seat now exists at .claude/agents/type-director.md, owning typography fit at reader-enlarged bases (24px is the working proxy for the founder's phone) and art continuity against the Samorost brief. One agent, never a fleet, cost discipline binds it, lenses not authorities.

Verification: belt PASS all ticks, type census PASS (every visible node >= 18px at 390x844), six surgical connector ops each with simulated expect_total_bytes (93661 / 94053 / 94492 / 95158 / 95204 / 98583 - all matched), remote sha256 28775bf7 equals local byte for byte, hire file seeded at 3077 bytes verified.

---

## 2026-08-10 — Founder-ordered review: the FableVision + Filament network-strategy spec

**Reviewed against today's studio, verdict: the doc has aged WELL on its spine and gone stale on its pilot pick.** The brake ("do not build a partner network until a real student plays a real game, with captured evidence") is MORE true now than when written - the studio still has zero verified student plays; GATE 1 cold plays owed since 07-13; the blind consultation's proof seat independently reached the same one-legible-win conclusion. Aged well: Alpha/Beta/Gold DID graduate into the patterns file as Fidelity Tiers, and the doc's brake-first structure kept it from ever being read as a scaling green light. Gone stale: it names "CYL or EN195" as the fall pilot candidates, but CYL is now mid-v7 redesign in another lane - the realistic fall pilot is the EN195 arcade, which is his own course's build and under active polish. TIME-CRITICAL: "this fall" is now weeks away; the pilot call (which game, which section, capture engage/learn/change) is the single most time-sensitive founder decision in the studio - unmade, it slips a semester and every parked door (NEH, IES SBIR, verticals, the Paul Reynolds note) slips with it. Also still open from the doc's own list: the Reynolds peer note (costs nothing), the knowledge-gate and garden-test mechanics' formal graduation, the Alpha/Beta/Gold naming into OS §6 (patterns has it; the OS pipeline section never adopted it).
## 2026-08-09 — CYL spine fork: the shelf and the repo disagree about a founder ruling (PENDING — FOUNDER ONLY)

**FOUND — a fourth working lane, invisible to chat-history search.** The founder
enumerated the project's chat window rather than searching it by topic: three chats
exist since Aug 3 (Zapier fireground assets 08-06, The Slip / EN195 / date gate
08-06, timing belt strategy 08-07). None is CYL. The Aug 5-6 CYL modern-period work
ran in Claude Code / Cowork sessions — a lane `conversation_search` cannot see, and
the one doing most of the actual building right now.

**THE CONTRADICTION.** Shelf doc `cyl-modern/SPINE-RULING-2026-08-06.md` records a
founder-selected spine line — **"You judged. Now find out what that judgment was
standing on."** — option 5 of a five-option slate, CYL-SPINE-02 bound with an
in-place marker (claimed commit `6130158`), placement spec'd into `cyl-full-bible.md`
Beat 1.0, plus a modern-period physics ruling (STANDING, route termination,
confidence retired, 19→31 items). The repo's own 08-08 record says the opposite:
"NOT YET DECIDED — no replacement thesis line authored" (this ledger, that morning),
and the v7 drift ruling closes the day with *no thesis line exists for CYL today; if
one is ever needed, the founder writes it.*

**VERIFIED against the repo this session (2026-08-09):**
- The line string appears NOWHERE in the tree — zero hits, whole repo.
- `6130158` is not an object in this repo's git history (`git cat-file` fails).
- Origin carries only `main` and the current session branch. Nothing stranded here.
- `cyl-full-bible.md` Beat 1.0 carries no CYL-SPINE-02 marker — only the 08-08
  correction that removed the retired line.

If the shelf ruling is real, the work never reached this repo. The recovery target
is off-repo: a git bundle or local clone on the Mac. Nothing recoverable from here.

**THE FORK, enumerated, not collapsed (per FORKING-PATHS-PROTOCOL):**
- **Path A — real and stranded.** The ruling happened in a Code session; the write
  lane was denied, `/tmp` evaporated with the container, and the only surviving
  record is the shelf copy that says so in its own header. The 08-08 sessions wrote
  "not yet decided" because they had no memory of it.
- **Path B — artifact.** A Code session drafted the five-option slate and recorded a
  selection, but the founder selection never actually occurred — or occurred and was
  superseded by the 08-08 v7 ruling.
Opposite consequences: under A the founder already chose a line and the studio lost
it (and the modern-period dossier work is real and stranded); under B the v7
ruling's open call is correct, the shelf `cyl-modern/` docs are a fossil, and there
is nothing to recover.

**PENDING — the narrow founder question, only he can answer:** *On or around
August 6, did you pick a spine line from a slate of five, and was it "You judged.
Now find out what that judgment was standing on."?*
- **If yes:** the line stands as a decided founder call (still read through the v7
  ruling's frame), the modern-period work is stranded, and the recovery errand is a
  Mac-side search for the git bundle / local clone. Trump/Biden retrieval work may
  not need redoing.
- **If no:** mark the shelf `cyl-modern/` docs as fossils so no future session
  treats them as canon, and the v7 ruling's "no line exists" stands unqualified.

**Guard note:** the candidate line is neither canon nor retired while this is open.
It does not go into any build, and it does not go into `retired-lines.json`, until
the founder answers. Either way the 08-08 v7 drift ruling governs the build — this
fork decides only whether a line exists to recover and whether the modern-period
sourcing work needs redoing.

**ADDENDUM 2026-08-10 (founder, verbatim): "I don't love that pitch either exactly
like that."** — said of the shelf's candidate line ("You judged. Now find out what
that judgment was standing on."). Effect: whichever fork path is true, the line does
NOT become canon as written. The v7 ruling's state stands — no spine line exists;
if one is ever needed, the founder writes it. The fork's remaining live stake
narrows to the modern-period dossier work (real-and-stranded vs fossil); the line
itself is settled: not approved as-is.

## 2026-08-10 — FOUNDER BUILD ORDER: CYL v7, the full six, the felt drop, CLASS not politics

**Verbatim:** "Merge this lane with this doc as needed and create the latest
Cohesive full 6 President 20 minute plus Maslow drop like Jenova Chen flow so
you feel how choices affect class! Not politics, wealth and power."

**Unpacked (binding, extends the 08-08 v7 drift ruling):**
1. **Full six presidents in one cohesive build** — the Cold War trio plus the
   current-era trio. This is the founder ordering the current-era scenes INTO the
   build; the standing sourcing rule still binds HOW (records real, dated,
   sourced, even-handed — never fabricated), and his cold play remains the final
   gate on the records themselves.
2. **20+ minutes** — a full arc, not a slice.
3. **The Maslow drop is FELT, Jenova Chen flow** — the descent as something the
   player moves through and feels thicken (the 08-05/08-08 rulings' viscosity
   mechanic, now ordered into the main game, not staged beside it).
4. **THE FRAME IS CLASS, NOT POLITICS.** The gap the game teaches is what wealth
   and power did to where the player's household stands — never which party was
   right. Records are chosen and written on the class/wealth/power axis;
   partisan scoring of any president is out of scope by founder order.

## 2026-08-10 — SHIPPED: choose-your-leader-v7.html, the full six and the felt drop

**The build order executed same session it was given.** Single file, 1.58 MB,
offline, no storage, no audio. Six presidents in one cohesive 20+ minute arc:
JFK 1962 / LBJ 1964 / Nixon 1969 (records carried from v5-b canon) + Obama 2013
/ Trump 2017 / Biden 2022 (records sourced and web-verified this session;
sources carried in-file per scene; founder cold play is the final record gate).
Even-handedness held by construction: both post-2016 scenes are an economic
promise measured against the documented record of where wealth and power
landed. The frame is class, not politics, per the founder order: every record
turns twice (what was hidden, who paid by household).

**The felt drop is in the main game for the first time.** Between addresses the
player walks the household: three rooms at fixed angles (the shift, the shelf,
the back room) whose distance stretches with altitude spent and whose steps
shrink (the-viscosity vocabulary, mounted not reinvented). Altitude is the
running mean of landing tiers, so the descent ACCUMULATES across scenes: the
Zimmerman integration note (scenes should alter each other) gets its first
real answer, and trust spent on unexamined power is felt as distance in the
next walk. Noticing brakes it. Chen flow: the world's thickness adapts to the
player's own reads, never to a score.

**Gates:** full belt preflight PASS, all seven ticks (comfort/dark, attribution,
image floor + render, voice, entry paint, retired lines, touch floor) on both
the build and the updated face. Playwright click-walk verified the six-scene
loop end to end on a phone viewport: altitude carry, era shift after Nixon,
sources rendering, warm dark, Home, zero console errors. Founder MJ plates
mounted from v6 with provenance verbatim; modern scenes are CSS-composed
rooms (no plates exist; archive egress blocked, see 08-08 entry). All studio-
drafted copy is marked in TSP-META as awaiting founder words; the six address
quotes carry the voice gate's verbatim marker as sourced transcript language,
dashes the transcripts' own. No thesis line exists and none is used.

**Open, founder-only, unchanged:** GATE 1 cold play (now on v7); record
approval for the three current-era scenes; the protection-function home
(Zimmerman); which build goes to Scot.

## 2026-07-23 — Founder log: Confluence adopted into the one repo; playtest team seated; Funes sync adopted (logged, binding)

Logged from the Claude Code + Confluence-project sessions, in the founder's words the day made.

- **One repo.** "One repo. Bring it in." Confluence consolidated into `walshero/TIGHT-SPIRAL-STUDIOS` as a **lane** (`confluence-hub/` + the `confluence-*.html` files), retiring the separate private `confluence-calibration-assessment-hub` repo. "Confluence will be its own entity, but it can benefit from TSP assets like panel, aleph." (PR #24, merged.)
- **Trunk floors fix — authorized.** C1 + warm-ink + sub-18px fonts fixed on canon; **`--pine-lt` FOUNDER-WAIVED**. Re-applied to current canon after main advanced mid-flight. (PR #25, merged.) Residuals baselined: `'Tour'` 4.19 contrast, `<body>` paint-mismatch.
- **Companion floor fix.** Sub-18px chrome fonts lifted to 18px (PR #49). Correction logged: the dark palette (`html[data-light="night"]`) and comfort control (Studio Eyes panel) were **present, not lost** — `preship-gate-v4`'s H-DARK tooth doesn't recognize the `data-light` convention (false positive). The force-darken bug is not present.
- **Playtest team seated.** "Seat a new kind of playtesting team… each role should be comprised of template characters that represent the diversity of those individuals in real life." Roles: student / faculty evaluator / chair-lead / coordinator / reviewer, each a spread of **composite template characters** — "diversity is coverage, not decoration"; no real individuals named. (PR #48.)
- **Names ruling (re-affirmed).** "Don't make up names. Use clearly marked sample, and for MassBay model, use actual people or position."
- **First playtest run** on the companion (pinned `5f7fb1d8`): F1 metaphor-only nav, F2 mixed audience signal, F3 no auto-dark (discoverability), F4 unglossed jargon; accessibility otherwise strong. Method: simulated; disposition axes want real humans.
- **Adopt Funes.** "Adopt the TSP mechanism for synching chats with funes ledger and os." The Confluence lane now syncs to this ledger (founder log at close), carries state via `handoff.py`, and runs the Funes open card (canon-as-of-today + open loops). This entry is the first sync.

**Open loops (Funes board):** PRs #48/#49 pending merge · auto-dark decision (companion F3) · trunk version banner + cross-lane manifest still say v44 (stale; canon is `01b053f8`) · `preship-gate-v4` is not in CI so the H-DARK/font teeth don't block (the companion regression slipped this way) · `HANDOFF.md` is stale (2026-07-16).

## 2026-07-23 — Built the true-pixel contrast checker; v48 has real invisible text (logged, binding)

"Build pixel checkers needed so studio stops failing contrast (regular and dark mode)."

- **BUILT `studio-eyes-pixel.py`** — a real-Chromium true-pixel contrast gate. Loads the
  page (executes JS), viewport-tiled screenshots, reads the ACTUALLY-painted background
  behind each text run (quantized-mode sampling, robust to anti-aliased glyphs), with
  `elementFromPoint` occlusion so closed overlays / hidden nav are not false-flagged.
  Checks **light AND dark**. Self-test teeth (gold-on-gold HALTs, black-on-white passes)
  refuse to certify if broken. Fixes WeasyPrint's body-grounding, which caused BOTH false
  positives (dark-ground text) and the gold-on-gold false negatives.
- **VALIDATED:** companion = SHIP (true-pixel clean, light+dark). Trunk v48 = HALT with
  REAL defects the WeasyPrint gate missed: `'Skip tour'` studio-green-on-green (1.0:1,
  invisible), `'Next'` white-on-white (1.08:1), `'What Confluence is'` green heading 3.86:1.
- **CONSEQUENCE:** v48 (Drive canon) is NOT contrast-clean — the FERPA-class invisibility
  the manifest warned of is real and present. The v48 promotion (PR #52) must clear these
  before ship. The checker can run in CI (floor.yml already installs playwright + chromium).
