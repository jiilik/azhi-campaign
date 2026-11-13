"""The far side of the ring as seen from the surface (2026-11-12) -> output/azhi_sky_*.png.

Ray-traces the coloured torus (R = 3, r = 1, as in torus3d.py) from an eye
standing on the surface, looking across the hole toward the far side of the
ring. Reference for drawing the ring arch in the cartoons and tapestries.
Atmosphere (2026-11-12): clouds on the far side and in the near sky, haze
with distance, and lighting from the Gold dragon (day) or Silver (night).
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


def fbm2(shape, seed, beta=3.2, lowcut=3):
    """Tileable, isotropic fractal noise (power spectrum 1/f^beta), 0..1."""
    rng = np.random.default_rng(seed)
    h, w = shape
    fy = np.fft.fftfreq(h)[:, None] * h
    fx = np.fft.fftfreq(w)[None, :] * h          # same units in both directions
    f = np.sqrt(fx ** 2 + fy ** 2)
    amp = np.where(f < lowcut, 0, 1 / np.maximum(f, 1) ** (beta / 2))
    F = np.fft.fft2(rng.normal(size=shape)) * amp
    out = np.real(np.fft.ifft2(F))
    out -= out.min(); out /= out.max()
    return out


CLOUD = fbm2((NP // 2, NT // 2), seed=11, beta=3.0, lowcut=4)
# cloud cover: soft threshold, more over the seas
CLOUD = np.clip((CLOUD - 0.52) / 0.18, 0, 1) ** 1.5


def cloud_at(th, ph):
    i = ((ph + np.pi) / (2 * np.pi) * CLOUD.shape[0]).astype(int) % CLOUD.shape[0]
    j = ((th % (2 * np.pi)) / (2 * np.pi) * CLOUD.shape[1]).astype(int) % CLOUD.shape[1]
    return CLOUD[i, j]


LIGHTS = {
    # sky colours (bottom, top), light colour, ambient, light direction in camera
    # terms (right, up, toward-viewer), glow colour
    'day': dict(sky=((0.80, 0.88, 0.96), (0.30, 0.52, 0.85)), light=(1.0, 0.93, 0.78), amb=0.30,
                ldir=(-0.45, 0.75, 0.50), glow=(1.0, 0.82, 0.35), haze=(0.82, 0.88, 0.95), stars=False),
    'night': dict(sky=((0.10, 0.13, 0.25), (0.02, 0.03, 0.09)), light=(0.62, 0.72, 0.95), amb=0.10,
                  ldir=(0.40, 0.70, 0.55), glow=(0.74, 0.82, 1.0), haze=(0.14, 0.18, 0.32), stars=True),
}


def render(phi_deg, theta_deg=200, mode='day', W=900, H=520, hfov=110, pitch=12, eye_h=0.0015):
    L_ = LIGHTS[mode]
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
    rho = np.sqrt(X[..., 0] ** 2 + X[..., 1] ** 2) - R
    ph = np.arctan2(X[..., 2], rho)
    col = sample(th, ph).astype(float)
    # clouds on the surface
    c = cloud_at(th, ph)[..., None]
    col = col * (1 - 0.85 * c) + 0.97 * c
    # lighting from the sun or moon dragon: Lambert on the smooth torus normal
    ldir = L_['ldir'][0] * right + L_['ldir'][1] * up + L_['ldir'][2] * (-fwd)
    ldir /= np.linalg.norm(ldir)
    N = np.stack([np.cos(ph) * np.cos(th), np.cos(ph) * np.sin(th), np.sin(ph)], -1)
    lam = np.clip(N @ ldir, 0, 1)[..., None]
    col = col * (L_['amb'] + (1 - L_['amb']) * lam * np.array(L_['light']))
    # sky: gradient, a glow toward the light, stars at night
    v = (ys / (H / 2) + 1) / 2
    sb, stp = np.array(L_['sky'][0]), np.array(L_['sky'][1])
    sky = sb * (1 - v[..., None]) + stp * v[..., None]
    cosg = np.clip(D @ ldir, -1, 1)
    sky = sky + np.array(L_['glow']) * (np.clip(cosg, 0, 1) ** 12 * 0.55)[..., None]
    if L_['stars']:
        rng = np.random.default_rng(5)
        st = rng.random((H, W)) > 0.9985
        sky = np.where(st[..., None], np.maximum(sky, 0.85), sky)
    # sky clouds near the viewer: soft screen-space wisps above the horizon
    wisp = fbm2((H, W), seed=23, beta=3.4, lowcut=2)
    wisp = np.clip((wisp - 0.58) / 0.2, 0, 1) * np.clip(v * 2 - 0.9, 0, 1)
    cloud_col = np.array(L_['light']) * (0.88 + 0.12 * np.clip(cosg, 0, 1)[..., None]) * (1.0 if mode == 'day' else 0.4)
    sky = sky * (1 - 0.7 * wisp[..., None]) + cloud_col * 0.7 * wisp[..., None]
    # aerial perspective: distant ground fades into the haze colour
    haze = np.clip(t / 6, 0, 1)[..., None] ** 0.8
    hz = np.array(L_['haze'])
    out = np.where(hit[..., None], col * (1 - 0.5 * haze) + hz * 0.5 * haze, sky)
    return (np.clip(out, 0, 1) * 255).astype(np.uint8)


if __name__ == '__main__':
    os.makedirs('output', exist_ok=True)
    try:
        fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf', 22)
    except OSError:
        fnt = None
    labels = {100: 'upper flank', 120: 'flank, leaning inner', 140: 'inner flank'}
    for mode, light in (('day', 'lit by the Gold dragon'), ('night', 'lit by the Silver dragon')):
        panels = []
        for phi in (100, 120, 140):
            im = Image.fromarray(render(phi, mode=mode))
            d = ImageDraw.Draw(im)
            d.text((14, 10), f'phi {phi}: {labels[phi]}, {light}',
                   fill=(20, 18, 14) if mode == 'day' else (235, 235, 245), font=fnt)
            im.save(f'output/azhi_sky_{mode}_phi{phi}.png')
            panels.append(im)
        sheet = Image.new('RGB', (panels[0].width, sum(p.height for p in panels) + 16), (24, 20, 16))
        y = 0
        for p in panels:
            sheet.paste(p, (0, y)); y += p.height + 8
        sheet.save(f'output/azhi_sky_{mode}.png')
    print('ok')
