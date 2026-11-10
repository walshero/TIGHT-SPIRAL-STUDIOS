# Gate assessment: sidewalk-war v0.1 zoom and overlay miss (2026-11-09)

VERDICT: The belt passed this build because every entry gate measures first paint at 390 or 375 CSS px at 100% text size, counts image area by element box rather than by what is visible, and rates the 50% image floor as a WARN. No gate emulates zoom, a viewport at or under 320 px, or a moment after timed overlays appear. The gap is already named in the repo's own ledger as "still open". A small extension of one-thing-gate.py closes most of it.

## 1. Which gates measure entry paint, and at what size
- one-thing-gate.py:45 sets VIEWPORTS to 390x844 and 1280x800. Line 225 opens pages with only width and height: no device scale, no zoom, no text scaling.
- studio-senses/top-floor.py:22 uses 390x844 and 375x667 with is_mobile (line 87). Its floors are first paint only (header comment line 18).
- feedback-floor.py:77 uses device_scale_factor=2. feel-probe.py:108 uses 390x844. comfort-gate.py:152 uses 390x844. Nothing goes below 375 wide.
- Studio Fingers owns F-ZOOM, but that floor is only a 16 px input-font check (studio-fingers.py:28), not browser zoom.
- CLIPPED-TEXT-FLOOR-2026-09-01.md:222-227 states it outright: Studio Fingers measures first paint only, and "Nothing in the belt tries WCAG 1.4.4's 200% resize."

## 2. Any measurement after timed overlays appear
- one-thing-gate.py:241 waits 400 ms after networkidle, then measures once. The sidewalk-war note fires at 2500 ms (lab/sidewalk-war.html:216), so the gate never sees it.
- top-floor.py:89 waits 500 ms. senses-crawl.py settles 1200 ms (lines 225, 242). feel-probe.py waits 1200 ms (line 115). None reach 2.5 s on first paint.
- playthrough-agent.py does measure clipped text across crawled states (lines 229-241, 319-362). It is a report-mode sweep, not a CI gate (CLIPPED-TEXT-FLOOR doc, "Still open"), and it runs at reduced motion with its own VIEWPORT.

## 3. Does any gate detect an overlay covering the main visual
- No. one-thing-gate.py:56-62 takes the largest img/svg/canvas, intersects its getBoundingClientRect with the viewport, and divides by viewport area. It never asks what is painted on top. A card at lab/sidewalk-war.html:65 (.note, position:absolute over .stage, shown at line 283) leaves the canvas box unchanged.
- The one occlusion-aware probe is top-floor.py:14-18 and :56, which uses elementFromPoint with pointer-events forced on, but only for text in the top 140 px.
- The image floor itself is only a WARN: one-thing-gate.py:166-168 raises SUB-50-TABLEAU as WARN and defers to "studio-eyes owns the hard gate". The CLIPPED-TEXT doc records that studio-eyes/studio-eyes.py is not invoked by floor.yml.

## 4. Does any gate detect clipped text in h1 or chips
- Floor 11 CLIPPED_TEXT (studio-eyes/studio-eyes.py) and the playthrough-agent clip card (playthrough-agent.py:229, 648-649) exist. Both measure at their own single viewport, and neither is in the preship path I traced. I did not confirm Floor 11 ran on this build.
- Nothing in preship.sh, one-thing-gate.py, top-floor.py or preship-gate-v4.py checks overflow:hidden plus nowrap on the h1. The h1 rule is lab/sidewalk-war.html:56 (white-space:nowrap; overflow:hidden), the exact shape that hides a chip.

## 5. Known class in the ledgers
- Yes, in part. CLIPPED-TEXT-FLOOR-2026-09-01.md:43, 222, 226 record that the flip cards were correct at 100% and broken at 200%, and that elves-house was "found by hand, not by a gate".
- TSP_Ledger.md:1288 shows en195-course.html verified at 200% text reflow, by hand.
- TSP_Ledger.md:1257 and the 2026-10-15 CLAUDE.md rule record a fixed layer painting over buried text, which led to top-floor.py. That fix was scoped to text in the top 140 px.
- FUNES-LEDGER.md:194 shows playthrough finding CLIPPED TEXT (7) in choose-your-leader-v6 after the fact, which is the report-mode lane again.
- LAWS-REGISTRY.md:66 lists floor 14 OBSCURED (fixed overlays over unreachable text), which covers text and focus, not a canvas.
- No ledger entry covers a 320 px or sub-320 effective viewport, iOS text-size scaling, or visible-image ratio.

## 6. Smallest arithmetic check
Extend one-thing-gate.py. Touch three places.
1. VIEWPORTS at line 45: add (320, 568, 'narrow') and (230, 380, 'zoom170'). The second is the effective CSS viewport of 390x844 at about 170%. The current dedupe-by-code logic (lines 244-247) already keeps the worst finding per code.
2. MEASURE_JS at lines 56-62: replace the box intersection with a sampling pass over the largest visual using document.elementFromPoint on an 8 px grid. Keep both numbers, visualRatio (box) and seenRatio (visible). Grade on seenRatio.
3. The loop at line 241: after the first measure, call wait_for_timeout(4000), re-run MEASURE_JS, and keep the lower seenRatio. Also add an h1 clip count to MEASURE_JS.

Sketch for MEASURE_JS additions:
    let hit=0,n=0; const r=biggest.getBoundingClientRect();
    for(let x=Math.max(r.left,0)+4;x<Math.min(r.right,vw);x+=8)
      for(let y=Math.max(r.top,0)+4;y<Math.min(r.bottom,vh);y+=8){n++;
        const t=document.elementFromPoint(x,y); if(t&&(t===biggest||biggest.contains(t)))hit++;}
    const seenRatio=hit*64/VA;
    const h1clip=[...document.querySelectorAll('h1,h1 *')].filter(e=>e.scrollWidth>e.clientWidth+1
      &&getComputedStyle(e).overflow!=='visible').length;
Grade changes in grade() at line 166: raise SUB-50-TABLEAU from WARN to HIGH when seenRatio < 0.25 at any viewport (a number, not the old 50% target), and add H1-CLIPPED as HIGH when h1clip > 0.

What I measured, using a throwaway probe at /tmp/zprobe/probe.py (not part of the repo):
- 390x844 at t=0.5 s: box 55%, visible 55%. At t=4 s: box 55%, visible 33%. The existing box method reports 55% while a third of the canvas is covered, so the sampling pass sees the overlay at normal size.
- 230x380 at t=0.5 s: visible 33%. At t=4 s: visible 24%. A 25% HALT line would fire only here.
- 320x568: visible 51% at both times. 390 with CSS zoom 1.7: visible 42%.
- I did not reproduce the founder's 0% canvas or the clipped LAB chip. Headless Chromium used different font metrics and no iOS text inflation, so h1clip stayed 0 in every run. The founder's device may differ from any emulation here. The h1 clip check is justified by the CSS at line 56, not by a reproduction.

Surface count: not measured. I did not sweep the corpus, per cost rules. Because the 25% line is applied only at 230x380 and only to visible area, I expect few HALTs, but that is a guess. Run the changed check against changed files first, then decide on a ratchet baseline using the existing --init mechanism (one-thing-gate.py:244-250 freezes known codes).

Honest limit: even this check approximates the founder's view. A true text-zoom emulation needs a real iOS WebKit or Playwright's webkit project with text-size-adjust; Chromium's html{zoom} did not shrink the header the way he saw.
