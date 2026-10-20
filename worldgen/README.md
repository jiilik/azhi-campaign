# worldgen: terrain, map projection, 3D torus

This folder generates Azhi's world: a heightmap that wraps seamlessly in both directions, a conformal flat map, and 3D renders of the ring.

## Requirements

Python 3.10+, `numpy`, `scipy`, `matplotlib`, `pillow`.

```
pip install numpy scipy matplotlib pillow   # add --break-system-packages in Claude's sandbox
```

## Run the full pipeline (≈3 min on a sandbox CPU)

Each script `chdir`s to this folder, so run it from anywhere. Run them in order: each one reads the previous one's `build/*.npy`.

```
python worldgen/terrain.py    # 1. heightmap          -> build/H.npy, build/grid.npy   (slowest step, ~2 min)
python worldgen/colorize.py   # 2. sea level + colour -> build/E.npy, build/img_angle.npy
python worldgen/flatmap.py    # 3. flat map           -> output/azhi_flat_map.png, output/azhi_map_raw.png
python worldgen/torus3d.py    # 4. 3D views           -> output/azhi_3d_{oblique,above,bite,hole}.png + azhi_3d_views.png
```

In Claude's sandbox, the tool call times out at 2 minutes, so run `terrain.py` as a background command. `build/` is git-ignored, and `output/` holds the committed results.

## Coordinates

The grid is `(phi, theta)`, shaped `(NP, NT)` = `(768, 2304)`.

| Symbol | Meaning |
|---|---|
| `theta` ∈ [0, 2π) | **Ringwise** angle around the hole. **θ = 0 is the Bite.** The head sits at small positive θ; the tail approaches 2π, wrapping back to the Bite. |
| `phi` ∈ [−π, π) | **Tubewise** angle around the tube. **φ = 0 is the outer equator (spine).** φ = ±π is the inner equator (belly). |
| `R, r = 3, 1` | Ring and tube radii (aspect 3:1). `flatmap.py` uses `RKM = 2080` km for r, which gives an Earth-sized surface area. |

Every feature is built from `gauss(dθ, dφ, σθ, σφ)`. It wraps both angles, so features crossing the seam are seamless. Always pass offsets through it, or through `wrap()`.

## Where the anatomy lives (terrain.py)

| Feature | Code block | Main knobs |
|---|---|---|
| Base shape | `0.45*cos(PH)` (outer high) + the belly basin | Raise the basin depth for more Inner Sea |
| Noise | `fbm(beta, seed)`: `n1` continents, `n2` detail, `n3` erosion, `ridged` mountains | **Change the seeds 1–4 to re-roll the continents.** Lower `beta` gives rougher terrain. |
| Spine Range | `spine = …`: vertebral rhythm `cos(70*TH)`, gap at the Bite, thinning toward the tail | `70` = number of vertebrae |
| Skull | dome at θ = 0.17, two horn ridges, eye-socket lakes | |
| **Lower Jaw** | `J`: two mandible rami meeting at the chin (θ ≈ 0), teeth along the inner rim, rami up the flanks | `2.15*J` = jaw height. Keep it above sea level; the author requires it. |
| The Maw | negative gauss inside the jaw | |
| Vestigial limbs | `limb(t0, sweep, reach, amp, toes, s, width, bend)`: fore θ = 0.80, hind θ = 3.30, wing spars from θ = 1.25 | `H += L*2.4`. The author wants these **subtle**. |

## colorize.py

- **Sea level** is chosen so that **68% of the surface, area-weighted, is water**: `np.searchsorted(cw, 0.68)`. Area weight = `R + r cos φ`.
- The climate tint depends only on φ: lush on the outer equator, temperate on the flanks, misty on the inner side, plus a dry band just off the spine. Altitude bands run lowland → rock → snow, with hillshade.

## flatmap.py: conformal toroidal projection

```
x = theta
y = (2r / sqrt(R² − r²)) * arctan( sqrt((R−r)/(R+r)) * tan(phi/2) )
```

- The projection is conformal: bearings are true and a constant heading is a straight line. Scale grows toward the inner equator, up to (R+r)/(R−r) = 2×, so the map prints a **scale ladder** with 1,000 km bars per row.
- The map is laid out so that the vertical seam falls mid–lower flank (φ = −90°). The spine and the jaw both appear whole.
- `SHIFT = 0.55` moves the Bite in from the left edge.
- Labels are `lab(theta, phi, text)` calls near the bottom. Move them if you change the terrain.
- The direction banner reads "◀ HEADWARD … TAILWARD ▶". That is correct: moving right means increasing θ, which goes from the head along the body toward the tail.

## torus3d.py

This script drapes `img_angle.npy` on a torus mesh, downsampled 3×, with relief exaggerated `0.05*e/emax`. It renders four `views = (name, elev, azim, title)`. Add tuples for more angles. `lim` controls the zoom.

## Known quirks

- matplotlib's `plot_surface` has no true depth sorting. Odd angles can show minor artifacts, so stick to the provided views or check the result visually.
- If you change `NP`, every Gaussian width stays in radians and behaves the same, but run time scales with `NP²`.
