import re
s=open('/tmp/tsp/sandbags.html').read()
def once(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:90]); s=s.replace(a,b)
# G1 the pale halo on every shape read as vector stickers: a cut layer shows a thin dark edge, not a white one
once("#scenery .ly1 *{ stroke:rgba(255,248,232,.26); stroke-width:1.3; stroke-linejoin:round; }","#scenery .ly1 *{ stroke:rgba(18,10,4,.16); stroke-width:.5; stroke-linejoin:round; }")
once("#scenery .ly2 *{ stroke:rgba(255,248,232,.32); stroke-width:1.5; stroke-linejoin:round; }","#scenery .ly2 *{ stroke:rgba(18,10,4,.2); stroke-width:.55; stroke-linejoin:round; }")
once("#scenery .ly3 *{ stroke:rgba(255,248,232,.36); stroke-width:1.7; stroke-linejoin:round; }","#scenery .ly3 *{ stroke:rgba(18,10,4,.24); stroke-width:.6; stroke-linejoin:round; }")
# G2 the card's thickness: the edge facing the key light catches it (top-left), the far edge falls to shadow
RIM='<feOffset in="d" dx="0.7" dy="0.8" result="dO"/><feComposite in="d" in2="dO" operator="out" result="rA"/><feFlood flood-color="#fff4dc" flood-opacity="%s"/><feComposite in2="rA" operator="in" result="rim"/><feOffset in="d" dx="-0.5" dy="-0.6" result="dO2"/><feComposite in="d" in2="dO2" operator="out" result="rB"/><feFlood flood-color="#120a04" flood-opacity=".32"/><feComposite in2="rB" operator="in" result="dim"/>'
for fid,op in [('card1','.22'),('card2','.34'),('card3','.42')]:
    i=s.index('<filter id="%s"'%fid); j=s.index('</filter>',i)
    f=s[i:j]; k=f.rindex('<feMerge>')
    f=f[:k]+RIM%op+f[k:].replace('<feMergeNode in="p"/></feMerge>','<feMergeNode in="p"/><feMergeNode in="dim"/><feMergeNode in="rim"/></feMerge>')
    s=s[:i]+f+s[j:]
# G3 film grain: the vignette rule had silently replaced the grain (same ::after); grain gets its own sheet
once('<g id="gag" aria-hidden="true"></g>','<g id="gag" aria-hidden="true"></g>',1)
once('      <div class="altrow" id="altnum">','      <div class="grain" aria-hidden="true"></div>\n      <div class="altrow" id="altnum">')
once("#scenery .mass *{","""/* v47 FILM GRAIN, its own sheet (the vignette's ::after had overwritten it since v35) */
.skybox > .grain{ position:absolute; inset:0; z-index:3; pointer-events:none; opacity:.30; mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.1' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 1.6 -.3'/%3E%3C/filter%3E%3Crect width='220' height='220' filter='url(%23n)'/%3E%3C/svg%3E");
  background-size:220px 220px; }
#scenery .mass *{""")
open('/tmp/sb/w.html','w').write(s); print('ok')

# ============ BLACK SPOTS (scene 1) ============
s=open('/tmp/sb/w.html').read()
def once(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:90]); s=s.replace(a,b)
BS_HELP=r'''  /* v47 LUMINO PASS, Black Spots. A tower crane that is a tower crane: a
     lattice mast rising from behind the blocks, the slewing ring and cab at
     its head, the long lattice jib with its trolley and hook, the short
     counter-jib with its concrete counterweights, the A-frame apex and the
     pendant ties. Built from the real parts, not a sign for "crane". */
  function lattice(x0,y0,x1,y1,w,col,lw){
    var dx=x1-x0, dy=y1-y0, L=Math.hypot(dx,dy), ux=dx/L, uy=dy/L, nx=-uy*w/2, ny=ux*w/2, d='', n=Math.max(2,Math.round(L/(w*1.1)));
    d+='M'+(x0+nx)+' '+(y0+ny)+' L'+(x1+nx)+' '+(y1+ny)+' M'+(x0-nx)+' '+(y0-ny)+' L'+(x1-nx)+' '+(y1-ny)+' ';
    for(var i=0;i<n;i++){ var a=i/n, b=(i+1)/n, s1=i%2?1:-1;
      d+='M'+(x0+dx*a+nx*s1).toFixed(2)+' '+(y0+dy*a+ny*s1).toFixed(2)+' L'+(x0+dx*b-nx*s1).toFixed(2)+' '+(y0+dy*b-ny*s1).toFixed(2)+' '; }
    return ln(d,col,lw);
  }
  function towerCrane(x,base,top,jib,cj){
    var c='#c9542e', cd='#8e3a20', o='<g class="noedge">';
    o+=lattice(x,base,x,top,5,c,.9);
    o+=rc(x-4,top-4,8,4,cd)+rc(x+3,top-9,7,6,'#e8e2d2')+rc(x+4,top-8,5,3,'#7f98ad');
    o+=lattice(x,top-6,x+jib,top-6,4,c,.8)+lattice(x,top-6,x-cj,top-6,4,c,.8);
    o+=rc(x-cj,top-8,9,9,'#8a8478')+rc(x-cj+10,top-8,6,9,'#9d978a');
    o+=lattice(x,top-8,x,top-24,3.4,c,.7);
    o+=ln('M'+x+' '+(top-24)+' L'+(x+jib*.72)+' '+(top-8)+' M'+x+' '+(top-24)+' L'+(x-cj+4)+' '+(top-8),'#6e2a18',.45);
    var tx=x+jib*.58; o+=rc(tx-2,top-4,4,2,cd)+ln('M'+tx+' '+(top-2)+' V'+(top+34),'#2c2b30',.35)+rc(tx-1.6,top+34,3.2,2.6,'#d2a13c');
    return o+'</g>';
  }
  // the 1970s signal: DONT WALK in orange letters, not the hand and countdown of later years
  function dontWalk(x,y){ return '<g class="noedge">'+rc(x,y,14,12,'var(--p-char)')+rc(x+1,y+1,12,10,'#1b1c21')+'</g>'
     +'<g class="blink"><text x="'+(x+7)+'" y="'+(y+5.2)+'" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="3.6" fill="#ff9a3d">DONT</text><text x="'+(x+7)+'" y="'+(y+9.6)+'" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="3.6" fill="#ff9a3d">WALK</text></g>'; }
  // a window air conditioner, the kind every 1970s brick block wore
  function acUnit(x,y){ return rc(x,y,6,3.6,'#c9c2b0')+'<g class="noedge">'+ln('M'+(x+.8)+' '+(y+.9)+' h4.4 M'+(x+.8)+' '+(y+1.8)+' h4.4 M'+(x+.8)+' '+(y+2.7)+' h4.4','#8d8472',.35)+rc(x,y+3.6,6,.6,'rgba(0,0,0,.25)')+'</g>'; }
  function stains(x,y,w,n,seed){ var r=tssR(seed), d=''; for(var i=0;i<n;i++){ var sx=x+r()*w; d+='M'+sx.toFixed(1)+' '+y+' q'+((r()-.5)*1.4).toFixed(1)+' '+(6+r()*10).toFixed(1)+' '+((r()-.5)*1).toFixed(1)+' '+(10+r()*14).toFixed(1)+' '; } return '<g class="noedge">'+ln(d,'rgba(40,24,14,.16)',1.2)+'</g>'; }
  // a bright morning: the sun is up to the right, every upright thing lays a
  // long soft shadow down and to the left across the pavement
  function sunShadow(x,g,h,k){ k=k||1; return '<path d="M'+(x-1.5)+' '+g+' l'+(-h*.7*k).toFixed(1)+' '+(h*.12*k).toFixed(1)+' l3 .6 L'+(x+1.5)+' '+g+' Z" fill="rgba(30,34,52,.22)"/>'; }
'''
i=s.index('  var SCENERY=[\n'); s=s[:i]+BS_HELP+s[i:]
once("     '<g class=\"noedge\">'+ln('M236 -4 l30 -30 M266 -34 l-4 12 M244 -10 l26 0','var(--p-verm)',1.2)+ln('M266 -34 l0 30','var(--p-verm)',.6)+ln('M238 -2 v48','var(--p-verm)',1.4)+'</g>'+",
     "     towerCrane(250,150,-46,78,26)+")
# weathering on the near blocks, an awning over the lit door
once("     '<g class=\"noedge\" fill=\"var(--p-char-d)\">'+win(-116,116,8,2,8,9,7,7)+'</g>'+",
     "     '<g class=\"noedge\" fill=\"var(--p-char-d)\">'+win(-116,116,8,2,8,9,7,7)+'</g>'+acUnit(-114,125.6)+acUnit(-54,125.6)+acUnit(-24,141.6)+stains(-120,125,130,9,11)+")
once("     '<g class=\"noedge\" fill=\"var(--p-char-d)\">'+win(204,114,19,2,8,9,8,7)+'</g>'+",
     "     '<g class=\"noedge\" fill=\"var(--p-char-d)\">'+win(204,114,19,2,8,9,8,7)+'</g>'+acUnit(205,123.6)+acUnit(253,123.6)+acUnit(349,139.6)+acUnit(413,123.6)+acUnit(461,139.6)+stains(200,123,316,16,23)+")
once("     '<g class=\"lit glow\">'+lr(314,134,24,14)+'</g>'+",
     "     '<g class=\"lit glow\">'+lr(314,134,24,14)+'</g>'+P('M308 131 h44 l4 6 h-52 Z','#2f5a46')+'<g class=\"noedge\">'+ln('M310 137 v-.1 M316 137 M322 137','#244637',.1)+rc(304,136.4,52,1,'#244637')+'</g>'+")
# the ambulance out from behind the balloon; its bar with it
once("     ambulance(214,136)+","     ambulance(262,136)+")
once('<rect class="blink mid" x="234" y="136" width="6.4"','<rect class="blink mid" x="282" y="136" width="6.4"')
once('<rect class="blink2 mid" x="241" y="136" width="6.4"','<rect class="blink2 mid" x="289" y="136" width="6.4"')
once('<circle class="blink mid" cx="237" cy="137.8" r="6"','<circle class="blink mid" cx="285" cy="137.8" r="6"')
# one double yellow; the trolley-rail lines are gone (Longwood never had rails)
once("ln('M-124 173.6 h648 M-124 176.4 h648','#d9b53c',1)+ln('M-124 169 h648 M-124 181 h648','#8a8478',.7,.8)+'</g>'+",
     "ln('M-124 174.2 h648 M-124 176.2 h648','#d9b53c',.8)+'</g>'+")
# the signal: DONT WALK, the period sign
a=s.index("     '<g class=\"blink hand\"><path d=\"M151.6 144"); b=s.index("\n",s.index('<rect x="158.4" y="143" width="3" height=".9"/></g>',a))+1
s=s[:a]+"     dontWalk(148,134)+\n"+s[b:]
# long morning shadows, down and to the left
once("     figure(60,198,42,{felt:'blue'","     '<g class=\"noedge\">'+sunShadow(155.3,198,52)+sunShadow(60,198,42,1.1)+sunShadow(118,183.4,23)+'<path d=\"M262 160 l-26 6 h60 l6 -6 Z\" fill=\"rgba(30,34,52,.2)\"/></g>'+\n     figure(60,198,42,{felt:'blue'")
open('/tmp/sb/w.html','w').write(s); print('bs ok')

