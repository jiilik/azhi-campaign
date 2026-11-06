# Brainstorm: Extended Traits (replacing feats)

**Status: PROPOSED** (opened 2026-11-05). This is the working record for the traits that replace feats. Troy's statements are marked *(Troy)*. Everything else is Claude's and is PROPOSED until Troy approves it.

## 1. The decision *(Troy, 2026-11-05)*

- **Feats are scrapped entirely.**
- At the levels where a character would normally get a feat, they get a **replacement set** of traits instead. The working name is **"extended traits"**, or something similar.
- The feats are broken down into a **toolbox of parts** (§4). The extended traits are then designed from those parts.
- **SRD feats** are broken down in the SRD's own wording (CC BY 4.0). **Player's Handbook feats** are described here in generic wording only. Anything taken from them is reworded again when the extended traits are written.
- This supersedes `canon/proposed-feat-changes.md`, which tried to fix individual feats.

## 2. Where the rules depend on feats

Removing feats breaks these rules. Each one needs replacement text. The search covered every SRD section file.

| # | Where | What it says now | Proposed replacement |
|---|---|---|---|
| W1 | **Ability Score Improvement**, in all 12 classes: levels 4, 8, 12 and 16; Fighter also at 6 and 14; Rogue also at 10 | "You gain the Ability Score Improvement feat… or another feat of your choice for which you qualify." | Gain an extended trait. See Q3 for whether a plain ability increase stays as an option. |
| W2 | **Epic Boon**, level 19 in all 12 classes | "You gain an Epic Boon feat… or another feat…", with a recommended boon for each class | Gain an epic extended trait (Q5). Keep the recommendations, renamed. |
| W3 | **Fighting Style**: Fighter level 1 (and the Champion's second style at 7), Paladin level 2, Ranger level 2 | "You gain a Fighting Style feat of your choice." | Turn the styles into class options, not feats (Q4). |
| W4 | **Warlock invocation *Lessons of the First Ones*** | Gives one Origin feat, repeatable | Gives one personality trait you don't have, repeatable (Q8). |
| W5 | **Character Creation**, step "Record Your Feat" | A background gives you a feat. | Already gone with backgrounds; delete it in the Character Creation revision. |
| W6 | **Level Advancement**, step 5 | "If you choose a feat that increases one or more of your ability scores…" | Change "feat" to "extended trait". |
| W7 | **Starting at Higher Levels**, the sidebar "Bonus Feats at Level 20" | Grant feats after level 20. | Grant extended traits after level 20. |
| W8 | **Gameplay Toolbox**, "Creating a Background", step 2 | "Choose one feat from the Origin category." | Delete with backgrounds, or rewrite as "creating a personality trait". |
| W9 | **Feats** chapter (`srd/05-feats/feats.md`) | The feats themselves | Replaced by an Extended Traits chapter. Delete the old file in the Phase 2d deletions commit. |

## 3. Questions for Troy

Numbered so they can be answered one at a time.

1. **The name.** **Settled (Troy, 2026-11-05): Extended Traits**, "for now".
2. **The shape of the list.** **Settled (Troy, 2026-11-05): a tech tree.** See §3a. *Original question:* Options:
   - (a) One shared list, like the 24 base traits.
   - (b) Each base trait grows into its own extended versions: the Bold becomes something more, and so does the Rock.
   - (c) Both: a shared list, plus some extended traits that require a particular base trait.
3. **Plain ability increases.** Does +2 to one ability (or +1 to two) survive as one choice in the set? Without it, a character could never raise their main ability to 20. *(Claude: recommend yes, as an extended trait of its own.)*
4. **Fighting Styles.** They're class features in disguise. Keep them as a list inside the classes, no longer called feats? *(Claude: recommend yes, so the Fighter, Paladin and Ranger aren't rebuilt.)*
5. **Epic Boons at level 19.** Keep them as an epic tier of extended traits, or fold them into the main list with a level 19 prerequisite?
6. **Ability increase on each extended trait.** Each base trait gives +1, and almost every PHB General feat does too. Should every extended trait give +1? *(Claude: recommend yes; it keeps the trade against a plain +2 fair.)*
7. **Prerequisites.** Keep ability prerequisites, such as Strength 13+, and training prerequisites, such as needing Shield training?
8. **The warlock invocation** (W4): change it to give a personality trait?
9. **Can a character take an unchosen base trait** as their extended trait, once they reach level 4? This is option A3 from the old feat list.
10. **Power target.** The base traits sit at about 10 points, below an Origin feat (the trait-benefits brainstorm). Should extended traits sit at about a PHB General feat's strength?

