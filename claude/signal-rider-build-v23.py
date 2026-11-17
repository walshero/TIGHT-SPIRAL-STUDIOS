#!/usr/bin/env python3
"""Signal Rider v0.23: teaching through the mechanic (plan claude/SIGNAL-RIDER-TEACHING-PLAN-2026-11-16.md, option 5).
Founder 2026-11-16 21:07: "5." (the advanced set: fill the next neuron, bare stretch, ghost spark).
1. Bare stretch (Horvath #5): the first ride of a visit opens on 18 units of fiber with no insulation.
   No node rings, grey membrane rings, the spark creeps at 0.4x and the readout reads 1 m/s. Then the
   myelin begins: cyan rings, nodes, full speed. The words come after the feeling (Schwartz & Bransford
   1998). The crawl is a demonstration and does not count toward travel time.
2. Fill the next neuron (Horvath #1): the landing ring leaks. A beat with no match drains it (relays
   -0.5, the thinking cortex -0.4). The alarm's charge never leaks, so under stress the thinking side
   loses charge while the alarm holds it (summation; Arnsten 2009). The relay ring shows live progress.
3. Ghost spark (Osterweil #6): after a ride, the next ride shows a pale ring where your last spark was,
   so two weeks can be compared side by side, ungraded.
Base: canon v0.22 (c06b279f)."""
import hashlib
P = 'lab/down-the-nerve.html'
s = open(P).read()
assert hashlib.sha256(s.encode()).hexdigest().startswith('c06b279f'), 'base is not canon v0.22'
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:90]); s = s.replace(a, b)

rep('<title>Signal Rider v0.22</title>', '<title>Signal Rider v0.23</title>')
rep('<span class="chip">v0.22</span>', '<span class="chip">v0.23</span>')

# ---- shared: a caption helper on the passed line (placed clear of the spark)
rep("var passedT=0;", "var passedT=0;\nfunction caption(html,secs){var el=document.getElementById('passed');el.innerHTML=html;el.style.display='block';passedT=secs||3;}\nfunction inBare(u){return !!(run&&run.bare&&u>=run.bare[0]&&u<run.bare[1]);}\nvar BAREDONE=false,GHOST=null;")

# ---- 1. bare stretch
rep("    for(var n=s+6;n<L.end-10;n+=7)nodes.push({s:n,hit:false});",
    "    for(var n=s+6;n<L.end-10;n+=7)if(!(i===0&&BARE0&&n<19))nodes.push({s:n,hit:false});")
rep("var tgtv=cruise*(run.surgeT>0?(run.surgeMul||SURGE):1);",
    "var tgtv=cruise*(run.surgeT>0?(run.surgeMul||SURGE):1);if(inBare(run.s))tgtv*=0.4;\n"
    "  if(run.bare&&!run.bareSaid&&run.s>=run.bare[0]){run.bareSaid=1;caption('<b>No insulation</b>: the signal creeps, about 1 meter per second.',5);speak('No insulation. The signal creeps, about one meter per second.',true);}\n"
    "  if(run.bare&&!run.bareDone&&run.s>=run.bare[1]){run.bareDone=1;BAREDONE=true;run.flash=0.8;run.flashCol='#3fd6ff';sfxGood(2);caption('<b class=\"g\">Myelin</b> wraps the fiber. Now the signal leaps node to node: 75 meters per second.',5);speak('Myelin wraps the fiber. Now the signal leaps from node to node.',true);}")
rep("run.vSci=(run.vSci||75)+((run.frayT>0?12:75)-(run.vSci||75))*Math.min(1,dt*4);",
    "run.vSci=(run.vSci||75)+((inBare(run.s)?1:run.frayT>0?12:75)-(run.vSci||75))*Math.min(1,dt*(inBare(run.s)?6:4));")
rep("if(vReal>0.5)run.realMs+=dm/vReal*1000;", "if(vReal>0.5&&!inBare(run.s))run.realMs+=dm/vReal*1000;")
rep("    cx.strokeStyle='#3fd6ff';cx.shadowColor='#3fd6ff';cx.shadowBlur=blur()*0.6;cx.lineWidth=Math.max(0.6,2.2*lw()/zz*1.2);cx.globalAlpha=0.18+0.45*fog;",
    "    var bare=inBare(u2);cx.strokeStyle=bare?'#8f9bb0':'#3fd6ff';cx.shadowColor=bare?'#000000':'#3fd6ff';cx.shadowBlur=bare?0:blur()*0.6;cx.lineWidth=Math.max(0.6,(bare?1.4:2.2)*lw()/zz*1.2);cx.globalAlpha=(bare?0.12:0.18)+(bare?0.3:0.45)*fog;")

