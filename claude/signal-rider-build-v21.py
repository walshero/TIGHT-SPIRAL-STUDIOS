#!/usr/bin/env python3
"""Signal Rider v0.21: the Playtest Table build.
Founder 2026-11-14 14:00: "1 idk. 2. Y. 3 y. And implement advised changes" on
claude/playtest/SIGNAL-RIDER-v0.20-TABLE-2026-11-14.md.
Ruling 1 (made by the chair since the founder declined to choose): week stress is LOAD, not hits.
  Pink cubes slow you and widen frayed bands but never end the ride; hits come from frayed bands
  and gaps that do not fire. Stress raises risk without being the player's fault (SAMHSA 2014).
Ruling 2: the speedometer shows the science (drops only in frayed bands); greens keep their surge feel.
Ruling 3: a one-tap prediction before ride 2+.
Tier 1: steering sign, grown spines placed off the alarm face + match beats alarm, one load per red
  group, calm road deals plain "hard moment" cubes, stale text, stressed spines drawn above the key.
Tier 2: week effects on leg 4 only, wording fixes, bands knit back after clean stretches.
Tier 3: landing reach two spines + far-against-pull under stress + next-shape preview; sets and rests
  so curves have room; travel time headline with best this visit; chained greens rise and stack;
  name spoken only first time; "Try next" button; inventory trim with sticky Ride; first green earlier;
  practice landing in the warm-up; "Rose to it" for a test right after a green.
Access: dark disc under cube icons, #ff8fc4 verdict labels, spine value split, lightning setting and
  3/s cap, Skip replay in the thumb arc, confirm before leaving mid-ride.
Base: canon v0.20 (303844ec)."""
import hashlib
P = 'lab/down-the-nerve.html'
s = open(P).read()
assert hashlib.sha256(s.encode()).hexdigest().startswith('303844ec'), 'base is not canon v0.20'
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:90]); s = s.replace(a, b)

rep('<title>Signal Rider v0.20</title>', '<title>Signal Rider v0.21</title>')
rep('<span class="chip">v0.20</span>', '<span class="chip">v0.21</span>')

# ================= Tier 1 =================
# 1 steering: hold and keys now turn the same way as drag
rep("run.theta+=steer*2.7*dt;", "run.theta-=steer*2.7*dt; // v0.21: same sign as drag")

# 2 grown spines stay on the thinking face; a match always counts as a match
rep("syns.push({s:L.end,pads:pads,", "syns.push({base:last&&stressed?alarm+Math.PI:null,s:L.end,pads:pads,")
rep("function reachPick(", "function layPads(sy){var n=sy.pads.length,b=sy.base;if(b===null)return;if(n===2){sy.pads=[b-0.7,b+0.95];return;}for(var p=0;p<n;p++)sy.pads[p]=b-1.2+p*2.4/(n-1);}\nfunction reachPick(")
rep("var onAlarm=sy.apads.some(", "var onAlarm=!(full||half)&&sy.apads.some(")

# 3 + ruling 1: one load per red group; pinks are load; Rose to it
rep("""  pickups.forEach(function(p){if(!p.hit&&prev<p.s&&run.s>=p.s&&Math.abs(angDiff(run.theta,p.a))<0.42){p.hit=true;
    if(run.warm){effect(p.good,p.card.cap,p.card.ic);var wl=p.warm;setTimeout(function(){speak(wl,true);},900);}
    else{var rc=run.rec[p.good?'g':'r'];rc[p.card.id]=(rc[p.card.id]||0)+1;if(p.good)effect(true,p.card.cap,p.card.ic);else hit(p.card.cap,p.card.ic);}
    var sy4=syns[3];if(!run.warm&&run.leg===3&&sy4&&!sy4.done&&sy4.stressed){if(p.good&&sy4.pads.length<5){run.rec.grown++;sy4.pads.push(sy4.pads[sy4.pads.length-1]+0.55);sy4.w=Math.min(1,sy4.w+0.15);}
      else if(!p.good&&sy4.pads.length>2){run.rec.lost++;sy4.pads.pop();sy4.w=Math.max(0.3,sy4.w-0.1);}}}});""",
"""  pickups.forEach(function(p){if(!p.hit&&prev<p.s&&run.s>=p.s&&Math.abs(angDiff(run.theta,p.a))<0.42){p.hit=true;
    if(!p.good&&p.grp!==undefined){if(!run.grpHit)run.grpHit={};if(run.grpHit[p.grp])return;run.grpHit[p.grp]=1;} // v0.21: one load per red group
    if(run.warm){effect(p.good,p.card.cap,p.card.ic);var wl=p.warm;setTimeout(function(){speak(wl,true);},900);return;}
    if(!p.good&&p.card.id==='test'&&tAll-(run.lastGoodAt||-9)<2.5){run.rec.rose=(run.rec.rose||0)+1;effect(true,'Rose to it: '+p.card.cap,p.card.ic);return;} // stress reappraisal (Jamieson 2012)
    var rc=run.rec[p.good?'g':'r'];rc[p.card.id]=(rc[p.card.id]||0)+1;if(p.good)effect(true,p.card.cap,p.card.ic);else addLoad(p.card.cap,p.card.ic);
    var sy4=syns[3];if(run.leg===3&&sy4&&!sy4.done&&sy4.stressed){if(p.good&&sy4.pads.length<5){run.rec.grown++;sy4.pads.push(0);layPads(sy4);sy4.w=Math.min(1,sy4.w+0.15);}
      else if(!p.good&&sy4.pads.length>2){run.rec.lost++;sy4.pads.pop();layPads(sy4);sy4.w=Math.max(0.3,sy4.w-0.1);}}}});""")
