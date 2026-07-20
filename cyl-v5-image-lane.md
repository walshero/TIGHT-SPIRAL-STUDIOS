# Choose Your Leader v5 — Image Lane manifest & generation prompts

*Tight Spiral Productions · walshero@gmail.com · companion to `choose-your-leader-v5.html`*
*Lane: dual, PD‑first, Ideogram‑fill (game spec §1.1 / §3.3). This doc IS the asset‑drop scaffold — every image slot in the game, its source target, and a ready‑to‑paste generation prompt.*

---

## The floors (every asset inherits these — non‑negotiable)

1. **A real face NEVER ships. A voice likeness NEVER ships.** The chair stays anyone's. Rooms are empty or shown from behind; crowds are wide/anonymous. This is why the game exists — the player judges the words, not a portrait.
2. **No baked text.** No letters, numbers, headlines, captions, or signage *in the image*. All text (the headline, the quote, the record) is rendered in code over the asset. Generate the *room / the object / the glow*, never the words.
3. **Center stays clear.** Composition leaves the middle uncluttered so the interface (notice‑spots, panel) sits on top cleanly.
4. **Period‑accurate + matte.** Documentary realism for the exact year; true cast shadows, warm, slightly worn; not glossy, not "cinematic teal‑orange."
5. **Studio‑Eyes‑ready.** Because text is added in code, the image only has to survive the contrast gate *underneath* text — keep a usable tonal zone where captions land (the game already handles this via its panel, but avoid a busy high‑contrast center).

**Global style suffix** — append to every generation prompt below:
> *…photoreal documentary photograph, {YEAR}, period‑accurate; lit chiefly by the television's glow; NO people, NO faces, NO figures; absolutely no text, letters, numbers, or signage anywhere; center of frame kept clear and uncluttered for a UI overlay; matte finish, true cast shadows, warm tungsten, slightly worn; 16:9 horizontal. Negative: text, words, caption, watermark, logo, people, faces, hands.*

---

## Where each step happens (the division of labor)

