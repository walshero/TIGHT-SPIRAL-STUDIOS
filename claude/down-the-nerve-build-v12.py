#!/usr/bin/env python3
"""Down the Nerve v0.12: the leap can fail, and it's a little harder.
Founder 2026-11-08: "there is no fail state on the jumps and there should be. It should be slightly harder."
Base: canon v0.11 (sha256 3483932c...). Science: a neuron fires only if enough input arrives
together to reach threshold; below threshold, no action potential (OpenStax A&P 12.5)."""
import hashlib, sys
SRC = '/home/claude/art/dtn-v0.11.html'
OUT = '/home/claude/tight-spiral-studios/lab/down-the-nerve.html'
s = open(SRC).read()
assert hashlib.sha256(s.encode()).hexdigest().startswith('3483932c'), 'base is not canon v0.11'

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:80])
    s = s.replace(a, b)

# version on the surface
rep('<title>Down the Nerve v0.11</title>', '<title>Down the Nerve v0.12</title>')
rep('<span class="chip">v0.11</span>', '<span class="chip">v0.12</span>')

# beat quickens each leg; fewer beats before the window closes
rep("""  var beats=sy.last?(sy.stressed?6:4):3;
  run.lm={t:0,k:0,beats:beats,max:sy.last?9:6,""",
"""  BEAT=[1.0,0.92,0.85,0.8][run.leg]||0.8;
  var beats=sy.last?(sy.stressed?6:4):3;
  run.lm={t:0,k:0,beats:beats,max:sy.last?(sy.stressed?8:6):5,""")

# targets jump, but only as far as the game's steering (2.7 rad/s) can reach in 60% of a beat: hard, never unfair
rep("""function nextTarget(sy){var pads=sy.pads;if(pads.length<2)return pads[0];var cur=run.lm.tgt,best=null,bd=9;""",
"""function reachPick(pads,from,skip){var reach=2.7*BEAT*0.6,ok=pads.filter(function(p){var d=Math.abs(angDiff(p,from));return d<=reach&&!(skip&&d<0.05);});
  if(!ok.length){var near=pads.slice().sort(function(a,b){return Math.abs(angDiff(a,from))-Math.abs(angDiff(b,from));});if(skip){var far=near[1];if(far!==undefined&&run.lm&&run.lm.k%3===0&&Math.abs(angDiff(far,from))<=2.7*BEAT)return far;} return near[0];} // nothing in easy reach: hold, and every third beat jump if a full beat can cover it
  if(Math.random()<0.6){ok.sort(function(a,b){return Math.abs(angDiff(b,from))-Math.abs(angDiff(a,from));});return ok[0];}
  return ok[Math.floor(Math.random()*ok.length)];}
function nextTarget(sy){if(sy.pads.length<2)return sy.pads[0];return reachPick(sy.pads,run.theta,true);
  var pads=sy.pads,cur=run.lm.tgt,best=null,bd=9;""")
rep("tgt:sy.pads[Math.floor(Math.random()*sy.pads.length)],", "tgt:reachPick(sy.pads,run.theta,false),")

# tighter windows; a half landing counts half toward a relay too
rep("var full=d<0.3,half=!full&&d<0.6;", "var full=d<0.25,half=!full&&d<0.5;")
rep("sy.fill+=add;lm.hits++;", "sy.fill+=add;lm.hits+=full?1:0.5;")

# window closes without enough landed: the next neuron stays quiet
rep("if(done||lm.k>=lm.max){fireRelay(sy,done);return;}",
    "if(done){fireRelay(sy,true);return;}\n  if(lm.k>=lm.max){missLanding(sy);return;}")

rep("function endLanding(){",
"""function missLanding(sy){ // below threshold: no action potential. Costs a hit; a fresh spark tries again.
  endLanding();RING=null;sy.done=false;sfxFizzle();
  if(sy.last)sy.fill*=0.5;else sy.fill=0; // some of what landed lingers (summation fades)
  run.s=sy.s-7;run.v=Math.min(run.v,3*S.speed);run.lastHit='miss';
  run.hits++;drawHits();run.flash=0.6;run.flashCol='#ff4fa3';
  var e=document.getElementById('effect');e.className='ui bad';e.textContent='Did not fire';e.style.display='block';effectT=2.2;logEvent(false,'Did not fire');
  speak('Not enough crossed. The next neuron stayed quiet.',false);
  lesson('A neuron fires only when enough messengers land at once. Too few, and the signal stops at the gap.');
  if(run.hits===2){setTimeout(function(){if(AC&&S.sound){tone(880,0.12,'square',0.06);setTimeout(function(){tone(660,0.16,'square',0.06);},150);}speak('One hit left',false);},1600);}
  if(run.hits>=3){run.faded=true;setTimeout(function(){speak('The signal faded.',false);openSheet('sFade');},900);}
}
function endLanding(){""")

