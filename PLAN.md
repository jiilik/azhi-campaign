# Azhi — Project Plan

The goal is a setting-specific derivative of the D&D 5e SRD for the ring-world Azhi, refined through a consistency pass, simulated character builds and interactive playtests.

**How to use this file:** work top to bottom. Tick items as they finish (`- [x]`). Items marked *(proposed)* are Claude's suggestions, so Troy can strike or reorder them. Add new items where they belong rather than at the end.

---

## Phase 0: Setup

- [x] Scaffold the repo: primer (`CLAUDE.md`), setting bible, decision log, myth text, worldgen and art code, outputs
- [x] Player handout with the myth, cover art, map, torus view and dragonborn scenes (Claude Doc; link in `handouts/README.md`)
- [x] Create the private GitHub repo `jiilik/azhi-campaign`
- [x] Install the Claude GitHub App on `jiilik/azhi-campaign` (only that repo) so sessions can push
- [x] Push the initial commit
- [ ] Create the Claude Project; paste `project-instructions.md` and add the knowledge files it lists
- [ ] Answer the OPEN questions that block Phase 1:
  - [x] SRD version: **5.2** (2024 rules); the file in hand is **5.2.1**
  - [x] Myth status: canonical for worldbuilding; in-universe, variant tellings exist

## Phase 1: SRD intake

- [x] Upload the SRD (PDF or markdown): SRD 5.2.1 PDF in `srd/_source/`
- [x] Convert it to markdown and split it into one file per section under `srd/` (for example `srd/03-classes/03-cleric.md`), keeping the original text in the first commit so every later change shows as a diff. Imported from downfallx/dnd-5e-srd-markdown, checked against the PDF.
- [x] Generate `srd/srd-tracker.md`: every section with Status (`untouched` / `keep` / `revise` / `delete` / `new` / `done`), Priority and Notes
- [x] Replace the placeholder in `ATTRIBUTION.md` with the SRD's exact CC BY 4.0 statement
- [ ] **Triage pass (Troy decides):** *(in progress: Playing the Game and Character Creation done)* mark each section keep / revise / delete. Claude proposes a default with a one-line reason per section.
- [ ] Add planned **new** sections to the tracker (Phase 2c)

## Phase 2: Section-by-section revision (the long phase)

**Loop for each section:**

1. Claude summarizes the section and lists proposed changes as numbered items.
2. Troy approves, rejects or rewrites them.
3. Claude applies exactly the approved set and shows the diff.
4. Update the tracker, decision log and bible, then commit.

### 2a. Highest impact first *(proposed order)*

- [ ] **Species → Dragonborn:** Unphased plus a nine-form colour wheel (5 dragon colours, 4 younger colours; replaced the ten-form wheel 2026-10-24), plus rare Gold and Silver definitions for NPCs. Phasing rules with an anti-exploit penalty. Drafted in `srd/04-character-origins/02-character-species.md`. Open: the phasing breaking-point triggers only (the penalty is tentative as of 2026-11-04; see the mortality brainstorm). Gold and Silver are backburnered to the DM material (see the backlog); the trait benefits are canon (2026-10-30).
- [ ] **Character Creation** (after Character Origins is settled): revise Step 2 (species → colour choice; rebuild the Standard and Rare Languages tables) and the Trinkets table (swap other-species entries for Azhi flavour). Everything else is kept; see the tracker.
  - [ ] **Languages:** *(Troy, 2026-10-30)* tied to your region of origin, not to traits or colour (sidebar in Character Origins). Still to do: list Azhi's languages by region, in a "Geography of Azhi" section (see 2c, Gazetteer), and rebuild Step 2's language tables.
