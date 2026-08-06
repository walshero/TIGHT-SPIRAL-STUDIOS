# TSP NO-TOKEN LANE - repo writes without a PAT
*2026-08-06. Supersedes the "get a fine-grained PAT from Matt" cold-start step in TSP-GIT-LANE.md.*
*This file was itself landed through the lane it describes - tokenless, byte-verified.*

## THE RULE
Repo writes go through the **Zapier GitHub lane** (GitHub connected once by OAuth as `walshero`).
**No fine-grained PATs. No tokens in chat. No 7-day expiry.** A PAT is the worst path for RP -
dense settings UI, tiny toggles, a repo picker, a recurring re-issue - and it is no longer needed.

## HOW TO WRITE A FILE (proven 2026-08-06)
Zapier action: **GitHub -> Create or Update File** (`github_create_or_update_file`).
- params: `repo` = `walshero/TIGHT-SPIRAL-STUDIOS`, `branch` = `main`, `path`, `content` (text), `message`.
- NEW file: omit `sha`. UPDATE an existing file: first read its `sha` (GitHub -> Get File Contents), pass it.
- The commit lands on `main` under `walshero`, auto-parented off current HEAD - no rebase, no race to manage.
- Binary / Drive-sourced files: use the studio's existing Drive->GitHub code actions
  (`drive_binary_to_repo_branch`, `github_write_from_drive_same_domain`).

## THE DISCIPLINE (unchanged - computed > typed)
After every write, **byte-verify from canon**: pull and confirm the file compiles/parses and matches.
"success:true" from the API is not proof; HEAD on origin is. Route the verdict to `funes-ledger.py`.

## WHEN A PAT IS ACTUALLY NEEDED (almost never)
Only for operations the Zapier GitHub actions cannot do. Then generate it on the **Mac** and use it
from the Mac Keychain lane. **Never paste a PAT into chat** - it burns into the transcript on contact
and must be rotated immediately.

## COSMETIC NOTE
Zapier-lane commits show as "Unverified" (unsigned) on GitHub. That is a signature badge, not a
validity problem - the commits are real and on `main`. Add commit signing later only if you want to.

## THE RP POINT
You touch voice and Drive. Automations carry it to GitHub. One browser "Allow" - already done.
No token screen, ever again.