rep("function hit(title,icon){\n  run.lastHit='band';run.hits++;",
    "function addLoad(title,icon){run.load=(run.load||0)+1;run.lastBadAt=tAll;run.assist=Math.max(0.72,(run.assist||1)-0.06);effect(false,title,icon);drawHits();}\nfunction hit(title,icon){\n  run.lastHit='band';run.lastBadAt=tAll;run.frayT=1.2;run.hits++;")
rep("  h.innerHTML='Hits '+out;h.setAttribute('aria-label','Hits: '+run.hits+' of 3');}",
    "  h.innerHTML='Hits '+out+(run.load?'<span class=\"load\">Load '+run.load+'</span>':'');h.setAttribute('aria-label','Hits: '+run.hits+' of 3'+(run.load?'. Load: '+run.load:''));}")
rep("function restoreCp(){var c=run.cp;", "function restoreCp(){var c=run.cp;run.grpHit={};")

# 4 calm road and support-only weeks: plain hard moments, never named stresses the player did not pick
rep("var CATS=[", 'var MOMENT={"id":"moment","label":"A hard moment","t":"r","cat":"none","w":1,"cap":"A hard moment","ic":"<circle cx=\\"17\\" cy=\\"17\\" r=\\"9\\" fill=\\"none\\" stroke=\\"#eef2f6\\" stroke-width=\\"3\\"/><path d=\\"M17 11 v7\\" stroke=\\"#eef2f6\\" stroke-width=\\"3\\" stroke-linecap=\\"round\\"/><circle cx=\\"17\\" cy=\\"22.5\\" r=\\"1.8\\" fill=\\"#eef2f6\\"/>"};\nvar CATS=[')
rep("if(!poolR.length)poolR=DECK.filter(function(c){return c.t==='r';});", "if(!poolR.length)poolR=[MOMENT];")
rep("DECK.forEach(function(c){c.img=new Image();", "DECK.concat([MOMENT]).forEach(function(c){c.img=new Image();")
rep("var lab=function(id){var d=DECK.filter(", "var lab=function(id){var d=DECK.concat([MOMENT]).filter(")

# 6 stressed face: spines drawn above the key disc so beat 0 never hides them
a = s.index("    sy.pads.forEach(function(pa,i){var p=proj(pa,zf,1.0);cx.fillStyle='#04050a'")
b = s.index("cx.shadowBlur=0;});\n", a) + len("cx.shadowBlur=0;});\n")
spines = s[a:b]; s = s[:a] + s[b:]
rep("    if(fb&&fb.kind==='full'){var cp=proj(", spines + "    if(fb&&fb.kind==='full'){var cp=proj(")

# ================= Tier 2 =================
# 7 ruling 2: the speedometer reads the science: only frayed bands slow a real signal
rep("var vReal=Math.min(120,run.v/(6.5*S.speed*rampF())*75);",
    "run.frayT=Math.max(0,(run.frayT||0)-dt);run.vSci=(run.vSci||75)+((run.frayT>0?12:75)-(run.vSci||75))*Math.min(1,dt*4);var vReal=run.vSci;/* v0.21: damaged insulation is what slows conduction (OpenStax A&P 12.5) */")