# ---- 3. ghost spark: record, carry to the next ride, draw
rep("function nameMissed(){", "function ghostRec(){if(run.warm||run.lm)return;if(!run.gh)run.gh=[];run.gh[Math.floor(run.s*2)]=run.theta;}\nfunction nameMissed(){")
rep("  if(!run.warm)nameMissed();", "  if(!run.warm){nameMissed();ghostRec();}")
rep("function openTray(){if(run&&run.model&&!run.warm&&run.s>5)LASTPADS=run.model.pads;",
    "function openTray(){if(run&&run.model&&!run.warm&&run.s>5){LASTPADS=run.model.pads;if(run.gh&&run.s>40)GHOST=run.gh;}")
rep("  var SR=sparkRad();var pp=proj(run.theta,ZP,SR);window.__ball=pp;placeMsgs(pp);",
    "  var SR=sparkRad();var pp=proj(run.theta,ZP,SR);window.__ball=pp;placeMsgs(pp);\n"
    "  if(run.ghost&&!run.warm&&!run.lm){var gt=run.ghost[Math.floor(run.s*2)];if(gt!==undefined){var gp=proj(gt,ZP,SR);cx.globalAlpha=0.75;cx.strokeStyle='#eef2f6';cx.lineWidth=3;cx.setLineDash([6,4]);cx.beginPath();cx.arc(gp[0],gp[1],14,0,TAU);cx.stroke();cx.setLineDash([]);cx.globalAlpha=1;}}")

# buildRun hooks: bare on the first ride of a visit; ghost from the last ride
a = s.index("  nodes=[];feats=[];syns=[];pickups=[];checkpoints=[];var s=0;")
rep("  nodes=[];feats=[];syns=[];pickups=[];checkpoints=[];var s=0;",
    "  nodes=[];feats=[];syns=[];pickups=[];checkpoints=[];var s=0;var BARE0=(w!==undefined&&!BAREDONE),GH0=w!==undefined?GHOST:null;")
rep("toldNode:false,toldFray:false,missCount:0,", "toldNode:false,toldFray:false,missCount:0,bare:BARE0?[4,17]:null,ghost:GH0,")

rep("function buildWarmup(){buildRun(null);run.warm=true;", "function buildWarmup(){buildRun(null);run.warm=true;run.bare=null;run.ghost=null;")
# ---- 2. leaky ring
rep("  if(onAlarm&&sy.stressed){sy.afill++;sfxBeat(-1);",
    "  if(onAlarm&&sy.stressed){sy.afill++;sy.fill=Math.max(0,sy.fill-0.4);sfxBeat(-1);")
rep("  else sfxBeat(0);\n  var done=sy.last?",
    "  else{sfxBeat(0);if(!sy.practice){if(sy.last)sy.fill=Math.max(0,sy.fill-0.4);else lm.hits=Math.max(0,lm.hits-0.5);if(AC&&S.sound)tone(300,0.3,'sine',0.04,150);}} // v0.23: charge leaks between inputs\n  var done=sy.last?")
rep("if(RING)RING.fill=sy.last?Math.min(1,sy.fill/sy.need):(done?1:0);",
    "if(RING)RING.fill=sy.last?Math.min(1,sy.fill/sy.need):sy.practice?(done?1:0):Math.min(1,lm.hits/3);")

# ---- words that name what was felt (Library)
rep("<li>Yellow double rings: checkpoints, halfway through each leg and at each relay.</li>",
    "<li>Yellow double rings: checkpoints, halfway through each leg and at each relay.</li>\n"
    "  <li>The first ride opens on a bare stretch: no insulation, so the signal creeps at about 1 meter per second. Then myelin wraps the fiber and the signal leaps node to node. Real touch fibers are wrapped from the start; unwrapped fibers, like some slow pain fibers, really do run near 1 meter per second.</li>\n"
    "  <li>The ring at each gap is the next neuron's charge. Each match adds to it; a beat with no match lets it leak. Only a full ring fires the next neuron. Under a hard week the thinking cortex leaks while the alarm keeps its charge.</li>\n"
    "  <li>A dashed ring riding beside you is your last ride's spark. Change the week and compare.</li>")

open(P, 'w').write(s)
print('v0.23 written', hashlib.sha256(s.encode()).hexdigest()[:8], len(s))