| Step | Where | Who |
|---|---|---|
| **1. PD sourcing** (real archival photos) | Library of Congress (loc.gov) · National Archives (catalog.archives.gov) · US Navy / DoD (all US‑gov = public domain) | You / an image session (this sandbox's egress can't reach them) |
| **2. Ideogram‑fill** (generate environments where no PD exists) | Ideogram · Adobe Firefly (the OS's in‑lane generator) · your ChatGPT Pro → Midjourney reference lane | You / an image session |
| **3. Composite → base64 ≤400 KB/room → Studio Eyes → ship** | a code session (here) | Me — drop assets in the repo or Drive and I wire, gate, deploy |

*The Adobe tools connected to this session only **edit** existing images (masking, fill, background removal) — they do not generate. Generation is step 2's job, not this sandbox's.*

---

## The slots

Each slot below maps 1:1 to a `data-art-*` schema in the game. When an asset is ready, fill: `data-art-src` (base64 or path), `data-art-license`, `data-art-author`, `data-art-source` (URL), `data-art-date`. Until then the shell renders its period‑toned SVG placeholder — nothing breaks.

### ERA ’62 — October 22, 1962 (`jfk62`)

**`room.jfk62` — the scene.** *"A living room lit only by a television set. It is nearly 7 p.m. Nobody has gone to bed."*
- **Source:** GENERATE (no PD room needed).
- **Prompt:** *A 1962 American living room at dusk, empty; a single console black‑and‑white television is on and is the only light source, casting a cool glow across an empty armchair, a patterned sofa, a side table; heavy curtains drawn; the room feels held, waiting.* + global suffix (YEAR 1962).
- **Record as:** license `AI‑generated (Ideogram/Firefly)`, author `Super Sketchy Graphics / TSP`, date of generation.

**`prelude.jfk62.a` — "U‑2 flights confirm missile sites in Cuba"** · *CIA reconnaissance, declassified · Oct 1962*
- **Source:** PD‑FIRST. The declassified U‑2 aerial reconnaissance frames of the San Cristóbal MRBM sites are **US‑government public domain** — the canonical asset. Target: **National Archives** (JFK Library / CIA declassified imagery) or LoC. Grainy top‑down aerial, no faces by nature.
- **Fallback:** generate a grainy monochrome aerial reconnaissance frame of rural terrain with faint rectangular clearings (no markings/text).

**`prelude.jfk62.b` — "Grocers report a run on canned goods"** · *Contemporary press, Oct 1962*
- **Source:** GENERATE (period press photos are usually rights‑encumbered). Prompt: *A 1962 supermarket aisle, shelves half‑emptied of canned goods, a lone shopping cart, fluorescent light* + suffix. No faces.

**`prelude.jfk62.c` — "Schools drill children under their desks"** · *Civil Defense footage, public domain*
- **Source:** PD‑FIRST. Federal **Civil Defense "Duck and Cover"** materials are public domain — National Archives. Prefer wide shots / empty classroom to keep faces out; or crop.
- **Fallback:** generate an empty period classroom, desks in rows, mid‑afternoon light.

**`prelude.jfk62.d` — "Three networks. One address. Tonight."** · *Broadcast listings, Oct 22 1962*
- **Source:** GENERATE. Prompt: *Close on a 1962 console television, screen warming to a blank glow in a dark room* + suffix. (Headline text is added in code — none in the image.)

### ERA ’64 — August 4, 1964 (`lbj64`)

**`room.lbj64` — the scene.** *"A den, past midnight. The set is still on. A bulletin has cut into the late movie."*
- **Source:** GENERATE. Prompt: *A 1964 American den after midnight, empty; a black‑and‑white television glows with a bright "bulletin" wash (no text) interrupting darkness; an empty recliner, a floor lamp off, a half‑finished drink on the side table; heavy shadow.* + suffix (1964).

**`prelude.lbj64.a` — "Reports of a second attack … Gulf of Tonkin"** · *Wire services, Aug 4 1964*
- **Source:** PD‑FIRST. **US Navy** photographs of **USS Maddox** / destroyers at sea are public domain (NARA / Naval History & Heritage Command). No faces.
- **Fallback:** generate a grainy monochrome open‑ocean horizon from a destroyer's rail at night.

**`prelude.lbj64.b` — "An election season; the incumbent runs as the steady hand"** · *Campaign press, 1964*
- **Source:** GENERATE (avoid candidate likeness). Prompt: *A 1964 street with campaign bunting and empty bleachers at dusk, red‑white‑blue swags, no people, no readable signs* + suffix.

**`prelude.lbj64.c` — "Late‑night bulletin interrupts programming"** · *Broadcast logs, Aug 4 1964*
- **Source:** GENERATE. Prompt: *A 1964 television screen filled with a bright blank broadcast wash in a dark den* + suffix. (No "BULLETIN" text — added in code.)

### ERA ’69 — November 3, 1969 (`nixon69`)

**`room.nixon69` — the scene.** *"A living room, early color television. The picture is a little unstable; the colors bleed at the edges."*
- **Source:** GENERATE. Prompt: *A 1969 American living room at night, empty; an early color television set glows, the picture slightly unstable with colors bleeding at the edges, casting shifting warm hues on an empty armchair and shag rug; wood paneling.* + suffix (1969).

**`prelude.nixon69.a` — "Hundreds of thousands march against the war"** · *Moratorium coverage, Oct–Nov 1969*
- **Source:** PD‑FIRST. **Moratorium to End the War** coverage held by **National Archives / LoC** includes public‑domain wide crowd shots. Use **wide/anonymous** framing only — no identifiable close faces.
- **Fallback:** generate a very wide, high‑angle anonymous crowd on a broad avenue at dusk, banners abstracted, no faces legible.

**`prelude.nixon69.b` — "Casualty figures read aloud on the evening news"** · *Network news, 1969*
- **Source:** GENERATE. Prompt: *Close on a 1969 color television set glowing in a dark room, the screen an unstable warm blur* + suffix. No faces, no text.

**`prelude.nixon69.c` — "The President will address the nation on Vietnam"** · *Broadcast advisory, Nov 3 1969*
- **Source:** GENERATE. Prompt: *A 1969 living room, the color television just switched on, warm glow filling an empty room* + suffix.

### Gated slots (`gate-a/b/c`)
Marked `[PENDING]` in the game and **excluded from play** — living‑president records are not fabricated. **No assets. Do not source or generate.** Leave them gated.

---

## Provenance tag (record on every embedded asset — OS §16.4)

Add an HTML comment beside each embed:
```
<!-- art: {slot} · {PD source & URL, or "AI‑generated: Ideogram/Firefly"} ·
     license: {Public Domain, US Gov | AI‑generated, TSP} · added {date} · refinish: {steps} -->
```
- **PD asset:** `data-art-license="Public Domain (US Gov)"`, `data-art-author="{agency}"`, `data-art-source="{archive URL}"`, `data-art-date="{original date}"`.
- **Generated asset:** `data-art-license="AI‑generated (Ideogram/Firefly)"`, `data-art-author="Super Sketchy Graphics / TSP"`, `data-art-source=""`, `data-art-date="{generation date}"`. Never labeled CC‑BY. Never presented as a real photograph of a real event unless it is a sourced PD photograph.

## Drop‑in contract (what I do when assets land)
1. You put finals (PNG/JPG, or a folder) in the repo (`/art/cyl-v5/`) or Drive and tell me the slot each maps to.
2. I refinish if needed, base64‑embed at **≤400 KB per room** (downscale/optimize), fill the `data-art-*` schema + provenance comment, swap each placeholder.
3. I run the **composite** through Studio Eyes (contrast under the text, image‑ratio, offline, no‑baked‑text), then push → the floor gate → deploy.

**You (or an image session) generate/source. I integrate, gate, and ship.**
