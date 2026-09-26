  /* v40 EVERY ROOF DIFFERENT (founder 09-26: "Build echigo with all different
     roofs", with a photograph of Magome-juku on the Nakasendo: grey kawara
     roofs stepping down a hill, deep eaves, a stone lantern, pots, a hanging
     board, mountains behind). Composition is print C of the ukiyo-e mock-ups,
     "Evening Rain Under the Mountain" (founder did not choose; studio pick):
     a low horizon, the mountain two thirds of the frame, the town in three
     rows stepping down the slope. No two roofs share a type:
       front  hisashi machiya, kura, noodle shop with udatsu, stone-weighted
              shingle (ishi-okiyane), irimoya inn, tin lean-to, hipped tile
       middle split-ridge tin gable, copper shrine roof with curved eaves,
              lopsided snow roof, brewer's roof with a raised ridge vent,
              flat concrete slab, hipped tin
       back   kayabuki farmhouse, gassho A-frame
     The sheet fills the sky box, 400 x 250; a phone crops it to the middle. */
  var UK={ tile:'#4a4e57', tileD:'#2e3138', tileL:'#6b707a', board:'#8a8173', boardD:'#5f584d', copper:'#5e9585', copperL:'#86b8a6', copperD:'#3c6b5e', rust:'#8a4a2e', rustD:'#62331f' };
  var RID=0;
  function ukClip(d,tex){ var id='rf'+(RID++); return '<defs><clipPath id="'+id+'"><path d="'+d+'"/></clipPath></defs><g class="noedge" clip-path="url(#'+id+')">'+tex+'</g>'; }
  function ukGrad(id,stops,x,y,w,h,extra){
    var s=''; stops.forEach(function(t){ s+='<stop offset="'+t[0]+'" stop-color="'+t[1]+'"'+(t[2]!=null?' stop-opacity="'+t[2]+'"':'')+'/>'; });
    return '<defs><linearGradient id="'+id+'" x1="0" y1="0" x2="0" y2="1">'+s+'</linearGradient></defs><rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="url(#'+id+')"'+(extra||'')+'/>';
  }
  function ukGlow(id,cx,cy,rx,ry,col,op){
    return '<defs><radialGradient id="'+id+'"><stop offset="0" stop-color="'+col+'" stop-opacity="'+op+'"/><stop offset="1" stop-color="'+col+'" stop-opacity="0"/></radialGradient></defs><ellipse cx="'+cx+'" cy="'+cy+'" rx="'+rx+'" ry="'+ry+'" fill="url(#'+id+')"/>';
  }
  function ukRain(seed,n,x0,x1,y0,y1,ang,len,col,w){
    var r=tssR(seed), d='';
    for(var i=0;i<n;i++){ var x=x0+r()*(x1-x0), y=y0+r()*(y1-y0), l=len*(.6+r()*.8);
      d+='M'+x.toFixed(1)+' '+y.toFixed(1)+' l'+(l*Math.sin(ang)).toFixed(1)+' '+(l*Math.cos(ang)).toFixed(1)+' '; }
    return '<g class="noedge urain">'+ln(d,col,w)+'</g>';
  }
  function ukForest(d,id,seed,base,cols,y0,y1,step){
    var r=tssR(seed), o='';
    for(var y=y0;y<y1;y+=step*.8) for(var x=-20+r()*step;x<420;x+=step*(.8+r()*.7)){
      var h=step*(1.3+r()*.8), w=h*.4;
      if(r()<.03){ o+='<ellipse cx="'+x.toFixed(1)+'" cy="'+(y+h*.6).toFixed(1)+'" rx="'+(w*1.3).toFixed(1)+'" ry="'+(h*.35).toFixed(1)+'" fill="'+(r()<.5?'#8f4a34':'#a8733c')+'"/>'; continue; }
      o+='<path d="M'+x.toFixed(1)+' '+y.toFixed(1)+' l'+w.toFixed(1)+' '+h.toFixed(1)+' h-'+(2*w).toFixed(1)+' z" fill="'+cols[(r()*cols.length)|0]+'"/>';
    }
    return P(d,base)+'<defs><clipPath id="'+id+'"><path d="'+d+'"/></clipPath></defs><g class="noedge" clip-path="url(#'+id+')">'+o+'</g>';
  }
  function ukSeal(x,y,s){
    return '<g class="noedge" transform="translate('+x+' '+y+') scale('+s+')"><rect x="0" y="0" width="48" height="48" rx="4" fill="#a8391f"/><use href="#tss-spiral" style="stroke:#f1e4c8;stroke-width:3.6;fill:none"/></g>';
  }
  function ukLean(svg,x,y,a){ return '<g transform="rotate('+a+' '+x+' '+y+')">'+svg+'</g>'; }

  // kawara: the channels running down the slope and the courses across it
  function kawara(x0,y0,x1,y1,pitch){
    var v='',h='';
    for(var x=x0;x<x1;x+=(pitch||2)) v+='M'+x.toFixed(1)+' '+y0.toFixed(1)+' V'+y1.toFixed(1)+' ';
    for(var y=y0+2.2;y<y1;y+=2.6) h+='M'+x0.toFixed(1)+' '+y.toFixed(1)+' H'+x1.toFixed(1)+' ';
    return ln(v,UK.tileD,.7,.6)+ln(h,UK.tileL,.45,.45);
  }
  // a ridge with onigawara, the tall end tiles that turn up at each end
  function ridge(x0,x1,y,col){
    return rc(x0,y-2.4,x1-x0,3,col)+P('M'+x0+' '+(y+.6)+' l-1.2 -5 l3.4 1.4 v3.6 z',col)+P('M'+x1+' '+(y+.6)+' l1.2 -5 l-3.4 1.4 v3.6 z',col);
  }
  // 1. eaves to the street, tiled, plain gable (kirizuma)
  function roofKiri(x,y,w,rh,e){
    var d='M'+(x-e)+' '+(y+1)+' L'+(x+w+e)+' '+(y+1)+' L'+(x+w+e-3)+' '+(y-rh)+' L'+(x-e+3)+' '+(y-rh)+' Z';
    return P(d,UK.tile)+ukClip(d,kawara(x-e,y-rh,x+w+e,y+1))+'<g class="noedge">'+rc(x-e,y,w+2*e,1.6,UK.tileD)+'</g>'+ridge(x-e+3,x+w+e-3,y-rh,UK.tileD);
  }
  // 2. irimoya: a hipped skirt with a small gable riding on top
  function roofIrimoya(x,y,w,rh,e,wall){
    var m=y-rh*.5, d1='M'+(x-e)+' '+(y+1)+' L'+(x+w+e)+' '+(y+1)+' L'+(x+w*.88)+' '+m+' L'+(x+w*.12)+' '+m+' Z';
    var d2='M'+(x+w*.1)+' '+(m+1)+' L'+(x+w*.9)+' '+(m+1)+' L'+(x+w*.84)+' '+(y-rh)+' L'+(x+w*.16)+' '+(y-rh)+' Z';
    return P(d1,UK.tile)+ukClip(d1,kawara(x-e,m,x+w+e,y+1))
      +P('M'+(x+w*.12)+' '+(m+.4)+' L'+(x+w*.16)+' '+(y-rh)+' L'+(x+w*.22)+' '+(m+.4)+' Z',wall)+P('M'+(x+w*.88)+' '+(m+.4)+' L'+(x+w*.84)+' '+(y-rh)+' L'+(x+w*.78)+' '+(m+.4)+' Z',wall)
      +P(d2,UK.tile)+ukClip(d2,kawara(x+w*.1,y-rh,x+w*.9,m+1))
      +'<g class="noedge">'+rc(x-e,y,w+2*e,1.6,UK.tileD)+rc(x+w*.1,m,w*.8,1.4,UK.tileD)+'</g>'+ridge(x+w*.16,x+w*.84,y-rh,UK.tileD);
  }
  // 3. yosemune: hipped all round, the hips running down to the corners
  function roofHip(x,y,w,rh,e,f,fD,tin){
    var d='M'+(x-e)+' '+(y+1)+' L'+(x+w+e)+' '+(y+1)+' L'+(x+w*.72)+' '+(y-rh)+' L'+(x+w*.28)+' '+(y-rh)+' Z', tex;
    if(tin){ tex=''; for(var sx=x-e;sx<x+w+e;sx+=3) tex+='M'+sx.toFixed(1)+' '+(y-rh)+' V'+(y+1)+' '; tex=ln(tex,fD,.6,.7); }
    else tex=kawara(x-e,y-rh,x+w+e,y+1);
    return P(d,f)+ukClip(d,tex)+'<g class="noedge">'+ln('M'+(x-e)+' '+(y+1)+' L'+(x+w*.28)+' '+(y-rh)+' M'+(x+w+e)+' '+(y+1)+' L'+(x+w*.72)+' '+(y-rh),fD,1.4)+'</g>'+rc(x+w*.28,y-rh-1.6,w*.44,2.4,fD);
  }
  // 4. ishi-okiyane: shallow board roof held down with battens and river stones
  function roofIshi(x,y,w,rh,e){
    var d='M'+(x-e)+' '+(y+1)+' L'+(x+w+e)+' '+(y+1)+' L'+(x+w+e-2)+' '+(y-rh)+' L'+(x-e+2)+' '+(y-rh)+' Z', b='', st='', r=tssR(41);
    for(var sx=x-e;sx<x+w+e;sx+=3.2) b+='M'+sx.toFixed(1)+' '+(y-rh)+' V'+(y+1)+' ';
    var o=P(d,UK.board)+ukClip(d,ln(b,'#a39a8b',.5,.6));
    [y-rh*.7,y-rh*.25].forEach(function(by){ o+=rc(x-e+1,by,w+2*e-2,1.1,UK.boardD);
      for(var sx=x-e+3;sx<x+w+e-2;sx+=5+r()*3) st+='<ellipse cx="'+sx.toFixed(1)+'" cy="'+(by-.6).toFixed(1)+'" rx="'+(1.3+r()*.8).toFixed(1)+'" ry="'+(1+r()*.4).toFixed(1)+'" fill="'+(r()<.5?'#9b978d':'#7d7a73')+'"/>'; });
    return o+'<g class="noedge">'+st+rc(x-e,y,w+2*e,1.2,UK.boardD)+'</g>';
  }
  // 5. katanagare: one slope, corrugated tin, the gable end to us
  function roofShed(x,y,w,rise,e,wall,f,fD){
    var o=P('M'+x+' '+y+' L'+(x+w)+' '+(y-rise)+' L'+(x+w)+' '+y+' Z',wall);
    var d='M'+(x-e)+' '+(y+1)+' L'+(x+w+e)+' '+(y-rise-3)+' L'+(x+w+e)+' '+(y-rise+2.4)+' L'+(x-e)+' '+(y+6.4)+' Z';
    return o+P(d,f)+'<g class="noedge">'+ln('M'+(x-e)+' '+(y+2.4)+' L'+(x+w+e)+' '+(y-rise-1.6)+' M'+(x-e)+' '+(y+4.4)+' L'+(x+w+e)+' '+(y-rise+.4),fD,.6)+'</g>';
  }
  // 6. copper, the shrine kind: eaves that sweep up at the ends, green with age
  function roofCopper(x,y,w,rh,e){
    var d='M'+(x-e-4)+' '+(y-3)+' Q'+(x+w/2)+' '+(y+3)+' '+(x+w+e+4)+' '+(y-3)+' Q'+(x+w+e-4)+' '+(y-rh*.35)+' '+(x+w*.8)+' '+(y-rh)+' L'+(x+w*.2)+' '+(y-rh)+' Q'+(x-e+4)+' '+(y-rh*.35)+' '+(x-e-4)+' '+(y-3)+' Z', s='';
    for(var sx=x-e;sx<x+w+e;sx+=3.6) s+='M'+sx.toFixed(1)+' '+(y-rh)+' V'+(y+2)+' ';
    return P(d,UK.copper)+ukClip(d,ln(s,UK.copperL,.6,.6))+ridge(x+w*.2,x+w*.8,y-rh,UK.copperD)
      +'<g class="noedge">'+ln('M'+(x+w*.3)+' '+(y-rh-2)+' l-3 -4 M'+(x+w*.7)+' '+(y-rh-2)+' l3 -4',UK.copperD,1)+'</g>';
  }
  // 7. koshi-yane: a brewer's tile roof with a small raised roof over the ridge vent
  function roofVent(x,y,w,rh,e){
    return roofKiri(x,y,w,rh,e)+rc(x+w*.3,y-rh-6,w*.4,6,'#1f2025')+roofKiri(x+w*.28,y-rh-5,w*.44,5,2);
  }
  // 8. flat: a concrete slab with a parapet, the house built in 1978
  function roofFlat(x,y,w){ return rc(x-2,y-3,w+4,3,'var(--p-granite-d)')+rc(x-2,y-6,w+4,3,'var(--p-granite)')+rc(x+w*.62,y-12,10,6,'var(--p-steel)'); }
  // 9. gassho: the steep thatched A-frame, windows up in the gable
  function gassho(x,g,w,h){
    var o=rc(x+w*.1,g-10,w*.8,10,'var(--p-cedar-d)');
    o+=P('M'+(x-3)+' '+(g-8)+' L'+(x+w/2)+' '+(g-8-h)+' L'+(x+w+3)+' '+(g-8)+' Z','var(--p-thatch)');
    o+=P('M'+(x+w*.2)+' '+(g-8)+' L'+(x+w/2)+' '+(g-8-h*.8)+' L'+(x+w*.8)+' '+(g-8)+' Z','var(--p-cedar)');
    o+='<g class="noedge">'+ln('M'+(x+w/2)+' '+(g-8-h)+' L'+(x-3)+' '+(g-8)+' M'+(x+w/2)+' '+(g-8-h)+' L'+(x+w+3)+' '+(g-8),'var(--p-thatch-d)',1.6)+'</g>';
    return o+fw(x+w*.4,g-8-h*.45,w*.2,5,1)+fw(x+w*.3,g-8-h*.2,w*.14,5,0)+fw(x+w*.56,g-8-h*.2,w*.14,5,1);
  }
  // an udatsu: the raised firewall at the end of a roof, plastered, tile-capped
  function udatsu(x,y,h){ return rc(x,y-h,4.4,h,'var(--p-white)')+rc(x-1,y-h-1.6,6.4,2,UK.tileD)+rc(x,y-3,4.4,1.2,'var(--p-white-d)'); }
  // a stone lantern, lit
  function toro(x,g){
    return rc(x-4,g-3,8,3,'var(--p-granite-d)')+rc(x-1.6,g-12,3.2,9,'var(--p-granite)')+rc(x-3.4,g-14,6.8,2,'var(--p-granite-d)')
      +rc(x-3,g-20,6,6,'var(--p-granite)')+'<g class="lit glow">'+lr(x-1.8,g-19,3.6,4)+'</g>'
      +P('M'+(x-6)+' '+(g-20)+' L'+x+' '+(g-25)+' L'+(x+6)+' '+(g-20)+' Z','var(--p-granite-d)')+'<circle cx="'+x+'" cy="'+(g-25.6)+'" r="1.2" fill="var(--p-granite)"/>';
  }
  function narrator(x,y,s){ return figure(x,y,s,{felt:'yellow',coat:'var(--p-char)',coatD:'var(--p-char-d)',legs:'var(--p-char-d)',hair:'var(--p-bone)'}); }

  function echigoTown(){
    var o='';
    // sky and mountain: night indigo grading to a pale break over the ridge
    o+=ukGrad('ukCsky',[[0,'#141d31'],[.22,'#2c3d5f'],[.46,'#6f7a95'],[.62,'#b8b2ab'],[1,'#b8b2ab']],-10,-10,420,270);
    o+='<g class="ly1">'+P('M-10 178 L40 152 L92 122 L128 100 L150 88 L176 58 L204 40 L222 44 L240 36 L262 58 L292 82 L310 80 L338 112 L372 134 L410 150 L410 200 L-10 200 Z','#5a6880')+'</g>';
    o+=ukGrad('ukCm1',[[0,'#b8b2ab',0],[.5,'#b8b2ab',.55],[1,'#b8b2ab',0]],-10,98,420,26);
    o+='<g class="ly1">'+ukForest('M-10 162 L28 136 L70 146 L112 118 L158 132 L200 106 L238 124 L286 110 L330 130 L372 120 L410 136 L410 205 L-10 205 Z','ukCf',17,'#243632',['#1d2e2a','#2f453c','#26392f','#3a5244'],102,205,4)+'</g>';
    o+=ukGrad('ukCm2',[[0,'#9aa0a6',0],[.5,'#9aa0a6',.45],[1,'#9aa0a6',0]],-10,138,420,22);
    // back row, up the slope
    o+='<g class="ly2">'+kayabuki(22,150,42,16)+gassho(252,170,40,44)+'</g>';
    // the viaduct and the E7, between the back row and the middle row
    o+='<g class="ly2">'+rc(-10,158,420,2.4,'var(--p-granite-d)');
    for(var px=4;px<410;px+=28) o+=rc(px,160,2.4,12,'#4a4f55');
    o+='</g>'+shinkansen(214,158);
    // middle row
    var m='';
    m+=snowGable(-8,164,44,24,30,7,'var(--p-cedar)','var(--p-cedar-d)','var(--p-tingreen)','var(--p-tingreen-d)',5,.5,1)+cedar(-8,164,44,24)+fw(4,170,9,7,1)+fw(20,170,9,7,0);
    m+=rc(42,170,52,18,'var(--p-timber)')+rc(46,170,3,18,'var(--p-verm)')+rc(87,170,3,18,'var(--p-verm)')+'<g class="lit glow">'+lr(54,174,30,8)+'</g>'+roofCopper(42,170,52,18,5);
    m+=snowGable(150,164,50,24,34,8,'var(--p-cream)','var(--p-cream-d)','var(--p-tinblue)','var(--p-tinblue-d)',6,.26,1)+fw(160,170,9,8,1)+fw(182,170,9,8,0);
    m+=rc(206,166,60,22,'var(--p-white)')+rc(206,178,60,10,'var(--p-char)')+fw(216,169,8,6,1)+fw(244,169,8,6,0)+roofVent(206,166,60,12,5);
    m+=rc(296,158,44,30,'var(--p-granite)')+'<g class="noedge">'+rc(302,163,12,8,'var(--p-steel-d)')+rc(322,163,12,8,'var(--p-steel-d)')+rc(302,176,12,8,'var(--p-steel-d)')+'</g>'+'<g class="lit glow">'+lr(322,176,12,8)+'</g>'+roofFlat(296,158,44);
    m+=rc(346,168,62,20,'var(--p-cedar)')+cedar(346,168,62,20)+fw(356,172,9,7,1)+fw(390,172,9,7,1)+roofHip(346,168,62,18,5,UK.rust,UK.rustD,1);
    o+='<g class="ly2">'+m+'</g>'+haze(.1);
    // front row, the street
    var f='';
    // hisashi machiya: two storeys, a pent roof between them, slotted plaster upstairs
    f+=rc(-12,195,58,19,'var(--p-cedar)')+koshi(-6,199,40,13,1)+rc(-12,180,58,15,'var(--p-cream)')
      +'<g class="noedge">'+rc(0,184,20,7,'var(--p-timber-d)')+ln('M3 184 v7 M6 184 v7 M9 184 v7 M12 184 v7 M15 184 v7 M18 184 v7','var(--p-cream)',1)+'</g>'+fw(30,184,8,7,1)
      +P('M-16 199 L50 199 L48 193 L-14 193 Z',UK.tile)+ukClip('M-16 199 L50 199 L48 193 L-14 193 Z',kawara(-16,193,50,199))+roofKiri(-12,180,58,12,4);
    // the kura
    f+=kura(50,180,40,34,6)+sugidama(70,184);
    // the noodle shop, eaves to the street, udatsu at both ends
    f+=rc(106,188,56,26,'var(--p-cream)')+timber(106,188,56,25,'var(--p-timber)')+fw(114,192,10,7,1)+fw(144,192,10,7,1)
      +'<g class="lit glow">'+lr(110,203,26,11)+'</g>'
      +'<g class="noedge">'+rc(109,202,28,1.4,'var(--p-timber-d)')+'<ellipse cx="116" cy="211" rx="3.4" ry="1.8" fill="var(--p-cream)"/><ellipse cx="124" cy="211" rx="3.4" ry="1.8" fill="var(--p-cream)"/><ellipse cx="132" cy="211" rx="3.4" ry="1.8" fill="var(--p-cream)"/>'
      +'<ellipse cx="116" cy="210.2" rx="3.4" ry=".8" fill="var(--p-terra)"/><ellipse cx="124" cy="210.2" rx="3.4" ry=".8" fill="var(--p-terra)"/><ellipse cx="132" cy="210.2" rx="3.4" ry=".8" fill="var(--p-terra)"/>'
      +ln('M115 209.6 l2.6 -5 M117 209.6 l2.6 -5 M123 209.6 l2.6 -5 M125 209.6 l2.6 -5 M131 209.6 l2.6 -5 M133 209.6 l2.6 -5','var(--p-kraft-d)',.5)+'</g>'
      +noren(140,202,18,'var(--p-indigo)')+roofKiri(106,188,56,16,5)+udatsu(100,188,12)+udatsu(163.6,188,12)+kanban(98,192,6,18,'var(--p-timber)','var(--p-cream)',11);
    // stone-weighted shingles over a cedar house
    f+=rc(168,192,50,22,'var(--p-cedar)')+cedar(168,192,50,22)+fw(176,196,9,7,1)+fw(200,196,9,7,0)+roofIshi(168,192,50,8,6);
    // the inn: irimoya, a row of lit rooms
    f+=rc(228,186,66,28,'var(--p-bone)')+timber(228,186,66,27,'var(--p-timber)')+fw(234,190,9,7,1)+fw(248,190,9,7,1)+fw(262,190,9,7,0)+fw(276,190,9,7,1)
      +'<g class="lit glow">'+lr(236,203,20,11)+'</g>'+noren(262,202,22,'var(--p-verm-d)')+roofIrimoya(228,186,66,26,6,'var(--p-bone)');
    // a lean-to in red tin
    f+=rc(300,190,40,24,'var(--p-white)')+fw(308,196,9,7,1)+rc(324,200,10,14,'var(--p-timber)')+roofShed(300,190,40,16,4,'var(--p-white)','var(--p-tinred)','var(--p-tinred-d)');
    // hipped tile over white plaster
    f+=rc(348,188,62,26,'var(--p-white)')+timber(348,188,62,25,'var(--p-timber)')+fw(356,192,10,7,0)+fw(376,192,10,7,1)+fw(394,192,10,7,1)+koshi(356,203,30,10,1)+roofHip(348,188,62,18,5,UK.tile,UK.tileD,0);
    // in front: the vending machines, the stone lantern, pots
    f+=vending(204,214,'var(--p-white)','var(--p-white-d)')+vending(222,214,'var(--p-verm)','var(--p-verm-d)')+toro(176,214)
      +pot(94,214,'#d8566a',4)+pot(298,214,'#e0a23a',8)+pot(344,214,'#e8c64a',9);
    o+='<g class="ly3">'+f+'</g>';
    // the street, black and wet, every light laid on it
    o+='<g class="ly3">'+rc(-10,214,420,46,'#1b2028')+'</g>';
    var sp=''; [[123,.9,26],[146,.6,18],[176,.6,16],[228,.5,14],[246,.55,16],[18,.4,14],[386,.4,14],[312,.35,12],[272,.45,14]].forEach(function(s){
      sp+='<rect x="'+(s[0]-2.6)+'" y="215" width="5.2" height="'+(s[2]*1.4)+'" fill="url(#ukCr)" opacity="'+s[1]+'"/>'; });
    o+='<defs><linearGradient id="ukCr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd58a" stop-opacity=".9"/><stop offset="1" stop-color="#ffd58a" stop-opacity="0"/></linearGradient><filter id="ukCb" x="-50%" y="-10%" width="200%" height="120%"><feGaussianBlur stdDeviation="1.2 2"/></filter></defs>';
    o+='<g class="noedge"><g filter="url(#ukCb)">'+sp+'</g>'+ukGlow('ukCg',128,214,40,8,'#ffcf7a',.45)+'</g>';
    var pp=ukLean(villager(60,236,18,'var(--p-indigo)','var(--p-gold)','#c9b48a','var(--p-cream)','cyan'),60,236,-4)
      +ukLean(villager(292,232,16,'var(--p-plum)','var(--p-cream)','var(--p-verm)','var(--p-bone)','pink'),292,232,-4)
      +ukLean(villager(372,234,17,'var(--p-moss-d)','var(--p-cream)','var(--p-tingreen)','var(--p-bone)','orange'),372,234,-4)
      +narrator(150,240,24);
    o+='<g class="ly3">'+pp+'</g>';
    o+='<g class="fx noedge">'+chochin(108,204)+chochin(160,204)+chochin(232,200)+chochin(292,200)
      +'<rect class="pulse" x="205.2" y="190.6" width="10.6" height="11" fill="#fff6d8" opacity=".35"/><rect class="pulse" x="223.2" y="190.6" width="10.6" height="11" fill="#fff6d8" opacity=".35" style="animation-delay:-1.4s"/></g>';
    o+=ukRain(31,170,-40,420,-10,250,.08,80,'rgba(214,222,236,.38)',.45);
    o+='<g class="noedge keylight">'+ukGlow('kl0',128,206,60,34,'#ffd58a',.5)+'</g>';
    o+=ukSeal(382,232,.2);
    return o;
  }