### 3a. The tech tree *(Troy, 2026-11-05)*

- Extended traits are **hierarchical and build on each other**, almost like a tech tree.
- Each path is **anchored** to a base personality trait (24) or a dragonborn form (9): 33 anchors.
- Assume each path goes **about five levels deep**, which allows for growth.
- **Some paths branch and some converge**, so a tier won't always have 33 traits.
- **Losing an anchor:** if a character phases and loses their anchor trait or form, they will likely need to **repick their extended traits**, perhaps with a delay, such as picking one per day as part of coming out of the phasing penalty.
- **Capstones are rare:** with only 5–7 picks over a career, most characters won't reach a capstone, but some will. "Munchkin city."
- **Form paths** are a little like the monster classes in 3rd edition's *Savage Species*: a dragonborn who follows their form's path may gain dragon traits. The trees give a path of advancement **in parallel to class advancement**.

- **Capstones at level 19** *(Troy, 2026-11-05)*: most characters won't reach a capstone, and that's fine. A character who took all five tiers of one path reaches tier 5 with the **level 19 Epic Boon** pick. The capstone should be **"epic as hell"**, to reward all the options set aside.
- **Phasing as a respec** *(Troy)*: phasing forces a repick, so it could be used to reach a capstone, or to escape one.
- **OPEN (Troy): does phasing change class?** For example, a White, Wisdom-built level 12 cleric phases into a Black, Intelligence-built form. Do they get the chance to become a level 12 wizard? Phasing may force a rebuild of the whole class structure around this idea. The character probably keeps their experience.

**Claude's notes** *(PROPOSED)*:
- **The pick count by class.** Feat levels are 4, 8, 12 and 16 for most classes, plus 6 and 14 for the Fighter and 10 for the Rogue, plus the Epic Boon at 19. So a single class gets **4 picks** (6 for a Fighter, 5 for a Rogue), and 5 counting level 19. If tier 1 needs a pick, most classes reach a tier-5 capstone only by spending every pick on one path, including level 19.
- **The Unphased** have no form to anchor to, and swap a trait each Long Rest. They may need their own path, or a rule.
- **Gold and Silver** forms (DM material) could have paths too.

### Claude's evaluation of Q2–Q10 (2026-11-05)

- **Q2 shape: (a) now, (c) later.** Extensions tied to a base trait break when that trait goes away: the Unphased swap a trait on every Long Rest, and phasing may cost traits (the tentative penalty keeps only one). A shared list avoids orphans. Trait-specific extensions can come later, with a rule that they go dormant if the base trait is lost.
- **Q3 plain +2: keep it**, as an option alongside the list, not as a trait. A starting main ability is 16–18 on Azhi, and many players will want 20 by level 8.
- **Q4 Fighting Styles: yes**, as class options. That keeps the Champion's second style at level 7, the Fighter's swap on level-up and the Paladin and Ranger alternatives working unchanged.
- **Q5 Epic Boons: a separate tier, keeping the name.** A "boon" reads naturally as a gift from one of the Seven, or from Azhi's vestige, at the level where dragonborn match the dragons in spellcasting.
- **Q6 +1 on each: yes**, to a maximum of 20. That makes the choice between one extended trait and a plain +2 a real one, as it is between a feat and an ASI in the 2024 rules.
- **Q7 prerequisites:** drop the ability-score ones, which in the 2024 rules rarely stop anyone. Keep the ones that make sense: training (armour, Shield), the Spellcasting feature, and level (19 for boons; perhaps 8+ for a few strong traits).
- **Q8 the warlock invocation: yes**, a base personality trait, but without its ability increase, since the invocation never gave one.
- **Q9 base traits as picks: yes.** A base trait is weaker than an extended trait, so it can't be abused, and it lets a character's personality grow over a campaign, which was the backlog idea.
- **Q10 power: about a PHB General feat**, including its +1, so about as attractive as a plain +2. Epic Boons stay at the PHB boons' level.

## 4. The toolbox

Every feat in the SRD 5.2.1 and the 2024 *Player's Handbook* is broken into parts, grouped by what each part does.

**Sources and wording:**
- **SRD parts** quote the SRD's own wording, from `srd/05-feats/feats.md`, cut down to the mechanic. The SRD is CC BY 4.0.
- **PHB parts** are generic, plain-language summaries of what the feat does, written from memory. They aren't the book's text. The feat names and categories were checked against a published list (Wargamer, "2024 feats"); the effects were not, so check them against the book before relying on one.

