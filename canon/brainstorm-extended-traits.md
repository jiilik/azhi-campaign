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

- **OPEN idea (Troy, 2026-11-05): drop classes entirely**, and build a new progression system with phasing in mind from the outset. Not decided; it reverses the earlier assumption that players start with the PHB's classes. Claude's evaluation (options A–D) is in the chat of 2026-11-05 and summarized here:
  - A. Keep classes; phasing doesn't change them.
  - B. Classes as *jobs*, as in *Final Fantasy XIV*: one character, a level in each job, switching between them.
  - C. Forms as classes: phasing is a class change. It conflicts with playing against type, and risks tying ability to colour.
  - D. Everything is trees: class features broken into a toolbox like the feats, with one pick per level from martial, spellcasting, form and trait trees. Phasing removes only the form-anchored picks. The 12 classes could survive as **preset paths** through the trees, so PHB players still recognize "a wizard".

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

**Moved (2026-11-05)** to `canon/parts-bin.md` §4, where every feat part now has a points score, alongside the class parts.

## 5. Observations

- **About a dozen parts are already spent** on base traits: initiative, Brawler, Steady Hands, Hardy, Shield training, Long Stride and others. Extended traits should build on those parts rather than repeat them. For example, an extended Bold could add something new to *Quick to Act*, not add the Proficiency Bonus again.
- **The weapon-type trio** (bludgeoning, piercing and slashing riders) is a natural pattern for a small family of extended traits.
- **The "-Touched" pattern** (+1 ability, then two spells castable once each per Long Rest) maps neatly onto the spell origins: a trait could be "taught by" one of the Seven. Black-Touched, Silver-Touched, Green-Touched and so on.
- **Armour training** comes as a three-step chain in the PHB (light, then medium, then heavy). Folding the whole chain into one trait would save players two picks.
- **The setting clashes** (Fey-Touched, Telepathic, Blindsight, Truesight) can be fixed while redesigning, at no extra cost.