# ============ G5 PAPER RELIEF: the card's own fibre, lit ============
s=open('/tmp/sb/w.html').read()
REL='<feTurbulence type="fractalNoise" baseFrequency="%s" numOctaves="3" seed="%d" result="bump"/><feDiffuseLighting in="bump" surfaceScale="%s" diffuseConstant="1" lighting-color="#fff" result="lit"><feDistantLight azimuth="225" elevation="58"/></feDiffuseLighting><feComposite in="p" in2="lit" operator="arithmetic" k1=".26" k2=".84" k3="0" k4="0" result="pl"/><feComposite in="pl" in2="d" operator="in" result="p2"/>'
for fid,bf,sd,ss in [('card1','.45',21,'.8'),('card2','.55',22,'1.0'),('card3','.65',23,'1.1')]:
    i=s.index('<filter id="%s"'%fid); j=s.index('</filter>',i); f=s[i:j]
    k=f.rindex('<feMerge>')
    f=f[:k]+REL%(bf,sd,ss)+f[k:].replace('<feMergeNode in="p"/><feMergeNode in="dim"/>','<feMergeNode in="p2"/><feMergeNode in="dim"/>')
    assert 'p2' in f
    s=s[:i]+f+s[j:]
open('/tmp/sb/w.html','w').write(s); print('relief ok')

# ============ PEACH COBBLER (scene 2) ============
s=open('/tmp/sb/w.html').read()
def once(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:90]); s=s.replace(a,b)
def repfn(name,new):
    global s
    a=s.index('  function '+name+'('); b=s.index('\n  }\n',a)+4; s=s[:a]+new+s[b:]
repfn('fence',r'''  // v47: a picket fence as it is built: two rails behind, pointed pickets
  // nailed on with gaps, each a little off true, soil at the foot
  function fence(x,y,n,h,gap,f){
    var r=tssR(Math.round(x*3+y)), o='', w=3.2, sp=gap*.62;
    var cnt=Math.round(n*gap/sp);
    o+=rc(x-1,y+h*0.28,cnt*sp+1,2.2,'var(--p-bone-d)')+rc(x-1,y+h*0.7,cnt*sp+1,2.2,'var(--p-bone-d)');
    for(var i=0;i<cnt;i++){ var px=x+i*sp, ph=h*(.96+r()*.08), a=(r()-.5)*2.4;
      o+='<g transform="rotate('+a.toFixed(1)+' '+(px+w/2).toFixed(1)+' '+(y+h)+')">'+P('M'+px.toFixed(1)+' '+(y+h)+' V'+(y+h-ph+w*.9).toFixed(1)+' L'+(px+w/2).toFixed(1)+' '+(y+h-ph).toFixed(1)+' L'+(px+w).toFixed(1)+' '+(y+h-ph+w*.9).toFixed(1)+' V'+(y+h)+' Z',f)+'</g>'; }
    return o+'<g class="noedge">'+rc(x-1,y+h-1.2,cnt*sp+1,1.6,'rgba(70,52,30,.35)')+'</g>';
  }
''')
repfn('bulkhead',r'''  // v47: a steel cellar bulkhead against the foundation: a poured concrete
  // curb, two sloped doors with their seam and hasp, rust at the hinges
  function bulkhead(x,y){
    return rc(x-2,y-1,44,3,'var(--p-granite)')
      + P('M'+x+' '+y+' h40 l0 -8 l-6 -7 h-28 l-6 7 z','#5d6b73')
      + '<g class="noedge">'+P('M'+x+' '+(y-8)+' l6 -7 h28 l6 7 z','#71808a')+ln('M'+(x+20)+' '+(y-15)+' V'+y,'#3c474e',.7)
      + rc(x+18.4,y-7,3.2,1.8,'#2c3136')+rc(x+5,y-14.4,3,1.2,'#8a4a2e')+rc(x+32,y-14.4,3,1.2,'#8a4a2e')+rc(x-2,y-1,44,.8,'rgba(0,0,0,.3)')+'</g>';
  }
''')
repfn('trampoline',r'''  // v47: a backyard trampoline of the time: a steel ring on bent-tube legs,
  // the springs all round, the black mat, a padded blue frame cover
  function trampoline(x,g,r){
    var o='<g class="noedge">'+ln('M'+(x-r*.9)+' '+(g-7)+' q-1 4 -1 7 h5 M'+(x+r*.9)+' '+(g-7)+' q1 4 1 7 h-5 M'+(x-r*.35)+' '+(g-6)+' v6 M'+(x+r*.35)+' '+(g-6)+' v6','#7e8a92',1)+'</g>';
    o+='<ellipse cx="'+x+'" cy="'+(g-7)+'" rx="'+r+'" ry="'+(r*.22)+'" fill="#2f5f8a"/>';
    o+='<ellipse cx="'+x+'" cy="'+(g-7)+'" rx="'+(r*.84)+'" ry="'+(r*.16)+'" fill="#9aa4ab"/>';
    o+='<ellipse cx="'+x+'" cy="'+(g-7)+'" rx="'+(r*.72)+'" ry="'+(r*.12)+'" fill="#17181c"/>';
    var sp='';
    for(var i=0;i<24;i++){ var a=i/24*Math.PI*2, c=Math.cos(a), s2=Math.sin(a);
      sp+='M'+(x+c*r*.72).toFixed(1)+' '+(g-7+s2*r*.12).toFixed(1)+' L'+(x+c*r*.84).toFixed(1)+' '+(g-7+s2*r*.16).toFixed(1)+' '; }
    return o+'<g class="noedge">'+ln(sp,'#c9cfd3',.45)+'<ellipse cx="'+(x+r*1.4)+'" cy="'+(g-.4)+'" rx="'+(r*1.3)+'" ry="'+(r*.14)+'" fill="rgba(60,40,20,.28)"/></g>';
  }
''')
PEACH=r'''  /* v47 LUMINO PASS, Peach Cobbler. Golden hour: the sun is low on the left,
     so every upright thing lays a long warm-dark shadow out to the right
     across the lawn. */
  function goldShadow(x,g,h,w){ w=w||3; return '<path d="M'+(x-w/2)+' '+g+' l'+(h*1.9).toFixed(1)+' '+(h*.1).toFixed(1)+' h'+(w*.9)+' L'+(x+w/2)+' '+g+' Z" fill="rgba(62,38,22,.24)"/>'; }
  // a slip and slide laid out on the grass, wet, with the hose that feeds it
  function slipSlide(x,g,L){
    return rc(x,g-2.6,L,3.2,'#f2c230',' rx="1"')+'<g class="noedge">'+rc(x,g-1.6,L,.8,'#3f7fc0')+rc(x+2,g-2.4,L*.7,.5,'rgba(255,255,255,.55)')
      +'<ellipse cx="'+(x+L+3)+'" cy="'+(g-.8)+'" rx="5" ry="1.6" fill="#f2c230"/><ellipse cx="'+(x+L+3)+'" cy="'+(g-.9)+'" rx="3.6" ry="1" fill="#8fc4e8" opacity=".8"/>'
      +ln('M'+(x-1)+' '+(g-.8)+' q-6 1 -10 -1 q-5 -2 -2 -4 q4 -2 6 1 q2 3 -3 3.6 q-6 .6 -12 -1','#3f7a3a',.9)+'</g>';
  }
  function mailbox(x,g){ return rc(x,g-14,2.4,14,'var(--p-kraft-d)')+rc(x-6,g-20,14,7,'var(--p-steel)',' rx="3"')+'<g class="noedge">'+rc(x+5.4,g-19.4,1.6,5.6,'var(--p-verm)')+rc(x-6,g-14.6,14,.8,'rgba(0,0,0,.25)')+'</g>'; }
'''
i=s.index('  var SCENERY=[\n'); s=s[:i]+PEACH+s[i:]
once("     bulkhead(110,186)+","     bulkhead(70,184)+")
once("     grill(128,194)+","     grill(98,196)+")
once("     '<g class=\"noedge\">'+rc(214,193,46,3.2,'var(--p-gold)',' rx=\"1\"')+rc(214,193.6,46,.9,'var(--p-cream)')+'</g>'+","     slipSlide(212,196,46)+")
once("     rc(378,170,3,22,'var(--p-kraft-d)')+rc(372,164,16,9,'var(--p-steel)',' rx=\"3\"')+\n     rc(384,165,2,7,'var(--p-verm)')+","     mailbox(380,196)+")
once("     figure(188,197,34,{felt:'purple',dir:1,arm:'carry',carry:cobbler,stride:5,","     '<g class=\"noedge\">'+goldShadow(122,197,34,8)+goldShadow(98,196,8,8)+goldShadow(381,196,20,3)+'</g>'+\n     figure(122,197,34,{felt:'purple',dir:1,arm:'carry',carry:cobbler,stride:5,")
# the fence throws its shadow too
once("     fence(150,158,3,28,11,'var(--p-white)')+fence(206,158,4,28,11,'var(--p-white)')+",
     "     '<g class=\"noedge\"><path d=\"M150 186 l54 3 h58 l-6 -3 Z\" fill=\"rgba(62,38,22,.2)\"/></g>'+fence(150,158,3,28,11,'var(--p-white)')+fence(206,158,4,28,11,'var(--p-white)')+")
# a far blue mountain on the horizon (Monadnock from the Massachusetts line) takes more of the empty sky
once("   '<g class=\"ly1\">'+\n     P('M-124 30 Q-40 4 60 18 T250 6 T420 20 T524 12 L524 200 L-124 200 Z','#b49a73')+",
     "   '<g class=\"ly1\">'+P('M-124 20 Q20 0 150 -4 L232 -40 Q250 -46 268 -38 L330 -12 Q420 -2 524 -8 L524 60 L-124 60 Z','#b6a0a4')+'</g>'+'<g class=\"noedge\"><rect x=\"-124\" y=\"-50\" width=\"648\" height=\"90\" fill=\"#e7b98c\" opacity=\".18\"/></g>'+\n   '<g class=\"ly1\">'+\n     P('M-124 30 Q-40 4 60 18 T250 6 T420 20 T524 12 L524 200 L-124 200 Z','#b49a73')+")
open('/tmp/sb/w.html','w').write(s); print('peach ok')

