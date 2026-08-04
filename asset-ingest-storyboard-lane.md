# The Asset-Ingest & Storyboard Lane — standing, permissible
*Founder ruling 2026-08-03: "make this a standing permissible lane — locating relevant images arranged through storyboard expertise to leverage learning sciences and domain expertise within a situated learning experience that appeals to the four freedoms." Studio-wide. Grounded via Funes + the fireground Aleph panel; enforced by the fool-me-once checks.*

---

## WHAT THE LANE IS
A repeatable studio pipeline that turns **legally-sourced real imagery** into an **image-driven situated-learning experience**. Not "drop a picture in a page" — a craft lane with five stages, each with a named discipline. It is **permissible by standing** (authorized to run without re-asking) once its permission + provenance + dignity gates are satisfied.

## THE FIVE STAGES
1. **LOCATE — provenance-first sourcing.** Find images where the *judgment lives in the frame* (the size-up cue is visible), from named, license-clear sources only. Tier-1: USFA Fire Service Image Gallery (copyright-free), DVIDS (PD, per-asset check). Tier-2 for named incidents: NIST / NIOSH **staff-authored figures only** (drop any "courtesy of [3rd party]"). Self-host — never hotlink. Exclude UL FSRI (permission-gated) and the San Diego drill imagery (Dodson copyright — study reference, not a source). *(Kernels K2, K4.)*
2. **STORYBOARD — sequence for perception, not decoration.** Arrange as **image → predict (private, under uncertainty) → reveal the record**. Pair **contrasting cases** (look-alikes that read differently); **fade the scaffolding** (name the cue frame early, strip it later). One image, one decision. *(Kernel K3; Kellman PALMs.)*
3. **GROUND — learning sciences + domain expertise.** Read-schema and reveal both run on the domain's real frame — for fire, **B-SAHF** (Building·Smoke·Air track·Heat·Flame) + **Dodson's Reading Smoke** (volume·velocity·density·color). Capture **confidence → surface calibration**, never a score. Domain accuracy per incident (NIST/NIOSH). *(Kernel K3.)*
4. **SITUATE — a situated-learning experience.** The learner does the discipline-real task in its context (Gee; Lave & Wenger; Nunan task-based), not a quiz *about* it. The record is the authority; the learner's read is theirs.
5. **FOUR FREEDOMS (Osterweil) — the experience must appeal to all four:**
   - **Freedom to fail** — the read is private and never scored; a wrong read costs nothing but insight. (Non-negotiable for a noticing game.)
   - **Freedom to experiment** — try a read, turn to the record, try the next case; contrasting cases invite "what if I'd seen it this way."
   - **Freedom to fashion identity** — the learner reads *as* a size-up officer; the facilitator/crew-debrief lets a crew bring its own voice.
   - **Freedom of effort** — sit with one case or run the deck; leave the read blank and just hold the question. Rhythm is the learner's.

## THE INGEST MECHANISM (how bytes actually land — binary-safe)
The photos are real binaries; the studio's OS §3.2 says the licensed-photo lane is "produced in a capable session." Findings, tested:
- **Native GitHub "Create or Update File" with a URL string → CORRUPTS binary** (text-decodes). Fine for HTML/text, not images.
- **Raw-HTTP code actions are domain-walled** (GitHub-context reaches only api.github.com; Drive-context only googleapis) — cannot bridge.
- **`drive_file_to_github` (Zapier code action) is the path.** It downloads the Drive file **intact** (verified: 34,459 B → base64) and writes via **Zapier's connection layer** — which is **not** domain-blocked. It failed on exactly one thing: **`no github credential on this connection`.**
- **THE ONE STEP TO ARM IT:** attach a **GitHub account credential** to the Zapier connection `drive_file_to_github` runs on (Zapier UI — this is the "store a scoped token in Zapier" step). Then the ingest fires binary-safe, committing as **walshero** (the studio identity — same provenance as the CYL plates).
- **Branch targeting:** `drive_file_to_github` has no repo/branch param (hardcoded). Build a **branch-aware clone** (`drive_ingest_to_branch`: drive_file_id, github_repo, github_path, branch, commit_message) once the credential is attached, so images can land on a feature branch, not just default.
- **Drop-and-deploy alternative (no code action):** a UI Zap — **Google Drive "New File in Folder" → GitHub "Create or Update File"**, mapping the trigger's **File** object into File Content (server-side hydration = binary-safe). Drop a legal image in the ingest folder → auto-commit.

## PERMISSION (why it's a *permissible* lane)
Zapier ingest actions are allowlisted in committed `.claude/settings.json` (loads at session start) so the lane runs without per-call approval prompts. The Medium-Gate + dignity + provenance checks (`medium-gate-check.py`, the K1–K4 kernels) are the gates that make it *safe* to run standing.

## DIGNITY (hard, always)
Investigation/structure/smoke/construction/aftermath-without-victims only. Never victims, bodies, or fire-as-spectacle. Memorial framing — the lessons were paid for in lives. Caption every image with its source; never launder provenance; never present a render as a scene photo. *(Kernel K4; founder-canon §3.1.)*

## SOURCE READY NOW
`nist-charleston-image.jpg` — studio Drive (`walshero`, id `1xX9EGKjgb2jWePDpLO5M4nS6Dm_FhHIQ`, 34,459 B, md5 `5ea9080329a83c8780b291d41720c88d`, 325×221). One armed ingest away from `fireground-assets/charleston-1.jpg`.

## RUN-ORDER (for any future image-driven build)
LOCATE (provenance) → Medium Gate declares `tsp:medium=licensed-photo` → STORYBOARD (predict→reveal, contrasting) → GROUND (domain schema + calibration) → SITUATE (task-real) → FOUR FREEDOMS check → ingest (armed Zap) → Studio Eyes on the composite → caption + credit → ship.