# 8 the week reaches the last relay only
rep("toldNode:false,toldFray:false,missCount:0,band:band0,bandT:band0,",
    "toldNode:false,toldFray:false,missCount:0,band:0.7,bandT:0.7,bandBase:0.7,band0w:band0,")
rep("run.leg++;run.s=sy.s+4.01;", "run.leg++;if(run.leg===3){run.bandBase=run.band0w;run.bandT=Math.max(run.bandT,run.band0w);}run.s=sy.s+4.01;")
# 10 frayed bands knit back after four clean seconds (Radley 2005, in game time)
rep("run.band+=(run.bandT-run.band)*Math.min(1,dt*3);",
    "run.band+=(run.bandT-run.band)*Math.min(1,dt*3);if(!run.warm&&tAll-(run.lastBadAt||0)>4&&run.bandT>(run.bandBase||0.7))run.bandT=Math.max(run.bandBase||0.7,run.bandT-0.05*dt);")
# 9 wording
rep("Each sleep block also takes one landing spine from the thinking cortex.",
    "In the game, each sleep block takes one landing spine. (In mice, five hours of lost sleep cut spines in the memory center, the hippocampus; Havekes et al., 2016.)")
rep("A full night of sleep. Landing places relight overnight.", "A full night of sleep. After practice, sleep helps new spines form.")
n_bus = s.count("A surprise you cannot control is the kind of stress that lands hardest; predictable stress is easier to absorb.")
rep("A surprise you cannot control is the kind of stress that lands hardest; predictable stress is easier to absorb.",
    "Stress you cannot control lands harder than stress you can. A sense of control lets the planning center calm the alarm.", n_bus)
n_al = s.count("Across 148 studies, people with stronger social ties had 50% better odds of survival over the study periods.")
rep("Across 148 studies, people with stronger social ties had 50% better odds of survival over the study periods.",
    "In adult mice, weeks of isolation thinned the insulation (myelin) on fibers in the thinking cortex.", n_al)
rep("Holt-Lunstad et al., 2010, PLOS Medicine", "Liu et al., 2012, Nature Neuroscience", s.count("Holt-Lunstad et al., 2010, PLOS Medicine"))
rep("A long stretch of short nights thins the landing spines in the thinking cortex, and the alarm circuits get stronger.",
    "A long run of hard weeks thins the landing spines in the thinking cortex (rats; Radley et al., 2006), and the alarm circuits get stronger.")
rep("Sleep, movement and support help connections relight and new spines grow back (Radley et al., 2005; exercise raises BDNF).",
    "Sleep, movement and support help new spines grow back. In real brains that takes days to weeks once the stress eases (Radley et al., 2005); the game shows it in seconds.")
rep("grow spiky cell bodies, and the other fibers dim.", "grow spiky cell bodies (over weeks of stress, Vyas et al., 2002), and the other fibers dim.")

# 5 stale rule text
rep("After a green, the thinking fibers light up and grow new tips.</div>", "After a green, the thinking fibers light up and grow new tips (in real brains, over days to weeks).</div>")
rep("Frayed bands (striped, loose fibers) slow you down.</div>", "Frayed bands (striped, loose fibers) slow the signal. Hitting one is a hit. Clear stretches let them knit back.</div>")
rep("Bads: frayed bands get wider and you slow. Hit three and the signal fades.</div>",
    "Pink cubes are load from your week: they slow you and widen the frayed bands, but load never ends the ride. Hits come from frayed bands and gaps that do not fire. Three hits and the signal fades.</div>")
rep("Greens: steer into them. Frayed bands get narrower. They do not change your speed.</div>",
    "Greens: steer into them for a speed surge, and the frayed bands get narrower. Greens in a row surge harder.</div>")
rep("At each gap, match the shape: steer onto the spine whose receptor matches the messenger in the center before its ring closes. Two good landings fire the next neuron. Too few and it costs a hit.",
    "At each gap, match the shape: steer onto the spine with the shape in the center before its ring closes. The next shape waits beside it. Two good landings fire the next neuron. Too few and it costs a hit.")
rep("""<li>Red cubes (rough edges) are bads: a short night, a test, a phone at 2 a.m. Every bad that pops up or that you hit makes the frayed bands wider and slows you. Three hits and the signal fades; you go back to the last checkpoint.</li>""",
    """<li>Pink cubes (rough edges) are the load from your week: a short night, a test, rent due. Each one you hit slows you and widens the frayed bands, but load never ends the ride. Hits come from frayed bands and gaps that do not fire. Three hits and the signal fades; you go back to the last checkpoint. With no week loaded, the pink cubes are plain hard moments.</li>""")
