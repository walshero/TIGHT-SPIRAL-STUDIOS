#!/usr/bin/env python3
"""Signal Rider v0.24: the win state (claude/SIGNAL-RIDER-WIN-STATE-2026-11-17.md, option 1).
Founder 2026-11-17 20:32: "1." (the combined ending).
Cortex ending, about 6.5 s, a tap skips it:
  0.0-2.4  Hitchcock pull-back: the camera starts close on the thinking cortex and pulls out while the
           whole route you rode lights up as a Brainbow fiber bundle, fingertip to cortex, relays flashing.
  2.2-4.4  Turkle: your neuron blooms in the cortex: Brainbow dendrites with one bright spine per landing
           spine this week gave you (plus any you grew). Temple bell (founder pick W6) as it opens.
  4.2-6.5  Osterweil: the touch arrives: a ripple at the fingertip answered by a pulse in your neuron;
           then, after the picture has held, one line: "You felt it."
Alarm ending, about 4.5 s: the route lights to the sensory cortex, the alarm glows bright, then settles
  into a slow amber breath; then "Your alarm answered first." Never a losing screen.
The end card shows your neuron again (Turkle's object). Reduced motion: no camera move, a 2.5 s fade.
No text over the picture until it has held (Hitchcock). Base: canon v0.23 (e249f9f3)."""
import hashlib
P = 'lab/down-the-nerve.html'
s = open(P).read()
assert hashlib.sha256(s.encode()).hexdigest().startswith('e249f9f3'), 'base is not canon v0.23'
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:90]); s = s.replace(a, b)

rep('<title>Signal Rider v0.23</title>', '<title>Signal Rider v0.24</title>')
rep('<span class="chip">v0.23</span>', '<span class="chip">v0.24</span>')

# end card carries the neuron
rep('  <h2 id="hE">You reached the thinking cortex</h2>',
    '  <h2 id="hE">You reached the thinking cortex</h2>\n  <canvas id="endNeuron" width="480" height="300" style="width:240px;height:150px;display:none;margin:2px auto 6px" role="img" aria-label="Your neuron from this ride"></canvas>')
rep("</style>", "body.winning #hud,body.winning #msgs,body.winning #inset{visibility:hidden!important}\n</style>", s.count("</style>"))

