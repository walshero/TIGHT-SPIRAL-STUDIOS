#!/usr/bin/env python3
"""Signal Rider v0.16. Founder 2026-11-09 19:28:
"Rebrand 'alarm road' - and let's make green boxes now act as accelerators and damaged bands
or pink boxes slow you down. Also the white dot matching sequence is much too easy. Needs to
be real work with slight quick puzzle element."
- "alarm road" -> "survival shortcut" (LeDoux's low road: the fast, protective route that
  skips the thinking cortex). Science terms like "alarm center" stay.
- Greens surge the spark to 1.3x cruise, fading over about 2 s (healthy insulation conducts
  faster). This reverses the 2026-11-05 "greens must not affect speed" ruling, by founder say-so.
  Reds and frayed bands keep their slowdown (speed x0.45, recovers over 0.9 s).
- The landing becomes lock-and-key: every spine carries a receptor shape; each beat the
  center shows a messenger shape (and plays its tone). Only the spine whose receptor matches
  counts. No white target marker. Neurotransmitters bind only receptors that fit them.
Base: canon v0.15 (91f29e83)."""
import hashlib, re
P = 'lab/down-the-nerve.html'
s = open(P).read()
assert hashlib.sha256(s.encode()).hexdigest().startswith('91f29e83'), 'base is not canon v0.15'
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)

rep('<title>Signal Rider v0.15</title>', '<title>Signal Rider v0.16</title>')
rep('<span class="chip">v0.15</span>', '<span class="chip">v0.16</span>')

# ---- rename the path (text only; code identifiers keep their names)
s = s.replace('Alarm road pull', 'Shortcut pull')
s = s.replace('Alarm road', 'Survival shortcut').replace('alarm road', 'survival shortcut')
s = s.replace('alarm-road pull', 'shortcut pull').replace('alarm-road', 'survival-shortcut')
s = s.replace('thorny alarm face', 'thorny shortcut face').replace('alarm face', 'shortcut face')
assert 'alarm road' not in s.lower()

# ---- greens surge, reds slow
rep("var BANDMAX=2.0,BANDMIN=0.35;", "var BANDMAX=2.0,BANDMIN=0.35,SURGE=1.3;")
rep("run.floatTxt='+ clear path';sfxGood();}", "run.floatTxt='+ clear path';sfxGood();run.surgeT=2.0;run.v*=1.15;run.boostT=Math.max(run.boostT,0.35);}")
rep("else{run.v+=(cruise-run.v)*Math.min(1,dt*(run.v>cruise?0.6:1.2));}",
    "else{var tgtv=cruise*(run.surgeT>0?SURGE:1);run.surgeT=Math.max(0,(run.surgeT||0)-dt);run.v+=(tgtv-run.v)*Math.min(1,dt*(run.v>tgtv?0.6:1.6));}")

# ---- lock-and-key landing
rep("function landingBeat(sy){",
"""var SHAPES=['circle','triangle','square','diamond','plus'],SHAPE_HZ={circle:392,triangle:494,square:587,diamond:659,plus:784};
function shapePath(c,x,y,r,k){c.beginPath();
  if(k==='circle'){c.arc(x,y,r,0,TAU);}
  else if(k==='triangle'){c.moveTo(x,y-r);c.lineTo(x+r*0.95,y+r*0.75);c.lineTo(x-r*0.95,y+r*0.75);c.closePath();}
  else if(k==='square'){c.rect(x-r*0.82,y-r*0.82,r*1.64,r*1.64);}
  else if(k==='diamond'){c.moveTo(x,y-r);c.lineTo(x+r,y);c.lineTo(x,y+r);c.lineTo(x-r,y);c.closePath();}
  else {var w=r*0.38;c.rect(x-w,y-r,w*2,r*2);c.rect(x-r,y-w,r*2,w*2);}}
function keyOf(sy,pa){var i=sy.pads.indexOf(pa);return sy.rshape?sy.rshape[i]:SHAPES[0];}
function playKey(sy){if(!run.lm)return;var k=keyOf(sy,run.lm.tgt);run.lm.key=k;if(AC&&S.sound)tone(SHAPE_HZ[k],0.22,'triangle',0.08);}
function landingBeat(sy){""")
# receptor shapes are dealt when the landing starts; the first key sounds at once
rep("  BEAT=[1.0,0.92,0.85,0.8][run.leg]||0.8;",
    "  BEAT=[1.0,0.92,0.85,0.8][run.leg]||0.8;\n  if(!sy.rshape){var sh=SHAPES.slice();for(var q=sh.length-1;q>0;q--){var j=Math.floor(Math.random()*(q+1));var t=sh[q];sh[q]=sh[j];sh[j]=t;}sy.rshape=sy.pads.map(function(p,i){return sh[i%sh.length];});}")
rep("  lm.tgt=nextTarget(sy);\n}", "  lm.tgt=nextTarget(sy);playKey(sy);\n}")
# a full landing on the wrong receptor gets its own sound: the key did not fit
rep("var lm=run.lm;lm.k++;var d=Math.abs(angDiff(run.theta,lm.tgt));var full=d<0.25,half=!full&&d<0.5;",
    "var lm=run.lm;lm.k++;var d=Math.abs(angDiff(run.theta,lm.tgt));var full=d<0.25,half=!full&&d<0.5;\n"
    "  if(!full&&!half&&sy.pads.some(function(p){return p!==lm.tgt&&Math.abs(angDiff(run.theta,p))<0.25;})&&AC&&S.sound){tone(150,0.18,'square',0.06);}")