rep("""<li>Green cubes (rounded) are goods: sleep, a walk, a friend, a meal, practice. Steer into a green and the frayed bands get narrower. Nothing in the ride speeds you up; the bright rings show the signal leaping, at a steady speed.</li>""",
    """<li>Green cubes (rounded) are supports: sleep, a walk, a friend, practice. Steer into a green for a speed surge and narrower frayed bands; greens in a row surge harder. The speedometer shows the real signal: it drops only in frayed bands, because damaged insulation is what slows a nerve signal.</li>""")
rep("<li>The end of each fiber: a gap, then the next neuron's landing spines. Line up with a lit spine to land.</li>",
    "<li>The end of each fiber: a gap, then the next neuron's landing spines. Each beat a shape appears in the center, with the next one waiting beside it. Steer onto the spine with that shape before its ring closes.</li>")
rep("<li>Before each ride you load a week onto the balance. Every card in the deck: short night, test tomorrow, phone at 2 a.m., missed bus, loud room (stress); real sleep, a walk, a friend, a good meal, practice (support). Each card you load shows up as a picture during the ride. Choose the calm road to ride with no week.</li>",
    "<li>Before each ride you load a week onto the balance. Each block you load shows up as a picture on the cubes during the ride. Choose the calm road to ride with no week.</li>")
rep("The first three relays carry the touch the same either way, because stress does not stop you feeling a touch.</li>",
    "Frayed bands start wider or narrower only on that last leg. The first three relays carry the touch the same either way, because stress does not stop you feeling a touch.</li>")
rep("Three hits. What's happening here: damaged insulation can stop a signal. Each hard thing widened the frayed bands until there was almost no clear path left. Greens narrow them again.",
    "Three hits. Hits come from frayed bands and gaps that do not fire. What's happening here: damaged insulation can stop a signal, and the load from your week widened the bands until there was almost no clear path. Greens and clear stretches narrow them again.")
rep("'<div>Frayed bands: <b>'", "'<div>Last-leg frayed bands: <b>'")
rep("out.push('Frayed bands started '+band+'.'", "out.push('On the last leg, frayed bands started '+band+'.'")
rep("Frayed bands start wider.", "Frayed bands on the last leg start wider.")
rep("Frayed bands start narrower.", "Frayed bands on the last leg start narrower.")
rep("ride.push(r?'Pink blocks hit you '+r+' time'+(r>1?'s':'')+': '+tally(rec.r)+'.':'You dodged every pink block.');",
    "ride.push(r?'Pink blocks added load '+r+' time'+(r>1?'s':'')+': '+tally(rec.r)+'.':'You dodged every pink block.');if(rec.rose)ride.push('You rose to a test '+rec.rose+' time'+(rec.rose>1?'s':'')+' right after a green: positive stress.');")

# ================= Tier 3 =================
# 11 landing: reach two spines, stressed target far from the pull, show the next shape
rep("function reachPick(pads,from,skip){var reach=2.7*BEAT*0.6,", "function reachPick(pads,from,skip){var reach=2.7*BEAT*0.92,")
rep("function nextTarget(sy){if(sy.pads.length<2)return sy.pads[0];return reachPick(sy.pads,run.theta,true);",
    "function nextTarget(sy,from){from=from===undefined?run.theta:from;if(sy.pads.length<2)return sy.pads[0];\n  if(sy.stressed&&Math.random()<0.6){var far=sy.pads.filter(function(p){return Math.abs(angDiff(p,from))>0.05;}).sort(function(a,b){return Math.abs(angDiff(b,run.alarm))-Math.abs(angDiff(a,run.alarm));})[0];if(far!==undefined)return far;}\n  return reachPick(sy.pads,from,true);")
rep("  RING={fill:sy.last?Math.min(1,sy.fill/sy.need):0,t:0,col:'#ff4fa3',hold:true};sfxSlowIn();",
    "  RING={fill:sy.last?Math.min(1,sy.fill/sy.need):0,t:0,col:'#ff4fa3',hold:true};sfxSlowIn();run.lm.nxt=nextTarget(sy,run.lm.tgt);")
