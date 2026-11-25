# Xenos Island rebuild: spec (updated 2026-11-25, 17:45 ET)

source: Xenos trailer (youtu.be/_Cmyn-eo4_o) + all 34 2013 LGN tutorial clips (Matt's copy: Drive 1bssnnrvJvIP9fMSVkk_nQURTUwSUbe7t, Mac ~/Downloads/Videos)
feature dossier: claude/XENOS-FLASH-REFERENCE-2026-11-25.md; games spec: claude/SPEC-XENOS-THREE-GAMES-2026-11-25.md; island map: Xenos Isle.jpg (Drive 1030PAuz2b4j6sENzP6C0AXlWbqa46M4k); inventory: claude/XENOS-DRIVE-INVENTORY-2026-11-24.md
current build: xenos-v0.12.html (repo lab/xenos.html, commit 2b27e34), 1,239,096 bytes, sha256 7c79dfd6d3190bff4322f2067a1fbc8a0933f6e66ca6ddd269efdf5b3d863461
lanes: repo walshero/TIGHT-SPIRAL-STUDIOS lab/xenos.html (blob 34fafb4c verified on origin); Drive Claude_files id 1e3ZEApsUYBBubndnZa5yfaK7ZjCY47V8 (size verified); public artifact https://claude.ai/artifact/AEwEFKBSEL12GBEk7x5Mxa version 1795646613-f2a7 (sha256 verified). Earlier: v0.11 Drive 1AXzAmLGx_XBD3gSKa5_vC9NkWicBd4-p; v0.9 1KiSHdCTQxl36eSMJJSb10CCFaW0oTM4s; v0.8 1hyaS0MsEPCKUBP_DGp3CK-i9RRWmcE-f. Project shelf FULL for builds.
audience: adult English learners (Spanish glosses), and the teachers and coaches who guide them. Carried from Xenos 2013 (LGN learning paths, coaches, Spanish glosses); founder to confirm for the rebuild.
rights: Matt holds the rights personally. direction: 2012-13 FLASH era.

## Founder rulings
- 2026-11-24: clone the art closely; original characters; crisper; fit phone and desktop, smaller characters.
- 2026-11-25: use the tutorial videos to expand; NO orange ground arrows; NO page loads or fades when travelling (ONE world); keep the player out of the outer 20% of the screen.
- 2026-11-25: reference ALL the videos.
- 2026-11-25: republish the public artifact without asking, going forward.
- 2026-11-25: next build focuses on crisp graphics and on layering; the player crosses over the setting often, so work out layers and physics.

- 2026-11-25 17:23: phone feels like a laptop seen through a keyhole; player way too small; world size, navigation and art all need work; compare to successful similar games. (Reconciles with 11-24 "smaller characters": that was desktop. Phone gets its own camera.)
- 2026-11-25 12:52: v0.8 landscape is blurry, glitchy, layers off, seams noticeable; wants game-design skills. 12:54: map out the whole island; needs a studio tool or skill for this.

## v0.9: the whole island, props not plates
Why: v0.8 stitched filmed screens into one picture. Seams, soft fill and objects cut at plate edges are built into that method, so it was replaced.
| Area | v0.9 | Check |
|---|---|---|
| Layout | Island shape, districts and roads traced from the original Xenos Isle map (Drive 1030PAuz2b4j6sENzP6C0AXlWbqa46M4k) at 5 world px per map px: 3750x2500. University NW, Lobby centre, Market E, Pier SW, Palace Gardens SE, Windmill Hill N. Roads routed overland (A* away from shore) | all 20 footprints on land |
| Ground | Vector shapes drawn every frame: sea, shallows, surf line, sand rim, grass, brick roads with curbs, plazas (brick Market, flagstone University, boardwalk Pier). Textures: native Market brick (period 25x10, tiles exactly), grass and sand painted procedurally from the native palette (#51cd40 family), flagstone and deck quilted from native frames; all stored 2x | no seams by construction; crisp at every zoom |
| Buildings | 17 separate sprites (15 cut from the 2x world, train and Glyphs ruin cut fresh from native video and super-resolved), 20 placed instances, contact shadows | atlas review |
| Depth | Sprites drawn back to front by footprint; a person behind a footprint's front edge gets the sprite redrawn over them | filmstrip ring around 10 props, 60 frames, all correct |
| Collision | Footprints padded 7 px; 8 px grid | 240 routes between districts and kiosk doors: all found, 0 samples inside a footprint, max 8.3 ms |
| Kiosks | Each game at its 2013 landmark: Glyphs ruin, Rails train, Empty Handed sign, In Other Words cart, Breaking News stand; Fish Tank (Week 1 mission), Market Pagoda, Fish Shop, Notice Board, Xenos University clock tower | Places and Games lists walk there |
| Gates | contrast SHIP 9.89 (repo 4f7c4ce); 0 emoji; no external hosts; 0 console errors desktop and phone 3x | Playwright |
Pipeline (workspace): /home/claude/isle (layout.py, place.py, plaza.py, props.py, cutnative.py, mktex*.py, mkproc.py), /home/claude/xenos-island/build9.py + engine-v0.9.js. Studio skill proposed: iso-world-builder.

## v0.8: crisp pass + layering + physics (superseded)
| Area | What changed | How it was checked |
|---|---|---|
| Crisp art | Pier and part of University re-composited from native 1056x720 tutorial frames (games clip holds, per-pixel median, scroll-stitched), registered onto the plates by SIFT (scale ~1.05, residual under 1 px), baked-in player masked out. Fish house now whole (roof, door, string lights) | side-by-side crops vs v0.7 |
| Resolution | Whole world super-resolved 4x (Real-ESRGAN anime6B, CPU) and stored at 2x (4800x3040 WebP q82, 867 KB). Drawn from the 2x source, so phones (3x) and retina stay sharp | desktop 2x and phone 3x screenshots |
| Layering | 31 objects, each with a ground footprint and a pixel-exact cutout (GrabCut seeded by the extruded footprint; canopy hint for trees). Player is behind an object when the feet are above the object's front edge at that x; the cutout is then redrawn over the player, clipped to the player's box | scripted test: player placed just behind and just in front of every object, 62 screenshots, all correct |
| Physics | Collision from the same footprints, padded by a 7 px player radius; path grid 8 px (was 12) so lamp posts register; old hand-drawn blockers retired | 56 cross-district routes: all found, 0 samples inside any footprint, 1-12 ms each |
| Debug | `?debug=1` draws footprints (yellow) and front edges (red) and exposes a test hook | dev only |
| Gates | contrast SHIP (worst pair 9.89, repo 4f7c4ce); no emoji; no external hosts; 0 console errors | Playwright |

Pipeline files (workspace): /home/claude/mos (frame extract, holds, composite), /home/claude/sr (super-resolution, patch), /home/claude/lay (objects.py footprints, genmask.py), /home/claude/xenos-island/build8.py, /home/claude/t8 (occlusion, physics, view tests).

## Known gaps (v0.9)
- Sparse: the island has 20 props on a lot of open grass. The Flash rooms were dense. Palace Gardens and Windmill Hill are open land with no buildings yet.
- Prop variety is small (3 copies of one tree). More props need cutting from the remaining native holds (crab-roof shop, octopus dome hut, lamps with string lights, Glyphs garden plants, shell-house Lobby from the trailer).
- Props come from 2013 video upscaled 4x: sharp at normal zoom, slightly soft at the closest phone zoom.

## Next
1. Density pass: cut 15 to 25 more props from native holds; scatter planters, lamps and benches along roads with a placement rule.
2. Missions: fish tank in the Pier; blue-roof building in the Market.
3. Glyphs as the first playable game.

## v0.12: phone-first camera (2026-11-25)
Measured on v0.11 at 390x844: the phone camera showed 540 world px across (scale 0.72) while desktop showed 1100 (scale 1.07). The phone was zoomed OUT relative to desktop. Player about 46 css px tall, 5.5% of screen height. Chrome (header, nav, say bar) took about 20% of the screen.

Benchmark (sources: Stardew Valley wiki mobile controls; TouchArcade and GameIndustry mobile reviews; Stardew sprite spec 16x32 at 4x):
| Measure | Xenos v0.11 phone | Stardew Valley (PC 1080p, 100%) | Xenos v0.12 phone |
| Player height / screen height | 5.5% | about 12% (128 of 1080 px) | about 10% |
| Movement | tap to walk | tap to walk, hold to follow finger, tap NPC to walk and talk | tap, plus hold to follow finger |
| Zoom | fixed | pinch zoom (reviewers single it out; zoom out to tap far, walk there) | fixed phone zoom |
| Screen given to UI | about 20% | small corner HUD | about 14% (header hidden on phone) |

Shipped in v0.12: phone shows 320 world px across (tablet 600; desktop unchanged); header hidden on screens 700 px and under; hold-to-follow-finger on the canvas (re-paths every 140 ms).

Plan, ranked by return:
1. World size: compress walking distances about 40% (Market to every district under 8 s of walking at phone zoom); fill or cut empty grass (W-EMPTY warns at 60% on Windmill Hill). Pocket Camp's answer to a big world on a phone is small dense areas plus a travel map; Xenos keeps one continuous world, so the answer is density, not fades.
2. Art: characters are 2013 video sprites at 2x; at phone zoom they render about 1.2x past source and read soft and thin. Redraw the six characters in house (Figma vector, 4x) with a thicker silhouette and outline so they read at 100 css px.
3. Navigation: tap an NPC or kiosk to walk there and talk (Stardew pattern); a zoom-out button (not pinch, which misfires on touch) for tapping far points; Places stays the voice and keyboard route.
4. Chrome: fold the say bar into a button that opens the keyboard on demand; the world then gets about 92% of the phone screen.
