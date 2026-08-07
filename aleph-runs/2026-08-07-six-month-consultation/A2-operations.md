# SEAT: FOUNDER OPERATIONS & ACCESS — six-month consultation
*ALEPH A2. Grounded against live bytes in `walshero/TIGHT-SPIRAL-STUDIOS`, 2026-08-07. Blind to
the other four seats' output in this run by instruction — did not read `scratchpad/consult2/`
beyond this file. One prior artifact in canon, `SIX-MONTH-CONSULTATION-2026-08-07.md`, contains an
earlier "Seat 2" pass at this same question; where this consultation converges with it, that is
two independent reads landing on the same evidence, not borrowed work — noted explicitly below,
never silently.*

---

## Month-0 finding zero: this consultation is itself evidence

Before diagnosing how Matt runs the hub, one fact from `git log` bears directly on my seat's
mandate and should not be buried in a phased plan:

```
0c940a3  CLAUDE.md: standing cost-discipline rule — Matt pays out of pocket
1a09dc8  consultation: six-month panel, run inline after the parallel fleet hit the account spend limit
```

`0c940a3` is the newest commit in the repo. It records that a **5-agent parallel run of this
exact consultation already blew the account's monthly spend limit before producing output**, and
it commits the studio to a standing rule in response: no parallel subagent fleet without a
cost estimate and a go-ahead first, unless Matt already said to run full speed on that specific
task. `1a09dc8` is the successful retry — the same panel, run sequentially inline, landed in
`SIX-MONTH-CONSULTATION-2026-08-07.md`.

**This session — five seats, run as parallel Task-tool agents (`scratchpad/consult2/A1..A5`) —
is structurally the same shape as the run that already failed once.** I cannot see from inside
my own sandbox whether the orchestrator quoted a cost estimate and got Matt's go-ahead before
spawning this fleet, as the rule Matt's own repo now requires. I am not asserting it didn't
happen — that would be exactly the kind of unverified claim `COLD-START.md` forbids. But I can
say plainly: **if this run was launched without that estimate-and-go-ahead step, it is the
identical mistake happening a second time, twelve commits after the studio wrote the rule to
stop it, inside the very consultation about how to stop it.** That is the sharpest, most concrete
"month-0 diagnosis" available to this seat, because it is not inference about Matt's habits — it
is the studio's own git history, today, possibly still unfolding as this file is written.

