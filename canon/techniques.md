# Techniques

**Status: PROPOSED** (opened 2026-11-07). Designed techniques for the stamina system, written as stat blocks. The parts they're built from are in `canon/parts-bin-techniques.md`. Decisions are Troy's (voice, 2026-11-07) unless marked *(Claude)*.

## How techniques work *(Troy, 2026-11-07)*

- **"Technique" is the umbrella term.** A technique can have a **free** use, a **stamina** use, or both. The word "at-will" is no longer used for a separate kind of thing; free techniques are the stamina side's equivalent of cantrips.
- **Kits give techniques from a list.** The Herald picks **three**, the Scout **two** and the Fighter **one**, each from their kit's technique list. Each kit needs its own list. *(Claude: build each list from the kit's own section of the parts-bin distribution table plus its neighbouring seams.)*
- **Stat block, like a spell's:** timing (action, Bonus Action or Reaction), range, targets, the free effect, then the stamina add-ons.
- **Add-ons:** each technique can offer **several ways to spend stamina**, each with its own cost. You **stack whichever you want** on one use, **with no overall cap**, to keep the rules simple. The small pools limit it naturally. An add-on can be bought **once** unless the technique says otherwise.
- **Reactions** in a technique can be used **"at any time"**, even on another creature's turn, with no other trigger. Reactions are a scarce resource (one per round), and choosing when to spend one is the skill: a Herald holding a Reaction for *Scatter!* gives up its Opportunity Attack.
- **Weapon Mastery comes first:** every kit with weapons now has at least one mastery, so the basic riders (Push, Topple, Slow and the rest) come from masteries. **Techniques must not copy them.** Free techniques at the Dex–Str seam are things like moving a character after a hit, or a little extra damage of a particular type.

## Generic tiles *(Troy, 2026-11-07)*

Two kinds of tile are scattered across the whole skills grid and stack no matter which branch they're on:
- **Proficiency Bonus** tiles.
- **Damage Boost** tiles. When you take the Attack action, each one counts as an **extra attack** (like Extra Attack). When you cast a cantrip, each one adds an **extra damage die** (like cantrip scaling). One action can't do both, so they never stack. They scale with total progress rather than depth in a branch.
  - *(Claude)* The timing matches the 2024 rules: cantrips scale at levels 5, 11 and 17, and the fighter gains attacks at 5, 11 and 20. **To check:** Troy mentioned a 20-node character finding **four** Damage Boosts. Four would be one more step than either the cantrip scaling or the fighter (both three), so three may be the ceiling for a 20-node character.
  - **Placed (Troy, 2026-11-07):** six **Proficiency Bonus +1** tiles on **ring 4, on the seams** (the exact middle of each side of the ring, between two kits), 4 steps from the centre.
  - **Placed (Troy, 2026-11-07):** six Damage Boost tiles on **ring 5, straight out from each kit** (the ring's six corner hexes, on each kit's main line), 5 steps from the centre.
  - **Settled (Troy, 2026-11-07): four is fine.** Finding four in 20 nodes takes a real munchkin, going about five deep in four branches. *(Claude: this assumes Damage Boost tiles sit at about depth 5 in a branch, the level-5 milestone.)*

## Dropped

- **True Strike** (2024 SRD cantrip): made for a caster who fights with a weapon (bladesinger, valour bard). Troy: it doesn't fit the theme, at least not in its 2024 form. *(Claude: the only seam it could suit is Cha–Dex, since Intelligence and Strength aren't neighbours.)*

## Techniques

### On Me!

*Herald technique*

- **Timing:** Bonus Action.
- **Range:** one ally who can hear you.
- **Free effect:** the ally moves 5 feet towards you. This costs it no movement and doesn't provoke Opportunity Attacks.
- **Stamina add-ons** (1 stamina each; each can be bought once):
  - **Reaction:** use it as a Reaction, at any time.
  - **Everyone:** it affects every ally who can hear you.
  - **Further:** the move is 10 feet instead of 5.
- *Full cost: 3 stamina for a Reaction that moves the whole party 10 feet.*

### Scatter!

*Herald technique; the inverse of* On Me!

- **Timing:** Bonus Action.
- **Range:** one ally who can hear you.
- **Free effect:** the ally moves 5 feet away from you. This costs it no movement and doesn't provoke Opportunity Attacks.
- **Stamina add-ons** (1 stamina each; each can be bought once):
  - **Reaction:** use it as a Reaction, at any time.
  - **Everyone:** it affects every ally who can hear you.
  - **Further:** the move is 10 feet instead of 5. *(Troy limited this to one purchase: it's free movement, multiplied by the party's size.)*
- *(Claude)* Five or 10 feet won't get anyone clear of a large area like a 20-foot-radius *Fireball* unless they're at its edge. It works best against lines, cones and small areas.

### The coaching set: *You've Got This!*, *There's an Opening!* and *Heads Up!*

*Herald techniques (voice, 2026-11-09).* Three Guidance-style coaching techniques, one each for ability checks, attacks and saves, built the same way. Troy wanted the Herald to have a Guidance equivalent, plus one that helps only attacks and one that helps only defence. Names: *You've Got This!* and *There's an Opening!* were Claude's, accepted; *Heads Up!* is Troy's.

| Technique | The d4 applies to |
|---|---|
| **You've Got This!** | the ally's next **ability check** |
| **There's an Opening!** | the ally's next **attack roll** |
| **Heads Up!** | the ally's next **saving throw** (saves only for now, not AC) |

