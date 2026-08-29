# CLAUDE.md — standing notes for this repo

## COMFORT WORK IS PAUSED — founder ruling, standing (2026-08-29)
**No build asks the player about their preferences. No comfort button, no light row, no
text-size row, no legibility panel. No walls.** One universal home: one palette, one type
scale, one dark rule, the same everywhere.

- **Do not start** a new palette, light mode, type-scale experiment or comfort-kernel
  version. Existing kernels are frozen as they stand. The pause lifts only when the
  founder lifts it in writing.
- **Delete the WALL, never the KERNEL.** The wall is the UI that asks. The kernel is the
  CSS that responds to `data-light` and holds the contrast floor — `comfort-gate.py`
  measures the kernel and never clicks a control, so removing walls keeps the belt green.
  Proven 2026-08-29 on `choose-your-leader-nixon-slice.html`: wall out, gate still passes.
- **The default must now be excellent**, because the player has no escape hatch left.
- **Confluence is exempt** — dashboards may keep preference controls.

Full ruling and the scope note (two dialects, 67 surfaces, 4 above the 1 MB ceiling):
`tight-spiral-studio-os.md` §3.1.1.

## Cost discipline — HIGH PRIORITY, standing (2026-08-07)
**Matt pays for this out of pocket, as a teacher.** Credit usage is a real constraint on
every session, not an afterthought — this already burned a monthly spend limit mid-session
on 2026-08-07 (a 5-agent parallel consultation fleet died before producing any output).
Default posture from here forward, every session, no exception:

- **Default model: the cheapest tier that can do the job.** Do not assume Opus. If a
  session opens on Sonnet, stay there — only ask to escalate when a task's reasoning
  depth genuinely needs it, and say why in one sentence.
- **No parallel subagent fleets without asking first, and a cost estimate before asking.**
  Each parallel Agent/Workflow spawn pays full context overhead again — system prompt,
  tool schemas, re-grounding reads — so 3-5 agents can run 5-10x the cost of one inline
  pass at the same depth. Before spawning more than one subagent, or any Workflow call,
  give a one-line estimate (agent count, rough token order of magnitude) and get a
  go-ahead — unless Matt has already said to run full speed on that specific task.
- **Prefer inline work over subagents whenever the session already holds the grounding.**
  If the answer is reachable by reading or grepping a few files directly in this
  conversation, do that. Don't spin up an agent to re-derive context already in hand —
  proven cheap and sufficient on 2026-08-07 (a 5-seat panel run inline on Sonnet, after
  the same panel as five parallel agents had failed).
- **Scope sweeps to what changed; don't default to the full corpus.** A full-corpus gate
  sweep (100+ surfaces × several gates × multiple viewports) is expensive per run. Run it
  against changed files first. Only sweep everything when something structural moved (a
  gate's own teeth, a threshold) that could affect files outside the changed set.
- **Don't re-read a large file already summarized in this session's context.** Grep for
  the specific section instead of reading a 2,000+ line doc end to end a second time.
- **When in doubt, quote the budget before spending it — not after.** State the estimated
  scope (agent count, sweep size, rough token order of magnitude) before committing,
  the way a contractor quotes before starting work, not after the invoice.

This is not a call to work slower or timider. It is matching the tool to the job, and
asking before reaching for the expensive tool when a cheaper one would do the same work.

**Reaffirmed 2026-08-08, standing preference — factor this into every turn, not just
big ones.** Matt's own words: *"Don't stray from optimal work, but factor account
credit usage or I get locked out."* Two things, both true at once, neither cancels
the other:
- **Quality doesn't drop.** This is not permission to cut corners, skip verification,
  or ship something worse to save tokens — "optimal work" stays the bar on every task,
  including the ones in this file (belt runs verified against the literal PASS/HALT
  line, gates self-tested, nothing landed unverified).
- **But the account-lockout risk is real and already happened once** (2026-08-07,
  mid-session). So the check above the checks: before any parallel fleet, any full
  corpus sweep, any large re-read — ask "is this the cheapest path to the SAME
  quality bar," not "is this the most thorough thing I could possibly do." Thoroughness
  bought with tokens Matt doesn't have to spend isn't optimal work, it's a lockout
  waiting to happen.

## Session-close lane sweep — standing (2026-08-08)
`funes-tendrils.py` walks git mechanically and now names, on every run, the 5 lanes
no CI sweep can reach (`lane-tendrils.json` is the registry). The session-connector
lanes are THIS session's job at close, connectors permitting and cost-scoped (a
spot-check, not an audit):
- **Spoke repos** — anything unmerged/stranded on the 4 spokes' branches.
- **Google Drive** — any TSP file modified more recently than its repo counterpart
  (the v48-trunk loss shape). Drive is an address book; real work found there is a
  loose end by definition.
