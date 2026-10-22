# art: cartoon drawing code

All art is **hand-built SVG generated in Python**, then rasterized with headless Chromium. There is no image-generation model involved. The look is defined in code, so new pieces stay consistent with old ones. Read `STYLE.md` first.

## Requirements

Python 3.10+, `numpy`, `pillow`, and `playwright` with Chromium. In Claude's sandbox, Chromium is pre-installed. Do **not** run `playwright install`.

## Scripts (`art/cartoon/`)

Each script `chdir`s to its own folder and writes to `build/` (SVG, git-ignored) and `output/` (PNG).

| Script | Output |
|---|---|
| `party.py` | The library: dragonborn figures, weapons, sky dragons, scenes, and four style presets. Run directly → `build/sheet_<style>.svg`. |
| `render_style_sheets.py [styles…]` | `output/dragonborn_<style>.png`: the four-style comparison sheets (bold, chibi, storybook, geo) |
| `make_scenes.py` | `output/dragonborn_spine.png`, `output/dragonborn_innersea.png`: the handout scenes in Bold |
| `colour_wheel.py` | `output/colour_wheel.png`: the colour wheel of the species design (canon, 2026-10-21) (five colours, five hybrids, the Unphased, Gold and Silver watching). Hybrid colours are working values. |
| `azhi_cover.py` | `output/azhi_cover.png`: Azhi looming over the young world (handout cover) |
| `svg2png.py in.svg out.png W H` | A generic SVG → PNG rasterizer used by the others |

## Drawing a dragonborn

```python
from party import STYLES, figure
st = STYLES['bold']
svg_fragment = figure(x, y, scale, 'Red', 'fighter', outfit='#8d98a6', accent='#2f4f8f', st=st,
                      flip=1, look_back=False)
```

- **Colours:** `Gold Silver Black Blue White Red Green`.
- **Roles and their gear:**

| Role | Gear |
|---|---|
| `fighter` | sword and ring-emblem shield |
| `wizard` | staff with a glowing orb |
| `cleric` | raised ring holy symbol and mace |
| `rogue` | two daggers and a cape |
| `ranger` | bow, quiver and cape |

- **Coordinates:** local units with the feet at `(0, 0)` and the figure about 115 units tall. A typical scale is 2.25 on a 1200×800 canvas.
- `flip=-1` faces the figure left. `look_back=True` turns only the head.
- Wrap fragments in `<svg width=… height=… viewBox=…>`, write the file, and call `svg2png.py`.

## Other building blocks in `party.py`

- `sky_dragon(cx, cy, s, colour, glow_colour, st)` draws a flying dragon with a glow (the sun or moon).
- `scene_spine(st)` and `scene_sea(st)` are full backgrounds plus parties. Copy one as a template for new scenes.
- `ring_arch`, `FANG` (sea stacks and spires), `ridge`, `wave` and `cloud` are scenery helpers.
- `P(path_d, fill, st)` is a filled path with the style's outline, and `limb(points, width, fill, st)` is an outlined thick stroke. These two primitives build everything else.

In `azhi_cover.py`, Azhi's body is built from a Catmull-Rom spine with a variable width, which makes a tapered tube. Belly plates, scale chevrons, ornaments, flame tufts and legs are placed along the sampled normals. Edit the `spine` control points to re-pose it. `SHOW_GIFTS` stays `False` (author decision).

## Adding a new piece (checklist for Claude)

1. Read `STYLE.md` and use `STYLES['bold']` unless told otherwise.
2. Build the SVG from the primitives above, and keep people dragonborn only.
3. Render with `svg2png.py`, **then look at the PNG** (Read the image) before showing it. Fix overlaps, such as a weapon over a face or a light source buried behind a body.
4. Save the generator script here, commit the output PNG, and note the piece in `PLAN.md` if it was a planned item.
