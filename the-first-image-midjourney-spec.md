# The First Image
### A Midjourney spec for one asset — the balloon under tension
*Tight Spiral Studios · walshero@gmail.com · scoped by Cleese (don't spiral) and Saunders (withhold; start with one image and let it teach you the rest).*

---

Here is a thing that wants to fly and can't.

That is the whole game in one picture, and it is the only picture you are going to make today. Not a bible. Not eleven assets. One balloon, roped to the ground, straining — and once you have it on your phone, behind the live game, *it* will tell you what the next prompt should be. The spec for the rest writes itself after you have seen the first one land. That is the discipline here: the document is small on purpose.

---

## The three roles (no tool is the approver but you)

- **ChatGPT Pro — the prompt engine.** It writes and refines the Midjourney prompt and holds the style block. It is blind to the render; it proposes, it never approves.
- **Midjourney Pro — the renderer.** It makes the image. It cannot make text and it has no opinion about your floors. It renders, nothing more.
- **You + me — the only approver.** The one judgment that can both *see* the image and check it against the floor (skin-tone-neutral, no baked-in text, phone-light, comfort-safe) is the human in the loop. That is the whole reason this is a handoff and not a hook.

---

## Set ChatGPT Pro up once (so it writes MJ prompts, not prose)

1. ChatGPT, left sidebar → **+ New Project** → name it **"Tight Spiral — Scriptorium (art)"**. (If your Scriptorium project already exists, use it.)
2. Open the project → find **Instructions** (the project's settings panel, usually a button near the project name at the top). Paste this:

   > You write Midjourney prompts for Tight Spiral Studios. House look: **pre-steampunk circus Dada meets BioShock brass-machine** — Victorian letterpress, woodtype, riveted brass, hand-built diorama, warm paper, true cast shadows, matte (not glossy), slightly worn. Output **only** a Midjourney-ready prompt string plus the `--ar` and any params — no preamble, no explanation. **Hard rules, every prompt:** (1) NO text, letters, numbers, or signage in the image — text is added later in code. (2) NO human figures with realistic skin or faces — figures, if any, are neutral kraft-paper/cardboard forms only. (3) Transparent or flat single-color background when I ask for an isolated object. (4) Composition leaves the center clear for an interface to sit on top. Ask me one clarifying question only if the subject is ambiguous.

3. That's the setup. From now on you tell ChatGPT *what asset you need*, it hands you a clean MJ prompt.

---

## The one prompt — the balloon under tension

You can paste this straight into Midjourney, or paste the plain-English version into ChatGPT Pro and let it refine. Either works. Here is the direct one:

```
a single hot-air balloon made of torn kraft paper and letterpress scraps,
roped tightly to the ground by many taut cords, straining upward, circus
playbill texture, riveted brass basket, pre-steampunk handmade diorama,
warm aged paper, true cast shadows, matte finish, slightly worn edges,
centered object on a flat warm-paper background, no text, no people
--ar 9:16 --style raw
```

Why these choices, briefly:
- **`--ar 9:16`** — phone-shaped, because the game is played on a phone and the balloon rises *up* the screen. Vertical is the whole point.
- **"roped tightly… straining upward"** — the *tension* is the story. A calm floating balloon is the wrong image; this one wants to escape. That tension is what the cutting releases.
- **"no text, no people"** — your two hard floors, in the prompt itself, every time.
- **"flat warm-paper background"** — so I can drop it behind the live HTML cleanly.

Generate it. Make a few variants. Pick the one where the *strain* reads — where you can feel it pulling against the ropes. That feeling is the accept/reject test, not polish.

---

## The reject gate (what makes an image fail)

Send it back and regenerate if any of these are true:
- It has **text or numbers** anywhere (MJ will try; refuse them).
- It has a **person with skin/face** (breaks the neutral floor).
- The balloon looks **calm or floating** instead of *roped and straining* (wrong story).
- The background is **busy to the center** (no room for the interface).
- It reads **glossy / 3D-render slick** instead of **handmade paper** (wrong medium).

One good image beats ten almost-rights. Withhold until one lands.

---

## Pipeline insertion — how it gets from Midjourney into the game

1. **Generate** in Midjourney. Pick the one where the strain reads.
2. **Upscale** it (Midjourney's U button under the grid), then save the full image to your phone.
3. **Name it by what it is**, not the moment: `sandbags-balloon-strain.png`. (Your file-naming rule — no "-final", no dates in the name.)
4. **Save it to Google Drive `Claude_files` from your phone** — the one shelf, the save device. This is the step that makes it real; a download that never reaches the shelf is a ghost.
5. **Hand it to me** in a chat (attach the image, or tell me it's in the Project). I composite it **behind the live HTML** of `sandbags.html` — the balloon becomes the backdrop; your text, buttons, and the altitude meter stay real, accessible DOM on top. The picture never traps the words.
6. **I re-run Studio Eyes** — confirms the composite didn't break contrast, didn't bloat the file past phone-load, didn't bury a control.
7. **You playtest on the phone.** Does the balloon's strain make you *want* to cut? That's the only verdict.

Then — and only then — we write the prompts for the sandbags, the brass console, the playbill, from what the first image taught us.

---

## What this spec deliberately does NOT do

It does not specify eleven assets. It does not lock a full style bible. It does not build a research pipeline or a permanent art org. Cleese's rule: the art doctrine for a game with zero rendered images would be the funniest document in the studio, and we are not writing it. Saunders' rule: start with one image, let it teach you the rest. Same conclusion from both chairs.

One balloon. Roped. Straining. Go see it.

---

*Tight Spiral Studios · walshero@gmail.com — pipeline insertion for the Scriptorium art lane (ChatGPT Pro → Midjourney → composite → Studio Eyes → you). Skin-tone-neutral and no-baked-text floors are written into the ChatGPT Pro instructions so every future prompt inherits them. Save this to the Project from your phone to keep it.*
