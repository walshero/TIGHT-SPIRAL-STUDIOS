# Choose Your Leader v5 — Image Lane manifest (slot map + sourcing + drop‑in)

*Tight Spiral Productions · walshero@gmail.com · companion to `choose-your-leader-v5.html`*
**Art direction is owned by `cyl-period-bible.md` — this doc does NOT re‑decide it.** This is the operational layer: which slot is which, where each asset comes from, how it drops in and gets gated.

---

## Reconciliation — 2026‑07‑20 (two rivers, one ledger)

This file was first written (2026‑07‑19) prescribing **AI‑generated photoreal** rooms. That was off‑canon and is now corrected. Reconciled against the TSP project chat's CYL work as it lands in the repo (I can't read that chat directly — the cross‑chat access boundary in `CYL_Harvest…md`; the repo is the shared ledger):

- **`edec2e1` — "draw the world":** the three era rooms ship as **handcrafted SVG dioramas** (`paintRoom()`), *honestly illustrative, never [smooth‑AI] photoreal* — the **"Greg the pancake" ruling stands.** This is the **current live floor.**
- **`cyl-period-bible.md`:** the canonical promotion — a **composite** build: a real **photographic room** + a **withheld figure**, across the 62/64/69 era ladder. **No real faces, ever.**
- **Founder ruling (2026‑07‑20): _magazine collage IS photoreal._** The photographic layer is achieved by **cutting and compositing real period print** (LIFE / Look / newspapers / ads of the exact year) — genuinely photographic **and** period‑authentic (real film stock carries the real color science for free), while sidestepping both AI‑hallucinated photoreal and the Greg‑the‑pancake trap.

**Net canonical state:** SVG diorama = shipped floor. **Magazine‑collage composite = the promotion** (produced in an image‑capable session, composited behind the live interactive layer). Never smooth‑AI‑photoreal. The figure is always withheld.

---

## The floors (every asset inherits these)

