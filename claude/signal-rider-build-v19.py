#!/usr/bin/env python3
"""Signal Rider v0.19: a curvier tube and real music.
Founder 2026-11-10 16:09: "I feel like the tube can be curvier and the music catchier."
16:10 "Okay. Rebuild so" (default plan: curves + music from the landing tones).
Curves: wider, tighter S-bends that ease to half strength at frayed bands and landings (blocks are too dense to straighten for),
so reading what comes never fights the bend; the camera banks up to ~10 degrees into turns.
Music: there was none (a speed hum only). Now a 112 BPM track in G built on the five receptor
tones: kick/clap/hat pulse, bass over Em-C-G-D, a two-bar hook. Greens bring the hook forward
and lift the tempo; reds and frayed bands muffle the mix. At a landing the beat locks to the
landing beat (two music beats per landing beat) and each match plays the next note of the hook.
Music ducks under speech. Settings: Music on/off; Curves winding/gentle (gentle under reduced motion).
Base: canon v0.18 (968fb7c0)."""
import hashlib
P = 'lab/down-the-nerve.html'
s = open(P).read()
assert hashlib.sha256(s.encode()).hexdigest().startswith('968fb7c0'), 'base is not canon v0.18'
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)

rep('<title>Signal Rider v0.18</title>', '<title>Signal Rider v0.19</title>')
rep('<span class="chip">v0.18</span>', '<span class="chip">v0.19</span>')

# ---------------- settings
rep("var S={speed:1,glow:1,roll:reduce?0:1,outside:1,sound:1}",
    "var S={speed:1,glow:1,roll:reduce?0:1,outside:1,sound:1,music:1,curves:reduce?0.4:1}")
rep('<h3>Sound</h3><div class="seg" data-k="sound"><button class="btn" data-v="1">On</button><button class="btn" data-v="0">Off</button></div>',
    '<h3>Sound</h3><div class="seg" data-k="sound"><button class="btn" data-v="1">On</button><button class="btn" data-v="0">Off</button></div>\n'
    '  <h3>Music</h3><div class="seg" data-k="music"><button class="btn" data-v="1">On</button><button class="btn" data-v="0">Off</button></div>\n'
    '  <h3>Curves</h3><div class="seg" data-k="curves"><button class="btn" data-v="1">Winding</button><button class="btn" data-v="0.4">Gentle</button></div>')

# ---------------- curves: stronger bends, flattened near events, banking
rep("function curveX(u){return 4*Math.sin(u*0.025)+1.5*Math.sin(u*0.055+1.1);}\nfunction curveY(u){return 3*Math.sin(u*0.021+2.0)+1.0*Math.sin(u*0.047);}",
"""var STRAIGHT=null,BANK=0;
function buildStraight(){ // 1 in open stretches, easing to 0 within 5-15 units of a band, a block or a landing
  var N=Math.ceil((legs[3].end||600)+80),d=new Array(N).fill(99),mark=function(u){u=Math.round(u);if(u>=0&&u<N)d[u]=0;};
  feats.forEach(function(x){mark(x.s);});
  syns.forEach(function(x){for(var u=x.s-16;u<=x.s+6;u++)mark(u);});
  for(var i=1;i<N;i++)d[i]=Math.min(d[i],d[i-1]+1);for(i=N-2;i>=0;i--)d[i]=Math.min(d[i],d[i+1]+1);
  STRAIGHT=d.map(function(v){var q=Math.max(0,Math.min(1,(v-2)/7));return q*q*(3-2*q);});}
function strAt(u){if(!STRAIGHT)buildStraight();var i=Math.max(0,Math.min(STRAIGHT.length-2,Math.floor(u))),fr=Math.max(0,Math.min(1,u-i));return STRAIGHT[i]+(STRAIGHT[i+1]-STRAIGHT[i])*fr;}
function curveX(u){return (S.curves||1)*(0.5+0.5*strAt(u))*(8.0*Math.sin(u*0.031)+2.8*Math.sin(u*0.068+1.1));}
function curveY(u){return (S.curves||1)*(0.5+0.5*strAt(u))*(5.6*Math.sin(u*0.026+2.0)+2.0*Math.sin(u*0.061));}""")
rep("function buildRun(w){", "function buildRun(w){\n  STRAIGHT=null;BANK=0;")
rep("var rot=S.roll?(Math.PI/2-run.theta):0;", "var rot=(S.roll?(Math.PI/2-run.theta):0)+BANK;")
rep("  var ds=run.v*dt;var prev=run.s;run.s+=ds;",
    "  var ds=run.v*dt;var prev=run.s;run.s+=ds;\n"
    "  var bk=(reduce||S.curves<0.5)?0:Math.max(-0.17,Math.min(0.17,-(curveX(run.s+10)-2*curveX(run.s+5)+curveX(run.s))*0.09));BANK+=(bk-BANK)*Math.min(1,dt*1.8);")

