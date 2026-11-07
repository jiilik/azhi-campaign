# Parts Bin: Techniques (stamina and at-wills)

**Status: PROPOSED** (opened 2026-11-07). These are the parts for one unified technique system. It brings together the **monk's** Focus techniques, the **Battle Master's** manoeuvres, the **bard's** inspiration and command-and-control spells, and the **4th Edition warlord**. Troy asked for it so the parts can be shared out across the fantasy map of the skills grid (`canon/brainstorm-progression.md`). Everything here is Claude's and PROPOSED unless marked *(Troy)*.

**Sources and wording.**
- **SRD 5.2.1** (CC BY 4.0): the monk (`srd/03-classes/06-monk.md`) and the bard's features and spell list (`srd/03-classes/02-bard.md`). Summarized here in short form.
- **The Battle Master's manoeuvres** (2024 *Player's Handbook*) are **not in the SRD**. They are described here in my own words, from memory, and not checked against the book.
- **The 4th Edition warlord** is **not open content**. Its ideas are described here in my own words, under my own labels; none of its power names or text are used.

## 1. The framework

**Settled** *(Troy, 2026-11-07, voice)*:
- **Two pools.** **Stamina (SP)** fuels martial techniques; **mana (MP)** fuels spells.
- **Costs.** A technique costs **1 SP**; a spell costs mana by level (2, 3, 5, 6, 7, 9, 10, 11 and 13).
- **Recovery.** A Long Rest restores everything. A Short Rest restores points equal to your PB, **in each pool**.
- **Values.** Mana is valued at **2 points** per point on the parts-bin scale. Stamina stays at **1 point**, "like half spells".
- **Free techniques** are called **at-wills**.
- **The goal is one system** that covers the monk, manoeuvres, the bard and the warlord.

**Proposed** *(Claude; the skeleton was offered in voice, and Troy took it as a starting point)*:
- **Three parts.** Every technique has:
  - a **trigger**: an action, a Bonus Action, a Reaction, a rider on a hit, or a check
  - a **cost**: 0 for an at-will, otherwise SP
  - a **target**: yourself, an enemy, an ally, or an area
- **Typical targets by fantasy.** The monk mostly targets **itself**, manoeuvres target **enemies**, and the Herald targets **allies**.
- **The at-will / SP line comes from the SRD monk.** *Patient Defense* and *Step of the Wind* each have a **free version** (Disengage, or Dash, as a Bonus Action) and a **1-point version** (both actions, plus a rider). So:
  - an **at-will** is a small, reliable trick you can use every turn;
  - **SP** buys the bigger moment, or **upgrades an at-will**.
- **Converting spells.** A technique that copies a spell's effect costs **SP equal to that spell's mana price**: level 1 is 2 SP, level 2 is 3 SP, level 3 is 5 SP. This holds because one SP technique is worth about half a level 1 spell.
- **The manoeuvre die.** The Battle Master adds a superiority die to most manoeuvres. A single **technique die** (d6 at first, growing through nodes) would serve the Battle Master's die, the bard's inspiration die and the monk's martial-arts die alike. It would sit on line 3 of a tile only if it grows by adding up; otherwise it goes in the description.

**Columns used below:**
- **Trigger:** A = action; BA = Bonus Action; R = Reaction; Hit = rider on a hit; Check = adds to an ability check; Passive.
- **Cost:** at-will, or SP *n*.
- **Target:** Self, Enemy, Ally, or Area.
- **Home:** where it might live on the skills grid.
  - Herald = command; Hex = the hexer
  - Cha–Dex = swashbuckler and rogue
  - Scout = movement
  - Dex–Str = fighting styles and manoeuvres
  - Fighter = hit hard
  - Str–Con = armour
  - Tank = hit points
  - Con–Wis = monk
- **Pts:** a rough value for knowing the technique, on the parts-bin scale.

## 2. The monk (SRD)