# ============ ECHIGO (scene 0) ============
s=open('/tmp/sb/w.html').read()
def once(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:90]); s=s.replace(a,b)
EH=r'''  /* v47 LUMINO PASS, Echigo. Each roof fired its own grey; windows that are
     not all the same window (shoji, glass, a bamboo blind, shutters drawn);
     the street furniture of a real Niigata town: wooden poles and a mess of
     wires, downpipes, the drain channel along the fronts, crates, a bicycle;
     lantern light that falls on the plaster and on the puddles; rain in
     depth, fine far away, soft streaks close to the lens, splashes. */
  var TT=['#4a4e57','#565962','#42454d','#5c5b5f','#4f545b','#474a50'], TTi=0;
  function tileTone(){ return TT[(TTi++)%TT.length]; }
  function jfw(x,y,w,h,on){
    var k=((Math.round(x*7+y*13))%4+4)%4, o='<g class="noedge">'+rc(x-1.4,y-1.4,w+2.8,h+2.8,'var(--p-timber-d)')+'</g>';
    if(on){
      o+='<g class="lit glow">'+lr(x,y,w,h)+'</g>';
      if(k===0){ var g=''; for(var gx=x+w/4;gx<x+w-.5;gx+=w/4) g+='M'+gx.toFixed(1)+' '+y+' v'+h+' '; for(var gy=y+h/3;gy<y+h-.5;gy+=h/3) g+='M'+x+' '+gy.toFixed(1)+' h'+w+' '; o+='<g class="noedge">'+ln(g,'var(--p-timber)',.45)+'</g>'; }
      else if(k===1){ var b=''; for(var by=y+.8;by<y+h*.6;by+=.9) b+='M'+x+' '+by.toFixed(1)+' h'+w+' '; o+='<g class="noedge">'+rc(x,y,w,h*.6,'rgba(120,80,30,.55)')+ln(b,'rgba(60,34,12,.5)',.3)+'</g>'; }
      else o+='<g class="noedge">'+ln('M'+(x+w/2)+' '+y+' v'+h,'var(--p-timber-d)',.7)+rc(x,y,w,Math.max(1,h*.18),'rgba(74,34,8,.3)')+'</g>';
      o+='<g class="noedge"><ellipse cx="'+(x+w/2)+'" cy="'+(y+h+3.2)+'" rx="'+(w*.8)+'" ry="1.8" fill="#ffc46a" opacity=".22"/></g>';
    } else {
      if(k%2){ var sh=''; for(var sx=x+1.2;sx<x+w;sx+=1.6) sh+='M'+sx.toFixed(1)+' '+y+' v'+h+' '; o+='<g class="noedge">'+rc(x,y,w,h,'#5a4330')+ln(sh,'#3a2a1e',.45)+'</g>'; }
      else o+='<g class="noedge">'+rc(x,y,w,h,'#262a33')+rc(x+.6,y+.6,w*.4,h*.3,'rgba(160,176,196,.18)')+ln('M'+(x+w/2)+' '+y+' v'+h,'var(--p-timber-d)',.6)+'</g>';
    }
    return o+'<g class="noedge">'+rc(x-2,y+h+1.2,w+4,1.4,'var(--p-timber-d)')+'</g>';
  }
  function downpipe(x,y0,y1){ return '<g class="noedge">'+ln('M'+x+' '+y0+' l1.6 2 V'+(y1-2)+' l1.4 1.6','#383b42',1.3)+rc(x-1.4,y0-1.2,5,1.4,'#383b42')+'</g>'; }
  function crates(x,g){ var o='', cols=['#e0b23a','#c9432e','#e0b23a'];
    for(var i=0;i<3;i++){ var y=g-5.2*(i+1); o+=rc(x+(i%2)*.8,y,11,5,cols[i],' rx=".4"')+'<g class="noedge">'+rc(x+1.4+(i%2)*.8,y+1.2,3.4,2.2,'rgba(0,0,0,.35)')+rc(x+6.2+(i%2)*.8,y+1.2,3.4,2.2,'rgba(0,0,0,.35)')+'</g>'; }
    return o; }
  function bicycle(x,g){ var r=4.4;
    return '<g class="noedge">'+'<circle cx="'+x+'" cy="'+(g-r)+'" r="'+r+'" fill="none" style="stroke:#26282d;stroke-width:.9"/><circle cx="'+(x+14)+'" cy="'+(g-r)+'" r="'+r+'" fill="none" style="stroke:#26282d;stroke-width:.9"/>'
      +ln('M'+x+' '+(g-r)+' L'+(x+5)+' '+(g-r-6)+' L'+(x+12)+' '+(g-r-6)+' L'+(x+14)+' '+(g-r)+' M'+(x+5)+' '+(g-r-6)+' L'+(x+7.5)+' '+(g-r)+' L'+x+' '+(g-r)+' M'+(x+7.5)+' '+(g-r)+' L'+(x+12)+' '+(g-r-6)+' M'+(x+12)+' '+(g-r-6)+' l1 -3 h2 M'+(x+5)+' '+(g-r-6)+' l-1 -2','#7a8a96',.8)
      +rc(x+13,g-r-12,5,3.4,'#4a4f55',' rx=".4"')+'</g>'; }
  function upole(x,g,h){ return rc(x-1.2,g-h,2.4,h,'#5b4a3a')+rc(x-7,g-h+3,14,1.4,'#4a3a2c')+rc(x-5,g-h+8,10,1.2,'#4a3a2c')+'<g class="noedge">'+rc(x+1.2,g-h+11,3.4,5,'#7d868c',' rx="1"')+'</g>'; }
'''
i=s.index('  function echigoTown(){'); s=s[:i]+EH+s[i:]
# tile tones, one per roof
once("    return P(d,UK.tile)+ukClip(d,kawara(x-e,y-rh,x+w+e,y+1))+'<g class=\"noedge\">'+rc(x-e,y,w+2*e,1.6,UK.tileD)+'</g>'+ridge(x-e+3,x+w+e-3,y-rh,UK.tileD);",
     "    return P(d,tileTone())+ukClip(d,kawara(x-e,y-rh,x+w+e,y+1))+'<g class=\"noedge\">'+rc(x-e,y,w+2*e,1.6,UK.tileD)+'</g>'+ridge(x-e+3,x+w+e-3,y-rh,UK.tileD);")
# Echigo-only windows
a=s.index('  function echigoTown(){'); b=s.index('\n  }\n',a)
body=s[a:b].replace('fw(','jfw(').replace('jjfw(','jfw(')
# a massif, not Fuji
body=body.replace("P('M-10 178 L40 152 L92 122 L128 100 L150 88 L176 58 L204 40 L222 44 L240 36 L262 58 L292 82 L310 80 L338 112 L372 134 L410 150 L410 200 L-10 200 Z','#5a6880')",
                  "P('M-10 176 L30 150 L66 132 L100 110 L128 98 L156 76 L180 66 L200 72 L224 54 L246 60 L268 78 L298 74 L326 96 L360 116 L410 136 L410 200 L-10 200 Z','#5a6880')")
assert "L224 54 L246 60" in body
# the seal is gone (it sat on the art)
body=body.replace("    o+=ukSeal(382,232,.2);\n","")
# street furniture, drain channel, lantern spill, puddles
body=body.replace("    o+='<g class=\"ly3\">'+f+'</g>';",
 """    f+=downpipe(103,184,214)+downpipe(164,184,214)+downpipe(225,186,214)+downpipe(297,184,214)+downpipe(345,184,214)+crates(186,214)+bicycle(334,214);
    o+='<g class="ly3">'+f+'</g>';
    // wooden poles and the wires that cross every Japanese street, with service drops to the eaves
    o+='<g class="ly3">'+upole(46,214,66)+upole(206,214,68)+upole(388,214,64)+'</g>';
    o+='<g class="noedge">'+ln('M-10 152 Q18 156 46 150 Q126 158 206 148 Q298 157 388 152 Q400 153 410 154 M-10 156 Q20 160 46 155 Q126 163 206 153 Q298 162 388 157 M46 151 Q70 160 84 180 M206 149 Q230 162 244 184 M206 150 Q180 160 160 184 M388 152 Q370 162 356 184','#1d1f24',.45)+'</g>';""")
body=body.replace("    o+='<g class=\"ly3\">'+rc(-10,214,420,46,'#1b2028')+'</g>';",
 """    o+='<g class="ly3">'+rc(-10,214,420,46,'#1b2028')+'</g>';
    // the drain channel along the fronts, its grates
    var gr=''; for(var gx=-8;gx<410;gx+=10) gr+=rc(gx,214.6,7,1.8,'#2c3036');
    o+='<g class="noedge">'+rc(-10,214,420,3,'#5b5e63')+gr+'</g>';
    // puddles, holding the lights
    o+='<g class="noedge"><ellipse cx="128" cy="228" rx="26" ry="3.2" fill="#2d3644"/><ellipse cx="252" cy="239" rx="34" ry="3.6" fill="#2d3644"/><ellipse cx="58" cy="246" rx="20" ry="2.4" fill="#2d3644"/><ellipse cx="344" cy="231" rx="24" ry="2.8" fill="#2d3644"/>'
      +'<ellipse cx="124" cy="228" rx="9" ry="1.3" fill="#ffcf7a" opacity=".55"/><ellipse cx="248" cy="239" rx="12" ry="1.3" fill="#ffcf7a" opacity=".35"/><ellipse cx="340" cy="231" rx="7" ry="1" fill="#ffcf7a" opacity=".3"/></g>';""")
body=body.replace("    o+='<g class=\"fx noedge\">'+chochin(108,204)+chochin(160,204)+chochin(232,200)+chochin(292,200)",
 """    o+='<g class="noedge" style="mix-blend-mode:screen">'+ukGlow('lsp1',108,208,16,12,'#ff9a4a',.4)+ukGlow('lsp2',160,208,16,12,'#ff9a4a',.4)+ukGlow('lsp3',232,204,16,12,'#ff9a4a',.35)+ukGlow('lsp4',292,204,16,12,'#ff9a4a',.35)+'</g>';
    o+='<g class="fx noedge">'+chochin(108,204)+chochin(160,204)+chochin(232,200)+chochin(292,200)""")
# rain in depth: fine far rain, a few soft near streaks, splashes on the street
body=body.replace("    o+=ukRain(31,170,-40,420,-10,250,.08,80,'rgba(214,222,236,.38)',.45);",
 """    o+=ukRain(31,150,-40,420,-10,250,.08,60,'rgba(214,222,236,.26)',.32);
    o+=ukRain(37,16,-40,420,-30,200,.1,120,'rgba(226,232,242,.16)',1.9);  // no blur filter: an animated blur costs every frame
    var spl='', rs=tssR(77); for(var k=0;k<46;k++){ var sx=-8+rs()*416, sy=218+rs()*40; spl+='M'+(sx-1.4).toFixed(1)+' '+sy.toFixed(1)+' l1.4 -1.6 l1.4 1.6 '; }
    o+='<g class="noedge">'+ln(spl,'rgba(214,222,236,.45)',.4)+'</g>';""")
s=s[:a]+body+s[b:]
open('/tmp/sb/w.html','w').write(s); print('echigo ok')

