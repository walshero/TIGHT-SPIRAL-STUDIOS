#!/usr/bin/env python3
"""Signal Rider v0.20: your week, replayed, on the end card and the fade card.
Founder 2026-11-10 16:10 "Okay. Rebuild so" (default plan, second build). Answers the
2026-11-07 worry that players can't see what their choices did.
Three parts: what the week set up (spines, shortcut pull, band width, red group size, each
tied to the categories that caused it); what happened on the ride (greens collected and pinks
hit by name, frayed bands, match/half/wrong/missed at the gaps, stalls, leg-4 spines grown or
lost); and one "Try next" naming the support category that answers the heaviest stress.
Base: canon v0.19 (f834e02c)."""
import hashlib
P = 'lab/down-the-nerve.html'
s = open(P).read()
assert hashlib.sha256(s.encode()).hexdigest().startswith('f834e02c'), 'base is not canon v0.19'
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)

rep('<title>Signal Rider v0.19</title>', '<title>Signal Rider v0.20</title>')
rep('<span class="chip">v0.19</span>', '<span class="chip">v0.20</span>')

# ---- count what happens on the ride
rep("run={s:0,v:4,", "run={rec:{g:{},r:{},bands:0,match:0,half:0,wrong:0,missBeat:0,stalls:0,grown:0,lost:0},s:0,v:4,")
rep("    else if(p.good)effect(true,p.card.cap,p.card.ic);else hit(p.card.cap,p.card.ic);",
    "    else{var rc=run.rec[p.good?'g':'r'];rc[p.card.id]=(rc[p.card.id]||0)+1;if(p.good)effect(true,p.card.cap,p.card.ic);else hit(p.card.cap,p.card.ic);}")
rep("f.hit=true;hit('Hit a frayed band');", "f.hit=true;run.rec.bands++;hit('Hit a frayed band');")
rep("if(p.good&&sy4.pads.length<5){sy4.pads.push(sy4.pads[sy4.pads.length-1]+0.55);",
    "if(p.good&&sy4.pads.length<5){run.rec.grown++;sy4.pads.push(sy4.pads[sy4.pads.length-1]+0.55);")
rep("else if(!p.good&&sy4.pads.length>2){sy4.pads.pop();", "else if(!p.good&&sy4.pads.length>2){run.rec.lost++;sy4.pads.pop();")
rep("ang:full||half?lm.tgt:(wrongPad!==null?wrongPad:run.theta),t0:lm.t};",
    "ang:full||half?lm.tgt:(wrongPad!==null?wrongPad:run.theta),t0:lm.t};\n  run.rec[{full:'match',half:'half',wrong:'wrong',miss:'missBeat'}[lm.fb.kind]]++;")
rep("function missLanding(sy){ // below threshold: no action potential. Costs a hit; a fresh spark tries again.\n  endLanding();",
    "function missLanding(sy){ // below threshold: no action potential. Costs a hit; a fresh spark tries again.\n  run.rec.stalls++;endLanding();")

# ---- the replay
rep('  <p id="endStats"></p>\n', '  <p id="endStats"></p>\n  <div id="endWeek" class="replay"></div>\n')
rep('Greens narrow them again.</p>\n  <div class="row"><button class="btn primary" id="bCp">',
    'Greens narrow them again.</p>\n  <div id="fadeWeek" class="replay"></div>\n  <div class="row"><button class="btn primary" id="bCp">')
