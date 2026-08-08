# ALEPH A1 — STUDIO ARCHITECT — six-month consultation
*Seat: the engine. Hub-and-spoke, the belt, the gates, canon vs cache, one person's attention as the
scarce resource. Written blind to the other four seats. Grounded against live bytes on 2026-08-07,
not against memory — everything below was measured this session.*

---

## MONTH 0 DIAGNOSIS

### What the architecture actually is

Five git repos, hub-and-spoke. `TIGHT-SPIRAL-STUDIOS` is the hub: it owns canon and the belt
(`studio-belt.sh`, five ticks). Four spokes — `en195-apps`, `confluence-calibration-assessment-hub`,
`-writerly-moves-game`, `matt-radar` — mount the hub's belt at CI time and run it against their own
files. This is the right shape: mount, never copy, is a correct answer to a real failure mode
(`STUDIO-GOVERNANCE.md` names copying as "the drift generator the studio already diagnosed").

But the corpus is almost entirely NOT in the spokes. The belt's own surface scan
(`find . -name '*.html' ... | wc -l`, the exact expression in `studio-belt.sh`) returns **131** HTML
surfaces in the hub. The four spokes hold **three** between them. So today's hub-and-spoke topology
is spending its coordination cost — five repos, a reusable workflow, cross-repo checkout, a
`STUDIO_SYNC_TOKEN` — to govern **2% of the corpus** the belt was built to reach. The 98% sits in
one repo, ungoverned by the multi-repo machinery, governed instead (barely, see below) by whatever
runs on the hub's own `push`.

The belt itself is five ticks: `comfort-gate.py` (flat), an inline attribution grep (flat),
`preship-gate-v4.py --ratchet`, `studio-voice-gate.py --ratchet`, `one-thing-gate.py --ratchet`.
Ticks 3-5 were added **today** (2026-08-07, commit `83c988b`). Before today the belt carried two
ticks and none of the founder's actual rulings — the image floor, the voice standard, the entry
grammar each had a working gate sitting in the hub that nothing wired into CI. That is the honest
starting line for this consultation: the belt that is supposed to be the moat has been running at
full strength for a matter of hours, not months.

### Structural fault 1 — the hub now runs two independent, overlapping CI enforcement systems for the same claim

`.github/workflows/floor.yml` (armed 2026-07-14, blocking, `on: push: branches: [main]` +
`pull_request`) and `.github/workflows/studio-belt.yml` (added 2026-08-07, also `on: push` +
`pull_request`) both fire on every push to `main` and both claim to enforce "the accessibility
floor." They are not the same check running twice — they are two **different** mechanisms with
two **different** baselines reaching two **different** verdicts:

- `floor.yml` runs `ratchet.py` (baseline `gate-baseline.json`, 131 keyed entries of H-codes like
  `H-DARK-MISSING`, `E1-CSS`) plus `comfort-audit.mjs` (Node + axe-core, a real-browser dark-stop
  contrast check) as a **hard block** — "This one refuses," per its own comment — and then deploys
  to Pages if the job passes.
- `studio-belt.yml` calls the reusable `belt.yml`, whose tick 1 runs `comfort-gate.py --ratchet`
  per-file against a **separate** baseline, `comfort-baseline.json`, and does not deploy anything.

Two Chromium installs, two ratchets, two baseline files, two vocabularies of failure code, for one
founder claim ("Matt has retinitis pigmentosa; contrast is arithmetic, not a judgment" —
`STUDIO-GOVERNANCE.md` tick 1). When these two disagree — and given different code paths they
will — there is no doc that says which one is authoritative, and a solo founder now has two red/green
signals to reconcile instead of one. This is the treadmill the SWOT names, already running, on the
belt's first day.

### Structural fault 2 — the governance rate-limiter has been silently unenforced for twelve days

`BUILD-DEBT.md` states the studio's own anti-sprawl rule: *"No session may add a governance
artifact... unless the PRIOR session shipped a player-facing capability,"* enforced by a
session-open check that reads the last two lines of the file's append-only log and refuses new
governance if the most recent line is `GOV` without a `SHIP` before it.