- **Zapier** — deploy-studio-file skill still points at GitHub Pages.
Human-only lanes (project shelf, chats) can't be swept by anyone: mitigate by
harvesting anything that matters into a repo doc BEFORE the chat closes, and a KD!
ledger line for whatever landed only on the shelf. Skipping the sweep is allowed
when cost or connectors dictate — but say so out loud; blind is not clean.

## Panels — the Union Rep is seated, with advocacy weight (2026-08-08, raised same day)
Any studio work that convenes a panel follows the OS's "Panelist Union Rep" block
(§5), four duties: **caucus** first (consult the OS benches, patterns, ledger, the
wings — prop room, elves, eyes/fingers, tendrils — and the grievance record before
proposing a bench); **advocate with agency** (the Rep proposes the bench and argues
for underused talent and standing assets the work should mount instead of
reinvent — accountably: Rep-seated seats are recorded); **roll call** at seating
(every seat names its real method AND its planned scrub-in); **grievances** at
close (`GRIEVANCE: <seat> seated, never scrubbed in` in the KD!/ledger entry;
three grievances, no contributions → governance-attic candidate). A designated
agent form exists (`.claude/agents/union-rep.md`) for heavy seating decisions,
wings-and-talent audits, or grievance reviews — inline by default, one agent
never a fleet, cost discipline binds it. Seats are lenses, not authorities; the
Rep included.
Faculty email addresses, **published** student work, and the Confluence pages are
fine to share publicly. These are **not** privacy/PII concerns here. Do not flag
them, do not ask about them, do not hedge on them. The founder decides what gets
shared. (This was asked and answered too many times — it is settled.)

## Deliverables & durability — standing (2026-08-08)
- **Phone-first delivery.** Anything handed to Matt defaults to a downloadable
  attachment or a URL (raw GitHub link, canonical once merged) — never an inline
  render-only view. He reviews from a phone; a render-only panel can't be copied,
  selected, or downloaded there. A deliverable he can't move is not delivered.
- **Make work stick, whenever possible.** Any decision, preference, instrument,
  or promise made in conversation lands in canon (this repo) the same turn it's
  made. A rule stated only in chat, a ledger line promised "at close," a
  preference acknowledged but not written — each is a loss waiting for a
  compaction or a dead battery. When something genuinely must stay pending (a
  founder call not yet made), write the PENDING state itself into the tracking
  doc, so the next session inherits the question instead of silence.

## Founder's creative work is available to the studio - standing (2026-08-28)
Founder's words: *"Draw from my creative work. I'll say no if it doesn't work."* Broadening
an earlier same-session grant (*"You can use Monserrat and China gold"*). His own poems,
flash and drafts may be drawn on for text banks, practice pieces and game content. **He
holds the veto per piece**, so mount work with its title and provenance visible and expect
individual pieces to come back out.

