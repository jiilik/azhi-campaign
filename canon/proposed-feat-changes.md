# Proposed Feat Changes

**Status: PROPOSED** (opened 2026-11-05). This is a running list of feats that clash with the personality traits, each with its reason, to apply in one pass if accepted. Nothing here changes `srd/05-feats/feats.md` until Troy approves it. Everything is *(Claude)* unless marked *(Troy)*.

**Scope** *(Troy, 2026-11-05)*: fix only the feats that conflict with the personality traits. Classes are on hold.

**Sources.**
- SRD 5.2.1 feats: `srd/05-feats/feats.md` (17 feats), checked against the trait text in `srd/04-character-origins/01-personality-traits.md`.
- 2024 *Player's Handbook* feats: the names and categories are verified against a published list (Wargamer, "2024 feats"). Their **effects are from memory** and not in the SRD, so check them against the book before deciding. None of their text is used here.
- Players will probably use the *Player's Handbook* (Troy), so its feats matter as much as the SRD's.

---

## A. The root problem: Origin feats come back at level 4

The Character Origins sidebar says Azhi has **no Origin feats**. But under the 2024 rules, the Ability Score Improvement feature at level 4 (and later) lets you take **any feat you qualify for**, and Origin feats have no prerequisite. So a level-4 character can still take Alert, as Troy noticed. The sidebar removes them from character creation only.

**Options** (pick one):

- **A1. No Origin feats, ever.** Extend the sidebar: the Origin category doesn't exist on Azhi, so these feats can't be taken at any level. Simplest, and matches the sidebar's intent. Players lose Lucky, Healer, Crafter and the rest as level-4 picks.
- **A2. Origin feats from level 4, minus the duplicates.** Keep the category as level-4+ options, but strike the ones that copy a trait (§B).
- **A3. A personality trait in place of a feat.** At any level where you could take a feat, you can take a new personality trait instead (one you don't have). This is Troy's backlog idea ("traits at levels 4, 8…"), tried at its smallest. A trait is about 10 points against a feat's +2 ability, so it's a fair trade. Combine it with A1 or A2.

## B. Feats that duplicate a trait

| # | Feat | Source | Trait | The clash | Proposed fix |
|---|---|---|---|---|---|
| B1 | **Alert** (Origin) | SRD | **The Bold** (*Quick to Act*: PB to Initiative), **The Strategist** (*Initiative Swap*) | Alert *is* those two benefits; they were split from it (trait-benefits brainstorm). Bold plus Alert adds the PB **twice**, since different features stack. Strategist plus Alert gives the swap twice, which does nothing. | Remove Alert. |
| B2 | **Tavern Brawler** (Origin) | PHB | **The Scrapper** (*Brawler*; improvised weapon proficiency) | Same unarmed damage and the same proficiency. Taking both wastes most of the feat. (The brainstorm already noted the Scrapper is close to it.) | Remove, or strike under A2. |
| B3 | **War Caster** (General) | PHB | **The Rock** (*Steady Hands*: Advantage on Concentration saves) | War Caster's first benefit is the same Advantage; Advantage doesn't stack, so a Rock gets two-thirds of the feat. Troy has said generic feats like War Caster may go away (2026-10-29). | Keep, and accept the overlap; or remove if traits replace feats. |

## C. Feats that stack with a trait

These don't duplicate anything, but they add to a trait's benefit. Most are fine; listed so nothing surprises us.

| # | Feat | Source | Trait | What stacks | View |
|---|---|---|---|---|---|
| C1 | **Tough** (Origin) | PHB | **The Hearty** (*Hardy*: +1 HP per level) | +3 HP per level together. | Probably fine. |
| C2 | **Speedy** (General) | PHB | **The Wanderer** (*Long Stride*: +5 feet) | +15 feet together; a Red Wanderer was already checked at +5 (2026-10-30). | Probably fine. |
| C3 | **Crossbow Expert** (General) | PHB | **The Rock** (*Cool Under Pressure*) | Both remove the Disadvantage on ranged attacks next to an enemy; the Rock covers every ranged attack. | Fine; the feat has other benefits. |
| C4 | **Sentinel** (General) | PHB | **The Rock** (*Hold Your Ground*: Advantage on Opportunity Attacks) | A strong pairing for a battlefield lock-down character. | Watch in playtest. |
| C5 | **Unarmed Fighting** (Fighting Style) | PHB | **The Scrapper** (*Brawler*) | The feat's larger damage die makes *Brawler*'s d4 redundant for that character. | Fine; the Scrapper still has its proficiencies and social piece. |
| C6 | **Interception** (Fighting Style) | PHB | **The Guardian** (*Shield Bearer*) | Both protect an adjacent ally with a Reaction, so only one can be used per round. | Fine. |

## D. Feats that clash with the setting, not the traits

Noted here so they aren't lost; outside today's scope.

| # | Feat | Source | The clash |
|---|---|---|---|
| D1 | **Fey-Touched** | PHB | The Feywild and the Fey are scrapped (2026-11-01). Its spells could be reflavoured (to Silver, for teleportation). |
| D2 | **Blind Fighting**, **Boon of Truesight** | PHB; SRD | Both let a non-Black, non-Indigo character see in darkness; Darkvision belongs to Black and Indigo alone (2026-10-24). Short range or high level, so probably fine. |
| D3 | **Telepathic** | PHB | No psionics on Azhi yet (see the Psi Warrior note in `canon/brainstorm-classes.md`). |

## E. No clash found

The SRD's Magic Initiate, Savage Attacker, Skilled, Ability Score Improvement, Grappler, the four Fighting Style feats and the other Epic Boons clash with no trait. Skilled overlaps the Curious only in giving skills, which is harmless.

---

## Decisions for Troy

1. **The root problem (§A):** A1, A2 or A3 (A3 can be combined with either).
2. **Alert (B1):** remove it.
3. **Tavern Brawler (B2):** remove it.
4. **War Caster (B3):** keep it and accept the overlap, or remove it.
5. **The stacking cases (§C):** accept them all as fine, pending playtest.
6. **A general rule** for anything missed: "If a feat gives a benefit you already have from a personality trait or form, you don't gain that benefit twice; choose a different benefit of the feat, or another feat."
