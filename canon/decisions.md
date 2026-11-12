# Decision Log

Newest first. One line per decision: what was decided, and why if a reason was given. Add to this log every time the author settles something, and update `canon/setting-bible.md` to match.

## 2026-11-11

- **Species wheel Hit Dice** (Troy, voice): none on ring 1; one die per colour on rings 2–6, the same along the spoke; large dice allowed (buying hit points here costs grid progress).
- **Species wheel rings and progress points** (Troy): the base form is ring 1, advancement rings 2–6 (45 arcs). One progress point per level-up, spent on this wheel or the skills grid; six deep in either gives about the same power. Prof. Up on every ring-3 arc, Attack Up on every ring-6 arc.
- **Species advancement wheel** (Troy): the root is the existing species description and colour-wheel form; linear cost per ring for now, six rings deep (54 arcs); choices per ring, Unphased points and accumulation left open. No breath weapons (reaffirmed). Diagram: `art/cartoon/species_advancement.py`.
- **Full class rebuild** (Troy): classes are replaced by the progression trees and the skills grid. `canon/brainstorm-progression.md` moves from EXPLORING to ADOPTED direction. Troy: "Progression on wheels is a fun theme for a ring-shaped world."
- **Ring 2 names** (Troy, voice): kit lines Herald II, Scout II, Fighter II, Tank II, Mystic II, Mage II; seams 202 Cunning, 204 Precision, 206 Might, 208 Vitality, 210 Lore, 212 Control, continuing as II on the ring-4 seams and III on the ring-6 seams.
- **Tile names** (Troy, voice): the top line becomes a short look-up name (kits keep their prerequisite). Ring 3: 301 Warlord, 302 Tactician, 303 Rogue, 304 Ranger, 305 Skirmisher, 306 Virtuoso, 307 Champion, 308 Brute, 309 Bulwark, 310 Juggernaut, 311 Blood Mage, 312 Shaman, 313 Oracle, 314 Sage, 315 Alchemist, 316 Wizard, 317 Summoner, 318 Hexer. Each gets a "II" tile straight out on ring 6 (601–635, odd). The monk moves to the Scout and manoeuvres side.
- **Stamina, Herald–Scout–Fighter side** (Troy, voice): 4 on the Herald side of the Herald–Scout seam, the whole Scout wedge and the Scout–Fighter (Battle Master) seam (202, 203, 204 raised from 3); 2 on the Fighter wedge, 3 on 509 and 611; 1 on 206 (lowered from 2), 411, 616, 514, 617. Only the Constitution stripe has no stamina or mana: the Tank's hit points are its resource.
- **Mystic and Tank mana** (Troy, voice): 4 mana on every Mystic-wedge tile (209 raised from 3) and on 419, 628; 2 mana on 415, 622, 518, 621; 1 mana on 311, 414, 517, 620. Mystic powers beyond mana (Wild Shape-like) to come; check the overlap with the Green form then.
- **Mana and stamina, Mage and Herald sides** (Troy, voice): 5 mana on every Mage-wedge tile (the reference curve; the Mage is the strongest mana user); the summoner seam mixes (212, 423, 634: 2 mana 2 stamina; 528, 633: 4 mana 1 stamina; 529, 635: 1 mana 3 stamina); 4 stamina on 201 (was 3), 301, 401, 501, 601, 318, 424, 530, 636.
- **Tile labels renamed** (Troy, voice): *Damage Boost* tiles now read **Attack Up**, and *Proficiency* tiles **Prof. Up** ("Proficiency Up" didn't fit), with the "+1" and "PB +1" dropped, because "❤️d10 +1" read as a d10 plus one. Attack Up covers both an extra attack and a bigger cantrip. Older notes still say Damage Boost; same thing.
- **Scout Kit techniques** (Troy, voice): the kit teaches **I'm Going First!** (on Initiative, 1 stamina for +5, 2 for +10) and **Sidestep** (Reaction when hit or making a Dexterity save, light or no armour: 1/2/3 stamina for 1d4/1d8/1d12 to AC or Dexterity saves until the start of your next turn). Like Shield, it's used once the roll is known (when hit, or on a failed Dexterity save) and counts against the triggering roll. Kit techniques must suit every kind of Scout. Precise Strike rejected.
- **Greater Sidestep on ring 4** (Troy): adds 4 stamina for 2d8 and 5 stamina for 2d10; tile to be chosen. **Evasion** (SRD) saved for a deeper ring.
- **Hit Dice, Herald–Scout side** (Troy, voice): d6 on 302, 402, 502, 503, 504, 602, 603, 605; d8 on 303, 305, 404, 406, 505, 507, 508, 509, 606, 608, 609, 611. Drawn on the skills grid.
- **Hit Dice, Fighter side** (Troy, voice): d10 on 306, 308, 408, 410, 510, 512, 513, 514, 612, 614, 615, 617.
- **Hit Dice, Tank, Mystic and Mage sides** (Troy, voice): d12 on 309, 311, 412, 414, 515, 517, 618, 620; d10 on 518, 519, 621, 623; d8 on 312, 314, 416, 418, 520, 522, 624, 626; d6 on 523, 524, 528, 529, 627, 629, 633, 635; d4 on 315, 317, 420, 422, 525, 527, 630, 632. d6 on the last four (318, 424, 530, 636): every tile now has a Hit Die.
- **Skills grid print version** (Troy asked): `skills_grid.py --print` writes a letter-size PDF.

## 2026-11-10

- **Scout technique placements** (Troy, voice): Duellist dropped (the Dueling style covers it); free Dash or Disengage and Deflect Attacks on 304; Take Aim (Steady Aim-style, free with a 1-stamina add-on) on ring 3, tile to be chosen; Uncanny Dodge on ring 5, manoeuvres side, tile to be chosen. The Scout Kit's own techniques are still open.
- **Fighting styles kept** (Troy, voice): not feats, just fighting styles, using the six 2014 SRD styles verbatim (an explicit exception to the no-2014-rules rule), with a source note; more may be added later. Kits: Scout picks Archery, Dueling or Two-Weapon Fighting; Fighter any; Tank Defense or Protection; Herald none. More along the manoeuvres seam. Stamina upgrades for styles parked. File: `srd/05-fighting-styles/fighting-styles.md`.
- **Tank Kit gains Weapon Mastery with 1 weapon** (Troy).
- **Scout directions** (Troy): archery and mobility in the middle (ranger); roguish deception and Sneak Attack on the Charisma seam; manoeuvres on the Strength seam; mostly self-buffing. "Duellist" proposed as a kit technique name.
- **Hit Dice propagated along the 12 rays** (Troy): kit rays (straight hex lines, rings 3–6) and seam rays (exact hexes on rings 4 and 6) take their ring-2 tile's Hit Die. Odd-ring seam hexes left open.
- **Fighter Damage Boosts moved** (Troy): 511 removed; boosts added at 510 and 614, making extra damage core to the Fighter fantasy and adding a boost to the Scout's and Tank's cones. A boost at 307 was considered and dropped.

## 2026-11-09

- **Ring 2 pools** (Troy): 201–204 +3 stamina; 205–206 +2 stamina; 208 +2 mana; 209 +3 mana; 210 +4 mana; 211 +5 mana; 212 +2 mana and +2 stamina.
- **Stamina by branch** (Troy): the Herald branch gets about a full caster's pool (it replaces the bard); the Fighter branch less, with other bonuses; the Scout branch in between (rangers, Arcane Tricksters).
- **Ring 2 Hit Dice** (Troy): 201 d6, 202 d6, 203 d8, 204 d8, 205 d10, 206 d10, 207 d12, 208 d10, 209 d8, 210 d6, 211 d4, 212 d6.
- **No technique or spell names on tiles** (Troy): they go in each tile's text description, to keep the grid uncrowded.
- **Six more Proficiency Bonus tiles on the ring-6 corners** (Troy): 601, 607, 613, 619, 625, 631.
- **Six more Damage Boosts on the ring-6 seams** (Troy): 604, 610, 616, 622, 628, 634. A full 36-tile cone from one kit now holds three.
- **The techniques system** (Troy): for every kit and tile, you know every technique the tile teaches. The Herald Kit teaches *Rally* and the coaching set; tile 201 adds *Momentum* to the *Invigorate* family.
- **Heralds know every technique on each tile they take** (Troy): no picking, no preparation. Their choices are how to spend stamina and which way to progress; the numbers stay manageable and grow more interesting deeper in the tree.
- **Technique tiles** (Troy): *Rally* on the Herald Kit's list (11); the *Invigorate* family on tile 201; *On Me!* and *Scatter!* on tile 202.
- **Technique variety is per kit** (Troy); some techniques are unique to seams; characters start with a few and learn more through the tiles, some tiles carrying a cluster. *On Me!* and *Scatter!* go together on one ring-2 tile, to be chosen.
- **Technique variety target** (Troy): about the variety of the Battle Master's manoeuvres or the monk's abilities, not the whole bard spell list. **Campaign length assumption:** most games reach about level 10, so most characters get one Damage Boost and some two.
- **Again! renamed Momentum** (Troy).
- **Skills grid: outward moves only** (Troy): no lateral moves. Each kit opens a cone that holds only its own Damage Boost, so extra boosts need extra kits.
- **Mark the Target reworked** (Troy) into a sustained mark, working name *Again!*: an action attack; on a hit, 1 stamina marks the foe so the next damaging hit gains 1d12; on each hit you may pay another stamina (free, no action) to keep it, with no time limit; no Damage Boost scaling.
- **Rally picks up downed allies** (Troy). **Mark the Target** drafted (action, an attack; on a hit, 1 stamina marks the foe with 1 + Damage Boosts charges, each ally hit using one for +1d6), to be re-evaluated.
- **Three more Herald techniques** (Troy, voice): *Greater Invigorate* (action + 2 stamina: an ally takes an action right away, without using its Reaction), *Reinvigorate* (Reaction + 1 stamina: an ally regains its Reaction, usable only after another creature moves or takes its turn) and *Rally* (Bonus Action, 1 stamina per ally: each spends a Hit Point Die and heals). The bigger-die add-on on *There's an Opening!* stays at 1 stamina. That makes nine Herald techniques.
- **Four more Herald techniques** (Troy, voice): the coaching set, *You've Got This!* (checks), *There's an Opening!* (attacks) and *Heads Up!* (saves): free Bonus Action d4 on an ally's next roll, with 1-stamina add-ons for a Reaction, everyone, or a d6. And *Invigorate*: Bonus Action plus 1 stamina, an ally takes a Bonus Action right away, with no spell restriction. Details: `canon/techniques.md`.
- **Action-economy brokering** (Troy): the Herald can move action economy between characters, always at a real cost.

## 2026-11-07

- **Tile numbers** (Troy): each skills-grid tile has a unique number, ring first: kits 11–16, then 201–212 up to 601–636; shown in grey behind each tile.
- **Six Proficiency Bonus +1 tiles on ring 4** (Troy), on the seams between kits.
- **Six Damage Boost tiles on ring 5** (Troy), straight out from each kit, on its main line.
- **Techniques** (Troy, voice): the umbrella term for martial abilities; each may have a free use (the stamina side's cantrips), stamina add-ons, or both. Kits give techniques picked from a kit list (Herald 3, Scout 2, Fighter 1). Stat blocks like spells: timing, range, targets, free effect, then add-ons; add-ons stack with no overall cap, each bought once unless stated. Reactions in techniques work "at any time". Details: `canon/techniques.md`.
- **First techniques** (Troy): *On Me!* and *Scatter!* (Bonus Action, one ally moves 5 ft towards or away from you for free; 1 stamina each for Reaction, everyone, or 10 ft).
- **Herald gets Weapon Mastery with 1 weapon** (Troy), so techniques never copy mastery riders.
- **Generic tiles** (Troy): Proficiency Bonus and **Damage Boost** tiles are scattered across the grid. A Damage Boost is an extra attack with the Attack action, or an extra cantrip damage die.
- **True Strike dropped** (Troy): doesn't fit the theme in its 2024 form.
- **Simple weapons leave the printed centre tile** (Troy): they don't fit the counting theme. They're still granted, in the description; the tile shows only PB +2.
- **Tile symbols** (Troy): ❤️ Hit Die (hit points), ⭐ stamina (SP), 📜 mana (MP), to keep line 3 compact. For example, the Scout Kit reads "❤️d8 ⭐4 +5ft".
- **Mana is worth 2 points per point, stamina 1** (Troy, voice). The Herald gets no mana or cantrips; its kit waits until stamina techniques are designed, as one system unifying the monk, manoeuvres, bardic inspiration and the warlord. Parts: `canon/parts-bin-techniques.md`.
- **Kit contents, ring 1** (Troy, voice): every hex is worth about the same; a starting kit is a whole level 1, and a later kit about one hex (for now a second kit gives everything). Two separate pools: **stamina (SP)** for martial techniques at 1 SP each, and **mana (MP)** for spells at the 2014 spell points prices for now (2, 3, 5, 6, 7, 9, 10, 11, 13). Long Rest restores all; a Short Rest restores PB in each pool (rules text, not tiles). Free martial features are **at-wills**. Kits: Herald d6 SP4, 3 at-wills, light armour (command and control, not a caster); Scout d8 SP4 +5 ft, 2 at-wills, light armour, Finesse/Light/ranged martial weapons, 2 masteries; Fighter d10 SP2, 1 at-will, light and medium armour, Shields, martial weapons, 3 masteries; Tank d12, hit points as its pool, light and medium armour, Shields, martial weapons, Second Wind; Mystic d8 MP4, 2 cantrips, light armour; Mage d4 MP5, 3 cantrips, rituals.
- **Spells** (Troy): the Mystic learns spells from its nodes; the Mage prepares any spell it finds (library, scroll); both prepare twice their PB. Spellcasting uses the tree's ability. Seam tiles don't teach spells, except seam-only kinds: blood magic (Con–Wis, paid in hit points, ability set per spell) and summoning (Int–Cha, mana to summon, stamina to control). Manoeuvres sit on the Dex–Str seam.
- **Herald Kit Hit Die is d6** (Troy), changed from d8, for a smooth gradient around the wheel.
- **Mystic Kit Hit Die is d8** (Troy): briefly changed to d6, then back to d8 so the Hit Dice step smoothly round the wheel (Mage d4, Herald d6, Scout d8, Fighter d10, Tank d12, Mystic d8).
- **Ring 1, part 2** (Troy, voice): the Mage Kit's Hit Die is d4; line 3 of a tile lists only what adds up across the grid; saving throws move to the form tree (the Unphased get their own at the wheel's centre); ring 1 gives no skills, and the traits keep theirs for now; the centre tile is PB +2 and Simple weapons; starting equipment goes to a character creation section.
- **Fantasy map for ring 1 and its seams** (Troy): Herald (bard, warlord, hexer without a pact), Cha–Dex (swashbuckler, rogue, assassin), Scout (pure movement), Dex–Str (fighting styles), Fighter (hit hard), Str–Con (armour, slow), Tank (hit points), Con–Wis (monks, blood magic), Mystic (shaman, oracle, seer; the cleric is dropped), Wis–Int (sage, alchemist), Mage (wizard), Int–Cha (summoner by force of will). The druid moves to the Green form; the artificer to the Yellow form, combining with the Mage.
- **Ring 1 of the skills grid** (Troy, voice): printable three-line tiles (Req; name; Hit Die and boosts); the centre tile holds what's common to all entries, so far PB +2; names avoid D&D class names except Fighter. Herald Kit (Cha, d8), Scout Kit (Dex, d8, for now), Fighter Kit (Str, d10), Tank Kit (Con, d12), Mystic Kit (Wis, d8), Mage Kit (Int, Hit Die open). Details in `canon/brainstorm-progression.md`.
- **The hex grid is now the "skills grid"** (Troy). Its centre tile is empty, with the six ability hexes around it; ring 1 is populated first.

## 2026-11-06

- **Personality tree is shallow and converging** (Troy): at most four levels deep, counting the root traits; nodes are like mini feats; 24 → 16 → 12 → 8, with 8 final traits and 60 nodes in all. A phased character can hold at most 8 (an Unphased one 12). Assumes phasing is relatively common.
- **Three trees, not two** (Troy, voice): **form** (colour and dragonborn progression; on a phase the points come back to reinvest in the new form, gameable on purpose), **personality** (keep one of two traits on a phase; nodes built on the lost trait are lost, nodes on the kept trait stay; the real phasing penalty) and **learned skills** (kept). Details and conflicts with 2026-11-05: `canon/brainstorm-progression.md` §1a.
- **Learned-skills tree is a hex grid** (Troy): start in the centre, one hex per ability around it, ring order Charisma, Dexterity, Strength, Constitution, Wisdom, Intelligence (Claude's proposal, accepted as "fine"). Ring 1 is the class-like entry kit with multiclass limits. Six rings, 127 hexes.
- **Form tree is the colour wheel** (Troy): Unphased in the centre, who can't develop on it until they phase; starting Unphased gives three traits, dropping to two on the first phase. Nine colour spokes; neighbours don't matter; rings alternate choices and fixed steps; deeper rings cost more, perhaps on a Fibonacci scale.
- **Points per advance: parked** (Troy) until the tree depths are known.

## 2026-11-05

- **A new character starts with one entry node plus their origin** (Troy), at least on the experience side. The phasing side (33 roots: 24 traits and 9 forms) needs polish.
- **No class presets** (Troy): more design space, and room for tropes beyond the 12 classes (shaman, warden, warlock, summoner). Schools and domains may become branches. Adjacent branches can share cross-branch nodes that need prerequisites from both, such as fire arrows from an elemental branch and an archer branch.
- **Spell lists are curated per casting branch** (Troy), with ways to short-circuit them, like the bard's Magical Secrets.
- **A mana pool instead of spell slots** (Troy, direction): mana is gained through different branches. Basis: the SRD sorcerer's Creating Spell Slots costs (the 2014 DMG's spell points variant isn't in the SRD, so it can't be used).
- **Spellcasting can sit in any tree** (Troy), using that tree's ability. Learned magic (wizard-like) goes on the experience tree and natural magic on the phasing tree, and one character can have both. Some magic may sit outside the trees: a warlock's pact is more like faction membership. **No warlock equivalent on either tree for now**, to avoid untangling Pact Magic from the lore.
- **Tree design principles** (Troy): every entry point has at least two initial branches; branches can recombine; milestones sit at similar depths on every branch; going depth first should track the 2024 single-class power curve, while branching plays like multiclassing (slower, with combination abilities). The Constitution tree is a branching mix. Very old characters can pursue depth on many paths or great breadth.
- **Entering a second ability tree** (Troy): allowed, with a reduced starter kit, as in the SRD's multiclassing rules.
- **Scaling becomes nodes** (Troy): cantrip upgrades and multiple attacks are acquired in the trees, not by level. Encounter building is to be checked against something like the party's average total nodes.
- **Levelling up is only nodes** (Troy): gaining a level means one node from each tree and nothing else. Hit points and Proficiency Bonus come only from nodes. The class level-up tables are gone, and "level" may be dropped except as shorthand for gaining a node from each tree.
- **Hit Dice and Proficiency Bonus boosts are scattered through the trees** (Troy): the Constitution tree has the biggest Hit Dice (d12s), Strength perhaps d10s, Intelligence perhaps d4s; +1 Proficiency Bonus boosts are scattered too, so boosts must be pursued by choice.
- **Two counters, tentatively** (Troy): the experience tree's node count is the character's level; a separate phasing level resets to zero on a phase, and each level earned afterwards gives one node on each tree, so a character can pass 20 experience nodes. Chosen to have something to run with; to be contemplated further.
- **Shallow and deep** (Troy): the phasing tree is powerful but shallow, and losing it on a phase is the true phasing penalty. The experience tree is deep and kept. After phasing you can keep pursuing a learned path or start a new one, so a long-lived character could end up deep in many parts of the experience tree, like extreme multiclassing beyond level 20.
- **One node from each tree per level** (Troy), in the two-tree progression, because it makes balance easier. Next: break the SRD and PHB classes into parts and score every part (classes and feats) on the Character Origins point scale: `canon/parts-bin.md`.
- **Exploring a classless progression** (Troy): option D, two trees (experience, kept on phasing; phasing, reset on phasing), six ability entry nodes with a threshold such as 13. Not decided; classes are not yet dropped. Working file: `canon/brainstorm-progression.md`.
- **Extended-trait capstones come at level 19** (Troy): a character who took all five tiers of one path reaches the capstone with the Epic Boon pick. Most won't; the capstone should be epic to reward the options set aside.
- **Extended traits form a tech tree** (Troy): paths about five tiers deep, anchored to one of the 24 base traits or 9 forms; branching and converging; losing an anchor by phasing means repicking, perhaps one per day while recovering; capstones are rare; form paths can grant dragon traits, like *Savage Species* monster classes, in parallel to class advancement. Details in `canon/brainstorm-extended-traits.md` §3a.
- **Name: Extended Traits** (Troy), "for now", for the traits that replace feats.
- **Feats are scrapped entirely** (Troy). At the levels where feats normally come, characters gain replacement sets, working name "extended traits". The feats are broken down into a toolbox of parts, then reimplemented: SRD feats in SRD wording, PHB feats in generic wording, all reworded when the extended traits are designed. Working file: `canon/brainstorm-extended-traits.md`. This supersedes the feat-by-feat fixes in `canon/proposed-feat-changes.md`.
- **Classes on hold** (Troy): players will probably start with the default classes in the *Player's Handbook*, reflavouring any that don't fit. Nothing gets fixed yet; `canon/brainstorm-classes.md` stays as a reference.
- **Assume players own the *Player's Handbook*** (Troy): the SRD's feat list is short, so reviews must cover the book's feats too, not just the SRD's.
- **Feats: fix only clashes with the personality traits** (Troy), for example no taking Alert at level 4. Running list: `canon/proposed-feat-changes.md`.

## 2026-11-04

- **Indigo: *Masquerade* replaces *Black Pearls*** (Troy). At will, as a Bonus Action, an Indigo can take on the illusory look of a dragonborn of any colour, with none of its traits; touch or an Investigation check sees through it. About 3.5 points, bringing Indigo to about 18.5. It's unique on the wheel, and suits the infiltrator ("the Cylon in the ballroom") without forcing Indigo into a faction.
  - Troy considered and set aside a real partial shape-change (it needs too many exceptions, such as White's flight).
- **The black pearls leave the Indigo form** (Troy). Membership of the Undertow emerges from society and play, through the faction rules, rather than coming with the form.
- **Colour wheel wording** (Troy): the paragraph on blends and mixing is replaced with new text, and the "Colours" column and the "(Red + Green)" style brackets after the Brown, Yellow, Indigo and Grey headings are removed from Character Origins.
- **Phasing penalty, tentative** (Troy): phase shock (−4 to D20 Tests, easing by 1 per Long Rest); keep at least one trait; the new form set by circumstance, the DM or a roll; catatonia during the change; a first settling is not a phase. The triggers stay open.
- **The Unphased stay as they are** (Troy). It's a playstyle choice: a player either has fun swapping traits or gets bored and settles into a form.
- **"Epoch 7" removed** (Troy) from the notes. The present is epoch 6.
- **No blends anywhere** (Troy): all blend and mixing wording removed from Character Origins' opening, the setting bible, the plan, the colour-wheel art (new labels: earth, the sun's reflection, the deep, the moon's reflection) and the "Azhi: A Quick Tour" doc. The four are now "the younger colours".
- **Giant Eagle, Elk and Owl** (Troy): they become Beasts, and nothing else in their stat blocks changes, including the Giant Owl's spells. (Monster change B1; knock-ons a–e rejected.)
- **Magic in epoch 2** (Troy): no dragon taught magic until Red and Blue switched sides in the machine war, and the dragons taught up to level 9 (first set at level 5, then raised the same evening so that every spell of levels 1–9 can have a teaching dragon). Still PROPOSED lore, in `canon/brainstorm-epochs.md`, with the other answers from the drive.

## 2026-11-01

- **Spell origins pass their test** (Troy): giving each spell the dragon that taught it, or the later epoch that discovered it, works as an idea and continues. The assignments themselves stay tentative, in `canon/brainstorm-spell-origins.md`. The lore that came out of the test (necrotic, undead, shape-changing and divine magic dating from epoch 3; the dragonborn ending the homunculi war with *Wish*) is PROPOSED, in `canon/brainstorm-epochs.md`.
- **Blue is "the trader"** (Troy), for the spell notes.
- **The Outer Planes are scrapped** (Troy), with all fiends and celestials. The Giant Eagle, Elk and Owl become Beasts.
- **Planes kept for now:** the Astral, the Ethereal and the four Elemental Planes. The **Feywild is scrapped**, and all Fey go from the monster list. Some may return later as incursions from beyond.
  - Proposed monster changes are tracked in `canon/proposed-monster-changes.md`.
- **Proposed spell changes** (Troy): keep a running list of spell changes with reasons, as for the monsters, to apply in one pass later: `canon/proposed-spell-changes.md`.
- **"Peoples" rule reworded** (Troy):
  - "Dragonborn of seven colours" becomes **"dragonborn of several colours"**. The old list of seven left out the Unphased, Yellow, Grey, Brown and Indigo, and the instructions need room for rare Crimson, Gold and Silver, with perhaps other exceptions.
  - The rule is now about **peoples**: species with societies, or playable ones. **Other sentient beings exist**: the dragons, the thinking machines, things from beyond, intelligent monsters. Troy noted that the thinking machines had already broken the old wording.
- **Other species in in-world fiction** (Troy): the dragonborn-only rule now allows other sentient species in **stories told on Azhi**, which everyone there considers fantasy. "On Azhi, writers will also have imaginations." Updated in the primer, the project instructions, the setting bible and design check 4.
- **Thinning boundaries and cosmic horror** (Troy): too much magic or computation thins reality, and things can break through from outside. This is a concept borrowed from Stross's *Laundry Files*; see `canon/brainstorm-epochs.md`.

## 2026-10-31

- **Gender** (Troy, voice): the dragons are genderless. Most dragonborn show little sexual dimorphism; players choose their character's look and pronouns. Added as a sidebar in Character Origins.
- **Dragonborn lay eggs** (Troy). Phasing can change a dragonborn's sex as well as their colour (to be developed in the phasing brainstorm).
- **Real-world wildlife** (Troy): mammals, insects and the rest of the ecosystem are as on Earth, so the text can name kittens and oxen without new words.
- **Undead dropped from the Grey homunculus site** (Troy): undead may not fit a world of easy rebirth. Whether undead exist at all is for the monster review.
- **Epoch sites as campaigns** (Troy): the great sites from past epochs, such as *The Last Machine*, are likely to become ready-to-play campaign settings of their own. The world book only hints at them.

## 2026-10-30

- **Languages are geographic** (Troy): languages are tied to a character's region of origin, not to personality traits or colour, since a dragonborn can phase into any form anywhere and keeps the languages they know. A sidebar in Character Origins says so; the languages themselves go in a "Geography of Azhi" section, still to be written.
- **Creature type as a sidebar** (Troy): dragonborn count as Humanoid for the rules, so other source material works. A sidebar notes the irony of the word in a world with no humans.
- **Languages deferred** (Troy): to be worked out later; they're probably tied to geography rather than species. A to-do item is in `PLAN.md`.
- **Life span removed** (Troy) from Character Origins. It returns with the phasing rules. Since Azhi died and was reborn as a world, the game may drop the concept of mortality altogether, after a fashion; that needs its own brainstorm.
- **"Creature Type: Humanoid" removed** (Troy) from every form, along with the "Creature Type" part of a form.
- **Darkvision ranges** (Troy): Black has 120 feet, since they live underground, like the SRD dwarf and orc. Indigo keeps 60 feet.
- **The Unphased** (Troy): no damage resistance. Size is Small or Medium, the player's choice; mechanically the two are nearly identical. The blends are all Medium.
- **Form rituals need no Material components** (Troy): Black's *Comprehend Languages* and *Identify*, and Grey's *Augury*, *Detect Magic* and *Find Traps*, are cast without them. This also avoids a clash between *Identify*'s pearl and the Undertow's black pearls.
- **No Origin feats** (Troy): personality traits replace both backgrounds and Origin feats. A sidebar in Character Origins says so.
- **Gold and Silver forms: backburnered** (Troy). They will be built as colours eventually, but hidden in the DM material rather than the players' Character Origins chapter, as the 2014 DMG hid the aasimar.
- **Factions** (Troy): factions are the rules of a civilization.
  - Some are city or nation-state factions with no dragon affiliation; others serve or oppose particular dragons.
  - Rules for standing, debts and expulsion belong to the faction's description, not to a form.
  - A member in good standing enjoys the faction's benefits; one out of favour is an outcast, and possibly hunted.
  - New working file: `canon/factions.md`.
- **The Undertow is a faction name** (Troy), Indigo's society, no longer the name of a form trait.
  - Indigo's trait is now *Black Pearls*: "Unless you've recently phased into Indigo, you start with two black pearls, the tokens of debt traded by the Undertow. If you've recently phased into Indigo, you will be approached shortly with an opportunity."
  - The old trait's favour, debt and cast-out rules moved word for word to the faction file, to be reworked there.
- **Personality trait benefits are canon** (Troy): the trait-benefits brainstorm is approved. The 24 benefits in `srd/04-character-origins/01-personality-traits.md` become official, including the balance-pass changes and the feature names that had been placeholders (such as *Quick to Act* and *Long Stride*).
- **+3 to one ability is allowed** (Troy): two traits plus a form may all raise the same ability.
- **No breath weapons** (Troy): no form, and no dragonborn, has a breath weapon. The SRD Breath Weapon is retired.
- **Balance pass, part 2** (Troy, voice):
  - Green's tail can hold a weapon or Shield but can't attack with a weapon or gain a Shield's benefit.
  - Red has Expertise with one of its two tools.
  - Brown's Tremorsense is now its own feature, split from *Rooted*.
  - White's *Flight* is renamed *Spectral Wings*: summoned, not permanent.
  - Everything else reviewed was approved as is (§17 of the trait-benefits brainstorm).
- **Balance pass, part 1** (Troy, voice): Reaction crowding, the Help engine, stacked rolls and Initiative stacking were all reviewed and approved as is. Overlap checks are recorded in `canon/brainstorm-trait-benefits.md` §16.

## 2026-10-29

- **Starting equipment approved** (Troy): with no backgrounds, a character starts with **50 GP** to spend on equipment, plus their class's equipment.
- **The Theorist's description** (Troy, written): "take it apart and put it back together a little better" is cut, and the last line becomes "You've read about almost everything and done almost none of it, which has never once stopped you from having a plan." This fits the book-smart, harebrained Theorist of the reworked benefits.
- **The Scrapper's description** (Troy, voice): "a dare on a cliff edge" becomes **"a spilled drink"**, so the trait stays about brawling and leaves daring to the Bold.
- **Design directions Troy is considering** (not decided):
  - **Traits instead of feats:** drop feats, and have characters gain personality traits at levels 4, 8 and so on. Later, more advanced traits would take the role of feats, and generic feats such as War Caster might go away.
  - **A Warlord class:** possibly designing one. Battlefield-control ideas such as swapping two allies' places are held back for it rather than given to traits.

## 2026-10-26

- **Approach to trait benefits** (Troy):
  - **Strength:** not as strong as a feat, but nearly (about 6 points, or about 7 for ★; an Origin feat is 8).
  - **SRD parts:** borrow directly from the SRD species, all now replaced by the wheel, and from the SRD feats and backgrounds: "the SRD phasing".
  - **Third-party sources:** borrow only concepts, never wording.
  - **Aim:** placeholder content first, refined later.
  - Working record: `canon/brainstorm-trait-benefits.md`.

## 2026-10-25

- **Three more personality traits, for 24 in all** (Troy, voice session). All three are body-led: the personality comes as a side effect of the body. Troy noted that phasing into a new body could bring such a personality along with it.
  - **The Gentle Giant:** Strength or Wisdom.
  - **The Hearty:** Constitution ★, the first pure-Constitution trait.
  - **The Scrapper:** Strength or Dexterity. Its "dare on a cliff edge" line is flagged for a trim, since that's the Bold's territory.
- **Rejected:** the Labourer, which overlapped the Disciplined and the Wanderer.
- **Ability rebalance:**
  - The Wanderer is now **Constitution or Dexterity**; Strength was dropped.
  - The Prudent is now **Wisdom or Intelligence**, since its "and then what?" planning is reasoning.
  - The Confidant is now **Wisdom or Charisma**, since rapport is Charisma.
  - The Prudent and the Confidant lose their ★.
- **Ability counts are now** seven each for Strength, Dexterity, Constitution, Wisdom and Charisma, and six for Intelligence. Troy says that's fine, since mostly wizards want Intelligence. It may be rebalanced later.
- **Seven ★ traits:** the Devout, the Dreamer, the Hearty, the Restless, the Strategist, the Theorist and the Unbound.
- **The minigame** "famous characters, two builds" is kept as a build-testing tool (`canon/minigame-character-builds.md`). Its outputs are never recorded.

## 2026-10-24

- **The colour wheel is replaced** (Troy). The ten-form wheel (five colours plus Marsh, Soil, Oxblood, Slate, Glacier) gives way to **nine forms**: Red → Brown → Yellow → Green → Blue → Indigo → Black → Grey → White. Worked out in `canon/brainstorm-colour-wheel.md`; the rules text is `srd/04-character-origins/02-character-species.md`.
- **Blends mix like paint, not light**, except **Yellow**, which is Red and Green mixed like light. **Yellow and Grey** are the earthly echoes of Gold and Silver.
- **The elemental feeding and checking cycle is retired** as a design constraint. The wheel is a colour order, by rule of cool, and no longer decides which elements oppose which.
- **Power budget:** all nine forms have **similar point totals** (about 17–18.5); blends are no longer held below the colours.
- **Darkvision:** Black **and Indigo** (Troy's override of "Black alone").
- **Form changes:**
  - **Green** trades Regeneration for a **Prehensile Tail** (a third hand that can't hold a Shield, plus a 1d4 Slashing tail strike using Dexterity), and its +1 becomes **Dexterity or Constitution**.
  - **Brown** (was Soil) gains Plough and Cart.
  - **Grey** (was Slate) gains Moonsight and Heard It on the Road.
  - **Indigo** and **Yellow** are new.
  - Every form now has **two ribbons**.
- **Societies and lore** (bible §3):
  - Red miners and smiths; Yellow open-source inventors; Brown farmers; Green environmentalists.
  - Blue's cosmopolitan port cities; White's mountain monasteries; Black as zealots of a living god.
  - Indigo as a secret society with pearl debts.
  - The five knowledge colours.
  - Phasing as emigration.
- **Retired:** Regeneration, Swamp Walker, Inventive Genius, Seasoned Traveller (its parts went to Brown and Grey), and Careful Senses.
- **Personality traits replaced** (Troy, voice session). The original twelve are retired from canon and kept as source material (`canon/source-personality-traits-v1.md`). They're replaced by **twenty-one** traits, which have descriptions and ability choices but whose benefits are still to be written:
  - **From the brainstorm:** the nineteen.
  - **New:** **the Restless** (Dexterity), which brings Hyperactive forward as an epithet, and **the Disciplined** (Strength or Constitution): obsessive self-improvement, the bodybuilder or martial artist.
- **Each trait lists one or two abilities**; the character raises one of them by 1. Single-ability traits (★) get a slightly stronger benefit. Each trait is worth about 10 points, or about 11 for ★.
- **Ability changes:** the Resourceful is **Wisdom or Dexterity** (its skills lean on Wisdom); the Unbound is **Charisma** (defiance as force of personality).
- **Unphased** still swap one trait on each Long Rest, if they want to.

## 2026-10-23

- **Design review checklist** created (`canon/design-review-checklist.md`). It holds **canon items only**; brainstorm ideas join it once approved. It can be run as a preliminary analysis at any time, and as a final systems check.
- **Canonical builds** (a form plus traits for each class) are a **review check**, not something written now, because the classes may still change. Once the design is done, every class should have two or three workable builds.

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