Three things this does NOT change:
- **Student work stays closed.** The 2026-08-10 ruling ("Don't draw from student work
  unless specifically authorized by me") is untouched. This grant is about HIS writing.
- **Reproduce exactly, slips included.** Several pieces are drafts. Do not silently correct
  a tense slip, a doubled word or a missing quotation mark; those are often the most useful
  thing in a practice piece, and correcting an author's draft without asking is the machine
  overwriting the author.
- **Name the draft as a draft.** A piece shown to students as a finished exemplar when it is
  a club-session draft teaches the wrong lesson, which is the same defect flagged in the
  Station Seven "Model Text" file.

Source: the *Creative writing club* folder in Drive. Five pieces are mounted in
`claude/LENS-REGISTRY-AND-PRACTICE-BANK-2026-08-28.md` (§B5).

## Art: the studio-cut lane is open - founder rule, standing (2026-08-27)
Founder's words, asking for a game: *"And we want art."* The MJ lane closed 08-13 and
licensed photography cannot ride in an offline single-file game, so for two weeks the
only compliant build was a build with no art. `art-gate.py` now has a THIRD lane:

- **STUDIO-CUT** - art cut in the studio, marked `data-art-class="studio-cut"`, and
  **proved by `art-execution-gate.py`** rather than by its own label. art-gate runs the
  execution gate on the file and HALTs if it HALTs, measures no scene, or cannot open a
  browser. A marker that clears a gate by being present is a gate gone blind.

This is not a reversal of the 08-01 ban. That ban was a proxy for a quality bar nobody
could measure; the execution gate measures it now (type dominance, cross-hatch, flat
layers). Bad hand-cut art still does not ship - it now fails for being bad rather than
for being hand-cut. Full ruling: `claude/RULING-STUDIO-CUT-ART-LANE-2026-08-27.md`.

## Status ladder - founder rule, standing (2026-08-27)
**LAB is a real status and most builds belong in it.** Founder's words: *"Many games
have to be placed in lab status. All the cliche cowpath games - put in lab not as done
game."*

The ladder, in order: **Lab** (real, playable, an experiment kept on the bench on
purpose - allowed to fail the gates) -> **In build** (worked on right now) -> **Live**
(playable end to end, gates green, the studio stands behind it) -> **Full production**
(the measured state in `production-gate.py`).

Two rules that bind:
- **State the status on the surface, not only on the face.** A `.tsp-lab` chip inside
  the `<h1>`, same position and style floor as the version chip. A player who opens a
  build from a bookmark never sees index.html.
- **No promotion by relabelling.** A Lab build reaches Live when the gates go green and
  somebody plays it, never by editing a chip.

Full ruling, the ladder table, and the PENDING sweep question: `claude/RULING-LAB-STATUS-2026-08-27.md`.

## Version on the surface - founder rule, standing (2026-08-23)
**Every build states its version beside its title, on the screen.** Not only in a commit
message, not only in a file comment. Founder's words: *"From now on, include version
numbers clearly on app next to title."*

The pattern, as shipped in `funnybonies/index.html` v8.1:
- a `.ver` chip inside the `h1`, e.g. `<h1>Funny Boney's Factory <span class="ver">v8.1</span></h1>`
- the same version in `<title>`, so a screenshot identifies its own build
- the same version in the file's build banner comment
- all three must agree; a build that disagrees with itself about its version is worse
  than one that says nothing

Style floors still bind: the chip is 20px, uses `--hot-ink` (which clears 4.5:1 on paper
and on the dark ground), and never wraps away from the title.

**Why it is a rule and not a preference:** a version you cannot see from the phone you are
holding is a version nobody can report a bug against. The founder reviews on a phone, often
from a bookmark, sometimes against a stale CDN copy. Without a visible version there is no
way to tell "this build is wrong" from "I am looking at last week's build" - which is
exactly what happened on 2026-08-23, when v8 sat on main for a day while the live site
served v7 and nothing on either screen said which was which.

TICK 12 CANDIDATE (not built): a grep for a version token beside the title. Deliberately
not built the same day as TICK 11 - the recursion loop's rate governor allows one graduation
per build, and TICK 11 graduated 2026-08-22.

## Deploy lanes
- **git / GitHub Pages is the primary lane.** Ship here by default.
- **Netlify is one-off sharing only** — nothing the studio depends on. Prefer git
  over Netlify whenever there is a choice.
- The Zapier "deploy studio file" skill also targets GitHub Pages.

## What the studio is (as of 2026-07)
- The **studio is the engine**; specific assets are downstream deliverables with
  their own distribution points. Current phase: **proof of concept**.
- Focus is ~**9:1** — building the studio (engine / OS / quality tooling) over
  individual asset builds.
- The engine's moat is the quality layer: the ratchet, Studio Eyes (render), and
  Studio Fingers (touch).

## Face
- `index.html` accounts for **every** page in the repo — nothing is orphaned.
  Keep it that way: new pages get linked from the face.

## Voice — settled
- **No invented or inflated claims.** Use the founder's actual words; if a claim isn't
  in his docs or this session, don't write it.
- **Make NO claim about blind players being able to play the games.** There is no playtest
  or evidence behind it and the founder does not assert it. Do not write that a blind
  player/student "can play," that their version "is the game," or that blind and sighted
  players "play the same way." The only defensible framing is the founder's retinitis
  pigmentosa and an accessibility-first design *intent* — never an outcome claim about blind play.
- **Pull back on disclaimers as a rule** — hedges, caveats, safety-flags, "note:" asides,
  in prose and in files. Say the thing plainly. Caveat only when it is load-bearing.

## Canon vs shelf — settled (2026-08-03)
- **The Claude Project shelf is a CACHE, never the finish line.** A deliverable that only reached the shelf is NOT done — the shelf lags this repo and is not canon.
- **Default to canon.** Land docs, decisions, and builds in this git repo via the "deploy studio file" skill: the authenticated GitHub connector — `get_file_contents` for the SHA, `create_file` / `apply_patch_to_repo_file` / `append_chunk_to_repo_file` to write, then raw-verify. `git push` from a session container is blocked (403); the connector is the working lane and needs no open tab.
- **Never end on a "ready-to-paste" handoff** when the connector can land it. Paste-handoffs die by closed tab or dead battery. Write it to canon, verify the bytes, then tell Matt what landed.

## CHECKED IS NOT SHIPPED - standing, non-negotiable (2026-08-27)

**Never report a push as landed on the strength of a connector's success message.**
A green result is a claim about what a tool did. It is never proof of what arrived.

The procedure, every connector write, no exceptions:
1. **Assert on the way out.** Pass `expect_total_bytes` with the byte count of the
   verified local file. The connector refuses the write on a mismatch. This already
   saved a recovery push that was 63 bytes short of the file it claimed to be.
2. **Compare on the way back.** Run `./verify-push.sh <path>...`. It fetches the
   remote and compares content hashes against the verified local file. Content
   identical or it HALTs.
3. **Say nothing about shipping until step 2 prints clean.**

**Why this is a rule.** On 2026-08-27 a connector write sent the literal string
`PLACEHOLDER` as file content and destroyed `funnybonies/index.html` on main. The write
succeeded and returned a commit sha. Nothing objected, because every gate in this repo
grades a file in a working tree and none of them can see the moment of transmission:
`git push` is blocked from the sandbox, so bytes are RETYPED into a tool call rather
than moved mechanically.

**The failure class, which this repo hit four times in three weeks:** the 18 day deploy
outage (checked the belt, not the live URL), Site Watch reporting SUCCESS over a stale
site (checked liveness, not freshness), seven Funnybonies builds passing every tick while
being the wrong game (checked the artifact, not the intent), and PLACEHOLDER (checked the
local file, not the bytes sent). **The thing that was checked was not the thing that
shipped.** Full account: `TSP_Ledger.md`, 2026-08-27.

**Corollary, and it generalises past the connector:** for anything that leaves this
sandbox, verify the ARRIVED artifact, never the sending. Landing bytes on main is not
shipping, so check the live URL. Publishing an artifact is not rendering, so confirm it
opens. This is the belt's oldest law pointed one step downstream: a gate that has gone
blind must never read as clean, and a gate that was never looking at the shipped
artifact was blind the whole time.

**Not a belt tick, on purpose.** The belt reads files in a tree and cannot see a tool
call. Not every lesson becomes a tick; some failures live outside what the belt can look
at, and pretending otherwise produces gates that grade the wrong thing.
