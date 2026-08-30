# HANDOFF — 2026-08-30, Cowork lane · NO WALLS

**Supplements the TSP lane, which holds the Pages repair. This lane holds the demolition.**
Written to canon rather than pasted, because the last three handoffs in this repo were
uploads and all three went unwitnessed. Every number below was computed in-session against
`origin/main` or by running the repo's own gates. Nothing is carried forward untested.

---

## 0 · READ THIS FIRST IF YOU READ NOTHING ELSE

**The push refusal is an allowlist, not a missing credential.** `git push` from a session
container returns, verbatim:

> *access denied by the git proxy: walshero/TIGHT-SPIRAL-STUDIOS is not in this session's
> authorized repository set, so the proxy will not inject a credential for it. To fix, add
> the repository to the session's sources.*

`GH_TOKEN` and `GITHUB_TOKEN` are both set in the container. `git clone`, `git fetch` and
`git ls-remote` all succeed. **Read works. Write is refused at the proxy, by repository
allowlist.**

`LANE-REGISTRY.md` has recorded this as "no push credential" since it was written. That is
wrong in a way that matters: a missing credential is nothing anyone can fix in a chat, so
the entry read as a dead end and the studio built a whole retyping lane around it. An
allowlist entry is a founder click.

**What the click retires, all at once:**
- the PLACEHOLDER incident (2026-08-27) — a connector write sent the literal string
  `PLACEHOLDER` as file content and destroyed `funnybonies/index.html` on main
- the five-chunk base64 ritual that corrupted canon twice on 2026-08-06, `success: true`
  both times
- the **1 MB connector ceiling**, which currently puts `choose-your-leader-full.html`,
  `choose-your-leader-v6.html` and `old-problems-at-new-speed.html` out of reach of every
  session lane
- the 3-4-connector-calls-per-file cost that stalled the no-walls run twice

Every one of those is the same failure: **bytes retyped into a tool call instead of moved
by git.** Nothing else in this repo's backlog has that blast radius for that little effort.

---

## 1 · WHAT LANDED IN CANON TODAY

| | commit | bytes | verified |
|---|---|---|---|
| `nowalls.py` | `9705250` | 7,819 | md5 `b46a0303…` matches remote fetch |
| `FUNES-LEDGER.md` row | `5f55b22` | 69,200 total | append confirmed by the action |

`nowalls.py` is the demolition made repeatable. It is not a gate and does not belong on the
belt — it is a one-shot corpus edit that will retire itself when the last wall is out.

**Usage:**

```
python3 nowalls.py <file.html> [<file.html> ...]
```

It prints `CUT` or `SKIP` per file and **refuses rather than guesses**. A SKIP is a correct
outcome. It edits in place; run it in a clone and diff before landing anything.

---

## 2 · THE FINDING, AND WHY IT IS THE SAME FINDING AS LAST WEEK

Four dialects of the identical comfort wall exist in the corpus. Canon recorded two.

1. flat handler run — the arcade shape. The 08-29 batch handled this one.
2. `if(eyes&&panel){ … }` guarded block — **12 files.** A flat line-matcher walks past it.
3. `if(!eyes||!panel) return;` early return — `trail-notes.html`.
4. `$('seEyes')` instead of `document.getElementById`.

**Dialect 3 passed every string check and still broke the page.** Cutting the wall took the
strings `seEyes` and `sePanel` out of the file along with the `var` line, so nothing named
the wall any more — and the page threw `eyes is not defined` on load.

> **A wall can be gone from the markup and still break the page.**

Only a headless Chromium load with a `pageerror` listener caught it. Grep proves the absence
of a string; it cannot prove the page still runs. This is the same shape as INERT TOUCH
(2026-08-26) and the same shape as the four failures in the CHECKED IS NOT SHIPPED block:
**the thing that was checked was not the thing that shipped.**

**Practical consequence for any lane doing corpus surgery:** a string check is a
pre-condition, never the verdict. Load the file.

### Guardrails that earned their place by refusing

- The first panel matcher used `<div[^>]*id="sePanel".*?</div>`. Non-greedy stops at the
  first inner `</div>` — the `.se-row` holding the light buttons — and leaves half the panel
  standing. The leftover check refused **all 40 files** rather than shipping a half-cut
  panel. Keep that check.
- The kernel check compares `<style>` blocks byte-for-byte and the `<html>` tag. A
  token-count check was tried first and refuses everything, because `se-a1`,
  `se-contrast` and `data-light` live in **both** the kernel (keep) and the handlers (cut).
  Counting cannot separate them; bracketing can.

