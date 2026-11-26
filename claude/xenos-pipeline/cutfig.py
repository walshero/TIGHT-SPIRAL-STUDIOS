import numpy as np, cv2, json
from PIL import Image
from skimage.morphology import reconstruction
figs=[]
for src in ['acimg-000.jpg','acimg-001.jpg']:
    im=np.array(Image.open(src).convert('RGB')).astype(np.int16)
    fg=(im.min(-1)<232)|((im.max(-1)-im.min(-1))>28)
    fg=fg.astype(np.uint8)
    core=cv2.morphologyEx(fg,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))          # thin label strokes vanish
    rec=reconstruction(core.astype(np.uint8),fg,method='dilation').astype(np.uint8)  # regrow only what touches the bodies
    n,lab,st,_=cv2.connectedComponentsWithStats(rec,8)
    for i in range(1,n):
        x,y,w,h,a=st[i]
        if h<120 or a<2500:continue
        m=(lab==i).astype(np.uint8)
        figs.append((src,int(x),int(y),int(w),int(h)))
        rgba=np.dstack([im.astype(np.uint8),(m*255).astype(np.uint8)])[y:y+h,x:x+w]
        Image.fromarray(rgba).save(f'fig_{len(figs)-1:02d}.png')
print(len(figs));json.dump(figs,open('figs.json','w'))
for i,f in enumerate(figs):print(i,f)
