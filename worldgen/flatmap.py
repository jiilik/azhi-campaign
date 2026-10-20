"""Step 3 of 4: conformal toroidal projection, labels, graticule and scale ladder -> output/azhi_flat_map.png."""
import os
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
os.makedirs('build', exist_ok=True); os.makedirs('output', exist_ok=True)
import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.patheffects as pe
from scipy.ndimage import map_coordinates
R, r = 3.0, 1.0; RKM = 2080.0   # tube radius in km -> Earth-like surface area
img = np.load('build/img_angle.npy'); NP, NT, _ = img.shape
W = 3200
SHIFT = 0.55                     # put the Bite a little in from the left edge
# conformal y, measured from the lower flank phi=-pi/2 upward through spine (0) to belly (pi)
phs = np.linspace(-np.pi/2, 1.5*np.pi, 20001)
yv = np.concatenate([[0], np.cumsum(r/(R+r*np.cos(0.5*(phs[1:]+phs[:-1])))*np.diff(phs))])
Ytot = yv[-1]; Hpx = int(round(W*Ytot/(2*np.pi)))
yp = (np.arange(Hpx)+0.5)/Hpx*Ytot
phi_rows = np.interp(yp, yv, phs)
th_cols = (np.arange(W)+0.5)/W*2*np.pi - SHIFT
pi_ = ((phi_rows+np.pi)%(2*np.pi))/(2*np.pi)*NP
ti_ = (th_cols%(2*np.pi))/(2*np.pi)*NT
PI, TI = np.meshgrid(pi_, ti_, indexing='ij')
out = np.stack([map_coordinates(img[...,c], [PI-0.5, TI-0.5], order=1, mode='grid-wrap') for c in range(3)], -1)
out = np.clip(out,0,1)
plt.imsave('output/azhi_map_raw.png', out[::-1])

def X(th): return ((th+SHIFT)%(2*np.pi))/(2*np.pi)*W
def Y(ph): return Hpx - np.interp(ph if ph>=-np.pi/2 else ph+2*np.pi, phs, yv)/Ytot*Hpx

fig = plt.figure(figsize=(W/200+2.6, Hpx/200+1.5), dpi=200, facecolor='#efe6d2')
ax = fig.add_axes([0.03, 0.08, W/200/(W/200+2.6)*0.97, 0.84])
ax.imshow(out[::-1], extent=[0,W,Hpx,0]); ax.set_xlim(0,W); ax.set_ylim(Hpx,0); ax.axis('off')
# graticule: ringwise every 30 deg, tubewise every 30 deg
for d in range(0,360,30):
    ax.axvline(X(np.radians(d)), color='white', lw=0.4, alpha=0.35)
for d in range(-90,270,30):
    ax.axhline(Y(np.radians(d)), color='white', lw=0.4, alpha=0.35)
for d,lab in [(0,'Spine (outer equator)'),(180,'Belly (inner equator)')]:
    ax.axhline(Y(np.radians(d)), color='#f6e7b0', lw=0.9, alpha=0.7, ls='--')
fx = [pe.withStroke(linewidth=3, foreground='#1b1a17')]
def lab(th, ph, s, size=11, style='normal', color='#fbf3dc', rot=0):
    ax.text(X(th), Y(ph), s, ha='center', va='center', fontsize=size, color=color, fontfamily='serif',
            style=style, path_effects=fx, rotation=rot)
lab(-0.02, 0.75, 'THE BITE', 12, color='#ffd27a')
lab(0.20, 0.0+0.33, 'The Skull', 9)
lab(0.20, np.pi-0.42, 'Lower Jaw', 11, color='#ffd27a')
lab(0.30, np.pi, 'The Maw', 9, 'italic')
for t in (1.9, 2.8, 4.3):
    lab(t, 0.12, 'S P I N E   R A N G E', 9)
lab(1.0, np.pi-0.05, 'I N N E R   S E A', 16, color='#d7ecf5')
lab(4.0, np.pi-0.05, 'I N N E R   S E A', 16, color='#d7ecf5')
lab(0.95, 1.95, 'Forelimb Ridges', 8, 'italic'); lab(0.95, -1.95+0.0, 'Forelimb Ridges', 8, 'italic')
lab(1.95, 1.25, 'Wing Spars', 8, 'italic'); lab(1.95, -1.25, 'Wing Spars', 8, 'italic')
lab(3.25, 2.05, 'Hindlimb Ridges', 8, 'italic'); lab(3.25, -2.05, 'Hindlimb Ridges', 8, 'italic')
lab(5.9, 0.42, 'The Tail', 9, 'italic')
lab(3.1, 1.0, 'Upper Flank', 10, 'italic', '#e8dcc0'); lab(3.1, -1.0, 'Lower Flank', 10, 'italic', '#e8dcc0')
ax.text(W*0.5, -Hpx*0.035, '◀  HEADWARD                         ringwise  (wraps left ↔ right)                         TAILWARD  ▶',
        ha='center', va='bottom', fontsize=10, fontfamily='serif', color='#3a2f22')
ax.text(-W*0.012, Hpx*0.5, 'tubewise  (wraps top ↔ bottom)', rotation=90, ha='right', va='center', fontsize=10, fontfamily='serif', color='#3a2f22')
fig.text(0.5, 0.965, 'AZHI  ·  The Ring of the Dragon Philosopher', ha='center', fontsize=20, fontfamily='serif', color='#2b2118', weight='bold')
fig.text(0.5, 0.025, 'Conformal toroidal projection (R : r = 3 : 1). Angles and bearings are true; scale varies by row — use the ladder at right. '
         'Graticule every 30°.', ha='center', fontsize=9, fontfamily='serif', color='#3a2f22', style='italic')
# scale ladder: 1000 km bars at several rows
ax2 = fig.add_axes([0.03+W/200/(W/200+2.6)*0.97+0.005, 0.08, 0.10, 0.84]); ax2.set_xlim(0,1); ax2.set_ylim(Hpx,0); ax2.axis('off')
pxpk = lambda ph: (W/(2*np.pi))/((R+r*np.cos(ph))*RKM)
axw = 0.10*(fig.get_figwidth()*200)  # pixels of ax2 width in figure px
mapscale = (W/200/(W/200+2.6)*0.97*fig.get_figwidth()*200)/W   # fig px per map px
for d in (-90,-60,-30,0,30,60,90,120,150,180,210,240):
    ph=np.radians(d); L = 1000*pxpk(ph)*mapscale/axw
    y=Y(ph); ax2.plot([0.05,0.05+L],[y,y], color='#2b2118', lw=2.2, solid_capstyle='butt')
    ax2.text(0.05+L+0.04, y, f'{d:+d}°', va='center', fontsize=7, fontfamily='serif', color='#3a2f22')
ax2.text(0.05, -Hpx*0.035, '1000 km', fontsize=8, fontfamily='serif', color='#2b2118', va='bottom')
fig.savefig('output/azhi_flat_map.png', dpi=200, facecolor=fig.get_facecolor())
print(W, Hpx)