- [ ] **Remove other species** from character options. Adjust any rule that assumes them (languages, ancestry feats, and so on).
- [x] **Backgrounds:** recast for dragonborn-only societies, for example sky-reader (Gold/Silver), archivist (Black), harbour pilot (Blue). *Superseded 2026-10-21: backgrounds are folded into species (traits plus affinity). Revisit what is left of this item when revising Character Origins.* Closed 2026-10-30: personality traits replace backgrounds and Origin feats (sidebar in Character Origins).
- [ ] **Classes:** align subclasses with the seven dragons, for example cleric domains, warlock patrons, druid circles and sorcerer origins. *On hold (Troy, 2026-11-05): players start with the PHB's default classes, reflavoured as needed. Evaluation for later: `canon/brainstorm-classes.md`. Also exploring (2026-11-05) replacing classes with a two-tree progression built for phasing: `canon/brainstorm-progression.md`.*
- [ ] **Feats → extended traits** *(Troy, 2026-11-05)*: feats are scrapped. Replacement sets ("extended traits", working name) come at the feat levels. Assume players own the PHB. Working file: `canon/brainstorm-extended-traits.md`.
  - [x] Toolbox: every SRD and PHB feat broken into parts (2026-11-05)
  - [x] Classes broken into parts, and every part scored: `canon/parts-bin.md` (2026-11-05)
  - [ ] **Two-tree progression** (exploring, `canon/brainstorm-progression.md`): all nine first questions answered 2026-11-05.
    - [ ] **Next (agreed 2026-11-05): build a couple of test paths** from `canon/parts-bin.md` to test the concept: milestone depth against the 2024 power curve.
    - [ ] Polish the phasing tree's 33 roots; mana costs for spell levels 6–9 and the nova limit
  - [ ] Troy answers the design questions (§3 of the working file)
  - [ ] Design the extended traits from the toolbox, reworded
  - [ ] Replace the feat hooks in the classes and other chapters (§2 of the working file)
- [ ] **Spells:** review light, darkness, time and travel spells against unpredictable day and night and True Dark.
- [ ] **Equipment and economy:** bone as stone, ichor as oil, light-storing crystals, timekeeping by "watches".

### 2b. World-dependent rules *(proposed)*

- [ ] **Monsters and NPC stat blocks:** remove or recast every humanoid that isn't dragonborn (orcs, goblins, elves…). Re-skin generic NPCs as dragonborn. Decide what sentient-seeming monsters become.
- [ ] **Deities:** the seven dragons as living gods (domains, symbols, holy days). Holy symbol: the ouroboros ring.
- [ ] **Environment rules:** light levels without a fixed day, True Dark, the cold floods, weak gravity on the inner rim (jump and fall distances?).

### 2c. New sections *(proposed)*

- [ ] Setting overview and the myth (link to `canon/azhi-myth.md`)
- [ ] **Deep timeline:** six epochs before the present, each ending in catastrophe, with ruins and old lairs on the map. New origin lore for Brown, Yellow, Indigo and Grey replaces colour mixing (Troy, 2026-10-31). Working file: `canon/brainstorm-epochs.md`.
  - [ ] **Epoch myths** (Troy writes them): a canonical myth for each epoch. Older ones are hazier and disputed; the homunculi war is in living memory, so its account must be precise.
  - [ ] **Other planes:** see the planes notes in `canon/brainstorm-epochs.md` (2026-10-31).
    - [x] **Plane audit (Claude, text session; done 2026-10-31, `canon/audit-planes.md`):** search for everything that depends on other planes: SRD spells, magic items, monsters, classes and subclasses, plus well-known non-SRD subclasses by name only. Report what would break; don't decide. This feeds a player guide on which outside options fit Azhi.
  - [ ] **Spell origins** (working list: `canon/brainstorm-spell-origins.md`): assign each spell to the dragon that taught it, or to the later epoch that discovered it. A test run of 53 spells passed (2026-11-01), and 59 are listed so far; continue spell by spell. Also: stat blocks for the god-dragons, now level 9 casters.
  - [ ] **Monster review** (running list: `canon/proposed-monster-changes.md`): once the lore settles, review the existing creature types and monsters against it (including undead, fey, fiends and celestials). Not a full rebuild.
  - [ ] **Campaign settings:** the epoch sites as ready-to-play campaigns, starting perhaps with *The Last Machine*. Each states a default ending that later books assume, which DMs can adjust.
  - [ ] **Monstrosities** from the homunculi's spilled power: pick up in the monsters chapter.