# ============ splash fix (Echigo) + DEAD ANTS (scene 3) ============
s=open('/tmp/sb/w.html').read()
def once(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:90]); s=s.replace(a,b)
once("""    var spl='', rs=tssR(77); for(var k=0;k<46;k++){ var sx=-8+rs()*416, sy=218+rs()*40; spl+='M'+(sx-1.4).toFixed(1)+' '+sy.toFixed(1)+' l1.4 -1.6 l1.4 1.6 '; }
    o+='<g class="noedge">'+ln(spl,'rgba(214,222,236,.45)',.4)+'</g>';""",
"""    // rings where the rain lands in the puddles
    var spl='', rs=tssR(77); [[128,228,24],[252,239,32],[58,246,18],[344,231,22]].forEach(function(p){ for(var k=0;k<5;k++){ var sx=p[0]+(rs()-.5)*p[2]*1.4, sy=p[1]+(rs()-.5)*2; spl+='<ellipse cx="'+sx.toFixed(1)+'" cy="'+sy.toFixed(1)+'" rx="'+(1+rs()*1.6).toFixed(1)+'" ry="'+(.3+rs()*.3).toFixed(2)+'" fill="none" style="stroke:rgba(214,222,236,.4);stroke-width:.35"/>'; } });
    o+='<g class="noedge">'+spl+'</g>';""")
def repfn_last(name,new):
    global s
    a=s.rindex('  function '+name+'('); b=s.index('\n  }\n',a)+4; s=s[:a]+new+s[b:]
repfn_last('payphone',r'''  // v47: a NYNEX pedestal payphone of 1993: a steel post, a three-sided
  // stainless hood over the phone, the lit TELEPHONE panel on top, the
  // handset on its hook with the armoured cord
  function payphone(x,y){
    return rc(x-1.1,y-24,2.2,24,'#6f7880')+rc(x-4,y-1.4,8,1.4,'#56606a')
      + rc(x-5.8,y-44,11.6,19,'#b9c0c5')+rc(x-5.8,y-44,1.4,19,'#8f989f')+rc(x+4.4,y-44,1.4,19,'#8f989f')
      + '<g class="lit glow">'+lr(x-5.8,y-48.2,11.6,4)+'</g>'
      + '<g class="noedge"><text x="'+x+'" y="'+(y-45.2)+'" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="2.05" fill="#1e3a6e">PHONE</text>'
      + rc(x-4.4,y-41,8.8,12,'#6f7880')+rc(x-3.4,y-39.6,6.8,3.4,'#1f2a24')+rc(x-3,y-35,6,5,'#c9cfd3')
      + '<g fill="#2a2e33">'+[0,1,2].map(function(c){ return [0,1,2].map(function(r){ return '<rect x="'+(x-2.4+c*2)+'" y="'+(y-34.4+r*1.6)+'" width="1.2" height="1"/>'; }).join(''); }).join('')+'</g>'
      + rc(x-6.2,y-40,2,8,'#22252b',' rx=".9"')+ln('M'+(x-5.2)+' '+(y-32)+' q-1.4 4 1.6 6 q2 1 2.6 -1','#9aa2a8',.55)+'</g>';
  }
''')
a=s.index('  function busstop(x,y){'); b=s.index('\n  }\n',a)+4
s=s[:a]+r'''  // v47: the MBTA stop: a white panel on its pole, the black T roundel
  function busstop(x,y){
    return rc(x,y,2.4,56,'#4a5058')+rc(x-8,y,18,14,'#f3f0e8',' rx=".6"')
      + '<g class="noedge"><circle cx="'+(x+1.2)+'" cy="'+(y+7)+'" r="5" fill="#141414"/>'+rc(x-2.2,y+4,6.8,1.6,'#f3f0e8')+rc(x+.4,y+4,1.6,6.4,'#f3f0e8')+'</g>';
  }
'''+s[b:]
# the bus, lived in: seats and riders against the lit glass, a shadow on the road
a=s.index('  function mbtaBus(x,y){'); b=s.index('\n  }\n',a)
bus=s[a:b]
bus=bus.replace("    for(var wx=x+8;wx<x+w-24;wx+=11.4) o+=lr(wx,y+5.8,9.4,6.8);\n    o+='</g><g class=\"noedge\">';",
"""    for(var wx=x+8;wx<x+w-24;wx+=11.4) o+=lr(wx,y+5.8,9.4,6.8);
    o+='</g><g class="noedge">';
    // seat backs along the glass, and three riders going home
    var rr=tssR(39);
    for(var sx=x+9;sx<x+w-26;sx+=5.7) o+=rc(sx,y+10,2.6,2.8,'rgba(60,40,24,.55)',' rx=".6"');
    [x+22,x+47,x+71].forEach(function(px,i){ o+='<ellipse cx="'+px+'" cy="'+(y+8.6)+'" rx="1.6" ry="1.9" fill="rgba(40,28,20,.78)"/>'+rc(px-2.4,y+10.2,4.8,2.6,'rgba(40,28,20,.78)',' rx="1"'); });""")
assert 'riders' in bus
s=s[:a]+bus+s[b:]
once("    o+='<g class=\"ly3\">'+mbtaBus(232,157)","    o+='<g class=\"noedge\"><ellipse cx=\"290\" cy=\"183\" rx=\"62\" ry=\"2.6\" fill=\"rgba(0,0,0,.45)\"/></g>';\n    o+='<g class=\"ly3\">'+mbtaBus(232,157)")
# the road out of the cutting filter: straight rails, flat asphalt, sodium laid on it
once("    o+='<g class=\"ly3\">'+huntington()+'</g>';",
"""    o+='<g class="road">'+huntington()+'</g>';
    o+='<g class="noedge" filter="url(#dofMid)">'+[42,110,176,290,382].map(function(x,i){ return '<rect x="'+(x-3)+'" y="154" width="6" height="'+(i===2?26:20)+'" fill="#ffc76a" opacity="'+(i===2?.26:.16)+'"/>'; }).join('')+'</g>';""")
# a lamp over the two of them, whose light makes the pool the ant walks in
once("      +payphone(194,196)+payphone(207,196)+payphone(220,196)",
     "      +payphone(194,196)+payphone(207,196)+payphone(220,196)\n      +rc(186,112,2.4,86,'#4a5058')+rc(170,112,18,1.8,'#4a5058')+'<ellipse cx=\"168\" cy=\"113.6\" rx=\"6\" ry=\"2.4\" fill=\"#3e4e5d\"/><g class=\"lit glow\"><ellipse cx=\"168\" cy=\"115\" rx=\"5\" ry=\"1.4\"/></g>'")
once("    o+='<g class=\"fx noedge\">'\n      +'<ellipse cx=\"163\" cy=\"195\"","    o+='<g class=\"noedge\"><path d=\"M164 116 L140 196 L196 196 L172 116 Z\" fill=\"#ffcf7a\" opacity=\".07\"/></g>';\n    o+='<g class=\"fx noedge\">'\n      +'<ellipse cx=\"163\" cy=\"195\"")
# MassArt: the penthouse on the roof, blinds at different heights, the sills weeping
once("    o+=rc(x0,g-14,x1-x0,14,'#5d5a55')","    o+=rc(x0+14,top-12,40,10,'#7a766f')+rc(x0+20,top-18,16,6,'#6d6a64')+rc(x0+60,top-9,12,7,'#77736c');\n    var bl='', br2=skR(88); for(var by=top+6;by<g-16;by+=13) for(var bx=x0+3;bx<x1-6;bx+=9){ if(br2()<.35) bl+='<rect x=\"'+bx+'\" y=\"'+(by+2.6)+'\" width=\"6\" height=\"'+(2+br2()*5).toFixed(1)+'\" fill=\"#cfc6b0\" opacity=\".85\"/>'; }\n    o+='<g class=\"noedge\">'+bl+stains(x0,top+8,x1-x0,14,33)+'</g>';\n    o+=rc(x0,g-14,x1-x0,14,'#5d5a55')")
# the moon, a cut paper disc, and its glow
once("      return [{c:'<g>'+st+'</g>',v:0,far:1},{c:o,v:3,far:1}];",
     "      var mn='<defs><radialGradient id=\"mnG\"><stop offset=\"0\" stop-color=\"#f3ecd6\" stop-opacity=\".35\"/><stop offset=\"1\" stop-color=\"#f3ecd6\" stop-opacity=\"0\"/></radialGradient></defs><circle cx=\"'+skF(W*.74)+'\" cy=\"'+skF(H*.18)+'\" r=\"'+skF(S*.12)+'\" fill=\"url(#mnG)\"/>'+skG('sx1','<circle cx=\"'+skF(W*.74)+'\" cy=\"'+skF(H*.18)+'\" r=\"'+skF(S*.034)+'\" fill=\"#efe6cc\"/><circle cx=\"'+skF(W*.74-S*.01)+'\" cy=\"'+skF(H*.18-S*.006)+'\" r=\"'+skF(S*.009)+'\" fill=\"#ddd2b2\"/><circle cx=\"'+skF(W*.74+S*.012)+'\" cy=\"'+skF(H*.18+S*.01)+'\" r=\"'+skF(S*.006)+'\" fill=\"#ddd2b2\"/>');\n      return [{c:'<g>'+st+'</g>'+mn,v:0,far:1},{c:o,v:3,far:1}];")
# a road group: flat, no cutting filter; a trace of paper grain
once("#scenery .mass *{","#scenery .road{ filter:url(#dofMid); }\n#scenery .mass *{")
open('/tmp/sb/w.html','w').write(s); print('da ok')

# ============ G6 EVERY PIECE IS RAISED CARD: emboss the colour edges ============
s=open('/tmp/sb/w.html').read()
EMB='<feColorMatrix in="d" type="matrix" values=".33 .5 .17 0 0  .33 .5 .17 0 0  .33 .5 .17 0 0  0 0 0 1 0" result="lum"/><feConvolveMatrix in="lum" order="3" kernelMatrix="-1 -1 0  -1 0 1  0 1 1" divisor="1" bias=".5" preserveAlpha="true" kernelUnitLength="%s" result="emb"/><feComposite in="p2" in2="emb" operator="arithmetic" k1="0" k2="1" k3="%s" k4="-%s" result="p3"/><feComposite in="p3" in2="d" operator="in" result="p4"/>'
for fid,ku,k in [('card1','.7','.35'),('card2','.6','.55'),('card3','.55','.7')]:
    i=s.index('<filter id="%s"'%fid); j=s.index('</filter>',i); f=s[i:j]
    k2=f.rindex('<feMerge>')
    f=f[:k2]+EMB%(ku,k,str(round(float(k)/2,3)))+f[k2:].replace('<feMergeNode in="p2"/><feMergeNode in="dim"/>','<feMergeNode in="p4"/><feMergeNode in="dim"/>')
    assert 'p4"/><feMergeNode in="dim' in f
    s=s[:i]+f+s[j:]
# the white plaster was reading as a crumpled filter: ease the fibre relief on the near sheet
s=s.replace('<feDiffuseLighting in="bump" surfaceScale="1.1"','<feDiffuseLighting in="bump" surfaceScale=".6"')
open('/tmp/sb/w.html','w').write(s); print('emboss ok')

# ============ ROUND 3: the critic's ranked fixes ============
s=open('/tmp/sb/w.html').read()
def once(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:90]); s=s.replace(a,b)
def repfn(name,new,last=False):
    global s
    a=(s.rindex if last else s.index)('  function '+name+'('); b=s.index('\n  }\n',a)+4; s=s[:a]+new+s[b:]