WIN_JS = r"""
// ---------- v0.24 the win state ----------
var WIN=null;
function wEase(x){x=Math.max(0,Math.min(1,x));return x<0.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;}
function wPts(){return {F:[0.17*W,0.84*H],S:[0.52*W,0.63*H],T:[0.50*W,0.40*H],C1:[0.33*W,0.22*H],C2:[0.64*W,0.17*H],A:[0.27*W,0.36*H]};}
function wLegs(P,alarm){var L=[[P.F,[0.22*W,0.66*H],P.S],[P.S,[0.56*W,0.52*H],P.T],[P.T,[0.36*W,0.33*H],P.C1]];
  L.push(alarm?[P.C1,[0.22*W,0.26*H],P.A]:[P.C1,[0.47*W,0.08*H],P.C2]);return L;}
function qpt(l,t){var a=l[0],b=l[1],c=l[2],u=1-t;return [u*u*a[0]+2*u*t*b[0]+t*t*c[0],u*u*a[1]+2*u*t*b[1]+t*t*c[1]];}
function makeNeuron(spines){var seed=7+spines*13+(run.rec?run.rec.grown*5:0);function rnd2(){seed=(seed*16807)%2147483647;return seed/2147483647;}
  var segs=[],tips=[];var n=6+Math.floor(rnd2()*3);
  function grow(x,y,a,len,d,col){var x2=x+Math.cos(a)*len,y2=y+Math.sin(a)*len;segs.push({x:x,y:y,x2:x2,y2:y2,d:d,col:col,w:Math.max(1,3.2-d)});
    if(d<3){var k=d===0?2:1+(rnd2()<0.6?1:0);for(var j=0;j<k+0;j++)grow(x2,y2,a+(rnd2()-0.5)*1.1,len*(0.62+rnd2()*0.15),d+1,col);}else tips.push({x:x2,y:y2,a:a,col:col});}
  for(var i=0;i<n;i++)grow(0,0,i*TAU/n+rnd2()*0.5,26+rnd2()*10,0,COLS[i%COLS.length]);
  var sp=[];for(var q=0;q<Math.min(tips.length,Math.max(2,spines)*3);q++){var t=tips[Math.floor(q*tips.length/Math.max(1,Math.min(tips.length,Math.max(2,spines)*3)))];sp.push(t);}
  return {segs:segs,spines:sp.slice(0,Math.max(2,spines)*3),n:spines};}
function drawNeuron(c,nx,ny,sc,g,glow){c.save();c.translate(nx,ny);c.scale(sc,sc);c.globalCompositeOperation='lighter';c.lineCap='round';
  WIN.neuron.segs.forEach(function(sg){var a=Math.max(0,Math.min(1,g*4-sg.d));if(a<=0)return;c.strokeStyle=sg.col;c.shadowColor=sg.col;c.shadowBlur=8*glow;c.globalAlpha=0.85;c.lineWidth=sg.w;
    c.beginPath();c.moveTo(sg.x,sg.y);c.lineTo(sg.x+(sg.x2-sg.x)*a,sg.y+(sg.y2-sg.y)*a);c.stroke();});
  if(g>0.85){var sa=Math.min(1,(g-0.85)/0.15);WIN.neuron.spines.forEach(function(t){c.globalAlpha=sa;c.fillStyle='#ffffff';c.shadowColor=t.col;c.shadowBlur=10*glow;c.beginPath();c.arc(t.x+Math.cos(t.a)*3,t.y+Math.sin(t.a)*3,2.6,0,TAU);c.fill();});}
  c.globalAlpha=1;c.fillStyle='#ffffff';c.shadowColor='#ffd23f';c.shadowBlur=18*glow;c.beginPath();c.arc(0,0,7+2*glow,0,TAU);c.fill();c.restore();}
function startWin(kind){var spines=run.model?run.model.pads:5;var sy4=syns[3];if(sy4&&sy4.pads)spines=Math.max(spines,sy4.pads.length);
  WIN={kind:kind,t:0,dur:reduce?2.6:(kind==='cortex'?6.6:4.6),neuron:makeNeuron(spines),rang:false,said:false};document.body.classList.add('winning');
  var e=document.getElementById('effect');if(e)e.style.display='none';var pz=document.getElementById('passed');if(pz)pz.style.display='none';}
function endWin(){if(!WIN)return;var k=WIN.kind;var ec=document.getElementById('endNeuron');
  if(ec){if(k==='cortex'){ec.style.display='block';var c2=ec.getContext('2d');c2.setTransform(1,0,0,1,0,0);c2.fillStyle='#04050a';c2.fillRect(0,0,480,300);var keep=WIN;drawNeuron(c2,240,150,2.4,1,1);WIN=keep;}else ec.style.display='none';}
  WIN=null;document.body.classList.remove('winning');openSheet('sEnd');}
function drawWin(dt){var w=WIN,t=w.t,alarm=w.kind==='alarm',P=wPts(),L=wLegs(P,alarm);
  cx.setTransform(DPR,0,0,DPR,0,0);cx.globalCompositeOperation='source-over';cx.fillStyle='#04050a';cx.fillRect(0,0,W,H);
  var A=reduce?1:wEase(t/2.4),k=reduce?1:3.0-2.0*A,pr0=Math.min(3.999,Math.min(1,t/2.3)*4),hd=qpt(L[Math.floor(pr0)],pr0-Math.floor(pr0)),fx=hd[0]+(W/2-hd[0])*A,fy=hd[1]+(H/2-hd[1])*A;
  cx.save();cx.translate(W/2,H/2);cx.scale(k,k);cx.translate(-fx,-fy);
  // the brain, faint: a dome with a few folds
  cx.globalAlpha=0.55*(reduce?Math.min(1,t/0.6):1);cx.strokeStyle='#2c3a58';cx.lineWidth=2;cx.beginPath();cx.ellipse(0.49*W,0.21*H,0.40*W,0.155*H,0,Math.PI*0.98,Math.PI*2.02);cx.stroke();
  for(var g2=0;g2<5;g2++){cx.beginPath();cx.arc(0.22*W+g2*0.13*W,0.215*H,0.05*W,Math.PI*1.1,Math.PI*1.9);cx.stroke();}
  cx.globalAlpha=1;
  // the route as a Brainbow bundle, lit in order
  var prog=reduce?1:Math.min(1,t/2.3)*4;cx.globalCompositeOperation='lighter';cx.lineCap='round';
  for(var li=0;li<4;li++){var lp=Math.max(0,Math.min(1,prog-li));if(lp<=0)continue;var l=L[li];
    for(var st=0;st<5;st++){var off=(st-2)*2.2,col=alarm&&li===3?['#ff4f7a','#ff9a3f','#ff6b6b','#ffd23f','#ff4fa3'][st]:COLS[(st+li*2)%COLS.length];
      cx.strokeStyle=col;cx.shadowColor=col;cx.shadowBlur=10;cx.globalAlpha=0.75;cx.lineWidth=1.8;cx.beginPath();
      for(var q=0;q<=40*lp;q++){var u=q/40,p=qpt(l,u),p2=qpt(l,Math.min(1,u+0.01)),nx2=-(p2[1]-p[1]),ny2=p2[0]-p[0],nl=Math.hypot(nx2,ny2)||1;var X=p[0]+nx2/nl*off,Y=p[1]+ny2/nl*off;q?cx.lineTo(X,Y):cx.moveTo(X,Y);}cx.stroke();}
    if(lp<1){var hp=qpt(l,lp);cx.globalAlpha=1;cx.fillStyle='#ffffff';cx.shadowColor='#bff3ff';cx.shadowBlur=24;cx.beginPath();cx.arc(hp[0],hp[1],7,0,TAU);cx.fill();}
    else if(li<3){var sp2=l[2],fl=Math.max(0,1-(prog-li-1)*1.5);cx.globalAlpha=0.6+0.4*fl;cx.fillStyle='#ffd23f';cx.shadowColor='#ffd23f';cx.shadowBlur=14+20*fl;cx.beginPath();cx.arc(sp2[0],sp2[1],5+5*fl,0,TAU);cx.fill();}}
  cx.globalAlpha=1;cx.shadowBlur=0;
  // fingertip
  cx.fillStyle='#ffe2c4';cx.shadowColor='#ffe2c4';cx.shadowBlur=12;cx.beginPath();cx.arc(P.F[0],P.F[1],9,0,TAU);cx.fill();cx.shadowBlur=0;
  if(!alarm){
    var g=reduce?Math.min(1,t/1.2):wEase((t-2.2)/1.9);if(g>0){if(!w.rang&&t>=(reduce?0.3:2.4)){w.rang=true;bell();}
      var pulse=t>4.3?0.6+0.4*Math.sin((t-4.3)*5):1;drawNeuron(cx,P.C2[0],P.C2[1],1.15,g,pulse);}
    if(t>4.2||reduce){var rt=reduce?0.5:(t-4.2);for(var r=0;r<3;r++){var rr=(rt*60+r*22)%70;cx.globalAlpha=Math.max(0,1-rr/70)*0.9;cx.strokeStyle='#ffe2c4';cx.lineWidth=2.5;cx.beginPath();cx.arc(P.F[0],P.F[1],10+rr,0,TAU);cx.stroke();}cx.globalAlpha=1;}
  }else{
    var ga=reduce?1:wEase((t-2.1)/0.8),settle=reduce?1:wEase((t-3.0)/1.2),breath=0.5+0.5*Math.sin(t*2.2);
    if(ga>0){var col2=settle<1?'#ff4f7a':'#ffb347',rad=(14+18*ga)*(1-0.35*settle)+breath*3*settle;cx.globalAlpha=0.9;cx.fillStyle=settle>0.5?'#ffb347':'#ff4f7a';cx.shadowColor=cx.fillStyle;cx.shadowBlur=30+30*(1-settle);
      cx.beginPath();cx.arc(P.A[0],P.A[1],rad,0,TAU);cx.fill();cx.globalAlpha=1;cx.shadowBlur=0;}
  }
  cx.restore();cx.globalCompositeOperation='source-over';
  // words only after the picture has held
  var wt=alarm?3.6:5.2;if(reduce)wt=1.2;
  if(t>wt){var a2=Math.min(1,(t-wt)/0.5);cx.globalAlpha=a2;cx.font='800 34px "Avenir Next","Segoe UI",system-ui,sans-serif';cx.textAlign='center';cx.textBaseline='middle';
    cx.lineWidth=6;cx.strokeStyle='#04050a';var line=alarm?'Your alarm answered first.':'You felt it.';cx.font='800 '+(alarm?28:36)+'px "Avenir Next","Segoe UI",system-ui,sans-serif';cx.strokeText(line,W/2,H*0.9,W-32);cx.fillStyle='#eef2f6';cx.fillText(line,W/2,H*0.9,W-32);cx.globalAlpha=1;
    if(!w.said){w.said=true;speak(line,false);}}
}
addEventListener('pointerdown',function(e){if(WIN&&WIN.t>0.5){e.preventDefault();e.stopPropagation();endWin();}},true);
addEventListener('keydown',function(e){if(WIN&&WIN.t>0.5){e.preventDefault();e.stopPropagation();endWin();}},true);
"""
rep("function addBtn(label,primary,fn){", WIN_JS + "function addBtn(label,primary,fn){")
rep("  run.over=true;bell();document.getElementById('hE').textContent='You reached the thinking cortex';",
    "  run.over=true;document.getElementById('hE').textContent='You reached the thinking cortex';")
rep("  addBtn('Library',false,function(){closeSheets();openSheet('sLib');});\n  openSheet('sEnd');\n}",
    "  addBtn('Library',false,function(){closeSheets();openSheet('sLib');});\n  startWin('cortex');\n}")
rep("addReplayBtn();speak('The survival shortcut fired first.',false);setTimeout(function(){openSheet('sEnd');},700);",
    "addReplayBtn();startWin('alarm');")
rep("  render();requestAnimationFrame(loop);\n}", "  if(WIN){WIN.t+=dt;drawWin(dt);if(WIN&&WIN.t>=WIN.dur+1.2)endWin();requestAnimationFrame(loop);return;}\n  render();requestAnimationFrame(loop);\n}")

open(P, 'w').write(s)
print('v0.24 written', hashlib.sha256(s.encode()).hexdigest()[:8], len(s))