| Part | Trigger | Cost | Target | Home | Pts | Note |
|---|---|---|---|---|---|---|
| Bonus Unarmed Strike (*Martial Arts*) | BA | at-will | Enemy | Con–Wis | 4 | Needs no armour and monk weapons |
| *Flurry of Blows*: two Unarmed Strikes | BA | SP 1 | Enemy | Con–Wis | 4 | Three strikes with *Heightened Focus* |
| *Patient Defense*: Disengage | BA | at-will | Self | Scout | 2 | The free half |
| *Patient Defense*: Disengage and Dodge | BA | SP 1 | Self | Con–Wis | 3 | Adds Temporary HP with *Heightened Focus* |
| *Step of the Wind*: Dash | BA | at-will | Self | Scout | 2 | The free half; Troy put Bonus Action movement on **ring 3** (2026-11-07) |
| *Step of the Wind*: Disengage and Dash, double jump | BA | SP 1 | Self | Scout | 3 | Carries an ally with *Heightened Focus* |
| *Deflect Attacks*: reduce damage by 1d10 + Dex + level | R | at-will | Self | Con–Wis | 5 | B/P/S only; any type with *Deflect Energy* |
| *Deflect Attacks*: redirect it | R | SP 1 | Enemy | Con–Wis | 3 | Only when the damage is reduced to 0 |
| *Slow Fall* | R | at-will | Self | Scout | 1.5 | |
| *Stunning Strike*: Con save or Stunned | Hit | SP 1 | Enemy | Con–Wis | 8 | Once per turn; the strongest single technique |
| *Uncanny Metabolism*: regain all points and heal | Initiative | 1/Long Rest | Self | Con–Wis | 3 | A recovery node, like the short-rest nodes Troy wants |
| *Disciplined Survivor*: reroll a failed save | R | SP 1 | Self | Con–Wis | 4 | |
| *Superior Defense*: Resistance to all but Force | Start of turn | SP 3 | Self | Con–Wis or Tank | 6 | |
| *Open Hand Technique*: addle, push or topple on a *Flurry* hit | Hit | rider | Enemy | Con–Wis | 6 | |
| *Wholeness of Body*: heal yourself | BA | uses | Self | Con–Wis | 4 | |
| *Quivering Palm* | Hit | SP 4 | Enemy | Con–Wis | 6 | A capstone |
| *Warrior of Mercy* (PHB, generic): extra necrotic harm, or healing, with your strikes | Hit or A | SP 1 | Enemy or Ally | Con–Wis or Mystic | 5 | |
| *Warrior of Shadow* (PHB, generic): teleport between shadows | BA | at-will or SP | Self | Cha–Dex | 6 | Avoid darkness and Darkvision (the forms' territory) |
| *Warrior of the Elements* (PHB, generic): reach and elemental damage; area bursts | Hit, A | SP 1–2 | Enemy, Area | Con–Wis | 6 | |

## 3. Battle Master manoeuvres (PHB; generic, from memory)

Each adds the technique die. In 5e each use spends one superiority die, which maps directly to **SP 1**.

| Part | Trigger | Cost | Target | Home | Pts |
|---|---|---|---|---|---|
| **Precision**: add the die to an attack roll | Attack roll | SP 1 | Self | Dex–Str | 2 |
| **Trip**: extra damage, and the target saves or falls Prone | Hit | SP 1 | Enemy | Dex–Str or Fighter | 2.5 |
| **Push**: extra damage, and the target saves or is pushed 15 ft | Hit | SP 1 | Enemy | Fighter | 2 |
| **Disarm**: extra damage, and the target saves or drops an item | Hit | SP 1 | Enemy | Dex–Str or Cha–Dex | 2 |
| **Menace**: extra damage, and the target saves or is Frightened | Hit | SP 1 | Enemy | Herald or Fighter | 2.5 |
| **Goad**: extra damage, and the target saves or has Disadvantage against anyone but you | Hit | SP 1 | Enemy | Str–Con or Tank | 2.5 |
| **Distract**: extra damage; the next ally's attack on it has Advantage | Hit | SP 1 | Enemy and Ally | Herald or Cha–Dex | 2.5 |
| **Reposition**: extra damage; an ally moves half Speed freely | Hit | SP 1 | Ally | Herald | 2.5 |
| **Sweep**: damage a second creature nearby | Hit | SP 1 | Enemy | Fighter | 2 |
| **Feint**: Bonus Action for Advantage on your next attack, plus the die | BA | SP 1 | Enemy | Cha–Dex | 2.5 |
| **Lunge**: more reach or a step for one attack, plus the die | Attack | SP 1 | Self | Dex–Str | 2 |
| **Parry**: reduce melee damage by the die plus your modifier | R | SP 1 | Self | Dex–Str or Str–Con | 2.5 |
| **Riposte**: when a foe misses you, attack it, plus the die | R | SP 1 | Enemy | Cha–Dex (swashbuckler) | 3 |
| **Evasive footwork**: the die to AC while you move | Move | SP 1 | Self | Scout | 2 |
| **Bait and switch**: swap places with an ally; one of you gains AC | Move | SP 1 | Ally | Herald or Scout | 2 |
| **Directed strike** (the commander's strike): give up an attack so an ally attacks, plus the die | BA + Attack | SP 1 | Ally | **Herald** | 3 |
| **Rally**: give an ally Temporary HP | BA | SP 1 | Ally | **Herald** | 2.5 |
| **Ambush**: the die to Stealth or Initiative | Check | SP 1 | Self | Cha–Dex or Scout | 1.5 |
| **Commanding presence**: the die to a social check | Check | SP 1 | Self | Herald | 1.5 |
| **Tactical assessment**: the die to a lore or Insight check | Check | SP 1 | Self | Herald or Wis–Int | 1.5 |

## 4. Warlord ideas (4th Edition; generic, my own labels)

The warlord's core idea is **acting through allies**: granting attacks, movement, healing and accuracy, rather than acting alone.

| Part | Trigger | Cost | Target | Home | Pts |
|---|---|---|---|---|---|
| **Order an attack**: an ally makes a weapon attack with its Reaction | A or BA | SP 1–2 | Ally | Herald | 3–4 |
| **Order a move**: one or more allies move without provoking Opportunity Attacks | BA | SP 1 | Allies | Herald | 3 |
| **Rallying word**: an ally spends a Hit Point Die and heals | BA | SP 1, or limited uses | Ally | Herald | 4 |
| **Battle plan**: allies add a bonus to Initiative | Passive | — | Allies | Herald | 3 |
| **Mark the target**: allies' attacks on one foe gain a bonus until your next turn | Hit | SP 1 | Allies | Herald | 3 |
| **Hammer and anvil**: on your hit, an adjacent ally deals damage | Hit | SP 1 | Ally | Herald or Fighter | 3 |
| **Hold the line**: allies near you gain a bonus to AC or saves | BA | SP 1–2 | Allies, Area | Herald or Str–Con | 3 |
| **Second chance**: an ally rerolls a failed attack or save | R | SP 1 | Ally | Herald | 3 |
| **Seize the moment**: when an ally spends a big resource, it gains a rider | Passive | — | Ally | Herald | 2 |
| **Grant an action**: an ally takes an extra action | A | SP high | Ally | Herald (capstone) | 8 |

**Trait clash to steer around:** the Commander (*Follow Me*), the Mentor (*Teachable Moment*), the Steward (*Ready Assistance*) and the Generous (*After You*) already give allies Advantage, Help and Reactions. So **second chance** and **directed strike** sit closest to existing traits.

## 5. The bard (SRD)

**Features:**

| Part | Trigger | Cost | Target | Home | Pts | Note |
|---|---|---|---|---|---|---|
| *Bardic Inspiration*: an ally gains a die to add to a failed d20 Test | BA | SP 1 | Ally | Herald | 8 at entry | Troy: Herald inspiration is spent from SP (2026-11-07) |
| *Cutting Words*: subtract the die from a foe's damage roll, check or attack | R | SP 1 | Enemy | Herald or Hex | 6 | |
| *Countercharm*: allies reroll against Charmed or Frightened | R | SP 1 | Allies | Herald | 2 | Overlaps the Commander's *Follow Me* |
| *Font* and *Superior Inspiration*: recovery | Short Rest, Initiative | — | Self | Herald | 3–4 | A recovery node, like *Uncanny Metabolism* |
| *Jack of All Trades*, *Expertise* | Passive | — | Self | Herald or Cha–Dex | 4–5 | Learned skills, not techniques |

**Spells that could become techniques.** These are bard spells with a command-and-control effect that could work without magic. The SP cost equals the spell's mana price. **Ref** means the spell reflavours cleanly as a technique; *magic* means it stays a spell.

| Level (SP) | Ref: command, rally, mockery, curse | Stays *magic* |
|---|---|---|
| Cantrip (at-will) | *Vicious Mockery* (an insult: psychic damage and Disadvantage), *Message* (battlefield signals), *True Strike* | Dancing Lights, Light, Mage Hand, Mending, Minor Illusion, Prestidigitation, Starry Wisp |
| 1 (SP 2) | *Command*, *Heroism*, *Healing Word* (as a rallying word), *Bane* (as demoralize, or Hex), *Hideous Laughter* (as mockery), *Dissonant Whispers* (as dread), *Longstrider* (a forced-march order), *Charm Person* (as persuasion) | Animal Friendship, Color Spray, Comprehend Languages, Cure Wounds, Detect Magic, Disguise Self, Faerie Fire, Feather Fall, Identify, Illusory Script, Silent Image, Sleep, Speak with Animals, Thunderwave, Unseen Servant |
| 2 (SP 3) | *Aid* (a rallying speech), *Calm Emotions*, *Enhance Ability* (coaching), *Enthrall* (oratory), *Suggestion* | Animal Messenger, Blindness/Deafness, Detect Thoughts, Enlarge/Reduce, Heat Metal, Hold Person, Invisibility, Knock, Lesser Restoration, Locate Animals or Plants, Locate Object, Magic Mouth, Mirror Image, See Invisibility, Shatter, Silence, Zone of Truth |
| 3 (SP 5) | *Fear* (a terrifying war cry), *Mass Healing Word* (a mass rally), *Bestow Curse* (Hex) | Clairvoyance, Dispel Magic, Glyph of Warding, Hypnotic Pattern, Major Image, Nondetection, Plant Growth, Sending, Slow, Speak with Dead, Speak with Plants, Stinking Cloud, Tiny Hut, Tongues |
| 4 (SP 6) | *Compulsion* (forced movement by command), *Confusion* (Hex) | Charm Monster, Dimension Door, Freedom of Movement, Greater Invisibility, Hallucinatory Terrain, Locate Creature, Phantasmal Killer, Polymorph |
| 5 (SP 7) | *Dominate Person* (Hex) | Animate Objects, Awaken, Dream, Geas, Greater Restoration, Hold Monster, Legend Lore, Mass Cure Wounds, Mislead, Modify Memory, Planar Binding, Raise Dead, Scrying, Seeming, Telepathic Bond, Teleportation Circle |
| 6 (SP 9) | *Heroes' Feast* (a victory feast), *Mass Suggestion*, *Irresistible Dance* (Hex) | Eyebite, Find the Path, Guards and Wards, Programmed Illusion, True Seeing |
| 7 (SP 10) | — | Arcane Sword, Etherealness, Forcecage, Magnificent Mansion, Mirage Arcane, Prismatic Spray, Project Image, Regenerate, Resurrection, Symbol, Teleport |
| 8 (SP 11) | *Power Word Stun* (a word of command) | Antipathy/Sympathy, Befuddlement, Dominate Monster, Glibness, Mind Blank |
| 9 (SP 13) | *Power Word Heal*, *Power Word Kill*: **Herald capstones** | Foresight, Prismatic Wall, True Polymorph |

**Notes:**
- *Planar Binding* depends on scrapped planes (`canon/audit-planes.md`).
- Spells with *Charm* or *Dominate* belong to the hexer, and the Unbound's *Free Will* resists them.
- The bard's own SRD capstone, *Words of Creation*, is Power Word Heal and Kill, which fits a Herald capstone neatly.

## 6. Distribution by fantasy

| Home | What lands there |
|---|---|
| **Herald (command)** | Inspiration; directed strike; order a move; rallying word; rally; battle plan; mark the target; hold the line; second chance; grant an action (capstone); *Command*, *Heroism*, *Aid*, *Fear*, *Mass Healing Word*, *Compulsion*, *Mass Suggestion*, the Power Words |
| **Herald (hexer)** | *Cutting Words*; *Vicious Mockery*; *Bane*, *Hideous Laughter*, *Dissonant Whispers*, *Bestow Curse*, *Confusion*, *Dominate Person*, *Irresistible Dance* |
| **Cha–Dex** (swashbuckler, rogue) | Riposte; feint; distract; disarm; ambush; shadow step |
| **Scout** (movement) | The free Dash and Disengage (on ring 3); *Step of the Wind*; evasive footwork; bait and switch; *Slow Fall* |
| **Dex–Str** (styles, manoeuvres) | Precision; trip; disarm; lunge; parry |
| **Fighter** (hit hard) | Push; sweep; trip; menace; hammer and anvil |
| **Str–Con** (armour) | Goad; parry; hold the line |
| **Tank** (hit points) | *Superior Defense*; perhaps goad. *(Little here, because the Tank's pool is hit points.)* |
| **Con–Wis** (monk) | Bonus Unarmed Strike; *Flurry*; *Patient Defense*; *Deflect*; *Stunning Strike*; *Open Hand*; *Wholeness*; *Quivering Palm*; *Uncanny Metabolism*; Mercy; Elements |

## 7. Observations and questions

1. **The Herald is the richest home**, which answers the balance gap: its kit can start with strong techniques. For example, inspiration plus directed strike as at-will or SP picks, worth about 8–11 points, which would lift it from about 12 toward the others.
2. **The Tank has almost nothing**, but that's by design: hit points are its pool. Its techniques could **spend hit points** the way blood magic does, which would make it a third kind of pool.
3. **The technique die.** One shared die for manoeuvres, inspiration and monk strikes? It would grow through nodes.
4. **Bonus Actions crowd.** *Flurry*, inspiration, directed strike, Dash and Disengage all compete for the Bonus Action. That's a natural limit on stacking, and worth keeping.
5. **Saves against techniques** need a DC. The monk uses 8 + Wisdom + PB. The proposal: **8 + the tree's ability + PB**, matching the spellcasting rule.
