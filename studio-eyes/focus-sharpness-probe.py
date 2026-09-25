import sys,numpy as np
from PIL import Image
from scipy import ndimage as ndi
from skimage.color import rgb2lab
def S(p):
    L=rgb2lab(np.asarray(Image.open(p).convert('RGB'),float)/255)[...,0]
    lap=np.abs(ndi.laplace(ndi.gaussian_filter(L,.6)))
    H=L.shape[0]
    back=lap[int(H*.35):int(H*.70)].mean(); front=lap[int(H*.80):].mean()
    return back,front
for a,b in zip(sys.argv[1::2],sys.argv[2::2]):
    (bb,bf),(lb,lf)=S(a),S(b)
    print(f'{a:12s} back/front sharpness {bb/bf:.2f}  ->  {b:12s} {lb/lf:.2f}')
