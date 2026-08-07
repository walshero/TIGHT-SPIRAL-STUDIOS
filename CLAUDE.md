# CLAUDE.md — standing notes for this repo

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

## Sharing & privacy — settled, do NOT re-litigate
Faculty email addresses, **published** student work, and the Confluence pages are
fine to share publicly. These are **not** privacy/PII concerns here. Do not flag
them, do not ask about them, do not hedge on them. The founder decides what gets
shared. (This was asked and answered too many times — it is settled.)

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
