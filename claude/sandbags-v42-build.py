s=open('/tmp/tsp/sandbags.html').read()
js=open('/tmp/sb/roofs.js').read()
def once(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:80]); s=s.replace(a,b)
a=s.index('  /* v40 EVERY ROOF DIFFERENT'); b=s.index('\n  var SCENERY=[\n',a)
s=s[:a]+js.rstrip('\n')+s[b:]

# SKY: far layers can drift too, so clouds sit behind the set, never on it
once("""    if(far) far.innerHTML=LS.filter(function(L){ return L.far; }).map(function(L){ return '<svg class="sk skfull" viewBox="0 0 '+W+' '+H+'" aria-hidden="true" focusable="false">'+L.c+'</svg>'; }).join('');
    box.innerHTML=LS.filter(function(L){ return !L.far; }).map(function(L){
      if(!L.v) return '<svg class="sk skfull" viewBox="0 0 '+W+' '+H+'" aria-hidden="true" focusable="false">'+L.c+'</svg>';
      return '<svg class="sk skdrift" style="width:'+(2*W)+'px;--dur:'+skF(W/L.v)+'s" viewBox="0 0 '+(2*W)+' '+H+'" aria-hidden="true" focusable="false">'
        +L.c+(L.wide?'':'<g transform="translate('+W+' 0)">'+L.c+'</g>')+'</svg>';
    }).join('');""",
"""    function mk(L){
      if(!L.v) return '<svg class="sk skfull" viewBox="0 0 '+W+' '+H+'" aria-hidden="true" focusable="false">'+L.c+'</svg>';
      return '<svg class="sk skdrift" style="width:'+(2*W)+'px;--dur:'+skF(W/L.v)+'s" viewBox="0 0 '+(2*W)+' '+H+'" aria-hidden="true" focusable="false">'
        +L.c+(L.wide?'':'<g transform="translate('+W+' 0)">'+L.c+'</g>')+'</svg>';
    }
    /* v42: clouds are far layers - they pass behind towers and hills, never in front */
    if(far) far.innerHTML=LS.filter(function(L){ return L.far; }).map(mk).join('');
    box.innerHTML=LS.filter(function(L){ return !L.far; }).map(mk).join('');""")
# Black Spots clouds behind the towers; fewer, larger
once("      var near=skRow(rnd,W,S,H*.34,.3,3,col,'sx1'), far=skRow(rnd,W,S,H*.47,.16,4,col,'sx0','.85');\n      return [{c:far,v:4},{c:near,v:9}];",
     "      /* v42: the clouds sit behind the towers (they were drawn over them) */\n      var near=skRow(rnd,W,S,H*.2,.34,2,col,'sx1'), far=skRow(rnd,W,S,H*.36,.18,3,col,'sx0','.8');\n      return [{c:far,v:3,far:1},{c:near,v:6,far:1}];")
# Peach Cobbler: golden-hour cumulus, lit from below, over the new hill
once("""      [[.14,.20,'#f0cfa6','.55'],[.27,.26,'#f2c58e','.7'],[.40,.30,'#f5cf9a','.8'],[.52,.34,'#f3cf98','.75']].forEach(function(L,k){
        var nb=Math.max(2,Math.round((2+k)*W/S)), g='';
        for(var b=0;b<nb;b++){ if(rnd()<.2) continue;
          g+=skBlob(rnd,W*(b+.5)/nb+(rnd()-.5)*W/nb*.5,H*L[0]+(rnd()-.5)*H*.02,W/nb*(.3+L[1]),H*(.012+k*.004),L[2],L[3]); }
        o+=skG('sx0',g);
      });
      return [{c:o,v:1.6}];""",
"""      /* v42 (founder: "Peach Cobbler clouds are bad and there's too much sky.
         Add a hill in the background."): the flat bands are gone. A few big
         fair-weather clouds at the top of the frame, their undersides lit
         rose and gold by the low sun, their tops still pale; the hill in the
         set takes the lower sky. */
      function flat(y,k,t){ return '<g transform="translate(0 '+skF(y)+') scale(1 '+k+') translate(0 '+skF(-y)+')">'+t+'</g>'; }
      var big=flat(H*.17,.55,skRow(rnd,W,S,H*.17,.42,2,['#efcb9c','#cf8f72','#f7e0bd'],'sx0','.92'));
      var small=flat(H*.27,.5,skRow(rnd,W,S,H*.27,.22,3,['#eec79a','#c98a6e','#f4d9b4'],'sx0','.7'));
      return [{c:small,v:1.1,far:1},{c:big,v:1.8,far:1}];""")