**Columns:**
- **Feat** gives the feat's name and its source: SRD (S) or PHB (P).
- **In use** names a personality trait or form that already uses the part. Those parts are spent, or may only stack.

### 4.1 Ability scores

| Part | Feat | In use |
|---|---|---|
| "Increase one ability score of your choice by 2, or increase two ability scores of your choice by 1. This feat can't increase an ability score above 20." | Ability Score Improvement (S) | Base traits give +1 each |
| +1 to one of two or three listed abilities, to a maximum of 20 (the PHB General feats nearly all have this) | most General feats (P); "Ability Score Increase. Increase your Strength or Dexterity score by 1, to a maximum of 20." Grappler (S) | Base traits |
| "Increase one ability score of your choice by 1, to a maximum of 30." | every Epic Boon (S, P) | |

### 4.2 Initiative and surprise

| Part | Feat | In use |
|---|---|---|
| "When you roll Initiative, you can add your Proficiency Bonus to the roll." | Alert (S) | **The Bold** (*Quick to Act*) |
| "Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing ally in the same combat. You can't make this swap if you or the ally has the Incapacitated condition." | Alert (S) | **The Strategist** (*Initiative Swap*) |

### 4.3 Skills, tools and knowledge

| Part | Feat | In use |
|---|---|---|
| "You gain proficiency in any combination of three skills or tools of your choice." | Skilled (S) | The Curious (two) |
| Proficiency in one skill, plus Expertise in one skill you're proficient in | Skill Expert (P) | |
| Proficiency, or Expertise if already proficient, in one of a few knowledge skills; the Study action as a Bonus Action | Keen Mind (P) | |
| Proficiency, or Expertise if already proficient, in Insight, Investigation or Perception; the Search action as a Bonus Action | Observant (P) | |
| Proficiency with three artisan's tools; a discount on nonmagical items; craft simple gear quickly during a rest | Crafter (P) | |
| Proficiency with three musical instruments | Musician (P) | The Magnificent (one) |
| Advantage on deception or performance checks while disguised; mimic voices and sounds, seen through with an Insight check | Actor (P) | **Indigo** (*Masquerade*) pairs with it |
| Cook's Utensils; extra healing from food on a Short Rest; treats that give Temporary Hit Points | Chef (P) | Cut from the Generous (2026-10-30) |
| Poisoner's Kit: brew doses that deal poison damage and poison; your poison damage ignores Resistance | Poisoner (P) | |
| Proficiency in every skill, plus Expertise in one | Boon of Skill (P, epic) | |

### 4.4 Armour and weapon training

| Part | Feat | In use |
|---|---|---|
| Light armour and Shield training | Lightly Armored (P) | The Guardian (Shield training) |
| Medium armour training (requires light) | Moderately Armored (P) | |
| Heavy armour training (requires medium) | Heavily Armored (P) | |
| Proficiency with Martial weapons | Martial Weapon Training (P) | |
| Use the mastery property of one more kind of weapon; can be changed on a Long Rest | Weapon Master (P) | |
| Add up to +3 Dexterity to AC in medium armour; no Stealth penalty in it | Medium Armor Master (P) | |
| Reduce bludgeoning, piercing and slashing damage by your PB while in heavy armour | Heavy Armor Master (P) | |
| "While you're wearing Light, Medium, or Heavy armor, you gain a +1 bonus to Armor Class." | Defense (S, style) | The Guardian (+1 AC with a Shield) |

### 4.5 Weapon attacks and damage

