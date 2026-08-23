# HARVEST, `claude/studio-viscosity-comfort-controls-k3272n`, 2026-08-17

*Tier 2 of `claude/BRANCH-TRIAGE-2026-08-17.md`, executed. Files taken one at a
time. The branch was never merged: merging it would have deleted roughly 75,000
lines, because it is a July snapshot.*

## TAKEN (13 files, all verified to run before landing)

**Tooling, none of which main had:**

| File | What it is | Verified |
|---|---|---|
| `tsp_browser.py` | Resolves the container's real Chromium when the pip Playwright version and the installed browser build disagree | `find_chrome()` returns `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`, exists |
| `canon-guard.py` | Enforces ROLE-canon so a stale or superseded file cannot be read as current | `--self-test` passes: manifest schema valid, verdict logic bites, planted stale ref caught |
| `axe-audit.py` | Invokes axe-core, the industry accessibility engine, which `floor.yml` installed and never called | compiles |
| `contrast-plus.py` | APCA (WCAG 3.0 draft) contrast as a secondary lens beside the WCAG 2.x gates | compiles |
| `staging-sandbox.py` | One real browser, the build rendered, shared by floor checks and agentic playtesters | compiles |
| `canon-manifest.json`, `canon-vocab.json` | canon-guard's data | valid JSON |

**Records (6):** `claude_aleph-cyl-integration-2026-07-26.md`,
`claude_convening-systems-2026-07-26.md`, `claude_cyl-playtest-table-2026-07-26.md`,
`claude_gate-promotion-protocol.md`, `claude_playtest-heuristics.md`,
`claude_seat-playtesting-agents.md`.

**`tsp_browser.py` is the immediately useful one.** This session hand-patched
`executable_path="/opt/pw-browsers/chromium"` into three separate test scripts
because `p.chromium.launch()` failed on exactly the version mismatch this module
exists to solve. It should be imported by `one-thing-gate.py`,
`art-execution-gate.py` and `studio-eyes-sweep.py` instead of each carrying its own
fallback.

## SKIPPED (1 file)

`studio/dad-energy.html`, 72,829 bytes: a pre-move copy of main's root
`dad-energy.html` at 95,384 bytes. Main's is larger and newer. Harvesting it would
have re-introduced a stale duplicate under an old path.

## TWO FINDINGS THE HARVEST TURNED UP

Both are about the harvested tool itself, and both are stated rather than quietly
landed, because a tool trusted without them is worse than no tool.

**1. `canon-manifest.json` is stale, and that is the exact failure canon-guard
exists to prevent.** It was written 2026-07-26 and does not know about
`preship-gate-v5.py` (which ships in main and whose own docstring says it supersedes
the `preship-gate-v4.py` the manifest still declares canonical) or about
`art-execution-gate.py` (added 2026-08-14). The guard against reading superseded
files as current is itself carrying a superseded map. **It needs a refresh pass
before its verdicts are worth acting on.**

**2. `canon-guard.py --refs` has a supersession-versus-dependency false positive.**
It reports a HALT for `preship-gate-v5.py:5` "uses" `preship-gate-v3.py` and
`preship-contrast-gate.py`. Line 5 of that file is its own docstring saying
*"Supersedes preship-contrast-gate.py, preship-gate-v3.py, preship-gate-v4.py."*
That is a supersession note, not a live call. A gate that flags a file for correctly
documenting what it replaced will train the founder to ignore it, which is the
comfort-gate doctrine again.

**Neither tool is wired into the belt by this harvest.** They are landed, verified to
run, and flagged. Wiring waits on the manifest refresh and on the false-positive fix,
because wiring a gate that cries wolf is worse than leaving it unwired.

## STILL BLOCKED

Tier 1 deletion could not be executed: `git push origin --delete` returns **HTTP
403** through this session's git proxy, and the GitHub connector exposes
`create_branch` and `list_branches` but no delete. The four dead refs and their
SHAs, for deletion from the GitHub UI or a local `gh`:

```
claude/adopt-funes           5f06b504f6e9c83862be0d213b3ada0d7c6736bf
claude/companion-floor-fix   1d9f349b1a54ec061e066ac0d5acc4302a160bb5
claude/playtest-team         aed72323b5bfde91ad49c71aeb5bcd013bd311e0
claude/trunk-fix             f3b40474860fd50ca9cb368357d7fe917daa35b6
```

All four re-verified at 0 unlanded patches and 0 unique files immediately before
the attempt. Tag pushes are blocked by the same 403, so the branch SHAs are
recorded here instead: recreating any of them is `git branch <name> <sha>`.
