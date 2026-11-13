"""The far side of the ring as seen from the surface (2026-11-12) -> output/azhi_sky_*.png.

Ray-traces the coloured torus (R = 3, r = 1, as in torus3d.py) from an eye
standing on the surface, looking across the hole toward the far side of the
ring. Reference for drawing the ring arch in the cartoons and tapestries.
Needs build/img_angle.npy (run terrain.py and colorize.py first).

phi: 0 = outer equator, 90 = top flank, 180 = inner equator.
From the outer half (phi < 90) the far side is hidden below the horizon.
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
R, r = 3.0, 1.0
img = np.load('build/img_angle.npy')
NP, NT, _ = img.shape


def sample(th, ph):
    i = ((ph + np.pi) / (2 * np.pi) * NP).astype(int) % NP
    j = ((th % (2 * np.pi)) / (2 * np.pi) * NT).astype(int) % NT
    return img[i, j]


def render(phi_deg, theta_deg=200, W=900, H=520, hfov=110, pitch=12, eye_h=0.0015):
    th0, ph0 = np.radians(theta_deg), np.radians(phi_deg)
    n = np.array([np.cos(ph0) * np.cos(th0), np.cos(ph0) * np.sin(th0), np.sin(ph0)])
    P = np.array([(R + r * np.cos(ph0)) * np.cos(th0), (R + r * np.cos(ph0)) * np.sin(th0), r * np.sin(ph0)])
    eye = P + n * eye_h
    # look toward the axis (across the hole), flattened onto the local horizon
    toward = -np.array([np.cos(th0), np.sin(th0), 0.0])
    fwd = toward - n * (toward @ n); fwd /= np.linalg.norm(fwd)
    right = np.cross(fwd, n); right /= np.linalg.norm(right)
    up = n
    p = np.radians(pitch)
    fwd, up = fwd * np.cos(p) + up * np.sin(p), up * np.cos(p) - fwd * np.sin(p)
    f = 0.5 * W / np.tan(np.radians(hfov) / 2)
    xs, ys = np.meshgrid(np.arange(W) - W / 2, H / 2 - np.arange(H))
    D = fwd[None, None] * f + right[None, None] * xs[..., None] + up[None, None] * ys[..., None]
    D /= np.linalg.norm(D, axis=-1, keepdims=True)
    t = np.full((H, W), 1e-4); hit = np.zeros((H, W), bool); alive = np.ones((H, W), bool)
    for _ in range(400):
        X = eye + D * t[..., None]
        q = np.sqrt(X[..., 0] ** 2 + X[..., 1] ** 2) - R
        d = np.sqrt(q ** 2 + X[..., 2] ** 2) - r
        newhit = alive & (d < 1e-5 * (1 + t))
        hit |= newhit; alive &= ~newhit
        t = np.where(alive, t + np.maximum(d, 1e-5) * 0.9, t)
        alive &= t < 12
    X = eye + D * t[..., None]
    th = np.arctan2(X[..., 1], X[..., 0])
    ph = np.arctan2(X[..., 2], np.sqrt(X[..., 0] ** 2 + X[..., 1] ** 2) - R)
    col = sample(th, ph).astype(float)
    if col.max() > 1.5: col /= 255
    # haze with distance, so the far side looks far
    haze = np.clip(t / 6, 0, 1)[..., None] ** 0.8
    sky_top, sky_bot = np.array([0.33, 0.55, 0.85]), np.array([0.78, 0.88, 0.97])
    v = (ys / (H / 2) + 1) / 2
    sky = sky_bot * (1 - v[..., None]) + sky_top * v[..., None]
    out = np.where(hit[..., None], col * (1 - 0.55 * haze) + sky_bot * 0.55 * haze, sky)
    return (np.clip(out, 0, 1) * 255).astype(np.uint8)


if __name__ == '__main__':
    os.makedirs('output', exist_ok=True)
    panels = []
    for phi in (100, 120, 140):
        im = Image.fromarray(render(phi))
        d = ImageDraw.Draw(im)
        try:
            fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf', 22)
        except OSError:
            fnt = None
        lab = {100: 'phi 100: upper flank', 120: 'phi 120: flank, leaning inner', 140: 'phi 140: inner flank'}[phi]
        d.text((14, 10), lab, fill=(20, 18, 14), font=fnt)
        im.save(f'output/azhi_sky_phi{phi}.png')
        panels.append(im)
    sheet = Image.new('RGB', (panels[0].width, sum(p.height for p in panels) + 8 * 2), (24, 20, 16))
    y = 0
    for p in panels:
        sheet.paste(p, (0, y)); y += p.height + 8
    sheet.save('output/azhi_sky_views.png')
    print('ok')