| Part | Feat | In use |
|---|---|---|
| "Once per turn when you hit a target with a weapon, you can roll the weapon's damage dice twice and use either roll against the target." | Savage Attacker (S) | |
| "You gain a +2 bonus to attack rolls you make with Ranged weapons." | Archery (S, style) | |
| "…you can treat any 1 or 2 on a damage die as a 3. The weapon must have the Two-Handed or Versatile property…" | Great Weapon Fighting (S, style) | |
| "When you make an extra attack as a result of using a weapon that has the Light property, you can add your ability modifier to the damage of that attack…" | Two-Weapon Fighting (S, style) | |
| +2 damage with a one-handed melee weapon and no other weapon | Dueling (P, style) | |
| Draw a thrown weapon as part of the attack; +2 damage with thrown weapons | Thrown Weapon Fighting (P, style) | |
| With a Heavy weapon, add your PB to damage; a critical hit or a kill gives a Bonus Action attack | Great Weapon Master (P) | |
| Ignore Loading; no Disadvantage in melee range; add your modifier to the off-hand crossbow attack | Crossbow Expert (P) | The Rock (*Cool Under Pressure*) |
| Ignore half and three-quarters cover; no Disadvantage at long range or in melee range | Sharpshooter (P) | The Rock (partly) |
| Two-weapon fighting with non-Light weapons; draw two weapons at once | Dual Wielder (P) | |
| Once per turn, a **bludgeoning** hit pushes the target 5 feet; a critical hit gives allies Advantage against it | Crusher (P) | |
| Once per turn, reroll one **piercing** damage die; a critical hit adds a die | Piercer (P) | |
| Once per turn, a **slashing** hit cuts the target's Speed by 10 feet; a critical hit gives it Disadvantage on attacks | Slasher (P) | |
| Long reach and polearms: a Bonus Action strike with the haft; an Opportunity Attack when a creature enters your reach | Polearm Master (P) | |
| A Dash or a straight run before a melee hit adds damage or pushes the target | Charger (P) | |
| "When you miss with an attack roll, you can hit instead. Once you use this benefit, you can't use it again until the start of your next turn." | Boon of Combat Prowess (S, epic) | |
| "The Bludgeoning, Piercing, and Slashing damage you deal always ignores Resistance." On a 20, extra damage equal to the boosted score | Boon of Irresistible Offense (S, epic) | |

### 4.6 Unarmed strikes and grappling

| Part | Feat | In use |
|---|---|---|
| "When you hit a creature with an Unarmed Strike as part of the Attack action on your turn, you can use both the Damage and the Grapple option. You can use this benefit only once per turn." | Grappler (S) | |
| "You have Advantage on attack rolls against a creature Grappled by you." | Grappler (S) | |
| "You don't have to spend extra movement to move a creature Grappled by you if the creature is your size or smaller." | Grappler (S) | |
| Unarmed Strikes deal 1d4 + Strength; reroll 1s on that damage; proficiency with improvised weapons; once per turn, push 5 feet | Tavern Brawler (P) | **The Scrapper** (*Brawler*, improvised weapons) |
| Unarmed Strikes deal d6, or d8 with both hands free; a creature you grapple takes damage each turn | Unarmed Fighting (P, style) | The Scrapper (d4) |

### 4.7 Defence, Reactions and protecting allies

| Part | Feat | In use |
|---|---|---|
| A Reaction with a Finesse weapon adds your PB to AC against one melee attack | Defensive Duelist (P) | |
| Reaction: reduce the damage to an ally within 5 feet by 1d10 + PB (needs a Shield or weapon) | Interception (P, style) | The Guardian (*Shield Bearer*) |
| Reaction: give Disadvantage on attacks against an ally within 5 feet (needs a Shield) | Protection (P, style) | |
| Shield bash after an attack (push or knock Prone); take no damage on a successful Dexterity save against an area effect, using the Shield | Shield Master (P) | |
| Opportunity Attacks against a creature that Disengages or attacks an ally; a hit stops its movement | Sentinel (P) | The Rock (*Hold Your Ground*) |
| Advantage on attacks against unmounted smaller creatures; protect your mount | Mounted Combatant (P) | |

### 4.8 Hit points, healing and resistance

| Part | Feat | In use |
|---|---|---|
| +2 HP per level | Tough (P) | The Hearty (+1 per level) |
| Advantage on Death Saving Throws; spend a Hit Point Die as a Bonus Action to heal | Durable (P) | The Devout (adds Wisdom to Death Saves) |
| Use a Healer's Kit so a creature spends a Hit Point Die and regains extra HP; reroll 1s on healing dice | Healer (P) | |
| After a rest, give Temporary Hit Points to a group of allies | Inspiring Leader (P) | |
| Resistance to two damage types (from a list); a Reaction to redirect that damage | Boon of Energy Resistance (P, epic) | The Hearty (Poison) |
| +40 HP max; extra healing once per turn | Boon of Fortitude (P, epic) | |
| Drop to 0 HP and regain half once per Long Rest; a pool of healing dice | Boon of Recovery (P, epic) | |

### 4.9 Saving throws and luck

| Part | Feat | In use |
|---|---|---|
| Proficiency in one saving throw, plus +1 to that ability | Resilient (P) | |
| A pool of luck points (equal to PB) per Long Rest: give yourself Advantage, or an attacker Disadvantage | Lucky (P) | The Dreamer (*Déjà Vu*, once per rest) |
| After a rest, give some allies Heroic Inspiration | Musician (P) | |
| "When you or another creature within 60 feet of you succeeds on or fails a D20 Test, you can roll 2d4 and apply the total rolled as a bonus or penalty to the d20 roll." Once per Initiative or rest | Boon of Fate (S, epic) | The Theorist (*Harebrained Scheme*), similar |

