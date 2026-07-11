# SELF-DIAGNOSIS — TSP, 2026-07-11
**Written after a session that produced excellent repairs on the wrong file.**
**Grounded in outside practice, not in more studio invention.**

---

## THE DIAGNOSIS IN ONE LINE

**The studio keeps solving governance problems that git already solved in 2005, and the
one problem git cannot solve — knowing which artifact is canon before you open it — has
no gate on it at all.**

---

## PART 1 — WHAT ACTUALLY WENT WRONG TODAY

I spent a full session applying good work (loom→irrigation, stale-ISLO fix, three open
questions) to `confluence-TRUNK.html` **v34**. Canon was **v43**, in the repo, nine
versions ahead.

The file that would have told me this — `confluence-TRUNK-POINTER.md` — **already existed
in Drive Claude_files**, already said "canon is v43, here is its md5, here are the fossils
by ID," and **already named the exact v34 file I was editing as superseded.**

It was four tool calls away. I never opened it.

**The system was not broken. There was no gate forcing me through it.**

Three compounding failures:

1. **The session-open card demotes the mount in general but not per-file.** It says "the
   Command Center is truth, mount is fallback." It does not say *"before touching any file,
   resolve its canon address."* A general rule failed to fire on a specific case.
2. **The mount is seductive.** `/mnt/project/` is instant, always available, and always
   stale. Reading it *feels* like diligence. It is the opposite.
3. **A search returned zero and I believed it.** `name contains 'onfluence'` returned
   nothing while two matching files sat in the folder. The pointer file itself already
   records this exact lesson (about `conversation_search` and "phantom v42"). **The same
   failure recurred today in a different tool.** That is a class, not an instance.

---

## PART 2 — WHAT THE OUTSIDE WORLD ALREADY KNOWS

I went looking for how people who solved this actually solved it. Four findings, and
three of them indict the studio's current approach.

### FINDING 1 — "Version drift" is a named, studied problem with a known cause

The literature is blunt: *"Every product organization has said it: 'We need a single source
of truth.' Yet in most teams, that truth quickly fractures."* Documentation research
(Dasanayake et al., 2019) links even small artifact mismatches to higher defect rates and
schedule slips. The diagnostic questions are exactly the ones TSP fails:

> *"Can you identify the authoritative source for each artifact (and who owns it)?"*

Today: **no.** Three copies, no ownership, whichever one I opened became canon by accident.

The prescribed fixes are boring and known: **clear ownership per artifact · treat docs as
code (version-control them) · automate the pipeline · make the source authoritative and the
copies generated.**

**The studio has all of these written down and none of them enforced.**

### FINDING 2 — SSOT kills the "save as" workflow, and that is precisely the studio's disease

From the technical-documentation world: SSOT *"eliminates the 'save as' workflow that causes
version drift, duplicate translations, and release-day chaos."* The failure mode named
there is exactly ours:

> *"A subject matter expert might approve a specification in one manual, completely unaware
> it's been copied into twenty others. And underneath all of this: nobody actually knows
> which version is authoritative."*

**TSP is a save-as shop.** Confluence exists as: shelf v18, shelf v34, Drive v33 fossil,
Drive "confluence-TRUNK 2.html" v34, repo v43, plus per-chat `outputs/` copies. Six-plus
locations. **The pointer pattern (OS §12: "canon is an ADDRESS, not a copy") is the correct
cure and it is already written — it is just not enforced at the moment of edit.**

### FINDING 3 — Content-addressing is the mechanical answer, and git gives it free

Git is *"a content addressable filesystem"* — every object is named by the hash of its
content. The property that matters: *"Integrity checking is easy. Bit flips are easily
detected, as the hash of corrupted content does not match its name."*

Research on build systems makes the sharper point — **timestamp-trusting validation is
unsound; content-checking is sound.** In the OxyMake benchmark, bumping a file's mtime
without changing a byte caused a timestamp-trusting system to re-run **6,667 jobs**; a
content-hashing system re-ran **zero**.

**Translation for the studio:** "newest file" and "the one on the shelf" and "the one I
have open" are all mtime-style heuristics. **They are unsound.** The only sound question is:
*does this file's hash match the hash canon claims?*

**The pointer file already stores the md5.** Nobody checks it before editing.

### FINDING 4 — This is a *solved* problem in the AI-agent world, and the fix is the SAME

The Claude Code ecosystem hit this wall hard and converged on one answer. Anthropic's own
guidance: *"the goal is to make session boundaries cheap by ensuring the important knowledge
is persisted in files, not trapped in conversation history."*

The failure mode has a name — **context rot** — and the symptoms are ours exactly:
*"The agent starts contradicting earlier decisions. It introduces patterns you already
discussed discarding."*

And critically, the community found that **more instructions do not fix it.** From a
practitioner who tried:

> *"My first attempt to fix this was naive. I told every agent to read every document. As
> you would guess, that blew up my context window in fifteen minutes. At some point I
> stopped blaming the agents and started looking at the setup itself. They weren't the
> issue. The way I was asking them to work was. So what I needed wasn't sharper instructions
> or clever prompt tricks. I needed a place where the memory lived, separate from the agents
> doing the work. Something steady. Maybe boring. A file, basically."*

**"Not sharper instructions. A boring file."** That sentence is the whole diagnosis of TSP.

Their working protocol, distilled: **a registry that is checked BEFORE work begins.**
*"Never recreate. Before invoking agents: 1. Check project registry for relevant prior work.
2. Read relevant reports. 3. Provide complete context."*

**TSP has the registry (pointers, Command Center, Drive Atlas). TSP has no rule that says
CHECK IT FIRST.**