# -- global: gentler fibre everywhere; no vector gloss on the balloon
for fid,v in [('card1','.8'),('card2','1.0'),('card3','.6')]:
    i=s.index('<filter id="%s"'%fid); j=s.index('</filter>',i); f=s[i:j]
    import re
    f=re.sub(r'<feDiffuseLighting in="bump" surfaceScale="[0-9.]+"','<feDiffuseLighting in="bump" surfaceScale="%s"'%{'card1':'.4','card2':'.45','card3':'.45'}[fid],f)
    s=s[:i]+f+s[j:]
a=s.index('<path d="M58 16 C40 26 30 46 29 66'); b=s.index('/>',a)+2; s=s[:a]+s[b:]
HELP=r'''  /* v47 ROUND 3 helpers. ao(): the dark where a thing meets the ground, the
     ambient occlusion a real photograph always has. */
  function ao(x0,x1,g,h,op,id){
    return '<defs><linearGradient id="'+id+'" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#0c0806" stop-opacity="'+(op||.4)+'"/><stop offset="1" stop-color="#0c0806" stop-opacity="0"/></linearGradient></defs><rect x="'+x0+'" y="'+(g-h)+'" width="'+(x1-x0)+'" height="'+h+'" fill="url(#'+id+')"/>';
  }
  // a persimmon in autumn: bare black branches, the fruit left hanging
  function kaki(x,g,h,seed){
    var r=tssR(seed||5), br='', fr='';
    (function grow(x0,y0,a,len,w,d){ var x1=x0+Math.cos(a)*len, y1=y0+Math.sin(a)*len, nx=-Math.sin(a), ny=Math.cos(a), w1=w*.66;
      br+='M'+(x0+nx*w/2).toFixed(2)+' '+(y0+ny*w/2).toFixed(2)+' L'+(x1+nx*w1/2).toFixed(2)+' '+(y1+ny*w1/2).toFixed(2)+' L'+(x1-nx*w1/2).toFixed(2)+' '+(y1-ny*w1/2).toFixed(2)+' L'+(x0-nx*w/2).toFixed(2)+' '+(y0-ny*w/2).toFixed(2)+' Z ';
      if(d>=5){ if(r()<.8) fr+='<circle cx="'+x1.toFixed(1)+'" cy="'+(y1+.8).toFixed(1)+'" r="'+(1.1+r()*.5).toFixed(2)+'" fill="'+(r()<.5?'#e2702a':'#d25a1e')+'"/>'; return; }
      if(d>=3 && r()<.5) fr+='<circle cx="'+x1.toFixed(1)+'" cy="'+(y1+.8).toFixed(1)+'" r="1.2" fill="#e2702a"/>';
      var n=r()<.3?3:2; for(var i=0;i<n;i++){ var sp=(24+r()*30)*Math.PI/180, side=n===2?(i?1:-1):(i-1); grow(x1,y1,a+side*sp+(r()-.5)*.4,len*(.74+(r()-.5)*.2),w1,d+1); } })(x,g,-Math.PI/2,h*.28,Math.max(.8,h*.07),1);
    return '<g class="noedge"><path d="'+br+'" fill="#231a15"/>'+fr+'</g>';
  }
  // a wooden utility pole as it is: two crossarms, glass insulators, a transformer can, the cobrahead on its arm
  function pole(x,y,h,armL,lit){
    var hx=x+4+armL+3, o=rc(x,y,4,h,'#6d5a44')+rc(x+.6,y,.9,h,'rgba(255,240,210,.18)');
    o+=rc(x-9,y+4,22,2.2,'#5a4836')+rc(x-7,y+10,18,2,'#5a4836');
    o+='<g class="noedge">'+[-8,-4,7,11].map(function(d){ return rc(x+d,y+2.2,1.4,1.8,'#9fc2c9'); }).join('')+[-6,9].map(function(d){ return rc(x+d,y+8.2,1.4,1.8,'#9fc2c9'); }).join('')+'</g>';
    o+=rc(x+4.4,y+13,5,8,'#8e979b',' rx="1.6"')+'<g class="noedge">'+rc(x+4.4,y+13,5,1.2,'#6f777b')+'</g>';
    o+=rc(x+4,y+24,armL,1.8,'#56606a')+'<path d="M'+(hx-7)+' '+(y+25)+' q7 -3.6 14 0 l-1 2 q-6 1.6 -12 0 z" fill="#56606a"/>';
    if(lit) o+='<g class="lit glow"><ellipse cx="'+hx+'" cy="'+(y+27.4)+'" rx="5.4" ry="1.6"/></g>';
    return o;
  }
  function hydrant(x,g){ return rc(x-3,g-2,6,2,'#b8452e')+rc(x-2.2,g-10,4.4,8,'#c9502e',' rx=".8"')+'<path d="M'+(x-2.8)+' '+(g-10)+' q2.8 -3.4 5.6 0 z" fill="#b8452e"/>'+rc(x-4,g-7.4,8,1.8,'#b8452e',' rx=".8"')+'<g class="noedge">'+rc(x-.6,g-12.4,1.2,1.4,'#8d3221')+'</g>'; }
  function usMailbox(x,g){ return rc(x-4.6,g-2,1.2,2,'#2c3e63')+rc(x+3.4,g-2,1.2,2,'#2c3e63')+'<path d="M'+(x-5.4)+' '+(g-2)+' V'+(g-12)+' q5.4 -4.2 10.8 0 V'+(g-2)+' Z" fill="#2f4a8a"/>'+'<g class="noedge">'+rc(x-3.2,g-11,6.4,1.2,'#1f3366')+rc(x-2,g-8,4,2.2,'#e8e2d2')+'</g>'; }
  function newsBox(x,g,col){ return rc(x,g-12,8,12,col)+'<g class="noedge">'+rc(x+1,g-11,6,5,'rgba(230,236,240,.7)')+rc(x+1.4,g-10.4,5.2,.8,'#2a2e33')+rc(x+1.4,g-9,5.2,.5,'#2a2e33')+rc(x,g-12,8,.8,'rgba(0,0,0,.25)')+'</g>'; }
  function trashCan(x,g){ return '<path d="M'+(x-4)+' '+(g-12)+' h8 l-1 12 h-6 z" fill="#3d4a3e"/>'+'<g class="noedge">'+ln('M'+(x-3.4)+' '+(g-9)+' h6.8 M'+(x-3)+' '+(g-6)+' h6 M'+(x-2.6)+' '+(g-3)+' h5.2','#56685a',.5)+rc(x-4.4,g-12.8,8.8,1,'#56685a')+'</g>'; }
  function geese(x,y,n,s){ var o=''; for(var i=0;i<n;i++){ var k=i-(n-1)/2, gx=x+Math.abs(k)*s*2.2, gy=y+k*s*1.4; o+=ln('M'+(gx-s)+' '+(gy-s*.5)+' l'+s+' '+(s*.5)+' l'+s+' '+(-s*.5),'#4a3426',.7); } return '<g class="noedge">'+o+'</g>'; }
'''
i=s.index('  var SCENERY=[\n'); s=s[:i]+HELP+s[i:]
# the old single-crossarm pole is replaced (function declarations: the later one wins)

# -- ECHIGO: gangi arcade along the fronts, a persimmon where the roof blob was, AO, phone frame keeps the sign
a=s.index('  function echigoTown(){'); b=s.index('\n  }\n',a); body=s[a:b]
body=body.replace("[[122,176,40],","[[210,170,30],".replace("[[210,170,30],","[[-9999,0,0],")) if False else body
body=body.replace("mp+=momiji(t[0],t[1],t[2],mr);","mp+=(t[0]===122?kaki(122,172,44,9):momiji(t[0],t[1],t[2],mr));")
assert "kaki(122" in body
body=body.replace("""    o+='<g class="ly3">'+f+'</g>';""","""    o+='<g class="ly3">'+f+'</g>';
    // the gangi: the covered walkway snow country builds along its shop fronts, a shed roof on posts
    var gp=''; for(var gx=-4;gx<410;gx+=28) gp+=rc(gx,198,1.8,16,'#3a2c20');
    o+='<g class="ly3">'+rc(-10,195,420,3.4,'#3d3f46')+rc(-10,198.4,420,1.2,'#2a2019')+gp+'</g>'+'<g class="noedge">'+ao(-10,420,206,8,.32,'aoG').replace('y="198"','y="198"')+'</g>';
    o+='<g class="noedge">'+ao(-10,420,214,6,.45,'aoE')+'</g>';""")
s=s[:a]+body+s[b:]
once("    if(pi===0){ sv.setAttribute('viewBox','0 0 400 250'); sv.setAttribute('preserveAspectRatio','xMidYMax slice'); return; }",
     "    if(pi===0){ var rb=sv.getBoundingClientRect(), aa=rb.width/Math.max(1,rb.height);\n      if(aa<1.6){ var vw0=250*aa, xo=Math.max(0,Math.min(400-vw0,80)); sv.setAttribute('viewBox',xo.toFixed(1)+' 0 '+vw0.toFixed(1)+' 250'); sv.setAttribute('preserveAspectRatio','xMinYMax slice'); }\n      else { sv.setAttribute('viewBox','0 0 400 250'); sv.setAttribute('preserveAspectRatio','xMidYMax slice'); }\n      var bl0=$('balloon'); if(bl0) bl0.style.left=''; return; }")

# -- BLACK SPOTS
once("  function sunShadow(x,g,h,k){ k=k||1; return '<path d=\"M'+(x-1.5)+' '+g+' l'+(-h*.7*k).toFixed(1)+' '+(h*.12*k).toFixed(1)+' l3 .6 L'+(x+1.5)+' '+g+' Z\" fill=\"rgba(30,34,52,.22)\"/>'; }",
     "  function sunShadow(x,g,h,k){ k=k||1; return '<path d=\"M'+(x-2)+' '+g+' l'+(-h*1.1*k).toFixed(1)+' '+(h*.14*k).toFixed(1)+' l4 .8 L'+(x+2)+' '+g+' Z\" fill=\"rgba(30,34,52,.36)\"/>'; }")
