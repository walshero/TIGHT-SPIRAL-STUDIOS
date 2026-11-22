// injected into the page; drives Rewilder headless at fixed dt with a seeded RNG
window.__runBot = function(cfg){
  let seed=cfg.seed>>>0||1; Math.random=function(){seed=(seed+0x6D2B79F5)>>>0;let t=seed;t=Math.imul(t^t>>>15,t|1);t^=t+Math.imul(t^t>>>7,t|61);return((t^t>>>14)>>>0)/4294967296};
  const R=Math.random; // bot shares rng (deterministic per seed)
  const log={persona:cfg.persona,seed:cfg.seed,level:cfg.level,events:[],toasts:{},hurts:{},kos:0,tags:0,picks:{},cards:0,stuck:[],errors:[],finishAt:null,siteT:{},maxSites:0};
  const t0=()=>Math.round(T*10)/10;
  const _toast=toast; toast=function(t,d){ if(t&&KEEPMSG.some(k=>t.indexOf(k)===0)){log.toasts[t]=(log.toasts[t]||0)+1} return _toast(t,d)};
  const _hurt=hurt; hurt=function(n){const st=(new Error).stack.split('\n')[2]||'';const m=st.match(/at (\S+)/);const k=(m?m[1]:'?')+'';log.hurts[k]=(log.hurts[k]||0)+n;return _hurt(n)};
  const _ko=knockOut; knockOut=function(){if(restartT>0)return _ko();log.kos++;log.events.push([t0(),'KO',who]);return _ko()};
  const _fin=finish; finish=function(){if(log.finishAt===null)log.finishAt=t0();return _fin()};
  const _sb=spawnBaron; spawnBaron=function(w){log.events.push([t0(),'baron',w&&w.kind]);return _sb(w)};
  const Q=[]; window.setTimeout=function(fn,ms){Q.push({at:T+(ms||0)/1000,fn});return Q.length};
  const _jl=jumpLevel; jumpLevel=function(n){log.events.push([t0(),'RESTART',n]);log.restarts=(log.restarts||0)+1;return _jl(n)};
  try{ if(cfg.level>1) jumpLevel(cfg.level); else startGame(); }catch(e){log.errors.push('start:'+e.message)}
  const dt=1/30, steps=Math.round(cfg.secs/dt); let lastX=P.x, lastProg=0, progT=0, stuckOpen=false, holdT=0, mode='walk', modeT=0;
  const prev={};
  const prog=()=>sites.reduce((a,s)=>a+s.rows.reduce((b,r)=>b+r.filter(k=>k&&k.hp>0).length,0),0)*-1 + sites.filter(s=>s.state==='grown').length*1000 + sites.filter(s=>s.state==='growing').length*300;
  for(let i=0;i<steps;i++){
    try{
      if(pickOpen){const bs=[...document.querySelectorAll('#pickBtns button')];if(bs.length){const b=cfg.persona==='novice'?bs[Math.floor(R()*bs.length)]:bs[0];const k=b.textContent.trim().slice(0,30);log.picks[k]=(log.picks[k]||0)+1;b.click()}else pickOpen=false}
      if(cardOpen){log.cards++;document.getElementById('cardBtn').click()}
      if(notesOpen){closeNotes()}
      if(menuOpen)setMenu(false);
      // choose target
      const swimming=!!swim;
      K.l=K.r=K.u=K.d=0;
      const tgts=[]; // [x, kind, site]
      sites.forEach((s,ix)=>{ if(s.state!=='standing'||!s.rows.length)return; for(let c=0;c<s.cols;c++){let lo=-1,any=false;for(let f=0;f<s.rows.length;f++){const k=s.rows[f]&&s.rows[f][c];if(k&&k.hp>0&&k.t!=='k'){any=true;if(lo<0)lo=f}} if(any)tgts.push({x:s.x+(c+.5)*s.cw,lo,s})}});
      if(typeof via!=='undefined'&&via&&!via.down&&!via.fall)via.piers.forEach(p=>{if(p.hp>0)tgts.push({x:p.x,lo:0,pier:1})});
      const EX=EAST()-30; let tgt=null,best=1e9; for(const t of tgts){if(t.x>EX)continue;const d=Math.abs(t.x-P.x)+(t.lo>1?150:0)+(t.s&&sites.indexOf(t.s)>=5?3000:0);if(d<best){best=d;tgt=t}}
      if(downed&&!swimming&&R()<.7){tgt={x:restX,lo:0,revive:1}}
      if(cfg.persona==='novice'&&R()<0.35){
        const r=R(); if(r<.3)K.l=1;else if(r<.6)K.r=1;else if(r<.75){upQ=true;K.u=1}else if(r<.9)smashQ=true;
      } else if(swimming){ K.r=1; if(R()<.05)smashQ=true; }
      else if(tgt){
        const stand = tgt.pier? tgt.x-(tgt.x>P.x?40:-40) : tgt.x;
        const dx=stand-P.x;
        if(P.climb){ // smash forward-ish while climbing, drift toward target column, come down if nothing at chest
          if(Math.abs(dx)>20){dx>0?K.r=1:K.l=1}
          if(cfg.persona==='climber'&&R()<.3)K.u=1;
          if(P.cool<=0)smashQ=true;
          if(R()<.01)K.d=1;
        } else if(Math.abs(dx)>(tgt.pier?10:18)){ dx>0?K.r=1:K.l=1 }
        else{
          if(tgt.pier)P.face=tgt.x>P.x?1:-1;
          const wantClimb = tgt.lo>1 || (cfg.persona==='climber'&&R()<.05);
          if(wantClimb && R()<.1){upQ=true;K.u=1}
          else if(P.cool<=0)smashQ=true;
        }
        if(P.sup>=1 && R()<.02 && !tgt.revive){sHeld=true;sT=.6;slamQ=true;sHeld=false}
      } else {
        const g=sites.find(s=>s.state==='growing'); if(g){const c=g.x+g.w/2; if(Math.abs(c-P.x)>40){if(c>P.x)K.r=1;else K.l=1}} else K.r=1;
      }
      if(P.energy<30 && typeof canTag==='function' && canTag()){try{tagOut();log.tags++}catch(e){}}
      update(dt);
      for(let j=Q.length-1;j>=0;j--){if(T>=Q[j].at){const f=Q.splice(j,1)[0].fn;try{typeof f==='function'&&f()}catch(e){}}}
      if(log.finishAt!==null&&T>log.finishAt+3)break;
      // telemetry
      sites.forEach((s,ix)=>{const k=ix+':'+s.id;if(prev[k]!==s.state){log.events.push([t0(),k,s.state]);prev[k]=s.state;if(!log.siteT[k])log.siteT[k]={};if(log.siteT[k][s.state]===undefined)log.siteT[k][s.state]=t0()}});
      const p=prog(); if(p>lastProg){lastProg=p;progT=0;if(stuckOpen){stuckOpen=false}} else {progT+=dt; if(progT>45&&!stuckOpen){stuckOpen=true;log.stuck.push({t:t0(),x:Math.round(P.x),y:Math.round(P.y),who,swim:!!swim,climb:P.climb?P.climb.id:null,tgt:tgt?(tgt.pier?'pier':tgt.revive?'revive':tgt.s&&tgt.s.id):null,states:sites.map(s=>s.id+':'+s.state).join(' ')})}}
      if(cfg.probeAt&&Math.abs(T-cfg.probeAt)<dt/2+0.001){const lot=sites[3];log.probe={chest:(()=>{try{return chestF(sites[3])}catch(e){return e.message}})(),tg3:target(sites[3]),support:P.support&&P.support.id,ncl:P.ncl,T,K:JSON.stringify(K),walls:walls.map(w=>w.x+':'+w.up),crates:crates.map(c=>Math.round(c.x)+':'+c.g),EAST:EAST(),sites:sites.map(s=>s.id+':'+s.state+':'+s.x+':'+s.rows.length+':'+(s.rows[0]||[]).map(k=>k?k.t+k.hp:0).join('')),who,x:P.x,y:P.y,flip:P.flip,nap:P.nap,stuck:P.stuck,cool:P.cool,climb:!!P.climb,sup:P.support==='ground'?'g':!!P.support,tumble:P.tumble,energy:P.energy,lot:{state:lot.state,x:lot.x,w:lot.w,rows:lot.rows.map(r=>r.map(k=>k?k.t+k.hp:0).join(',')),tgt:target(lot)},trucks:trucks.map(t=>t.state+'@'+Math.round(t.x)),restartT,downed,tireJam}}
      if(state!=='play'&&state!=='vacation'){log.events.push([t0(),'state',state]);break}
    }catch(e){log.errors.push(t0()+' '+e.message);if(log.errors.length>5)break}
  }
  log.end={T:t0(),state,level,who,grown:sites.filter(s=>s.state==='grown').length,sites:sites.map(s=>s.id+':'+s.state),paved:stats.paved,built:typeof built!=='undefined'?built:null,energy:Math.round(P.energy),x:Math.round(P.x),done};
  return log;
};
