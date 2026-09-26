s=open('/tmp/tsp/sandbags.html').read()
def once(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:90]); s=s.replace(a,b)
def cut_fn(name):
    global s
    a=s.index('  function '+name+'('); b=s.index('\n  }\n',a)+4; return a,b

TREE=r'''  /* v45 (founder: "We don't do lollipop trees as TSP"). No ball on a stick,
     anywhere. A tree is grown: a trunk that forks, limbs that fork again and
     taper, and foliage cut as ragged clumps at the ends of the limbs, so the
     crown is uneven and the sky and the branches show through the gaps. Four
     habits: the Boston street elm (a vase of limbs, a high arching canopy),
     the maple (broad, rounded, irregular), the Japanese maple (spreading,
     layered flat), the oak (wide, crooked). Shade clumps underneath, the body,
     lit clumps on the sun side. */
  function paperTree(x,g,h,o){
    o=o||{};
    var r=tssR(o.seed||Math.round(Math.abs(x*131+g*17+h*7))+1), form=o.form||'maple';
    var F={elm:{d:5,sp:[12,26],len:.8,base:.26,cl:.11,up:.28,fl:.74},
           maple:{d:4,sp:[22,40],len:.74,base:.2,cl:.2,up:.1,fl:.82},
           momiji:{d:4,sp:[34,58],len:.72,base:.22,cl:.16,up:-.12,fl:.52},
           oak:{d:4,sp:[28,50],len:.72,base:.2,cl:.21,up:.02,fl:.74}}[form];
    var D=o.depth||F.d, br='', tips=[], cols=o.cols||['#2f4633','#43603f','#6d8a57'], trunk=o.trunk||'#3a2a20';
    function grow(x0,y0,ang,len,w,dep){
      var x1=x0+Math.cos(ang)*len, y1=y0+Math.sin(ang)*len, nx=-Math.sin(ang), ny=Math.cos(ang), w1=w*.66;
      br+='M'+(x0+nx*w/2).toFixed(2)+' '+(y0+ny*w/2).toFixed(2)+' L'+(x1+nx*w1/2).toFixed(2)+' '+(y1+ny*w1/2).toFixed(2)+' L'+(x1-nx*w1/2).toFixed(2)+' '+(y1-ny*w1/2).toFixed(2)+' L'+(x0-nx*w/2).toFixed(2)+' '+(y0-ny*w/2).toFixed(2)+' Z ';
      if(dep>=D){ tips.push([x1,y1,1]); return; }
      if(dep>=D-2 && r()<.75) tips.push([x1,y1,.8]);
      var n=r()<.3?3:2;
      for(var i=0;i<n;i++){
        var sp=(F.sp[0]+r()*(F.sp[1]-F.sp[0]))*Math.PI/180, side=n===2?(i?1:-1):(i-1), a=ang+side*sp+(r()-.5)*.3;
        a+=(-Math.PI/2-a)*F.up;
        grow(x1,y1,a,len*(F.len+(r()-.5)*.16),w1,dep+1);
      }
    }
    grow(x,g,-Math.PI/2+(o.lean||0)+(r()-.5)*.1,h*F.base,Math.max(.7,h*.075),1);
    function clump(cx,cy,rx,ry,col){
      var n=9, pts=[], d='';
      for(var i=0;i<n;i++){ var a=i/n*Math.PI*2, k=.68+r()*.5; pts.push([cx+Math.cos(a)*rx*k, cy+Math.sin(a)*ry*k]); }
      d='M'+((pts[0][0]+pts[n-1][0])/2).toFixed(2)+' '+((pts[0][1]+pts[n-1][1])/2).toFixed(2);
      for(i=0;i<n;i++){ var p=pts[i], q=pts[(i+1)%n]; d+=' Q'+p[0].toFixed(2)+' '+p[1].toFixed(2)+' '+((p[0]+q[0])/2).toFixed(2)+' '+((p[1]+q[1])/2).toFixed(2); }
      return '<path d="'+d+' Z" fill="'+col+'"/>';
    }
    var sh='', mid='', hi='';
    tips.forEach(function(t){ var cr=h*F.cl*t[2]*(.75+r()*.55), cx=t[0]+(r()-.5)*cr*.4, cy=t[1]+(r()-.5)*cr*.3;
      sh+=clump(cx+cr*.14,cy+cr*.22,cr*1.05,cr*F.fl*1.05,cols[0]);
      mid+=clump(cx,cy,cr,cr*F.fl,cols[1]);
      if(r()<.5) hi+=clump(cx-cr*.28,cy-cr*.26,cr*.55,cr*F.fl*.55,cols[2]); });
    return '<g class="noedge">'+sh+'<path d="'+br+'" fill="'+trunk+'"/>'+mid+hi+'</g>';
  }
  // a woodland edge seen across a field: one ragged canopy made of many
  // clumps, trunks lost in the shade underneath, never a row of balls
  function woodland(x0,x1,top,base,cols,seed){
    var r=tssR(seed), o='', hi='';
    for(var x=x0;x<x1;x+=5+r()*6){ var cr=6+r()*7, cy=top+r()*(base-top)*.45;
      o+='<path d="M'+(x-cr)+' '+base+' L'+(x-cr*.9)+' '+(cy+cr*.3).toFixed(1)+' Q'+(x-cr)+' '+(cy-cr*.6).toFixed(1)+' '+(x-cr*.2).toFixed(1)+' '+(cy-cr*.7).toFixed(1)+' Q'+(x+cr*.3).toFixed(1)+' '+(cy-cr*1.1).toFixed(1)+' '+(x+cr*.8).toFixed(1)+' '+(cy-cr*.4).toFixed(1)+' Q'+(x+cr*1.2).toFixed(1)+' '+(cy+cr*.1).toFixed(1)+' '+(x+cr)+' '+(cy+cr*.5).toFixed(1)+' L'+(x+cr)+' '+base+' Z" fill="'+cols[(r()*2)|0]+'"/>';
      if(r()<.5) hi+='<ellipse cx="'+(x-cr*.2).toFixed(1)+'" cy="'+(cy-cr*.35).toFixed(1)+'" rx="'+(cr*.45).toFixed(1)+'" ry="'+(cr*.25).toFixed(1)+'" fill="'+cols[2]+'" opacity=".7"/>'; }
    return '<g class="noedge">'+o+hi+'</g>';
  }
  // the old tree() call sites keep their footprint: r was the ball's radius
  function tree(x,y,r,f,fS){
    return paperTree(x,y+r*1.2,r*3.3,{form:r>=15?'elm':(r>=12?'oak':'maple'),cols:[fS,f,'color-mix(in srgb, '+f+' 62%, #fff1cf)'],trunk:'#4a3a2c'});
  }
'''
a,b=cut_fn('tree'); s=s[:a]+TREE+s[b:]