The fix is not a new rule. The rule already exists (`CLAUDE.md`, "Cost discipline — HIGH
PRIORITY"). The fix is an orchestrator that reads it before spawning, the same way this session
was told to read `COLD-START.md` before touching anything else.

---

## Month-0 diagnosis: three concrete costs sitting under a mostly-correct doctrine

`COLD-START.md`'s shape is right and should not be reinvented: compute canon, don't remember it;
four resident files; fetch everything else from git, verify, drop. Say that plainly, because the
rest of this section is about what sits *underneath* that doctrine and still costs Matt eyes,
attention, or money.

### 1. The channel Matt actually opens on his phone still points at the wrong lane

`PROJECT-INSTRUCTIONS-paste-block.md` is the **carrier that fires without being invoked** — its
own header says so: "Instructions are the only carrier that fires without being invoked. Memory
can be crowded out; Drive files can be ignored. This block cannot — a session in this project
reads it before it does anything else." It is the mechanism for exactly the phone-primary,
one-step-at-a-time claude.ai Project chat Matt actually opens day to day, distinct from a
Claude-Code repo clone like this session.

Read today, its SESSION-OPEN block says, verbatim:

> "1. **LOAD CANON.** Pull `STUDIO-COMMAND-CENTER.md` from Drive Claude_files... via the Zapier
> `read_drive_file_content` action. That file is CANON; the `/mnt/project` shelf mount is
> FALLBACK only."

That is the **exact inverse** of `COLD-START.md` (locked 2026-07-13, "this file is law"): "Drive
is an address book. **Never canon.** It has no mechanism to prevent eighteen copies." The paste
block was last touched 2026-08-05 (`git log --follow`, commit `6e16918`) — three weeks after
Cold Start was sealed — but the touch was a lane-fidelity test ("verify base64 write path"), not
a content reconciliation. The content itself still tells every automatically-primed project
session to trust Drive over the repo.

This is not a hypothetical drift. `STUDIO-COMMAND-CENTER.md` names the exact failure mode this
would cause: Drive held "eighteen copies of `confluence-TRUNK`" and a "20-byte stub of
`studio-eyes-sweep.py` sitting next to the real 9,608 B tool," indistinguishable by inspection.
A session primed by this paste block on Matt's phone opens already pointed at the lane the
studio spent a full audit proving cannot be trusted. This is the single highest-leverage fix
available to this seat, for one reason: it requires no new doctrine, no founder judgment call,
and no reasoning about tradeoffs — it is bringing an already-fired carrier into agreement with
an already-ratified law. That makes it mechanical, and mechanical work is the machine's by
default.

### 2. Auth documentation answers the same question four times, and the newest answer is incomplete

Read in file order:
- `TSP-GIT-LANE.md` (2026-07-29): get a 7-day fine-grained PAT from Matt, wire it into the push
  URL, scrub it after.
- `HANDOFF.md` (2026-07-16): documents a PAT that leaked into a transcript and had to be rotated
  — the exact failure the founder's "secrets never touch the chat" floor exists to prevent.
- `DECISION-zapier-auth-lane.md` (2026-08-03): founder ruling — GitHub auth runs through Zapier's
  OAuth connection, auto-refreshing, never in a transcript. Supersedes hand-minted PATs.
- `TSP-NOTOKEN-LANE.md` (2026-08-06): "Supersedes the 'get a fine-grained PAT from Matt' cold-start
  step in TSP-GIT-LANE.md." The current, correct default: Zapier `github_create_or_update_file`,
  no token, no expiry, one browser "Allow" already done.

That succession is *correct* in direction — each doc is a real improvement, and the newest one
(`TSP-NOTOKEN-LANE.md`) is the right default for exactly the reason it states: "A PAT is the
worst path for RP — dense settings UI, tiny toggles, a repo picker, a recurring re-issue." But
`STUDIO-GOVERNANCE.md` (2026-08-07, same day) names a gap none of the four docs know about:
**the Zapier connector cannot write `.github/workflows/`** (no `workflow` OAuth scope, probed
2026-07-28), while **an authenticated session container can** — workflow files were written and
pushed that way the same day. Nothing in `TSP-NOTOKEN-LANE.md` says what to do when a belt tick
needs adding to a workflow file. The next session that hits this has to rediscover it from
`STUDIO-GOVERNANCE.md`'s status table, which is not where an operator would think to look for an
auth answer. Four files, one live gap, no single current pointer.

### 3. Session-stall survival is real infrastructure, already wired, and worth confirming rather than re-litigating

`.claude/settings.json` (read directly, not inferred):

```json
"hooks": { "SessionStart": [ { "matcher": "startup|resume|clear|compact",
  "hooks": [ { "type": "command", "command": "python3 funes-tendrils.py . 2>/dev/null || true" } ] } ] }
```

This is correct and already does the job `FUNES-TENDRILS.md` describes: it fires on `startup`,
`resume`, `clear`, *and* `compact` — the exact four moments a stall happens — and it is advisory
(`|| true`, and the tool itself "never guesses and never deletes, it reports"), so it cannot block
a session, only surface what a prior one left stranded. This is the actual mechanism that answers
"how does a stall get survived" and it does not need new design. What it needs is for the four
resident files to keep pointing at it, which they currently do.

The gap is narrower than "does stall-survival exist" — it is "does every entry point run it."
`.claude/settings.json` fires it for a repo clone (this environment). `PROJECT-INSTRUCTIONS-paste-block.md`
fires an entirely different SESSION-OPEN sequence for the claude.ai Project channel, and that
sequence does not mention Tendrils at all — it predates it. A stall inside a Project chat (the
channel Matt is phone-primary on) is not currently walked by anything, because the carrier that
fires automatically there has never been updated past its Drive-canon, pre-Tendrils design.

### 4. Named, quantified cost sinks (from `ACCOUNT-SURVEY-AND-BEST-PRACTICES.md`, 2026-08-05, re-confirmed by reading the same files today)

- `actions_list` dumps ~390KB and was hit three times in one session just to check a run's
  status — a status check should read `version.json` or a single scoped call, never the full log
  list.
- 520 tracked files, 110 (21%) in `rescued/`+`archive/`; three HTML files over 2MB
  (`choose-your-leader-full.html` 3.5MB, `old-problems-at-new-speed.html` 3.4MB) — every clone,
  worktree, and full sweep drags this weight even when the work touches none of it.
- `floor.yml` reinstalls weasyprint + playwright + chromium on every push with no caching —
  minutes of CI per push that a cached toolchain image would remove entirely.
- Full corpus sweeps (131 HTML surfaces × 5 gates × phone + desktop viewports) run by default
  in places a scoped `git grep` or a changed-files-only pass would answer the same question for
  a fraction of the cost — this is now also `CLAUDE.md`'s own written rule ("scope sweeps to what
  changed").

None of these four are new findings — they were already surveyed and written down. What is new
is confirming, by reading the files myself rather than trusting the survey's date, that none of
them have been acted on yet: the 2MB files are still 2MB, `floor.yml` still has no cache step,
`rescued/` is still 21% of the tree. A survey that sits unactioned for two days is not a fix; it
is one more prose file competing for the founder's attention with everything else.

---

## The operating loop recommended

Keep Cold Start's shape. Do not add a competing doctrine. The fix is making the loop actually
run on **every** entry point Matt uses, not just the one this session happens to be in.

```
SESSION OPEN (repo-clone / Claude Code lane — already correct, confirm not rebuild)
  1. Read the four resident files (COLD-START.md, tight-spiral-studio-os.md,
     STUDIO-COMMAND-CENTER.md, LANE-REGISTRY.md + cross-lane-manifest.md).
  2. funes-tendrils.py fires automatically via SessionStart hook — no step to remember.
  3. Surface at most ONE decision if anything is founder-owed: pull the "OPEN — FOUNDER ONLY"
     block already maintained in STUDIO-COMMAND-CENTER.md and lead with the single item at
     the top, phrased as yes/no/pick-one — not the whole block, not a doc to read end to end.

SESSION OPEN (claude.ai Project / phone-primary lane — currently WRONG, fix first)
  1. Rewrite PROJECT-INSTRUCTIONS-paste-block.md's step 1 so it matches ratified law:
     canon = repo (raw.githubusercontent.com or `git show origin/main:<path>`), Drive
     is address-book/fallback only — inverted from what it says today.
  2. Add a Tendrils-equivalent call for this lane (funes-tendrils.py needs a git working
     tree; a Project-chat session has no local clone, so this likely means: on open, fetch
     STUDIO-COMMAND-CENTER.md's "OPEN — FOUNDER ONLY" section from the repo, not from Drive,
     as the decision-surfacing step). This is mechanical text-editing of an existing file
     to match existing law — no founder judgment required, do it unasked.

SESSION WORK (both lanes)
  4. Mechanical work proceeds unasked: byte-verification, gate runs, pushes via the Zapier
     no-token lane, doc-and-code cleanup that implements an already-ratified rule.
  5. Any destructive or consequential action gets exactly ONE plain-language confirmation.
     Never a menu, never "which of these three options."
  6. A workflow-file (.github/workflows/) change is the one write path Zapier cannot take —
     route it through the authenticated session-container git lane per STUDIO-GOVERNANCE.md's
     2026-08-07 finding, and say so in one sentence, not as a blocking mystery.

SESSION CLOSE (both lanes)
  7. Land everything in a real lane before the turn ends — never "ready to paste,"
     never left in outputs/. This is already CLAUDE.md's "Never end on a ready-to-paste
     handoff" rule; it just needs to be true of the Project-chat lane too, which currently
     has no push mechanism of its own and depends on a human copying text.
  8. Byte-verify: pull it back, match the hash. "success:true" is never proof.
  9. Report short: what changed, what's owed, nothing else. No repeated reminders — "say it
     once" is already a founder ruling (TSP-GIT-LANE.md, 2026-07-29).
```

**Auth, collapsed to one current sentence, to replace the four-document sprawl:** *GitHub writes
default to the Zapier OAuth connection, no token, ever — for `.github/workflows/` specifically,
use an authenticated session container's git push instead, since that path is the one the OAuth
grant cannot reach; a founder-generated PAT is the last resort named in `TSP-NOTOKEN-LANE.md`,
generated on the Mac, entered off-transcript, never pasted into chat.* That is not a new
doctrine — it is `TSP-NOTOKEN-LANE.md` plus `STUDIO-GOVERNANCE.md`'s one correction, landed as a
single edit to the newest file rather than left as a fact only findable in a status table.

---

## Phased plan

### Months 1–2
- **Fix `PROJECT-INSTRUCTIONS-paste-block.md`'s canon source** (Drive→repo inversion, above).
  This is the single highest-leverage change available: it corrects the automatically-firing
  carrier on the channel Matt actually opens phone-primary, and it costs one file edit.
- **Consolidate the four auth documents into one current answer**, folded into
  `TSP-NOTOKEN-LANE.md` (newest, closest to correct) rather than a fifth file. Archive the
  superseded three with a one-line pointer, per the studio's own "one source of truth per
  concern" practice.
- **Action, not re-survey, the four named cost sinks**: cache `floor.yml`'s toolchain install,
  move `rescued/`+`archive/` off the hot path (git tag or separate branch, not deletion — the
  morgue stays provenance), split or LFS the two 2MB+ HTML files, replace any remaining
  `actions_list` status checks with the scoped alternative already named. These are mechanical,
  cheap, and each one directly reduces the per-session token/compute cost this seat is charged
  with watching.
- **Confirm, don't rebuild, funes-tendrils' SessionStart wiring** — it is already correct; the
  only open item is extending an equivalent decision-surfacing step to the Project-chat lane
  (above), not redesigning the repo-clone lane.

### Months 3–4
- **Arm branch protection** (`STUDIO-GOVERNANCE.md`'s own "Arming" section, step 2): require the
  studio-belt check before merge, once, with Matt's token, off-transcript. This is the single
  highest-leverage *one-time* founder action left in the whole operating loop — it converts five
  already-ratcheted ticks from advisory to an actual wall, and after that one action it asks
  nothing further of him. Everything after arming is machine work.
- **Re-run `ACCOUNT-SURVEY-AND-BEST-PRACTICES.md`'s cost section once**, not as a fresh audit but
  as a check that the Month-1-2 fixes actually landed — a survey that never gets re-checked is
  itself a stale-doc risk, the same class of failure `STUDIO-GOVERNANCE.md` diagnosed in itself.
- **Decide the workflow-file write path formally**: either get Matt's token the `workflow` scope
  it currently lacks (removing the two-path split entirely) or keep the authenticated-session
  fallback as permanent policy and document it as such in the consolidated auth file. Founder
  call — see below.

### Months 5–6
- **If the studio adopts a productization or second-user direction** (a call belonging to other
  seats, not this one), this is where a second operating loop — one that isn't built entirely
  around Matt's own phone and own judgment — would need to exist. Not before. Building that loop
  now, for a studio with one user, would itself be governance-without-shipping.
- **Re-measure whether the four-file resident shelf is still four files.** Cold Start's own
  arithmetic is the check: if resident state has crept past four files by month five, that is
  the signal to prune, not to rationalize a fifth.

---

## What becomes a standing routine vs. what stays ad hoc

**Standing, no founder attention required once wired:**
- `funes-tendrils.py` at every SessionStart (already true, repo-clone lane).
- Byte-verification after every push (already true, keep it — "success:true is never proof").
- The single-decision-card surfacing of `STUDIO-COMMAND-CENTER.md`'s "OPEN — FOUNDER ONLY" list
  at session open, both lanes, once the Project-chat lane gets it too.
- Scoped, changed-files-only gate runs by default (`CLAUDE.md`'s own new rule); full sweeps
  reserved for pre-ship or after a gate's own teeth change.

**Ad hoc, deliberately, never automated:**
- Which debt item gets fixed next (instruction walls, dead buttons, the nine unmerged OS-block
  section collisions) — that is craft judgment. Automate the ranked list, never the pick.
- Any GATE 1 cold-phone-play verdict — undelegatable by the studio's own repeated naming of it.
- The lane-count question itself (repo-only vs. four-lane vs. eleven-lane canon doctrine) — three
  documents currently claim to be "law" with three different lane counts
  (`COLD-START.md` = repo alone; `LANE-REGISTRY.md` = four; `FORKING-PATHS-PROTOCOL.md` = eleven),
  none marked superseded by the others. That is a founder decision, not a session's unilateral
  cleanup, precisely because Forking Paths was itself a founder ratification (2026-08-03) — an
  agent retiring it on its own authority would be the same class of overreach this seat exists to
  prevent in the other direction.

---

## What I would refuse

- **I would refuse to spawn or continue a parallel multi-agent fleet without a cost estimate and
  an explicit go-ahead**, even when the task is dressed as "a consultation" — the studio's own
  newest commit exists specifically because that exemption was assumed once and cost real money.
  A consultation about cost discipline is not exempt from cost discipline; if anything it is the
  worst possible place to skip the quote.
- **I would refuse to hand the founder a raw PAT-generation flow as any kind of default.**
  `TSP-NOTOKEN-LANE.md` already names why: dense settings UI, tiny toggles, a repo picker, a
  recurring re-issue, all hostile to an RP phone user. The Zapier OAuth lane is correct and
  should stay the answer for everything except the one documented gap. If that gap needs closing
  with a token, it goes in through Zapier's config UI, off-transcript, exactly as
  `DECISION-zapier-auth-lane.md` already rules — never pasted into a chat.
- **I would refuse to leave a founder-owed decision reachable only by reading a multi-page doc
  end to end.** Every item currently sitting in `STUDIO-COMMAND-CENTER.md`'s "OPEN — FOUNDER
  ONLY" section, the nine unmerged `os-block-*.md` section-number collisions, the Writerly Moves
  two-taxonomy question, the CYL × Viscosity five calls — all of these are already correctly
  named as undelegatable. What I refuse is leaving them as prose a founder with RP has to scan
  for, rather than as single yes/no/pick-one cards a session surfaces unasked.
- **I would refuse to build a second dashboard or UI for any of this.** `matt-radar` already
  exists as the private lane; a second interface layer is governance weight with no shipped
  capability behind it, which is exactly what `BUILD-DEBT.md`'s ratio rule exists to block.
- **I would refuse to treat "the founder is the single point of judgment" as a problem to solve
  by diluting his judgment.** The fix this seat recommends throughout is making his judgment
  *cheaper to exercise* — fewer screens, one decision card instead of a document, no token
  hunting — never replacing it with a second authority. That is a studio-wide floor, not just an
  operations preference: `CLAUDE.md` already says the mechanical half is the machine's and
  founder rulings, creative calls, and voice are not. This seat's whole recommendation set is an
  application of that one line to the operating loop, nothing more.
