# Studio Integrity Guard — Report
*Weekly read-only sweep. One file per name; this report is replaced each run, not dated-copied.*
*Run: 2026-07-13 ~13:06 UTC · Run #34 (scheduled, unattended) · Status: PARTIAL — probe blind, but one structural fix confirmed landed · Supersedes Run #33 in place.*

## Bottom line
Mixed run. The site probe was **blind** — WebFetch returned `PROVENANCE_REQUIRED` on every attempt (a parallel batch of 8, single-URL retries, and one retry after a pause), same wall as Run #33 and #21. No live page was verified this run, so the standing CRITICAL and HIGH findings are carried forward **unconfirmed since 01:10 UTC (Run #32)** — the guard cannot currently tell whether anything came down.

But this run is **not** empty: a read-only trigger check surfaced real progress. **One of the two structural fixes has landed.** Read-only rule honored throughout — nothing deployed, deleted, published, or sent; no canonical document edited; no curl/wget (web-content policy).

## NEW THIS RUN — the cadence fix is DONE (good news)
The scheduled task `trig_01FQqXXXHr5mFBUt1JGWK3n4` ("Studio Integrity Guard — weekly sweep") now has cron **`0 13 * * 1`** — weekly, Mondays 13:00 UTC. It was updated **2026-07-13T02:52 UTC** (right after the blind Run #33) and its `next_run_at` is **2026-07-20T13:04 UTC**. The hourly churn that produced Runs #1–#33 is over; this run fired on the correct weekly schedule. The "reset the trigger to weekly" action that had been owed since Run #5 is **resolved** — drop it from the open list.

## STILL OWED — the fetch path (second structural fix, NOT done)
This blind run is itself the proof: the probe still depends on the intermittent provenance gate, and it was closed this week. Until the fetch path is made durable, roughly every other weekly run will come back blind and unable to confirm the FERPA floor. The two durable options remain Matt's call:
- Pre-authorize `walshero.github.io/TIGHT-SPIRAL-STUDIOS/` for WebFetch, **or**
- Commit a server-side GitHub Actions link-checker (no provenance gate at all — recommended; it also runs even when no chat session is open).

## STANDING FINDINGS — last verified at Run #32 (01:10 UTC), NOT re-verified this run
Carried forward as **last-known-open, unconfirmed since 01:10 UTC ≈ 12 h ago**. Could still be live or could have been taken down — the guard is blind and cannot tell.

### CRITICAL — named students + faculty PII on the public web (last seen HTTP 200 at 01:10 UTC)
Two files serving the same "Confluence Calibration / Assessment Hub" payload:
- `confluence-TRUNK.html` — last seen LIVE (200). Canon (`STUDIO-COMMAND-CENTER 2.md` v5.1, `studio-live-links-2026-07-11.md`) still wrongly says 404/RESOLVED.
- `confluence-TRUNK-2026-06-23.html` — last seen LIVE (200). Dated twin, same payload.

Named students (last seen on the page): Peter Kistner, Nick Giancioppo, Chelsea Dow, Gabriela Moreno, Georgia Oakley, Nathan Desmarias, Lena Sebugwawo, David Earl, Faisal Murad, Diego Rocha, JayJay Conrad, Sarah Courchesne. FERPA-floor student PII, not faculty-only.
Faculty/staff + emails (last seen): Matt Walsh, Clarissa Codrington, Sean McCarthy, John Donato, Katie McGrath, Demola Adeyemi; mwalsh@massbay.edu, litmag@massbay.edu, jdonato@massby.edu (typo), kmcgath@massbay.edu (typo), dadeyemi@massbay.edu, ENchair@massbay.edu.

### HIGH — internal / institutional files (last seen live at 01:10 UTC)
- `claude-project-instructions.md` — internal operating playbook.
- `chatgpt-pro-instructions.md` — art-pipeline instructions; contains `walshero@gmail.com`.
- `massbay-fact-book-word.docx` — institutional document, served as binary.

### LOW — stale canon; glyph watch (carried, unverified this run)
- Front page was rebuilt since the 2026-07-11 map (nine builds); `studio-live-links-2026-07-11.md` is stale and needs a re-probe + rewrite once a probe succeeds and the takedown is done.
- Matt's own `walshero@gmail.com` on `the-tell.html` and `behind-this-door.html` — by choice, informational.
- Theme-toggle glyphs on `the-console.html` / `choose-your-leader-v5-slice.html` — monochrome dingbats, watch item, not a violation.

## What needs Matt
1. **Delete the two PII trunks first** — `confluence-TRUNK.html` and `confluence-TRUNK-2026-06-23.html` (these carry the named students). GitHub web editor: repo file list (main branch) → click the filename → trash-can icon at the top-right of the file view → "Delete file" → green "Commit changes" button at the bottom, below the fold — scroll down.
2. **Same delete for the three HIGH files** — `claude-project-instructions.md`, `chatgpt-pro-instructions.md`, `massbay-fact-book-word.docx`. Five files, one sitting.
3. **Correct the canon after removal** — `STUDIO-COMMAND-CENTER 2.md` (v5.1) and `studio-live-links-2026-07-11.md` both falsely say the FERPA trunk is 404/RESOLVED; fix once files are down.
4. **The one remaining structural fix** — make the fetch path durable (GitHub Actions link-checker recommended, or pre-authorize the domain for WebFetch). The cadence half of this is now done; this is the last piece keeping the guard from confirming the FERPA floor on its own each week.

## Method note
Read forward-guard, live-links map, prior report (#33), and Ledger. Date via bash (13:06 UTC). WebFetch: `PROVENANCE_REQUIRED` on all attempts (batch of 8, single-URL retries, one post-pause retry) — gate did not clear; no live page verified. Verified the trigger cron read-only via list_triggers: `0 13 * * 1`, updated 2026-07-13T02:52 UTC, next run 2026-07-20T13:04 UTC — cadence fix confirmed landed. No canonical document edited; no deploy/delete/publish/send; no curl/wget. Report replaced in place. Standing CRITICAL/HIGH from Run #32 carried forward as unconfirmed.