- [ ] Variant tellings of the myth: who tells which version, and why *(proposed)*
- [ ] The Seven Dragons: personalities, lairs and current agendas
- [ ] Gazetteer: the Bite, the Skull, the Lower Jaw and the Maw, the Spine Range, the Inner Sea, the limb ridges, the Tail
- [ ] Climate, timekeeping and the calendar ("watches", True Dark)
- [ ] Travel on a torus: using the wrapping map, the scale ladder, and why bearings are true
- [ ] The Underworld as anatomy: arteries, heart, lungs, stomach
- [ ] Factions and cultures per colour, including internal disagreements and inter-colour policy disputes. Started 2026-10-30 in `canon/factions.md`, with the concept and the Undertow; unaffiliated city and nation-state factions are still to come.

### 2d. Deletions

- [ ] Confirm the deletions list from triage and remove those files in a single commit, for an easy revert

## Phase 3: Consistency pass

- [ ] Run `canon/design-review-checklist.md` against the finished design (it can also be run as a preliminary check at any time)
- [ ] Build `canon/glossary.md` (proper nouns, terms, colours, spelling)
- [ ] Run parallel review agents, one per batch of sections, each checking against the setting bible and glossary. Each returns conflicts as `file:line · issue · suggested fix`.
- [ ] Check cross-references: features named in one section that are defined in another
- [ ] Mechanics sanity check: every colour lineage stays within typical species power budgets
- [ ] Troy rules on each conflict; apply, then commit

## Phase 4: Virtual players

- [ ] Define 4–6 player personas in `playtest/personas.md` (optimizer, roleplayer, newcomer, rules-lawyer, chaos gremlin, tactician)
- [ ] Each persona builds characters at **levels 1, 5, 11, 17** across a spread of colours and classes. Save them to `playtest/builds/`.
- [ ] Each build reports "interesting things that popped out": exploits, dead options, flavour gaps, rules questions
- [ ] Compile `playtest/findings.md`, ranked by severity, and feed the fixes back into Phase 2 items

## Phase 5: Interactive playtests

- [ ] Write `playtest/dm-mode.md`: instructions for a Claude session to run scenes, and to play NPCs and dragons in Saturday-Morning Bold voice
- [ ] Choose 3–4 scenarios that stress the setting, for example a True Dark survival, a Spine Range crossing, a Lower Jaw sea-stack heist, and an audience with a dragon god
- [ ] Run sessions with the Phase 4 characters. Save logs to `playtest/logs/`.
- [ ] Record rulings and fixes, update the rules, then commit

## Phase 6: Compile and publish

- [ ] Assemble the player-facing handbook from `srd/` plus the new sections, with the attribution statement
- [ ] Art pass (Saturday-Morning Bold): seven dragon portraits, a lineup of the seven dragonborn colours, lair scenes, gazetteer spot art
- [ ] Export (Claude Doc → PDF or Word) and do a print test

## Backlog / Ideas *(proposed, unscheduled)*

- [ ] Mortality brainstorm: since Azhi died and was reborn as a world, perhaps remove mortality from the game, after a fashion. Covers life span and ties into the phasing rules (Troy, 2026-10-30)
- [ ] Gold and Silver dragonborn as colours, for the DM material, not the players' chapter (Troy, backburnered 2026-10-30)
- [ ] Personality traits replace feats: gain traits at levels 4, 8 and so on, with advanced traits in the role of feats (Troy, considering, 2026-10-29)
- [ ] A Warlord class, a battlefield controller; *Rotate the Line* is parked for it (Troy, considering, 2026-10-29)
- [ ] Biome and climate overlay for the world map (light and wind model)
- [ ] Regional maps at higher resolution around the Bite and the Lower Jaw
- [ ] Re-roll continents with a new seed if the current ones don't suit (`worldgen/terrain.py`)
- [ ] Cult hooks: "finish the meal" zealots, Bite pilgrims, Black's hidden agenda
