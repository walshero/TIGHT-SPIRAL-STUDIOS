# HARVEST — Accessibility / Design-Floor Lane

*ALEPH (one point, whole corpus) + FUNES (verified memory, gated). Lane:
`claude/tsp-accessibility-design-review-w55xa0`. Swept from source 2026-07-27.
Every claim below is verified from the repo working copy + git this session, or it
is named as a boundary. Nothing here is guessed.*

---

## TL;DR

- **The lane is not stale-empty — it finished something.** One commit (`be2fef0`)
  brought **35 HTML pages** to the three ship floors. Both studio gates now read
  **0 HALT across all 42 root pages** (`preship-gate-v3.py`, `structure-gate.py`),
  verified twice this session.
- **The usables are three reusable patterns now standardized across the corpus**,
  a set of **gate blind-spots minted into checks**, and **two real defects caught**.
- **ALEPH's standing finding holds: this is a finishing problem, not a building
  problem.** The single highest-value act now is **not more building** — it is a
  human **merge of this branch to `main`**, because a session cannot push to canon
  (LANE-REGISTRY) and the floors do not ship until someone does.
- **Two things a harvest must not walk past:** (1) the confluence-TRUNK canon
  pointer in FUNES-INDEX is **stale by ~11 KB** vs the actual repo file; (2) the
  **PII-flagged 2026-06-23 trunk still has copies** in `archive/` and `rescued/`.

---

## THE USABLES (what to carry forward)

### 1. Three reusable patterns, now applied identically across the corpus
Verified counts from source (`grep -l` over root `*.html`):

| Pattern | Files carrying it | What it is |
|---|---|---|
| **Comfort knob** (`.comfort-knob` / `#comfortBtn`) | 14 | Fixed corner control, ink pinned, cycles Default→Softer(→Warm). Never a wall. |
| **In-app nav floor** (`.app-nav`, `#backBtn`/`#homeBtn` over a history stack) | 12 | Gate-visible back+home wired to each page's `show()`. Modeled on `your-rp-world.html`. |
| **Shared Home/Back injector** (`tsp-mobile.js` + `TSP_MOBILE`) | 30 | Runtime chip; parent hierarchy games→`arcade`, en195→`en195-hub`, all→`index`. |
| **Token-driven inline SVG scene** | 34 | Authored `<svg>` in the page's own tokens to clear the >50% image floor — no external assets. |

These four are the studio's accessibility + floor vocabulary, now consistent enough
to lift into `tight-spiral-patterns.md` as the canonical snippets. (Recommendation R4.)

### 2. Gate blind-spots — minted from "we should remember" into checks (FUNES teeth)
This lane learned exactly where the arithmetic gates are blind. Each is now a rule:

- **structure-gate false positive:** a comfort button whose **aria-label contains
  `"mode:"`** trips the `\bmode:` CONFIG regex and is reported as an OPENING WALL.
  → **Check:** comfort aria-labels must not contain the literal `mode:` (write
  "Switch comfort — …", not "comfort mode: …"). *Proof:* `your-rp-world.html` was
  the last residual FP; dropping the colon cleared the whole corpus to 0 HALT.
- **preship nav-gate is blind to runtime-injected and indirectly-wired nav:** it
  cannot see (a) `tsp-mobile` chips (injected at load), (b) controls wired by
  `#id`-prefixed selectors, or (c) handlers keyed off **unquoted** object keys.
  → **Check:** a multi-screen page's back/home must be **statically legible** —
  real `id="backBtn"/"homeBtn"` in the source — which is also better for the user
  than an invisible affordance. (This is why 12 pages gained an `.app-nav`.)