- **Timing:** Bonus Action.
- **Range:** one ally who can hear you.
- **Free effect:** the ally adds a d4 to its next roll of that kind before the end of its next turn.
- **Stamina add-ons** (1 stamina each; each can be bought once):
  - **Reaction:** use it as a Reaction, at any time, even after the ally has rolled.
  - **Everyone:** it affects every ally who can hear you.
  - **Bigger die:** a d6 instead of a d4.
- **Balance** *(discussed, Troy: "reasonable", it doesn't unbalance anything)*:
  - The Bonus Action is the free version's cost, and it competes with *On Me!*, *Scatter!* and the rest. Outside combat it's free to use, like Guidance, which nobody casts in combat anyway.
  - *There's an Opening!* with the Reaction add-on, for 1 stamina, is roughly a Bardic Inspiration die. A 2024 bard gives one as a Bonus Action, a d6 the ally adds after failing a d20 Test, as many times as its Charisma modifier per Long Rest, with Short Rest recovery from level 5. A Herald with 4 stamina and a PB top-up on a Short Rest gets about as many.
  - **Resolved (voice, 2026-11-09):** the bigger-die add-on stays at 1 stamina on *There's an Opening!* too. The Reaction add-on is the strong part: the ally misses, you shout, and it hits after all. Troy: "a fair trade". The free Bonus Action version is a gamble that the ally will need it; stamina buys the certainty of waiting for the miss.
- *(Claude; checked against the SRD 2026-11-09)* The 2024 *Guidance* takes an action, lasts up to a minute with Concentration, and adds 1d4 to every check with one chosen skill. These techniques give one roll each instead.

### Invigorate

*Herald technique (voice, 2026-11-09); name Troy's.*

- **Timing:** Bonus Action.
- **Range:** one ally who can hear you.
- **Cost:** 1 stamina. **No free version.**
- **Effect:** the ally **takes a Bonus Action right away**, on your turn. You trade your Bonus Action, plus 1 stamina, for theirs.
- **No restriction on spells** *(Troy)*. The stamina is the real cost: renewable but expensive, especially early, like half a spell.
- *(Claude)* "Right away" keeps it safe: the ally can't save it for its own turn and take two Bonus Actions there, which is where two *Flurries of Blows* or two Bonus Action spells would break.

### Greater Invigorate

*Herald technique (voice, 2026-11-09); name Troy's.* It replaces Claude's *Strike Now!* pitch: giving up one attack of several gets cheap as attacks are added, so Troy reframed it as a bigger *Invigorate*.

- **Timing:** action.
- **Range:** one ally who can hear you.
- **Cost:** 2 stamina. **No free version.** It's more powerful than *Invigorate*, since it gives one character two actions in a round.
- **Effect:** the ally **takes an action right away**, on your turn, **without spending its Reaction**.
- **No add-ons** for now; Troy is happy with the plain balance.
- *(Claude)* The closest comparison is the Fighter's Action Surge. The ally acts on your turn, so it never has two actions in its own turn. The case to watch is a caster ally casting two big spells in one round.

### Reinvigorate

*Herald technique (voice, 2026-11-09); name Troy's.* It completes the set: *Invigorate* passes on a Bonus Action, *Greater Invigorate* an action, and *Reinvigorate* a Reaction.

- **Timing:** Reaction.
- **Range:** one ally who can hear you.
- **Cost:** 1 stamina. No free version.
- **Effect:** the ally **regains its Reaction**. But it can't use it until **another creature moves or takes its turn**.
- *(Why the delay; Troy gamed it out:)* Otherwise a fighter could make an Opportunity Attack, and a Herald could immediately restore its Reaction for a second one against the same foe. *(Claude: strictly, the trigger has already passed, but the delay makes it explicit.)*

### Rally

*Herald technique (voice, 2026-11-09). Claude pitched it as "Get Up!"; Troy named it Rally and added the per-ally cost.* It's the warlord's healing without magic: the ally heals from its own reserves.

- **Timing:** Bonus Action.
- **Range:** allies who can hear you.
- **Cost:** 1 stamina for the first ally, **plus 1 for each additional ally**, with no limit. *(Troy: at first level, four allies is your whole pool.)*
- **Effect:** each ally spends one of its **Hit Point Dice**, rolls it, adds its Constitution modifier, and regains that many Hit Points right away.
- **Balance** *(discussed; Troy happy)*: 1 stamina should be about half a level 1 spell. *Healing Word* (checked against the SRD 2026-11-09) is a Bonus Action at 60 feet that heals one creature 2d4 plus the caster's modifier, about 8 at first level. Rally heals about 6–7 with a d8 Hit Die, a bit over half of that. It also spends one of the ally's Hit Point Dice, which it would otherwise use on a Short Rest, and that brings it close to half.
- *(Claude, to confirm)* It can pick up an ally at 0 Hit Points, as *Healing Word* and *Cure Wounds* can, since that ally can still hear you. Troy asked how 5e handles this, and it's assumed here.
- **First home for healing on the grid.** Healing had none after the cleric was dropped.

## Ideas in progress

- **Action-economy brokering** *(Troy, 2026-11-09)*: the Herald can use the warlord's action economy to boost others, and even **move action economy from one character to another** on the field. There has to be a reason and a cost: you can't give away all your actions for nothing, because the receiving character gains an advantage (better position, a stronger attack). Each transfer has to be checked for what it could break. *Invigorate* is the first.
  - *(Claude's ideas)* Spend your Reaction to give an ally theirs back; swap turn order so an ally acts now.
- **Strike Now!** *(Claude's pitch; replaced by* Greater Invigorate *on 2026-11-09)*: give up one of your attacks so an ally makes one with its Reaction, the warlord's signature move. Troy noted the action-economy cost: your attack plus the ally's Reaction. *(Claude)* If the ally declines, nothing happens and no stamina is spent.