The log's last entry is dated **2026-07-26**. Since then, 58 commits have landed (`git log --oneline
--since=2026-07-26`), including today's five belt ticks, the entire Aleph Fleet (two new os-blocks,
`aleph-fleet.py`, five lens briefs), `resolve-canon.py` v2, `stage-push.py`, and this
consultation's own infrastructure — a heavily `GOV`-weighted stretch by any reading — and **not one
line was appended to the ratio-rule log**. The rule cannot fire on a log it was never updated to
read. A governance rate-limiter whose own bookkeeping goes stale is not a rate-limiter; it is a
comment. This is the same shape as `STUDIO-GOVERNANCE.md` going stale in a day (see the drift
section) but with a longer fuse and higher stakes, because this is the mechanism that was supposed
to prevent exactly the treadmill the SWOT warns about.

### Structural fault 3 — the OS's own "what's unmerged" pointer is stale, and nothing diffs it

`tight-spiral-studio-os.md` (2,416 lines, 230,949 bytes, dated 2026-07-05, landed to the repo
2026-07-12) carries a header block titled "UNMERGED LAW" — the compensating pointer for the fact
that the OS text itself is frozen and incomplete. It names nine `os-block-*.md` files as the live
law living outside the OS text. **Thirteen exist today.** Four are missing from the header's own
list: `os-block-aleph-fleet.md`, `os-block-aleph-diagnose-repair.md`, `os-block-bodyguards.md`,
`os-block-fidelity-gate.md`. The mechanism built specifically to compensate for staleness is itself
stale, by exactly the kind of drift it exists to flag — and the fix is a one-line `ls
os-block-*.md | diff - <(grep -oE 'os-block-[a-z-]+\.md' os-header)`, which nothing runs.

### Structural fault 4 — the resident "always-fresh" shelf contains a file that violates its own premise

Cold Start (`COLD-START.md`, locked 2026-07-13, "law") defines a four-file resident shelf
specifically so a session never has to trust two hundred stale files — the OS, the Command Center,
the Lane Registry pair, and Cold Start itself. `STUDIO-COMMAND-CENTER.md` is explicitly described
as *"Live state... the one doc that changes every session,"* *"Rewritten at every belt close."* Its
own header reads **"v19 — 2026-07-13"** and its body's newest section is "CLOSED 2026-07-13 — THE
ARCHAEOLOGY IS OVER." Its last git touch was 2026-08-05 (a partial edit), but its content still
describes a world three-plus weeks and dozens of commits stale — no mention of the belt, the five
ticks, the Aleph Fleet, or `STUDIO-GOVERNANCE.md`. One of the four files a cold session is required
to trust without a fetch is the one most likely to mislead it, because "rewritten every session" is
an aspiration written into the file, not a check run against it.

### Structural fault 5 (the one the founder himself surfaced) — instruction walls are the accessibility floor's own blind spot, at scale

`INSTRUCTION-WALL-QUEUE.md`, measured today: **52 `INSTRUCTION-WALL`, 29 `ACTION-BELOW-FOLD`, 4
`H-OVERFLOW`** across the 131-surface baseline; 33 of 74 root-level surfaces carry a wall. Worst
case, `fys_fys-treasure-trove.html`: **1,386 words / 18.15 screens** before a player can act. This
is not a contrast defect — the corpus is comparatively strong on contrast (comfort-gate pre-arm
debt was only 23/131). It is a structural habit: prose-first pages, front-loaded instructions,
because nothing gated entry paint until `one-thing-gate.py` was wired into the belt **today**, and
because the gate that was supposed to catch it was measuring the wrong screen (1280x800, a laptop)
until this session corrected it to phone-binding. A founder with retinitis pigmentosa, phone-primary,
was shipped 33 root-level pages that front-load a wall of text his own stated complaint names
almost verbatim ("a wall of directions that were irrelevant and unreadable for my phone" — his words,
quoted in the queue file itself). The gate existed. It was pointed at the wrong device for weeks.

---

## THE PHASED PLAN

### Months 1-2 — collapse redundancy, make the belt the only truth, arm what's already built

**Land first, in this order, because everything downstream depends on there being one enforcement
path, not two:**

1. **Merge `floor.yml` and `studio-belt.yml` into one workflow.** Pick the belt's per-file model
   (it already covers ticks 1-5, has ratchets with dated baselines, and is the doc-of-record per
   `STUDIO-GOVERNANCE.md`). Fold `comfort-audit.mjs`'s real-browser axe-core check into belt tick 1
   as its enforcement engine (it is measurably better than `comfort-gate.py` alone — it is the tool
   that caught `en195-arcade.html`'s real 1.08:1 violation that a hardcoded-selector predecessor
   missed, per commit `d173fa6`). Retire `gate-baseline.json`, `ratchet.py`, and `floor.yml`'s
   Pages-deploy coupling into the belt's own baseline mechanism. **Exit state: one CI file, one
   ratchet mechanism, one baseline shape, one ratchet.py or none.** This is not a nice-to-have —
   a solo founder cannot hold two red/green signals in his head and know which to trust, and a
   security/quality system that requires cross-referencing two dashboards to know if it's lying is
   worse than one honest dashboard.

2. **Fix `BUILD-DEBT.md`'s bookkeeping before adding anything else.** Backfill the session-close
   log for the twelve missing days honestly (most of it reads as legitimate GOV given ticks 3-5
   and the Aleph Fleet are real founder-ruling enforcement, not busywork — but say so in the log,
   don't pretend it didn't happen), then actually gate new governance PRs on it. If the rule is
   worth keeping, it earns a mechanical check (see the drift section) rather than a paragraph
   trusted to be read.

3. **Extend the belt to the hub's own `push`, verify it stays green, then flip on branch protection**
   on `main` requiring the belt check — this closes the exact gap `STUDIO-GOVERNANCE.md` found
   today: the belt reached the spokes' 3 surfaces and none of the hub's 131 until this session.
   Branch protection is what gives a tick agency (a HALT the founder can override by force-pushing
   is a suggestion, not a gate).

4. **Pay down the instruction-wall queue by worst-first, not comprehensively.** `INSTRUCTION-WALL-
   QUEUE.md` is already sorted worst-first. Fix the top five (`fys_fys-treasure-trove.html` at 18
   screens, `islo-hub.html`, `old-problems-at-new-speed.html`, `advantage-intake.html`,
   `confluence-massbay-assessment.html`) and re-run the ratchet after each — the baseline shrinks
   permanently per fix, which is the correct incentive shape already built into `one-thing-gate.py`.
   Do not try to clear all 52 this phase; that is a rabbit hole this same doc's own sunset clause
   would flag.

5. **Consolidate the contrast-tool family.** Nine scripts touch contrast or the floor in some form
   today: `comfort-gate.py`, `comfort-sweep.py`, `comfort-audit.mjs`, `preship-contrast-gate.py`,
   `preship-gate-v3.py`, `-v4.py`, `-v5.py`, `studio-eyes-sweep.py`, `floor-status.py`. Some of
   these are legitimately different jobs (render-proof vs contrast vs image floor); some are dead
   ancestors (`v3`, `v5` next to the belt's canonical `v4`). Audit which of `v3`/`v5` are still
   called by anything (`grep -rn 'preship-gate-v3\|preship-gate-v5' .github .claude *.sh *.py`) and
   delete the ones that aren't. A version number in a filename is a fork that never got closed.

**Why this order:** none of month 3-6's work is trustworthy while there are two disagreeing CI
systems and a governance-debt check that isn't actually checking anything. Fix the instruments
before trusting their readings.

### Months 3-4 — teach the gates the phone is not optional, and close the touch blind spot the fleet already found

1. **Fix the corpus-wide touch blind spot named today.** `studio-fingers.py` probes controls at
   page load; TSP games use `.screen{display:none}` with controls JS-built on transition. **Every
   control after a game's entry screen has never been touch-measured**, in every multi-screen game
   in the corpus. This is not a hypothetical — it is the exact shape of failure the studio has hit
   before (comfort-gate blind to fill-token text 2026-08-03, studio-eyes-sweep blind to `<text>`
   inside a `viewBox` 2026-08-07, both logged in `os-block-aleph-fleet.md`'s "hole" table). Fix
   `studio-fingers.py` to walk screen transitions, not just load state, and canary it against a
   game with a known bad post-transition tap target before trusting it again.

2. **Wire `playthrough-agent.py` and `studio-fingers.py`'s exit codes into the belt as a real tick.**
   Both were "silently dead" — failing on a Chromium build drift, printing an error, and continuing,
   which reads downstream as "nothing found." This is the exact shape as the WeasyPrint exit-2 bug
   that rubber-stamped the corpus for weeks (named in the grounding packet). A tool that fails open
   on its own crash is worse than no tool: it manufactures false confidence. Every gate in the belt
   needs the same discipline `os-block-truth-ticks.md` TICK 4 already states in prose — "a gate must
   distinguish what it PROVED from what it GUESSED" — turned into a literal non-zero exit on
   internal failure, checked by a canary in CI, not caught by a human noticing months later.

3. **Extend `one-thing-gate.py` and the belt generally to grade selectable profiles, not one theme**
   — this is the SWOT's own next move ("teach the gates adaptivity... grade each shipped profile"),
   and it belongs here because it is the natural sequel to fixing the phone-binding bug this session
   already made: the instrument now measures the right *device*; months 3-4 is where it starts
   measuring the right *profile* (WCAG floor + founder default preset + selectable alternates, per
   the 2026-08-02 amendment already codified in OS §3.1).

4. **Bring one spoke fully under the belt with branch protection live**, not just mounted. Today
   `matt-radar` has 6 green runs; `en195-apps` has been red since 2026-08-04, three days unread at
   measurement time. Pick `en195-apps` — it is public-facing and already has a known, named fix
   (`voice-slop/index.html` loads `fonts.googleapis.com`, breaking the offline floor per
   `BELT-BASELINE-2026-08-03.md`) — fix it, go green, and require the check before merge. This
   proves the cross-repo mount can hold a wall, not just report one.

### Months 5-6 — the proof point, and only the governance the proof point needs

1. **Land the SWOT's named next move: one legible PoC win.** Pick one build from the Noticing
   collection (CYL, Flok/the-console, or similar) and take it end-to-end through the now-unified
   belt, the fixed touch gate, and the instruction-wall queue, to a state an outside reader can
   evaluate without a tour guide. This is explicitly named in `SWOT-2026-08-02.md` as the missing
   external proof point and the single highest-leverage move against the "beautiful engine, no
   proof" threat. Everything in months 1-4 exists to make this month's work trustworthy, not to be
   the deliverable itself.

2. **Only add governance in this window if the PoC build's own failure demands it** — per
   `BUILD-DEBT.md`'s own rule, now actually enforced (see months 1-2, item 2). If the PoC surfaces
   a new class of defect, harden the gate that missed it (the Aleph Fleet's own "feedback tooth"
   pattern, `aleph-blindspots.json`) rather than writing a new os-block about it in the abstract.

3. **Decide, on evidence, whether the five-repo topology earns its keep.** By month 6 there will be
   real data: did any spoke actually diverge in a way the belt caught, or has the hub-and-spoke
   machinery spent six months of upkeep guarding three files that never moved? If the latter, fold
   the spokes' three surfaces into the hub and retire the reusable-workflow apparatus — a topology
   that costs coordination and returns nothing is not neutral, it is a tax.

---

## WHAT TO STOP BUILDING

**Stop shipping new HTML surfaces faster than the belt can gate them.** 131 surfaces, two months,
one person, and the belt reached zero of them until today. Every new surface is a new row in five
baseline files. The founder does not need surface 132 before surfaces 1-131 are on one consistent
enforcement path.

**Stop writing new os-block files as the default response to a founder ruling.** Thirteen exist,
four of them already missing from the one pointer meant to track them. Every new block is a new
thing that can drift out of the header, out of the manifest, out of a reader's mental model. Before
writing block 14, fold the existing 13 into the OS text (the manifest already names this as an open,
scheduled founder gate — "a mechanical merge overwrites live sections. Founder call owed" — and it
has been open since at least 2026-07-14 per the OS header's own dating). A merge that keeps getting
deferred in favor of writing the next block is the treadmill, not a rule against it.

**Stop maintaining `preship-gate-v3.py` and `-v5.py` if `-v4.py` is canon.** Confirm via grep
whether anything still calls them; if not, delete rather than archive-in-place. A dead script next
to a live one with a higher version number is exactly the "20-byte stub sitting next to the real
file" failure `COLD-START.md` already diagnosed in Drive — don't let the repo grow the same disease.

**Stop adding ticks to the belt as fast as gates get built.** The belt went from 2 ticks to 5 in
one session. That was the right catch-up move today (four founder rulings had zero enforcement),
but the next several months should not repeat the pattern of "build a gate, let it sit unwired for
weeks, then panic-wire it." A gate that isn't in the belt within the same session it's built is a
gate that will sit unwired for weeks — wire-on-build should be the default, which argues for fewer,
better gates rather than more gates plus a backlog of wiring debt.

**Deliberately leave un-gated:** the founder's own creative and voice calls, per the standing rule
this repo already states — mechanical work is delegated by default, founder rulings and voice are
not. Do not build a gate that scores "is this fun" or "is this good writing." The Aleph Fleet's own
charter says this correctly already: "It does not judge fun — that is the founder... Authored craft
is his." Keep it that way. A gate that tries to automate taste will either rubber-stamp everything
(useless) or block real craft decisions it can't understand (worse than useless — it trains the
founder to route around his own quality system).

---

## THE DRIFT PROBLEM

**The concrete failure, restated with its full evidence trail, because "governance doc went stale"
undersells it — this happened at least twice this month, at two different layers:**

1. `STUDIO-GOVERNANCE.md`, adopted 2026-08-03, claimed "the belt is present and inert by design."
   `en195-apps`'s belt run failed 2026-08-04 — one day later — and sat red, unread, until this
   session re-measured it on 2026-08-07. Four days of a false "inert by design" claim sitting next
   to a live red build.
2. `tight-spiral-studio-os.md`'s own "UNMERGED LAW" header — the mechanism built specifically to
   compensate for the OS text being frozen — has been silently missing four of thirteen os-block
   files for however long it took to write `os-block-aleph-fleet.md` and the other three (all dated
   2026-08-07 or recent) without anyone re-running the list against the header.
3. `STUDIO-COMMAND-CENTER.md`, whose entire job description is "the one doc that changes every
   session," has described a world frozen at 2026-07-13 for over three weeks.

**The common shape:** every one of these is a *prose claim about a countable, checkable fact* — a
CI run status, a file listing, a rewrite cadence — sitting in a markdown file with no mechanism
forcing the prose to match the fact. The studio's own rule already names the fix in the abstract:
*"if a rule can't be a check, it's a wish"* (`BUILD-DEBT.md`). Here is that rule made literal for
this failure class.

### The mechanism: `canon-freshness.py`, one script, three check classes, wired to the SessionStart hook that already exists

The studio already has exactly one mechanical, unskippable trigger point: `.claude/settings.json`'s
`SessionStart` hook, which today runs `funes-tendrils.py` (branch/worktree/staging drift only — a
different problem). This is the chokepoint to extend, not a new one to invent.

**Add a companion script, `canon-freshness.py`, run by the same hook, that checks three classes of
drift a human would otherwise have to remember to check:**

1. **CLAIM-VS-CI.** Any doc that asserts a CI/workflow state in prose (grep for phrases like
   "present and inert," "armed," "blocking," "disarmed," near a workflow filename) gets that claim
   checked against the actual `.github/workflows/*.yml` `on:` triggers and, where reachable, the
   latest run conclusion via `gh api` / the GitHub MCP tools already available in this environment
   (`mcp__github__actions_list`, `actions_get`). Mismatch = HALT at session open, loud, with the
   file and line. This is exactly the check that would have caught `STUDIO-GOVERNANCE.md`'s "inert
   by design" claim on day two instead of day four.

2. **POINTER-COMPLETENESS.** Any doc that names an enumerable set of files it claims to track (the
   OS header's "UNMERGED LAW" list, the Lane Registry's shelf-only list, the manifest's governed-doc
   table) gets its named set diffed against a live glob (`ls os-block-*.md`, etc.) at session open.
   Mismatch = named-but-missing or present-but-unnamed, both printed. This is a five-line diff, not
   a research project, and it would have caught the OS header's four missing os-blocks the moment
   the fourth one landed.

3. **STALENESS-BY-CLAIM.** Any of the four Cold Start resident files that self-describes its own
   update cadence in prose ("the one doc that changes every session," "rewritten at every belt
   close") gets its git `last-touch` compared against the most recent belt-relevant commit
   (governance commits, tick additions, ship lines) to that same repo. If the file has gone N
   commits or M days without a touch while the repo kept moving, flag it — not as a hard HALT
   (staleness alone isn't always wrong), but as a loud, un-ignorable session-open line, the same
   register `funes-tendrils.py` already uses for loose ends.

**Why this design and not something heavier:** it follows the studio's own stated doctrine in
`os-block-cross-lane-mount.md` §12.8 almost exactly — "do not build a sync engine, a database, or a
merge layer... addresses + flags + one HALT check." `canon-freshness.py` is the same primitive
applied to prose claims instead of file addresses: a claim is a pointer to a fact, the fact is
checkable, and the check either matches or it HALTs. It rides the hook that already fires on every
session start, costs one more Python invocation on top of the one already there, and produces the
same class of loud, structured, un-scrollable-past output `funes-tendrils.py` already produces for
its own drift class. No new infrastructure, no new lane, no new place for the founder to remember
to look.

**The test that proves it works:** run it today, cold, against this exact repo. It should print all
three of the findings in this section — `STUDIO-GOVERNANCE.md`'s stale belt claim (now already
fixed, so this becomes its canary/regression case), the OS header's four missing os-blocks (still
live), and `STUDIO-COMMAND-CENTER.md`'s three-week staleness (still live). If it doesn't catch all
three on its first real run, it isn't done — same standard the studio already holds every other
gate to (`os-block-truth-ticks.md` TICK 4: "every repair to a gate ships with a canary").

---

## WHAT I WOULD REFUSE TO DO

**I would refuse to add a sixth repo, a database, or any state store outside git for canon.** The
studio has already paid for this lesson twice — Drive's eighteen copies of `confluence-TRUNK`, the
20-byte stub sitting next to a real 9,608-byte file, the Netlify single-lane Dad Energy that almost
got declared lost. Git is content-addressed and cannot lie about what a byte sequence is; every
other lane in this studio's own history has lied at least once. Any proposal in the next six months
that adds a new place facts can live — a wiki, a database, a second git remote as "staging," a
project-management tool as source of truth — is a regression to a failure mode already paid for in
full, twice.

**I would refuse to build a "does this text read well" or "is this fun" gate**, for the reason
given in the STOP section: it is the founder's authored judgment, explicitly carved out by the
studio's own charter, and a machine approximation of taste either rubber-stamps everything or
blocks real decisions it can't actually evaluate. The belt's job is to clear mechanical rubble
before the founder's taste is spent, not to replace the spending of it.

**I would refuse to arm a new ratcheted tick flat, unmeasured, the way `floor.yml` originally was
in July** ("armed... over 104 pre-existing HALTs," disarmed, and "the exception outlived it"). Every
tick added to the belt from here forward should follow the pattern ticks 3-5 already used today:
measure the corpus first, baseline the existing debt, block only regressions, and — this is the
part that's easy to skip under time pressure — actually go back and burn the baseline down on a
schedule, not let it sit as permanent carried debt the way `gate-baseline.json`'s 131 entries risk
becoming if nothing is assigned to shrink them.

**I would refuse to let the hub-and-spoke topology grow a sixth spoke before the existing four are
proven to need the multi-repo apparatus at all.** Per structural fault 1 in the diagnosis: three
HTML surfaces across four spokes is not evidence the topology is earning its coordination cost yet.
Prove it holds a real wall in months 1-4 (the `en195-apps` branch-protection plan above) before
scaling it. A hub-and-spoke pattern is not free just because it is architecturally clean — it is
five repos' worth of CI minutes, cross-repo tokens, and reusable-workflow debugging for a one-person
studio whose scarcest resource is exactly the attention this spends.

**I would refuse to treat this consultation itself as exempt from the ratio rule.** This document is
governance. Per `BUILD-DEBT.md`'s own rule, the session that reads it owes a ship before it earns
the right to add more process on top of it — including anything in this document's own phased plan
past month 1's item 1.
