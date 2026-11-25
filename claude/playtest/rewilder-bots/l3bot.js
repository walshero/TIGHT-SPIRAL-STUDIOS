// Level 3 agent for Rewilder: plays the whole level and the island with the player's inputs only
// (direction keys, Up, Smash, the Dive/Swim and Tag buttons, taps). Reads the screen the way a player would
// (where the wires, drones, feet and walls are) but never sets game state.
window.__runL3 = function(cfg){
  let seed=cfg.seed>>>0||1; Math.random=function(){seed=(seed+0x6D2B79F5)>>>0;let t=seed;t=Math.imul(t^t>>>15,t|1);t^=t+Math.imul(t^t>>>7,t|61);return((t^t>>>14)>>>0)/4294967296};
  const R=Math.random, dt=1/30;
  const Q=[]; window.setTimeout=function(fn,ms){Q.push({at:T+(ms||0)/1000,fn});return Q.length};
  const log={seed:cfg.seed,style:cfg.style,phases:[],shocks:{},kos:0,revives:0,airOuts:0,droneHits:0,stuck:[],errors:[],finishAt:null,toasts:[]};
  const t0=()=>Math.round(T*10)/10;
  const _fs=fortShock; fortShock=function(m){if(fort&&fort.hitT<=0){const k=(fort.s&&fort.s.isle?'isle':'fortress')+':'+(m||'').slice(0,18);log.shocks[k]=(log.shocks[k]||0)+1}return _fs(m)};
  const _ko=knockOut; knockOut=function(){if(restartT<=0){log.kos++;log.phases.push([t0(),'KO '+who])}return _ko()};
  const _lr=landRevive; landRevive=function(){log.revives++;log.phases.push([t0(),'BOTH DOWN -> revived']);return _lr()};
  const _ir=isleRevive; isleRevive=function(){log.revives++;log.phases.push([t0(),'BOTH DOWN (island) -> revived']);return _ir()};
  const _fin=finish; finish=function(){if(log.finishAt===null){log.finishAt=t0();log.phases.push([t0(),'FINISH'])}return _fin()};
  const _toast=toast; toast=function(t,d){if(t)log.toasts.push([t0(),t.slice(0,90)]);return _toast(t,d)};
  if(cfg.island) jumpIsland(); else jumpLevel(3);
  let phase='', phaseT=0, lastSmash=-9, sinceProg=0, progKey='';
  const setPhase=p=>{if(p!==phase){phase=p;phaseT=0;log.phases.push([t0(),p])}};
  const smash=(rate)=>{ if(T-lastSmash>=(rate||0.22)){smashQ=true;lastSmash=T} };
  const tap=(x,y)=>tapWorld(x,y);
  const tag=()=>document.getElementById('tagBtn').onclick();
  const go=x=>{ if(Math.abs(x-P.x)>8){ if(x>P.x)K.r=1; else K.l=1 } };
  const standing=()=>sites.slice(0,5).filter(s=>s.state==='standing'&&s.rows.length);
  const wallBetween=x=>walls.find(w=>w.up&&((P.x<w.x&&x>w.x)||(P.x>w.x&&x<w.x)));
  const nearestDock=x=>docks.filter(d=>d>=0).slice().sort((a,b)=>Math.abs(a-x)-Math.abs(b-x))[0];
  // underwater work: a list of x targets to smash; returns true while busy
  function swimTo(x, yWant, hitIt){
    const w=swim; if(!w) return;
    // air first
    if(!w.fish && w.air<0.4){ // find open water and rise
      let best=null;for(let dx=0;dx<1600;dx+=40){for(const sx of [w.x-dx,w.x+dx]){if(waterOpen(sx)){best=sx;break}}if(best!==null)break}
      if(best!==null){ if(Math.abs(best-w.x)>12){best>w.x?K.r=1:K.l=1} K.u=1; return }
    }
    if(Math.abs(x-w.x)>(hitIt?30:14)){ x>w.x?K.r=1:K.l=1 }
    else if(hitIt){ w.face = x>w.x? 1:-1; }
    const ty=yWant===undefined?WT+60:yWant; if(w.y<ty-10)K.d=1; else if(w.y>ty+10)K.u=1;
    if(hitIt && Math.abs(x-w.x)<=40) smash(0.25);
  }
  function climbSite(s, goalY){ // generic climber for the fortress / spire: dodge wires and swat drones
    if(P.climb!==s){
      if(P.support&&P.support.deck){ // on a landing: step to the tower face and press Up
        upQ = phaseT%0.5<dt; K.u=1; return }
      const ex=clamp(P.x,s.x+12,s.x+s.w-12); if(Math.abs(ex-P.x)>6){go(ex);return} upQ=true; K.u=1; return }
    const c=colOf(s,P.x), f=chestF(s);
    const bad=(cc,ff)=>cc<0||cc>=s.cols||wireAt(s,cc,ff);
    // swat a drone that is close
    const near=(tdr||[]).find(d=>!d.dead&&Math.abs(d.x-(P.x+P.face*30))<80&&Math.abs(d.y-(P.y-46))<74);
    if(near){P.face=near.x>P.x?1:-1; smash(0.3)}
    if(fort&&fort.tq){ // island tower: wait out a peeling drone line that is coming at our height
      const q=fort.tq, threat=q.dr.some(d=>(d.st==='cue'||(d.st==='fly'&&d.t>-0.3))&&Math.abs(d.y-(P.y-56))<140&&Math.abs(d.x-P.x)<260);
      if(threat && cfg.style==='careful'){ if(P.support&&P.support.deck){K.u=0;return} }
    }
    if(P.y<=goalY+4){ return 'there' }
    if(typeof mzLiveAt==='function'&&fort&&fort.mz&&!(fort.tq&&fort.tq.end)&&f<=MZ&&cfg.style!=='clumsy'){ // v1.11: route through the electric maze
      const L=(cc,ff)=>ff>=1&&ff<=MZ&&mzLiveAt(cc,ff), key=(a,b)=>a+'_'+b, prev={}, Q=[[f,c]]; prev[key(f,c)]=null; let goal=null;
      while(Q.length){const [ff,cc]=Q.shift(); if(ff>MZ){goal=[ff,cc];break}
        [[ff+1,cc],[ff,cc+1],[ff,cc-1],[ff-1,cc]].forEach(([nf,nc])=>{if(nf<0||nc<0||nc>=s.cols||L(nc,nf)||key(nf,nc) in prev)return;prev[key(nf,nc)]=[ff,cc];Q.push([nf,nc])})}
      if(goal){let n=goal;while(prev[key(n[0],n[1])]&&!(prev[key(n[0],n[1])][0]===f&&prev[key(n[0],n[1])][1]===c))n=prev[key(n[0],n[1])];
        if(n[0]>f){ const cx=s.x+(c+.5)*s.cw; if(Math.abs(cx-P.x)>10){cx>P.x?K.r=1:K.l=1;return} K.u=1; return }
        if(n[0]<f){ K.d=1; return }
        const tx=s.x+(n[1]+.5)*s.cw; tx>P.x?K.r=1:K.l=1; return }
      return }
    if((bad(c,f+1)||bad(c,f))&&!(cfg.style==='clumsy'&&R()<0.5)){ // move sideways to a safe column for the next floor
      let best=null,bd=99;for(let cc=0;cc<s.cols;cc++){if(!bad(cc,f+1)&&!bad(cc,f)){const d=Math.abs(cc-c);if(d<bd){bd=d;best=cc}}}
      if(best!==null&&best!==c){ const tx=s.x+(best+.5)*s.cw; tx>P.x?K.r=1:K.l=1; return }
      return // nothing safe: wait for a pulse to go dark
    }
    K.u=1;
  }
  const steps=Math.round(cfg.secs/dt);
  for(let i=0;i<steps;i++){
    try{
      K.l=K.r=K.u=K.d=0;
      if(pickOpen){const bs=[...document.querySelectorAll('#pickBtns button')];if(bs.length)bs[Math.floor(R()*Math.min(2,bs.length))].click();else pickOpen=false}
      if(cardOpen)document.getElementById('cardBtn').click();
      if(notesOpen){ if(log.finishAt!==null) break; closeNotes(); }
      if(menuOpen)setMenu(false);
      const q=fort&&fort.tq;
      if(q&&q.jail&&who===q.jail.who&&!q.fish.on){ // v1.1: caught in the drone cage on floor 16: tag the partner (the badge, as a player would)
        setPhase('jailed: tag partner'); const b=tagBadge(); if(b) tapWorld(b.x,b.y); else tagSwap();
      } else if(q&&q.fish.on&&q.refill){ // bonus (v0.95): the salmon swims past the drain to the pool
        setPhase('bonus: salmon up to the pool'); K.u=1;
      } else if(q&&q.fish.on){ // the salmon in the pipe: up to the drain and turn it
        setPhase('island: salmon to the drain'); const g=qGeo(fort.s),f=q.fish;
        if(f.y>g.drainY+18)K.u=1; else if(f.y<g.drainY-18)K.d=1; else smash(0.3);
      } else if(isle && (P.x>=0||swim)) { // cross to the island
        if(!swim){ setPhase('to the island: dive'); const d=nearestDock(0); if(Math.abs(d-P.x)>20)go(d); else {K.d=1; if(phaseT>1.5) document.getElementById('swimBtn').onclick()} }
        else { setPhase('to the island: swim'); const w=swim; if(w.x>ISX1+40){K.l=1;if(w.y>WT+20)K.u=1}else{K.l=1;K.u=1} }
      } else if(isle){ // the island quest
        const tw=sites.find(z=>z.isle), g=qGeo(tw);
        if(!q){ setPhase('island: no quest?'); }
        else if(!q.water){
          setPhase('island: beaver climbs to the valve (floor 24)');
          if(who!=='beaver'&&!q.jail&&!q.jailDone&&canTag()&&phaseT>1) tag();
          const LV=fort.decks.find(d=>d.k===QV);
          if(P.support===LV){ const vx=tw.x+tw.w-60; if(P.x<vx-10)K.r=1; else {P.face=1; smash(0.3)} }
          else climbSite(tw, LV.y-2);
        } else if(!q.drain){ setPhase('island: water filling'); }
        else if(!q.hand){ setPhase('island: drones dropping'); }
        else if(!q.door){
          setPhase('island: turtle climbs to the plate (floor 24)');
          const LV=fort.decks.find(d=>d.k===QV);
          if(P.support===LV){ if(Math.abs(P.x-LV.x)>30)go(LV.x) }
          else climbSite(tw, LV.y-2);
        } else if(q.roof.ph==='wait'){
          setPhase('island: climb to the roof'); const LV=fort.decks.find(d=>d.k===QV);
          if(P.support===tw&&P.y<=g.roofY+2){ go(tw.cx) } else climbSite(tw, g.roofY+4);
        } else if(q.roof.ph==='run'||q.roof.ph==='climb'){
          setPhase('island: cut the blimp rope'); if(P.support===tw&&P.y<=g.roofY+2){ if(Math.abs(P.x-g.post.x)>40)go(g.post.x); else {P.face=g.post.x>P.x?1:-1;smash(0.3)} } else climbSite(tw,g.roofY+4);
        } else if(cfg.bonus&&q.end&&!q.party){ // bonus (v0.93-v0.95): water back on, then all three in the pool
          const LV=fort.decks.find(d=>d.k===QV), PD=fort.decks.find(d=>d.k===QP);
          if(!log.bonusAt){log.bonusAt=t0()}
          const descendTo=d=>{ if(P.support===d) return true; if(P.y<=d.y+1){ K.d=1 } else { climbSite(tw, d.y-2) } return false };
          if(!q.refill){ setPhase('bonus: down to the valve'); if(descendTo(LV)){ const vx=tw.x+tw.w-60; if(P.x<vx-10)K.r=1; else {P.face=1; smash(0.3)} } if(q.refill&&!log.refillAt)log.refillAt=t0() }
          else if(q.pool<1){ setPhase('bonus: pool filling') }
          else { setPhase('bonus: '+who+' to the pool'); if(descendTo(PD)){ if(Math.abs(P.x-tw.cx)>20)go(tw.cx) } }
        } else { if(q.party&&!log.partyAt)log.partyAt=t0(); setPhase('island: ending ('+q.roof.ph+')') }
      } else if(swim){ // mainland underwater jobs
        const job=log.job;
        if(!job){ // nothing to do: climb out at a ladder
          setPhase('surface'); const d=nearestDock(swim.x); swimTo(d,WT+10,false); if(Math.abs(swim.x-d)<40){K.u=1; if(swim.y<WT+20)upQ=true}
        } else {
          setPhase('underwater: '+job.what);
          swimTo(job.x, job.y, true);
          if(job.done()){ log.job=null }
        }
      } else { // mainland on foot
        const st=standing();
        const dam=sites[4], fortS=sites[0];
        // jobs that need the river
        let job=null;
        if(dam.state==='standing'&&dam.foot&&dam.foot.some(f=>f.hp>0)&&st.filter(s=>s!==fortS&&s!==dam).length===0){
          const f=dam.foot.find(f=>f.hp>0); job={what:'dam footing',x:f.x+(f.x>1500?-30:30),y:WT+70,done:()=>f.hp<=0};
        }
        let tgt=null;
        if(!job){
          // order: normal sites nearest first, then the highway piers, then the fortress
          const cand=[];
          st.forEach(s=>{ if(s===fortS||s===dam&&s.foot) return; if(s.id==='highway'&&via&&!via.down){ via.piers.forEach(p=>{if(p.hp>0)cand.push({x:p.x,pier:1,s})}); if(via.piers.some(p=>p.hp>0))return }
            for(let c=0;c<s.cols;c++){let lo=-1;for(let f=0;f<s.rows.length;f++){const k=s.rows[f]&&s.rows[f][c];if(k&&k.hp>0&&k.t!=='k'){lo=f;break}} if(lo>=0)cand.push({x:s.x+(c+.5)*s.cw,lo,s})} });
          let best=1e9; cand.forEach(t=>{const d=Math.abs(t.x-P.x)+(t.lo>1?200:0);if(d<best){best=d;tgt=t}});
          if(!tgt && fortS.state==='standing') tgt={fort:1,s:fortS,x:fortS.cx};
        }
        if(tgt && !job){ const wb=wallBetween(tgt.x); if(wb){ job={what:'steel wall',x:wb.x+(P.x>wb.x?30:-30),y:WT+50,done:()=>!wb.up} } }
        if(job){
          setPhase('walk to a ladder for: '+job.what); const d=nearestDock(job.x>P.x?Math.min(job.x,P.x+9999):job.x); const dd=docks.filter(z=>z>=0&&!wallBetween(z)).sort((a,b)=>Math.abs(a-job.x)-Math.abs(b-job.x))[0];
          if(P.climb){K.d=1} else if(Math.abs(dd-P.x)>20) go(dd); else { K.d=1; log.job=job; }
        } else if(tgt&&tgt.fort){
          setPhase('fortress climb'); const s=tgt.s;
          if(P.support===s&&P.y<=GY-(s.rows.length-.5)*s.fh+2){ if(Math.abs(P.x-s.cx)>40)go(s.cx); else smash(0.3) }
          else { const r=climbSite(s, GY-(s.rows.length)*s.fh-2); if(r==='there'){K.u=1} }
        } else if(tgt){
          setPhase('smash '+tgt.s.id);
          if(tgt.pier){ const sx=tgt.x-(tgt.x>P.x?40:-40); if(P.climb)K.d=1; else if(Math.abs(sx-P.x)>10)go(sx); else {P.face=tgt.x>P.x?1:-1;smash()} }
          else if(P.climb){ if(Math.abs(tgt.x-P.x)>20)go(tgt.x); smash(); if(R()<.01)K.d=1 }
          else if(Math.abs(tgt.x-P.x)>18) go(tgt.x);
          else { if(tgt.lo>1&&R()<.1){upQ=true;K.u=1} else smash() }
        } else setPhase('waiting for growth');
      }
      if(downed&&!swim&&!(q&&q.fish.on)&&Math.abs(restX-P.x)<600&&phase.indexOf('island: ')!==0){ /* a downed partner nearby: go revive (drop any other move first, or the two cancel out) */ K.l=K.r=0;go(restX); if(Math.abs(restX-P.x)<80)smash() }
      if(cfg.style==='clumsy'&&R()<0.2){const r=R();K.l=r<.3?1:0;K.r=r>=.3&&r<.6?1:0;K.u=r>=.6&&r<.8?1:0;K.d=r>=.8?1:0}
      if(state==='poolcut'){if(!log.cutAt)log.cutAt=t0();if(pcT>5)endPoolCut()} // v1.2: the pool party is a cut scene; the bot takes its bow after the review
      zoomStep(dt);update(dt);if(cfg.render===true)render();else if(isle){ctx.save();try{drawIsle()}catch(e){}ctx.restore()}
      for(let j=Q.length-1;j>=0;j--){if(T>=Q[j].at){const f=Q.splice(j,1)[0].fn;try{typeof f==='function'&&f()}catch(e){log.errors.push('timer '+e.message)}}}
      phaseT+=dt;
      const pk=phase+'|'+sites.map(s=>s.state+s.rows.length).join(',')+'|'+(swim?Math.round(swim.x/200):Math.round(P.x/200))+'|'+Math.round(P.y/100);
      if(pk!==progKey||/waiting for growth|ending|filling|dropping/.test(phase)){progKey=pk;sinceProg=0}else{sinceProg+=dt;if(sinceProg>60){sinceProg=-1e9;log.abort=true;log.dbg={rx:restX,dx:downed&&downed.x,who,cells:sites[1].rows.slice(0,2).map(r=>r.map(c=>c?c.hp+c.t:"-").join(",")),downed:typeof downed!=="undefined"&&!!downed,tj:typeof tireJam!=="undefined"&&!!tireJam,trucks:trucks.map(t=>t.why+":"+t.state+":"+Math.round(t.x)),piers:via&&via.piers.map(p=>Math.round(p.x)+":"+p.hp),vd:via&&via.down,P:[Math.round(P.x),P.y,P.support&&P.support.id,P.climb&&P.climb.id],K:JSON.stringify(K),hw:sites[1].state,walls:typeof walls!=="undefined"?JSON.stringify(walls).slice(0,200):0};log.stuck.push({t:t0(),phase,x:Math.round(swim?swim.x:P.x),y:Math.round(swim?swim.y:P.y),who,climb:!!P.climb,sup:P.support&&(P.support.id||(P.support.deck?'deck'+P.support.k:P.support))})}}
      if(log.finishAt!==null&&T>log.finishAt+2)break;
      if(log.abort)break;
    }catch(e){log.errors.push(t0()+' '+e.message+' '+(e.stack||'').split('\n')[1]);if(log.errors.length>5)break}
  }
  if(fort&&fort.tq){const q=fort.tq;log.bonus={refill:!!q.refill,fishPool:!!q.fish.pool,n:q.n||0,party:!!q.party}}
  log.end={T:t0(),phase,level,who,isle:!!isle,sites:sites.map(s=>s.id+':'+s.state),x:Math.round(P.x),y:Math.round(P.y),swim:!!swim,quest:fort&&fort.tq?{water:!!fort.tq.water,drain:!!fort.tq.drain,hand:fort.tq.hand,door:!!fort.tq.door,roof:fort.tq.roof.ph}:null};
  return log;
};
