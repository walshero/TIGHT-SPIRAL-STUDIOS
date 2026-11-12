// Mock only: alternate drawings for the 93 ramp, swapped in for drawRamp. Not shipped in the game.
window.rampA=function(s,ty,right){ // helix: the ramp corkscrews down round a cluster of posts
 const d=right?1:-1,e=right?VX1:VX0,cx=e+d*84,rx=78,ry=13,y0=ty+6,H=GY-6-y0,col=s.l2?'#3a3a40':'#4f7a5c',N=2,pt=a=>[cx-d*rx*Math.cos(a),y0+H*a/(N*2*Math.PI)+ry*Math.sin(a)];
 const seg=(a0,a1,back)=>{const P=[];for(let i=0;i<=14;i++)P.push(pt(a0+(a1-a0)*i/14));const path=()=>{ctx.beginPath();P.forEach((q,i)=>i?ctx.lineTo(q[0],q[1]):ctx.moveTo(q[0],q[1]))};ctx.lineCap='butt';ctx.lineJoin='round';
  path();ctx.strokeStyle=INK;ctx.lineWidth=25;ctx.stroke();path();ctx.strokeStyle=back?'#35573f':col;ctx.lineWidth=21;ctx.stroke();ctx.save();ctx.translate(0,-5);path();ctx.strokeStyle=back?'#8f8a80':'#b3ada2';ctx.lineWidth=11;ctx.stroke();ctx.setLineDash([10,12]);path();ctx.strokeStyle='#fbf6ea';ctx.lineWidth=1.6;ctx.stroke();ctx.setLineDash([]);ctx.restore();
  if(!back)P.forEach((q,i)=>{if(i%2===0)line(q[0],q[1]-11,q[0],q[1]-20,'#6d7684',2.2)})};
 for(let k=0;k<N;k++)seg(k*2*Math.PI+Math.PI,k*2*Math.PI+2*Math.PI,true);
 [-.55,0,.55].forEach((u,i)=>{const x=cx+u*rx;shape(rectPts(x-7,y0+18,14,H-12,i+40,.5),col,{lw:2});for(let y=y0+40;y<GY-30;y+=46)line(x-5,y,x+5,y+16,'#35573f',2.2)});
 line(cx-rx*.55,y0+60,cx+rx*.55,y0+60,col,5);line(cx-rx*.55,y0+150,cx+rx*.55,y0+150,col,5);
 for(let k=0;k<N;k++)seg(k*2*Math.PI,k*2*Math.PI+Math.PI,false);
 shape([[cx-d*rx-d*4,GY],[cx-d*rx+d*60,GY],[cx-d*rx+d*44,GY-12],[cx-d*rx-d*4,GY-12]],'#b3ada2',{lw:2})};
window.rampB=function(s,ty,right){ // flyover: the ramp peels off and swings toward you, road surface showing
 const d=right?1:-1,e=right?VX1:VX0,col=s.l2?'#3a3a40':'#4f7a5c',X=u=>e+d*u,
  U=[[X(0),ty+2],[X(118),ty+2],[X(176),ty+96],[X(168),GY-10]],L=[[X(0),ty+22],[X(70),ty+26],[X(112),GY-104],[X(58),GY+2]];
 const mid=t=>{const a=bez(U,t),b=bez(L,t);return[(a[0]+b[0])/2,(a[1]+b[1])/2,Math.hypot(a[0]-b[0],a[1]-b[1])]};
 [.3,.55,.8].forEach((t,i)=>{const m=mid(t);shape(rectPts(m[0]-9,m[1],18,GY-m[1],i+50,.5),col,{lw:2});shape(rectPts(m[0]-m[2]*.42,m[1]-2,m[2]*.84,12,i+53,.4),col,{lw:2});for(let y=m[1]+24;y<GY-26;y+=40)line(m[0]-6,y,m[0]+6,y+14,'#35573f',2.2)});
 const poly=[];for(let i=0;i<=16;i++)poly.push(bez(U,i/16).slice(0,2));for(let i=16;i>=0;i--)poly.push(bez(L,i/16).slice(0,2));
 const fas=[];for(let i=0;i<=16;i++){const q=bez(L,i/16);fas.push([q[0],q[1]])}for(let i=16;i>=0;i--){const q=bez(L,i/16);fas.push([q[0],q[1]+10+i*.5])}shape(fas,col,{lw:2});
 shape(poly,'#b3ada2',{lw:2.4,sh:1});
 ctx.setLineDash([10,12]);ctx.beginPath();for(let i=0;i<=16;i++){const m=mid(i/16);i?ctx.lineTo(m[0],m[1]):ctx.moveTo(m[0],m[1])}ctx.strokeStyle='#fbf6ea';ctx.lineWidth=2;ctx.stroke();ctx.setLineDash([]);
 for(let i=1;i<=9;i++){const q=bez(U,i/10);line(q[0],q[1],q[0],q[1]-11,'#6d7684',2.2)}ctx.beginPath();for(let i=0;i<=16;i++){const q=bez(U,i/16);i?ctx.lineTo(q[0],q[1]-11):ctx.moveTo(q[0],q[1]-11)}ctx.strokeStyle='#6d7684';ctx.lineWidth=2.4;ctx.stroke()};
