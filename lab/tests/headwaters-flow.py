#!/usr/bin/env python3
"""HEADWATERS FLOW CHECK: no dead ends.

Founder, 2026-11-11: "Having to hit a wall and go back at the start is a boring start. Hit wall,
then add detour." A blocker may stop the marble; it may never leave it with no way down but back up.

Method (arithmetic): on each mountain's height grid, a priority flood from the bottom station gives
every spot the least climbing needed to reach the station on any route (pipes count as one-way
links). A forward flood from the summit (each step may rise at most 0.25) gives every spot a
rolling marble can reach. A reachable spot that needs more than 1.0 height units of climbing to get
out is a trap. Blockers are modelled as they stand at the start: live targets and closed gates.

Exit 0 PASS (no trapped spots on any mountain), 1 HALT, 2 refused.
usage: python3 lab/tests/headwaters-flow.py [lab/headwaters.html]
"""
import asyncio, pathlib, sys
JS = r"""(mk)=>{const hw=__hw;hw.setM(mk);const m=hw.M;const nx=m.nx+1,ny=m.ny+1,cs=m.cs,N=nx*ny;
 const H=m.hc,F=m.fc,CLIMB=1.0,STEP=.25;const idx=(i,j)=>j*nx+i;
 const blocked=new Uint8Array(N);
 for(let j=0;j<ny;j++)for(let i=0;i<nx;i++){const x=i*cs,y=j*cs,n=idx(i,j);
   if(F[n]<=0){blocked[n]=1;continue;}
   for(const t of m.targets)if(!t.dead&&Math.hypot(x-t.x,y-t.y)<t.r+.3)blocked[n]=1;
   if(m.gate&&!m.gate.open&&x>m.gate.x0&&x<m.gate.x1&&Math.abs(y-m.gate.y)<.35)blocked[n]=1;}
 const nb=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]];
 const near=(x,y)=>idx(Math.round(x/cs),Math.round(y/cs));
 const pipes=m.pipes.map(pp=>[near(pp.pts[0][0],pp.pts[0][1]),near(pp.pts[pp.pts.length-1][0],pp.pts[pp.pts.length-1][1])]);
 // priority flood from the bottom station: W = lowest possible "highest point" on any route to the station
 const W=new Float32Array(N).fill(1e9);const heap=[];const push=(n,w)=>{heap.push([w,n]);let k=heap.length-1;while(k>0){const p=(k-1)>>1;if(heap[p][0]<=heap[k][0])break;[heap[p],heap[k]]=[heap[k],heap[p]];k=p;}};
 const pop=()=>{const top=heap[0],last=heap.pop();if(heap.length){heap[0]=last;let k=0;for(;;){const l=2*k+1,r=l+1;let s=k;if(l<heap.length&&heap[l][0]<heap[s][0])s=l;if(r<heap.length&&heap[r][0]<heap[s][0])s=r;if(s===k)break;[heap[s],heap[k]]=[heap[k],heap[s]];k=s;}}return top;};
 const e=m.end;for(let j=0;j<ny;j++)for(let i=0;i<nx;i++){const n=idx(i,j);if(!blocked[n]&&Math.hypot(i*cs-e[0],j*cs-e[1])<1.6){W[n]=H[n];push(n,H[n]);}}
 while(heap.length){const[w,c]=pop();if(w>W[c])continue;const i=c%nx,j=(c-i)/nx;
   for(const[a,b]of nb){const ii=i+a,jj=j+b;if(ii<0||jj<0||ii>=nx||jj>=ny)continue;const n=idx(ii,jj);if(blocked[n])continue;const nw=Math.max(H[n],w);if(nw<W[n]){W[n]=nw;push(n,nw);}}
   for(const[mo,ex]of pipes)if(Math.abs((ex%nx)-i)<=2&&Math.abs(((ex-(ex%nx))/nx)-j)<=2){const nw=Math.max(H[mo],w);if(nw<W[mo]){W[mo]=nw;push(mo,nw);}}}
 // forward: where can a marble roll from the summit (each step rises at most STEP)?
 const s0=m.checks[0],start=near(s0[0],s0[1]);const fw=new Uint8Array(N);const q=[start];fw[start]=1;
 while(q.length){const c=q.pop(),i=c%nx,j=(c-i)/nx;const out=[];
   for(const[a,b]of nb){const ii=i+a,jj=j+b;if(ii<0||jj<0||ii>=nx||jj>=ny)continue;const n=idx(ii,jj);if(!blocked[n]&&H[n]<=H[c]+STEP)out.push(n);}
   for(const[mo,ex]of pipes)if(Math.abs((mo%nx)-i)<=2&&Math.abs(((mo-(mo%nx))/nx)-j)<=2)out.push(ex);
   for(const n of out)if(!fw[n]){fw[n]=1;q.push(n);}}
 let reach=0,trap=0;const cl=[];let worst=0,wx=0,wy=0;
 for(let n=0;n<N;n++)if(fw[n]){reach++;const need=W[n]-H[n];if(need>CLIMB){trap++;const i=n%nx,j=(n-i)/nx;cl.push([i*cs,j*cs]);if(need>worst){worst=need;wx=i*cs;wy=j*cs;}}}
 const bands={};for(const[x,y]of cl){const k=Math.floor(y/4)*4;(bands[k]=bands[k]||[]).push(x);}
 const sum=Object.keys(bands).sort((a,b)=>a-b).map(k=>'y'+k+'-'+(+k+4)+': x'+Math.min(...bands[k]).toFixed(0)+'-'+Math.max(...bands[k]).toFixed(0)+' ('+bands[k].length+')');
 return {mk,reach,trap,pct:+(100*trap/Math.max(1,reach)).toFixed(1),endOK:(W[start]-H[start]<=CLIMB)?'summit reaches bottom':'SUMMIT CANNOT REACH BOTTOM (climb '+(W[start]-H[start]).toFixed(1)+')',worst:worst.toFixed(1)+' at '+wx.toFixed(1)+','+wy.toFixed(1),sum:sum.slice(0,14)};}
"""
async def main(path):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        await pg.goto(pathlib.Path(path).resolve().as_uri()); await pg.wait_for_timeout(600)
        bad = 0
        for k in 'ABCDE':
            r = await pg.evaluate(JS, k)
            ok = r['trap'] == 0 and r['endOK'].startswith('summit reaches')
            bad += 0 if ok else 1
            print(f"  {'pass' if ok else 'HALT'}  {k}: {r['reach']} reachable spots, {r['trap']} trapped ({r['pct']}%), {r['endOK']}")
            for s in r['sum']: print('        ', s)
        await b.close()
    print('FLOW: PASS, no dead ends' if not bad else f'FLOW: HALT, {bad} mountain(s) with dead ends')
    return 1 if bad else 0
if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'lab/headwaters.html'
    try: sys.exit(asyncio.run(main(path)))
    except ImportError: print('FLOW: REFUSED, no playwright'); sys.exit(2)