rep("function openSheet(id){",
"""function weekReplay(){
  if(!run||!run.rec)return '';var m=run.model||{},cat=m.cat||{},rec=run.rec,out=[],ride=[];
  var nm=function(id){var c=CATS.filter(function(x){return x.id===id;})[0];return c?c.name:id;};
  var lab=function(id){var d=DECK.filter(function(x){return x.id===id;})[0];return d?d.label:id;};
  var tally=function(o){return Object.keys(o).map(function(k){return lab(k)+(o[k]>1?' x'+o[k]:'');}).join(', ');};
  var sum=function(o){return Object.keys(o).reduce(function(a,k){return a+o[k];},0);};
  if(!run.week){out.push('Calm road: no week loaded, so nothing tipped the balance.');}
  else{
    var sp='The thinking cortex had '+m.pads+' landing spines (a calm road has 5).';
    if(cat.sleep)sp+=' Your '+nm('sleep')+' blocks took '+cat.sleep+'.';if(cat.body)sp+=' Your '+nm('body')+' blocks gave one back.';out.push(sp);
    var pull=m.drift<0.05?'':m.drift<0.45?'lightly':m.drift<0.8?'strongly':'very strongly';
    out.push(pull?'The survival shortcut pulled '+pull+'.'+(cat.people?' Your '+nm('people')+' blocks made it stronger.':'')+(cat.kin?' Your '+nm('kin')+' blocks eased it.':''):'The survival shortcut stayed quiet.'+(cat.kin?' Your '+nm('kin')+' blocks helped keep it that way.':''));
    var band=m.band0<0.65?'narrow':m.band0<0.95?'medium':m.band0<1.25?'wide':'very wide';
    out.push('Frayed bands started '+band+'.'+(cat.place?' Your '+nm('place')+' blocks widened them.':'')+(cat.belong?' Your '+nm('belong')+' blocks narrowed them.':''));
    if(m.clAdj)out.push('Red block groups were one block '+(m.clAdj>0?'bigger ('+nm('time')+').':'smaller ('+nm('help')+').'));
  }
  var g=sum(rec.g),r=sum(rec.r);
  ride.push(g?'You steered into '+g+' green'+(g>1?'s':'')+', each a speed surge: '+tally(rec.g)+'.':'You collected no greens. Steering into one gives a surge.');
  ride.push(r?'Pink blocks hit you '+r+' time'+(r>1?'s':'')+': '+tally(rec.r)+'.':'You dodged every pink block.');
  if(rec.bands)ride.push('Frayed bands caught you '+rec.bands+' time'+(rec.bands>1?'s':'')+'.');
  var beats=rec.match+rec.half+rec.wrong+rec.missBeat;
  if(beats)ride.push('At the gaps: '+rec.match+' match'+(rec.match===1?'':'es')+', '+rec.half+' half, '+rec.wrong+' wrong shape, '+rec.missBeat+' missed.'+(rec.stalls?' The signal stalled '+rec.stalls+' time'+(rec.stalls>1?'s':'')+'.':''));
  if(rec.grown||rec.lost)ride.push('On the last leg, greens grew back '+rec.grown+' spine'+(rec.grown===1?'':'s')+' and pinks dimmed '+rec.lost+'.');
  var pairs=[['sleep','body'],['people','kin'],['basics','help'],['time','help'],['place','belong'],['school','skills']],tip='';
  if(run.week){for(var i=0;i<pairs.length;i++){if(cat[pairs[i][0]]&&!cat[pairs[i][1]]){var c=CATS.filter(function(x){return x.id===pairs[i][1];})[0];var TIPFX={body:'It adds a landing spine at the thinking cortex.',kin:'It eases the pull of the survival shortcut.',help:'It makes red block groups one block smaller.',belong:'It narrows the frayed bands.',skills:'It makes each red block weigh less on the balance.'};tip='Try next: add a block from '+c.name+'. '+(TIPFX[c.id]||c.fx);break;}}
    if(!tip)tip=g<2?'Try next: the same week, steering into more greens.':'Try next: a harder week, and see what holds.';}
  var li=function(a){return a.map(function(x){return '<li>'+x+'</li>';}).join('');};
  return '<h3>Your week, replayed</h3>'+(out.length?'<p class="sub">What your week set up</p><ul>'+li(out)+'</ul>':'')+'<p class="sub">What happened on the ride</p><ul>'+li(ride)+'</ul>'+(tip?'<p><b>'+tip+'</b></p>':'');}
function openSheet(id){if(id==='sEnd'||id==='sFade'){var wr=document.getElementById(id==='sEnd'?'endWeek':'fadeWeek');if(wr)wr.innerHTML=weekReplay();}""")
rep(".cath h3{margin:4px 0;font-size:20px}", ".cath h3{margin:4px 0;font-size:20px}\n.replay ul{margin:4px 0 8px;padding-left:22px}.replay li{margin:4px 0}.replay .sub{margin:8px 0 0}")

# ---- founder 16:32: "almost unplayable. Too fast and sudden. Keep some of the fun curves when no blocks or
# bands are near, but tone this down big time." Straight near any block, band or landing; slower, smaller
# bends in open stretches only; half the bank.
rep("feats.forEach(function(x){mark(x.s);});\n", "feats.forEach(function(x){mark(x.s);});pickups.forEach(function(x){mark(x.s);});\n")
rep("STRAIGHT=d.map(function(v){var q=Math.max(0,Math.min(1,(v-2)/7));return q*q*(3-2*q);});}",
    "STRAIGHT=d.map(function(v){var q=Math.max(0,Math.min(1,(v-4)/10));return q*q*(3-2*q);});}")
# bend by turning, not by position: curvature is gated by the open-stretch envelope and integrated,
# so near events the tube runs straight and never swings back to centre
rep("function curveX(u){return (S.curves||1)*(0.5+0.5*strAt(u))*(8.0*Math.sin(u*0.031)+2.8*Math.sin(u*0.068+1.1));}",
    "var PX=null,PY=null,PDU=0.5;\n"
    "function buildPath(){if(!STRAIGHT)buildStraight();var n=Math.ceil(STRAIGHT.length/PDU)+2,sx=0,x=0,sy=0,y=0;PX=new Float32Array(n);PY=new Float32Array(n);\n"
    "  for(var i=0;i<n;i++){var u=i*PDU,e=strAt(u),kx=e*(0.0075*Math.sin(u*0.045)+0.0025*Math.sin(u*0.11+1.1)),ky=e*(0.005*Math.sin(u*0.038+2.0)+0.0018*Math.sin(u*0.09));\n"
    "    sx+=(kx-sx*0.02)*PDU;x+=sx*PDU;sy+=(ky-sy*0.02)*PDU;y+=sy*PDU;PX[i]=x;PY[i]=y;}}\n"
    "function pathAt(A,u){var t=u/PDU,i=Math.max(0,Math.min(A.length-2,Math.floor(t))),fr=Math.max(0,Math.min(1,t-i));return A[i]+(A[i+1]-A[i])*fr;}\n"
    "function curveX(u){if(!PX)buildPath();return (S.curves||1)*pathAt(PX,u)/4.5*8;}")
rep("function curveY(u){return (S.curves||1)*(0.5+0.5*strAt(u))*(5.6*Math.sin(u*0.026+2.0)+2.0*Math.sin(u*0.061));}",
    "function curveY(u){if(!PY)buildPath();return (S.curves||1)*pathAt(PY,u)/4.5*8;}")
rep("function buildRun(w){\n  STRAIGHT=null;BANK=0;", "function buildRun(w){\n  STRAIGHT=null;PX=null;PY=null;BANK=0;")
rep("Math.max(-0.17,Math.min(0.17,-(curveX(run.s+10)-2*curveX(run.s+5)+curveX(run.s))*0.09))",
    "Math.max(-0.08,Math.min(0.08,-(curveX(run.s+10)-2*curveX(run.s+5)+curveX(run.s))*0.09))")

open(P, 'w').write(s)
print('ok', len(s.encode()), hashlib.sha256(s.encode()).hexdigest())
