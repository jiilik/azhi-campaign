"""Far-side landforms for the tapestries (2026-11-12) -> ../art/cartoon/data/farside_t<theta>.npz.

Ray-traces the far side of the ring from an eye on the surface (same geometry as
skyview.py) and resamples it onto a normalized band grid (u across, v from the
band's top edge down to its underside), so the cartoon ring arch in
art/cartoon/tapestry_lib.ring_band() can be drawn with the real coastlines,
mountains and clouds of the map instead of made-up blobs.

u: 0 = left edge, UF = left foot of the arch, 0.5 = middle, 1 - UF = right foot, 1 = right edge.
v: 0 = top edge of the band, 1 = underside of the arch (or the horizon beyond the feet).
Stored: E (height above sea level, from build/E.npy) and C (cloud cover, from skyview.CLOUD).

Run: python worldgen/farside.py [theta_deg ...]   (needs build/E.npy and build/img_angle.npy)
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE); sys.path.insert(0, HERE)
import skyview  # noqa: E402  (loads the coloured map and the cloud field)

R, r = 3.0, 1.0
E = np.load('build/E.npy')
NP, NT = E.shape
UF = 0.18
NU, NV = 720, 200
OUT = os.path.join('..', 'art', 'cartoon', 'data')


def trace(theta_deg, phi_deg=120, W=1200, H=700, hfov=110, pitch=12, eye_h=0.0015):
    th0, ph0 = np.radians(theta_deg), np.radians(phi_deg)
    n = np.array([np.cos(ph0) * np.cos(th0), np.cos(ph0) * np.sin(th0), np.sin(ph0)])
    P = np.array([(R + r * np.cos(ph0)) * np.cos(th0), (R + r * np.cos(ph0)) * np.sin(th0), r * np.sin(ph0)])
    eye = P + n * eye_h
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
        if not alive.any():
            break
    X = eye + D * t[..., None]
    th = np.arctan2(X[..., 1], X[..., 0])
    rho = np.sqrt(X[..., 0] ** 2 + X[..., 1] ** 2) - R
    ph = np.arctan2(X[..., 2], rho)
    return th, ph, hit, t


def band_grid(theta_deg, phi_deg=120):
    th, ph, hit, t = trace(theta_deg, phi_deg)
    H, W = hit.shape
    band = hit & (t > 0.8)
    top = np.full(W, -1); bot = np.full(W, -1); arch = np.zeros(W, bool)
    for j in range(W):
        rows = np.flatnonzero(band[:, j])
        if not len(rows):
            continue
        top[j] = rows[0]
        k = rows[0]
        while k + 1 < H and band[k + 1, j]:
            k += 1
        bot[j] = k
        near = np.flatnonzero(hit[k + 1:, j])
        gap = near[0] if len(near) else H - k
        arch[j] = gap > 0.02 * H        # sky shows through under the band: inside the arch
    cols = np.flatnonzero(arch)
    footL, footR = cols[0], cols[-1]
    u = np.linspace(0, 1, NU)
    col = np.interp(u, [0, UF, 0.5, 1 - UF, 1], [0, footL, W / 2, footR, W - 1]).round().astype(int)
    v = np.linspace(0, 1, NV)
    rows = top[col][None, :] + v[:, None] * (bot[col] - top[col])[None, :]
    rows = np.clip(rows.round().astype(int), 0, H - 1)
    TH, PH = th[rows, col[None, :]], ph[rows, col[None, :]]
    i = ((PH + np.pi) / (2 * np.pi) * NP).astype(int) % NP
    j = ((TH % (2 * np.pi)) / (2 * np.pi) * NT).astype(int) % NT
    return E[i, j].astype(np.float32), skyview.cloud_at(TH, PH).astype(np.float32)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    thetas = [int(a) for a in sys.argv[1:]] or [110, 20, 250, 60, 10]   # Epochs 2-5; the Inner Sea handout scene
    for td in thetas:
        Eg, Cg = band_grid(td)
        np.savez_compressed(os.path.join(OUT, f'farside_t{td}.npz'), E=Eg.astype(np.float16), C=Cg.astype(np.float16))
        print(td, 'land', round(float((Eg > 0).mean()), 3))
