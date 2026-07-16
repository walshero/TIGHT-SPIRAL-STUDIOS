# HANDOFF — 2026-07-16 (evening close)
**Supersedes prior HANDOFF.md. Read first.**

---

## WHAT LANDED THIS SESSION (durable, byte-verified in repo)

- **tsp-opportunity-bridge.html** — 26,888 B, commit f443e0d, md5 f6d45c4d58795d72df8f3dbe4cea4176.
  The FIVE-LANE version: conferences, grants (deep-dive), commissions, Games for Change, FableVision.
  This is the file that held the conference + grant research and was stranded in outputs for a session.
  Address: raw.githubusercontent.com/walshero/TIGHT-SPIRAL-STUDIOS/main/tsp-opportunity-bridge.html
- **HANDOFF-render-proof-gate.md** — 5,662 B, commit f443e0d, md5 3af7d7a7272c9ac44f07b1b1c5deecf0.
  The four render-proof gate teeth to build (see below).

## PAT — ROTATED THIS SESSION
Fresh fine-grained token generated on phone (github.com web, not app — app buries Developer settings).
Token is EXPOSED in this transcript. **Rotate again at next stopping point:**
github.com -> profile pic -> Settings -> Developer settings (bottom of left sidebar) ->
Personal access tokens -> Fine-grained tokens -> TSP fine grain token deploy -> Regenerate token.
Scope: Only select repositories -> TIGHT-SPIRAL-STUDIOS. Permissions: Contents = Read and write.

## DRIVE BUS IS DOWN AGAIN
write_drive_file_content errored twice this session (file_name-required, then code-execution error).
The stale four-lane bridge (Drive ID 1YH6MmJ8RByOhF9slL41dmsPv1nNV5eey) was NOT overwritten —
it still holds the old 20KB v1. Next session: overwrite it with a pointer to the repo canon, OR
delete it (canon is safely in the repo, so the stale Drive copy is a fossil, not a loss).

---

## THE RENDER-PROOF GATE (customer #1: your-rp-world.html)

The pre-ship gate certified your-rp-world.html warm-dark mode at 13.23:1 and it RENDERED at 1.17:1
on the founder's phone — light-gold text on the white iOS in-app sheet showing through because the
page background did not paint opaque + gold-as-text broke token-role law.

**THE GATE IS A SUSPECT.** No build ships on the gate's say-so alone until the render-proof teeth
exist. Build order (full spec in HANDOFF-render-proof-gate.md):
1. OPACITY TOOTH — every full-screen section resolves to an opaque bg in every comfort mode or HALT.
2. PER-MODE HAND-VERIFY — force each comfort stop as its own full palette, measure independently.
3. RENDER-PROOF NOT TOKEN-PROOF — background-inheritance grounding; if nearest painted ancestor is
   white/unset, measure against THAT.
4. HUE FLOOR FOR RP — warm TEXT must be cool near-white; amber/gold are fills + accents only.
Then sweep the full game corpus, one HALT list, worst-first.

## your-rp-world.html — FOUNDER-REJECTED, HELD (not in repo)
38,638 B in outputs only. Stage 1 RP-literacy game (intake -> mirror -> research landscape).
Rejected on warm mode. Do NOT ship until rebuilt with render-proof fix. It is customer #1 of the
new teeth. Literature-validated identity variables; three real registry doors (ClinicalTrials.gov,
Foundation Fighting Blindness, Mass Eye and Ear).

---

## SESSION-OPEN LAW — THREE SEATS (locked 2026-07-16)
Fires every new project chat, out loud, before first file claim, performed by PM:
1. FUNES — resolve any named file LIVE across four lanes before touching it. Disagreement HALTS.
2. ALEPH — one corpus glance; lead with the FINISHING list (Borges paper unsent, Diagnose mode
   parked, four Tell cards, meta-machine, lumiere->Suubi), not building.
3. CORA (Registrar) — institutional-fact questions route to her; citation + as-of date or
   "not in the corpus" + who owns it.

## ACCESSIBILITY FAILURE NOTED + LOGGED (2026-07-16)
Gave phone-navigation instructions from a desktop mental model without asking which screen the
founder was on. Violated "folded eyes" / SIGHT-BEFORE-STEPS. Corrected reflex: before ANY device
navigation instruction, ask what screen + what's visible, then guide from HIS view, never assume
"top-right". Locked as a check, not a wish.

---

## PENDING (carried, urgent-first)
- [URGENT] Build render-proof teeth into preship gate per HANDOFF-render-proof-gate.md. Sweep corpus.
- [URGENT] Rebuild your-rp-world.html warm mode; then founder GATE 1 cold play (undelegatable).
- [URGENT before Jul 20] Console Post->Boost verb fix so gate passes; then GALA EasyChair submission.
- [ACTIVE] Rotate the exposed PAT.
- [ACTIVE] Matt to CREATE Drive folder STUDENT-WORK-PROTECTED by hand, register ID.
- Matt's GATE 1 cold play of barcelona-summers.html v2 — undelegatable.
- Send Borges paper to Chronicle of Higher Ed this month (Tier 1).
- Email Pauline@academic-conferences.org for ECGBL abstract window.
- Confirm MassBay SAM.gov + Grants.gov registration current.
- Sign up for Teach Access newsletter (grant reopen watch).
- Overwrite/delete stale Drive bridge v1 (ID 1YH6MmJ8RByOhF9slL41dmsPv1nNV5eey) once Drive bus back.
- File_008 11.5MB zip (Drive 1e7bGU_W2hNvmeyJTnauzzqGgEX1jcW-7) — Matt unzip on Mac, upload folder.

---

## DRIVE BUS ERROR — DIAGNOSIS (2026-07-16)
Two distinct failures this session, not one:
1. "file_name is required" — SCHEMA failure. write_drive_file_content needs file_name even when
   file_id is given. Recoverable by adding the param.
2. "Code execution hit an error" + opaque error_id, no detail — SANDBOX crash PAST validation.
   Not fixable by changing parameters. This is the recurring one.
Pattern: every READ (list_all_drive_files) succeeded this session; every WRITE-by-existing-ID
(overwrite file 1YH6MmJ8...) failed. Suspect the overwrite-by-ID / replace-in-place path has
regressed, OR that specific file ID is in a bad state.
ISOLATING TEST (next session, one call): write a NEW small file, content+file_name only, NO
file_id. Success => bus is fine, bug is specifically overwrite-by-ID. Failure => bus is down.
No loss incurred: all canon went to the repo lane (up, byte-verified); Drive only ever held pointers.