---

## 3 · MEASURED STATE

Inventory grep, **corrected**. Both prior runs used an unanchored `Legibility`, which
matches `text-rendering:optimizeLegibility` and reported two already-clean CYL slices as
walls. Use:

```
grep -lE 'id="seEyes"|id="sePanel"|Comfort — reading|(^|[^a-zA-Z])Legibility' *.html \
  | grep -v '^confluence'
```

**43 walls standing · 40 reachable · 3 above the 1 MB ceiling.** Confluence exempt by
founder ruling.

Run on the 40 reachable: **36 CUT, 4 SKIP.**

| gate | result |
|---|---|
| `comfort-gate.py` on the 36 | **0 HALT of 36** — kernel intact, day/dusk/night all ≥4.5, dark confirmed |
| `studio-eyes/studio-fingers.py` on the 36 | 7 at HALT — **all 7 already HALTed before the cut, same codes**. C-BUTTON 43 → 36; the seven that vanish are the Comfort buttons. No new finding. |
| Chromium load, 36 | no `pageerror`; `#seEyes` and `#sePanel` gone from the DOM; `header.se-chrome` carries both **Studio** and **Cabinet** |

`index.html` goes 93,007 → 91,351 bytes.

**The four refusals, and what each needs:**

| file | reason | fix |
|---|---|---|
| `enjambment.html` | no `se-chrome` header | hand-set the top rail |
| `enjambment-skins.html` | no `se-chrome` header | hand-set the top rail |
| `workshop-wall.html` | `se-chrome` present, non-standard Home link | one hand edit |
| `the-compound-capstone.html` | fragments survive | **a fifth dialect, not yet read** |

---

## 4 · WHAT IS IN FLIGHT

Scheduled task `trig_01Y3zqbNDEDxnLDghVU8MXNC` ("No walls, universal home (tool-driven)"),
daily 12:00 UTC, self-retiring. Rewritten today to run `nowalls.py` instead of hand-editing,
and fired manually at 15:56 UTC — session `cse_01Xg4oGA9CfXCBjCfWwfK4mS`.

**Two runs of this task have now stalled.** 08-30 at 12:06 UTC ran 3.5 hours PENDING with
zero commits and nothing mirrored. The cause was method, not agent: four surgical connector
calls per surface does not finish inside a run's budget. The rewrite is one write per file,
4x fewer calls. If it stalls a third time, the diagnosis is no longer the method — check
whether the connector is rate-limiting.

**A local commit exists that cannot be pushed.** Branch `no-walls-2026-08-30`, commit
`de0188e`, all 36 cuts, in a container clone. It dies with the container. If the allowlist
in §0 is opened while that container is alive, push it; otherwise the connector run in
flight lands the same bytes.

---

## 5 · DO NOT REBUILD

- **Studio Fingers.** Built three times. Root `studio-fingers.py` is a deliberate loud
  tombstone (`sys.exit(2)`, postmortem in the docstring). The surviving gate is
  `studio-eyes/studio-fingers.py` and it works. A fourth build was started in a Cowork
  session on 2026-08-26 and stopped by reading the repo first.
- **A comfort kernel, palette, light mode or type scale.** Comfort work is PAUSED by
  founder ruling. Per-game palette is NOT paused and belongs to the Colour & Palette Lead.
- **A second inventory grep.** Use the anchored one in §3.

---

## 6 · OPEN, RANKED

1. **Open the repository allowlist (§0).** One click. Retires four recorded failure modes.
2. Finish the 36 — in flight; watch **https://walshero.github.io/tss-playtest/no-walls.html**
3. Read the fifth dialect in `the-compound-capstone.html`; extend `nowalls.py`.
4. Hand-set the three surfaces with non-standard headers.
5. The three oversize builds. **Blocked on §0** — no session lane can write them.
6. `github_get_pages_latest_build` ignores its `repo` parameter and is hardcoded to
   `confluence-calibration-assessment-hub`. Its sibling `get_pages_status` honours it.
   Not yet in the ledger. Small, but it means any lane trusting that action is reading
   another repo's build.

**Not this lane's:** the main repo's dead Pages. Founder ruled 2026-08-29 that it is being
handled in the TSP lane.

---

*Computed against `origin/main` at `5f55b22`. Gates run, not cited: `comfort-gate.py`
(0 HALT / 36), `studio-eyes/studio-fingers.py` (7 HALT, all pre-existing, codes diffed
before and after), headless Chromium load check (36 clean).*
