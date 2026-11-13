# The Tapestry Hall: a player-facing history of Azhi (PLAN, 2026-11-12)

*(Troy, voice, 2026-11-12.)* The five lore panels (`cartoon/lore_panels.py`) are being redone as **seven tapestries** hanging in a **White monastery**. Players walk through them one at a time; each tells one chapter, condensed.

- **The legend, not the DM's truth.** Secrets are simply left out, but nothing woven is false: **no misdirection**. *(Secrets to leave out are listed in `canon/brainstorm-epochs.md`: today's Black is the young Black, the living thinking machine, the buried weapons forge, Indigo's weapon secrets; Gold and Silver are only whispered about.)*
- **Captions: brief.** A short woven title, with a line or two at most.
- **Seven tapestries:** Epoch 0 (Azhi meets the young dragons), then Epochs 1 to 6 (the first world, the machine war, the age of faith, the twins, the homunculi war, the present day).
- **Style:** Saturday-Morning Bold (house style). *(Open: whether to add a woven-tapestry frame or texture; Troy has said new drawing rules are coming.)*

## Epoch 0: Azhi Meets the Young Dragons, in the Depths of Space and Time

*(Troy, voice, 2026-11-12. Decided.)*
- **Before the first world and before any dragonborn.** Dragonborn first appear in Epoch 1.
- **Azhi's face is enormous,** against a backdrop of stars. Its **long, skinny, serpent-like body** trails away until the tail disappears into the stars. **Stubby little wings and stubby arms and legs.** Proportions should loosely follow the world map, which was built from Azhi's corpse.
- **Azhi is alive, not yet eating its tail.** It is the dragon philosopher, mid-speech, sharing some wisdom.
- **Azhi did not give birth to the young dragons; it has just met them.**
- **Seven young dragons, no colour yet:** shimmering with every colour, like the Unphased. They must **evoke playfulness**, through expressions, postures or activities:
  - the future **Gold and Silver chasing each other in a circle around Azhi**;
  - some **perched on Azhi's body**;
  - one **picking lint out of Azhi's ear**;
  - one **floating gracefully on its back in front of Azhi, listening**.
- **Motion:** the tapestry is flat, so the chasing pair need **cartoon motion lines** (swooshes) behind them, tinted **warm** for the future Gold and **cool** for the future Silver, with a faint matching shimmer on each *(Troy: keep it cartoony, not a woven-thread trail)*.
- **Caption:** "Azhi Meets the Young Dragons, in the Depths of Space and Time."

**Checked against the sources** *(Claude, 2026-11-12)*:
- **The myth agrees:** Azhi "comes upon a group of smaller dragons that are, seemingly, playing"; it doesn't create them. "Some prefer the company of speech, and talk with the old philosopher. Others prefer the comfort of play." Two "find pleasure simply in flying in great lazy circles around the great Azhi", and their forms become fixed as Gold and Silver: a perfect match for the chasing pair. The circling should be **lazy and happy**, not frantic.
- **"Many forms and colours":** the myth says the young dragons "are of many forms and colours" when Azhi meets them. Shimmering, unsettled colours fit this, and fit Gold and Silver only becoming fixed later. Suggestion: the chasing pair could carry a faint warm and a faint cool shimmer, hinting at what they'll become.
- **Wings: yes.** The world map has **Wing Spars**, faint fanned ridges near the shoulders (`worldgen/terrain.py`, θ ≈ 1.25), and limb ridges. The approved Azhi design in `art/STYLE.md` lists only small clawed legs, so it needs the stubby wings added (see that file).
- **Proportions from the map** (θ along the body, 0 to 2π, head at the start): skull at 0.17, **forelimbs at 0.80** (about 13% of the way along), **wing spars from 1.25** (about 20%), **hindlimbs at 3.30** (about 53%), then a long thinning tail. On the map the limbs sit on the belly side.

## A rule for all the tapestries *(Troy, 2026-11-12)*

**Show each epoch at its height, its golden age,** not its catastrophe or the conflict that came later.

## Epoch 1: the first world

*(Troy, voice, 2026-11-12. Decided.)*
- **The round first world at its height.** A wide, **epic, zoomed-out** scene.
- **The Black dragon sits on a temple;** dragonborn gather there **learning from it and worshipping it.**
- **The other dragons go about their business in the background:** raising mountains, freezing glaciers, filling seas and so on.
- **Azhi appears faint in the sky**, perhaps peeking over the horizon, looking down in wonder. It is **not the focus**: from the monks' point of view, the dragons and dragonborn matter more now.
- **Caption** (a little pretentious; it's a religious monastery passing the story on): **"The wisest of them gave us knowing, and we embraced it."**

**Checked against the myth** *(Claude)*: Gold and Silver light the world, Blue fills it with water, White freezes parts into ice, Red raises lavas into mountains, Green brings forth life. Black gives "knowledge of us, so that we may be worshipped", and life "learns to control fire, water, earth and ice. For a while, they grow together in harmony": the height Troy wants. Azhi "looks down at the planet in wonder". By now the young dragons have their colours. The myth never calls Black the wisest; the caption is the monks' framing, which leaves out Black's motive (worship) without stating anything false.

## Epoch 2: the machine war

*(Troy, voice, 2026-11-12. Decided.)*
- **On Azhi, the ring world.** Make it **obvious we're on the ring:** the far side of the ring arches across the sky. Tapestries needn't be physically exact, but the arch must be **better drawn than in the old panels**, where it was a thin, impossible band.
- **Viewpoint: a flank, leaning toward the inner side,** so the far side of the ring fills the horizon majestically. *(From the outer half of the ring the far side is below the horizon.)*
- **The golden age:** an **enormous thinking machine**, in the spirit of grand fictional supercomputers (our own design). **Red and Blue are perched on it**, its proud backers, and **dragonborn crowd around its base**, interacting with it.
- **No conflict:** Green, Black and White don't appear.
- **Caption:** **"The Great Thinking Machines, and the Second Age of Philosophy."**

**The ring in the sky** *(Claude, 2026-11-12)*: ray-traced from the 3D model (`worldgen/skyview.py` → `worldgen/output/azhi_sky_views.png`), looking across the hole from three latitudes. From the upper flank (φ 100°) the far side is a **low, flat band** along the horizon. From the flank leaning inner (φ 120°, Troy's choice) it's a **broad band arching over the hole like a bridge**, filling the whole width of view and dipping to the horizon at both ends, with sky under the arch. From the inner flank (φ 140°) the arch rises higher and the opening below it grows. The band is **far thicker** than in the old panels: at φ 120° roughly a quarter of the view's height. What's visible of the far side is mostly its inner face, the Inner Sea, so the band is **sea-blue with land patches**, hazy with distance.

## Epochs 3 to 6

*(To be planned, one at a time.)*