# drawing: no white target; a receptor shape on every spine, the messenger key at the center with the closing ring
rep("""  if(run.lm&&sy&&zf>0.3){ // target spine: white, with a ring closing on the beat
    var lm=run.lm,p=proj(lm.tgt,zf,1.0),rr0=Math.max(8,0.26*f/zf),ph=1-((lm.t%BEAT)/BEAT);
    cx.fillStyle='#ffffff';cx.shadowColor='#ffffff';cx.shadowBlur=blur()*3;cx.beginPath();cx.arc(p[0],p[1],rr0,0,TAU);cx.fill();
    cx.strokeStyle='#ffffff';cx.lineWidth=4;cx.globalAlpha=0.9;cx.beginPath();cx.arc(p[0],p[1],rr0*(1.3+2.2*ph),0,TAU);cx.stroke();cx.globalAlpha=1;cx.shadowBlur=0;}""",
"""  if(run.lm&&sy&&zf>0.3&&sy.rshape){ // lock and key: receptor shapes on the spines, the messenger in the center
    var lm=run.lm,ph=1-((lm.t%BEAT)/BEAT),rs=Math.max(9,0.24*f/zf);
    sy.pads.forEach(function(pa,i){var p=proj(pa,zf,1.0);cx.fillStyle='#04050a';cx.globalAlpha=0.85;cx.beginPath();cx.arc(p[0],p[1],rs*1.35,0,TAU);cx.fill();cx.globalAlpha=1;
      cx.fillStyle='#ffffff';cx.shadowColor='#ffffff';cx.shadowBlur=blur();shapePath(cx,p[0],p[1],rs,sy.rshape[i]);cx.fill();cx.shadowBlur=0;});
    var kx=cxv,ky=cyv,kr=Math.max(22,0.07*Math.min(W,H)),k=lm.key||keyOf(sy,lm.tgt);
    cx.fillStyle='#04050a';cx.globalAlpha=0.9;cx.beginPath();cx.arc(kx,ky,kr*1.55,0,TAU);cx.fill();cx.globalAlpha=1;
    cx.fillStyle='#ffe066';cx.shadowColor='#ffe066';cx.shadowBlur=blur()*2;shapePath(cx,kx,ky,kr,k);cx.fill();cx.shadowBlur=0;
    cx.strokeStyle='#ffe066';cx.lineWidth=4;cx.globalAlpha=0.9;cx.beginPath();cx.arc(kx,ky,kr*(1.6+1.6*ph),0,TAU);cx.stroke();cx.globalAlpha=1;}""")

# the first key of each landing sounds as the landing starts
rep("function updateLanding(dt,sy){ // returns true while the slow-motion landing owns the frame",
    "function updateLanding(dt,sy){ // returns true while the slow-motion landing owns the frame\n  if(run.lm&&!run.lm.keyed&&sy&&sy.rshape){run.lm.keyed=true;playKey(sy);}")

# player-facing text
rep("At each gap, steer onto the white spine as its ring closes. Two good landings fire the next neuron. Too few and it costs a hit.",
    "At each gap, match the shape: steer onto the spine whose receptor matches the messenger in the center before its ring closes. Two good landings fire the next neuron. Too few and it costs a hit.")

# ---- the week's examples rotate: each green (and each pink) shows once, in shuffled order,
# before any repeats, and never the same one twice in a row (founder 19:31)
rep("  if(!poolR.length)poolR=DECK.filter(function(c){return c.t==='r';});if(!poolG.length)poolG=DECK.filter(function(c){return c.t==='g';});",
    "  if(!poolR.length)poolR=DECK.filter(function(c){return c.t==='r';});if(!poolG.length)poolG=DECK.filter(function(c){return c.t==='g';});\n"
    "  var BAGR=[],BAGG=[],LASTR=null,LASTG=null;\n"
    "  function bagDraw(bag,pool,last){if(!bag.length){var sh=pool.slice();for(var q=sh.length-1;q>0;q--){var j=Math.floor(Math.random()*(q+1));var t=sh[q];sh[q]=sh[j];sh[j]=t;}"
    "if(sh.length>1&&sh[sh.length-1]===last){var t2=sh[0];sh[0]=sh[sh.length-1];sh[sh.length-1]=t2;}bag.push.apply(bag,sh);}return bag.pop();}")
rep("for(var k=0;k<n;k++){var card=pool[Math.floor(Math.random()*pool.length)];",
    "for(var k=0;k<n;k++){var card=bad?(LASTR=bagDraw(BAGR,poolR,LASTR)):(LASTG=bagDraw(BAGG,poolG,LASTG));")

# ---- puzzle pacing: a little more time per beat for the search; the first key never sits under the spark
rep("  BEAT=[1.0,0.92,0.85,0.8][run.leg]||0.8;\n  if(!sy.rshape)", "  BEAT=[1.1,1.0,0.95,0.9][run.leg]||0.9;\n  if(!sy.rshape)")
rep("tgt:reachPick(sy.pads,run.theta,false),", "tgt:reachPick(sy.pads,run.theta,true),")

open(P, 'w').write(s)
print('ok', len(s.encode()), hashlib.sha256(s.encode()).hexdigest())