rep("  lm.tgt=nextTarget(sy);playKey(sy);lm.keyT=lm.t;",
    "  lm.tgt=lm.nxt!==undefined?lm.nxt:nextTarget(sy);lm.nxt=nextTarget(sy,lm.tgt);playKey(sy);lm.keyT=lm.t;")
rep("    // progress toward firing: a green arc that fills with each landing",
    "    if(lm.nxt!==undefined){var nk=keyOf(sy,lm.nxt),nr=kr*0.42,nx=cxv-nr*1.4,ny=Math.max(104,ky-kr*5.2);cx.fillStyle='#04050a';cx.globalAlpha=0.9;cx.beginPath();cx.arc(nx,ny,nr*1.7,0,TAU);cx.fill();cx.globalAlpha=0.8;cx.fillStyle='#ffe066';shapePath(cx,nx,ny,nr,nk);cx.fill();cx.globalAlpha=1;\n      cx.font='700 '+Math.max(15,Math.round(nr*0.95))+'px \"Avenir Next\",\"Segoe UI\",system-ui,sans-serif';cx.textAlign='center';cx.textBaseline='middle';cx.fillStyle='#eef2f6';cx.textAlign='left';cx.fillText('next',nx+nr*2.1,ny);cx.textAlign='center';}\n    // progress toward firing: a green arc that fills with each landing")
# 12 sets and rests: blocks come in two sets per leg; the rests carry the curves
rep("ps=clearSpan(s+26+(L.len-48)*(gi+0.5)/4,span)", "ps=clearSpan(s+26+(L.len-48)*[0.06,0.2,0.58,0.72][gi],span)")
rep("for(var fs=s+(i===0?34:22);fs<L.end-16;fs+=rnd(26,34)-i*1.5)feats.push({s:fs,len:2.6,a:rnd(0,TAU),wm:rnd(0.85,1.15),hit:false,warned:false});",
    "for(var fs=s+(i===0?34:22);fs<L.end-16;fs+=rnd(21,28)-i*1.5){var frr=(fs-(s+26))/(L.len-48);if((frr>0.3&&frr<0.5)||frr>0.84)continue;feats.push({s:fs,len:2.6,a:rnd(0,TAU),wm:rnd(0.85,1.15),hit:false,warned:false});} // v0.21 rests (Smith et al. 2009)")
# 17 first cluster on the first leg is always a green
rep("var bad=gi===0?pR>=0.5:gi===1?pR<0.5:Math.random()<pR;", "var bad=i===0&&gi===0?false:i===0&&gi===1?true:gi===0?pR>=0.5:gi===1?pR<0.5:Math.random()<pR;")
# 14 chained greens: rising pitch, stacking surge; name spoken the first time only
rep("function sfxGood(){[523.25,659.25,783.99,1046.5].forEach(function(fq,i){synth(fq,", "function sfxGood(ch){var mul=Math.pow(2,Math.min(ch||0,6)*2/12);[523.25,659.25,783.99,1046.5].forEach(function(fq,i){synth(fq*mul,")
rep("run.floatTxt='+ clear path';sfxGood();musGood();run.surgeT=2.0;run.v*=1.15;",
    "var ch=(tAll-(run.lastGoodAt||-9)<3.5)?(run.chain||0)+1:0;run.chain=ch;run.lastGoodAt=tAll;run.floatTxt=ch?'chain x'+(ch+1):'+ clear path';sfxGood(ch);musGood();run.surgeT=2.0;run.surgeMul=Math.min(1.7,SURGE+0.1*ch);run.v*=1.15;")
rep("run.floatTxt='- speed';sfxBad();", "run.lastBadAt=tAll;run.floatTxt='- speed';sfxBad();")
rep("  callout(spoken(title));logEvent(good,title);", "  if(!run.said)run.said={};if(!run.said[title]){run.said[title]=1;callout(spoken(title));}logEvent(good,title);")
rep("var tgtv=cruise*(run.surgeT>0?SURGE:1);", "var tgtv=cruise*(run.surgeT>0?(run.surgeMul||SURGE):1);")
# 13 travel time headline, best this visit
rep("function finish(){", "var BEST=null,LASTPADS=null,TIPCAT=null;\nfunction finish(){")
rep("  document.getElementById('endStats').textContent='Your touch traveled about '+run.realM.toFixed(2)+' meters through four neurons in about '+run.realMs.toFixed(1)+' milliseconds, with '+run.hits+' of 3 hits.';",
    "  var ms=run.realMs,pb=BEST;BEST=pb===null?ms:Math.min(pb,ms);\n  document.getElementById('endStats').innerHTML='<span class=\"big\">'+ms.toFixed(1)+' ms</span>Fingertip to thinking cortex, about '+run.realM.toFixed(2)+' meters through four neurons. '+(pb===null?'Your first time this visit.':ms<pb-0.05?'New best this visit (was '+pb.toFixed(1)+' ms).':'Best this visit: '+pb.toFixed(1)+' ms.')+' Frayed bands are what slow it. '+run.hits+' of 3 hits.';")