---

## PART 3 — THE HARD FINDING ABOUT THIS STUDIO

Memory already names it: **SPEC-RICH, BUILD-POOR.** Today proves it is worse than that.

**The studio is GOVERNANCE-RICH and ENFORCEMENT-POOR.**

Look at what exists on paper vs. what actually fired today:

| Written down | Fired today? |
|---|---|
| OS §12: "canon is an ADDRESS not a copy" | **No** |
| `confluence-TRUNK-POINTER.md` with md5 + fossil list | **No — never opened** |
| Fork-diff rule: "never default to the older file; diff content first" | **No** |
| SOURCE-FIRST LOCK: "open the actual file FIRST, search is a fallback" | **No** |
| Session-open card: "mount is fallback only" | **Partially** |
| POST-TICK byte-verify | **YES — and it is the only reason the clobber was caught** |

**One gate out of six fired.** The one that fired was the only one that was *mechanical* —
a byte-check that either matches or does not. Every rule that depended on **remembering to
follow it** failed.

This is the same lesson the studio already learned about contrast and wrote down:

> *"Contrast is a COMPUTATION, not a judgment — eye-inspecting hex codes let the same
> amber-as-text bug survive three 'checks' and it died instantly to arithmetic. Matt has RP,
> contrast cannot be a step someone remembers."*

**Canon is a COMPUTATION, not a judgment.** It cannot be a step someone remembers either.
The studio proved this principle, wrote it down, and then did not apply it to the one thing
that matters most: *which file am I editing.*

**And today I minted four MORE ticks** (SOURCE-COUNT, AUTHORITY-BY-CLAIM-TYPE,
REFERENCE-STALENESS, AUDITOR-IN-CRITICAL-PATH) — three of which are behavioral, i.e. things
someone must *remember*. **I responded to an enforcement failure by writing more rules.**
That is the disease treating itself as the cure.

---

## PART 4 — WHAT TO ACTUALLY DO (smallest thing that works)

### THE ONE FIX: make canon mechanical, not remembered

**`resolve_canon(name)` — a single Zapier code action.** Not an agent. Not a framework.

```
resolve_canon("confluence-TRUNK")
  → canon_lane: repo
    address:    raw.githubusercontent.com/walshero/…/confluence-TRUNK.html
    version:    v43   bytes: 597191   md5: bed8c7a3…
    fossils:    [Drive 1ndz… v33, Drive 1fZR… v34, shelf mount v34]
    owner_lane: Confluence (RW)
```

It reads the `*-POINTER.md` files that **already exist**. It is a lookup, not an inference.
Implementation: an afternoon.

**THE GATE (this is the part that matters):**

> **No file may be edited until `resolve_canon` has returned for it in the current session,
> and the working copy's md5 matches what canon claims.** A hash mismatch is a **HALT**,
> identical in force to a failed contrast check.

That single gate would have stopped today's entire session at minute two. Not with a
reminder — with a **refusal**.

### The three supports (all already half-built)

1. **Pointers for every trunk.** `confluence-TRUNK-POINTER.md` is the working template.
   Clone for CYL, OS, Studio Eyes, Leeder. Pointers are small → they pass the Drive bus.
   Trunks are big → they live in the repo, which has **no size limit**. This is already
   correct and already proven.
2. **The zipper.** Walshero Drive `Claude_files` = the junction where every lane's canon
   *address* lives. Not a backup folder. **Confluence gets its own Claude Project** — off
   the TSP shelf, which is over-full and is itself a drift generator.
3. **AUTO-DRIVE / AUTO-PUSH at creation** (TICK 5). Small → Drive bus. Oversized → git-push
   (proven byte-exact today). Un-pushable → flagged **LOUDLY** as un-backed-up, never
   silently. The corrected Confluence build sat in `/tmp` for **nine turns** today and
   would have evaporated unasked.

### What to STOP doing

- **Stop minting behavioral ticks.** The studio has more rules than it can execute. Every
  new "remember to…" is a rule that will fail exactly when it matters. **If a rule cannot
  be a check, it is a wish.**
- **Stop trusting zero-results.** A search returning nothing is not evidence of absence.
  It has now lied twice (Drive today; `conversation_search` re: v42). **When a search comes
  back empty, list the container and look.**
- **Stop reading the mount as canon.** It is a cache. It lags. It is the single most
  reliable way to do good work on a dead file.

---

## PART 5 — THE HONEST LEDGER FOR TODAY

**Real wins, and they are not small:**
- **Studio Eyes genuinely repaired** — six grounding bugs (CSS comments glued to selectors
  was the root cause). Shelf HALTs **42/57 → 20/57**. Twenty-two files were blocked by an
  auditor that was wrong.
- **The auditor now separates PROVEN from GUESSED.** Grounded failure → HALT. Unresolvable
  → WARN/UNGROUNDED. It no longer cries wolf.
- **Canary shipped.** Every gate repair now must prove it still catches the real bug.
- **Nothing was lost.** v43 restored byte-exact; the clobber reverted.

**The cost:**
- **A full session of Confluence work applied to a nine-version-stale trunk.** Must be
  re-done on v43. The *findings* transfer; the artifact does not.
- **I reported two false accessibility failures** on the founder's own eyes (BUG 6 talking)
  before catching it.
- **I nearly destroyed v43** and was saved only by a byte-check.

**The pattern in all three:** the machine asserted, the founder pushed back, the founder was
right. **Every single time.** That is now the standing rule, and it is the only one worth
keeping if the others must go:

> **When the founder pushes back on a machine-produced fact, the machine is the suspect.
> Re-derive from source. Do not defend the output.**
