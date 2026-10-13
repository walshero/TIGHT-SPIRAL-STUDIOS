# RULING — 110%, and a chrome that gets out of the way (2026-10-13)
<!-- source: Matt, by voice, 2026-10-13: "I want things large because of accessibility, but right now they're too large ... if right now I'm at 125%, let me just go 110%"; on Studio/Cabinet: "way, way, way too big ... I want to make sure persistently that they scroll away when you're moving ... studio-wide"; on underlines: "bring that onto its own line ... not too far away from the text" | owner: mwalsh | status: FLOK LANDED, STUDIO ROLLOUT PENDING -->

**Plan, as agreed by voice:** Flok first. The founder feels it on his phone. Then it rolls out studio-wide and new games are born at this size.

## What 110% means, measured
- **Body and captions: 19px to 18px.** The 18px floor is law (retinitis pigmentosa) and is never crossed to chase "normal". A typical app is 15-16px.
- **Headlines and buttons do not change.** They carry the scene and the tap targets.
- **Studio / Cabinet:** plain underlined links at 18px (the RP link ruling: "Link. Per RP. Always."), 44px hit area kept, no box, no mono. Bar 68px to 49px.
- **The bar scrolls away.** No `position: sticky` or `fixed` on `.se-chrome`.
- **Underlined links stand on their own line**, never inside a sentence, with the hit area made of padding below the text so the line above does not drift away.

## Status
- **Flok v30: LANDED** (the-console.html). Smallest text 18px; senses, belt and gates green.
- **STUDIO ROLLOUT: PENDING the founder's phone check of Flok v30.** `chrome-scroll-check.py` lists the pages still to change (98 pages pin the bar and 104 still use the boxed buttons on 2026-10-13; a first single-line grep had said 14 and was wrong, which is why this is a script). When approved: apply the same three CSS changes per page, run the belt on changed files, then add chrome-scroll-check to the belt as a tick.
