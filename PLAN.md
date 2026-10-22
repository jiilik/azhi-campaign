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

- [ ] **Species → Dragonborn:** Unphased (young, flexible, weakest), 5 monochrome and 5 bichrome forms (adjacent colours only; bichrome sits between in power), plus rare Gold and Silver definitions for NPCs. Phasing rules with an anti-exploit penalty. Elemental affinities follow the wheel of opposition, never a superiority ranking. See the setting bible, §3. *Design approved to canon 2026-10-21:* `canon/brainstorm-species.md`. Next: write the SRD Species section from it. Open ribbons, more personality traits and the phasing penalty come later.
- [ ] **Character Creation** (after Character Origins is settled): revise Step 2 (species → colour choice; rebuild the Standard and Rare Languages tables) and the Trinkets table (swap other-species entries for Azhi flavour). Everything else is kept; see the tracker.
- [ ] **Remove other species** from character options. Adjust any rule that assumes them (languages, ancestry feats, and so on).
- [ ] **Backgrounds:** recast for dragonborn-only societies, for example sky-reader (Gold/Silver), archivist (Black), harbour pilot (Blue). *Superseded 2026-10-21: backgrounds are folded into species (traits plus affinity). Revisit what is left of this item when revising Character Origins.*
- [ ] **Classes:** align subclasses with the seven dragons, for example cleric domains, warlock patrons, druid circles and sorcerer origins.
- [ ] **Spells:** review light, darkness, time and travel spells against unpredictable day and night and True Dark.
- [ ] **Equipment and economy:** bone as stone, ichor as oil, light-storing crystals, timekeeping by "watches".

### 2b. World-dependent rules *(proposed)*

- [ ] **Monsters and NPC stat blocks:** remove or recast every humanoid that isn't dragonborn (orcs, goblins, elves…). Re-skin generic NPCs as dragonborn. Decide what sentient-seeming monsters become.
- [ ] **Deities:** the seven dragons as living gods (domains, symbols, holy days). Holy symbol: the ouroboros ring.
- [ ] **Environment rules:** light levels without a fixed day, True Dark, the cold floods, weak gravity on the inner rim (jump and fall distances?).

### 2c. New sections *(proposed)*

- [ ] Setting overview and the myth (link to `canon/azhi-myth.md`)
- [ ] Variant tellings of the myth: who tells which version, and why *(proposed)*
- [ ] The Seven Dragons: personalities, lairs and current agendas
- [ ] Gazetteer: the Bite, the Skull, the Lower Jaw and the Maw, the Spine Range, the Inner Sea, the limb ridges, the Tail
- [ ] Climate, timekeeping and the calendar ("watches", True Dark)
- [ ] Travel on a torus: using the wrapping map, the scale ladder, and why bearings are true
- [ ] The Underworld as anatomy: arteries, heart, lungs, stomach
- [ ] Factions and cultures per colour, including internal disagreements and inter-colour policy disputes

### 2d. Deletions

- [ ] Confirm the deletions list from triage and remove those files in a single commit, for an easy revert

## Phase 3: Consistency pass

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

- [ ] Biome and climate overlay for the world map (light and wind model)
- [ ] Regional maps at higher resolution around the Bite and the Lower Jaw
- [ ] Re-roll continents with a new seed if the current ones don't suit (`worldgen/terrain.py`)
- [ ] Cult hooks: "finish the meal" zealots, Bite pilgrims, Black's hidden agenda