once("figure(118,183,23,{felt:'orange'","figure(104,184,23,{felt:'orange'")
once("sunShadow(118,183.4,23)","sunShadow(104,184.4,23)")
once("ln('M-124 174.2 h648 M-124 176.2 h648','#d9b53c',.8)","ln('M-124 174.2 H28 M-124 176.2 H28 M158 174.2 H524 M158 176.2 H524','#d9b53c',.8)")
DW=r'''  function dontWalk(x,y){ return '<g class="noedge">'+rc(x-2,y-2,18,15,'var(--p-char)')+rc(x-1,y-1,16,13,'#1b1c21')+'</g>'
     +'<g><text x="'+(x+7)+'" y="'+(y+5)+'" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="4.6" fill="#ff9a3d">DONT</text><text x="'+(x+7)+'" y="'+(y+10.6)+'" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="4.6" fill="#ff9a3d">WALK</text></g>'; }
'''
a=s.index('  function dontWalk('); b=s.index("'; }\n",a)+5; s=s[:a]+DW+s[b:]
# a street with its things: parked cars, a hydrant, a mailbox, a news box; the far sidewalk in the buildings' shade
once("     ambulance(262,136)+","     ambulance(262,136)+'<g transform=\"translate(338 141) scale(.62)\">'+sedan(0,0,'#6b7f5e','#55663f')+'</g>'+'<g transform=\"translate(420 141) scale(.62)\">'+sedan(0,0,'#c9b48a','#a8946a')+'</g>'+'<g class=\"noedge\">'+ao(-124,524,150,6,.35,'aoB')+'</g>'+")
once("     curb(-124,188,648,5)+rc(-124,193,648,7,'var(--p-bone-d)')+","     curb(-124,188,648,5)+rc(-124,193,648,7,'var(--p-bone-d)')+hydrant(14,198)+usMailbox(300,198)+newsBox(-30,198,'#2f5f8a')+newsBox(-20,198,'#c9432e')+'<g class=\"noedge\">'+sunShadow(14,198,12)+sunShadow(300,198,12)+sunShadow(-26,198,12,1.2)+'</g>'+")
# the towers get their rooftop plant and spandrel bands
once("    return o+'<g class=\"noedge\">'+ln(sl,'rgba(20,14,10,.18)',.5)+g+'</g>';\n  }",
     "    o+=rc(x+w*.2,top-7,w*.38,7,side)+rc(x+w*.26,top-11,w*.16,4,'var(--p-char-d)')+rc(x+w*.66,top-4,w*.14,4,side);\n    return o+'<g class=\"noedge\">'+ln(sl,'rgba(20,14,10,.18)',.5)+g+'</g>';\n  }")
# torn tissue clouds, layered and translucent, lit from behind
once("      var near=skRow(rnd,W,S,H*.2,.34,2,col,'sx1'), far=skRow(rnd,W,S,H*.36,.18,3,col,'sx0','.8');\n      return [{c:far,v:3,far:1},{c:near,v:6,far:1}];",
     """      var tis=function(y,n,sz,op){ var g=''; for(var k=0;k<n;k++){ var cx=W*(k+.5)/n+(rnd()-.5)*W/n*.5, cy=y+(rnd()-.5)*H*.04, w=S*sz*(.8+rnd()*.5);
          for(var j=0;j<4;j++) g+=skBlob(rnd,cx+(rnd()-.5)*w*.5,cy+(rnd()-.5)*w*.08,w*(.35+rnd()*.25),w*(.08+rnd()*.05),j%2?'#f7f5ee':'#e3e9ee',op); } return g; };
      return [{c:skG('sx0',tis(H*.34,3,.3,'.55')),v:3,far:1},{c:skG('sx1',tis(H*.18,2,.5,'.62')),v:6,far:1}];""")

# -- PEACH
once("  function goldShadow(x,g,h,w){ w=w||3; return '<path d=\"M'+(x-w/2)+' '+g+' l'+(h*1.9).toFixed(1)+' '+(h*.1).toFixed(1)+' h'+(w*.9)+' L'+(x+w/2)+' '+g+' Z\" fill=\"rgba(62,38,22,.24)\"/>'; }",
     "  function goldShadow(x,g,h,w){ w=w||3; return '<path d=\"M'+(x-w/2)+' '+g+' l'+(h*2.2).toFixed(1)+' '+(h*.1).toFixed(1)+' h'+(w*.9)+' L'+(x+w/2)+' '+g+' Z\" fill=\"rgba(62,38,22,.34)\"/>'; }")
repfn('cobbler',r'''  // v47: a glass baking dish with a lattice crust, on a folded cloth, held in both hands
  function cobbler(x,y){
    return rc(x-7,y+.6,20,2.6,'#d8d2c4',' rx=".8"')+'<ellipse cx="'+(x+3)+'" cy="'+(y+1.2)+'" rx="10.4" ry="3.2" fill="rgba(210,228,232,.85)"/>'
      + '<ellipse cx="'+(x+3)+'" cy="'+y+'" rx="9" ry="2.6" fill="#d9a24a"/>'
      + ln('M'+(x-4)+' '+(y-1.2)+' l14 2.4 M'+(x-5)+' '+(y+.4)+' l14 2 M'+(x-2)+' '+(y-2)+' l-2 4 M'+(x+3)+' '+(y-2.4)+' l-2 4.6 M'+(x+8)+' '+(y-2)+' l-2 4.2','#b06a2a',.8)
      + '<ellipse cx="'+(x+1)+'" cy="'+(y-.6)+'" rx="2" ry=".7" fill="#e8b25c"/>';
  }
''')
once("     bulkhead(70,184)+","     bulkhead(20,182)+")
once("     '<g class=\"noedge\">'+goldShadow(122,197,34,8)","     '<g class=\"noedge\"><path d=\"M116 178 l72 4 h40 l-14 -4 Z\" fill=\"rgba(62,38,22,.18)\"/><path d=\"M374 178 l60 4 h30 l-10 -4 Z\" fill=\"rgba(62,38,22,.16)\"/>'+ao(-124,524,178,5,.35,'aoP').replace('<defs>','').replace('</defs>','')+'</g>'+\n     '<g class=\"noedge\">'+goldShadow(122,197,34,8)")
# the sun going down behind the left hill, and geese, and wires
once("   '<g class=\"ly1\">'+P('M-124 20 Q20 0 150 -4 L232 -40",
     "   '<g class=\"noedge\"><defs><radialGradient id=\"sunG\"><stop offset=\"0\" stop-color=\"#fff1c8\" stop-opacity=\".95\"/><stop offset=\".25\" stop-color=\"#ffd48a\" stop-opacity=\".55\"/><stop offset=\"1\" stop-color=\"#ffb86a\" stop-opacity=\"0\"/></radialGradient></defs><circle cx=\"-18\" cy=\"8\" r=\"70\" fill=\"url(#sunG)\"/><circle cx=\"-18\" cy=\"8\" r=\"11\" fill=\"#fff3d4\"/></g>'+geese(150,-70,7,2.6)+\n   '<g class=\"ly1\">'+P('M-124 20 Q20 0 150 -4 L232 -40")
once("     tree(380,150,19,'var(--p-moss)','var(--p-moss-d)')+","     tree(380,150,19,'var(--p-moss)','var(--p-moss-d)')+pole(236,112,66,0,false)+pole(-30,112,66,0,false)+'<g class=\"noedge\">'+ln('M-130 118 Q-80 124 -28 117 Q100 126 238 117 Q380 126 530 118 M-130 122 Q-80 128 -28 121 Q100 130 238 121 Q380 130 530 122','#2f2620',.4)+'</g>'+")
# clapboard on the New England walls
once("  function colonial(x,y,w,d,wall,wallS,roof,roofS){\n    var o=eaves(x,y,w,44,18,d,wall,wallS,roof,roofS,4);",
     "  function clap(x,y,w,h){ var d=''; for(var yy=y+2.2;yy<y+h;yy+=2.2) d+='M'+x+' '+yy.toFixed(1)+' h'+w+' '; return '<g class=\"noedge\">'+ln(d,'rgba(40,28,18,.14)',.35)+'</g>'; }\n  function colonial(x,y,w,d,wall,wallS,roof,roofS){\n    var o=eaves(x,y,w,44,18,d,wall,wallS,roof,roofS,4)+clap(x,y,w,44);")
once("  function cape(x,y,w,d,wall,wallS,roof,roofS){\n    var o=eaves(x,y,w,26,26,d,wall,wallS,roof,roofS,4);","  function cape(x,y,w,d,wall,wallS,roof,roofS){\n    var o=eaves(x,y,w,26,26,d,wall,wallS,roof,roofS,4)+clap(x,y,w,26);")
# the hills in layered card, sharper, with haze between rather than blur
once("#scenery .mass *{","#scenery .ly1.crisp{ filter:url(#card1) url(#dofMid) saturate(.9); }\n#scenery .mass *{")
a=s.index("   /* v42 THE HILL."); b=s.index("     P('M-124 126 L-64 114 L0 132",a)
seg=s[a:b].replace("'<g class=\"ly1\">'","'<g class=\"ly1 crisp\">'")
s=s[:a]+seg+s[b:]

# -- DEAD ANTS
once("    for(var x=-110;x<530;x+=74) cp+=rc(x,112,1.4,49,'#3e4e5d')+rc(x-6,114,13,1,'#3e4e5d');","    [-100,66,230,394].forEach(function(x){ cp+=rc(x,112,1.4,49,'#3e4e5d')+rc(x-6,114,13,1,'#3e4e5d'); });")
once("'<g class=\"crawl antnow\"><g transform=\"translate(163 195.2) scale(.34) translate(-163 -195.2)\">'","'<g class=\"crawl antnow\"><g transform=\"translate(163 195.2) scale(.48) translate(-163 -195.2)\">'")
once("<path d=\"M164 116 L140 196 L196 196 L172 116 Z\" fill=\"#ffcf7a\" opacity=\".07\"/>","<path d=\"M164 116 L132 197 L206 197 L172 116 Z\" fill=\"#ffcf7a\" opacity=\".12\"/><ellipse cx=\"170\" cy=\"197\" rx=\"40\" ry=\"4\" fill=\"#ffc86a\" opacity=\".22\"/><rect x=\"188\" y=\"150\" width=\"38\" height=\"44\" fill=\"#ffcf7a\" opacity=\".08\"/>")
once("    o+='<g class=\"ly2\">'+pole(24,86,64,-22,true)+pole(400,86,64,-22,true)+'</g>';",
     "    o+='<g class=\"ly2\">'+pole(24,86,64,-22,true)+pole(400,86,64,-22,true)+newsBox(40,150,'#2f5f8a')+newsBox(49,150,'#d8c24a')+'<g transform=\"translate(250 139) scale(.6)\">'+sedan(0,0,'#5a4a6a','#44385a')+'</g>'+'</g>'+'<g class=\"noedge\">'+ao(-130,530,150,5,.4,'aoD')+'</g>';")
once("      +payphone(194,196)+payphone(207,196)+payphone(220,196)","      +trashCan(140,198)+payphone(194,196)+payphone(207,196)+payphone(220,196)")
once("    o+='<g class=\"noedge\"><ellipse cx=\"290\" cy=\"183\" rx=\"62\" ry=\"2.6\" fill=\"rgba(0,0,0,.45)\"/></g>';","    o+='<g class=\"noedge\"><ellipse cx=\"290\" cy=\"183\" rx=\"62\" ry=\"2.6\" fill=\"rgba(0,0,0,.45)\"/><path d=\"M348 176 L420 170 L420 184 L348 180 Z\" fill=\"#fff2c0\" opacity=\".1\"/></g>';")
open('/tmp/sb/w.html','w').write(s); print('round3 ok')

