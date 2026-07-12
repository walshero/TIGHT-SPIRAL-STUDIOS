# PROJECT INSTRUCTIONS — PASTE BLOCK
*The carrier only the founder can load. Copy the block below into EVERY Project's
custom instructions. One-time, per project. This is what makes a cold session
start already pointed at canon instead of guessing.*

---

## WHERE TO PASTE IT (explicit, no hunting)

**On the Mac app or claude.ai:**
1. Open the Project.
2. The **Project** panel is on the **right side** of the window.
3. Find **"Add instructions"** (if empty) or **"Edit instructions"** (if it already
   has text) — it sits under the project title, above the file shelf.
4. Paste the block below. Save.

**Warning:** if the window is narrow, the right-hand Project panel may be collapsed
behind a **panel toggle** at the top-right. Widen the window or click that toggle
first, or the instructions field will not be visible at all.

Do this for: **Tight Spiral (TSP)**, **Confluence**, **Leeder**, **Capstone**, and any
other live project.

---

## THE BLOCK — copy everything between the lines

────────────────────────────────────────────────────────────

**SESSION-OPEN (run before the first project answer, every session, silent):**

1. **LOAD CANON.** Pull `STUDIO-COMMAND-CENTER.md` from Drive Claude_files
   (folder `1WJh7jRrIfVE9MNydjyKjYlErIQq7gRwC`, file `1dULxFj1fxg8sF3SF2DXGoA9B-tt1XMbQ`)
   via the Zapier `read_drive_file_content` action. That file is CANON; the
   `/mnt/project` shelf mount is FALLBACK only.

2. **LOAD THE MANIFEST.** Pull `cross-lane-manifest.md`
   (Drive `1bf9w5itKx7F4CvMdOCJRPbMEpww-WEOE`). It declares what this lane may READ
   and what it may WRITE. Canon is an address, not a copy. Never write to a doc this
   lane holds RO.

3. **SOURCE-FIRST LOCK.** For any question about a file, open the actual Drive/shelf
   file FIRST. Search is a fallback, never the front door.

4. **UN-SILO.** Run `conversation_search` across lanes before claiming anything is
   missing or lost. Asserting without searching is a reliability-floor violation.

5. **GATE READ.** State the ship-gate status of anything live. An unfired gate =
   HALTED by default.

**PRE-SHIP GATE (mandatory, no exceptions):**

Before ANY file reaches the founder — present_files, deploy, or hand-off — run:

```
python3 preship-contrast-gate.py <file.html>
```

(`preship-contrast-gate.py` is in the repo root and Drive Claude_files
`1iD1CKw8W6lHVlyiJiH433pCvI3TgAx28`. If it isn't in the container, write it there
from Drive first.)

**exit 0 = ship. exit 1 = HALT — the file does not leave.** Not as a draft, not as a
"quick look," not as "I'll fix it after." Contrast is a COMPUTATION, not a judgment.
The founder has retinitis pigmentosa; contrast cannot be a step someone remembers.

**TOKEN-ROLE LAW:** Light may be dim. Text may not. A color token is atmosphere
(background / border / fill / gradient / screen-rim) OR it is text — never both. Any
token used in both a `color:` declaration and a decoration declaration is a HALT.
Split it: text gets its own bright token; decoration keeps the dim one. Text colors
ride tokens, never literals, so the gate can see them.

**DEPLOY ORDER IS LAW:** GATE → git push → POST-TICK (curl the raw file back, md5 must
match local). "Pushed" is never proof, exactly as "created:true" is never proof.

**BUILD-POOR CHECK (at every close):** name what a PLAYER can now do that they could
not before. If the answer is "nothing, but the pipeline improved," the session was
build-poor. Two build-poor sessions in a row = the next one is a BUILD session, no new
governance permitted.

────────────────────────────────────────────────────────────

---

## WHY THIS IS THE STRONGEST CARRIER

Three things survive a chat boundary: **memory** (full, and shared across all
projects), **Drive files** (only loaded if something tells a session to load them),
and **Project instructions** (read *before the founder's first word*, automatically,
in that project, forever).

Instructions are the only carrier that fires without being invoked. Memory can be
crowded out; Drive files can be ignored. This block cannot — a session in this project
reads it before it does anything else.

That is why the leak persisted: this field has been empty.