# 15 Try next as one button
rep("var nm=function(id){var c=CATS.filter(function(x){return x.id===id;})[0];return c?c.name:id;};\n  var lab=",
    "TIPCAT=null;var nm=function(id){var c=CATS.filter(function(x){return x.id===id;})[0];return c?c.name:id;};\n  var lab=")
rep("tip='Try next: add a block from '+c.name+'. '", "TIPCAT=c.id;tip='Try next: add a block from '+c.name+'. '")
rep("function openSheet(id){if(id==='sEnd'||id==='sFade'){var wr=document.getElementById(id==='sEnd'?'endWeek':'fadeWeek');if(wr)wr.innerHTML=weekReplay();}",
    "function openSheet(id){if(id==='sEnd'||id==='sFade'){var wr=document.getElementById(id==='sEnd'?'endWeek':'fadeWeek');if(wr){wr.innerHTML=weekReplay();if(TIPCAT&&run.week){var tc=TIPCAT,tb=document.createElement('button');tb.className='btn primary';tb.type='button';tb.textContent='Add '+catOf(tc).name+' and ride';tb.onclick=function(){var it=DECK.filter(function(d){return d.cat===tc&&!week[d.id];})[0];if(it)week[it.id]=true;closeSheets();initAudio();buildRun(week);};wr.appendChild(tb);}}}")
# 16 inventory: short intro, research behind Why?, Ride always in reach
rep("<p class=\"sub\">Use a week like yours, or any week. Nothing is saved. Open a category, read what the research says, and add blocks. On the ride, steer into greens and around reds and frayed bands. The panel below shows what this week will change.</p>",
    "<p class=\"sub\">A week like yours, or any week. Nothing is saved.</p>")
rep("h.innerHTML='<h3>'+g[1]+'</h3><p>'+g[2]+' <span class=\"src\">('+g[3]+')</span></p>';",
    "h.innerHTML='<h3>'+g[1]+'</h3><details class=\"why\"><summary>Why?</summary><p>'+g[2]+' <span class=\"src\">('+g[3]+')</span></p></details>';")
# 18 handled with the pickups above (Rose to it)
# warm-up practice landing (one easy gap, no fail state)
rep("function buildWarmup(){buildRun(null);run.warm=true;feats=[];checkpoints=[];run.pics=[];",
    "function buildWarmup(){buildRun(null);run.warm=true;feats=[];checkpoints=[];run.pics=[];\n  run.warmSyn={base:null,s:62,pads:[0,1,2,3,4].map(function(q){return Math.PI/2+q*TAU/5;}),tol:0.42,done:false,gap:4,last:false,stressed:false,apads:[],w:1,need:3,fill:0,afill:0,tries:0,practice:true};")
rep("  run.warmEnd=70;}", "  run.warmEnd=76;}")
rep("var syL=syns[run.leg];if(syL&&!syL.done&&!run.warm&&updateLanding(dt,syL))", "var syL=run.warm?run.warmSyn:syns[run.leg];if(syL&&!syL.done&&(!run.warm||syL.practice)&&updateLanding(dt,syL))")
rep("  var sy=syns[run.leg];\n  if(sy){var zf=", "  var sy=run.warm?run.warmSyn:syns[run.leg];\n  if(sy){var zf=")
rep("var beats=sy.last?(sy.stressed?6:4):3;", "var beats=sy.practice?2:sy.last?(sy.stressed?6:4):3;")
rep("max:sy.last?(sy.stressed?8:6):5", "max:sy.practice?3:sy.last?(sy.stressed?8:6):5")
rep("var done=sy.last?sy.fill>=sy.need:lm.hits>=2;", "var done=sy.last?sy.fill>=sy.need:lm.hits>=(sy.practice?1:2);")
rep("  run.rec.stalls++;endLanding();RING=null;sy.done=false;sfxFizzle();",
    "  if(sy.practice){endLanding();RING=null;sy.done=true;speak('Close. At each gap, steer onto the matching shape.',false);return;}\n  run.rec.stalls++;endLanding();RING=null;sy.done=false;sfxFizzle();")
