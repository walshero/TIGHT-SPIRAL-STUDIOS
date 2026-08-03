# DECISION-TREE NODE — Zapier auth lane (kill the PAT-in-transcript gap)
*Founder ruling, 2026-08-03. Studio-wide. Staged here for TSP-GIT-LANE to merge to canon.*
*Context is adjacent by design — this node is self-contained so no session has to reconstruct it.*

---

## SPINE (one sentence)
**GitHub auth for the studio's git/deploy/ingest lanes runs through Zapier's OAuth connection — auto-refreshing, never in a transcript — and Zapier's MCP actions are allowlisted so the workflow never stops for a token again.**

## CONTEXT (why this exists — read before touching)
- **The recurring gap.** `HANDOFF.md` records the pattern plainly: the studio keeps hand-generating a fine-grained GitHub PAT, it lands **exposed in the transcript**, and must be **rotated** at the next stop. That is a workflow halt *and* a credential-hygiene leak, every time. Founder: "This is a regular gap. Perma fix."
- **RP protocol.** Maximize automation, minimize manual visual navigation. A halt that forces the founder to hunt buried GitHub menus on a phone is exactly the friction the accessibility floor exists to remove.
- **The walls found this session** (so no one re-derives them):
  - `nist.gov` (and other open web) egress is **policy-denied** through the sandbox proxy — no direct fetch of source images.
  - A real image is ~34 KB → ~46 KB base64; **an assistant cannot retype that verbatim** (it corrupts — base64 has zero error tolerance). So bytes must move server-side, never through chat.
  - **Zapier code-action sandboxes are single-app.** GitHub-context (`GitHubCLIAPI`) can reach **only** `api.github.com` (rejects `googleapis.com`, `drive.google.com`, `drive.usercontent.google.com` — all tested). Drive-context (`GoogleDriveCLIAPI`) reads Drive natively but has **no GitHub auth** and no Pillow to downscale. Neither context was confirmed to reach *both* Drive and GitHub.

## DECISION (founder ruling)
1. **Auth source = Zapier's connected GitHub account** (`walshero`, OAuth, auto-refreshing). It already exists and already writes GitHub with no token param. Stop hand-minting PATs that leak into chat.
2. **Allowlist Zapier MCP in committed settings** so ingest/deploy actions run with **no approval prompt**. (Landed — see "What landed".)
3. **If a scoped token is ever needed**, it enters Zapier via the **config UI, out of band** — never pasted into a chat/transcript.

## BRANCHES (the one open fork — resolve first next session)
> **Can a Drive-context Zapier code action reach `api.github.com`?** (Untested — this session was approval-gated before it could run.)

- **Branch A — reachable.** Build the Drive→GitHub bridge in **Drive-context** (native Drive read + GitHub write via the connected account, or a Zapier-held token). Then **save it as a reusable Zapier studio skill**: one call, zero stops, forever. Then run the first legal/labeled federal image into the fireground game.
- **Branch B — not reachable.** One code action cannot span both domains. Fall back to: (a) founder-committed images (the existing `art/cyl/plates/*.jpg` path), or (b) keep the studio-drawn cut-paper SVG medium — already shipped, legal-by-construction, labeled "studio schematic — not a photograph."

## MAXIMALLY-AUTOMATED NEXT STEPS (copy-paste; prompts already cleared next session)
1. **Probe the fork** — create + run this code action (`GoogleDriveCLIAPI`), requirements verbatim:
   > *"This action must reach api.github.com. GET https://api.github.com/rate_limit with header Accept: application/vnd.github+json, no auth. Return success(bool), http_status, and whether the domain was reachable vs blocked by a domain filter; on a domain-filter error return the exact error text."*
2. **If reachable → build the bridge** (`GoogleDriveCLIAPI`, no token param; connected accounts), requirements verbatim:
   > *"Copy a Google Drive file's raw bytes into a GitHub repo on a specific branch using the connected Google Drive account (GET googleapis.com …?alt=media) and the connected GitHub account (GET/PUT api.github.com/repos/{repo}/contents/{path}?ref={branch}, base64 content, capture sha if the file exists). Inputs: drive_file_id, github_repo, github_path, branch, commit_message. Return commit_sha, html_url, bytes_downloaded. Preserve exact bytes."*
   Then `create_zapier_skill` wrapping it as **"studio image ingest"** with `github_repo` locked to `walshero/TIGHT-SPIRAL-STUDIOS`.