# ---------------- music
rep("function sfxBeat(q){",
"""// v0.19 music: lookahead scheduler on the audio clock. G major pentatonic, the receptor tones.
var MUS={bus:null,lp:null,next:0,step:0,tempo:112,hookT:0,landing:false,mi:0,nb:null};
var MOTIF=[659.25,0,587.33,0,493.88,0,587.33,659.25, 0,783.99,0,659.25,587.33,0,493.88,0,
           587.33,0,493.88,0,440,0,493.88,587.33, 0,659.25,0,587.33,493.88,0,392,0];
var MNOTES=MOTIF.filter(function(x){return x>0;}),ROOTS=[82.41,65.41,98.0,73.42];
function musInit(){if(!AC||MUS.bus)return;MUS.bus=AC.createGain();MUS.bus.gain.value=0;MUS.lp=AC.createBiquadFilter();MUS.lp.type='lowpass';MUS.lp.frequency.value=9000;
  MUS.bus.connect(MUS.lp);MUS.lp.connect(master);var n=Math.floor(AC.sampleRate*0.3);MUS.nb=AC.createBuffer(1,n,AC.sampleRate);var dd=MUS.nb.getChannelData(0);for(var i=0;i<n;i++)dd[i]=Math.random()*2-1;MUS.next=AC.currentTime+0.1;}
function mNote(t,f,dur,type,vol,cut,slide){var o=AC.createOscillator(),g=AC.createGain(),fl=AC.createBiquadFilter();o.type=type;o.frequency.setValueAtTime(f,t);if(slide)o.frequency.exponentialRampToValueAtTime(slide,t+dur);
  fl.type='lowpass';fl.frequency.value=cut||4000;g.gain.setValueAtTime(0.0001,t);g.gain.exponentialRampToValueAtTime(vol,t+0.008);g.gain.exponentialRampToValueAtTime(0.0001,t+dur);
  o.connect(fl);fl.connect(g);g.connect(MUS.bus);o.start(t);o.stop(t+dur+0.05);}
function mNoise(t,dur,vol,hp){var src=AC.createBufferSource(),g=AC.createGain(),fl=AC.createBiquadFilter();src.buffer=MUS.nb;fl.type='highpass';fl.frequency.value=hp;
  g.gain.setValueAtTime(vol,t);g.gain.exponentialRampToValueAtTime(0.0001,t+dur);src.connect(fl);fl.connect(g);g.connect(MUS.bus);src.start(t);src.stop(t+dur+0.02);}
function musStep(t,st){var bar=Math.floor(st/16)%4,i=st%16,root=ROOTS[bar],land=MUS.landing;
  if(i%8===0)mNote(t,120,0.32,'sine',0.5,800,42);                        // kick
  if(!land&&(i===4||i===12))mNoise(t,0.16,0.22,1500);                     // clap
  if(!land&&i%2===0)mNoise(t,0.04,0.07,7000);                             // hat
  if(i%2===0&&(!land||i%8===0))mNote(t,i%4===0?root:root*1.5,0.22,'sawtooth',0.14,520); // bass
  if(!land){var h=MOTIF[st%32];if(h){var hv=0.045+0.06*Math.min(1,MUS.hookT/3);mNote(t,h,0.16,'square',hv,3200);}}}
function musTick(dt){if(!AC)return;musInit();var want=(S.music&&S.sound&&run&&!run.over&&!run.faded&&!paused)?(window.speechSynthesis&&speechSynthesis.speaking?0.22:0.6):0;
  MUS.bus.gain.setTargetAtTime(want,AC.currentTime,0.15);if(!want){MUS.next=AC.currentTime+0.05;return;}
  MUS.hookT=Math.max(0,MUS.hookT-dt);MUS.landing=!!run.lm;var tempo=MUS.landing?120/BEAT:(run.surgeT>0?120:112);
  var sp=60/tempo/4;if(MUS.next<AC.currentTime-0.2)MUS.next=AC.currentTime+0.02;
  while(MUS.next<AC.currentTime+0.12){musStep(MUS.next,MUS.step);MUS.step++;MUS.next+=sp;}}
function musGood(){MUS.hookT=8;}
function musBad(){if(!MUS.lp||!AC)return;var t=AC.currentTime;MUS.lp.frequency.cancelScheduledValues(t);MUS.lp.frequency.setValueAtTime(650,t);MUS.lp.frequency.exponentialRampToValueAtTime(9000,t+2.2);}
function musLandStart(){if(!AC||!MUS.bus)return;MUS.step=0;MUS.next=AC.currentTime+0.02;}
function musMatch(full){if(!AC||!MUS.bus||!S.music||!S.sound)return false;var t=AC.currentTime,f=MNOTES[MUS.mi%MNOTES.length];MUS.mi++;
  mNote(t,f,0.5,'square',full?0.16:0.08,5200);if(full)mNote(t,f*1.5,0.5,'triangle',0.08,5200);return true;}
function sfxBeat(q){""")

