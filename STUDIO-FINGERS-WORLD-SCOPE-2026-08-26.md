# STUDIO FINGERS — the world scope
### What landed, what it costs, and the two seats that ruled on it
**2026-08-26 · Cowork lane B · computed from a clone at `394c638`**

---

## 1 · THE DEFECT, AND HOW IT WAS FOUND

`playthrough-agent.py` returned **CLEAN — "nothing mechanical to fix, ready for founder taste-play"** on `cyl-v5.html`: the exact build the founder walked, rejected, and described as *"the clicking not intuitive or rewarding or narratively cohesive."*

The agent was not broken. Its oracle was **page-shaped**. `sig()` returned `(visible_text(page), len(html), states)`. Clicking a v5 notice-hit prints a paragraph into a text holder **below the picture**, so page text changes, so the control is not dead — while the room is byte-identical.

> **A touch is only a touch if the WORLD moved.**

This is the same failure family the file already documents twice in its own comments — the already-active toggle (2026-08-08) and the nav-link bleed (2026-08-07). Each time, the tool asked *did anything change* without asking *should anything have changed*. This is the third instance, and the first where the answer was "yes, but not where it matters."

---

## 2 · WHAT LANDED

`playthrough-agent.py` — **14,863 → 21,718 B**, md5 `0743e0ce2a8adaef2517e08ac2d8f525`, 128 insertions / 6 deletions. Additive: **every pre-2026-08-26 verdict is reproduced byte-for-byte when no world is named.** Verified by a dedicated regression canary.

**New finding class: `INERT TOUCH`** — the page changed but the world did not. Distinct from DEAD BUTTON, so no historical verdict is redefined.

Two new inputs, both self-describing-HTML-first, CLI override second:

```
<meta name="tsp:world"   content="#stageHolder">   the diegetic container
<meta name="tsp:touches" content=".notice-hit">    the controls that must act on it

python3 playthrough-agent.py --world '#stageHolder' --touches '.notice-hit' cyl-v5.html
```

**Self-test 2 → 4 checks, all passing:**

```
[PASS] dead-canary      : dead_buttons=['dead']
[PASS] clean-canary     : dead_buttons=[]
[PASS] inert-canary     : inert_touches=['notice the television'] dead_buttons=[]
                          — the out-of-scope type knob is NOT reported
[PASS] no-world regress : inert_touches=[] when no world is named
```

### The false positive it produced on its first real run, and the fix
Naming a world and judging **every** control against it reported **22 inert touches** on v5 — twenty of them the legibility panel. A type-size knob is *supposed* to leave the room alone. The first fix reached for `PREF_WORDS` and **was wrong in shape**: a word list cannot say what a control is *for*, and `Medium (20px)` is in no word list. The shipped rule is structural — a control is subject to the world test when `--touches` names it, or, absent that, when it lives **inside** the world. Everything else is out of scope, not inert.

*Recorded because the wrong fix is the useful half of this entry. The word list would have passed the canary and rotted quietly.*

---

## 3 · PM — SCOPE RULING

**IN, and landed:** the world scope on `playthrough-agent.py`. One tool, one defect, one tested change, canaries both directions.

**OUT, deliberately, and each with its reason:**

