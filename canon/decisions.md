# Decision Log

Newest first. One line per decision: what was decided, and why if a reason was given. Add to this log every time the author settles something, and update `canon/setting-bible.md` to match.

## 2026-10-21

- **Species design approved to canon.** Troy approved the whole design worked out in today's voice sessions. The specification is `canon/brainstorm-species.md`; its open items stay OPEN. More ribbons and more personality traits will be added later, for depth.
- **Character building:** a phased dragonborn takes one **affinity** (5 colours plus 5 hybrids) and two **personality traits**. An **Unphased** dragonborn takes three traits and no affinity, may swap one trait on each Long Rest, and may move those traits' +1s when it does.
- **Backgrounds are dropped.** Their benefits (ability scores, a feat-sized feature, skills, a tool) are folded into the affinities and traits, so personality matters more than background.
- **Ability scores:** +1 from each trait and +1 from the affinity (the 2024 +1/+1/+1 pattern). Each affinity's +1 goes to its form's primary ability: Red Str; Green Con; White Wis; Blue Dex or Cha; Black Int or Cha. Each hybrid chooses one of two parent abilities: Marsh Dex or Con; Soil Con or Str; Oxblood Str or Int; Slate Int or Wis; Glacier Wis or Cha.
- **Balance scale (tentative, can be redone):**
  - +1 to an ability is 4 points, an Origin feat 8, a skill 1.5, a tool 1, gear 1.
  - The budget is about 35 per character: about 10 per trait and about 16 per affinity.
  - The colours landed at 17–18.5 and the hybrids at about 13–16. Troy accepted this, since skills and tools are probably overvalued.
- **Personality traits:**
  - one shared list, not tied to colours;
  - each is a personality rather than a feat;
  - benefits are situational, never tied to a class;
  - 12 to start, two per ability.
- **Affinity rules:**
  - features fit the elemental wheel;
  - no combat abilities that a build must be designed around;
  - swapping belongs only to the Unphased; phased characters are settled;
  - swim, climb and fly speeds equal walking speed;
  - every form has two ribbons, worth 0 points.
- **Darkvision belongs to Black alone.** It is not a dragonborn baseline.
- **Hybrids** get their own signature feature, not their parents'. Their skill lists avoid each parent's core skills, with Slate's Religion as an exception. Names: Marsh, Soil, Oxblood, Slate and Glacier.
- **The elemental wheel and its adjacency** (Blue–Green–Red–Black–White) are now canon. They were PROPOSED.
- **Red's speed** is 35 feet in total; the Goliath's Large Form bonus doesn't stack. **Green's Regeneration** has no cold drawback.
- **Art:** the colour wheel (`art/cartoon/output/colour_wheel.png`) shows the Unphased as a shifting blend of all five colours.

## 2026-10-20

