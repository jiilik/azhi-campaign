# Parts Bin: Classes and Feats, Scored

**Status: PROPOSED, tentative** (opened 2026-11-05). Every part of the SRD and *Player's Handbook* classes and feats, broken down and given a best-guess score on the Character Origins point scale. It feeds the two-tree progression (`canon/brainstorm-progression.md`) and the extended traits (`canon/brainstorm-extended-traits.md`). Scores are Claude's best guesses, to be redone in balance passes.

**Sources and wording.**

- **SRD parts** come from `srd/03-classes/` and `srd/05-feats/feats.md` (SRD 5.2.1, CC BY 4.0). Feat parts quote the SRD; class parts are short summaries in SRD terms, with the full text in the class files.
- **PHB parts** (the 36 non-SRD subclasses and the non-SRD feats) are **generic summaries written from memory**, not the book's text. Names are checked against published lists; effects are not. Check against the book before relying on one, and reword anything used.

**The Tree column** guesses where a part belongs in the two-tree design: **E**, the experience tree (learned, kept on phasing); **P**, the phasing tree (nature, reset on phasing); **?**, unsure. The ? cases are mostly faith, pacts and bonds, which need a ruling.

## 1. The yardstick

From Character Origins (`canon/brainstorm-species.md` §4; CANON as a tentative tool):

| Item | Points |
|---|---|
| +1 to an ability score | 4 |
| Origin feat, or +2 to abilities | 8 |
| Skill proficiency | 1.5 |
| Tool proficiency | 1 |
| Starting gear | 1 |

**Extensions for classes** *(Claude, PROPOSED)*, each anchored to an existing value where possible:

| Item | Points | Anchor |
|---|---|---|
| Hit Die, per step above d6 | 4 (d8 4, d10 8, d12 12) | +1 average HP per level, half of Tough (+2 per level, an Origin feat, 8) |
| Saving throw proficiency | 4 for Dex, Con or Wis; 2.5 for Str, Int or Cha | Resilient: +1 (4) plus a save, as a General feat (about 8) |
| Light armour; Medium; Heavy; Shield | 2; 2; 3; 2 | Lightly Armored: +1 (4) plus light and Shield (4) |
| Simple weapons; Martial weapons | 0.5; 3 | Martial Weapon Training: +1 (4) plus martial (about 3) |
| Weapon Mastery, first kind; each more | 3; 1 | Weapon Master: +1 plus one mastery |
| Expertise, per skill | 2.5 | Skill Expert: +1, a skill (1.5) and an Expertise |
| Cantrip | 2 | Magic Initiate: two cantrips, a level 1 spell and a list (8) |
| Full spellcasting, per level | 10 at level 1; 7 at each level that opens a new spell level (3, 5 … 17); 3 otherwise | About 99 over 20 levels |
| Half spellcasting (Paladin, Ranger) | 6 at level 1; 5 at levels 5, 9, 13 and 17; 2 otherwise | About 56 |
| One-third spellcasting (Eldritch Knight, Arcane Trickster) | 10 at level 3, with cantrips; 4 at 7, 13 and 19; 1.5 otherwise | About 43 |
| Pact Magic | 7 at level 1; 3 at 2; 5 at 3, 5, 7 and 9; 2 otherwise to 10; 1 after | About 48, plus Mystic Arcanum (5 each) and invocations (3.5 each) |
| Extra Attack; a third attack; a fourth | 16; 10; 8 | About two General feats' worth of damage at level 5 |
| Sneak Attack | 6 for 1d6; 3 per extra die | About 33 by level 19; the Rogue's answer to Extra Attack |

The Ability Score Improvement and Epic Boon class features are left out of the class totals: in the two-tree design they become phasing-tree picks.

## 2. Classes

### Barbarian

**Starting kit (entry node): 31 points.** d12 Hit Die (12); Str and Con saves (6.5); 2 skills (3); Simple and Martial weapons (3.5); Light and Medium armour, Shields (6).

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 1 | Rage: Resistance to B/P/S, Rage Damage, Advantage on Str checks and saves; uses scale | 12 | P | 2,2 at 9 and 16 for damage, uses |
| 1 | Unarmored Defense (10 + Dex + Con) | 4 | ? | training or toughness? |
| 1 | Weapon Mastery (2 kinds, rising to 4) | 5 | E |  |
| 2 | Danger Sense (Advantage on Dex saves) | 3 | P |  |
| 2 | Reckless Attack | 6 | P | the Bold |
| 3 | Primal Knowledge (a skill; some checks use Str while raging) | 3 | P |  |
| 5 | Extra Attack | 16 | E |  |
| 5 | Fast Movement (+10 Speed) | 3 | P |  |
| 7 | Feral Instinct (Advantage on Initiative) | 4 | P |  |
| 7 | Instinctive Pounce (move half Speed on entering Rage) | 2 | P |  |
| 9 | Brutal Strike (forgo Advantage for +1d10 and an effect) | 6 | P |  |
| 11 | Relentless Rage (drop to 1 HP instead of 0) | 6 | P |  |
| 13 | Improved Brutal Strike (more effects) | 3 | P |  |
| 15 | Persistent Rage | 4 | P |  |
| 17 | Improved Brutal Strike (2d10, two effects) | 3 | P |  |
| 18 | Indomitable Might (Str score as minimum on Str checks) | 4 | P |  |
| 20 | Primal Champion (+4 Str and Con, maximum 25) | 16 | P |  |

**Path of the Berserker** (SRD subclass)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Frenzy (extra damage on the first Reckless hit) | 6 | P |  |
| 6 | Mindless Rage (immune to Charmed, Frightened) | 4 | P |  |
| 10 | Retaliation (Reaction melee attack) | 5 | P |  |
| 14 | Intimidating Presence (frighten a 30-ft area) | 6 | P |  |

**Path of the Wild Heart** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Animal Speaker (beast-sensing and animal-speech rituals) | 2 | P |  |
| 3 | Rage of the Wilds (choose bear, eagle or wolf each Rage) | 8 | P |  |
| 6 | Aspect of the Wilds (darkvision, climb or swim) | 3 | P | owl darkvision clashes |
| 10 | Nature Speaker (commune-with-nature ritual) | 2 | P |  |
| 14 | Power of the Wilds (flight, distraction or knock-down while raging) | 6 | P |  |

**Path of the World Tree** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Vitality of the Tree (Temporary HP for you and allies while raging) | 7 | P |  |
| 6 | Branches of the Tree (Reaction: pull a foe to you, stop it) | 6 | P |  |
| 10 | Battering Roots (longer reach; push or topple riders) | 5 | P |  |
| 14 | Travel along the Tree (teleport while raging, with allies) | 6 | P |  |

