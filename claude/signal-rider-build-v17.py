#!/usr/bin/env python3
"""Signal Rider v0.17: every beat of the lock-and-key landing gives a clear verdict.
Founder 2026-11-09 22:17: "The shapes at the cortex are good but it's not clear when you've
correctly 'clicked' a shape or if you've failed to. This should be cleaner, crisper."
Per beat, for 0.55 s: MATCH = the landed spine flashes green with an expanding ring and a
check on the key; HALF = amber ring; WRONG SHAPE = pink X on the spine you landed on;
MISSED = key dims and shakes. A one-word label sits under the key. A green progress arc
around the key fills toward firing. Each new key pops in.
Base: canon v0.16 (aa8c2f42)."""
import hashlib
P = 'lab/down-the-nerve.html'
s = open(P).read()
assert hashlib.sha256(s.encode()).hexdigest().startswith('aa8c2f42'), 'base is not canon v0.16'
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)

rep('<title>Signal Rider v0.16</title>', '<title>Signal Rider v0.17</title>')
rep('<span class="chip">v0.16</span>', '<span class="chip">v0.17</span>')

# record the verdict of each beat
rep("  if(!full&&!half&&sy.pads.some(function(p){return p!==lm.tgt&&Math.abs(angDiff(run.theta,p))<0.25;})&&AC&&S.sound){tone(150,0.18,'square',0.06);}",
    "  var wrongPad=null;if(!full&&!half){sy.pads.forEach(function(p){if(p!==lm.tgt&&Math.abs(angDiff(run.theta,p))<0.25)wrongPad=p;});}\n"
    "  if(wrongPad!==null&&AC&&S.sound){tone(150,0.18,'square',0.06);}\n"
    "  lm.fb={kind:full?'full':half?'half':wrongPad!==null?'wrong':'miss',ang:full||half?lm.tgt:(wrongPad!==null?wrongPad:run.theta),t0:lm.t};")
rep("  lm.tgt=nextTarget(sy);playKey(sy);\n}", "  lm.tgt=nextTarget(sy);playKey(sy);lm.keyT=lm.t;\n}")

# draw the verdict, the progress arc and the key pop
rep("""    var kx=cxv,ky=cyv,kr=Math.max(22,0.07*Math.min(W,H)),k=lm.key||keyOf(sy,lm.tgt);""",
"""    var fb=lm.fb&&(lm.t-lm.fb.t0)<0.55?lm.fb:null,fq=fb?(lm.t-fb.t0)/0.55:0;
    var FBC={full:'#7cfc9a',half:'#ffd166',wrong:'#ff4fa3',miss:'#ff4fa3'};
    if(fb&&fb.kind!=='miss'){var fp=proj(fb.ang,zf,1.0),fc=FBC[fb.kind];
      cx.strokeStyle=fc;cx.shadowColor=fc;cx.shadowBlur=blur()*2;cx.lineWidth=5;cx.globalAlpha=1-fq;
      cx.beginPath();cx.arc(fp[0],fp[1],rs*(1.5+1.8*fq),0,TAU);cx.stroke();
      if(fb.kind==='full'){cx.fillStyle=fc;cx.globalAlpha=0.9*(1-fq);var fi=sy.pads.indexOf(fb.ang);shapePath(cx,fp[0],fp[1],rs*1.05,sy.rshape[fi]);cx.fill();}
      if(fb.kind==='wrong'){var xr=rs*1.1;cx.lineWidth=7;cx.globalAlpha=1-fq*0.6;cx.beginPath();cx.moveTo(fp[0]-xr,fp[1]-xr);cx.lineTo(fp[0]+xr,fp[1]+xr);cx.moveTo(fp[0]+xr,fp[1]-xr);cx.lineTo(fp[0]-xr,fp[1]+xr);cx.stroke();}
      cx.globalAlpha=1;cx.shadowBlur=0;}
    var shake=fb&&fb.kind==='miss'?Math.sin(fq*40)*8*(1-fq):0;
    var pop=lm.keyT!==undefined?Math.min(1,(lm.t-lm.keyT)/0.15):1;
    var kx=cxv+shake,ky=cyv,kr=Math.max(22,0.07*Math.min(W,H))*(0.6+0.4*pop),k=lm.key||keyOf(sy,lm.tgt);""")
