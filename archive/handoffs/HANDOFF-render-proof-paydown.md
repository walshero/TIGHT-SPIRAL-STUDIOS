# HANDOFF — RENDER-PROOF R1 PAYDOWN, split with TSP-GIT-LANE
**Written 2026-07-28. The render-proof floor is now ALIVE in CI and catching real invisible
text. 6 of 21 R1 files are fixed. 15 remain. This splits the rest so the two lanes stop
colliding on the same files.**

---

## THE ONE THING

The v4 render-proof gate (`studio-eyes-sweep.py`) had been **dead in CI for weeks** —
WeasyPrint was never installed, so it exited 2 in 0 seconds and `ratchet.py` read the
blindness as "all clean" and rubber-stamped every push. It is now installed, armed, and
**fail-loud** (a blind sweep HALTs, never passes). It renders every comfort stop at 390px
and 1100px and grounds text on alpha-composited backgrounds. **R1 = text that is actually
invisible/low-contrast when rendered** — the class WCAG token-checks miss.

Both lanes edit the same game files. This handoff divides the R1 paydown so we don't
clobber each other, and names the shared root causes so most of it is a few edits, not 15.

---

## WHAT IS ALREADY LIVE (do not redo)

- **`floor.yml`** installs `weasyprint==69.0` + pango/harfbuzz libs. The gate runs for real
  (~4 min/push). Poppler/R2 pixel-check deferred to phase 2 (keeps CI == the baseline).
- **`ratchet.py`** fails loud on sweep exit 2; recognizes v4 classes. **`floor-baseline.json`
  is shared state — do not hand-edit it in a way that fights the other lane. Let the ratchet
  tighten it as files are fixed.**
- **`studio-eyes-sweep.py`**: C1 (color-scheme) and E1 (font<18px) are **report-only WARNs**.
  Only **R1 / R2 / H4 / EM** HALT. A gate red = *invisible text*, not small font.
- **Deploy is DECOUPLED** (`deploy: if: always()`), and **Site Watch** alarms on down/stale.
  So a red gate CANNOT freeze the live site. Fix at leisure; nothing is on fire.
- **`floor-status.py` + `floor-status.html`**: the live-site dashboard (worst-first, exact
  failing text + rendered ratio + comfort mode) and a **DRAFT ribbon** on each failing page.
  Ribbons auto-clear when a file passes. **This dashboard is the shared tracker.**

---

## THE SPLIT (claim before you cut)

**TSP-GIT-LANE — the COMFORT-CONTROL cluster (8 files). You are already in these.**
Your "comfort is a knob, not a gate — 8 gate-family pages" work touches the exact element
that fails: **`.cstop`** (the comfort button), `color:var(--ink)` on `background:var(--surface)`,
rendering **~2.86:1** in day mode. Fold the contrast fix into that work:

    course-river.html   en195-last-week.html   flash-ballast.html
    play-the-semester.html   play-the-semester-flash.html   review-bench.html
    the-tell.html   workshop-wall.html

Fix: make `.cstop` text vs its surface clear **≥4.5:1** in every stop (lift `--ink` on that
button, or give `.cstop` an explicit high-contrast pair). `the-compound-capstone.html` and
`en195-last-week.html` read `--ink` on surface at ~2.56:1 — same class.

**THIS LANE (Claude/pages) — the 7 non-comfort files.** I will take:

    fys_fys-treasure-trove.html  (3.32:1 'OWNER: ADMINISTRATION' — label color)
    tight-spiral-runbook.html    (4.33:1 'REFERENCE' — just under floor)
    confluence-TRUNK.html        (4.19:1 'Tour' — institutional, careful edits)
    choose-your-leader-nixon-slice.html  (R1: "zero text laid out" — a RENDER/JS issue,
                                          not a color; the stop lays out empty. Needs a look,
                                          not a contrast bump.)
    reading-the-fireground.html  }  skip-link '.skip' at warm 2.17:1 'Skip to content'
    your-rp-world.html           }  (shared .skip pattern — one fix pattern, 2 files)

If you'd rather swap any, say so on the dashboard/ledger before starting it.

---

## THE FIX RECIPE (what worked on the 6 already done)

1. Open the dashboard entry: it gives the **exact failing text, the rendered ratio, and the
   stop@width** (e.g. `day@390: 2.54:1 'CABINET'`).
2. Find that text's element in the file; find its `color` and the **real painted background**
   it lands on IN THAT STOP (mind grafted comfort palettes — a `body.softer{}` that only
   redefines `--bg`/`--ink` but leaves `--surface`/`--line` at the dark `:root` renders dark
   ink on dark surface. That was the funny-boneys 1.15:1 bug; complete the palette).
3. Lift the color (or surface) so it clears **4.5:1** (3.0 for large: ≥24px, or ≥18.66px bold).
   Reuse a token that already passes (`var(--dim)` was ~5:1 on the dark papers).
4. **Verify — do not guess.** Local run needs the engine:
   `sudo apt-get install -y libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz-subset0`
   `pip install weasyprint==69.0 pillow`
   `python3 studio-eyes-sweep.py <file>.html`   → expect **no `R1:` lines**.
5. When a batch is done, run `python3 floor-status.py .` — it strips the ribbons off the
   now-clean files and refreshes the dashboard. Commit the file fixes + the regen together.

---

## COORDINATION PROTOCOL (so we stop conflicting)

- **One lane per file.** Use the split above. If you must touch a file outside your set,
  note it first (ledger or dashboard commit) so the other lane rebases, not clobbers.
- **`git push --force-with-lease` + rebase on conflict.** Never `-f`. If a merge 409s,
  `git fetch origin main && git rebase origin/main`, re-verify, re-push. (Both lanes have
  hit this; force-with-lease is what keeps us from overwriting each other's work.)
- **`floor-baseline.json` is shared.** Prefer letting `ratchet.py` shrink it automatically
  as files pass. If you must re-`--init`, do it on a quiet main and announce it.
- **The dashboard count is the shared scoreboard.** 21 → 15 today. It should only go down.
- **Verify with the real engine before you commit.** The whole reason this gate exists is
  that the founder read a screen certified at 13:1 he could not see. A guessed fix that
  still renders invisible is the exact failure we are killing. Run the sweep.

---

## STATUS AT HANDOFF (2026-07-28)

Fixed + merged (this lane): `funny-boneys-factory` (1.15:1 → clean),
`cliche-cabinet` / `cliche-cowpaths` / `cliche-city` / `cliche-field` / `cliche-line`
(2.5:1 hardcoded muted labels → var(--dim)/#8a857b). **R1: 21 → 15.**
Remaining split above. Nothing blocks the live site (decoupled + Site Watch).
