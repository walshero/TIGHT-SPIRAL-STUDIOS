# Drive write lane — VERIFIED 2026-07-11 (updates studio-file-map §1)

The file map listed **native Google Drive WRITE** as UNVERIFIED. It is now **verified working**, tested live this session.

## What works (proven this session)
- **Native `create_file`** (Google Drive MCP) with `textContent` + `contentMimeType:text/html` + `disableConversionToGoogleType:true` → creates a real `.html` in a named folder by parentId. Stays HTML, does NOT convert to a Google Doc. Owner resolves to mwalsh@post.massbay.edu.
- **Zapier Google Drive** actions all fire: `update_file_name` (rename), `delete_file` (permanent), `read_drive_file_base64` (byte-exact readback). Also present: `upload_file` (accepts a public URL), `replace_file`, `write_base64_to_drive`.
- **MassBay cabinet** = Drive folder **MASSBAY: COURSE DOCS**, id `1YY997nYBGFxwBHU782D_qajO2e76uauB`.

## The one real gotcha (cost real time — record it)
Large files can't be moved cleanly through inline tool params. A hand-typed 63KB `textContent` **silently dropped two SVG blocks** (came in 6.6KB short). There is **no Drive "update content" tool** — you cannot patch; you must re-create.
- **Rule:** after any inline write >~10KB, VERIFY byte count via `read_drive_file_base64` → decode → compare size/sha and `grep -c '<svg'`. Do not trust "created:true".
- **Better lane for big/binary files:** push exact bytes to a URL, then Zapier `upload_file` (from URL). BUT per the file-map FERPA/hygiene rule, institutional docs must NOT go to the public GitHub repo — so for those, use verified inline + byte-check, or a private URL source.

## GitHub, for the record
- Session git proxy **blocks repo creation** (`POST /user/repos`) and repo listing for ANY token, including a user-supplied PAT — "sessions are bound to their configured repositories."
- **git-over-HTTPS is unrestricted** (reached arbitrary public repos), so pushing to an *existing* allowlisted repo would work; creating a new one from here will not.
- Net: to put something new on GitHub from a session, the empty repo must already exist (create it in the browser or via a Zapier GitHub action), then push.

## Outcome
`FYS-Treasure-Trove.html` (62,483 bytes, 31 SVGs, both banners, all 10 workshops, renders verified) now lives in the MassBay cabinet. Four probe/degraded scratch files were created during debugging and permanently deleted; folder is clean.