# ============ ROUND 4: one light per scene, and the ranked fixes ============
s=open('/tmp/sb/w.html').read()
def once(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:90]); s=s.replace(a,b)
# -- the light rig: each scene sets where its key light is, and every card layer's cast shadow and cut-edge light follow it
once("  function loadPiece(i){","""  /* v47 THE LIGHT RIG. One key light per scene, set by the story, and every
     paper layer's cast shadows and lit cut edges follow it.
       0 Echigo: lanterns and shop light low in front, rain-soft, short shadows up and back
       1 Black Spots: morning sun high to the upper right, shadows down to the left
       2 Peach Cobbler: the sun low on the left, long shadows out to the right
       3 Dead Ants: sodium lamps overhead, short hard shadows straight down */
  var RIG=[{x:.6,y:.9,k:1,o:.5},{x:-1.4,y:1.4,k:1.3,o:.55},{x:2.6,y:.7,k:2.2,o:.5},{x:.3,y:1.6,k:1,o:.6}];
  function lightRig(p){
    var R=RIG[p]; if(!R) return;
    ['card1','card2','card3'].forEach(function(id,li){
      var f=document.getElementById(id); if(!f) return;
      var offs=f.querySelectorAll('feOffset'), sc=[.6,1,1.4][li];
      // [0]=near shadow, [1]=long shadow, [2]=rim light, [3]=rim shade (order they appear in the filter)
      if(offs[0]){ offs[0].setAttribute('dx',(R.x*sc).toFixed(2)); offs[0].setAttribute('dy',(R.y*sc).toFixed(2)); }
      if(offs[1]){ offs[1].setAttribute('dx',(R.x*sc*2.4*R.k).toFixed(2)); offs[1].setAttribute('dy',(R.y*sc*2.8).toFixed(2)); }
      var n=Math.hypot(R.x,R.y)||1;
      if(offs[2]){ offs[2].setAttribute('dx',(R.x/n*.8).toFixed(2)); offs[2].setAttribute('dy',(R.y/n*.8).toFixed(2)); }
      if(offs[3]){ offs[3].setAttribute('dx',(-R.x/n*.6).toFixed(2)); offs[3].setAttribute('dy',(-R.y/n*.6).toFixed(2)); }
      var fl=f.querySelectorAll('feFlood'); if(fl[0]) fl[0].setAttribute('flood-opacity',R.o);
    });
  }
  function loadPiece(i){""")
once("    $('sceneLayers').innerHTML=SCENERY[pi];","    $('sceneLayers').innerHTML=SCENERY[pi];\n    lightRig(pi);")

# -- ECHIGO: rain shows where it crosses light; softer figure bases; snow-stop rails; stronger arcade shade; the lean-to reads
once("    o+=ukRain(31,150,-40,420,-10,250,.08,60,'rgba(214,222,236,.26)',.32);",
"""    o+=ukRain(31,150,-40,420,-10,250,.08,60,'rgba(214,222,236,.12)',.3);
    // bright only where it crosses the lanterns and the shop window
    o+='<defs><mask id="rainLit"><rect x="-20" y="-20" width="440" height="290" fill="#000"/>'+[[128,204,40],[108,204,22],[160,204,22],[232,200,22],[292,200,22],[248,206,30]].map(function(p){ return '<ellipse cx="'+p[0]+'" cy="'+p[1]+'" rx="'+p[2]+'" ry="'+(p[2]*1.3)+'" fill="url(#rlG)"/>'; }).join('')+'</mask><radialGradient id="rlG"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/></radialGradient></defs>';
    o+='<g mask="url(#rainLit)">'+ukRain(43,260,-40,420,120,250,.08,40,'rgba(255,226,170,.75)',.4).replace('noedge urain','noedge')+'</g>';""")
once("    o+='<ellipse cx=\"'+x+'\" cy=\"'+y+'\" rx=\"'+(s*.34)+'\" ry=\"1.8\" fill=\"rgba(18,14,10,.32)\"/>';",
     "    o+='<ellipse cx=\"'+x+'\" cy=\"'+(y+.4)+'\" rx=\"'+(s*.3)+'\" ry=\"1.1\" fill=\"rgba(18,14,10,.22)\"/><rect x=\"'+(x-s*.16)+'\" y=\"'+(y+.6)+'\" width=\"'+(s*.32)+'\" height=\"'+(s*.5)+'\" fill=\"'+robe+'\" opacity=\".16\"/>';")
once("    return P(d,tileTone())+ukClip(d,kawara(x-e,y-rh,x+w+e,y+1))+'<g class=\"noedge\">'+rc(x-e,y,w+2*e,1.6,UK.tileD)+'</g>'+ridge(x-e+3,x+w+e-3,y-rh,UK.tileD);",
     "    return P(d,tileTone())+ukClip(d,kawara(x-e,y-rh,x+w+e,y+1))+'<g class=\"noedge\">'+rc(x-e,y,w+2*e,1.6,UK.tileD)+ln('M'+(x-e+2)+' '+(y-rh*.28)+' H'+(x+w+e-2),'#8b929a',.5)+ln((function(){ var q=''; for(var sx=x-e+3;sx<x+w+e-2;sx+=4) q+='M'+sx.toFixed(1)+' '+(y-rh*.28)+' v1.6 '; return q; })(),'#8b929a',.35)+'</g>'+ridge(x-e+3,x+w+e-3,y-rh,UK.tileD);")
# kawara courses: hand-laid, not a grid
once("    for(var x=x0;x<x1;x+=(pitch||2)) v+='M'+x.toFixed(1)+' '+y0.toFixed(1)+' V'+y1.toFixed(1)+' ';\n    for(var y=y0+2.2;y<y1;y+=2.6) h+='M'+x0.toFixed(1)+' '+y.toFixed(1)+' H'+x1.toFixed(1)+' ';\n    return ln(v,UK.tileD,.7,.6)+ln(h,UK.tileL,.45,.45);",
     "    var kr=tssR(Math.round(x0*5+y0*3)+2), sh='';\n    for(var x=x0;x<x1;x+=(pitch||2)*(.85+kr()*.3)) v+='M'+x.toFixed(1)+' '+y0.toFixed(1)+' V'+y1.toFixed(1)+' ';\n    for(var y=y0+2.2;y<y1;y+=2.4+kr()*.5){ h+='M'+x0.toFixed(1)+' '+y.toFixed(1)+' H'+x1.toFixed(1)+' '; sh+='M'+x0.toFixed(1)+' '+(y+.6).toFixed(1)+' H'+x1.toFixed(1)+' '; }\n    return ln(v,UK.tileD,.6,.5)+ln(sh,'rgba(10,10,14,.35)',.7)+ln(h,UK.tileL,.4,.5);")
once("    o+='<g class=\"ly3\">'+rc(-10,195,420,3.4,'#3d3f46')+rc(-10,198.4,420,1.2,'#2a2019')+gp+'</g>'",
     "    o+='<g class=\"noedge\"><rect x=\"-10\" y=\"198\" width=\"420\" height=\"16\" fill=\"rgba(10,8,6,.22)\"/></g>'+'<g class=\"ly3\">'+rc(-10,194,420,4.4,'#3d3f46')+rc(-10,198.4,420,1.4,'#2a2019')+gp+'</g>'")
once("    var d='M'+(x-e)+' '+(y+1)+' L'+(x+w+e)+' '+(y-rise-3)+' L'+(x+w+e)+' '+(y-rise+2.4)+' L'+(x-e)+' '+(y+6.4)+' Z';\n    return o+P(d,f)",
     "    var d='M'+(x-e)+' '+(y+1)+' L'+(x+w+e)+' '+(y-rise-3)+' L'+(x+w+e)+' '+(y-rise+2.4)+' L'+(x-e)+' '+(y+6.4)+' Z';\n    o+=rc(x+w,y-rise-2,e+.6,rise+2,fD)+rc(x-e-.6,y,e+.6,6.4,'var(--p-white-d)');\n    return o+P(d,f)")

# -- BLACK SPOTS: faces toward the sun are lit; the glow moves off the tag; wheels sit on the road
once("--sky-light:radial-gradient(circle at 80% 15%,","--sky-light:radial-gradient(circle at 70% 22%,")
a=s.index("   /* 1, BLACK SPOTS"); b=s.index("   /* 2, PEACH COBBLER",a)
seg=s[a:b]
import re
def litside(m):
    face=m.group(2); return m.group(1)+"'"+face+"','color-mix(in srgb, "+face+" 72%, #fff2d4)'"
seg=re.sub(r"(tower\([^']*)'(var\(--p-[a-z-]+\))','var\(--p-[a-z-]+\)'",litside,seg)
seg=seg.replace("'<g transform=\"translate(338 141) scale(.62)\">'","'<g class=\"noedge\"><ellipse cx=\"360\" cy=\"154\" rx=\"24\" ry=\"1.6\" fill=\"rgba(0,0,0,.35)\"/><ellipse cx=\"442\" cy=\"154\" rx=\"24\" ry=\"1.6\" fill=\"rgba(0,0,0,.35)\"/><ellipse cx=\"294\" cy=\"151.6\" rx=\"32\" ry=\"1.8\" fill=\"rgba(0,0,0,.38)\"/></g>'+'<g transform=\"translate(338 141) scale(.62)\">'")
s=s[:a]+seg+s[b:]

# -- PEACH: untangle the car, the bulkhead and the bed; fields as cut shapes with walls, no seam
once("     bulkhead(20,182)+","     bulkhead(88,182)+")
once("     '<g class=\"noedge\" transform=\"translate(40 0)\">'","     '<g class=\"noedge\" transform=\"translate(22 0)\">'")
once("     grill(98,196)+","     grill(112,199)+")
once("P('M150 76 Q230 62 300 56 L330 84 Q250 92 170 98 Z','#a49152')+P('M-60 88 Q20 70 90 72 L110 100 Q30 104 -40 110 Z','#9c8f58')+P('M340 70 Q420 52 500 60 L510 90 Q420 92 350 98 Z','#a9965a')+",
     "P('M120 88 Q220 70 320 66 Q420 62 524 60 L524 92 Q420 94 320 98 Q220 102 120 108 Z','#a49152')+P('M-124 96 Q-20 80 110 84 L120 108 Q0 112 -124 118 Z','#9c8f58')+woodland(-130,530,84,96,['#6a6a3e','#77764a','#a19a60'],71)+'<g class=\"noedge\">'+ln('M-124 97 Q-20 81 110 85 M120 89 Q220 71 320 67 Q420 63 524 61','#8a8166',1.1,.9)+'</g>'+")
# -- DEAD ANTS: the lamp's light behind the people, not over them; far windows are windows; neon on Sparr's band
a=s.index("    o+='<g class=\"noedge\"><path d=\"M164 116 L132 197"); b=s.index("\n",a)+1
cone=s[a:b]; s=s[:a]+s[b:]
once("    o+='<g class=\"ly3\">'+mbtaBus(232,157)",cone+"    o+='<g class=\"ly3\">'+mbtaBus(232,157)")
once("       return t+'<g class=\"lit glow\" opacity=\".85\">'+L+'</g>'; })()+","       return t+'<g class=\"lit\" opacity=\".8\">'+L+'</g>'; })()+")
once("     '<g class=\"lit glow\" opacity=\".7\">'+win(380,90,1,1,7,9,0,0)","     '<g class=\"lit\" opacity=\".7\">'+win(380,90,1,1,7,9,0,0)")
once("    var sb=g-32, w=x1-x0-6;\n    o+=rc(x0,sb,w,7,'var(--p-verm)');","    var sb=g-32, w=x1-x0-6;\n    o+=rc(x0,sb,w,7,'var(--p-verm)')+'<g class=\"noedge\"><rect x=\"'+(x0+8)+'\" y=\"'+(sb-1.4)+'\" width=\"'+(w-16)+'\" height=\"9.8\" rx=\"3\" fill=\"#ff6a4a\" opacity=\".16\"/></g>';")
open('/tmp/sb/w.html','w').write(s); print('round4 ok')

