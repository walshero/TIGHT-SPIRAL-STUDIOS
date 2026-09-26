  /* v43 THE CORNER, REBUILT (founder 09-26: "Sparrs in dead ants looks
     whacked. Perspective: Sparrs on the left. Break street for Longwood Ave
     and then the pay phones then the bus. Put characters between bus and
     corner and make ant much smaller. Use real Boston photos to get
     background right").
     The real corner: Sparr's was 635 Huntington Avenue, the 1909 brick block
     (A. J. Carpenter) on the west corner of Longwood Avenue, its side wall
     running up Longwood as 158 Longwood; Harvard bought it in 2002 and the
     painted sign on that wall outlived the store. MassArt's Tower Building,
     621 Huntington, stands on the east corner. Longwood Avenue runs away
     from Huntington into the medical area. Huntington carries the E branch
     in its median, rails and catenary. We stand on the Mission Hill side,
     looking north, one-point perspective with the vanishing point up
     Longwood. Left to right: Sparr's, Longwood Avenue, the payphones, the two
     of them with the ant between, the 39 at the curb. */
  var DA={ vx:118, vy:138, g:150 };
  function daP(x,y,t){ return [x+(DA.vx-x)*t, y+(DA.vy-y)*t]; }
  function daQuad(x,yT,yB,t0,t1,f){
    var a=daP(x,yT,t0), b=daP(x,yT,t1), c=daP(x,yB,t1), d=daP(x,yB,t0);
    return P('M'+a[0].toFixed(1)+' '+a[1].toFixed(1)+' L'+b[0].toFixed(1)+' '+b[1].toFixed(1)+' L'+c[0].toFixed(1)+' '+c[1].toFixed(1)+' L'+d[0].toFixed(1)+' '+d[1].toFixed(1)+' Z',f);
  }
  // painted letters on a wall that runs away from us: each letter set at its
  // own depth, smaller as the wall recedes, sheared to the wall's slope
  function daWallText(str,x,yT,yB,t0,frac,size,col,op){
    var o='', t=t0;
    for(var i=0;i<str.length;i++){
      var ch=str.charAt(i), top=daP(x,yT,t), bot=daP(x,yB,t), k=1-t, fs=size*k, y=top[1]+(bot[1]-top[1])*frac;
      var slope=((DA.vy-yT)*(1-frac)+(DA.vy-yB)*frac)/(DA.vx-x);
      if(ch!==' ') o+='<text x="0" y="0" transform="translate('+top[0].toFixed(2)+' '+y.toFixed(2)+') matrix('+k.toFixed(3)+' '+(slope*k).toFixed(3)+' 0 1 0 0)" font-family="Georgia,\'Times New Roman\',serif" font-weight="700" font-size="'+size+'" fill="'+col+'" opacity="'+op+'">'+ch+'</text>';
      t+=(ch===' '?.4:ch==='’'?.3:.72)*fs/Math.abs(DA.vx-x);
    }
    return o;
  }
  // Sparr's front on Huntington: two storeys of brick, the cut corner with the
  // door in it, the red band with its name, the lunch counter behind the glass
  function sparrsFront(x0,x1){
    var g=DA.g, top=96, o='';
    o+=rc(x0,top,x1-x0-6,g-top,'var(--p-brick)')+rc(x0-1.6,top-4,x1-x0-4.4,4.6,'var(--p-bone-d)')+rc(x0,top+.6,x1-x0-6,1.4,'var(--p-brick-d)');
    // the cut corner: a narrow face turned toward us and up the avenue
    o+=P('M'+(x1-6)+' '+top+' L'+x1+' '+(top+2)+' L'+x1+' '+g+' L'+(x1-6)+' '+g+' Z','#a8604c')+P('M'+(x1-6.6)+' '+(top-4)+' L'+(x1+.6)+' '+(top-2)+' L'+(x1+.6)+' '+(top+1)+' L'+(x1-6.6)+' '+(top+.6)+' Z','var(--p-bone-d)');
    var n=5, uw=(x1-x0-14)/n, up='';
    for(var i=0;i<n;i++) up+=fw(x0+6+i*uw,top+8,uw-7,12,i===1||i===4);
    o+=up+'<g class="noedge">';
    for(i=0;i<n;i++) o+=rc(x0+5+i*uw,top+5.4,uw-5,1.8,'var(--p-bone-d)');
    o+='</g>';
    var sb=g-32, w=x1-x0-6;
    o+=rc(x0,sb,w,7,'var(--p-verm)');
    o+='<g class="noedge"><text x="'+(x0+w/2)+'" y="'+(sb+5.6)+'" text-anchor="middle" font-family="Georgia,\'Times New Roman\',serif" font-weight="700" font-size="6" letter-spacing=".8" fill="#fbecc8">SPARR’S DRUG</text></g>';
    o+='<g class="lit glow">'+lr(x0+3,sb+9,w*.46,21)+lr(x0+w*.52,sb+9,w*.44,21)+P('M'+(x1-5)+' '+(sb+9)+' L'+(x1-1)+' '+(sb+10)+' L'+(x1-1)+' '+(g-.4)+' L'+(x1-5)+' '+(g-.4)+' Z','#ffd98a')+'</g>';
    var st='';
    for(i=0;i<8;i++) st+=rc(x0+8+i*7,sb+22,1,8,'var(--p-char-d)')+'<ellipse cx="'+(x0+8.5+i*7)+'" cy="'+(sb+22)+'" rx="2.4" ry="1" fill="var(--p-verm-d)"/>';
    o+='<g class="noedge">'+rc(x0+3,sb+19,w*.46,2,'var(--p-kraft-d)')+st
      +ln('M'+(x0+3)+' '+(sb+9)+' v21 M'+(x0+3+w*.23)+' '+(sb+9)+' v21 M'+(x0+w*.52)+' '+(sb+9)+' v21 M'+(x0+w*.74)+' '+(sb+9)+' v21 M'+(x0+w*.96)+' '+(sb+9)+' v21','var(--p-char-d)',1.2)
      +ln('M'+(x1-3)+' '+(sb+10)+' v'+(g-sb-10),'var(--p-char-d)',.8)+'</g>';
    return o;
  }
  // the side wall up Longwood, in shadow, with the painted sign that outlived the store
  function sparrsSide(x){
    var o=daQuad(x,96,DA.g,0,.46,'var(--p-brick-d)')+daQuad(x,92,96.6,0,.46,'#8d8472');
    o+='<g class="noedge">'+daQuad(x,101,104,.04,.4,'#5e3024')+'</g>';
    o+='<g class="noedge">'+daWallText("SPARR’S",x,96,DA.g,.03,.2,6.4,'#efe0bd',.62)+daWallText('DRUG',x,96,DA.g,.07,.4,6.4,'#efe0bd',.62)+daWallText('Rx',x,96,DA.g,.1,.64,9,'#efe0bd',.55)+'</g>';
    [.12,.3].forEach(function(t){ o+='<g class="noedge">'+daQuad(x,106,115,t,t+.06,'var(--p-char-d)')+'</g>'; });
    return o;
  }
  // MassArt's Tower Building: poured concrete, ribbed, studios lit late
  function massArt(x0,x1){
    var top=-44, g=DA.g, o='', r=skR(83), L='';
    o+=daQuad(x0,top,g,0,.34,'#6d6a64');
    o+=rc(x0,top,x1-x0,g-top,'#8e8a82')+rc(x0-1,top-3,x1-x0+2,3.4,'#77736c');
    var fins='', bands='', win='';
    for(var fy=top+6;fy<g-16;fy+=13){ bands+='M'+x0+' '+fy+' h'+(x1-x0)+' ';
      for(var fx=x0+3;fx<x1-6;fx+=9){ if(r()<.18) L+=lr(fx,fy+2.6,6,8.4); else win+='<rect x="'+fx+'" y="'+(fy+2.6)+'" width="6" height="8.4" fill="#2c2e36"/>'; } }
    for(var fx2=x0+1.6;fx2<x1;fx2+=9) fins+='M'+fx2.toFixed(1)+' '+top+' V'+(g-14)+' ';
    o+='<g class="noedge">'+win+ln(bands,'#6d6a64',1.2)+ln(fins,'#a6a299',1.4)+'</g>'+'<g class="lit glow" opacity=".9">'+L+'</g>';
    o+=rc(x0,g-14,x1-x0,14,'#5d5a55')+'<g class="lit glow">'+lr(x0+6,g-11,x1-x0-12,10)+'</g>'+'<g class="noedge">'+ln('M'+(x0+20)+' '+(g-11)+' v10 M'+(x0+40)+' '+(g-11)+' v10 M'+(x0+60)+' '+(g-11)+' v10','#3a3834',1)+'</g>';
    return o;
  }
  // MassArt's lower block along Huntington, and the older brick further on
  function lowBlocks(){
    var o=rc(232,112,120,38,'#8a4a36')+rc(231,108,122,4.4,'#b9ad93'), L='', r=skR(91);
    for(var i=0;i<9;i++) for(var j=0;j<2;j++){ var x=238+i*13, y=116+j*16; if(r()<.3) L+=lr(x,y,8,10); else o+='<rect x="'+x+'" y="'+y+'" width="8" height="10" fill="#2a2427"/>'; }
    o+='<g class="lit glow">'+L+'</g>';
    o+='<g transform="translate(352 30) scale(.82)">'+shop(0,116,70,2,8,'var(--p-brick)','var(--p-brick-d)','var(--p-bone-d)',1)+shop(76,134,60,1,8,'var(--p-terra)','var(--p-terra-d)','var(--p-cream-d)',0)+shop(142,106,80,3,8,'var(--p-brick-d)','var(--p-char-d)','var(--p-bone-d)',2)+'</g>';
    o+=rc(-130,104,52,46,'var(--p-terra-d)')+rc(-131,100,54,4.4,'var(--p-bone-d)')+'<g class="noedge" fill="#2a2427">'+win(-124,108,3,2,8,10,8,6)+'</g>'+'<g class="lit glow">'+lr(-124,134,40,14)+'</g>';
    return o;
  }
  // Longwood Avenue running away to the medical area: the road, both
  // sidewalks, the street trees and lamps getting smaller, the lit end
  function longwood(){
    var o='', a=daP(74,153,0), b=daP(74,153,.82), c=daP(138,153,.82), d=daP(138,153,0);
    o+=P('M'+a[0]+' '+a[1]+' L'+b[0].toFixed(1)+' '+b[1].toFixed(1)+' L'+c[0].toFixed(1)+' '+c[1].toFixed(1)+' L'+d[0]+' '+d[1]+' Z','#2a2c33');
    var sl=daP(70,150,0), sl2=daP(70,150,.82), sr=daP(142,150,0), sr2=daP(142,150,.82);
    o+=P('M'+sl[0]+' '+sl[1]+' L'+sl2[0].toFixed(1)+' '+sl2[1].toFixed(1)+' L'+b[0].toFixed(1)+' '+b[1].toFixed(1)+' L'+a[0]+' '+a[1]+' Z','#5b5a5c')+P('M'+sr[0]+' '+sr[1]+' L'+sr2[0].toFixed(1)+' '+sr2[1].toFixed(1)+' L'+c[0].toFixed(1)+' '+c[1].toFixed(1)+' L'+d[0]+' '+d[1]+' Z','#5b5a5c');
    var cl=daP(106,153,0), cl2=daP(106,153,.82);
    o+='<g class="noedge">'+ln('M'+cl[0]+' '+cl[1]+' L'+cl2[0].toFixed(1)+' '+cl2[1].toFixed(1),'#8f8a6a',.6,.6)+'</g>';
    // the end of the avenue: the medical area at night, a white columned front
    var e=daP(106,150,.86);
    o+=rc(e[0]-12,e[1]-12,24,12,'#3a3b44')+rc(e[0]-6,e[1]-7,12,7,'#d9d4c4')+'<g class="noedge">'+ln('M'+(e[0]-4.6)+' '+(e[1]-7)+' v7 M'+(e[0]-2)+' '+(e[1]-7)+' v7 M'+(e[0]+.6)+' '+(e[1]-7)+' v7 M'+(e[0]+3.2)+' '+(e[1]-7)+' v7','#9e998b',.5)+rc(e[0]-7,e[1]-8.4,14,1.6,'#e8e2d2')+'</g>';
    // street trees and lamps, both sides, receding
    [.14,.34,.52,.66,.76].forEach(function(t,i){
      [72.4,139.6].forEach(function(x,k){ var p=daP(x,150,t), h=30*(1-t);
        if((i+k)%2===0){ o+='<g class="noedge">'+rc(p[0]-.5*(1-t),p[1]-h*.5,1.1*(1-t)+.3,h*.5,'#2b211c')+'<ellipse cx="'+p[0].toFixed(1)+'" cy="'+(p[1]-h*.66).toFixed(1)+'" rx="'+(h*.26).toFixed(1)+'" ry="'+(h*.24).toFixed(1)+'" fill="#26352c"/><ellipse cx="'+(p[0]-h*.08).toFixed(1)+'" cy="'+(p[1]-h*.72).toFixed(1)+'" rx="'+(h*.16).toFixed(1)+'" ry="'+(h*.13).toFixed(1)+'" fill="#324437"/></g>'; }
        else { o+='<g class="noedge">'+rc(p[0]-.3,p[1]-h*.8,.7*(1-t)+.2,h*.8,'#3e4e5d')+'</g><g class="lit glow"><ellipse cx="'+(p[0]+(k?-1:1)*h*.08).toFixed(1)+'" cy="'+(p[1]-h*.8).toFixed(1)+'" rx="'+(h*.07+.3).toFixed(1)+'" ry="'+(h*.03+.2).toFixed(1)+'"/></g>'; }
      }); });
    return o;
  }
  // Huntington Avenue: far lanes, the E branch in its median, near lanes
  function huntington(){
    var o=rc(-130,150,660,3.2,'var(--p-granite-d)')+rc(-130,153,660,29,'#23252c');
    o+='<g class="noedge">'+rc(-130,160,660,6.4,'#34363d')+rc(-130,159.4,660,.8,'#8e8a7c')+rc(-130,166,660,.8,'#8e8a7c')
      +ln('M-130 161.4 h660 M-130 163 h660 M-130 164.2 h660 M-130 165.4 h660','#77736a',.45,.9)
      +ln('M-130 156.4 h660','#d9c67a',.6,.5)+ln('M-130 174 h660','#d9c67a',.7,.55)+'</g>';
    // catenary poles on the median and the wire over the rails
    var cp='';
    for(var x=-110;x<530;x+=74) cp+=rc(x,112,1.4,49,'#3e4e5d')+rc(x-6,114,13,1,'#3e4e5d');
    o+=cp+'<g class="noedge">'+ln('M-130 118 h660','#1d1f24',.5)+ln('M-130 114.6 h660','#1d1f24',.35,.8)+'</g>';
    return o;
  }
  function deadAntsCorner(){
    var o='';
    // the distant city (kept from v42), behind everything
    o+=DA_FAR;
    o+=haze(.3);
    o+='<g class="ly2">'+lowBlocks()+longwood()+'</g>'+haze(.08);
    o+='<g class="ly2">'+massArt(142,232)+sparrsFront(-78,70)+sparrsSide(70)+'</g>';
    // a cobrahead over each sidewalk corner, sodium
    o+='<g class="ly2">'+pole(24,86,64,-22,true)+pole(400,86,64,-22,true)+'</g>';
    o+='<g class="ly3">'+huntington()+'</g>';
    o+='<g class="ly3">'+mbtaBus(248,157)+curb(-124,182,648,4)+brickwalk(-124,186,648,14)+busstop(374,142)
      +payphone(80,196)+payphone(94,196)+payphone(108,196)
      +figure(126,198,38,{felt:'cyan',dir:1,arm:'watch',coat:'var(--p-indigo)',coatD:'var(--p-indigo-d)',legs:'var(--p-char-d)',hair:'var(--p-char-d)'})
      +figure(158,198,38,{felt:'magenta',dir:-1,stride:9,coat:'var(--p-verm)',coatD:'var(--p-verm-d)',legs:'var(--p-indigo-d)',shoe:'var(--p-white)',hair:'var(--p-timber)'})+'</g>';
    o+='<g class="noedge keylight">'+'<defs><radialGradient id="kl3"><stop offset="0" stop-color="#ffb860" stop-opacity="0.5"/><stop offset=".55" stop-color="#ffb860" stop-opacity="0.175"/><stop offset="1" stop-color="#ffb860" stop-opacity="0"/></radialGradient></defs><ellipse cx="141" cy="192" rx="40" ry="14" fill="url(#kl3)"/></g>';
    o+='<g class="fx noedge">'
      +'<ellipse cx="141" cy="195" rx="16" ry="3.4" fill="#ffb054" opacity=".30"/><ellipse cx="141" cy="195.6" rx="7" ry="1.6" fill="#ffd28a" opacity=".5"/>'
      +'<g class="crawl antnow"><g transform="translate(141 195.2) scale(.34) translate(-141 -195.2)">'+ant(141,194.6)+'</g></g>'
      +'<rect class="pulse mid" x="-78" y="118" width="142" height="7" fill="#ff9a5c" opacity=".3"/>'
      +'<circle class="pulse" cx="364" cy="177" r="4" fill="#fff2b0" opacity=".5"/>'
      +'<ellipse cx="42" cy="152" rx="26" ry="3" fill="#ffcf7a" opacity=".28"/><ellipse cx="382" cy="152" rx="26" ry="3" fill="#ffcf7a" opacity=".28"/>'
      +'</g>';
    return o;
  }
