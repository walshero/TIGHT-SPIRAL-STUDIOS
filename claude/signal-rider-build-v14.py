#!/usr/bin/env python3
"""Signal Rider v0.14: a guided path through the week's categories.
Founder 2026-11-08: "the natural path is to drill down in the first box and then play the week
instead of having a chance to review all categories." Ruling 15:00: "1 rec." =
Next-category button in each category, Ride hidden inside categories, progress line,
"Skip to review", and a Your week review screen that names categories not looked at.
Base: canon v0.13 (c2ac6d05)."""
import hashlib
P = 'lab/down-the-nerve.html'
s = open(P).read()
assert hashlib.sha256(s.encode()).hexdigest().startswith('c2ac6d05'), 'base is not canon v0.13'
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)

rep('<title>Signal Rider v0.13</title>', '<title>Signal Rider v0.14</title>')
rep('<span class="chip">v0.13</span>', '<span class="chip">v0.14</span>')

# the ride row can be hidden while a category is open
rep('<div class="row" style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn primary" id="bRide"',
    '<div class="row" id="rideRow" style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn primary" id="bRide"')

# state: which categories this visit has opened
rep('var trayCat=null,infoId=null;', 'var trayCat=null,infoId=null,seenCats={};')

# opening a category from the list marks it seen
rep("b.onclick=function(){trayCat=c.id;infoId=null;buildCards();var f=document.querySelector('#cards .back');if(f)f.focus();};box.appendChild(b);});});",
    "b.onclick=function(){openCat(c.id);};box.appendChild(b);});});")

# the category view: progress line on top; Next and Skip to review at the bottom
rep("""    var bk=document.createElement('button');bk.type='button';bk.className='btn back';bk.textContent='All categories';bk.onclick=function(){trayCat=null;buildCards();};box.appendChild(bk);
    var h=document.createElement('div');h.className='cath';h.innerHTML='<h3>'+c.name+'</h3><p>'+c.intro+'</p><p><b>In the game:</b> '+c.fx+'</p>';box.appendChild(h);""",
"""    if(trayCat==='review'){buildReview(box);document.getElementById('rideRow').style.display='flex';drawTrayBal(weekModel(week));return;}
    var c=catOf(trayCat);
    var bk=document.createElement('button');bk.type='button';bk.className='btn back';bk.textContent='All categories';bk.onclick=function(){trayCat=null;buildCards();};box.appendChild(bk);
    var pg=document.createElement('p');pg.className='sub prog';pg.textContent=progLine();box.appendChild(pg);
    var h=document.createElement('div');h.className='cath';h.innerHTML='<h3 tabindex="-1">'+c.name+'</h3><p>'+c.intro+'</p><p><b>In the game:</b> '+c.fx+'</p>';box.appendChild(h);""")
rep("""var c=catOf(trayCat);
    if(trayCat==='review')""", "if(trayCat==='review')")
rep("""inf.innerHTML=infoHTML(shown);box.appendChild(inf);
  }""",
"""inf.innerHTML=infoHTML(shown);box.appendChild(inf);
    var ix=CATS.indexOf(c),nx=CATS[ix+1],nav=document.createElement('div');nav.className='catnav';
    var nb=document.createElement('button');nb.type='button';nb.className='btn primary nextcat';
    nb.textContent=nx?'Next: '+nx.name:'Review your week';nb.onclick=function(){nx?openCat(nx.id):openReview();};nav.appendChild(nb);
    if(nx){var sk=document.createElement('button');sk.type='button';sk.className='btn';sk.textContent='Skip to review';sk.onclick=openReview;nav.appendChild(sk);}
    box.appendChild(nav);
  }
  document.getElementById('rideRow').style.display=(trayCat&&trayCat!=='review')?'none':'flex';""")

# helpers: open a category, progress line, review screen
rep("var trayOpen=false;",
"""function openCat(id){trayCat=id;infoId=null;seenCats[id]=true;buildCards();var f=document.querySelector('#cards .cath h3');if(f)f.focus();}
function openReview(){trayCat='review';buildCards();var f=document.querySelector('#cards .cath h3');if(f)f.focus();}
function progLine(){var r=CATS.filter(function(c){return c.t==='r';}),g=CATS.filter(function(c){return c.t!=='r';});
  var sr=r.filter(function(c){return seenCats[c.id];}).length,sg=g.filter(function(c){return seenCats[c.id];}).length;
  return 'Stress '+sr+' of '+r.length+' looked at. Support '+sg+' of '+g.length+'.';}
function buildReview(box){
  var bk=document.createElement('button');bk.type='button';bk.className='btn back';bk.textContent='All categories';bk.onclick=function(){trayCat=null;buildCards();};box.appendChild(bk);
  var picked=DECK.filter(function(d){return week[d.id];}),unseen=CATS.filter(function(c){return !seenCats[c.id];});
  var h=document.createElement('div');h.className='cath';
  h.innerHTML='<h3 tabindex="-1">Your week</h3><p>'+(picked.length?'These blocks will be on the ride. Tap one to take it out. The panel above shows what this week will change.':'No blocks yet. With an empty week the ride is a calm road.')+'</p>'
    +(unseen.length?'<p><b>Not looked at:</b> '+unseen.map(function(c){return c.name;}).join(', ')+'.</p>':'<p>You looked at every category.</p>');
  box.appendChild(h);
  picked.forEach(function(d){var b=document.createElement('button');b.type='button';b.className='wk '+(d.t==='r'?'red':'grn');b.setAttribute('aria-pressed','true');
    b.innerHTML=cubeSvg(d)+'<span>'+d.label+'<small>'+catOf(d.cat).name+'. Tap to remove</small></span>';b.setAttribute('aria-label',d.label+', in your week. Remove');
    b.onclick=function(){week[d.id]=false;tone(340,0.08,'triangle',0.07);buildCards();};box.appendChild(b);});
  if(unseen.length){var go=document.createElement('button');go.type='button';go.className='btn';go.textContent='Look at '+unseen[0].name;go.onclick=function(){openCat(unseen[0].id);};
    var w=document.createElement('div');w.className='catnav';w.appendChild(go);box.appendChild(w);}
}
var trayOpen=false;""")

# each visit to the tray starts a fresh walk
rep("function openTray(){trayOpen=true;buildCards();", "function openTray(){trayOpen=true;trayCat=null;seenCats={};buildCards();")

# layout: nav row spans the grid; big, same place every time
rep(".cath h3{margin:4px 0;font-size:20px}",
    ".cath h3{margin:4px 0;font-size:20px}\n.catnav{grid-column:1/-1;display:flex;gap:10px;flex-wrap:wrap;margin:8px 0 2px}.catnav .btn{min-height:52px;font-size:19px}.nextcat{flex:1 1 220px}.prog{grid-column:1/-1;margin:2px 0}")

open(P, 'w').write(s)
print('ok', len(s.encode()), hashlib.sha256(s.encode()).hexdigest())
