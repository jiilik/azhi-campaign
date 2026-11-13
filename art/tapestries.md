# The Tapestry Hall: a player-facing history of Azhi (PLAN and first renders, 2026-11-12)

*(Troy, voice, 2026-11-12.)* The five lore panels (`cartoon/lore_panels.py`) are being redone as **six tapestries** hanging in a **White monastery**. Players walk through them one at a time; each tells one chapter, condensed.

- **The legend, not the DM's truth.** Secrets are simply left out, but nothing woven is false: **no misdirection**. *(Secrets to leave out are listed in `canon/brainstorm-epochs.md`: today's Black is the young Black, the living thinking machine, the buried weapons forge, Indigo's weapon secrets; Gold and Silver are only whispered about.)*
- **Captions: brief.** A short woven title, with a line or two at most.
- **Six tapestries:** Epoch 0 (Azhi meets the young dragons), then Epochs 1 to 5 (the first world, the machine war, the age of faith, the twins, the homunculi war). Epoch 6 is the present, so it has none.
- **Style:** Saturday-Morning Bold, which is **the White dragonborn's favoured art style** in the world, so the monastery's tapestries are naturally drawn in it. Realistic references (such as the ray-traced ring) become cartoony when woven. *(Open: whether to add a woven-tapestry frame or texture; Troy has said new drawing rules are coming.)*

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

**The ring in the sky** *(Claude, 2026-11-12)*: ray-traced from the 3D model (`worldgen/skyview.py` → `worldgen/output/azhi_sky_day.png` and `azhi_sky_night.png`, with clouds, haze, and light from the Gold or Silver dragon), looking across the hole from three latitudes. From the upper flank (φ 100°) the far side is a **low, flat band** along the horizon. From the flank leaning inner (φ 120°, Troy's choice) it's a **broad band arching over the hole like a bridge**, filling the whole width of view and dipping to the horizon at both ends, with sky under the arch. From the inner flank (φ 140°) the arch rises higher and the opening below it grows. The band is **far thicker** than in the old panels: at φ 120° roughly a quarter of the view's height. What's visible of the far side is mostly its inner face, the Inner Sea, so the band is **sea-blue with land patches**, hazy with distance.

## Who may appear when *(Troy, 2026-11-12)*

- **Yellow and Grey** dragonborn appear **only from Epoch 5** (they're the homunculi's converted followers).
- **Brown and Indigo** appear **only after the twins' war** *(Claude: the young Red became Brown and the elder Black became Indigo at the end of Epoch 4)*, so from Epoch 5. Epoch 4 shows the time before the war.
- So Epochs 1–4 show only the original seven colours (and the Unphased); Epoch 5 is the first with all nine.

## Epoch 3: the age of faith

*(Troy, voice, 2026-11-12. Decided.)*
- **Several temples in different architectural styles,** with **flowing banners in several colours.**
- **Three faiths, each with its own invented iconography** (to be **saved for reuse** later, even if never mentioned again):
  1. **The Black dragon's church.**
  2. **The Cult of the Ring,** one of Blue's creations: its symbol is **Azhi devouring itself**. *(It shares the house's ouroboros symbol; Troy: fine, as this is long before the present day, and a symbol can outlive its cult.)*
  3. **Machine revivalists**, longing for the thinking machines to return: their symbol echoes **the thinking machine as drawn in Epoch 2**.
- **Caption:** **"Tapping into the very power of creation itself, philosophies diverge."** *(Claude: true to the legend without spelling out the apocalypse.)*

## Epoch 4: the twins

*(Troy, voice, 2026-11-12. Decided.)* Keep the old panel's idea of **dragonborn looking at the empty eggshells** (one speckled blue, one green).
- **Before the twins phase** into Black and Red and go to war.
- **Behind the eggs, two young Unphased dragons cruise about,** shimmering every colour, and the **dragonborn in front point them out**: "Oh wow, look, new dragons!"
- **Blue and Green nuzzle in the background,** the proud parents.
- **Caption:** **"An accidental discovery: life springs forth anew."** *(Troy: life comes from Green and water from Blue. Claude: it echoes the myth, where "all life springs forth anew" after Azhi bites its own tail.)*

## Epoch 5: the homunculi war

*(Troy, voice, 2026-11-12. Decided.)* The civilization at its height, not the war.
- **The Yellow and Grey dragons sit on a hill, surrounded by their followers,** the newly phased Yellow and Grey dragonborn.
- **All nine colours** can appear: the first tapestry with Yellow, Grey, Brown and Indigo.
- **The real Gold and Silver dragons float in the sky** (with the ring visible), so no one mistakes Yellow and Grey for Gold and Silver.
- **Caption:** **"Earthly reflections of the sun and moon."**

**Checked** *(Claude)*: Epoch 4 was the first mass phasing (dragonborn phased in great numbers to fill the twins' armies), and the council banned it afterwards; the Yellow and Grey conversions in Epoch 5 were a loophole in that ban. The homunculi are adult dragons, homunculi of Gold and Silver. Nothing in the scene names the young Black, so the present-day secret (that today's Black is the young one) stays out.

## Epoch 6: no tapestry

*(Troy, 2026-11-12.)* Epoch 6 is **the present**, only about **200 years** old, so the hall has no tapestry for it. The hall holds **six tapestries, Epochs 0 to 5**.

## Render notes *(Claude, 2026-11-12; embellishments PROPOSED)*

Drawn by `cartoon/tapestries.py` (toolkit `cartoon/tapestry_lib.py`); the hall sheet is `cartoon/output/tapestry_hall.png`.
- **Frame:** each panel is woven, with a blue border knotted with small rings, a hanging rod with gold finials, a caption panel with the epoch number in medallions, a faint weave texture and a fringe. *(This settles the open frame question above unless Troy prefers otherwise.)*
- **Embellishments beyond the brief.** Each can be dropped:
  1. **Epoch 0:** of the seven hatchlings, one sits on Azhi's crown, one swings on a barbel and one lounges on its back, besides the listener, the lint-picker and the chasing pair. Also a moon with a bite out of it, a comet, a spiral galaxy, and golden curls for Azhi's voice.
  2. **Epoch 1:** each dragon shapes its own land: White on a glacier, Red at a volcano, Blue leaping from the sea, Green lounging in a blossoming forest. Elemental glyphs circle the teaching Black, and pilgrims walk in.
  3. **Epoch 2:** an academy city around the machine, a queue at its question slot, an answer tape, banderoles marked "?", "∴" and "!", and children.
  4. **Epoch 3:** beams of light rise from the three temples, with small shrines and a bazaar between them. A Blue huckster with a horn and a "The Ring!" scroll stands among processions. A White monk is sketching: the weavers' own nod.
  5. **Epoch 4:** the eggshells sit in a nest, with hearts over the nuzzling Blue and Green by a lake.
  6. **Epoch 5:** Yellow and Grey sit back to back, their tails meeting. Each gazes up at the one it reflects: Yellow at the setting Gold, Grey at the rising Silver. Sun and moon banners fly over the slopes, where the followers raise their arms; dragonborn of all nine colours gather below.