### 4.10 Spellcasting

| Part | Feat | In use |
|---|---|---|
| "You learn two cantrips of your choice from the Cleric, Druid, or Wizard spell list. Intelligence, Wisdom, or Charisma is your spellcasting ability for this feat's spells…" | Magic Initiate (S) | Base traits give one fixed cantrip each (Confidant, Devout, Generous, Magnificent) |
| "Choose a level 1 spell from the same list… You always have that spell prepared. You can cast it once without a spell slot… when you finish a Long Rest. You can also cast the spell using any spell slots you have." | Magic Initiate (S) | |
| "Whenever you gain a new level, you can replace one of the spells you chose for this feat…" | Magic Initiate (S) | |
| One fixed level 2 spell plus one level 1 spell of a chosen school, each castable once per Long Rest without a slot (teleport-and-charm themed) | Fey-Touched (P) | **Clashes:** the Fey are gone (2026-11-01) |
| As above, themed on invisibility and shadow | Shadow-Touched (P) | |
| Telepathy over a short range; one free *Detect Thoughts* per Long Rest | Telepathic (P) | **Clashes:** no psionics yet; the Unbound blocks mind-reading |
| An invisible, longer-range *Mage Hand*; a Bonus Action magical shove | Telekinetic (P) | |
| Learn some ritual spells and cast them as rituals; one quick ritual per Long Rest | Ritual Caster (P) | Black and Grey form rituals |
| Advantage on Concentration saves; cast a spell as an Opportunity Attack; perform somatic components with your hands full | War Caster (P) | **The Rock** (*Steady Hands*) |
| Spell attacks ignore cover and don't suffer Disadvantage in melee range; longer spell range | Spell Sniper (P) | |
| Spells of one damage type ignore Resistance; treat 1s as 2s on their damage | Elemental Adept (P) | |
| Disrupt a caster's Concentration when you hit it; once per Long Rest, turn a failed mental save into a success | Mage Slayer (P) | |
| "Whenever you cast a spell with a level 1–4 spell slot, roll 1d4. If the number you roll is the same as the slot's level, the slot isn't expended." | Boon of Spell Recall (S, epic) | |

### 4.11 Movement

| Part | Feat | In use |
|---|---|---|
| +10 Speed; Dash ignores Difficult Terrain; Opportunity Attacks against you have Disadvantage | Speedy (P) | The Wanderer (+5) |
| Climb Speed equal to your Speed; standing up costs 5 feet; a running jump after only 5 feet | Athlete (P) | The Restless (stand at no cost) |
| "Immediately after you take the Attack action or the Magic action, you can teleport up to 30 feet to an unoccupied space you can see." | Boon of Dimensional Travel (S, epic) | |
| A large Speed increase; Disengage as a Bonus Action | Boon of Speed (P, epic) | |

### 4.12 Senses, stealth and darkness

| Part | Feat | In use |
|---|---|---|
| Blindsight 10 feet | Blind Fighting (P, style); Skulker (P) | **Clashes** with Darkvision for Black and Indigo only (2026-10-24) |
| Missing with an attack while hidden doesn't reveal you | Skulker (P) | |
| "Truesight with a range of 60 feet." | Boon of Truesight (S, epic) | Clashes, as above, though only at level 19 |
| "While within Dim Light or Darkness, you can give yourself the Invisible condition as a Bonus Action…" and "…Resistance to all damage except Psychic and Radiant." | Boon of the Night Spirit (S, epic) | |

## 5. Observations

- **About a dozen parts are already spent** on base traits: initiative, Brawler, Steady Hands, Hardy, Shield training, Long Stride and others. Extended traits should build on those parts rather than repeat them. For example, an extended Bold could add something new to *Quick to Act*, not add the Proficiency Bonus again.
- **The weapon-type trio** (bludgeoning, piercing and slashing riders) is a natural pattern for a small family of extended traits.
- **The "-Touched" pattern** (+1 ability, then two spells castable once each per Long Rest) maps neatly onto the spell origins: a trait could be "taught by" one of the Seven. Black-Touched, Silver-Touched, Green-Touched and so on.
- **Armour training** comes as a three-step chain in the PHB (light, then medium, then heavy). Folding the whole chain into one trait would save players two picks.
- **The setting clashes** (Fey-Touched, Telepathic, Blindsight, Truesight) can be fixed while redesigning, at no extra cost.