1. **No real faces / no voice likeness — ever.** The leader is *made of the broadcast* (scan‑lines '62/'64, unstable‑color smear '69), never a resolved face. The empty chair is *you* — anyone. (Period‑bible withheld‑figure law; game spine.)
2. **Photoreal = collage of REAL period print, not AI‑generation.** Magazine/newspaper/ad clippings of the exact year, cut and composited. AI is only ever a *compositing/finishing* assist on real material — labeled "Super Sketchy Graphics, AI‑assisted," never CC‑BY, never "a real photo of a real event" unless it *is* a sourced archival photo.
3. **No baked GAME text.** Period print *as texture/atmosphere* is allowed (a torn ad, a masthead fragment) — but it must carry **no read‑line the game needs** (those live in the panel + alt‑text) and must not smuggle in a real leader's face or a legible endorsement. When in doubt, blur/crop it to texture.
4. **The seam is the meaning.** Vivid, specific, dated *world* + deliberately blank *person*. Light, grain, and scale must reconcile across that seam or the Compositor HALTs.
5. **Accessibility holds.** Grain/color are atmosphere, never the sole signal; every rhetoric the image carries also lives in alt‑text. Full‑contrast text floor untouched.

---

## Where each step happens

| Step | Where | Who |
|---|---|---|
| **Art direction** (color science, per‑scene, withheld figure) | `cyl-period-bible.md` | Locked |
| **Collage material — PD‑first** (real archival print/photo) | Library of Congress · National Archives · US Navy/DoD (US‑gov = public domain) | You / an image session (sandbox egress can't reach them) |
| **Compose the collage** (cut, layer, grain, seam) | an image‑capable session (period print + optional Super Sketchy Graphics AI finishing) | You / an image session |
| **Composite → base64 ≤400 KB/room → Studio Eyes → ship** | a code session (here) | Me — drop assets in the repo/Drive and I wire, gate, deploy |

*The Adobe tools in this session only **edit** existing images (mask/fill/bg‑removal) — useful for collage finishing, not for generating. No text‑to‑image here.*

---

## The slots

Each maps 1:1 to a `data-art-*` schema in the game. Fill `data-art-src` (base64/path), `-license`, `-author`, `-source` (URL), `-date` when an asset lands; until then the SVG diorama (edec2e1) stands. **Room direction: follow the period bible's per‑scene section — do not re‑spec it here.**

### ERA ’62 — Oct 22, 1962 (`jfk62`) — *Kodachrome, cool, hopeful; B&W broadcast*
- **`room.jfk62`** — collage a 1962 living room from period print (mid‑century furniture, cool Kodachrome walls); the console **B&W** set is the only light; withheld scan‑line figure on screen; empty armchair = you. Per bible Scene 1.
- **`prelude.jfk62.a`** "U‑2 flights confirm missile sites in Cuba" — **PD‑FIRST:** declassified U‑2 recon frames (San Cristóbal MRBM sites), **National Archives / CIA** — US‑gov public domain, no faces by nature.
- **`prelude.jfk62.b`** "Run on canned goods" — collage a period supermarket‑shelf clipping (no faces); PD where the print allows, else generic era stock.
- **`prelude.jfk62.c`** "Duck‑and‑cover school drill" — **PD‑FIRST:** federal Civil Defense materials (**National Archives**), wide/empty framing or crop to keep faces out.
- **`prelude.jfk62.d`** "Three networks. One address." — collage a 1962 console TV, blank warming glow. No headline text baked in.

### ERA ’64 — Aug 4, 1964, midnight (`lbj64`) — *a year heavier; cold B&W bulletin*
- **`room.lbj64`** — same room a year tireder, near midnight; cold B&W bulletin cut‑in, two flag *shapes*, wall map; withheld silhouette. Per bible Scene 2.
- **`prelude.lbj64.a`** "Second attack, Gulf of Tonkin" — **PD‑FIRST:** **US Navy** photos of USS Maddox / destroyers (NARA / Naval History & Heritage Command), no faces.
- **`prelude.lbj64.b`** "Election season, the steady hand" — collage period campaign material *without candidate likeness* (bunting, empty bleachers).
- **`prelude.lbj64.c`** "Late bulletin interrupts programming" — collage a 1964 TV, blank broadcast wash.

### ERA ’69 — Nov 3, 1969 (`nixon69`) — *Ektachrome amber, decaying; first unstable color*
- **`room.nixon69`** — warmer, faded, worn; early **unstable color** set, colors bleeding; warm smear where a face would be. Per bible Scene 3. *(Open founder call in the bible: early‑color vs ambiguous B&W.)*
- **`prelude.nixon69.a`** "Hundreds of thousands march" — **PD‑FIRST:** Moratorium coverage (**National Archives / LoC**), **wide/anonymous** crowd only — no identifiable close faces.
- **`prelude.nixon69.b`** "Casualty figures on the evening news" — collage a 1969 color TV, unstable warm blur.
- **`prelude.nixon69.c`** "President will address the nation" — collage a 1969 living room, color set just switched on.

### Gated slots (`gate-a/b/c`)
`[PENDING]`, **excluded from play** — living‑president records not fabricated (and the living‑president image lane is an active rights/disinfo hazard — see `CYL_Harvest…md`). **No assets.**

---

## Provenance (OS §16.4 — record on every embed)
```
<!-- art: {slot} · {archive source & URL | "period-print collage: {titles, year}" | "Super Sketchy Graphics, AI-assisted"} ·
     license: {Public Domain, US Gov | period print, see note | AI-assisted, TSP} · added {date} · steps: {cut/composite/grain} -->
```
- **PD archival:** `data-art-license="Public Domain (US Gov)"`, `-author="{agency}"`, `-source="{URL}"`, `-date="{original}"`.
- **Period‑print collage:** name the publications + year; flag rights (much post‑1963 print is still in copyright — prefer PD or clearly transformative/fair‑use crops; when unsure, ask before ship). Never labeled CC‑BY; never presented as a single authentic photograph of the event.

## Drop‑in contract (mine, when material lands)
1. You put finals in the repo (`/art/cyl-v5/`) or Drive and name the slot each maps to.
2. I finish/optimize, base64‑embed **≤400 KB/room**, fill `data-art-*` + provenance, swap the placeholder.
3. I run the **composite** through Studio Eyes (contrast under text, seam/opacity, offline, no‑baked‑game‑text), then push → floor gate → deploy.

**You (or an image session) source period print + compose the collage. I integrate, gate, ship. Art direction: the period bible.**
