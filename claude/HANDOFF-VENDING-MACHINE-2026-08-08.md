# HANDOFF — Workshop Vending Machine, comfort mount

Written 2026-08-08 at the end of a long session, for a fresh context window.
Everything below is verified against canon, not remembered. Hashes are real; check them.

---

## READ THIS FIRST, THEN STOP READING AND RUN ONE COMMAND

    bash studio-belt.sh <file.html>

That is new as of today and it is the most important line in this document. The belt
takes FILES now, not just a directory. All seven ticks, about ten seconds. Run it before
every push, on everything you touched. No exceptions, and no running gates one at a time.

The reason is the whole reason this handoff exists. Yesterday's session landed
`comfort-v3.html` after running SIX of the seven ticks by hand. The seventh exited 1.
`floor.yml` re-coupled deploy the same day, so that one file stopped the entire site
publishing, and nobody knew until a seven-lens review went looking hours later. The gate
that would have caught it in one line already existed. It was skipped because the belt
only accepted a directory, always walked 133 surfaces, and took minutes, so it was too
slow to use as a preflight and everybody fell back to memory. A checklist you run from
memory is not a checklist.

---

## THE JOB

Mount **comfort v3.1** into **`en195-arcade.html`** (the Workshop Vending Machine, four
cabinets, live). Then fold in the layout preview and delete it.

The arcade is the studio's most-finished student-facing build and it is the last real
surface still speaking the old comfort vocabulary. It has, as far as any instrument can
see, **none** of the five things the founder means by comfort.

### The founder's definition, verbatim, 2026-08-08. This is the spec.

> "Comfort is how you view content. It includes font size, contrast, modes like warm and
> dark, motion stop, and screen reader options."

### The arcade scored against it, measured today

    font size        hardcodes font-size:20px on :root  ->  OVERRIDES the reader
    contrast         works, worst pair 7.15
    warm and dark    data-stop="warmdark", night luminance 0.867 against a 0.2 ceiling
    motion stop      absent
    screen reader    absent (0 occurrences of clear-reader / c-reader)
    persistence      absent (0 occurrences of localStorage)

Six `data-stop` occurrences. Zero `data-light`. `comfort-gate` carries it as DEBT for
"NO DARK MODE (kernel not mounted)" and has since 2026-08-07. It is one of only three
files left on that vocabulary; the other two are its own layout preview and a canary.

### Belt status right now, so you know what you are starting from

    bash studio-belt.sh en195-arcade.html   ->  BELT: PASS, one debt line (comfort-gate)

It passes. Do not break that. In particular it PASSES `type-census` at 0 nodes under
18px, which makes it one of six clean surfaces in a 134-surface corpus carrying 4,171
nodes of debt. **But it passes for the wrong reason:** `:root{font-size:20px}` at line 10
makes everything big by overriding the reader's own browser setting. Right number, wrong
mechanism. Replace it with `font-size:100%` and rem multipliers, per the amended
standard, and the count must still hold at zero. Verify that, do not assume it.

---

## THE ONE REAL DESIGN DECISION

The arcade carries a **fixed dark palette** for the four guardian puppets (`scene0`, the
always-night arcade interior, plus the shadow-puppet silhouettes at line 787). That fixed
darkness is why `comfort-gate` reads 0.867 and it is why the puppets read at all.

**Ruling, proposed and not yet contradicted:** the puppet stage stays fixed-dark as its
own scene. Comfort governs the chrome and the reading surfaces around it. That preserves
the art and still delivers all five controls. If you disagree, say so before building,
not after.

---

## WHAT TO MOUNT, AND WHAT IS ALREADY FIXED IN IT

Source: `comfort-v3.html`, 35,100 bytes, sha256 `6a753a4ed473f38d…`, all seven ticks
clean. Do not rebuild it. It has already survived a seven-lens aleph pass and nine
fixes. Lift it.

What it gives the arcade:

- **Motion stop that works.** v2's rule merged an `@media` block into a selector list, so
  the CSS parser discarded it whole: measured 0 of 47 rules parsed. Two separate rules
  now. Never merge them. The comment above them says so.
- **Persistence, applied pre-paint**, so a reader who chose warm dark never sees a flash
  of daylight. Across 101 surfaces nothing remembered anything before this.
- **Clear Reader**, the screen-reader option, restored. It was the fifth stop of the
  original comfort control and commit `bc423ed` deleted it from 49 pages with no founder
  ruling recorded.
- **The control in the thumb arc**, bottom-right, not the top chrome. This also answers
  the `C-REACH` note studio-fingers currently prints on the arcade: its largest control
  sits at 480px of a 915px screen, above the bottom-40% arc.
- **A reader-controlled root** (`font-size:100%`), size steps as `font-size` not `zoom`.
- **`--control-edge` split from `--line`** for WCAG 1.4.11, which the arcade also fails
  and which no studio gate checks.

Nine defects were found in v3.0 by the fleet and fixed in v3.1. The three worth knowing
because they will bite you if you re-derive rather than lift:

1. **`all:revert` in Clear Reader resurrects hidden content.** It resets `display`, so a
   page's `display:none`, `[hidden]` and `visibility:hidden` content all became visible
   the moment the stop turned on. Measured: a `display:none` block came back as a 350x63
   box. This block gets mounted by 101 surfaces including games built out of unvisited
   branches and answer keys. v3.1 uses a named-property reset and re-asserts `[hidden]`.
2. **The panel clipped 34% of itself** at the largest size with no scrollbar and no fade,
   and what fell off the bottom was the Screen reader group. Moved up under Light.
3. **Motion stop could not be turned OFF** on a reduced-motion phone, because the media
   query was unconditional. An explicit choice must outrank the OS in both directions.

---

## FOUNDER RULINGS LANDED TODAY. DO NOT RE-LITIGATE.

- **"Comfort kernel" is not the founder's language.** Machine coinage from commit
  `3fa29e7`. His words: **comfort** is the capability, **Studio Eyes** is the internal
  name for the instrument. The control a reader sees is labelled **Comfort**. That label
  is also what makes v3 legal on player surfaces, because `retired-lines.json` bans the
  words "studio eyes" in rendered text outside `studio/`, zero tolerance, deploy coupled.
- **The 20px body line is retired.** One floor, 18px absolute, on every rendered node,
  enforced by `type-census.py`. The reader's browser setting supplies the base.
- **Clear Reader is its own toggle**, not a light-ladder stop, so it composes with warm
  dark instead of trading against it.
- **The leaderboard needs no login.** Verbatim: "No login needed." The board is
  self-declared; a name is a claim, not an authentication. Supabase posture unchanged:
  anon insert-only on `workshop_tokens`, select-only on `workshop_board`, RLS verified.
- **44x44 is the tap floor**, per the founder's own ruling in `PLAYTEST-REPORT.md` since
  July. The 48px "house floor" was derived from Apple by an agent, contradicted that
  ruling, manufactured 66 surfaces and 121 phantom halts, and its gate is retired. A
  session yesterday wrote the wrong version of this into the type standard and had to
  retract it in place. Do not repeat that. **When the founder and a machine-produced
  number disagree, the machine is the suspect.**

## STILL OPEN, GENUINELY

- **Retention and deletion policy for `workshop_tokens`.** Semester end, a fixed drop
  date, or on student request. Last founder-open on the arcade.
- Whether comfort becomes one linked shared file instead of 101 pasted copies. Real
  change to the offline floor; a founder call, not a cleanup.
- Non-text contrast is unmeasured studio-wide. WCAG 1.4.11 wants 3:1; the comfort block's
  own controls measured 1.50 to 2.07 before the `--control-edge` split. No gate checks it.

---

## WRITE-LANE HAZARDS. THESE COST REAL TIME TODAY.

`git push` from a session container returns 403. The Zapier `GitHubCLIAPI` connector is
the working lane. Three things that bit, all in one session:

1. **Chunks are decoded INDEPENDENTLY.** A byte-offset split that lands mid-character
   corrupts it. An em dash was cut across a boundary and landed as three replacement
   characters inside `studio-belt.sh`, a live gate. **Split on LINE boundaries**, and
   verify the reassembled sha256 locally before sending.
2. **`expect_total_bytes` is the check that caught it** (16351 against 16345). Always
   pass it. `success: true` is never proof.
3. **A chunk can error and leave canon truncated.** It happened once today, leaving a
   file at 12,471 bytes. Do not assume; call `verify_repo_binary` and compare the hash.
   `apply_patch_to_repo_file` INSERTS ONLY, it cannot replace or delete, and its param is
   a JSON string named `patch_json`.

---

## THE ORDER

1. `bash studio-belt.sh en195-arcade.html` and record the baseline output.
2. Mount comfort v3.1. Keep the puppet stage fixed-dark. Drop `:root{font-size:20px}`.
3. `bash studio-belt.sh en195-arcade.html` again. It must still PASS, `type-census` must
   still read 0 under 18px, and the `comfort-gate` DEBT line should now be GONE rather
   than carried, because the dark path becomes visible to the gate.
4. Push in line-safe chunks with `expect_total_bytes`. Byte-verify.
5. Fold the layout preview into canon, delete `en195-arcade-layout-preview.html`, and
   remove its line from `index.html`.
6. Ledger it.

## AND DO NOT

Do not build a second runner, a new gate, or a new doc unless something measured demands
it. The founder's words this session: *"No more stalking and empire building."* There are
already about thirty rules and seven ticks. If a rule cannot be a check, it is a wish; if
a check already exists, run it instead of writing another one.

---

Canon at handoff: `5f87478`. Verified this hour:

    comfort-v3.html                    35100  6a753a4ed473f38d
    type-census.py                      9641  6fe0fab8972f28dd
    type-baseline.json                  8162  80fb5b804e0c6836
    studio-belt.sh                     16345  0b5d9b7f9d6d4e88
    studio-type-contrast-standard.md    8517  d8449e7ada71677b
    en195-arcade.html                  57341  23e38d76d119b37b
    en195-arcade-layout-preview.html   62331  09fe5aaada47ea93

The vending machine has been waiting to breathe since 2026-08-05. Give it the five
controls and get out of its way.
