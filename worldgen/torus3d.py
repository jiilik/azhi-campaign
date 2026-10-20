"""Step 4 of 4: drape the coloured map over a 3D torus from four angles -> output/azhi_3d_*.png + azhi_3d_views.png."""
import os
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
os.makedirs('build', exist_ok=True); os.makedirs('output', exist_ok=True)
import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
R, r = 3.0, 1.0
img = np.load('build/img_angle.npy'); E = np.load('build/E.npy')
NP, NT, _ = img.shape
# downsample for the mesh
sp, st = 3, 3
im = img[::sp, ::st]; e = E[::sp, ::st]
emax = np.percentile(E[E > 0], 99.7)
ph = np.linspace(-np.pi, np.pi, NP, endpoint=False)[::sp]
th = np.linspace(0, 2*np.pi, NT, endpoint=False)[::st]
# close the mesh in both directions
im = np.concatenate([im, im[:1]], 0); im = np.concatenate([im, im[:, :1]], 1)
e = np.concatenate([e, e[:1]], 0); e = np.concatenate([e, e[:, :1]], 1)
ph = np.append(ph, ph[0] + 2*np.pi); th = np.append(th, th[0] + 2*np.pi)
TH, PH = np.meshgrid(th, ph)
rho = r + 0.05*np.clip(e, 0, None)/emax          # gentle relief exaggeration
X = (R + rho*np.cos(PH))*np.cos(TH)
Y = (R + rho*np.cos(PH))*np.sin(TH)
Z = rho*np.sin(PH)
# surface normals of the smooth torus for lighting
NX = np.cos(PH)*np.cos(TH); NY = np.cos(PH)*np.sin(TH); NZ = np.sin(PH)

rng = np.random.default_rng(3)
stars = rng.uniform(0, 1, (900, 2)); sb = rng.uniform(0.2, 1, 900)**3

views = [
    ('oblique', 32, -60, 'Three-quarter view'),
    ('above', 88, -90, 'From above the ring'),
    ('bite', 8, 0, 'Edge-on, facing the Bite'),
    ('hole', 22, 180, 'Across the hole toward the Lower Jaw'),
]
for name, elev, azim, title in views:
    el, az = np.radians(elev), np.radians(azim)
    cam = np.array([np.cos(el)*np.cos(az), np.cos(el)*np.sin(az), np.sin(el)])
    light = cam*0.6 + np.array([0.3, -0.5, 0.6]); light /= np.linalg.norm(light)
    diff = np.clip(NX*light[0] + NY*light[1] + NZ*light[2], 0, 1)
    shade = 0.28 + 0.85*diff
    fc = np.clip(im*shade[..., None], 0, 1)
    # thin atmospheric rim: brighten limb slightly
    mu = np.abs(NX*cam[0] + NY*cam[1] + NZ*cam[2])
    fc = np.clip(fc*(0.85 + 0.15*mu[..., None]) + (1-mu[..., None])**4*np.array([0.25, 0.4, 0.6])*0.5, 0, 1)
    fig = plt.figure(figsize=(9, 9), dpi=160, facecolor='#05070d')
    bg = fig.add_axes([0, 0, 1, 1]); bg.set_facecolor('#05070d'); bg.axis('off')
    bg.scatter(stars[:, 0], stars[:, 1], s=sb*3, c='white', alpha=0.8, lw=0); bg.set_xlim(0, 1); bg.set_ylim(0, 1)
    ax = fig.add_axes([0, 0, 1, 1], projection='3d'); ax.set_facecolor((0, 0, 0, 0))
    ax.plot_surface(X, Y, Z, facecolors=fc, rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False)
    lim = 2.55
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim); ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=elev, azim=azim); ax.axis('off')
    fig.text(0.5, 0.94, f'AZHI  ·  {title}', ha='center', color='#e9dfc6', fontsize=15, fontfamily='serif')
    fig.savefig(f'output/azhi_3d_{name}.png', dpi=160, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(name)

from PIL import Image
ims = [Image.open(f'output/azhi_3d_{n}.png').resize((720, 720)) for n in ['oblique', 'above', 'bite', 'hole']]
sheet = Image.new('RGB', (1440, 1440)); [sheet.paste(im, ((i % 2)*720, (i//2)*720)) for i, im in enumerate(ims)]
sheet.save('output/azhi_3d_views.png'); print('views sheet ok')
