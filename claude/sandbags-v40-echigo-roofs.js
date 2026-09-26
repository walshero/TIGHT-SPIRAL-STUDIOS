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
      o+='<path d="M'+x.toFixed(1)+' '+y.toFixed(1)+' l'+w.toFixed(1)+' '+h.toFixed(1)+' h-'+(2*w).toFixed(1)+' z" fill="'+cols[(r()*cols.length)|0]+'"/>';
    }
    return P(d,base)+'<defs><clipPath id="'+id+'"><path d="'+d+'"/></clipPath></defs><g class="noedge" clip-path="url(#'+id+')">'+o+'</g>';
  }
  // v41 (founder: "What are the yellow and red ovals? If foliage, go real tree"):
  // an autumn maple among the cedars. A trunk that forks, and a crown of small
  // lobes in reds and ambers, darker on the side away from the light.
  function momiji(x,g,h,r){
    var C=[['#c24a2c','#8e3019','#e07a45'],['#cf6a2e','#9a4620','#eb9a52'],['#d99a38','#a8702a','#f0bf5e'],['#b23a28','#7d2819','#d8653d']][(r()*4)|0], o='';
    var cy=g-h*.66, rx=h*.46, ry=h*.3, tr=Math.max(.8,h*.06);
    // trunk and the branches that show under the crown
    o+=ln('M'+x+' '+g+' q'+(-h*.03)+' '+(-h*.2)+' 0 '+(-h*.36)+' M'+x+' '+(g-h*.24)+' q'+(-h*.14)+' '+(-h*.06)+' '+(-h*.26)+' '+(-h*.22)+' M'+x+' '+(g-h*.3)+' q'+(h*.12)+' '+(-h*.05)+' '+(h*.28)+' '+(-h*.2)+' M'+x+' '+(g-h*.36)+' l'+(h*.04)+' '+(-h*.18),'#3a2a20',tr);
    // the crown: shade lobes underneath, the body, lit lobes on top; a scalloped edge
    var lobes=function(n,sx,sy,oy,rad,col){ var t=''; for(var i=0;i<n;i++){ var a=Math.PI*(1+i/(n-1)), rrr=rad*(.8+r()*.4);
      t+='<circle cx="'+(x+Math.cos(a)*rx*sx).toFixed(1)+'" cy="'+(cy+oy+Math.sin(a)*ry*sy).toFixed(1)+'" r="'+rrr.toFixed(2)+'" fill="'+col+'"/>'; } return t; };
    o+=lobes(9,1.05,-.35,ry*.35,h*.1,C[1]);
    o+='<ellipse cx="'+x+'" cy="'+cy.toFixed(1)+'" rx="'+(rx*.92).toFixed(1)+'" ry="'+(ry*.85).toFixed(1)+'" fill="'+C[0]+'"/>';
    o+=lobes(11,1,1,0,h*.1,C[0]);
    o+=lobes(6,.6,.75,-ry*.1,h*.07,C[2]);
    // gaps where the branches show through
    o+=ln('M'+(x-rx*.35)+' '+(cy+ry*.3)+' l'+(rx*.25)+' '+(-ry*.3)+' M'+(x+rx*.2)+' '+(cy+ry*.35)+' l'+(rx*.2)+' '+(-ry*.35),'#3a2a20',tr*.6,.8);
    return o;
  }

  // v41 (founder: "Use the real hiragana for ramen"): the noodle shop's
  // hanging board reads らーめん, top to bottom, cut from the letterforms of
  // Noto Serif CJK JP Bold (SIL Open Font License) and stored as outlines, so
  // it needs no font on the player's device. The long-vowel bar is turned
  // upright, the way it is set in vertical writing.
  var RAMEN=["M0.335 0.91 0.337 0.93C0.588 0.953 0.877 0.874 0.877 0.679C0.877 0.5720000000000001 0.797 0.462 0.636 0.462C0.5 0.462 0.376 0.544 0.305 0.5900000000000001C0.297 0.595 0.293 0.593 0.292 0.5820000000000001C0.291 0.552 0.302 0.511 0.307 0.472C0.311 0.44 0.316 0.419 0.314 0.39C0.311 0.362 0.296 0.33699999999999997 0.296 0.32099999999999995C0.296 0.31299999999999994 0.3 0.30499999999999994 0.318 0.30300000000000005C0.343 0.29900000000000004 0.40900000000000003 0.29100000000000004 0.456 0.29400000000000004C0.501 0.29800000000000004 0.525 0.30899999999999994 0.558 0.30899999999999994C0.591 0.30899999999999994 0.605 0.29200000000000004 0.605 0.264C0.605 0.20599999999999996 0.5730000000000001 0.16300000000000003 0.516 0.13C0.47500000000000003 0.10599999999999998 0.41300000000000003 0.08999999999999997 0.314 0.09699999999999998L0.31 0.11199999999999999C0.372 0.133 0.42 0.15200000000000002 0.446 0.19299999999999995C0.455 0.20499999999999996 0.454 0.21399999999999997 0.442 0.21999999999999997C0.40900000000000003 0.238 0.315 0.262 0.271 0.269C0.23600000000000002 0.275 0.225 0.30599999999999994 0.225 0.33299999999999996C0.225 0.358 0.226 0.375 0.223 0.40399999999999997C0.218 0.451 0.202 0.55 0.195 0.597C0.189 0.636 0.182 0.658 0.182 0.677C0.182 0.7 0.19 0.721 0.20800000000000002 0.74C0.227 0.762 0.246 0.773 0.265 0.773C0.298 0.773 0.311 0.733 0.336 0.698C0.393 0.626 0.513 0.504 0.625 0.504C0.711 0.504 0.758 0.5700000000000001 0.758 0.64C0.758 0.722 0.709 0.802 0.537 0.864C0.491 0.881 0.41300000000000003 0.9 0.335 0.91Z", "M0.615 0.673C0.615 0.635 0.591 0.62 0.5840000000000001 0.548C0.575 0.471 0.5609999999999999 0.247 0.5609999999999999 0.17100000000000004C0.5609999999999999 0.10099999999999998 0.5640000000000001 0.06599999999999995 0.5640000000000001 0.026000000000000023C0.5640000000000001 -0.016000000000000014 0.55 -0.040000000000000036 0.521 -0.040000000000000036C0.478 -0.040000000000000036 0.447 0.01200000000000001 0.447 0.07199999999999995C0.447 0.09599999999999997 0.455 0.14100000000000001 0.461 0.20799999999999996C0.46599999999999997 0.269 0.486 0.571 0.486 0.6779999999999999C0.486 0.731 0.459 0.748 0.419 0.778L0.425 0.795C0.449 0.798 0.478 0.801 0.501 0.792C0.55 0.774 0.615 0.712 0.615 0.673Z", "M0.49 0.718C0.519 0.718 0.539 0.705 0.539 0.6799999999999999C0.539 0.645 0.516 0.622 0.491 0.607C0.507 0.5820000000000001 0.522 0.556 0.535 0.528C0.5750000000000001 0.443 0.598 0.386 0.617 0.32899999999999996C0.744 0.358 0.8 0.463 0.8 0.5609999999999999C0.8 0.702 0.714 0.836 0.423 0.896L0.426 0.916C0.792 0.905 0.92 0.77 0.92 0.581C0.92 0.425 0.809 0.30100000000000005 0.634 0.277L0.645 0.239C0.655 0.20599999999999996 0.672 0.19299999999999995 0.672 0.17100000000000004C0.672 0.132 0.582 0.09199999999999997 0.543 0.09199999999999997C0.517 0.09199999999999997 0.488 0.10099999999999998 0.458 0.12L0.46 0.136C0.482 0.137 0.502 0.14 0.518 0.14500000000000002C0.534 0.15000000000000002 0.544 0.15700000000000003 0.543 0.17899999999999994C0.542 0.20199999999999996 0.538 0.235 0.529 0.273C0.445 0.28 0.375 0.30699999999999994 0.32 0.33999999999999997L0.315 0.31899999999999995C0.304 0.277 0.279 0.258 0.252 0.238C0.225 0.21799999999999997 0.182 0.20299999999999996 0.135 0.19399999999999995L0.127 0.20399999999999996C0.167 0.246 0.202 0.28700000000000003 0.218 0.33199999999999996L0.24 0.399C0.182 0.451 0.094 0.548 0.094 0.696C0.094 0.767 0.126 0.839 0.199 0.839C0.265 0.839 0.311 0.803 0.35100000000000003 0.772C0.373 0.755 0.399 0.729 0.426 0.6970000000000001C0.446 0.708 0.47000000000000003 0.718 0.49 0.718ZM0.517 0.32299999999999995C0.502 0.378 0.48 0.439 0.449 0.499C0.439 0.519 0.427 0.538 0.41500000000000004 0.556C0.398 0.5389999999999999 0.381 0.517 0.365 0.488C0.34600000000000003 0.455 0.337 0.42 0.329 0.387C0.388 0.345 0.451 0.32699999999999996 0.517 0.32299999999999995ZM0.35100000000000003 0.639C0.334 0.658 0.316 0.675 0.3 0.688C0.275 0.709 0.248 0.725 0.22 0.725C0.194 0.725 0.17400000000000002 0.7 0.17400000000000002 0.65C0.17400000000000002 0.597 0.2 0.52 0.257 0.453C0.268 0.485 0.278 0.516 0.289 0.5409999999999999C0.303 0.573 0.322 0.607 0.35100000000000003 0.639Z", "M0.665 0.919C0.804 0.919 0.924 0.822 0.9460000000000001 0.587L0.93 0.583C0.889 0.6910000000000001 0.8 0.8089999999999999 0.6940000000000001 0.8089999999999999C0.653 0.8089999999999999 0.626 0.792 0.626 0.742C0.626 0.687 0.628 0.642 0.625 0.595C0.619 0.518 0.5720000000000001 0.475 0.487 0.475C0.455 0.475 0.41000000000000003 0.486 0.362 0.51C0.355 0.514 0.353 0.511 0.357 0.505C0.397 0.437 0.484 0.32399999999999995 0.535 0.272C0.5630000000000001 0.243 0.595 0.23199999999999998 0.595 0.20899999999999996C0.595 0.16900000000000004 0.542 0.10599999999999998 0.463 0.09499999999999997C0.441 0.09099999999999997 0.404 0.09499999999999997 0.38 0.10399999999999998L0.378 0.119C0.396 0.126 0.423 0.139 0.438 0.15200000000000002C0.449 0.16200000000000003 0.453 0.17600000000000005 0.443 0.19599999999999995C0.41300000000000003 0.254 0.262 0.506 0.196 0.62C0.14100000000000001 0.715 0.08700000000000001 0.788 0.08700000000000001 0.84C0.08700000000000001 0.876 0.108 0.914 0.146 0.914C0.183 0.914 0.201 0.887 0.212 0.857C0.229 0.81 0.246 0.749 0.271 0.6910000000000001C0.307 0.609 0.377 0.52 0.458 0.52C0.512 0.52 0.527 0.554 0.527 0.596C0.527 0.66 0.515 0.715 0.516 0.784C0.517 0.866 0.5690000000000001 0.919 0.665 0.919Z"];
  function ramenSign(x,y,w,h){
    var c=Math.min(w*.78,(h-5)/4), gx=x+(w-c)/2, o='';
    o+=ln('M'+(x+w*.3)+' '+(y-3)+' v3 M'+(x+w*.7)+' '+(y-3)+' v3','var(--p-char-d)',.5);
    o+=P('M'+(x-1.4)+' '+(y+.6)+' L'+(x+w/2)+' '+(y-2.6)+' L'+(x+w+1.4)+' '+(y+.6)+' Z','var(--p-timber-d)');
    o+=rc(x-.6,y,w+1.2,h+.6,'var(--p-timber-d)')+rc(x,y+.6,w,h-.6,'#f1ead8');
    RAMEN.forEach(function(d,i){ o+='<path transform="translate('+gx.toFixed(2)+' '+(y+2.6+i*c).toFixed(2)+') scale('+c.toFixed(3)+')'+(i===1?' translate(.06 0)':'')+'" d="'+d+'" fill="#1d1a17"/>'; });
    return '<g class="noedge">'+o+'</g>';
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
    // v41: the maples stand in the gaps between the roofs, trunks showing
    var mr=tssR(52), mp=''; [[122,176,40],[210,170,30],[292,164,34],[344,170,30],[-2,166,30]].forEach(function(t){ mp+=momiji(t[0],t[1],t[2],mr); });
    o+='<g class="ly3"><g class="noedge">'+mp+'</g></g>';
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
      +noren(140,202,18,'var(--p-indigo)')+roofKiri(106,188,56,16,5)+udatsu(100,188,12)+udatsu(163.6,188,12)+ramenSign(92,181,10,31);
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
      +pot(84,214,'#d8566a',4)+pot(298,214,'#e0a23a',8)+pot(344,214,'#e8c64a',9);
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