# hook the music into the game
rep("run.floatTxt='+ clear path';sfxGood();run.surgeT=2.0;", "run.floatTxt='+ clear path';sfxGood();musGood();run.surgeT=2.0;")
rep("function sfxBad(){", "function sfxBad(){musBad();")
rep("  BEAT=[1.1,1.0,0.95,0.9][run.leg]||0.9;\n  if(!sy.rshape)", "  BEAT=[1.1,1.0,0.95,0.9][run.leg]||0.9;musLandStart();MUS.mi=0;\n  if(!sy.rshape)")
rep("lm.hits+=full?1:0.5;sfxBeat(sy.last?Math.min(1,sy.fill/sy.need):1);}",
    "lm.hits+=full?1:0.5;if(!musMatch(full))sfxBeat(sy.last?Math.min(1,sy.fill/sy.need):1);}")
rep("  if(AC&&hum){hum.frequency.setTargetAtTime(48+run.v*7,AC.currentTime,0.08);}",
    "  if(AC&&hum){hum.frequency.setTargetAtTime(48+run.v*7,AC.currentTime,0.08);humG.gain.setTargetAtTime(S.music?0.015:0.035,AC.currentTime,0.3);}\n  musTick(dt);")

rep("if(toastT>0){toastT-=dt;if(toastT<=0)toastEl.style.display='none';}audioCues(dt);return;}",
    "if(toastT>0){toastT-=dt;if(toastT<=0)toastEl.style.display='none';}audioCues(dt);musTick(dt);return;}")

rep("function musGood(){MUS.hookT=8;}", "function musGood(){MUS.hookT=8;}\nwindow.__sr={curveX:function(u){return curveX(u);},strAt:function(u){return strAt(u);},mus:function(){return MUS;},bank:function(){return BANK;}};")

# the backdrop follows the heading only as far as it did before (soft cap), so its edge never shows; it banks with the camera
rep("ctx=ctx||cx;var hx=dcurve(curveX,run.s),hy=dcurve(curveY,run.s);",
    "ctx=ctx||cx;var hx=0.18*Math.tanh(dcurve(curveX,run.s)/0.18),hy=0.18*Math.tanh(dcurve(curveY,run.s)/0.18);")
rep("ctx.save();ctx.translate(W/2-hx*W*pan,H/2-hy*H*pan);if(S.roll)ctx.rotate(Math.PI/2-run.theta);",
    "ctx.save();ctx.translate(W/2-hx*W*pan,H/2-hy*H*pan);if(S.roll)ctx.rotate(Math.PI/2-run.theta);ctx.rotate(BANK);")

open(P, 'w').write(s)
print('ok', len(s.encode()), hashlib.sha256(s.encode()).hexdigest())