rep("""    cx.fillStyle='#ffe066';cx.shadowColor='#ffe066';cx.shadowBlur=blur()*2;shapePath(cx,kx,ky,kr,k);cx.fill();cx.shadowBlur=0;
    cx.strokeStyle='#ffe066';cx.lineWidth=4;cx.globalAlpha=0.9;cx.beginPath();cx.arc(kx,ky,kr*(1.6+1.6*ph),0,TAU);cx.stroke();cx.globalAlpha=1;}""",
"""    cx.globalAlpha=fb&&fb.kind==='miss'?0.45:1;
    cx.fillStyle='#ffe066';cx.shadowColor='#ffe066';cx.shadowBlur=blur()*2;shapePath(cx,kx,ky,kr,k);cx.fill();cx.shadowBlur=0;cx.globalAlpha=1;
    cx.strokeStyle='#ffe066';cx.lineWidth=4;cx.globalAlpha=0.9;cx.beginPath();cx.arc(kx,ky,kr*(1.6+1.6*ph),0,TAU);cx.stroke();cx.globalAlpha=1;
    // progress toward firing: a green arc that fills with each landing
    var prog=sy.last?Math.min(1,sy.fill/sy.need):Math.min(1,lm.hits/2);
    cx.strokeStyle='#26313e';cx.lineWidth=7;cx.beginPath();cx.arc(kx,ky,kr*1.32,0,TAU);cx.stroke();
    if(prog>0){cx.strokeStyle='#7cfc9a';cx.shadowColor='#7cfc9a';cx.shadowBlur=blur();cx.beginPath();cx.arc(kx,ky,kr*1.32,-Math.PI/2,-Math.PI/2+TAU*prog);cx.stroke();cx.shadowBlur=0;}
    if(fb&&fb.kind==='full'){var cr=kr*0.55;cx.strokeStyle='#04050a';cx.lineWidth=8;cx.lineCap='round';cx.globalAlpha=1-fq*0.5;
      cx.beginPath();cx.moveTo(kx-cr,ky+cr*0.05);cx.lineTo(kx-cr*0.25,ky+cr*0.7);cx.lineTo(kx+cr,ky-cr*0.6);cx.stroke();
      cx.strokeStyle='#7cfc9a';cx.lineWidth=5;cx.stroke();cx.lineCap='butt';cx.globalAlpha=1;}
    if(fb){var lab={full:'Match',half:'Half',wrong:'Wrong shape',miss:'Missed'}[fb.kind],fs=Math.max(20,Math.round(kr*0.62));
      cx.font='800 '+fs+'px "Avenir Next","Segoe UI",system-ui,sans-serif';cx.textAlign='center';cx.textBaseline='middle';
      var tw=cx.measureText(lab).width,ty=ky+kr*1.32+fs*1.05;cx.fillStyle='#04050a';cx.globalAlpha=0.92;cx.beginPath();
      if(cx.roundRect)cx.roundRect(kx-tw/2-12,ty-fs*0.72,tw+24,fs*1.44,fs*0.5);else cx.rect(kx-tw/2-12,ty-fs*0.72,tw+24,fs*1.44);cx.fill();
      cx.globalAlpha=1;cx.fillStyle=FBC[fb.kind];cx.fillText(lab,kx,ty);}}""")

# one meter, not two: the old threshold ring stays hidden while the lock-and-key arc is showing
rep("if(RING){if(!RING.hold)RING.t+=1/60;", "if(RING&&!run.lm){if(!RING.hold)RING.t+=1/60;")
# the check belongs on the spine you hit, not on the next key
rep("""    if(fb&&fb.kind==='full'){var cr=kr*0.55;cx.strokeStyle='#04050a';cx.lineWidth=8;cx.lineCap='round';cx.globalAlpha=1-fq*0.5;
      cx.beginPath();cx.moveTo(kx-cr,ky+cr*0.05);cx.lineTo(kx-cr*0.25,ky+cr*0.7);cx.lineTo(kx+cr,ky-cr*0.6);cx.stroke();""",
"""    if(fb&&fb.kind==='full'){var cp=proj(fb.ang,zf,1.0),cr=rs*0.75,cX=cp[0],cY=cp[1];cx.strokeStyle='#04050a';cx.lineWidth=9;cx.lineCap='round';cx.globalAlpha=1-fq*0.5;
      cx.beginPath();cx.moveTo(cX-cr,cY+cr*0.05);cx.lineTo(cX-cr*0.25,cY+cr*0.7);cx.lineTo(cX+cr,cY-cr*0.6);cx.stroke();""")

open(P, 'w').write(s)
print('ok', len(s.encode()), hashlib.sha256(s.encode()).hexdigest())
