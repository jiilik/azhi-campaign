"""Step 2 of 4: sea level (68% water by area), climate tint, hillshade -> build/E.npy, build/img_angle.npy."""
import os
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
os.makedirs('build', exist_ok=True); os.makedirs('output', exist_ok=True)
import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
R, r = 3.0, 1.0
H = np.load('build/H.npy'); TH, PH = np.load('build/grid.npy')
NP, NT = H.shape
# area-weighted sea level -> ~68% water
w = (R + r*np.cos(PH)).ravel(); o = np.argsort(H.ravel()); cw = np.cumsum(w[o])/w.sum()
SEA = H.ravel()[o][np.searchsorted(cw, 0.68)]
E = H - SEA
np.save('build/E.npy', E)
emax = np.percentile(E[E>0], 99.7)

def colorize(E, PH):
    rgb = np.zeros(E.shape+(3,))
    sea = E<=0; d = np.clip(-E/ (np.abs(E.min())*0.7),0,1)[...,None]
    shallow = np.array([0.42,0.66,0.78]); deep = np.array([0.06,0.18,0.36])
    rgb[sea] = (shallow*(1-d)+deep*d)[sea]
    h = np.clip(E/emax,0,1)
    # climate tint by tube-position: outer hot/lush, flanks temperate, inner dim & misty
    c = np.cos(PH)                     # 1 outer .. -1 inner
    lush = np.array([0.22,0.45,0.20]); temp=np.array([0.47,0.58,0.33]); mist=np.array([0.48,0.56,0.50])
    t1 = np.clip(c,0,1)[...,None]; t2 = np.clip(-c,0,1)[...,None]
    low = lush*t1 + temp*(1-t1-t2) + mist*t2
    # drier foothill band just off the spine
    dry = np.exp(-((np.abs(PH)-0.55)/0.18)**2)[...,None]*0.55
    low = low*(1-dry)+np.array([0.70,0.62,0.42])*dry
    mid = np.array([0.52,0.46,0.36]); high=np.array([0.62,0.58,0.55]); snow=np.array([0.96,0.97,0.99])
    hh=h[...,None]
    land = np.where(hh<0.45, low*(1-(hh/0.45)**1.5)+mid*((hh/0.45)**1.5),
           np.where(hh<0.72, mid*(1-(hh-0.45)/0.27)+high*((hh-0.45)/0.27),
                    high*(1-(hh-0.72)/0.28)+snow*((hh-0.72)/0.28)))
    rgb[~sea] = land[~sea]
    coast = (~sea)&(E<emax*0.02); rgb[coast] = rgb[coast]*0.6+np.array([0.80,0.74,0.55])*0.4
    return rgb

rgb = colorize(E, PH)
ls = LightSource(azdeg=315, altdeg=40)
shade = ls.hillshade(np.where(E>0,E,0)*6, vert_exag=1, dx=1, dy=1)
img = rgb*(0.55+0.55*shade[...,None]); img=np.clip(img,0,1)
np.save('build/img_angle.npy', img)
print('sea', SEA, 'land frac', (w[(E.ravel()>0)]).sum()/w.sum(), 'emax', emax)
# jaw check
j = (np.abs(((TH+np.pi)%(2*np.pi))-np.pi)<0.3)&(np.abs(np.abs(PH)-np.pi)<0.15)
print('jaw above sea frac', (E[j]>0).mean())