rep("  endLanding();sy.done=true;run.flash=1;sfxFire();callout(clean?'Fired':'Fired, late');",
    "  endLanding();sy.done=true;run.flash=1;sfxFire();callout(clean?'Fired':'Fired, late');\n  if(sy.practice){run.s=sy.s+4.01;setTimeout(function(){speak('That gap is a synapse. Match the shape to cross it.',true);},700);return;}")

# ruling 3: predict before ride 2+
rep('  <div id="fxp" aria-live="polite"></div>',
    '  <div id="pred" style="display:none"><p class="sub"><b>Predict first.</b> Last ride the thinking cortex had <span id="predLast"></span> landing spines. With this week, more, the same, or fewer?</p><div class="row"><button class="btn" type="button" data-p="more">More</button><button class="btn" type="button" data-p="same">Same</button><button class="btn" type="button" data-p="fewer">Fewer</button></div></div><p class="sub" id="predRes" aria-live="polite"></p>\n  <div id="fxp" aria-live="polite"></div>')
rep("function openTray(){trayOpen=true;",
    "function predHide(on){['fxp','trayReadout','preview'].forEach(function(id){var e=document.getElementById(id);if(e)e.style.visibility=on?'hidden':'';});}\n"
    "document.getElementById('pred').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;var m=weekModel(week),act=m.pads>LASTPADS?'more':m.pads<LASTPADS?'fewer':'same',ok=b.dataset.p===act;\n"
    "  document.getElementById('predRes').textContent=(ok?'Right: ':'Not quite: ')+m.pads+' spines this week, '+LASTPADS+' last ride.'+(ok?'':' The panel shows why.');document.getElementById('pred').style.display='none';predHide(false);});\n"
    "function openTray(){if(run&&run.model&&!run.warm&&run.s>5)LASTPADS=run.model.pads;document.getElementById('predRes').textContent='';if(LASTPADS!==null){document.getElementById('predLast').textContent=LASTPADS;document.getElementById('pred').style.display='block';predHide(true);}else{document.getElementById('pred').style.display='none';predHide(false);}\n  trayOpen=true;")

# ================= Access =================
rep("if(p.card&&p.card.img.complete)cx.drawImage(p.card.img,-sz*0.42,-sz*0.42,sz*0.84,sz*0.84);",
    "if(p.card&&p.card.img.complete){cx.fillStyle='#04050a';cx.beginPath();cx.arc(0,0,sz*0.42,0,TAU);cx.fill();cx.drawImage(p.card.img,-sz*0.36,-sz*0.36,sz*0.72,sz*0.72);} // v0.21 icon on a dark disc")
rep("var FBC={full:'#7cfc9a',half:'#ffd166',wrong:'#ff4fa3',miss:'#ff4fa3'};", "var FBC={full:'#7cfc9a',half:'#ffd166',wrong:'#ff8fc4',miss:'#ff8fc4'};")
rep("cx.fillStyle=lined&&!run.lm?'#ffffff':'#ff4fa3';", "cx.fillStyle=lined&&!run.lm?'#ffffff':'#ff9ed2';")
rep("var R2=Math.max(5,0.22*f/zf);cx.fillStyle='#ff4f7a';", "var R2=Math.max(5,0.22*f/zf);cx.fillStyle='#d1003f';")
rep("cx.lineTo(p[0]+Math.cos(aa)*rr,p[1]+Math.sin(aa)*rr);}cx.closePath();cx.fill();});",
    "cx.lineTo(p[0]+Math.cos(aa)*rr,p[1]+Math.sin(aa)*rr);}cx.closePath();cx.fill();cx.strokeStyle='#ffb3c7';cx.lineWidth=2;cx.stroke();});")
rep("var S={speed:1,glow:1,roll:reduce?0:1,outside:1,sound:1,music:1,curves:reduce?0.4:1};", "var S={speed:1,glow:1,roll:reduce?0:1,outside:1,sound:1,music:1,curves:reduce?0.4:1,light:reduce?0:1};")
rep("function save(){try{localStorage.setItem('dtn.comfort',JSON.stringify(S));}catch(e){}}",
    "function save(){try{localStorage.setItem('dtn.comfort',JSON.stringify(S));}catch(e){}}\nif(S.light===undefined)S.light=reduce?0:1;")