# the fade card says what actually ended the run
rep("function hit(title,icon){\n  run.hits++;", "function hit(title,icon){\n  run.lastHit='band';run.hits++;")
rep('<p>Three hits. What\'s happening here: damaged insulation can stop a signal.',
    '<p id="fadeWhy">Three hits. What\'s happening here: damaged insulation can stop a signal.')
rep("run.faded=true;setTimeout(function(){speak('The signal faded.',false);openSheet('sFade');},500);}",
    "run.faded=true;setTimeout(function(){speak('The signal faded.',false);openSheet('sFade');},500);}\n  fadeText();")
rep("function drawHits(){",
"""var FADE_BAND=null;
function fadeText(){var p=document.getElementById('fadeWhy');if(!p)return;if(FADE_BAND===null)FADE_BAND=p.textContent;
  p.textContent=run.lastHit==='miss'?"Three hits. The last one was at a gap: too few messengers landed, so the next neuron stayed quiet. A neuron fires only when enough signal arrives at once. Greens give you more landing spines.":FADE_BAND;}
function drawHits(){""")
rep("if(run.hits>=3){run.faded=true;setTimeout(function(){speak('The signal faded.',false);openSheet('sFade');},900);}\n}",
    "if(run.hits>=3){run.faded=true;fadeText();setTimeout(function(){speak('The signal faded.',false);openSheet('sFade');},900);}\n}")

# legend: say how the leap is won and lost
rep('Yellow double rings are checkpoints.</div>',
    'Yellow double rings are checkpoints.</div>\n    <div><svg viewBox="0 0 30 30" aria-hidden="true"><circle cx="15" cy="15" r="5" fill="#ffffff"/><circle cx="15" cy="15" r="11" fill="none" stroke="#ffffff" stroke-width="2.5"/></svg>At each gap, steer onto the white spine as its ring closes. Two good landings fire the next neuron. Too few and it costs a hit.</div>')


# a hard week still counts for less, but stays winnable inside one window with clean play
rep("w:last&&stressed?Math.max(0.35,np/5):1","w:last&&stressed?Math.max(0.5,np/5):1")

# Studio Eyes floor: HUD text over the moving backdrop gets a solid backing; the fulcrum reads at 3:1+
rep(".chip{font-size:18px;border:1px solid var(--rule);", ".chip{font-size:18px;border:1px solid var(--rule);background:var(--bg);")
rep("#hits{display:flex;gap:6px;align-items:center;font-size:18px;font-weight:700}", "#hits{display:flex;gap:6px;align-items:center;font-size:18px;font-weight:700;background:var(--bg);border-radius:10px;padding:2px 8px;width:max-content}")
rep("#legname{font-size:18px}", "#legname{font-size:18px}\n#trip>div,#speed>div{background:var(--bg);border-radius:10px;padding:1px 8px;width:max-content;margin:2px auto}#speed>div{margin:2px 0 2px auto}")
rep('<path d="M60 40 l-12 26 h24 z" fill="#4a5568"/>', '<path d="M60 40 l-12 26 h24 z" fill="#8f9bb0"/>')

# TOKEN_ROLE (Studio Eyes): a token is text OR decoration. --ink/--bg stay text; fills and lines get their own tokens.
import re as _re
c=s.count('--rule:#8f9bb0')
s=s.replace('--rule:#8f9bb0','--rule:#8f9bb0;--inkfill:#eef2f6;--ground:#04050a')
assert c==2, c
for a,b in [('background:var(--ink)','background:var(--inkfill)'),('border-color:var(--ink)','border-color:var(--inkfill)'),
            ('solid var(--ink)','solid var(--inkfill)'),('2px var(--ink) inset','2px var(--inkfill) inset'),
            ('background:var(--bg)','background:var(--ground)'),('rgba(4,5,10,0),var(--bg))','rgba(4,5,10,0),var(--ground))'),
            ('linear-gradient(var(--bg),','linear-gradient(var(--ground),')]:
    assert a in s, a
    s=s.replace(a,b)

open(OUT, 'w').write(s)
print('ok', len(s.encode()), hashlib.sha256(s.encode()).hexdigest())
