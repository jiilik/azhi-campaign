# Brainstorm: A Progression System Built for Phasing (Option D)

**Status: EXPLORING** (opened 2026-11-05). This file explores replacing classes with trees. Nothing is decided: classes are not yet dropped. Troy's statements are marked *(Troy)*; everything else is Claude's and PROPOSED.

**Background.** Troy asked whether phasing should let a level 12 cleric become a level 12 wizard, then whether classes should go entirely, with progression built around phasing from the outset. Claude offered four options (`canon/brainstorm-extended-traits.md` §3a). Troy chose to explore option D, "everything is trees".

## 1. Troy's design (2026-11-05)

- **Two trees.**
  - **The experience tree** is what you learn and remember. **When you phase, you keep it.**
  - **The phasing tree** is the feat-like progression: the extended traits, anchored to your form and personality traits. **When you phase, you reset on it**, but keep your experience tree.
- **Six entry nodes** on the experience tree, one for each ability. Each has an **entry threshold**, for example Dexterity 13 to start on the Dexterity tree.
- **The entry node is a starter kit.** Starting with Dexterity gives a mix of benefits like a Dexterity-focused class (a monk or ranger): an appropriate Hit Die, some proficiencies, and so on.
- **Then it branches.** The tree **doesn't have to be linear**.
- **Five nodes from the entry** is a significant boost, like a class gets at level 5: Extra Attack, level 3 spells and so on.
- **Hit Die boosts and proficiency boosts** come along the way.
- **On level-up:** choose one node from each tree, **or maybe two from any**. The combinations should make super fun builds.
- **Nature versus learning:** some features, such as the barbarian's **Rage**, feel like a personality trait that you can gain or lose by phasing. Others, such as **Sneak Attack**, are learned and remembered.

### Shallow and deep *(Troy, 2026-11-05)*

- **The phasing tree is powerful but shallow.** When you phase, you lose it: that loss is **the true phasing penalty**.
- **The experience tree is deep,** and you keep your learned abilities when you phase.
- **After a phase,** you can keep pursuing the same part of the experience tree, or start fresh on another section of it.
- **Over a long life,** a character who survives several phases could be deep in many parts of the experience tree: like being ridiculously multiclassed beyond level 20. Most campaigns don't last that long anyway.

**Claude's notes** *(PROPOSED)*:
- **Shallow means wide.** With one phasing node per level, a level 20 character holds 20 phasing nodes. A tree only about five tiers deep (the extended-traits tech tree) has to be wide enough to hold them: many strong nodes near the root.
- **"Beyond level 20" implies the levels come back.** If phasing resets the phasing tree and you then re-earn it level by level, each of those levels also brings a new experience node, so the experience tree can grow past 20 nodes. Whether phasing resets your level is the next question.

## 2. Parts the SRD already has *(Claude)*

- **The threshold of 13** is the SRD's multiclassing prerequisite: "a score of at least 13 in the primary ability of the new class". An entry node is the same rule, applied to every character.
- **Spellcasting across trees:** the SRD's **Multiclass Spellcaster table** already turns combined caster levels into spell slots. Spellcasting nodes could count as caster levels on it, full or half, so "level 3 spells five nodes in" falls out of an existing table.
- **Hit points and proficiencies when multiclassing** are already solved in the SRD: Hit Dice by level, and reduced proficiencies for a second class. A second entry node could use the same rule.
- **The phasing tree's root already exists.** A character's form and two personality traits, from Character Origins, are its tier 0. The extended traits grow from them.
- **The class features** break down into a toolbox, like the feats. Done 2026-11-05: `canon/parts-bin.md` holds every class and feat part with a points score.

## 3. Sorting class features: learned or nature *(Claude, first pass)*

Following Troy's Rage and Sneak Attack examples, each SRD class feature is either **learned** (on the experience tree, kept on phasing) or **nature** (on the phasing tree, reset on phasing).

