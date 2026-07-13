# WALSHERO DURABLE-SAVE MECHANISM
<!-- source: TSP Ledger 2026-07-11 harvest + confluence-HANDOFF-2026-07-10 + belt-run-2026-07-05 | owner: mwalsh | status: spec, gated on one-time setup -->

## The problem this closes
The "save to Drive" half of the build round-trip has failed the **entire v34→v42 arc**. Drive Build Versions is stuck at v33, nine builds behind. It has recurred across 3+ belt runs. Every time, a manual phone-save closes the gap and the gap reopens on the next build.

**Root cause — named plainly:** the durable save depends on a human step (phone-save) or an unverified automation (a Zap/Shortcut that was never confirmed to fire). Nothing ever *checks* that the file actually landed, at the right byte count, in the right place. A save you don't verify is a save you don't have. That is why the same drift keeps coming back — it is a system with no closing check, not a chore you keep forgetting.

## The fix — verified save inside the session
Cowork now holds a Google Drive connector. That changes the whole picture: Claude can **write the build file to Drive and read it back to verify it in the same session** — no manual step, and verified rather than hoped. The round-trip closes itself.

The loop:
1. **Write** — Claude writes the shipped file into `walshero → Claude_files → Tight Spiral Studio`.
2. **Read back** — Claude pulls the file's metadata and confirms the byte count matches the intended size.
3. **Fingerprint** — Claude reads the content and confirms the version eyebrow + a content hash (catches the silent under-size / corrupt save the belt has warned about).
4. **Log** — one line to `TSP Ledger.md` and the omnibus run log: file, bytes, hash, verified Y/N, timestamp.
5. **Durable only after step 4.** No green light until the read-back passes.

This folds the Build-Integrity round-trip (bytes + hash + version stamp) into the save itself, automatically.

## One-time setup (the gate — nothing above runs until this is done)
The connected Google account today is **mwalsh@post.massbay.edu**, not walshero, and the connector holds one Google account at a time. Two ways to give Claude write access to the walshero shelf:

**Recommended — share the walshero folder to post.** In walshero Drive, share `Claude_files/Tight Spiral Studio` (and the `Build Versions` subfolder) to mwalsh@post as Editor. Then whichever account Cowork is signed into can write to the walshero shelf, and the same session can still reach MassBay-side files (assessment corpus, fact book). One durable structure, no connector-swapping tax.
- Steps, on the Mac: open Drive in the browser → right-click the `Tight Spiral Studio` folder → **Share** → type `mwalsh@post.massbay.edu` → set the role dropdown (right of the name field) to **Editor** → **Send**. Heads-up for the screen: the role dropdown sits to the *right* of the email box and is easy to miss; confirm it reads "Editor," not "Viewer," before Send.

**Alternative — switch the connector to walshero.** Settings → Connectors (gear, bottom-left) → Google Drive → Manage/Reconnect → sign in as walshero. Clean, but then post-owned MassBay files aren't reachable in the same session. The Google popup can open *behind* the main window — check for it before re-clicking.

## Standing guardrails (from the ledger, reaffirmed)
- **walshero is the only durable shelf.** post is never the shelf — institutional access can vanish.
- **SSOT = the walshero `Tight Spiral Studio` folder.** The Claude project shelf and the phone are downstream copies; refresh them *from* the shelf, never treat them as truth.
- **Every ship = one file, one verified round-trip.** No triple-stacking builds between saves.

## Status
- Mechanism: specified. Verify-half is ready (Claude can already read Drive metadata + content to check bytes/hash).
- Write-half: **gated on the folder-share above.** Once shared, the next build ships through this loop end-to-end and the v33→current backlog gets pushed and verified in one pass.

<!-- MANIFEST: this doc is the protocol + setup. It does NOT itself move files. First real run happens on the next build after the folder-share. -->