- **image-floor is blind to JS-injected SVG:** a page whose art is drawn by script
  still scans as a text wall. → **Check:** ship a **static authored SVG fallback**
  in the markup (e.g. `behind-this-door.html`'s door), even when JS enhances it.

### 3. Two real defects caught while enforcing the floors
- **`choose-your-leader-v6.html` — corrupt token.** A malformed value
  `--ink-dim:#2c3views;` (a fossil of a botched edit) was live. **Fixed** —
  0 occurrences remain; `--ink-dim` now resolves to `#c4ccd4` / `#2b3238`.
- **`en195-what-counts-now.html` — hard-wall violation.** Its comfort control used
  `color:inherit` (the studio's "never on an a11y control" rule). **Fixed** — ink
  pinned to `#241f16`.

---

## CANON (resolve_canon-style, from source this session)

```
this-lane
  branch:      claude/tsp-accessibility-design-review-w55xa0
  commit:      be2fef0  (+1373 / −63, 35 files)
  gate state:  preship 0 HALT / 42 ; structure 0 HALT / 42   [verified 2026-07-27]
  pushed to:   origin/<this branch>   NOT origin/main
  canon-lane:  repo main is canon for deployed — this work is NOT there yet
```

### CANON DRIFT — confluence-TRUNK.html  (FUNES teeth: md5 mismatch is a HALT)
```
FUNES-INDEX / LANE-REGISTRY cite:  v44  598114 B  md5 8dcf9903…
repo file, this session:                609246 B  md5 19ad2ee18a871c6fbc49e88530194cb4
  ├ pre-this-lane (origin/main):        609246 B  md5 8bef55b72ab8a1f01cac346b59678389
  └ this lane's edit:  ONE token, byte-neutral (--pine-lt #3d8a64→#367f57, contrast 4.08→4.73)
```
**Reading (gated, not guessed):** the ~11 KB gap (598114 → 609246) **predates this
lane** — the cited "v44" pointer describes a *different, smaller* file than what
`main` actually serves. This lane's edit only moved the md5 by two characters and
did not change the byte count. **The index pointer is stale and must be re-cut from
the live `main` file; the underlying "which is really v44?" question is for Matt/Josh.**

---

## RECOMMENDATIONS — the finishing list (ALEPH leads here, not with building)

1. **Merge this branch to `main`.** Nothing here ships until a human pulls it —
   a session cannot push to canon. This is the one act that converts the whole
   lane from "done in a branch" to "live." *Highest value, and it is not mine to do.*
2. **PII — probe and purge.** The 2026-06-23 trunk the charter flagged as serving
   faculty/possible-student PII **still has copies in the tree**:
   `archive/confluence-TRUNK-2026-06-23.html`,
   `rescued/shelf-final-2026-07-13/confluence-TRUNK-v43-2026-07-10.html`, and two
   `studio-eyes-shots/…2026-06-23…png`. I **cannot verify from the sandbox** whether
   Pages serves `archive/`  or `rescued/` — **live-probe those paths, then delete
   the copies if they resolve.** Keep this at the top of the board until it 404s.
3. **Re-cut the confluence-TRUNK canon pointer** in `FUNES-INDEX.md` /
   `LANE-REGISTRY.md` from the live `main` file (609246 B / current md5), and settle
   the v44 byte discrepancy.
4. **Promote the four patterns** (§Usables 1) into `tight-spiral-patterns.md`, and
   **fold the three blind-spot checks** (§Usables 2) into the gate scripts or the
   pre-ship checklist so the next lane inherits them as teeth, not lore.

---

## WHAT I COULD NOT VERIFY (the boundary — stated, not filled)

- **The other lanes.** I cannot reach **Netlify** or **Google Drive** from this
  sandbox (egress blocked), so `resolve_canon --audit` cannot run all four lanes
  from here. Every claim above is **repo-lane only**. A zero result here is a
  statement about my access, never proof of absence (the Dad-Energy lesson).
- **Whether Pages serves `archive/` or `rescued/`.** Needs a live probe (R2).
- **The full "11 files with proven contrast defects" roster.** This lane fixed
  four token defects (confluence `--pine-lt`, fys `--gold-deep`, warriors `--gold`,
  CYL v5/v6 accent + softer palettes). Whether those were *among* the charter's 11,
  and which of the 11 remain, requires the studio-eyes ledger I did not re-run.
- **The homeless finishing items** (Borges paper, Diagnose mode, the four Tell
  cards, the meta-machine, the four-fifths thesis, the lumière/Suubi story). This
  lane **did not touch them**; they remain on the finishing list unchanged. I am
  not reporting progress I did not make.

---

*Methodological note: built entirely from the repo working copy, git, and the two
gate scripts, run this session. It does not paraphrase or reconstruct any lane I
cannot read. The honest deliverable is the verified usables, the canon drift, the
PII flag, and the boundary — pushed to the repo the same turn it was written, so it
is not another silo. — ALEPH+FUNES, 2026-07-27.*
