# Art Style: Saturday-Morning Bold (campaign default)

The author chose this style on 2026-10-20. Use it for every cartoon unless he specifies otherwise.

**In the world** *(Troy, 2026-11-12)*: Saturday-Morning Bold is **the favoured art style of the White dragonborn**. In-universe images (the Tapestry Hall, murals, illustrated texts) are drawn in it because White monks and storytellers made them.

## Look

- **Thick ink outlines:** `#18120e`, about 1.7 units in figure space (≈4 px at the usual 2.25× figure scale). Background shapes use 3 px.
- **Flat, saturated colour.** There are no gradients on characters. Glows (light sources, magic) are the exception and may use soft radial gradients.
- **Heroic proportions:** head scale 1.05, torso 1.08, normal leg length, long snout. Eyes are yellow with a slit pupil and a heavy brow line.
- **Readable silhouettes:** horns swept back, tail visible, weapon held clear of the body.

## Dragonborn palette (scale, belly)

| Colour | Scale | Belly | Horn |
|---|---|---|---|
| Gold | `#e3a62a` | `#f8e09a` | `#efe4c9` |
| Silver | `#aab5c2` | `#eef2f6` | `#efe4c9` |
| Black | `#3a3546` | `#77708a` | `#cfc6dc` |
| Blue | `#2e6fd2` | `#a3c8f3` | `#efe4c9` |
| White | `#eceff4` | `#d5dde8` | `#8b96a8` |
| Red | `#c8342b` | `#f3a37c` | `#efe4c9` |
| Green | `#3c9a47` | `#b9e292` | `#efe4c9` |

## Dragonborn by form *(Troy, 2026-11-12)*

- **Red** is drawn a touch **larger** than its neighbours and **Blue** a touch **smaller** (Large and Small forms). In code, `tapestry_lib.SIZE_K`.
- **Green: Prehensile Tail.** The tail curls up behind the figure and holds an everyday thing like a third hand: a flower, a cup, a lantern, a basket, a quill, a parasol, a censer. **Never a weapon or a shield.** *(Claude: a leafy frill along the tail and a gold cuff near the tip are the embellishment.)*
- **Blue and Indigo** (Amphibious, Deep-Born): **webbed fingers and toes** wherever the figure is big enough to show fingers and toes.
- **White: Spectral Wings,** wings of shimmering light (translucent white to pale blue and lilac, white ribs, shed sparkles), shown in flight.

## Recurring motifs

- **Holy symbol and shield emblem:** a simple **ring** with a dot for a head, the ouroboros. It stands for Azhi.
- **Gold dragon in the sky** = the sun (warm glow `#ffd25a`). **Silver** = the moon (cool glow `#bcd2ff`).
- **The ring arch:** on the inner side and flanks, the far side of the world arcs across the sky as a blue band. Draw its land from the **real map**, not made-up patches *(Troy, 2026-11-12)*: `worldgen/farside.py` ray-traces the coastlines, highlands and clouds, and `tapestry_lib.ring_band(..., view=θ)` draws them. The Lower Jaw, rising from the Inner Sea, is the landmark to look for.

## Azhi (approved design)

Azhi is **Persian-myth-inspired, long and snakelike**, and **colossal**: its head is wider than a planet, and the young dragons are specks beside it.
- Lapis body `#3a3f8f` with darker scale chevrons, and turquoise belly plates `#4fc1b3`.
- Gold `#efbe48` dashed ribbon and diamond ornaments with red centres along the back.
- Dorsal spikes, and **flame-shaped tufts** in orange, red and gold, in the style of Shahnameh miniatures.
- Curling gold barbels, cream curled horns, an open fanged mouth, and a yellow slit eye.
- Small vestigial clawed legs on the inner (belly) side. This foreshadows the limb ridges on the world map.
- **Stubby little wings** near the shoulders *(Troy, 2026-11-12)*, matching the map's Wing Spars. Along the body: forelimbs about 13% of the way from the head, wings about 20%, hindlimbs about 53%, then a long thinning tail.
- Its body should read as a **near-loop** around the subject, foreshadowing the ring.

## Do and don't

- Do show only dragonborn as people. **No other sentient species.**
- Don't add effects the author has rejected. For example, the "gift" streams from the young dragons to the world were removed.
- Don't reproduce known characters, logos or existing artworks.
