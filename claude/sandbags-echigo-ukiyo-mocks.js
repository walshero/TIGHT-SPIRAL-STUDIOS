  /* UKIYO-E MOCK-UPS (founder 09-26: "Echigo scene doesn't feel like a
     photograph. An award winning photo. Keep our paper cut but think ukiyo-e
     style layout. Give me three mock ups"). Each composition fills the whole
     sky box in a 400 x 250 frame. On a phone the frame crops to its middle
     (about x 105 to 295), which is the tall oban format of Hiroshige's One
     Hundred Views; on a desktop it opens out to the wide Tokaido format.
     Story subjects sit between x 105 and 160, the one band the balloon
     covers on neither screen. */
  var UK={ sumi:'#22252b', prussian:'#2d4a68', prussianL:'#4f6f88', indigo:'#26365a', paper:'#e6dcc3' };
  function ukGrad(id,stops,x,y,w,h,extra){
    var s=''; stops.forEach(function(t){ s+='<stop offset="'+t[0]+'" stop-color="'+t[1]+'"'+(t[2]!=null?' stop-opacity="'+t[2]+'"':'')+'/>'; });
    return '<defs><linearGradient id="'+id+'" x1="0" y1="0" x2="0" y2="1">'+s+'</linearGradient></defs><rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="url(#'+id+')"'+(extra||'')+'/>';
  }
  function ukGlow(id,cx,cy,rx,ry,col,op){
    return '<defs><radialGradient id="'+id+'"><stop offset="0" stop-color="'+col+'" stop-opacity="'+op+'"/><stop offset="1" stop-color="'+col+'" stop-opacity="0"/></radialGradient></defs><ellipse cx="'+cx+'" cy="'+cy+'" rx="'+rx+'" ry="'+ry+'" fill="url(#'+id+')"/>';
  }
  // Hiroshige's rain: long, fine, parallel, the whole height of the sheet
  function ukRain(seed,n,x0,x1,y0,y1,ang,len,col,w){
    var r=tssR(seed), d='';
    for(var i=0;i<n;i++){ var x=x0+r()*(x1-x0), y=y0+r()*(y1-y0), l=len*(.6+r()*.8);
      d+='M'+x.toFixed(1)+' '+y.toFixed(1)+' l'+(l*Math.sin(ang)).toFixed(1)+' '+(l*Math.cos(ang)).toFixed(1)+' '; }
    return '<g class="noedge urain">'+ln(d,col,w)+'</g>';
  }
  // a ridge of cedar forest cut as one sheet, stippled with spires
  function ukForest(d,id,seed,base,cols,y0,y1,step){
    var r=tssR(seed), o='';
    for(var y=y0;y<y1;y+=step*.8) for(var x=-20+r()*step;x<420;x+=step*(.8+r()*.7)){
      var h=step*(1.3+r()*.8), w=h*.4;
      if(r()<.03){ o+='<ellipse cx="'+x.toFixed(1)+'" cy="'+(y+h*.6).toFixed(1)+'" rx="'+(w*1.3).toFixed(1)+'" ry="'+(h*.35).toFixed(1)+'" fill="'+(r()<.5?'#8f4a34':'#a8733c')+'"/>'; continue; }
      o+='<path d="M'+x.toFixed(1)+' '+y.toFixed(1)+' l'+w.toFixed(1)+' '+h.toFixed(1)+' h-'+(2*w).toFixed(1)+' z" fill="'+cols[(r()*cols.length)|0]+'"/>';
    }
    return P(d,base)+'<defs><clipPath id="'+id+'"><path d="'+d+'"/></clipPath></defs><g class="noedge" clip-path="url(#'+id+')">'+o+'</g>';
  }
  // a snow-country house for a street seen in depth: drawn at unit size about
  // its own ground point, then placed and scaled, nearest largest
  var UKV=[['var(--p-cedar)','var(--p-cedar-d)','var(--p-char)','var(--p-char-d)',.5,1],
           ['var(--p-cream)','var(--p-cream-d)','var(--p-tinblue)','var(--p-tinblue-d)',.3,1],
           ['var(--p-cedar)','var(--p-cedar-d)','var(--p-tinred)','var(--p-tinred-d)',.5,0],
           ['var(--p-bone)','var(--p-bone-d)','var(--p-tingreen)','var(--p-tingreen-d)',.7,1],
           ['var(--p-cedar-d)','var(--p-timber)','var(--p-steel)','var(--p-steel-d)',.5,1]];
  function ukHouse(X,G,s,k,lit){
    var V=UKV[k%5], w=40, h=30;
    return '<g transform="translate('+X+' '+G+') scale('+s+')">'+snowGable(-w/2,-h,w,h,34,8,V[0],V[1],V[2],V[3],5,V[4],V[5])
      +(V[0].indexOf('cedar')>0?cedar(-w/2,-h,w,h):'')+fw(-13,-25,8,7,lit&1)+fw(5,-25,8,7,lit&2)+koshi(-14,-12,28,9,lit&4?1:0)+'</g>';
  }
  // the noodle shop at unit size: cream plaster, dark tile, lit upstairs, the
  // window of plastic ramen and the indigo noren at street level
  function ukShop(X,G,s){
    var w=40, h=30, o=snowGable(-w/2,-h,w,h,34,8,'var(--p-cream)','var(--p-cream-d)','var(--p-char)','var(--p-char-d)',5,.5,0)
      + timber(-w/2,-h,w,h-1,'var(--p-timber)')+fw(-13,-25,8,7,1)+fw(5,-25,8,7,1);
    o+='<g class="lit glow">'+lr(-17,-12,17,11)+'</g>'
      +'<g class="noedge">'+rc(-18,-13,19,1.2,'var(--p-timber-d)')+'<ellipse cx="-13" cy="-3.2" rx="3" ry="1.7" fill="var(--p-cream)"/><ellipse cx="-6" cy="-3.2" rx="3" ry="1.7" fill="var(--p-cream)"/>'
      +'<ellipse cx="-13" cy="-4" rx="3" ry=".8" fill="var(--p-terra)"/><ellipse cx="-6" cy="-4" rx="3" ry=".8" fill="var(--p-terra)"/>'
      +ln('M-14 -4.6 l2.6 -5 M-12.6 -4.6 l2.6 -5 M-7 -4.6 l2.6 -5 M-5.6 -4.6 l2.6 -5','var(--p-kraft-d)',.5)+'</g>'
      +noren(3,-12,14,'var(--p-indigo)');
    return '<g transform="translate('+X+' '+G+') scale('+s+')">'+o+'</g>';
  }
  function ukLean(svg,x,y,a){ return '<g transform="rotate('+a+' '+x+' '+y+')">'+svg+'</g>'; }
  // the studio seal, where a print carries the artist's
  function ukSeal(x,y,s){
    return '<g class="noedge" transform="translate('+x+' '+y+') scale('+s+')"><rect x="0" y="0" width="48" height="48" rx="4" fill="#a8391f"/><use href="#tss-spiral" style="stroke:#f1e4c8;stroke-width:3.6;fill:none"/></g>';
  }
  function narrator(x,y,s){ return figure(x,y,s,{felt:'yellow',coat:'var(--p-char)',coatD:'var(--p-char-d)',legs:'var(--p-char-d)',hair:'var(--p-bone)'}); }

  /* A. SUDDEN SHOWER (after Hiroshige, "Sudden Shower over Shin-Ohashi Bridge
     and Atake", 1857). Seen from above. The black cloud band across the top,
     the street a long diagonal from the near corner to the far end of town,
     the villagers leaning into the rain, the river below the embankment with
     one boatman. The noodle shop is the second house, lit, at the third. The
     Shinkansen crosses the far valley on its viaduct like Hiroshige's bridge. */
  function ukA(){
    var F=function(x){ return 214-.185*x; }, N=function(x){ return 262-.26*x; }, o='';
    o+=ukGrad('ukAsky',[[0,'#1b232d'],[.1,'#2e3a47'],[.2,'#7c8680'],[.42,'#cfcbb7'],[1,'#d9d3bd']],-10,-10,420,270);
    o+='<g class="ly1">'+P('M-10 150 L30 112 L70 126 L118 84 L160 104 L214 70 L262 98 L300 86 L344 112 L380 96 L410 118 L410 170 L-10 170 Z','#8b958e')+'</g>';
    o+=ukGrad('ukAmist',[[0,'#cfcbb7',0],[1,'#cfcbb7',.7]],-10,90,420,60);
    o+='<g class="ly1">'+ukForest('M-10 160 L20 130 L52 142 L96 116 L140 136 L186 112 L236 134 L280 118 L326 138 L372 124 L410 140 L410 190 L-10 190 Z','ukAf',5,'#3d5440',['#2f4633','#4a6444','#3a5239'],110,190,4.2)+'</g>';
    // the viaduct across the valley, and the E7 on it
    o+='<g class="ly2">'+rc(-10,117,420,2.6,'var(--p-granite)')+rc(-10,119.6,420,1,'var(--p-granite-d)');
    for(var px=4;px<410;px+=26) o+=rc(px,120,2.4,26,'var(--p-granite-d)');
    o+='</g>'+shinkansen(190,117);
    // the river, below the embankment
    o+='<g class="ly2">'+P('M-10 262 L-10 250 L400 150 L410 150 L410 262 Z','#2d4a68')+'</g>';
    o+='<g class="noedge">'+ukGrad('ukAriv',[[0,'#6f8ea3',.5],[1,'#2d4a68',0]],-10,150,420,112,' clip-path="url(#ukArc)"')
      +'<defs><clipPath id="ukArc"><path d="M-10 262 L-10 250 L400 150 L410 150 L410 262 Z"/></clipPath></defs>'
      +ln('M260 214 h60 M300 226 h70 M232 238 h54 M330 200 h40 M350 186 h40 M280 246 h80','#8fb0c3',.7,.55)+'</g>';
    // the boatman under his straw hat, poling a raft downstream
    o+='<g class="ly3">'+P('M300 222 h64 l-4 4 h-58 z','var(--p-timber)')+'<g class="noedge">'+ln('M326 222 l-14 -26','var(--p-kraft-d)',1)+'</g>'
      +P('M321 222 l1.6 -10 h4 l1.6 10 z','var(--p-steel-d)')+P('M318.6 212.4 L324.6 207 L330.6 212.4 Z','var(--p-thatch)')+'</g>';
    // the street and the embankment wall
    o+='<g class="ly2">'+P('M-10 216 L400 140 L410 140 L410 158 L400 158 L-10 264 Z','#56606a')+'</g>';
    o+='<g class="ly3">'+P('M-10 264 L400 158 L410 158 L410 162 L400 162 L-10 270 Z','var(--p-granite-d)')+'</g>';
    // the town along the far side of the street, nearest largest
    var H=[[384,.46,3,1],[362,.54,1,2],[336,.64,4,5],[302,.76,0,1],[258,.92,2,4],[214,1.06,1,2],[14,1.62,3,1],[68,1.46,4,6]], t='';
    H.forEach(function(h,i){ t+=ukHouse(h[0],F(h[0]),h[1],h[2],h[3]); });
    t+=ukShop(135,F(135),1.32);
    o+='<g class="ly3">'+t+'</g>';
    // wet street: the shop's window laid on the stones
    o+='<g class="noedge">'+ukGlow('ukAg',128,F(135)+12,34,10,'#ffcf7a',.55)+rc(112,F(135)+2,4,18,'#ffd58a',' opacity=".35"')+rc(124,F(135)+4,3,16,'#ffd58a',' opacity=".28"')+'</g>';
    // people, leaning into the rain; he stands still, bare-headed
    var pp='';
    pp+=ukLean(villager(62,N(62)-10,30,'var(--p-indigo)','var(--p-gold)','var(--p-verm)','var(--p-cream)','cyan'),62,N(62)-10,-9);
    pp+=ukLean(villager(240,F(240)+13,17,'var(--p-plum)','var(--p-cream)','var(--p-indigo)','var(--p-bone)','pink'),240,F(240)+13,-9);
    pp+=ukLean(villager(300,F(300)+11,14,'var(--p-moss-d)','var(--p-cream)','var(--p-tingreen)','var(--p-bone)','orange'),300,F(300)+11,-8);
    pp+=ukLean(villager(346,F(346)+9,11,'var(--p-char)','var(--p-terra)','#c9b48a','var(--p-bone-d)','purple'),346,F(346)+9,-8);
    pp+=narrator(152,F(152)+17,30);
    o+='<g class="ly3">'+pp+'</g>';
    o+='<g class="fx noedge"><g transform="translate(135 '+F(135)+') scale(1.32)">'+chochin(-18,-12.6)+chochin(18,-12.6)+'</g></g>';
    // two sheets of rain, crossing, as Hiroshige cut them
    o+=ukRain(7,150,-40,420,-20,240,.16,70,'rgba(38,44,52,.55)',.55)+ukRain(9,90,-40,420,-20,240,.06,60,'rgba(236,240,228,.45)',.5);
    o+=ukSeal(108,44,.26);
    return o;
  }

  /* B. THROUGH THE NOREN (after Hiroshige's near-far prints, "Plum Garden at
     Kameido" and "Horikiri Iris Garden", 1857). We are inside the noodle
     shop. The eave beam and the indigo noren crop the top, a lantern hangs
     huge in front of us, the counter runs along the bottom with a real bowl
     steaming on it, and through the doorway the street is cold and blue:
     the rain, the houses across the way, the mountain, the Shinkansen passing
     behind the roofs. He is out in the rain, about to come in. Warm inside,
     cold outside, which is the whole piece. */
  function ukB(){
    var o='';
    // outside, through the doorway
    o+=ukGrad('ukBsky',[[0,'#6c7b86'],[.45,'#98a4a6'],[.7,'#c1c3b4'],[1,'#c9c8b6']],-10,-10,420,270);
    o+='<g class="ly1">'+ukForest('M-10 120 L30 88 L74 104 L120 62 L168 92 L214 58 L262 90 L312 72 L356 98 L410 80 L410 190 L-10 190 Z','ukBf',11,'#40573f',['#324a36','#4f6947','#3d553b','#56704d'],56,190,4.4)+'</g>';
    o+=ukGrad('ukBmist',[[0,'#c1c3b4',0],[1,'#c1c3b4',.75]],-10,96,420,44);
    o+='<g class="ly2">'+rc(-10,128,420,2.4,'var(--p-granite)')+rc(-10,130.4,420,1,'var(--p-granite-d)')+'</g>'+shinkansen(120,128);
    var t=''; [[26,1,0,1.06],[80,3,2,.9],[196,2,5,1.14],[252,4,1,.94],[322,0,1,1.1],[380,1,2,.88]].forEach(function(h){ t+=ukHouse(h[0],176,h[3],h[1],h[2]); });
    t+=kura(112,154,34,22,6)+sugidama(128,152);
    o+='<g class="ly2">'+t+'</g>';
    o+='<g class="ly3">'+rc(-10,176,420,42,'#4b5560')+'</g><g class="noedge">'+ln('M-10 186 h420 M-10 198 h420','#6d7780',.6,.6)+rc(58,178,6,34,'#ffd58a',' opacity=".18"')+rc(138,178,6,34,'#ffd58a',' opacity=".18"')+rc(258,178,6,34,'#ffd58a',' opacity=".18"')+'</g>';
    var pp=ukLean(villager(92,206,26,'var(--p-plum)','var(--p-cream)','var(--p-indigo)','var(--p-bone)','pink'),92,206,-6)
      +ukLean(villager(250,203,24,'var(--p-indigo-d)','var(--p-verm)','var(--p-cream)','var(--p-kraft-d)','coral'),250,203,5)
      +ukLean(villager(318,205,25,'var(--p-moss-d)','var(--p-cream)','var(--p-tingreen)','var(--p-bone)','orange'),318,205,-6)
      +narrator(146,210,36);
    o+='<g class="ly3">'+pp+'</g>';
    o+=ukRain(21,140,-30,420,40,215,.1,64,'rgba(236,240,228,.5)',.55)+ukRain(23,60,-30,420,40,215,.1,50,'rgba(40,48,56,.35)',.5);
    // inside: the frame, warm, a touch soft because the lens is focused on the street
    o+='<defs><filter id="ukBdof" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation=".7"/></filter></defs>';
    var fr='';
    fr+=rc(-10,-10,420,30,'#2a2019')+rc(-10,18,420,3,'#4b3a2b');
    for(var i=0;i<6;i++){ var nx=-6+i*70; fr+=rc(nx,21,66,46,UK.indigo); fr+='<g class="noedge">'+rc(nx,21,66,5,'#1c2946')+'<circle cx="'+(nx+33)+'" cy="44" r="7.5" fill="none" style="stroke:#e6dcc3;stroke-width:2.2"/></g>'; }
    fr+=rc(-10,-10,22,270,'#2a2019')+rc(12,-10,3,270,'#4b3a2b');
    fr+=rc(356,21,54,197,'#3a2c20');
    o+='<g class="ly3" filter="url(#ukBdof)">'+fr+'</g>'+'<g class="lit" filter="url(#ukBdof)">'+lr(362,70,44,140)+'</g><g class="noedge" filter="url(#ukBdof)">'+ln('M370 70 v140 M377 70 v140 M384 70 v140 M391 70 v140 M398 70 v140 M362 98 h44 M362 126 h44 M362 154 h44 M362 182 h44','#4b3a2b',.8)+rc(380.4,70,1.6,140,'#4b3a2b')+'</g>';
    // the counter, and the bowl on it
    o+='<g class="ly3">'+rc(-10,214,420,6,'#b98f5c')+rc(-10,220,420,40,'#5a3b25')+'</g><g class="noedge">'+rc(-10,214,420,1.4,'#e0c08e')+'</g>';
    o+='<g class="ly3">'+P('M96 214 q0 20 30 20 q30 0 30 -20 z','#efe3c6')+P('M100 222 q6 12 26 12 q20 0 26 -12 z','#b8452e')+'</g>'
      +'<g class="noedge"><ellipse cx="126" cy="214" rx="30" ry="5" fill="#d9a24a"/><ellipse cx="118" cy="213.4" rx="7" ry="2" fill="#f3ead2"/><ellipse cx="134" cy="214.2" rx="5" ry="1.6" fill="#6f7f55"/>'+ln('M150 216 l40 -16 M152 218 l40 -15','#8f6c43',1.4)+'</g>';
    o+='<g class="fx noedge"><g transform="translate(58 -24) scale(1.1)">'
      +'<path class="steam" d="M58 216 q-3 -6 0 -12 q3 -6 0 -12" fill="none" style="stroke:rgba(250,244,230,.85);stroke-width:1.8;stroke-linecap:round"/>'
      +'<path class="steam" d="M64 216 q3 -6 0 -12 q-3 -6 0 -12" fill="none" style="stroke:rgba(250,244,230,.85);stroke-width:1.8;stroke-linecap:round"/>'
      +'<path class="steam" d="M70 216 q-3 -6 0 -12 q3 -6 0 -12" fill="none" style="stroke:rgba(250,244,230,.85);stroke-width:1.8;stroke-linecap:round"/></g></g>';
    // the big lantern, close to the lens
    o+='<g class="noedge">'+ukGlow('ukBl',262,58,70,56,'#ffb86b',.45)+'</g>';
    o+='<g class="fx noedge"><g class="sway" filter="url(#ukBdof)">'+ln('M262 18 v12','#1c140e',1.2)
      +'<rect x="245" y="30" width="34" height="50" rx="15" fill="#d8452c"/><rect x="251" y="36" width="22" height="38" rx="10" fill="#ffb36b" opacity=".6"/>'
      +ln('M246 42 h32 M245 52 h34 M245 62 h34 M246 72 h32','#a8321e',.8,.8)
      +'<rect x="249" y="27" width="26" height="5" rx="1.4" fill="#1c140e"/><rect x="249" y="78" width="26" height="5" rx="1.4" fill="#1c140e"/></g></g>';
    // warm light from inside falls on the frame
    o+='<g class="noedge" style="mix-blend-mode:screen">'+ukGlow('ukBw',200,250,260,70,'#ffb866',.35)+'</g>';
    o+=ukSeal(20,226,.22);
    return o;
  }

  /* C. EVENING RAIN UNDER THE MOUNTAIN (after Kawase Hasui's rain prints and
     Hokusai's Fuji series). A low horizon; the mountain takes two thirds of
     the sheet in cedar and mist; the sky grades from night indigo to a pale
     break over the ridge. The village is a thin strip of lit windows at its
     foot, the Shinkansen slides along the base with its windows on, and the
     street is black and wet, every lantern laid on it as a long streak. He is
     small, bare-headed, looking up. Scale is the story. */
  function ukC(){
    var o='';
    o+=ukGrad('ukCsky',[[0,'#141d31'],[.22,'#2c3d5f'],[.46,'#6f7a95'],[.62,'#b8b2ab'],[1,'#b8b2ab']],-10,-10,420,270);
    o+='<g class="ly1">'+P('M-10 178 L40 152 L92 122 L128 100 L150 88 L176 58 L204 40 L222 44 L240 36 L262 58 L292 82 L310 80 L338 112 L372 134 L410 150 L410 200 L-10 200 Z','#5a6880')+'</g>';
    o+=ukGrad('ukCm1',[[0,'#b8b2ab',0],[.5,'#b8b2ab',.55],[1,'#b8b2ab',0]],-10,98,420,26);
    o+='<g class="ly1">'+ukForest('M-10 176 L28 150 L70 160 L112 128 L158 146 L200 118 L238 138 L286 122 L330 144 L372 134 L410 150 L410 205 L-10 205 Z','ukCf',17,'#243632',['#1d2e2a','#2f453c','#26392f','#3a5244'],114,205,4)+'</g>';
    o+=ukGrad('ukCm2',[[0,'#9aa0a6',0],[.5,'#9aa0a6',.45],[1,'#9aa0a6',0]],-10,150,420,22);
    o+='<g class="ly2">'+rc(-10,180,420,2.6,'var(--p-granite-d)');
    for(var px=4;px<410;px+=28) o+=rc(px,182,2.4,10,'#4a4f55');
    o+='</g>'+shinkansen(210,180);
    o+='<g class="ly2">'+village(-12,412,203,7,13,.7)+'</g>';
    var t=''; [[20,.9,2,3],[64,.86,4,1],[210,.88,1,6],[258,.84,3,1],[306,.9,0,3],[352,.86,2,2],[394,.9,4,1]].forEach(function(h){ t+=ukHouse(h[0],214,h[1],h[2],h[3]); });
    t+=ukShop(135,214,1.02);
    o+='<g class="ly3">'+t+'</g>';
    // the street, black and wet, every light laid on it
    o+='<g class="ly3">'+rc(-10,214,420,46,'#1b2028')+'</g>';
    var sp=''; [[125,'#ffd58a',.5,26],[141,'#ffd58a',.35,18],[117,'#ff8a5c',.4,20],[153,'#ff8a5c',.4,20],[22,'#ffd58a',.22,14],[210,'#ffd58a',.25,14],[306,'#ffd58a',.22,14],[258,'#ff8a5c',.28,12],[352,'#ffd58a',.2,12]].forEach(function(s){
      sp+='<rect x="'+(s[0]-2.6)+'" y="215" width="5.2" height="'+(s[3]*1.4)+'" fill="url(#ukCr)" opacity="'+Math.min(1,s[2]*1.8)+'"/>'; });
    o+='<defs><linearGradient id="ukCr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd58a" stop-opacity=".9"/><stop offset="1" stop-color="#ffd58a" stop-opacity="0"/></linearGradient><filter id="ukCb" x="-50%" y="-10%" width="200%" height="120%"><feGaussianBlur stdDeviation="1.2 2"/></filter></defs>';
    o+='<g class="noedge"><g filter="url(#ukCb)">'+sp+'</g>'+ukGlow('ukCg',135,214,40,8,'#ffcf7a',.45)+'</g>';
    o+='<g class="fx noedge"><g transform="translate(135 214) scale(1.02)">'+chochin(-18,-12.6)+chochin(18,-12.6)+'</g>'+chochin(258-15,202)+chochin(306+14,202)+'</g>';
    var pp=ukLean(villager(60,236,18,'var(--p-indigo)','var(--p-gold)','#c9b48a','var(--p-cream)','cyan'),60,236,-4)
      +ukLean(villager(292,232,16,'var(--p-plum)','var(--p-cream)','var(--p-verm)','var(--p-bone)','pink'),292,232,-4)
      +narrator(150,240,24);
    o+='<g class="ly3">'+pp+'</g>';
    o+=ukRain(31,170,-40,420,-10,250,.08,80,'rgba(214,222,236,.38)',.45);
    o+=ukSeal(382,232,.2);
    return o;
  }