# ============ ROUND 5: exposure — light falls off across the frame ============
s=open('/tmp/sb/w.html').read()
def once(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:90]); s=s.replace(a,b)
GR=r'''  /* v47 EXPOSURE. A photograph of a lit set is not evenly exposed. At night
     the frame falls to dark between the lights and each light punches a warm
     hole; by day the side toward the sun runs warm and bright and the far side
     cool. nightGrade() darkens everything but the lights; dayGrade() washes. */
  function nightGrade(id,x0,y0,w,h,dark,op,lights){
    var m='<defs><radialGradient id="'+id+'h"><stop offset="0" stop-color="#000"/><stop offset=".55" stop-color="#000" stop-opacity=".7"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>'
      +'<mask id="'+id+'m"><rect x="'+x0+'" y="'+y0+'" width="'+w+'" height="'+h+'" fill="#fff"/>'+lights.map(function(L){ return '<ellipse cx="'+L[0]+'" cy="'+L[1]+'" rx="'+L[2]+'" ry="'+(L[3]||L[2])+'" fill="url(#'+id+'h)"/>'; }).join('')+'</mask></defs>';
    var glow=lights.map(function(L){ return L[4]?'<ellipse cx="'+L[0]+'" cy="'+L[1]+'" rx="'+(L[2]*.7)+'" ry="'+((L[3]||L[2])*.7)+'" fill="url(#'+id+'w)"/>':''; }).join('');
    return '<g class="noedge">'+m+'<rect x="'+x0+'" y="'+y0+'" width="'+w+'" height="'+h+'" fill="'+dark+'" opacity="'+op+'" mask="url(#'+id+'m)"/>'
      +'<defs><radialGradient id="'+id+'w"><stop offset="0" stop-color="#ffc56a" stop-opacity=".28"/><stop offset="1" stop-color="#ffc56a" stop-opacity="0"/></radialGradient></defs><g style="mix-blend-mode:screen">'+glow+'</g></g>';
  }
  function dayGrade(id,x0,y0,w,h,warm,cool,ang){
    return '<g class="noedge"><defs><linearGradient id="'+id+'" x1="'+(ang>0?0:1)+'" y1="0" x2="'+(ang>0?1:0)+'" y2=".4"><stop offset="0" stop-color="'+warm+'" stop-opacity=".22"/><stop offset=".55" stop-color="'+warm+'" stop-opacity="0"/><stop offset="1" stop-color="'+cool+'" stop-opacity=".2"/></linearGradient></defs><rect x="'+x0+'" y="'+y0+'" width="'+w+'" height="'+h+'" fill="url(#'+id+')" style="mix-blend-mode:soft-light"/></g>';
  }
'''
i=s.index('  var SCENERY=[\n'); s=s[:i]+GR+s[i:]
# Echigo: lights are the shop, the lanterns, the lit windows' spill, the inn
once("    o+='<g class=\"noedge keylight\">'+ukGlow('kl0',128,206,60,34,'#ffd58a',.5)+'</g>';",
     "    o+=nightGrade('ngE',-10,-10,420,270,'#0b1020',.42,[[128,208,56,30,1],[108,204,22,18,1],[160,204,22,18,1],[232,200,26,20,1],[292,200,24,18,1],[250,206,40,20,0],[372,200,30,18,0],[20,200,30,18,0],[214,196,20,14,0]]);\n    o+='<g class=\"noedge keylight\">'+ukGlow('kl0',128,206,60,34,'#ffd58a',.5)+'</g>';")
# Dead Ants: Sparr's windows, the lamp over the two, the bus, the lobby, the corner lamps
once("    o+='<g class=\"fx noedge\">'\n      +'<ellipse cx=\"163\" cy=\"195\"",
     "    o+=nightGrade('ngD',-140,-80,680,290,'#070a18',.34,[[0,134,74,26,1],[170,190,46,26,1],[168,118,14,10,1],[290,168,70,18,1],[187,140,40,14,0],[40,146,28,14,1],[384,146,28,14,1],[-104,140,28,12,0],[300,140,60,26,0]]);\n    o+='<g class=\"fx noedge\">'\n      +'<ellipse cx=\"163\" cy=\"195\"")
# Black Spots: warm from the upper right, cool at the lower left
once("     '<g>'+pigeon(250,199,[16,0,40,-13.3])","     dayGrade('dgB',-130,-80,660,290,'#fff0c8','#5a6c90',-1)+\n     '<g>'+pigeon(250,199,[16,0,40,-13.3])")
# Peach: gold from the left, the right falling to lilac shade
once("     '<g id=\"hawk\" transform=\"translate(87.9 116)\">'+hawkPerched()+'</g></g>',","     '<g id=\"hawk\" transform=\"translate(87.9 116)\">'+hawkPerched()+'</g>'+dayGrade('dgP',-130,-80,660,290,'#ffcf7a','#5a4a78',1)+'</g>',")
open('/tmp/sb/w.html','w').write(s); print('round5 ok')

# ============ ROUND 5 BUG FIXES ============
s=open('/tmp/sb/w.html').read()
def once(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:90]); s=s.replace(a,b)
# sky seams: the grade sheets and the haze sheet started inside the frame
s=s.replace("dayGrade('dgB',-130,-80,660,290,","dayGrade('dgB',-130,-420,660,630,")
s=s.replace("dayGrade('dgP',-130,-80,660,290,","dayGrade('dgP',-130,-420,660,630,")
s=s.replace("nightGrade('ngD',-140,-80,680,290,","nightGrade('ngD',-140,-420,680,630,")
once('<rect x="-124" y="-50" width="648" height="90" fill="#e7b98c" opacity=".18"/>','<rect x="-124" y="-420" width="648" height="460" fill="#e7b98c" opacity=".18"/>')
# Black Spots: the ambulance and the parked cars belong on the road, not the far sidewalk
VEH="ambulance(262,136)+'<g class=\"noedge\"><ellipse cx=\"360\" cy=\"154\" rx=\"24\" ry=\"1.6\" fill=\"rgba(0,0,0,.35)\"/><ellipse cx=\"442\" cy=\"154\" rx=\"24\" ry=\"1.6\" fill=\"rgba(0,0,0,.35)\"/><ellipse cx=\"294\" cy=\"151.6\" rx=\"32\" ry=\"1.8\" fill=\"rgba(0,0,0,.38)\"/></g>'+'<g transform=\"translate(338 141) scale(.62)\">'+sedan(0,0,'#6b7f5e','#55663f')+'</g>'+'<g transform=\"translate(420 141) scale(.62)\">'+sedan(0,0,'#c9b48a','#a8946a')+'</g>'+"
once(VEH,"")
once("     '<g class=\"noedge\" opacity=\".92\">'+\n       rc(44,164,96,3.2,'var(--p-white)')",
     "     '<g class=\"noedge\"><ellipse cx=\"294\" cy=\"172.4\" rx=\"32\" ry=\"1.8\" fill=\"rgba(0,0,0,.4)\"/><ellipse cx=\"360\" cy=\"165.4\" rx=\"24\" ry=\"1.4\" fill=\"rgba(0,0,0,.38)\"/><ellipse cx=\"442\" cy=\"165.4\" rx=\"24\" ry=\"1.4\" fill=\"rgba(0,0,0,.38)\"/></g>'+'<g transform=\"translate(338 150) scale(.62)\">'+sedan(0,0,'#6b7f5e','#55663f')+'</g>'+'<g transform=\"translate(420 150) scale(.62)\">'+sedan(0,0,'#c9b48a','#a8946a')+'</g>'+ambulance(262,145)+\n     '<g class=\"noedge\" opacity=\".92\">'+\n       rc(44,164,96,3.2,'var(--p-white)')")
once('<rect class="blink mid" x="282" y="136" width="6.4"','<rect class="blink mid" x="282" y="145" width="6.4"')
once('<rect class="blink2 mid" x="289" y="136" width="6.4"','<rect class="blink2 mid" x="289" y="145" width="6.4"')
once('<circle class="blink mid" cx="285" cy="137.8" r="6"','<circle class="blink mid" cx="285" cy="146.8" r="6"')
# Dead Ants: the head sign fits its words; the far car sits on its street; the headlight on the bus
once("    o+=rc(x+w-22,y+1.3,15,3,'#15161a',' rx=\".4\"');","    o+=rc(x+w-30,y+1.2,22,3.2,'#15161a',' rx=\".4\"');")
once("font-size=\"2.2\" fill=\"#ffb347\">39 ARBORWAY</text>'","font-size=\"1.9\" fill=\"#ffb347\">39 ARBORWAY</text>'")
s=s.replace("o+='<text x=\"'+(x+w-14.5)+'\" y=\"'+(y+3.6)+'\"","o+='<text x=\"'+(x+w-19)+'\" y=\"'+(y+3.5)+'\"")
once('+\'<g transform="translate(250 139) scale(.6)">\'','+\'<g transform="translate(250 134) scale(.6)">\'')
once('<circle class="pulse" cx="347" cy="177" r="4"','<circle class="pulse" cx="345.4" cy="177" r="2.6"')
# Peach: the cellar bulkhead as it is seen from the front: a sloped steel door coming off the end of the house
a=s.index('  function bulkhead(x,y){'); b=s.index('\n  }\n',a)+4
s=s[:a]+r'''  function bulkhead(x,y){
    // x,y: where the house wall meets the ground at its end; the doors slope away from it
    var o=rc(x,y-1.6,26,2.4,'var(--p-granite)')+P('M'+x+' '+(y-12)+' L'+(x+24)+' '+(y-2)+' L'+x+' '+(y-2)+' Z','#6a7780');
    o+='<g class="noedge">'+ln('M'+(x+3)+' '+(y-10.2)+' L'+(x+22)+' '+(y-2.6)+' M'+(x+6)+' '+(y-9)+' L'+(x+6)+' '+(y-2),'#4a555c',.5)+rc(x+10,y-7.4,3,1.4,'#2c3136')+rc(x,y-12.6,1.6,10.6,'#4a555c')+'</g>';
    return o;
  }
'''+s[b:]
once("     bulkhead(88,182)+","     bulkhead(116,180)+")
once("     '<g class=\"noedge\">'+ln('M86 196 l16 -14','var(--p-kraft)',3.2)+'</g>'+","")
# Echigo: no drawn rings in the puddles; the villagers' reflections soft, not posts
a=s.index("    // rings where the rain lands in the puddles"); b=s.index("    o+='<g class=\"noedge\">'+spl+'</g>';",a)+len("    o+='<g class=\"noedge\">'+spl+'</g>';")
s=s[:a]+s[b:]
once("<rect x=\"'+(x-s*.16)+'\" y=\"'+(y+.6)+'\" width=\"'+(s*.32)+'\" height=\"'+(s*.5)+'\" fill=\"'+robe+'\" opacity=\".16\"/>","")
open('/tmp/sb/w.html','w').write(s); print('bugs ok')