MOM=r'''  function momiji(x,g,h,r){
    var C=[['#8e3019','#c24a2c','#e07a45'],['#9a4620','#cf6a2e','#eb9a52'],['#a8702a','#d99a38','#f0bf5e'],['#7d2819','#b23a28','#d8653d']][(r()*4)|0];
    return paperTree(x,g,h*1.1,{form:'momiji',cols:C,trunk:'#3a2a20',seed:Math.round(x*7+g)});
  }
'''
a,b=cut_fn('momiji'); s=s[:a]+MOM+s[b:]

DAT=r'''  function daTrees(){
    var o='';
    [[-120,150,92],[-84,150,104],[-50,150,94],[-18,150,108],[16,150,100],[48,150,106],[80,150,86],[104,150,78],[128,150,62]].forEach(function(t,i){
      o+=paperTree(t[0],t[1],t[2],{form:i%3===1?'oak':'elm',cols:['#151e1a','#1d2a24','#35432f'],trunk:'#141110',seed:900+i});
    });
    return '<g class="ly1">'+o+'</g>';
  }
'''
a,b=cut_fn('daTrees'); s=s[:a]+DAT+s[b:]

once("""        if((i+k)%2===0){ o+='<g class="noedge">'+rc(p[0]-.5*(1-t),p[1]-h*.5,1.1*(1-t)+.3,h*.5,'#2b211c')+'<ellipse cx="'+p[0].toFixed(1)+'" cy="'+(p[1]-h*.66).toFixed(1)+'" rx="'+(h*.26).toFixed(1)+'" ry="'+(h*.24).toFixed(1)+'" fill="#26352c"/><ellipse cx="'+(p[0]-h*.08).toFixed(1)+'" cy="'+(p[1]-h*.72).toFixed(1)+'" rx="'+(h*.16).toFixed(1)+'" ry="'+(h*.13).toFixed(1)+'" fill="#324437"/></g>'; }""",
"""        if((i+k)%2===0){ o+=paperTree(p[0],p[1],h,{form:'elm',depth:4,cols:['#1b2620','#26352c','#3a4a37'],trunk:'#2b211c',seed:700+i*3+k}); }""")

once("""     P('M-124 126 L-64 114 L0 132 L56 118 L124 128 L192 114 L264 126 L336 112 L400 124 L456 112 L524 126 L524 200 L-124 200 Z','var(--p-moss-d)')+""",
"""     P('M-124 126 L-64 114 L0 132 L56 118 L124 128 L192 114 L264 126 L336 112 L400 124 L456 112 L524 126 L524 200 L-124 200 Z','var(--p-moss-d)')+
     woodland(-130,530,104,140,['#5f6b3e','#6c7446','#a59a5a'],61)+""")
note='''  v45 2026-09-26 (founder: "We don't do lollipop trees as TSP"). Every tree
  in all four scenes is now grown, not stamped: a trunk that forks, tapering
  limbs, ragged foliage clumps at the ends, gaps where sky and branches show.
  Street elms up Longwood and behind Sparr's; maples and oaks in Peach
  Cobbler's treeline and yards and on Longwood Avenue by the hospital;
  spreading Japanese maples in Echigo.
'''
i=s.index('  v44 2026-09-26'); s=s[:i]+note+'\n'+s[i:]
assert s.count('<span class="ver">v44')==1 and s.count('&middot; v44</p>')==1
s=s.replace('<span class="ver">v44','<span class="ver">v45').replace('&middot; v44</p>','&middot; v45</p>')
open('/tmp/sb/v45.html','w').write(s); print('ok')