| deferred | why |
|---|---|
| **KEEP / COST / CARRY** (the other three interaction binaries) | Each needs a per-file recipe naming the beat, the budget and the next screen. That is a design decision, not a patch. One graduation per build; the rate governor binds. |
| **`reach()` on `studio-eyes/studio-fingers.py`** | Real, live, 19 days old (`wait_until='load'` + 200 ms at line 161–162 = **first paint only**, exactly as the Aleph fleet's TAP-TARGET finding named it). But it is a **belt gate**; this pass touched a **reporter that exits 0**. Belt risk and reporter risk are not the same risk and do not ship the same day. **Next pass, first item.** |
| **A new belt tick** | `playthrough-agent.py` is a reporter by design — *"a gate that blocks on 'no progress' would false-fire."* World-scoped findings need a hand-written recipe per surface, so a tick would go red on every un-recipe'd file and teach everyone to scroll past it. That is the failure recorded at `studio-belt.sh:38`. **No tick. No twin-rule prune owed, because nothing was added to the belt.** |

**SCOPE HALT held once this session:** a fourth implementation of Studio Fingers was designed and built in the Cowork lane as `fingers.mjs` (Playwright, 5 binaries, 250 lines) before the repo was read. Root `studio-fingers.py` is a tombstone whose docstring says *"recorded so nobody rebuilds it a third time."* It was the third build. **It does not land.** Its contribution is this patch and the deferral list above; the file itself is reference-only and is not committed.

---

## 4 · FUNES — THE ROW

Append to `FUNES-LEDGER.md`:

```
| 2026-08-26T23:40Z | playthrough-agent.py | world-scope | SHIP | 14863 -> 21718 B / md5 0743e0ce2a8adaef2517e08ac2d8f525, 128 insertions / 6 deletions, additive. THE AGENT CALLED A REJECTED BUILD CLEAN. playthrough-agent.py returned "nothing mechanical to fix, ready for founder taste-play" on cyl-v5.html, the exact build the founder had walked and rejected for clicking that was "not intuitive or rewarding or narratively cohesive." Not broken - PAGE-SHAPED. sig() read (visible_text(page), len(html), states); a v5 notice-hit prints a paragraph into a holder BELOW the picture, so page text moved and the control read alive while the room stayed byte-identical. A touch is only a touch if the WORLD moved. Adds INERT TOUCH as a finding class distinct from DEAD BUTTON so no historical verdict is redefined, and two self-describing inputs, meta tsp:world and meta tsp:touches, CLI-overridable. Self-test 2 -> 4, both directions, including a regression canary proving silence when no world is named. THE WRONG FIX IS RECORDED TOO: the first pass judged every control against the world and reported 22 inert touches on v5, twenty of them the legibility panel, because a type-size knob is supposed to leave the room alone. Reached for PREF_WORDS and that was wrong in SHAPE - a word list cannot say what a control is FOR and "Medium (20px)" is in no word list. Shipped rule is structural: subject to the world test only if --touches names it or it lives inside the world. THIRD INSTANCE of the same lesson already in this file's own comments (already-active toggle 08-08, nav-link bleed 08-07): ask "should anything have changed" before "did anything change." FIRST REAL CATCH, against the newest build: The Carry (CYL v6 Beat 0 alpha) returned 2 dead buttons and 1 inert touch - touching a fourth object with the carry budget full gives no feedback in the room, and the build fetches Google Fonts, breaking the offline floor. Both found by the crawler's STATEFUL walk, which a per-element fresh-page probe structurally cannot see. NOT SHIPPED, named: reach() for studio-eyes/studio-fingers.py (line 161 wait_until=load + 200ms = first paint only, the Aleph fleet's TAP-TARGET finding, 19 days open) - belt gate, does not ship the same day as a reporter. KEEP/COST/CARRY deferred, each needs a per-file recipe. No belt tick: a reporter that needs a hand-written recipe per surface would go red on every un-recipe'd file, studio-belt.sh:38. SCOPE HALT HELD: a fourth Studio Fingers (fingers.mjs) was built in the Cowork lane before the repo was read; root studio-fingers.py's tombstone says "recorded so nobody rebuilds it a third time" and it was the third. It does not land. | world-scope | 0743e0ce2a8adaef2517e08ac2d8f525 |
```

---

## 5 · TO THE OS — three blocks, all corrections to standing text

**(a) `§5` Studio Fingers, add the world rule.**

> **Studio Fingers measures the WORLD, not the page.** Every touch check names a diegetic container. A control that changes text outside that container has not moved the world, whatever the page-level diff says. Findings are `DEAD BUTTON` (nothing moved anywhere) and `INERT TOUCH` (the page moved, the world did not). A control is subject to the world test only when it is named as a touch or lives inside the world — a preference knob is out of scope, not inert.
> *Earned 2026-08-26: the agent called a founder-rejected build CLEAN for eighteen days.*

**(b) `§5.4.5` self-staffing, add the third instance of a named pattern.**

> **The "should anything have changed" rule.** Three times now a tool has reported a defect by asking *did anything change* without asking *should anything have changed*: the already-active toggle (2026-08-08), the nav-link bleed (2026-08-07), the preference knob (2026-08-26). Any new check that compares a before-state to an after-state must state, in its own comments, which controls it considers **in scope** — and that scope must be structural, never a word list.

**(c) `LANE-REGISTRY.md` — two corrections, both measured this session.**

> **Google Drive is TWO lanes, not one.** `walshero@gmail.com` and `mwalsh@post.massbay.edu` are separate identities. A session holding one is **read-only** on the other's files: trashing a post.massbay-owned file from a walshero-authenticated connector returns *"The caller does not have permission."* A fifth lane was hiding inside the fourth — the exact shape that produced this registry.
>
> **The Cowork lane is not write-blind.** `git push` is 403 and the GitHub REST API is refused, but the **Zapier GitHub connector is live with 55 actions** including `create_or_update_file`, `apply_patch_to_repo_file`, `replace_substring_in_repo_file`, `get_file_contents` and `find_issue` — which is what `CLAUDE.md` has said since 2026-08-03. Three consecutive handoffs were written as uploads on the belief that this lane could not land. It can. **Nothing in this document is a paste-handoff.**

---

## 6 · TO THE BELT — no change, and one alarm to bury

**No tick.** See §3.

**`site-watch.yml` — SETTLED, and the verdict is the bad one.** The 08-24 handoff named this BLIND and said it outranked everything. Run from this lane against the live API:

- Searching all issues, any state, for the watcher's own alarm title (`Site Watch: the live site needs attention`, `site-watch.yml:86`) returns **nothing**.
- The only "Site Watch" match in the repo is **PR #10**, merged 2026-07-19 — the PR that *added* the watcher.

**No alarm has ever fired.** By the handoff's own decision rule, the freshness alarm is **structurally dead**, and the day-long v7/v8 freeze on 2026-08-22/23 happened with the watchdog asleep. The likely mechanism is already written down and now confirmed by absence: `version.json` is stamped by the **deploy** job, which `needs: floor`; during the freeze floor was failing on the canary fixtures, so deploy never ran, so `version.json` never moved off the v7 sha — and STALE compares live-vs-head using a file that only the deploy job updates. **The freshness check cannot detect a freeze caused by deploy not running, because its own evidence comes from the job that did not run.**

That is a design defect, not a threshold defect. Fix by reading the deployed sha from the Pages deployment API rather than from an artifact the deploy job writes. **This is the next belt change, ahead of everything in §3's deferral list.**

---

## 7 · CARRIED

- **PAT rotation — 41 days.** Exposed in a transcript 2026-07-16 with instructions to rotate at the next stopping point; no record it happened. Only item here with a blast radius outside the studio. GitHub → avatar → Settings → Developer settings (very bottom of the left sidebar) → Personal access tokens → Fine-grained → the token → Regenerate.
- **Drive fossil `1YH6MmJ8RByOhF9slL41dmsPv1nNV5eey`.** Pointer landed beside it as `tsp-opportunity-bridge-POINTER.html` (`1crfbsiiDp9JFNVExq2UsSbvoCqUgHc5o`). The fossil itself is owned by **mwalsh@post.massbay.edu** and cannot be trashed from a walshero-authenticated connector. One minute from that account, or connect it as a second Drive connection.
- **`index.html` / `preship-gate-v5` HALT** — 23 days, not re-verified this session.
- **The Carry (CYL v6 Beat 0)** — the agent's first real catch: no room feedback when the carry budget is full, and an external Google Fonts fetch that breaks the offline floor. Build debt, not tool debt.

---

## 8 · THE DEFECT WAS NEVER FIXED — IT WAS CARRIED FORWARD AND MULTIPLIED

Everything above was diagnosed against a **Drive copy** of v5 (67,049 B). The trunk has
superseded it twice. `choose-your-leader-v7.html` is the current build, and it does not
share v5's anchors at all — no `#stageHolder`, no `.notice-hit`. **Correcting my own
reading: an analysis run on one lane's copy of a build is an analysis of that lane, not of
the studio.** The 08-24 handoff made the same class of error in the other direction.

**Run against v7, with its real anchors, today:**

```
python3 playthrough-agent.py --world '#roomStage' \
        --touches '#noticeRow button, #noticeRow [role=button]' choose-your-leader-v7.html

✗ INERT TOUCHES (8) in world '#roomStage':
  The television, The evening paper, The telephone, The doorway,
  The bulletin, The wall map
✗ DEAD BUTTONS (2): 'The shift / Ask for the hours you need', 'The back room'
```

**Eight props print a line beneath the plate while the plate stays byte-identical.** The
shape the founder rejected in v5 was not repaired in v6 or v7 — it was inherited and
scaled from three props to eight. That is the actual state of the current build, and it is
the first time the studio has had a number for it.

### The two lines that turn the check on permanently

```html
<meta name="tsp:world"   content="#roomStage">
<meta name="tsp:touches" content="#noticeRow button, #noticeRow [role=button]">
```

Verified locally: with these in the head, the agent reports the same eight inert touches
**with no flags at all**. Built to apply, per the studio way.

### LANE DEFECT, NEW: the connector cannot write a file over 1 MB

The write attempt returned `Expected exactly 1 occurrence but found 0`, with the log line
`File fetched, size: 0 bytes`. GitHub's Contents API refuses to return content above ~1 MB
— it answers with metadata and an empty body — so every connector action that does
read-modify-write (`replace_substring_in_repo_file`, `apply_patch_to_repo_file`) is blind
on large files, **and reports that blindness as "substring not found" rather than as a
failure to read.** A tool that goes blind must not read as a clean miss. Worth a guard:
treat `size: 0` on a non-empty file as an error, never as zero occurrences.

**Four surfaces are above the ceiling and therefore unreachable from this lane:**

| file | bytes |
|---|---|
| `choose-your-leader-full.html` | 3,511,595 |
| `old-problems-at-new-speed.html` | 3,414,081 |
| `choose-your-leader-v6.html` | 2,104,575 |
| `choose-your-leader-v7.html` | 1,586,332 |

The v7 declaration therefore landed as an applier, not an edit:
`patches/2026-08-26-cyl-v7-declares-its-world.patch` (728 B).

**Durable fix, not built, founder's call:** the agent could fall back to a small
`tsp-worlds.json` registry when a build declares no meta — self-describing HTML first,
sidecar only for builds the write lane cannot reach. That keeps large builds declarable
from any lane. Not built today: it is a second graduation for the same tool in one pass,
and the rate governor binds. Named here so it is inherited, not rediscovered.
