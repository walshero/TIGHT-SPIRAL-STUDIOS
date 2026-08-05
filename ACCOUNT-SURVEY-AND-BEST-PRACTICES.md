# Account Survey — leaks, canon coherence, credit usage + best practices
*2026-08-05. Read-only survey of how the studio stores & references docs and governance. Posted ONCE; refresh on demand, not on a schedule. History lives in git — this file is not re-dated.*

## Scope surveyed
- **`walshero/TIGHT-SPIRAL-STUDIOS`** (public) — the hub; ~all governance and the only public-leak surface. Deep scan of `origin/main`.
- **`walshero/matt-radar`** (private) — the Matt-eyes dashboard. Scanned.
- **Not yet surveyed** (need an approval-gated scope-add — see "For the next pass"): `en195-apps` (public), `confluence-calibration-assessment-hub` (private), `-writerly-moves-game` (private).

Method was deliberately cheap: targeted `git grep` over `origin/main`, not full renders or clones — credit-conscious per the mandate.

---

## 1. LEAKS — clean (one verify item)
- **No hardcoded secrets anywhere on main.** No GitHub tokens, AWS keys, PEM private keys, or JWTs. The only `service_role` hits are a **warning** in `BENCH-SETUP.md` ("never paste service_role into a public page") — good hygiene, not a leak.
- **Supabase keys are safe by design:** `confluence-TRUNK.html` config is empty/dormant; `index.html` is `PASTE_…` placeholders (guarded by a `PASTE_` check); `en195-arcade.html` ships a **publishable** key (`sb_publishable_…`), which is meant for client code.
- **`.gitignore` protects `.env`.** ✓
- **matt-radar** clean; the **Matt-eyes lane gate** now blocks private material from any public repo.
- **NEW: `secret-scan-gate.py`** — self-testing enforcer that makes "clean" a floor, not a hand-check (see Best Practices). Confirmed 0 HALT across 389 files.
- ⚠ **One verify item (not a leak):** the `en195-arcade` publishable key is only safe if the Supabase table has **RLS on, INSERT-only, SELECT to nobody** (the documented model). Confirm in the Supabase dashboard.

---

## 2. CANON COHERENCE — real sprawl, no contradictions found
The docs don't contradict each other, but single-source-of-truth is eroding:

| Issue | Evidence | Fix |
|---|---|---|
| **Handoff sprawl** | 7 files: `HANDOFF.md` + `HANDOFF-2026-07-20/-07-21`, `-TUESDAY`, `-confluence-2026-07-23`, `-render-proof-gate`, `-render-proof-paydown` | The LANE-REGISTRY's own rule: "all dated handoffs → one `HANDOFF.md`, no dates in filenames, history in git." Consolidate + archive the rest. |
| **Ledger ambiguity** | `TSP_Ledger.md` (canon) vs `claude_FUNES-INDEX.md` + rescued dupes; a prior commit had to "correct the record" that `FUNES-LEDGER.md` was never canon | Name the ONE canonical ledger in a header line; mark the others "index" or archive. |
| **Dated root clutter** | `SESSION-2026-07-22/-26`, `SELF-DIAGNOSIS-*`, `SWOT-2026-08-02`, `LANE-AUDIT-*`, `CORPUS-SWEEP-*`, `ZIP-AUDIT-*`, `lane-probe-*.txt` | Move to `archive/` (or delete — git holds history). Root should read like a table of contents, not a diary. |
| **Enforcer versioning** | `preship-gate-v3.py` **and** `-v4` **and** `-v5`; `studio-eyes-sweep.py` vs `studio-eyes/studio-eyes.py`; `comfort-gate.py` vs `comfort-sweep.py` | Keep one canonical version each; move superseded to `archive/`. Ambiguity = someone runs the wrong gate. |
| **Enforcement gap (biggest)** | **34 enforcer scripts at root; only ~4 are wired** into `floor.yml` (studio-eyes, ratchet, matt-eyes, funes-tendrils). The other ~30 run "if remembered" | This is the exact anti-pattern `ratchet.py`'s own docstring names ("a gate that runs only if the agent remembers"). Add an **enforcer manifest**: each gate marked WIRED / manual / superseded. Wire the load-bearing ones or explicitly retire them. |
| **Stale-branch fork** | `tsp-git-handoff-studio-wide` is 194 commits behind main with diverged `OS.md` / `LANE-REGISTRY` / `FUNES-INDEX` | Already flagged; funes-tendrils surfaces it every session. Reconcile the doc edits, then retire the branch. |

---

## 3. CREDIT USAGE — concrete sinks + fixes
| Sink | Cost | Fix |
|---|---|---|
| **`actions_list` dumps ~390KB** | Hit 3× today just to read a run's status; each blows context | Never list runs to check status. Get the specific run with `minimal_output`, or read `version.json` (the deploy stamps sha/run there), or a 1-line status script. |
| **Repo bloat** | 520 tracked files; **110 (21%) in `rescued/` + `archive/`**; three HTML files **>2MB** (`choose-your-leader-full.html` 3.5MB, `old-problems-at-new-speed.html` 3.4MB) | Every clone/worktree/sweep drags this. Move `rescued/` to an `archive` branch or tag; put giant single-file HTML on Git LFS or split embedded base64 images out. |
| **`floor.yml` installs weasyprint+playwright+chromium every push** | Minutes of CI per push | Cache the toolchain (actions/cache or a prebuilt image); it rarely changes. |
| **Full sweeps over 174 HTML files** | Heavy when a scoped check would do | Prefer `git grep`/targeted checks; reserve full render-sweeps for pre-ship, not every probe. |
| **Stale-branch rediscovery** | The 194-behind lane was invisible until walked | `funes-tendrils` (now on SessionStart) surfaces stranded work automatically. |
| **MCP connector flapping** | Retries/re-searches | Verify against state before retrying; don't re-run known-failing calls on the founder's credits. |

---

## 4. BEST PRACTICES — codified (the standing rules)
1. **One source of truth per concern.** One `HANDOFF.md`, one canonical ledger, one canonical version of each enforcer. Supersede by moving to `archive/`, never by leaving two live copies.
2. **No dates in filenames.** Git carries history. Dated snapshots go to `archive/` if kept at all.
3. **Every gate is wired or retired.** A check that runs only when remembered is not a floor. Maintain an enforcer manifest (WIRED / manual / superseded).
4. **Secrets:** never commit a real key; `.env` stays git-ignored; `secret-scan-gate.py` is the floor; anon/publishable keys are fine **with RLS**.
5. **Private material** lives only in private lanes (`matt-radar` + private cloud folder); the Matt-eyes gate enforces it.
6. **Credit hygiene:** cheap status checks (never dump `actions_list`); scoped `git grep` over full sweeps; don't re-run known failures; keep the corpus lean.
7. **Post once.** Surveys/reports are durable docs refreshed on demand — not recurring notifiers.

---

## 5. For the next pass (needs your one tap)
- **Approve a scope-add** for `en195-apps`, `confluence-calibration-assessment-hub`, `-writerly-moves-game` so the leak + coherence scan covers the whole account (blocked tonight because `add_repo` is approval-gated and you were asleep).
- **Say "do the cleanup"** and I'll execute §2 safely (consolidate handoffs, archive dated files + superseded enforcer versions, add the enforcer manifest) on a branch you can review — I did **not** do mass file moves autonomously, to avoid clobbering the concurrently-active main.
- **Confirm** the en195-arcade Supabase RLS posture (§1 verify item).