3. **Token path (founder-chosen), if the bridge needs one** — add it in Zapier, never in chat:
   - Zapier server config: **https://mcp.zapier.com/mcp/servers/d2265a83-f44b-4c46-a6e9-d6aface67ff8/config**
   - GitHub connection reconnect: **https://mcp.zapier.com/api/v1/connect-auth/GitHubCLIAPI?accountId=27849482&connectionId=64905949**
   - PAT scope, if reconnecting with a token: fine-grained, **repo = `walshero/TIGHT-SPIRAL-STUDIOS` only**, **Contents = Read and write**.

## CANON MERGE (for TSP-GIT-LANE)
- `.claude/settings.json` (Zapier allowlist) is carried on this branch **and** on the fireground lane (`1d7eee4`). **Merge/cherry-pick it to `main`** so the allowlist loads for **every** session and lane at fresh-clone start — that is what makes "no more stopping" permanent studio-wide (project settings load at session start; local settings are gitignored and don't survive the fresh clone).

## WHAT LANDED (fireground lane, PR #28)
- `7145161` — game scene art labeled "studio schematic — a drawn diagram of the scene, not a photograph" (the honest resolution of "legal and labeled"; contrast ~13:1 both themes).
- `1d7eee4` — `.claude/settings.json` Zapier MCP allowlist.

## HYGIENE
- **No credential ever in a transcript.** The old PAT flagged in `HANDOFF.md` should be **rotated/revoked** at the next stop; going forward the OAuth connection is the source.

---

## RESOLVED — 2026-08-03 (the fork is answered; tested, not assumed)

The whole binary-ingest space is now mapped by real execution. Do not re-derive.

**TOKENLESS SERVER-SIDE TRANSFER WORKS.** The native Zapier action `GitHub → Create or Update File` (`github_create_or_update_file`) writes to any repo/branch using the connected `walshero` OAuth account — **no token param, no code sandbox, no domain wall, no bytes through the model.** Proven: it committed a real file to the fireground branch server-side.
- **DO for TEXT / HTML** (the studio's main deploy lane): this is the perma-fix, done. `content` = the file text (or a URL Zapier fetches), `repo`, `branch`, `path`, `message`. Tokenless, promptless, no corruption. The "deploy studio file" automation is solved.

**BINARY (images) HAS ONE HARD BOUNDARY — the MCP string layer.** Every MCP-reachable binary path was tested and fails:
- Native create-file with a **string** `content` (a URL *or* a Zapier hydration pointer) → the action text-decodes the bytes (UTF-8), so a 34 KB JPEG lands as ~61 KB of `efbfbd` replacement chars. **Corrupts. Confirmed twice.**
- Code actions (either app context) are **domain-locked per action**: GitHub-context reaches only `api.github.com`; Drive-context reaches only `*.googleapis.com,docs.google.com` (tested — it downloaded the clean JPEG `ffd8ffe0`, then was blocked calling GitHub). A single code action cannot span both clouds, token or not.
- Retyping base64 through the model corrupts (46 KB, zero error tolerance).

**THE ONE BINARY-SAFE PATH = a real multi-step Zap (built once in the Zapier UI).** Zapier hydrates a file **object** server-side only when a `File` field is **mapped step→step inside a Zap** — not when a string is passed via a single MCP call. So: a 2-step Zap **[Google Drive: Retrieve/Find File] → [GitHub: Create or Update File]** with the Drive `file` output mapped into GitHub's `content` field moves raw bytes host-to-host, binary-safe, tokenless (OAuth). This is a ~5-minute one-time UI build; it then runs forever.

**SOURCE READY.** `nist-charleston-image.jpg` in the studio Drive (`walshero`, id `1xX9EGKjgb2jWePDpLO5M4nS6Dm_FhHIQ`, folder `1HgCt7LgM88cexg90tjVh0844eYfo0oOq`) is a verified-clean JPEG, 34,459 B, md5 `5ea9080329a83c8780b291d41720c88d`, 325×221. It is the incident-matched NIST image (credit "NIST"). Ready for the Zap.

**NET:** text/HTML deploys are fully automated and tokenless now. Binary images need the one-time 2-step Zap (or the game keeps its studio-drawn SVG art, already shipped, legal + labeled). No token was ever required for either — the OAuth connection carries it.
