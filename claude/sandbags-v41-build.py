s=open('/tmp/tsp/sandbags.html').read()
js=open('/tmp/sb/roofs.js').read()
a=s.index('  /* v40 EVERY ROOF DIFFERENT'); b=s.index('\n  var SCENERY=[\n',a)
s=s[:a]+js.rstrip('\n')+s[b:]
note='''  v41 2026-09-26 (founder: "Use the real hiragana for ramen. What are the
  yellow and red ovals? If foliage, go real tree."). The noodle shop's hanging
  board, after the one in the Magome photograph, now reads らーめん top to
  bottom, stored as letter outlines from Noto Serif CJK JP Bold (OFL) so no
  font is needed on the device. The ovals were autumn maples in the cedar
  forest; each is now a tree: a forked trunk and a crown of red and amber lobes.
'''
i=s.index('  v40 2026-09-26'); s=s[:i]+note+'\n'+s[i:]
assert s.count('<span class="ver">v40')==1 and s.count('&middot; v40</p>')==1
s=s.replace('<span class="ver">v40','<span class="ver">v41').replace('&middot; v40</p>','&middot; v41</p>')
open('/tmp/sb/v41.html','w').write(s); print('ok')