| Learned (experience tree) | Nature (phasing tree) | Unsure |
|---|---|---|
| Extra Attack, Fighting Style, Weapon Mastery, Action Surge, Second Wind | Rage, Reckless Attack, Danger Sense | Channel Divinity and the cleric's and paladin's divine magic: is faith learned or felt? (Ties to "faith survives phasing", `canon/brainstorm-classes.md` X9.) |
| Sneak Attack, Cunning Action, Expertise, Evasion, Uncanny Dodge | Innate Sorcery, Sorcery Points, Draconic Resilience (magic in the blood) | The warlock's pact: a relationship, not a skill or a nature. A patron might drop you after you phase. |
| Wizard spellcasting, the spellbook, Arcane Recovery, Ritual Adept | Wild Shape (shape-changing, from epoch 3) | Bardic Inspiration: a learned art, or charisma? |
| Martial Arts, Focus, Unarmored Movement (a monk's discipline) | Primal Champion, the barbarian's level 20 feature | Metamagic: a technique, or innate? |
| Favored Enemy, Deft Explorer, the ranger's spells | Lay on Hands and Divine Sense, if faith is nature | Unarmored Defense: training (monk) or toughness (barbarian)? |

## 4. Questions this raises *(Claude)*

To be taken **one at a time** (Troy, 2026-11-05).

1. **Level-up:** **Settled (Troy, 2026-11-05): one node from each tree** per level, which makes balance easier.
2. **Resetting the phasing tree** *(partly answered, 2026-11-05: you lose it; see "Shallow and deep")*. **Tentative (Troy, 2026-11-05): option B, two counters**, chosen "for the sake of choosing something", to be contemplated further. The experience tree keeps its nodes, and its count is the character's overall level (Proficiency Bonus, hit points). The **phasing level** resets to zero on a phase. Each level earned afterwards gives one phasing node and one experience node, so the experience count can pass 20. *(Claude, PROPOSED:)* re-levelling could use the low XP thresholds, as a catch-up. Rejected: A (level stays; re-pick gradually; no growth past 20) and C (full reset of experience points to zero). do you lose the picks, or keep the count and re-spend it in the new form, perhaps one per Long Rest while the phase shock eases (Troy's earlier idea)?
3. **Hit points and Proficiency Bonus** *(Troy, 2026-11-05)*: **scatter Hit Dice throughout the trees.** The Constitution tree has the biggest (d12s), the Strength tree perhaps d10s, and so on; the Intelligence tree might have d4s. **Scatter +1 Proficiency Bonus boosts** through the trees too, so you have to actually pursue boosts by making choices.
   - *(Claude, PROPOSED)* Read as: a node can carry a Hit Die, which adds one die of that size to your hit points and Hit Point Dice; and a node can carry +1 to your Proficiency Bonus. **To confirm:** do hit points and Proficiency Bonus come *only* from such nodes, with nothing automatic per level?
   - *(Claude)* Knock-ons to check: the d4 is new (the SRD's smallest Hit Die is d6); monster attack bonuses, save DCs and Challenge Ratings assume a Proficiency Bonus set by level (+2 to +6), so a character who skips the boosts falls behind on every roll.
4. **A second entry node:** can you enter a second ability tree (the equivalent of multiclassing), and does its starter kit come at full or reduced strength?
5. **The Constitution tree:** no SRD class has Constitution as its primary ability, so its entry node is new design space. A tank, a survivor, or a vessel?
6. **Spellcasting ability:** do arcane spells follow Intelligence, divine and primal Wisdom, and innate Charisma, as in the classes? Where do the dragons' teachings fit (`canon/brainstorm-spell-origins.md`)?
7. **The power curve:** keep the SRD's per-level power, so monsters' Challenge Ratings and encounter building still work.
8. **Presets:** keep the 12 classes as named paths through the trees, so a Player's Handbook player can still say "I'm a wizard"?
9. **Level 1:** what does a new character have? Probably an entry node and the phasing tree's root (form and traits).