# Dead Ants: night clouds and stars behind the blocks
once("      return [{c:'<g>'+st+'</g>',v:0},{c:o,v:3}];","      return [{c:'<g>'+st+'</g>',v:0,far:1},{c:o,v:3,far:1}];")

# Black Spots: morning glass, no lamps on in daylight
once("""      for(var c=0;c<cols;c++) g+='<rect x="'+(x+3+c*cw+.6).toFixed(1)+'" y="'+fy.toFixed(1)+'" width="'+(cw-1.4).toFixed(1)+'" height="'+(pitch*.52).toFixed(1)+'" fill="'+(lit&&r()<lit?'#f6e7bf':glass)+'"/>';""",
"""      /* v42 (founder: "Lights on in hospitals for Black Spots looks bad"): it
         is morning. No lamps; the glass carries the sky - most panes dark,
         some catching the blue, a few with the blinds down. */
      for(var c=0;c<cols;c++){ var k=r(), pane=k<.16?'#7f98ad':k<.24?'#a9b9c6':k<.3?'#c7bfae':glass;
        g+='<rect x="'+(x+3+c*cw+.6).toFixed(1)+'" y="'+fy.toFixed(1)+'" width="'+(cw-1.4).toFixed(1)+'" height="'+(pitch*.52).toFixed(1)+'" fill="'+pane+'"/>'; }""")

# Peach Cobbler: the hill behind the street
once("""   '<g class="ly1">'+
     P('M-124 126 L-64 114 L0 132 L56 118 L124 128 L192 114 L264 126 L336 112 L400 124 L456 112 L524 126 L524 200 L-124 200 Z','var(--p-moss-d)')+""",
"""   /* v42 THE HILL. A long New England hill behind the street takes the
      lower sky: a far ridge in the haze, then pasture and hayfields cut by
      stone walls, a red barn and a white steeple, the whole slope lit gold
      from the left by the low sun. */
   '<g class="ly1">'+
     P('M-124 30 Q-40 4 60 18 T250 6 T420 20 T524 12 L524 200 L-124 200 Z','#b49a73')+
   '</g>'+
   '<g class="ly1">'+
     P('M-124 70 Q-10 38 110 52 Q200 62 280 40 Q380 20 524 46 L524 200 L-124 200 Z','#8f8a57')+
     '<g class="noedge">'+
       P('M-124 70 Q-10 38 110 52 Q200 62 280 40 Q380 20 524 46 L524 54 Q380 30 280 50 Q200 72 110 62 Q-10 48 -124 80 Z','#b9a266')+
       P('M150 76 Q230 62 300 56 L330 84 Q250 92 170 98 Z','#a49152')+P('M-60 88 Q20 70 90 72 L110 100 Q30 104 -40 110 Z','#9c8f58')+P('M340 70 Q420 52 500 60 L510 90 Q420 92 350 98 Z','#a9965a')+
       ln('M-124 96 Q0 76 120 82 T330 74 T524 70 M-40 110 Q60 96 170 100 T400 92 M150 76 L170 98 M330 84 L340 70','#6d6a45',1,.8)+
       '<g transform="translate(236 58)">'+rc(-7,-6,14,6,'#8d3b2a')+P('M-8 -6 L0 -11 L8 -6 Z','#5e2a20')+rc(-2,-3.4,4,3.4,'#3b2a20')+'</g>'+
       '<g transform="translate(402 44)">'+rc(-4,-7,8,7,'#efe9da')+P('M-5 -7 L0 -10 L5 -7 Z','#8a8478')+rc(-1.6,-17,3.2,7,'#efe9da')+P('M-2 -17 L0 -25 L2 -17 Z','#8a8478')+'</g>'+
       ln('M-124 30 Q-40 4 60 18 T250 6 T420 20 T524 12','#f2d19c',1.4,.55)+
     '</g>'+
   '</g>'+ haze(.22) +
   '<g class="ly1">'+
     P('M-124 126 L-64 114 L0 132 L56 118 L124 128 L192 114 L264 126 L336 112 L400 124 L456 112 L524 126 L524 200 L-124 200 Z','var(--p-moss-d)')+""")

