#!/usr/bin/env python3
"""Signal Rider v0.22: name what you miss; matching back to near targets plus one more round.
Founder 2026-11-14 15:21 on v0.21: "The game seems to teach very little. Maybe we can translate
the blocks we've missed so at least the blocks are named even if missed or the game teaches
nothing. The matching section is now way too hard because the matching signs can be too far
apart. This worked better many builds ago and just needed one more round etc. Now it's worse."
1. Every cube group that passes unhit is named in a caption ("Missed: A friend who listens",
   "Dodged: Rent due Friday"), placed by the message system away from the spark; each card's name
   is spoken the first time it appears, hit or missed.
2. Matching: targets return to the reach of v0.20 (the spine beside you, no far-from-pull picks);
   relays now need three matches (was two) within six beats (was five). The next-shape preview stays.
Base: canon v0.21 (6e5f557a)."""
import hashlib
P = 'lab/down-the-nerve.html'
s = open(P).read()
assert hashlib.sha256(s.encode()).hexdigest().startswith('6e5f557a'), 'base is not canon v0.21'
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:90]); s = s.replace(a, b)

rep('<title>Signal Rider v0.21</title>', '<title>Signal Rider v0.22</title>')
rep('<span class="chip">v0.21</span>', '<span class="chip">v0.22</span>')

# ---- 1. name what passes
rep('<div id="effect" class="ui" role="status" aria-live="assertive"></div>',
    '<div id="effect" class="ui" role="status" aria-live="assertive"></div>\n<div id="passed" class="ui" role="status" aria-live="polite"></div>')
rep('#effect.bad{background:#3a1420}',
    '#passed{width:max-content;max-width:92vw;display:none;border-radius:14px;padding:6px 14px;font-weight:700;font-size:20px;background:#0d1220;border:2px solid #8f9bb0;color:#eef2f6;text-align:center}\n#passed b{color:#ffd1ec}#passed b.g{color:#b9ffc9}\n#effect.bad{background:#3a1420}')
rep("if(p.good&&!p.hit&&!p.passed&&run.s>p.s+0.6){p.passed=true;if(!run.warm&&AC&&S.sound)tone(560,0.18,'sine',0.035,400,panOf(p.a,1.2));}});",
    "if(p.good&&!p.hit&&!p.passed&&run.s>p.s+0.6){p.passed=true;if(!run.warm&&AC&&S.sound)tone(560,0.18,'sine',0.035,400,panOf(p.a,1.2));}});\n"
    "  if(!run.warm)nameMissed();")
rep("function addLoad(title,icon){",
    "var passedT=0;\n"
    "function nameMissed(){ // v0.22: a group that goes by unhit is still named, so every block teaches\n"
    "  if(!run.named)run.named={};var G={};\n"
    "  pickups.forEach(function(p){if(p.grp===undefined||run.named[p.grp]||p.s>run.s+0.5||p.s<run.s-30)return;(G[p.grp]=G[p.grp]||[]).push(p);});\n"
    "  Object.keys(G).forEach(function(k){var ps=pickups.filter(function(p){return p.grp==k;});if(ps.some(function(p){return p.s>run.s-0.4;}))return;\n"
    "    run.named[k]=1;if(run.grpHit&&run.grpHit[k])return;var miss=ps.filter(function(p){return !p.hit;});if(!miss.length)return;\n"
    "    var good=miss[0].good,labs=[];miss.forEach(function(p){if(labs.indexOf(p.card.label)<0)labs.push(p.card.label);});\n"
    "    var el=document.getElementById('passed');el.innerHTML=(good?'Missed: ':'Dodged: ')+labs.map(function(l){return '<b class=\"'+(good?'g':'')+'\">'+l+'</b>';}).join(', ');el.style.display='block';passedT=2.4;\n"
    "    if(!run.said)run.said={};var fresh=miss.filter(function(p){return !run.said[p.card.cap];});\n"
    "    if(fresh.length){fresh.forEach(function(p){run.said[p.card.cap]=1;});speak((good?'Missed ':'Dodged ')+fresh.map(function(p){return p.card.label;}).join(', '),true);}});}\n"
    "function addLoad(title,icon){")
rep("  if(effectT>0){effectT-=dt;if(effectT<=0)document.getElementById('effect').style.display='none';}",
    "  if(effectT>0){effectT-=dt;if(effectT<=0)document.getElementById('effect').style.display='none';}\n"
    "  if(passedT>0){passedT-=dt;if(passedT<=0)document.getElementById('passed').style.display='none';}")
# a hit or surge banner replaces the passed caption so two messages never stack
rep("  run.bandPulse=1;run.floatT=1.2;e.style.display='block';effectT=2.2;",
    "  run.bandPulse=1;run.floatT=1.2;e.style.display='block';effectT=2.2;passedT=0;document.getElementById('passed').style.display='none';")

# ---- 2. matching: near targets, one more round
rep("function reachPick(pads,from,skip){var reach=2.7*BEAT*0.92,", "function reachPick(pads,from,skip){var reach=2.7*BEAT*0.6,")
a = s.index("  if(sy.stressed&&Math.random()<0.6){var far=")
b = s.index("\n", a) + 1
s = s[:a] + s[b:]
rep("var beats=sy.practice?2:sy.last?(sy.stressed?6:4):3;", "var beats=sy.practice?2:sy.last?(sy.stressed?6:4):4;")
rep("max:sy.practice?3:sy.last?(sy.stressed?8:6):5", "max:sy.practice?3:sy.last?(sy.stressed?8:6):6")
rep("var done=sy.last?sy.fill>=sy.need:lm.hits>=(sy.practice?1:2);", "var done=sy.last?sy.fill>=sy.need:lm.hits>=(sy.practice?1:3);")
rep("Math.min(1,lm.hits/2)", "Math.min(1,lm.hits/(sy.practice?1:3))")
rep("Two good landings fire the next neuron.", "Three good landings fire the next neuron.")

open(P, 'w').write(s)
print('v0.22 written', hashlib.sha256(s.encode()).hexdigest()[:8], len(s))