- **Dragonborn are born polychromatic (Unphased)** and settle into a **monochrome** or **bichrome** form tied to one or two adjacent colours of the five surface dragons. That gives 10 common forms. Blend order is irrelevant, and blends get pigment names (Green + Red = brown). This removes any basis for colour prejudice.
- **Phasing:** dramatic, traumatic or deadly events can change a dragonborn's form. They keep parts of their personality and most of their memories. There is a penalty to stop exploitation. Players can't return to Unphased; the DM may allow it rarely.
- **Settling triggers** are left to player backstories.
- **Power budget:** Unphased (playable, young; may swap some features or feats on a Long Rest) < bichrome (picks features from either colour) < monochrome.
- **Gold and Silver dragonborn** are super-rare NPCs with no easy player path, but their species definitions should exist.
- **Triage: Character Backgrounds** is deferred until more lore exists. **Species** is high-priority revise, with design held until the lore discussion is finished.
- **Triage: Playing the Game** stays unchanged for now. It will be reviewed later for logic or lore inconsistencies introduced by changes to later sections.
- **Triage: Character Creation.** Revise Step 2 (species → colour choice; languages) and Trinkets. Keep everything else. The revision waits until **Character Origins** is settled, because it depends on those decisions.
- **SRD intake.** The uploaded PDF is **SRD 5.2.1** (the April 2025 update of 5.2), so attribution names 5.2.1. The markdown comes from **downfallx/dnd-5e-srd-markdown** (commit `1b4b99d`), chosen over Claude's own PDF conversion because it is cleaner. A word-by-word check against the PDF found about 120 of 202,000 words differing (repeated table headers, line-break hyphenation). The PDF stays authoritative.
- **Quote style:** keep the straight quotes from the imported markdown; don't convert them to the PDF's curly quotes.
- **SRD file layout:** one file per section; one per class; spells and magic items by first letter; one file per monster group and per animal.
- **Myth status:** canonical for worldbuilding (it is what really happened), but in-universe some groups have built their own versions of the story.
- **Rules base: SRD 5.2** (the 2024 core rules, CC BY 4.0).
- **Git host: GitHub** (`jiilik/azhi-campaign`, private), chosen after considering Codeberg, because Claude's sessions integrate with it directly. Google Drive was tried for snapshots and rejected because of file-size limits.
- **Project structure:** a git repo plus a Claude Project. Durable state lives in files (`CLAUDE.md`, `PLAN.md`, `canon/`), not in chat history.
- **Handout story text must match the corrected myth exactly.** Claude had added four scene-break lines to the handout; they were removed. No other changes are allowed.
- **No ellipsis in the myth's last line.** The ellipsis came from the dramatic voice reading, which smoothed and paused freely. That reading is not canon text.
- **Handout scope:** the handout is myth and visuals only. The welcome or "session zero" paragraph was removed, because that information will live in the SRD-derived document. The author may trim more handout paragraphs.
- **Cover art:** the gift streams (water, lava, frost, leaves) were removed from the young dragons as "silly".
- **Art style:** **Saturday-Morning Bold** is the default for all future cartoons unless specified otherwise. It was chosen from four candidates (Bold, Chibi Cel-Shaded, Storybook Watercolour, Mid-Century Flat).
- **Myth proofread.** Applied changes 1, 3, 4, 5, 6, 7, 11, 13, 18 and 19:
  - Capital "If" in the first quoted resolution.
  - "and finds it rather too spicy".
  - "the company of speech".
  - "Azhi soon discovers".
  - "turn to gold and to silver".
  - "the simplest of tasks".
  - Capital "It is fine…".
  - "providing light by which the other dragons".
  - "nothing for which to live, there was".
  - "the very spine of its body is bound".
- **Rejected proofread changes** 2, 8, 9, 10, 12, 14, 15, 16, 17 and 20. They were stylistic. The author wants the text to feel legendary and timeless, and **tense shifts are deliberate**, to evoke oral narration. Do not "fix" tense, the it/he pronouns, "asunder of", "the mind of the old", "parallel idealism", and similar.

## 2026-10-19

- **Maps generated:** a conformal flat map that wraps on both axes, plus 3D torus views. Requested features:
  - mountains on the spine
  - water on the belly
  - subtle vestigial legs, arms and wings
  - a head landform, with a pronounced lower jaw raised above sea level on the inner side
- **Physics:** the spine has **infinite stiffness**, which prevents gravitational collapse. Land and water should be roughly Earth-like. The world should feel physically real except for the sun–moon cycle.
- **Peoples:** dragonborn of the seven colours are the only playable species, and there are **no other sentient species**.
- **No "racist dragons" trope.** Differences are elements in opposition, not superiority. The author finds roleplaying racist NPCs boring, tiring and distasteful.
- **The seven dragons are alive.** Gold and Silver are the sun and moon, giving an unpredictable day and night. The other five have elemental lairs on the surface. Each dragon has dragonborn descendants or followers who share its affinity.
- **The myth "Azhi: The Dragon Philosopher" (by the author) is in-universe scripture.**
- **The world is a torus:** the corpse of the space dragon Azhi, who ate itself to death, ouroboros-style.