# Dead Ants: night lives in the windows, the tanks on the roofs, the lamp on the walk
once("""     box(780,70,70,90,10,'var(--p-terra)','var(--p-terra-d)','var(--p-char-d)')+""",
"""     box(780,70,70,90,10,'var(--p-terra)','var(--p-terra-d)','var(--p-char-d)')+
     /* v42: the water tanks on the roofs, and more of the city awake */
     (function(){ var t=''; [[30,10],[150,30],[270,0],[520,20],[380,44]].forEach(function(p){ var x=p[0], y=p[1];
         t+=rc(x-9,y-4,18,4,'#3a2a24')+ln('M'+(x-7)+' '+y+' l-2 0 M'+(x-8)+' '+(y-4)+' v-2 M'+(x+8)+' '+(y-4)+' v-2','#2b211c',1.4)
           +rc(x-8,y-20,16,16,'#5a3d2c',' rx="1.4"')+P('M'+(x-9)+' '+(y-20)+' L'+x+' '+(y-27)+' L'+(x+9)+' '+(y-20)+' Z','#3d2b21')
           +'<g class="noedge">'+ln('M'+(x-8)+' '+(y-15)+' h16 M'+(x-8)+' '+(y-9)+' h16','#2b211c',.8)+'</g>'; });
       var r=skR(71), L=''; [[-12,20,7,9,14,15],[108,40,8,8,14,15],[248,10,5,10,12.5,15],[338,54,9,7,14,15],[478,30,6,9,14,15],[-202,34,6,10,14,15],[688,40,6,9,13,15]].forEach(function(g){
         for(var i=0;i<g[2];i++) for(var j=0;j<g[3];j++) if(r()<.13) L+='<rect x="'+(g[0]+i*g[4])+'" y="'+(g[1]+j*g[5])+'" width="7" height="9" rx=".6"/>'; });
       return t+'<g class="lit glow" opacity=".85">'+L+'</g>'; })()+""")
once("""       pole(250,92,74,32,true)+""","""       pole(250,92,74,32,true)+
       '<g class="noedge"><path d="M282 112 L262 164 L318 164 L298 112 Z" fill="#ffcf7a" opacity=".1"/><ellipse cx="290" cy="164" rx="30" ry="4" fill="#ffcf7a" opacity=".32"/></g>'+""")

note='''  v42 2026-09-26 (founder: "Peach Cobbler clouds are bad and there's too much
  sky. Add a hill in the background. In echigo that lopsided blue house stands
  out. Fix, and make everything at least two stories to show gables. The train
  track should not be as thick and clear and the roof in foreground. I need
  artistry in all of the sandbags still. Lights on in hospitals for black spots
  looks bad").
    - Echigo: every house two full storeys; eaves-front roofs now show their
      gable ends turned down the street; the lopsided house is dark cedar under
      weathered slate-grey tin, smaller, one of the family now; the viaduct is
      a thin, hazed line far back on the slope behind every roof, the E7 small.
    - Peach Cobbler: a long hill behind the street takes the lower sky (far
      ridge, hayfields and stone walls, a red barn, a white steeple, a gold rim
      from the low sun); the flat cloud bands are replaced by a few big
      fair-weather clouds lit rose underneath.
    - Black Spots: no lamps on in daylight; the tower glass carries the sky,
      some panes blue, a few with blinds down. Clouds now pass behind the towers
      (they had been drawn over them) - fewer and larger.
    - Dead Ants: water tanks on the roofs, more of the city's windows awake,
      the cobrahead throws a cone and a pool of light on the far sidewalk.
    - All scenes: cloud layers render behind the set.
'''
i=s.index('  v41 2026-09-26'); s=s[:i]+note+'\n'+s[i:]
assert s.count('<span class="ver">v41')==1 and s.count('&middot; v41</p>')==1
s=s.replace('<span class="ver">v41','<span class="ver">v42').replace('&middot; v41</p>','&middot; v42</p>')
open('/tmp/sb/v42.html','w').write(s); print('ok')