**Path of the Zealot** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Divine Fury (extra radiant or necrotic on the first hit) | 6 | ? | faith |
| 3 | Warrior of the Gods (a pool of healing dice) | 5 | ? | faith |
| 6 | Fanatical Focus (reroll a failed save while raging) | 4 | P |  |
| 10 | Zealous Presence (a war cry: Advantage for many allies) | 6 | ? |  |
| 14 | Rage of the Gods (flight, resistances, prevent an ally's death) | 10 | ? |  |

### Bard

**Starting kit (entry node): 20.5 points.** d8 Hit Die (4); Dex and Cha saves (6.5); 3 skills (any) (4.5); Simple weapons (0.5); 3 musical instruments (3); Light armour (2).

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 1 | Bardic Inspiration (d6, Cha uses; die grows) | 8 | ? | art or charisma? |
| 1 | Spellcasting, full (Cha); per-level values in §1 | 10 at gain; 99 by 20 | ? |  |
| 1 | Cantrips (2, rising to 4) | 4 at gain; 8 by 20 | E |  |
| 2 | Expertise (2 skills) | 5 | E |  |
| 2 | Jack of All Trades (half PB to non-proficient checks) | 4 | E |  |
| 5 | Font of Inspiration (regain on Short Rest; spend slots) | 4 | ? |  |
| 7 | Countercharm (Reaction reroll vs Charmed or Frightened) | 2 | ? |  |
| 9 | Expertise (2 more skills) | 5 | E |  |
| 10 | Magical Secrets (spells from other lists) | 6 | E |  |
| 18 | Superior Inspiration (regain on Initiative) | 3 | ? |  |
| 20 | Words of Creation (Power Word Heal and Kill, two targets) | 8 | E |  |

**College of Lore** (SRD subclass)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Bonus Proficiencies (3 skills) | 4.5 | E |  |
| 3 | Cutting Words (Reaction: subtract the die) | 6 | ? |  |
| 6 | Magical Discoveries (2 spells from any list) | 6 | E |  |
| 14 | Peerless Skill (add the die to a failed check) | 4 | E |  |

**College of Dance** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Dazzling Footwork (unarmoured AC with Cha; unarmed strikes with the die) | 7 | ? |  |
| 6 | Inspiring Movement (Reaction: you and an ally move) | 4 | ? |  |
| 6 | Tandem Footwork (boost Initiative with the die) | 3 | ? |  |
| 14 | Leading Evasion (Evasion, shared with allies nearby) | 5 | E |  |

**College of Glamour** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Beguiling Magic (charm spells; a free charm or fright after them) | 6 | ? | Feywild flavour |
| 3 | Mantle of Inspiration (Temporary HP and free movement for allies) | 6 | ? |  |
| 6 | Mantle of Majesty (a free command each turn) | 6 | ? |  |
| 14 | Unbreakable Majesty (attackers must save or pick another target) | 6 | ? |  |

**College of Valor** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Martial Training (martial weapons, medium armour, Shields) | 7 | E |  |
| 3 | Combat Inspiration (the die adds to damage or AC) | 4 | ? |  |
| 6 | Extra Attack (a cantrip can replace one attack) | 14 | E |  |
| 14 | Battle Magic (a Bonus Action attack after a spell) | 6 | E |  |

### Cleric

**Starting kit (entry node): 20 points.** d8 Hit Die (4); Wis and Cha saves (6.5); 2 skills (3); Simple weapons (0.5); Light and Medium armour, Shields (6).

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 1 | Spellcasting, full (Wis) | 10 at gain; 99 by 20 | ? |  |
| 1 | Cantrips (3, rising to 5) | 6 at gain; 10 by 20 | ? |  |
| 1 | Divine Order (Protector: martial and heavy armour; or Thaumaturge: cantrip and lore bonus) | 5 | ? |  |
| 2 | Channel Divinity (Divine Spark, Turn Undead; more uses later) | 8 | ? | faith |
| 5 | Sear Undead | 2 | ? |  |
| 7 | Blessed Strikes (Divine Strike or Potent Spellcasting) | 5 | ? |  |
| 10 | Divine Intervention (a free spell of level 5 or lower) | 8 | ? |  |
| 14 | Improved Blessed Strikes | 3 | ? |  |
| 20 | Greater Divine Intervention (can choose Wish) | 6 | ? | Wish lore clash |

**Life Domain** (SRD subclass)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Disciple of Life (extra healing) | 4 | ? |  |
| 3 | Life Domain Spells (always prepared) | 6 | ? |  |
| 3 | Preserve Life (Channel Divinity mass heal) | 5 | ? |  |
| 6 | Blessed Healer (heal yourself when healing others) | 3 | ? |  |
| 17 | Supreme Healing (maximum healing dice) | 4 | ? |  |

**Light Domain** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Domain Spells | 6 | ? |  |
| 3 | Radiance of the Dawn (dispel darkness, radiant burst) | 5 | ? |  |
| 3 | Warding Flare (Reaction: Disadvantage on an attack) | 5 | ? |  |
| 6 | Improved Warding Flare (adds Temporary HP) | 3 | ? |  |
| 17 | Corona of Light (sunlight aura; foes save at Disadvantage) | 6 | ? |  |

**Trickery Domain** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Blessing of the Trickster (Stealth Advantage for an ally) | 2 | ? |  |
| 3 | Domain Spells | 6 | ? |  |
| 3 | Invoke Duplicity (an illusory double to cast from) | 6 | ? |  |
| 6 | Trickster's Transposition (swap places with it) | 3 | ? |  |
| 17 | Improved Duplicity (it aids and heals allies) | 4 | ? |  |

**War Domain** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Domain Spells | 6 | ? |  |
| 3 | Guided Strike (+10 to an attack) | 4 | ? |  |
| 3 | War Priest (Bonus Action attacks, limited uses) | 6 | ? |  |
| 6 | War God's Blessing (key buffs without Concentration) | 4 | ? |  |
| 17 | Avatar of Battle (Resistance to B/P/S) | 7 | ? |  |

### Druid

**Starting kit (entry node): 19 points.** d8 Hit Die (4); Int and Wis saves (6.5); 2 skills (3); Simple weapons (0.5); Herbalism Kit (1); Light armour, Shields (4).

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 1 | Spellcasting, full (Wis) | 10 at gain; 99 by 20 | ? |  |
| 1 | Cantrips (2, rising to 4) | 4 at gain; 8 by 20 | ? |  |
| 1 | Druidic (secret language; Speak with Animals prepared) | 2 | E |  |
| 1 | Primal Order (Magician: cantrip and lore bonus; or Warden: martial weapons, medium armour) | 5 | ? |  |
| 2 | Wild Shape (beast forms; uses scale) | 12 | P | shape-changing, epoch 3 |
| 2 | Wild Companion (Find Familiar via Wild Shape) | 3 | P | familiar is Fey |
| 5 | Wild Resurgence (trade slots and Wild Shape uses) | 3 | P |  |
| 7 | Elemental Fury (Potent Spellcasting or Primal Strike) | 5 | ? |  |
| 15 | Improved Elemental Fury | 3 | ? |  |
| 18 | Beast Spells (cast while shape-changed) | 3 | P |  |
| 20 | Archdruid (Wild Shape regained; slots from uses; slow ageing) | 6 | P |  |

**Circle of the Land** (SRD subclass)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Circle of the Land Spells (by land type) | 6 | ? | lands of Azhi's body |
| 3 | Land's Aid (heal and harm burst) | 5 | ? |  |
| 6 | Natural Recovery (regain slots; free circle spell) | 4 | ? |  |
| 10 | Nature's Ward (poison immunity; a resistance) | 4 | P |  |
| 14 | Nature's Sanctuary (protective grove) | 5 | ? |  |

**Circle of the Moon** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Circle Forms (stronger forms, Temporary HP, better AC) | 10 | P |  |
| 3 | Circle of the Moon Spells | 4 | ? |  |
| 6 | Improved Circle Forms (radiant attacks; Wis to Con saves) | 4 | P |  |
| 10 | Moonlight Step (Bonus Action teleport) | 5 | P | Silver |
| 14 | Lunar Form (extra radiant damage; carry an ally) | 5 | P |  |

**Circle of the Sea** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Circle of the Sea Spells | 5 | ? |  |
| 3 | Wrath of the Sea (a cold, shoving aura) | 7 | P | Blue |
| 6 | Aquatic Affinity (larger aura; swim Speed) | 3 | P |  |
| 10 | Stormborn (flight and resistances in the aura) | 6 | P |  |
| 14 | Oceanic Gift (give the aura to an ally) | 4 | P |  |

**Circle of the Stars** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Star Map (free guiding spells) | 4 | E | sky-readers |
| 3 | Starry Form (archer, chalice or dragon) | 9 | P |  |
| 6 | Cosmic Omen (Reaction: add or subtract a die) | 5 | E |  |
| 10 | Twinkling Constellations (stronger forms; flight) | 4 | P |  |
| 14 | Full of Stars (Resistance to B/P/S in form) | 7 | P |  |

### Fighter

**Starting kit (entry node): 30 points.** d10 Hit Die (8); Str and Con saves (6.5); 2 skills (3); Simple and Martial weapons (3.5); All armour, Shields (9).

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 1 | Fighting Style | 5 | E |  |
| 1 | Second Wind (Bonus Action heal; uses scale) | 5 | E |  |
| 1 | Weapon Mastery (3 kinds, rising to 6; swap) | 7 | E |  |
| 2 | Action Surge (rising to two uses) | 9 | E |  |
| 2 | Tactical Mind (Second Wind boosts a failed check) | 3 | E |  |
| 5 | Extra Attack | 16 | E |  |
| 5 | Tactical Shift (move after Second Wind) | 2 | E |  |
| 9 | Indomitable (reroll a save; uses scale) | 5 | E |  |
| 9 | Tactical Master (swap mastery properties) | 3 | E |  |
| 11 | Two Extra Attacks | 10 | E |  |
| 13 | Studied Attacks (Advantage after a miss) | 3 | E |  |
| 20 | Three Extra Attacks | 8 | E |  |

**Champion** (SRD subclass)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Improved Critical (19–20) | 4 | E |  |
| 3 | Remarkable Athlete (Advantage on Initiative and Athletics; move on a crit) | 4 | E |  |
| 7 | Additional Fighting Style | 5 | E |  |
| 10 | Heroic Warrior (Heroic Inspiration each turn) | 6 | ? |  |
| 15 | Superior Critical (18–20) | 3 | E |  |
| 18 | Survivor (Advantage on Death Saves; regain HP while Bloodied) | 7 | ? |  |

**Battle Master** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Combat Superiority (superiority dice and manoeuvres) | 12 | E |  |
| 3 | Student of War (a tool and a skill) | 2.5 | E |  |
| 7 | Know Your Enemy (assess a foe) | 1 | E |  |
| 10 | Improved Combat Superiority (bigger dice) | 3 | E |  |
| 15 | Relentless (regain a die) | 2 | E |  |
| 18 | Ultimate Combat Superiority (bigger dice) | 3 | E |  |

**Eldritch Knight** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Spellcasting, one-third (Int), with cantrips | 10 at gain; 43 by 20 | E |  |
| 3 | War Bond (summon a bonded weapon) | 2 | E |  |
| 7 | War Magic (a cantrip replaces an attack) | 4 | E |  |
| 10 | Eldritch Strike (a hit gives the target Disadvantage on a save) | 3 | E |  |
| 15 | Arcane Charge (teleport on Action Surge) | 3 | E |  |
| 18 | Improved War Magic (a spell replaces two attacks) | 5 | E |  |

**Psi Warrior** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Psionic Power (dice: shield an ally, strike, move things) | 10 | ? | no psionics yet |
| 7 | Telekinetic Adept (psionic leaps and shoves) | 4 | ? |  |
| 10 | Guarded Mind (psychic resistance; end Charmed or Frightened) | 4 | ? |  |
| 15 | Bulwark of Force (half cover for allies) | 3 | ? |  |
| 18 | Telekinetic Master (telekinesis, with attacks) | 6 | ? |  |

### Monk

**Starting kit (entry node): 16.5 points.** d8 Hit Die (4); Str and Dex saves (6.5); 2 skills (3); Simple and Light martial weapons (2); A tool or instrument (1).

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 1 | Martial Arts (scaling die; Bonus Action strike; Dex for strikes) | 10 | E |  |
| 1 | Unarmored Defense (10 + Dex + Wis) | 5 | E |  |
| 2 | Monk's Focus (Focus Points: Flurry, Patient Defense, Step of the Wind) | 10 | E |  |
| 2 | Unarmored Movement (+10 Speed, rising) | 4 | E |  |
| 2 | Uncanny Metabolism (regain Focus, heal) | 3 | E |  |
| 3 | Deflect Attacks | 5 | E |  |
| 4 | Slow Fall | 1.5 | E |  |
| 5 | Extra Attack | 16 | E |  |
| 5 | Stunning Strike | 8 | E |  |
| 6 | Empowered Strikes (force damage) | 2 | E |  |
| 7 | Evasion | 5 | E |  |
| 9 | Acrobatic Movement (walls and water) | 2 | E |  |
| 10 | Heightened Focus (better Flurry, Defense, Step) | 4 | E |  |
| 10 | Self-Restoration (end Charmed, Frightened, Poisoned) | 3 | E |  |
| 13 | Deflect Energy (any damage type) | 3 | E |  |
| 14 | Disciplined Survivor (all saves; reroll) | 8 | E |  |
| 15 | Perfect Focus | 2 | E |  |
| 18 | Superior Defense (Resistance to most damage) | 6 | E |  |
| 20 | Body and Mind (+4 Dex and Wis, maximum 25) | 16 | E |  |

**Warrior of the Open Hand** (SRD subclass)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Open Hand Technique (Flurry topples, pushes or denies Reactions) | 6 | E |  |
| 6 | Wholeness of Body (self-heal) | 4 | E |  |
| 11 | Fleet Step (Step of the Wind with another Bonus Action) | 3 | E |  |
| 17 | Quivering Palm | 6 | E |  |

**Warrior of Mercy** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Hand of Harm (extra necrotic; poison) | 4 | E |  |
| 3 | Hand of Healing (heal with Focus) | 5 | E |  |
| 3 | Implements of Mercy (Insight, Medicine, Herbalism Kit) | 4 | E |  |
| 6 | Physician's Touch (cure conditions) | 3 | E |  |
| 11 | Flurry of Healing and Harm | 4 | E |  |
| 17 | Hand of Ultimate Mercy (revive the dead) | 5 | E |  |

**Warrior of Shadow** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Shadow Arts (magical darkness you see through; illusion cantrip) | 6 | E | darkness clash |
| 6 | Shadow Step (teleport between shadows) | 6 | E |  |
| 11 | Improved Shadow Step | 3 | E |  |
| 17 | Cloak of Shadows (invisible, pass through) | 6 | E |  |

**Warrior of the Elements** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Elemental Attunement (reach, elemental damage, push or pull) | 6 | E |  |
| 3 | Manipulate Elements (elemental cantrip) | 2 | E |  |
| 6 | Elemental Burst (area damage) | 5 | E |  |
| 11 | Stride of the Elements (fly and swim Speeds) | 5 | E |  |
| 17 | Elemental Epitome (resistance, extra damage) | 7 | E |  |

### Paladin

**Starting kit (entry node): 30 points.** d10 Hit Die (8); Wis and Cha saves (6.5); 2 skills (3); Simple and Martial weapons (3.5); All armour, Shields (9).

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 1 | Lay On Hands (healing pool, 5 × level) | 8 | ? | faith |
| 1 | Spellcasting, half (Cha) | 6 at gain; 56 by 20 | ? |  |
| 1 | Weapon Mastery (2 kinds) | 5 | E |  |
| 2 | Fighting Style (or Blessed Warrior: 2 cantrips) | 5 | E |  |
| 2 | Paladin's Smite (a free Divine Smite per Long Rest) | 3 | ? |  |
| 3 | Channel Divinity (Divine Sense) | 4 | ? | detects scrapped types |
| 5 | Extra Attack | 16 | E |  |
| 5 | Faithful Steed (a free Find Steed) | 4 | ? |  |
| 6 | Aura of Protection (Cha to allies' saves) | 14 | ? | the key paladin feature |
| 9 | Abjure Foes (frighten foes) | 4 | ? |  |
| 10 | Aura of Courage | 3 | ? |  |
| 11 | Radiant Strikes (+1d8 radiant on hits) | 8 | ? |  |
| 14 | Restoring Touch (Lay On Hands ends conditions) | 2 | ? |  |
| 18 | Aura Expansion (30 ft) | 3 | ? |  |

**Oath of Devotion** (SRD subclass)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Oath of Devotion Spells | 5 | ? |  |
| 3 | Sacred Weapon (Cha to attacks) | 5 | ? |  |
| 7 | Aura of Devotion (immune to Charmed) | 3 | ? |  |
| 15 | Smite of Protection (half cover) | 3 | ? |  |
| 20 | Holy Nimbus (radiant aura; save Advantage) | 6 | ? |  |

**Oath of Glory** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Oath Spells | 5 | ? |  |
| 3 | Peerless Athlete (athletic boost) | 2 | ? |  |
| 3 | Inspiring Smite (Temporary HP for allies) | 4 | ? |  |
| 7 | Aura of Alacrity (Speed for you and allies) | 4 | ? |  |
| 15 | Glorious Defense (Reaction AC boost, counter-attack) | 5 | ? |  |
| 20 | Living Legend (Cha Advantage; turn misses into hits) | 7 | ? |  |

**Oath of the Ancients** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Oath Spells | 5 | ? | fey flavour |
| 3 | Nature's Wrath (restrain with vines) | 4 | ? |  |
| 7 | Aura of Warding (resistance to some magic damage) | 5 | ? |  |
| 15 | Undying Sentinel (drop to 1 HP; no ageing) | 4 | ? |  |
| 20 | Elder Champion (regeneration, quick spells, weaker foe saves) | 7 | ? |  |

**Oath of Vengeance** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Oath Spells | 5 | ? |  |
| 3 | Vow of Enmity (Advantage against one foe) | 6 | ? |  |
| 7 | Relentless Avenger (stop a fleeing foe) | 3 | ? |  |
| 15 | Soul of Vengeance (Reaction attack) | 5 | ? |  |
| 20 | Avenging Angel (flight; frightening aura) | 7 | ? |  |

### Ranger

**Starting kit (entry node): 28.5 points.** d10 Hit Die (8); Str and Dex saves (6.5); 3 skills (4.5); Simple and Martial weapons (3.5); Light and Medium armour, Shields (6).

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 1 | Spellcasting, half (Wis) | 6 at gain; 56 by 20 | E |  |
| 1 | Favored Enemy (free Hunter's Mark; uses scale) | 6 | E |  |
| 1 | Weapon Mastery (2 kinds) | 5 | E |  |
| 2 | Deft Explorer (Expertise in a skill; 2 languages) | 4 | E |  |
| 2 | Fighting Style (or Druidic Warrior: 2 cantrips) | 5 | E |  |
| 5 | Extra Attack | 16 | E |  |
| 6 | Roving (+10 Speed; climb and swim) | 4 | E |  |
| 9 | Expertise (2 skills) | 5 | E |  |
| 10 | Tireless (Temporary HP; less Exhaustion) | 4 | E |  |
| 13 | Relentless Hunter (Concentration on the mark can't break) | 2 | E |  |
| 14 | Nature's Veil (Bonus Action invisibility) | 5 | E |  |
| 17 | Precise Hunter (Advantage against the mark) | 5 | E |  |
| 18 | Feral Senses (Blindsight 30 ft) | 4 | E | darkness clash |
| 20 | Foe Slayer (mark damage d10) | 3 | E |  |

**Hunter** (SRD subclass)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Hunter's Lore (learn a marked foe's defences) | 2 | E |  |
| 3 | Hunter's Prey (Colossus Slayer or Horde Breaker) | 5 | E |  |
| 7 | Defensive Tactics | 4 | E |  |
| 11 | Superior Hunter's Prey (spread the mark's damage) | 4 | E |  |
| 15 | Superior Hunter's Defense (Reaction resistance) | 4 | E |  |

**Beast Master** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Primal Companion (a beast of land, sea or sky) | 12 | ? | a bond, kept or lost? |
| 7 | Exceptional Training (better commands; force damage) | 3 | ? |  |
| 11 | Bestial Fury (two attacks; mark damage) | 5 | ? |  |
| 15 | Share Spells | 3 | ? |  |

**Fey Wanderer** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Dreadful Strikes (psychic damage) | 4 | ? | Feywild clash |
| 3 | Otherworldly Glamour (Wis to Cha checks; a skill) | 3 | ? |  |
| 3 | Fey Wanderer Spells | 4 | ? |  |
| 7 | Beguiling Twist (redirect charm or fear) | 4 | ? |  |
| 11 | Fey Reinforcements (summon a fey spirit) | 4 | ? | Fey scrapped |
| 15 | Misty Wanderer (teleport with an ally) | 4 | ? |  |

**Gloom Stalker** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Dread Ambusher (Wis to Initiative; extra first-turn damage) | 6 | E |  |
| 3 | Umbral Sight (darkvision; unseen by darkvision) | 5 | E | darkness clash |
| 3 | Gloom Stalker Spells | 4 | E |  |
| 7 | Iron Mind (Wis save proficiency) | 4 | E |  |
| 11 | Stalker's Flurry (better dread strikes) | 4 | E |  |
| 15 | Shadowy Dodge (Reaction: Disadvantage on an attack) | 4 | E |  |

### Rogue

**Starting kit (entry node): 21.5 points.** d8 Hit Die (4); Dex and Int saves (6.5); 4 skills (6); Simple and Finesse or Light martial weapons (2); Thieves' Tools (1); Light armour (2).

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 1 | Expertise (2 skills) | 5 | E |  |
| 1 | Sneak Attack (1d6, rising to 10d6) | 6 at gain; 33 by 20 | E |  |
| 1 | Thieves' Cant (and a language) | 1.5 | E | the Undertow? |
| 1 | Weapon Mastery (2 kinds) | 5 | E |  |
| 2 | Cunning Action (Dash, Disengage, Hide as Bonus Actions) | 7 | E |  |
| 3 | Steady Aim | 4 | E |  |
| 5 | Cunning Strike (trade Sneak Attack dice for effects) | 5 | E |  |
| 5 | Uncanny Dodge | 6 | E |  |
| 6 | Expertise (2 skills) | 5 | E |  |
| 7 | Evasion | 5 | E |  |
| 7 | Reliable Talent (treat 9 or lower as 10) | 6 | E |  |
| 11 | Improved Cunning Strike (two effects) | 2 | E |  |
| 14 | Devious Strikes (daze, knock out, obscure) | 4 | E |  |
| 15 | Slippery Mind (Wis and Cha saves) | 6.5 | E |  |
| 18 | Elusive (no Advantage against you) | 5 | E |  |
| 20 | Stroke of Luck (turn a failed d20 into a 20) | 4 | E |  |

**Thief** (SRD subclass)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Fast Hands (Bonus Action items and tools) | 5 | E |  |
| 3 | Second-Story Work (climb Speed; Dex jumps) | 2 | E |  |
| 9 | Supreme Sneak (stealthy Cunning Strike) | 3 | E |  |
| 13 | Use Magic Device (extra attunement; scrolls) | 4 | E |  |
| 17 | Thief's Reflexes (two turns in round one) | 6 | E |  |

**Arcane Trickster** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Spellcasting, one-third (Int), with cantrips | 10 at gain; 43 by 20 | E |  |
| 3 | Mage Hand Legerdemain (invisible, deft Mage Hand) | 2 | E |  |
| 9 | Magical Ambush (Disadvantage on saves while hidden) | 3 | E |  |
| 13 | Versatile Trickster (Mage Hand distracts for Advantage) | 3 | E |  |
| 17 | Spell Thief (steal a spell) | 4 | E |  |

**Assassin** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Assassinate (Advantage on Initiative; first-round damage) | 6 | E |  |
| 3 | Assassin's Tools (Disguise and Poisoner's Kits) | 2 | E | Indigo |
| 9 | Infiltration Expertise (false identity; mimicry) | 2 | E |  |
| 13 | Envenom Weapons (extra poison) | 3 | E |  |
| 17 | Death Strike (double damage on a failed save) | 6 | E |  |

**Soulknife** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Psionic Power (dice: knack, whispers) | 6 | ? | no psionics yet |
| 3 | Psychic Blades | 6 | ? |  |
| 9 | Soul Blades (homing strikes; blade teleport) | 4 | ? |  |
| 13 | Psychic Veil (invisibility) | 5 | ? |  |
| 17 | Rend Mind (stun) | 4 | ? |  |

### Sorcerer

**Starting kit (entry node): 10 points.** d6 Hit Die (0); Con and Cha saves (6.5); 2 skills (3); Simple weapons (0.5).

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 1 | Spellcasting, full (Cha) | 10 at gain; 99 by 20 | P |  |
| 1 | Cantrips (4, rising to 6) | 8 at gain; 12 by 20 | P |  |
| 1 | Innate Sorcery (Advantage and +1 DC, twice per Long Rest) | 5 | P |  |
| 2 | Font of Magic (Sorcery Points; slots to points and back) | 8 | P |  |
| 2 | Metamagic (2 options, 4 at 10, 6 at 17) | 8 | ? | technique or innate? |
| 5 | Sorcerous Restoration (regain points on a Short Rest) | 3 | P |  |
| 7 | Sorcery Incarnate (Innate Sorcery from points; two Metamagics) | 4 | P |  |
| 20 | Arcane Apotheosis (a free Metamagic each turn) | 5 | P |  |

**Draconic Sorcery** (SRD subclass)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Draconic Resilience (+1 HP per level; AC 10 + Dex + Cha) | 7 | P |  |
| 3 | Draconic Spells | 5 | P |  |
| 6 | Elemental Affinity (resistance; add Cha to damage) | 4 | P | chromatic types |
| 14 | Dragon Wings (Fly Speed 60) | 5 | P | White's flight |
| 18 | Dragon Companion (a free Summon Dragon) | 5 | P | dragons are gods |

**Aberrant Sorcery** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Psionic Spells | 5 | P | things from beyond |
| 3 | Telepathic Speech | 2 | P |  |
| 6 | Psionic Sorcery (cast with points, no components) | 4 | P |  |
| 6 | Psychic Defenses (psychic resistance; charm and fear Advantage) | 3 | P |  |
| 14 | Revelation in Flesh (flight, swimming, seeing the invisible…) | 6 | P |  |
| 18 | Warping Implosion (teleport and implode) | 5 | P |  |

**Clockwork Sorcery** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Clockwork Spells | 5 | P | the thinking machines |
| 3 | Restore Balance (cancel Advantage or Disadvantage) | 5 | P |  |
| 6 | Bastion of Law (a ward of dice) | 4 | P |  |
| 14 | Trance of Order (rolls of 9 or lower count as 10) | 6 | P |  |
| 18 | Clockwork Cavalcade (heal, repair, dispel) | 5 | P |  |

**Wild Magic Sorcery** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Wild Magic Surge | 3 | P | Azhi's vestige |
| 3 | Tides of Chaos (gain Advantage) | 4 | P |  |
| 6 | Bend Luck (add or subtract a die) | 5 | P |  |
| 14 | Controlled Chaos (roll surges twice) | 2 | P |  |
| 18 | Tamed Surge (choose a surge) | 5 | P |  |

### Warlock

**Starting kit (entry node): 16 points.** d8 Hit Die (4); Wis and Cha saves (6.5); 2 skills (3); Simple weapons (0.5); Light armour (2).

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 1 | Pact Magic (Cha; Short Rest slots) | 7 at gain; 48 by 20 | ? |  |
| 1 | Cantrips (2, rising to 4) | 4 at gain; 8 by 20 | ? |  |
| 1 | Eldritch Invocations (1, rising to 10; about 3.5 each) | 3.5 at gain; 35 by 20 | ? |  |
| 2 | Magical Cunning (regain half the slots once per Long Rest) | 3 | ? |  |
| 9 | Contact Patron (a free Contact Other Plane) | 2 | ? | planes |
| 11 | Mystic Arcanum (one spell each of levels 6–9 per Long Rest) | 5 at gain; 20 by 20 | ? |  |
| 20 | Eldritch Master (regain all slots once per Long Rest) | 4 | ? |  |

**Fiend Patron** (SRD subclass)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Dark One's Blessing (Temporary HP on a kill) | 5 | ? | Lower Planes |
| 3 | Fiend Spells | 5 | ? |  |
| 6 | Dark One's Own Luck (+1d10 to a check or save) | 5 | ? |  |
| 10 | Fiendish Resilience (a chosen resistance) | 5 | ? |  |
| 14 | Hurl Through Hell | 6 | ? |  |

**Archfey Patron** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Archfey Spells | 5 | ? | Feywild clash |
| 3 | Steps of the Fey (free short teleports with riders) | 6 | ? |  |
| 6 | Misty Escape (teleport when hurt) | 4 | ? |  |
| 10 | Beguiling Defenses (charm immunity; turn it back) | 4 | ? |  |
| 14 | Bewitching Magic (a free teleport after enchantments) | 4 | ? |  |

**Celestial Patron** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Celestial Spells (and radiant cantrips) | 5 | ? | Upper Planes clash |
| 3 | Healing Light (a pool of healing dice) | 6 | ? |  |
| 6 | Radiant Soul (radiant resistance; extra damage) | 4 | ? |  |
| 10 | Celestial Resilience (Temporary HP for the party) | 5 | ? |  |
| 14 | Searing Vengeance (rise from 0 HP in a burst) | 5 | ? |  |

**Great Old One Patron** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Great Old One Spells | 5 | ? | things from beyond |
| 3 | Awakened Mind (telepathy) | 3 | ? |  |
| 3 | Psychic Spells (psychic damage; quiet casting) | 2 | ? |  |
| 6 | Clairvoyant Combatant (Disadvantage for a foe) | 4 | ? |  |
| 10 | Eldritch Hex and Thought Shield | 6 | ? |  |
| 14 | Create Thrall | 5 | ? |  |

### Wizard

**Starting kit (entry node): 10 points.** d6 Hit Die (0); Int and Wis saves (6.5); 2 skills (3); Simple weapons (0.5).

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 1 | Spellcasting, full (Int), with a spellbook | 10 at gain; 99 by 20 | E |  |
| 1 | Cantrips (3, rising to 5) | 6 at gain; 10 by 20 | E |  |
| 1 | Spellbook (learn any Wizard spell from scrolls and books; prepare from it) | 6 | E |  |
| 1 | Ritual Adept (rituals from the book unprepared) | 3 | E |  |
| 1 | Arcane Recovery (regain slots on a Short Rest) | 4 | E |  |
| 2 | Scholar (Expertise in a lore skill) | 2.5 | E |  |
| 5 | Memorize Spell (swap a prepared spell) | 2 | E |  |
| 18 | Spell Mastery (two spells at will) | 7 | E |  |
| 20 | Signature Spells (two free level 3 spells) | 6 | E |  |

**Evoker** (SRD subclass)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Evocation Savant (free evocation spells in the book) | 2 | E |  |
| 3 | Potent Cantrip (half damage on a miss) | 3 | E |  |
| 6 | Sculpt Spells (spare allies) | 5 | E |  |
| 10 | Empowered Evocation (Int to damage) | 4 | E |  |
| 14 | Overchannel (maximum damage) | 6 | E |  |

**Abjurer** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Abjuration Savant | 2 | E |  |
| 3 | Arcane Ward (a damage-absorbing ward) | 8 | E |  |
| 6 | Projected Ward (shield an ally) | 4 | E |  |
| 10 | Spell Breaker (better counter- and dispel magic) | 5 | E |  |
| 14 | Spell Resistance (save Advantage; magic damage resistance) | 7 | E |  |

**Diviner** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Divination Savant | 2 | E |  |
| 3 | Portent (replace two d20 rolls a day) | 9 | E |  |
| 6 | Expert Divination (regain slots) | 4 | E |  |
| 10 | The Third Eye (darkvision, see invisible or read languages) | 3 | E | darkness clash |
| 14 | Greater Portent (three rolls) | 4 | E |  |

**Illusionist** (PHB subclass; generic, from memory)

| Level | Part | Points | Tree | Note |
|---|---|---|---|---|
| 3 | Illusion Savant | 2 | E |  |
| 3 | Improved Illusions (quieter, longer illusions) | 3 | E |  |
| 6 | Phantasmal Creatures (illusory summons) | 4 | E |  |
| 10 | Illusory Self (an attack misses) | 5 | E |  |
| 14 | Illusory Reality (make an illusion real) | 6 | E |  |

## 3. Totals check

Starting kit plus core features plus the SRD subclass, without the Ability Score Improvements and Epic Boon. If the scale is sound, classes should land near each other at each level; where they don't, either the scale or the class is off.

| Class | Kit | Level 1 | Level 5 | Level 10 | Level 20 |
|---|---|---|---|---|---|
| Barbarian | 31 | 52 | 89 | 110 | 152 |
| Bard | 20.5 | 42.5 | 88 | 132 | 193 |
| Cleric | 20 | 41 | 88 | 129 | 188 |
| Druid | 19 | 40 | 91 | 129 | 192 |
| Fighter | 30 | 47 | 85 | 104 | 135 |
| Monk | 16.5 | 31.5 | 85 | 105 | 149 |
| Paladin | 30 | 49 | 102 | 139 | 187 |
| Ranger | 28.5 | 45.5 | 88.5 | 118.5 | 171.5 |
| Rogue | 21.5 | 39 | 74 | 99 | 145.5 |
| Sorcerer | 10 | 33 | 86 | 119 | 180 |
| Warlock | 16 | 30.5 | 74.5 | 111.5 | 162 |
| Wizard | 10 | 39 | 70.5 | 104.5 | 169.5 |

**Subclasses by total at level 20** (their own parts only):

| Class | Subclasses |
|---|---|
| Barbarian | Path of the Berserker 21; Path of the Wild Heart 21; Path of the World Tree 24; Path of the Zealot 31 |
| Bard | College of Lore 20.5; College of Dance 19; College of Glamour 24; College of Valor 31 |
| Cleric | Life Domain 22; Light Domain 25; Trickery Domain 21; War Domain 27 |
| Druid | Circle of the Land 24; Circle of the Moon 28; Circle of the Sea 25; Circle of the Stars 29 |
| Fighter | Champion 29; Battle Master 23.5; Eldritch Knight 60; Psi Warrior 27 |
| Monk | Warrior of the Open Hand 19; Warrior of Mercy 25; Warrior of Shadow 21; Warrior of the Elements 25 |
| Paladin | Oath of Devotion 22; Oath of Glory 27; Oath of the Ancients 25; Oath of Vengeance 26 |
| Ranger | Hunter 19; Beast Master 23; Fey Wanderer 23; Gloom Stalker 27 |
| Rogue | Thief 20; Arcane Trickster 55; Assassin 19; Soulknife 25 |
| Sorcerer | Draconic Sorcery 26; Aberrant Sorcery 25; Clockwork Sorcery 25; Wild Magic Sorcery 19 |
| Warlock | Fiend Patron 26; Archfey Patron 23; Celestial Patron 25; Great Old One Patron 25 |
| Wizard | Evoker 20; Abjurer 26; Diviner 22; Illusionist 20 |

## 4. Feats

Every feat in the SRD 5.2.1 and the 2024 *Player's Handbook*, broken into parts and grouped by what the parts do. This section was moved here from `canon/brainstorm-extended-traits.md` §4 on 2026-11-05, and the Points column was added. SRD parts quote the SRD; PHB parts are generic summaries written from memory. **In use** names a personality trait or form that already uses the part. **Points** score the part alone; the +1 ability increase that most PHB General feats carry is scored separately, in 4.1. **Feat** gives the source: SRD (S) or PHB (P).

### 4.1 Ability scores

| Part | Feat | In use | Points |
|---|---|---|---|
| "Increase one ability score of your choice by 2, or increase two ability scores of your choice by 1. This feat can't increase an ability score above 20." | Ability Score Improvement (S) | Base traits give +1 each | 8 |
| +1 to one of two or three listed abilities, to a maximum of 20 (the PHB General feats nearly all have this) | most General feats (P); "Ability Score Increase. Increase your Strength or Dexterity score by 1, to a maximum of 20." Grappler (S) | Base traits | 4 |
| "Increase one ability score of your choice by 1, to a maximum of 30." | every Epic Boon (S, P) | | 4 |

### 4.2 Initiative and surprise

| Part | Feat | In use | Points |
|---|---|---|---|
| "When you roll Initiative, you can add your Proficiency Bonus to the roll." | Alert (S) | **The Bold** (*Quick to Act*) | 5 |
| "Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing ally in the same combat. You can't make this swap if you or the ally has the Incapacitated condition." | Alert (S) | **The Strategist** (*Initiative Swap*) | 3 |

### 4.3 Skills, tools and knowledge

| Part | Feat | In use | Points |
|---|---|---|---|
| "You gain proficiency in any combination of three skills or tools of your choice." | Skilled (S) | The Curious (two) | 4.5 |
| Proficiency in one skill, plus Expertise in one skill you're proficient in | Skill Expert (P) | | 4 |
| Proficiency, or Expertise if already proficient, in one of a few knowledge skills; the Study action as a Bonus Action | Keen Mind (P) | | 4 |
| Proficiency, or Expertise if already proficient, in Insight, Investigation or Perception; the Search action as a Bonus Action | Observant (P) | | 4.5 |
| Proficiency with three artisan's tools; a discount on nonmagical items; craft simple gear quickly during a rest | Crafter (P) | | 5 |
| Proficiency with three musical instruments | Musician (P) | The Magnificent (one) | 3 |
| Advantage on deception or performance checks while disguised; mimic voices and sounds, seen through with an Insight check | Actor (P) | **Indigo** (*Masquerade*) pairs with it | 4 |
| Cook's Utensils; extra healing from food on a Short Rest; treats that give Temporary Hit Points | Chef (P) | Cut from the Generous (2026-10-30) | 4 |
| Poisoner's Kit: brew doses that deal poison damage and poison; your poison damage ignores Resistance | Poisoner (P) | | 4 |
| Proficiency in every skill, plus Expertise in one | Boon of Skill (P, epic) | | 12 |

### 4.4 Armour and weapon training

| Part | Feat | In use | Points |
|---|---|---|---|
| Light armour and Shield training | Lightly Armored (P) | The Guardian (Shield training) | 4 |
| Medium armour training (requires light) | Moderately Armored (P) | | 2 |
| Heavy armour training (requires medium) | Heavily Armored (P) | | 3 |
| Proficiency with Martial weapons | Martial Weapon Training (P) | | 3 |
| Use the mastery property of one more kind of weapon; can be changed on a Long Rest | Weapon Master (P) | | 3 |
| Add up to +3 Dexterity to AC in medium armour; no Stealth penalty in it | Medium Armor Master (P) | | 2 |
| Reduce bludgeoning, piercing and slashing damage by your PB while in heavy armour | Heavy Armor Master (P) | | 4 |
| "While you're wearing Light, Medium, or Heavy armor, you gain a +1 bonus to Armor Class." | Defense (S, style) | The Guardian (+1 AC with a Shield) | 5 |

### 4.5 Weapon attacks and damage

| Part | Feat | In use | Points |
|---|---|---|---|
| "Once per turn when you hit a target with a weapon, you can roll the weapon's damage dice twice and use either roll against the target." | Savage Attacker (S) | | 6 |
| "You gain a +2 bonus to attack rolls you make with Ranged weapons." | Archery (S, style) | | 6 |
| "…you can treat any 1 or 2 on a damage die as a 3. The weapon must have the Two-Handed or Versatile property…" | Great Weapon Fighting (S, style) | | 2 |
| "When you make an extra attack as a result of using a weapon that has the Light property, you can add your ability modifier to the damage of that attack…" | Two-Weapon Fighting (S, style) | | 4 |
| +2 damage with a one-handed melee weapon and no other weapon | Dueling (P, style) | | 5 |
| Draw a thrown weapon as part of the attack; +2 damage with thrown weapons | Thrown Weapon Fighting (P, style) | | 3 |
| With a Heavy weapon, add your PB to damage; a critical hit or a kill gives a Bonus Action attack | Great Weapon Master (P) | | 6 |
| Ignore Loading; no Disadvantage in melee range; add your modifier to the off-hand crossbow attack | Crossbow Expert (P) | The Rock (*Cool Under Pressure*) | 4 |
| Ignore half and three-quarters cover; no Disadvantage at long range or in melee range | Sharpshooter (P) | The Rock (partly) | 5 |
| Two-weapon fighting with non-Light weapons; draw two weapons at once | Dual Wielder (P) | | 4 |
| Once per turn, a **bludgeoning** hit pushes the target 5 feet; a critical hit gives allies Advantage against it | Crusher (P) | | 3 |
| Once per turn, reroll one **piercing** damage die; a critical hit adds a die | Piercer (P) | | 3 |
| Once per turn, a **slashing** hit cuts the target's Speed by 10 feet; a critical hit gives it Disadvantage on attacks | Slasher (P) | | 3 |
| Long reach and polearms: a Bonus Action strike with the haft; an Opportunity Attack when a creature enters your reach | Polearm Master (P) | | 5 |
| A Dash or a straight run before a melee hit adds damage or pushes the target | Charger (P) | | 3 |
| "When you miss with an attack roll, you can hit instead. Once you use this benefit, you can't use it again until the start of your next turn." | Boon of Combat Prowess (S, epic) | | 10 |
| "The Bludgeoning, Piercing, and Slashing damage you deal always ignores Resistance." On a 20, extra damage equal to the boosted score | Boon of Irresistible Offense (S, epic) | | 8 |

### 4.6 Unarmed strikes and grappling

| Part | Feat | In use | Points |
|---|---|---|---|
| "When you hit a creature with an Unarmed Strike as part of the Attack action on your turn, you can use both the Damage and the Grapple option. You can use this benefit only once per turn." | Grappler (S) | | 1.5 |
| "You have Advantage on attack rolls against a creature Grappled by you." | Grappler (S) | | 1 |
| "You don't have to spend extra movement to move a creature Grappled by you if the creature is your size or smaller." | Grappler (S) | | 0.5 |
| Unarmed Strikes deal 1d4 + Strength; reroll 1s on that damage; proficiency with improvised weapons; once per turn, push 5 feet | Tavern Brawler (P) | **The Scrapper** (*Brawler*, improvised weapons) | 4 |
| Unarmed Strikes deal d6, or d8 with both hands free; a creature you grapple takes damage each turn | Unarmed Fighting (P, style) | The Scrapper (d4) | 4 |

### 4.7 Defence, Reactions and protecting allies

| Part | Feat | In use | Points |
|---|---|---|---|
| A Reaction with a Finesse weapon adds your PB to AC against one melee attack | Defensive Duelist (P) | | 4 |
| Reaction: reduce the damage to an ally within 5 feet by 1d10 + PB (needs a Shield or weapon) | Interception (P, style) | The Guardian (*Shield Bearer*) | 4 |
| Reaction: give Disadvantage on attacks against an ally within 5 feet (needs a Shield) | Protection (P, style) | | 3 |
| Shield bash after an attack (push or knock Prone); take no damage on a successful Dexterity save against an area effect, using the Shield | Shield Master (P) | | 4 |
| Opportunity Attacks against a creature that Disengages or attacks an ally; a hit stops its movement | Sentinel (P) | The Rock (*Hold Your Ground*) | 5 |
| Advantage on attacks against unmounted smaller creatures; protect your mount | Mounted Combatant (P) | | 2 |

### 4.8 Hit points, healing and resistance

| Part | Feat | In use | Points |
|---|---|---|---|
| +2 HP per level | Tough (P) | The Hearty (+1 per level) | 8 |
| Advantage on Death Saving Throws; spend a Hit Point Die as a Bonus Action to heal | Durable (P) | The Devout (adds Wisdom to Death Saves) | 3 |
| Use a Healer's Kit so a creature spends a Hit Point Die and regains extra HP; reroll 1s on healing dice | Healer (P) | | 5 |
| After a rest, give Temporary Hit Points to a group of allies | Inspiring Leader (P) | | 4 |
| Resistance to two damage types (from a list); a Reaction to redirect that damage | Boon of Energy Resistance (P, epic) | The Hearty (Poison) | 8 |
| +40 HP max; extra healing once per turn | Boon of Fortitude (P, epic) | | 8 |
| Drop to 0 HP and regain half once per Long Rest; a pool of healing dice | Boon of Recovery (P, epic) | | 9 |

### 4.9 Saving throws and luck

| Part | Feat | In use | Points |
|---|---|---|---|
| Proficiency in one saving throw, plus +1 to that ability | Resilient (P) | | 3.5 |
| A pool of luck points (equal to PB) per Long Rest: give yourself Advantage, or an attacker Disadvantage | Lucky (P) | The Dreamer (*Déjà Vu*, once per rest) | 8 |
| After a rest, give some allies Heroic Inspiration | Musician (P) | | 5 |
| "When you or another creature within 60 feet of you succeeds on or fails a D20 Test, you can roll 2d4 and apply the total rolled as a bonus or penalty to the d20 roll." Once per Initiative or rest | Boon of Fate (S, epic) | The Theorist (*Harebrained Scheme*), similar | 8 |

### 4.10 Spellcasting

| Part | Feat | In use | Points |
|---|---|---|---|
| "You learn two cantrips of your choice from the Cleric, Druid, or Wizard spell list. Intelligence, Wisdom, or Charisma is your spellcasting ability for this feat's spells…" | Magic Initiate (S) | Base traits give one fixed cantrip each (Confidant, Devout, Generous, Magnificent) | 4 |
| "Choose a level 1 spell from the same list… You always have that spell prepared. You can cast it once without a spell slot… when you finish a Long Rest. You can also cast the spell using any spell slots you have." | Magic Initiate (S) | | 3 |
| "Whenever you gain a new level, you can replace one of the spells you chose for this feat…" | Magic Initiate (S) | | 1 |
| One fixed level 2 spell plus one level 1 spell of a chosen school, each castable once per Long Rest without a slot (teleport-and-charm themed) | Fey-Touched (P) | **Clashes:** the Fey are gone (2026-11-01) | 5 |
| As above, themed on invisibility and shadow | Shadow-Touched (P) | | 4.5 |
| Telepathy over a short range; one free *Detect Thoughts* per Long Rest | Telepathic (P) | **Clashes:** no psionics yet; the Unbound blocks mind-reading | 3 |
| An invisible, longer-range *Mage Hand*; a Bonus Action magical shove | Telekinetic (P) | | 4 |
| Learn some ritual spells and cast them as rituals; one quick ritual per Long Rest | Ritual Caster (P) | Black and Grey form rituals | 4 |
| Advantage on Concentration saves; cast a spell as an Opportunity Attack; perform somatic components with your hands full | War Caster (P) | **The Rock** (*Steady Hands*) | 5 |
| Spell attacks ignore cover and don't suffer Disadvantage in melee range; longer spell range | Spell Sniper (P) | | 4 |
| Spells of one damage type ignore Resistance; treat 1s as 2s on their damage | Elemental Adept (P) | | 3 |
| Disrupt a caster's Concentration when you hit it; once per Long Rest, turn a failed mental save into a success | Mage Slayer (P) | | 4 |
| "Whenever you cast a spell with a level 1–4 spell slot, roll 1d4. If the number you roll is the same as the slot's level, the slot isn't expended." | Boon of Spell Recall (S, epic) | | 9 |

### 4.11 Movement

| Part | Feat | In use | Points |
|---|---|---|---|
| +10 Speed; Dash ignores Difficult Terrain; Opportunity Attacks against you have Disadvantage | Speedy (P) | The Wanderer (+5) | 5 |
| Climb Speed equal to your Speed; standing up costs 5 feet; a running jump after only 5 feet | Athlete (P) | The Restless (stand at no cost) | 3 |
| "Immediately after you take the Attack action or the Magic action, you can teleport up to 30 feet to an unoccupied space you can see." | Boon of Dimensional Travel (S, epic) | | 9 |
| A large Speed increase; Disengage as a Bonus Action | Boon of Speed (P, epic) | | 8 |

### 4.12 Senses, stealth and darkness

| Part | Feat | In use | Points |
|---|---|---|---|
| Blindsight 10 feet | Blind Fighting (P, style); Skulker (P) | **Clashes** with Darkvision for Black and Indigo only (2026-10-24) | 3 |
| Missing with an attack while hidden doesn't reveal you | Skulker (P) | | 2 |
| "Truesight with a range of 60 feet." | Boon of Truesight (S, epic) | Clashes, as above, though only at level 19 | 8 |
| "While within Dim Light or Darkness, you can give yourself the Invisible condition as a Bonus Action…" and "…Resistance to all damage except Psychic and Radiant." | Boon of the Night Spirit (S, epic) | | 10 |

## 5. Observations *(Claude)*

- **The scale reproduces the martial–caster gap.** At level 20, full casters total about 160–195 points, and the Fighter, Rogue, Monk and Barbarian about 135–152. That matches the common view of the 2024 rules: martials keep up early and fall behind late. The two-tree design can choose to flatten it, for example by giving spellcasting nodes a higher cost.
- **Level 1 kits vary widely,** from 10 points (Sorcerer, Wizard) to 31 (Barbarian), because Hit Dice, armour and weapons are cheap per item but add up. Spellcasting at level 1 (about 10 points plus cantrips) is what levels the field. For the six entry nodes, a kit of about **20–30 points** plus one signature feature looks like the target.
- **Level 5 is the spike** that Troy's design expects five nodes in: Extra Attack (16) or level 3 spells (7, on top of the earlier levels). Most classes total 85–102 points at level 5; the Wizard (about 70) and the Rogue and Warlock (about 74) sit lower.
- **Subclasses total 19–31 points** each, SRD and PHB alike. The two one-third casters are the exception: about 55–60, because spellcasting is counted in them.
- **Many parts are unsure (?),** mostly faith (cleric, paladin), pacts (warlock) and bonds (the Beast Master's companion). One ruling, on whether faith and pacts survive phasing, would sort most of them.