rep("function spawnBolt(col){var mn=", "var BOLTT=[];function spawnBolt(col){if(!S.light)return;var nowB=performance.now();BOLTT=BOLTT.filter(function(t){return nowB-t<1000;});if(BOLTT.length>=3)return;BOLTT.push(nowB);var mn=")
rep('  <h3>Curves</h3>', '  <h3>Lightning</h3><div class="seg" data-k="light"><button class="btn" data-v="1">On</button><button class="btn" data-v="0">Off</button></div>\n  <h3>Curves</h3>')
rep('<a class="btn" href="https://walshero.github.io/TIGHT-SPIRAL-STUDIOS/lab/" aria-label="Studio home">Studio</a>',
    '<a class="btn" id="bStudio" href="https://walshero.github.io/TIGHT-SPIRAL-STUDIOS/lab/" aria-label="Studio home">Studio</a>')
rep('<div class="sheet" id="sFade"',
    '<div class="sheet" id="sLeave" role="dialog" aria-modal="true" aria-labelledby="hLv"><div class="card">\n  <h2 id="hLv">Leave the ride?</h2><p>Your week is not saved.</p>\n  <div class="row"><button class="btn primary" data-close>Stay on the ride</button><a class="btn" href="https://walshero.github.io/TIGHT-SPIRAL-STUDIOS/lab/">Leave for the studio</a></div>\n</div></div>\n<div class="sheet" id="sFade"')
rep("document.getElementById('bLib').onclick=function(){openSheet('sLib');};",
    "document.getElementById('bLib').onclick=function(){openSheet('sLib');};\ndocument.getElementById('bStudio').addEventListener('click',function(e){if(run&&!run.over&&!run.faded&&run.s>2&&!trayOpen){e.preventDefault();openSheet('sLeave');}});")
rep("#replay p{font-size:22px;", "#bSkipReplay{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(18px + env(safe-area-inset-bottom));min-height:52px;z-index:6}\n#hits .load{margin-left:10px;font-weight:800;color:#ffd1ec}\n#endStats .big{display:block;font-size:44px;font-weight:800;line-height:1.1;color:#eef2f6;margin-bottom:4px}\n#rideRow{position:sticky;bottom:calc(-14px - env(safe-area-inset-bottom));background:rgba(13,18,32,.98);padding:10px 0;z-index:3}\n.why summary{min-height:44px;display:flex;align-items:center;font-weight:700;cursor:pointer}\n#replay p{font-size:22px;")

# Senses E2/E3: a mute control in view at all times (WCAG 1.4.2)
rep('  <button class="btn" id="bMenu" type="button" aria-haspopup="dialog">Menu</button>',
    '  <button class="btn" id="bMute" type="button" aria-label="Sound on. Tap to mute." style="min-width:48px;padding:0 10px"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M3 9h4l5-4v14l-5-4H3z" fill="#eef2f6"/><path id="muteWave" d="M15 8c2 2 2 6 0 8M18 5c4 4 4 10 0 14" stroke="#eef2f6" stroke-width="2" fill="none"/><path id="muteX" d="M15 9l6 6M21 9l-6 6" stroke="#eef2f6" stroke-width="2.4" style="display:none"/></svg></button>\n  <button class="btn" id="bMenu" type="button" aria-haspopup="dialog">Menu</button>')
rep("document.getElementById('bLib').onclick=function(){openSheet('sLib');};",
    "document.getElementById('bLib').onclick=function(){openSheet('sLib');};\nfunction syncMute(){var b=document.getElementById('bMute');b.setAttribute('aria-label',S.sound?'Sound on. Tap to mute.':'Sound off. Tap to turn sound on.');b.setAttribute('aria-pressed',String(!S.sound));document.getElementById('muteWave').style.display=S.sound?'':'none';document.getElementById('muteX').style.display=S.sound?'none':'';}\nsyncMute();document.getElementById('bMute').onclick=function(){S.sound=S.sound?0:1;save();if(master)master.gain.value=S.sound?0.9:0;if(!S.sound&&window.speechSynthesis){try{speechSynthesis.cancel();}catch(e){}}syncMute();};")
rep("if(k==='sound'&&master)master.gain.value=S.sound?0.9:0;", "if(k==='sound')syncMute();if(k==='sound'&&master)master.gain.value=S.sound?0.9:0;")

open(P, 'w').write(s)
print('v0.21 written', hashlib.sha256(s.encode()).hexdigest()[:8], len(s))
