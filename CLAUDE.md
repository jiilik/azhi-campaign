# Session Primer: read this first

You are helping **Troy** (the author and DM) build **Azhi**, a D&D campaign setting on the 2024 rules (SRD 5.2). The world is a ring, the corpse of a self-devouring space dragon. This repo is the project's memory. Chat history does not carry over between sessions; these files do.

## Start of every session

1. Read `PLAN.md`. Find the first unchecked item in the current phase. That is probably today's work.
2. Read `canon/setting-bible.md` (facts, each tagged CANON, PROPOSED or OPEN) and skim `canon/decisions.md` (newest first).
3. If the work touches the rules, read `srd/srd-tracker.md` and the relevant section files.
4. In one or two sentences, tell Troy what you understand the next step to be. Then start.

## End of every session

- Tick the finished items in `PLAN.md`.
- Add new decisions to `canon/decisions.md` and update `canon/setting-bible.md` to match.
- Update `srd/srd-tracker.md` if any sections changed.
- Commit with a clear message, then push to `origin` (GitHub `jiilik/azhi-campaign`).

## Standing rules

- **Never change canon text without explicit approval.** This applies above all to `canon/azhi-myth.md` and the `.rtf`. Its shifting tenses, it/he pronouns and archaic phrasing are deliberate oral-legend style. Propose edits as a **numbered list** (original → proposed, with one line of context) and apply only the numbers Troy approves.
- **Edit only what was asked.** When revising any text, change nothing beyond the agreed scope. Show a diff, or list every change. Troy checks.
- **Keep CANON and PROPOSED apart.** Your own ideas go in as PROPOSED until Troy confirms them.
- **Peoples:** dragonborn of several colours are the only **people** on Azhi: the only species with societies, and the only playable one. Other **sentient beings** exist (the dragons themselves, the thinking machines, things from beyond, intelligent monsters), but none of them is a people. Other peoples, such as elves, appear only in **Azhi's own stories and legends**, which everyone there considers fantasy. *(Revised by Troy, 2026-11-01.)*
- **No "racist dragons".** Colour differences are elemental opposition and policy disputes, never superiority or prejudice.
- **Art:** use **Saturday-Morning Bold** unless Troy says otherwise. Draw it with the code in `art/cartoon/`. See `art/STYLE.md`.
- **Spelling:** Canadian (colour, favourite, flavour).
- **SRD licence:** CC BY 4.0. Keep `ATTRIBUTION.md` and the attribution statement in any compiled document.

## File map

| Path | What |
|---|---|
| `PLAN.md` | Phased project plan with a checklist. **Where we are.** |
| `canon/setting-bible.md` | All setting facts with status tags |
| `canon/decisions.md` | Dated decision log, newest first |
| `canon/brainstorm-species.md` | **Species design (CANON, 2026-10-21):** character building, traits, point budget. Its forms are superseded by the nine-form wheel (2026-10-24). |
| `canon/brainstorm-personality.md` | Personality archetype research for reworking the traits (PROPOSED, 2026-10-22). |
| `canon/brainstorm-colour-wheel.md` | Working record of the nine-form colour wheel (ADOPTED 2026-10-24). |
| `canon/source-personality-traits-v1.md` | The original twelve personality traits, retired 2026-10-24, kept as source material for mechanics. |
| `canon/brainstorm-trait-benefits.md` | Working record for the 24 traits' benefits: strategy, SRD parts bin, design and balance passes (ADOPTED 2026-10-30). |
| `canon/brainstorm-phasing.md` | Phasing and mortality brainstorm: canon so far, open questions, spillover (PROPOSED, 2026-10-30). |
| `canon/brainstorm-epochs.md` | Deep timeline: six epochs before the present, each ending in catastrophe; new origin lore for the non-dragon colours (PROPOSED, 2026-10-31). |
| `canon/brainstorm-spell-origins.md` | Where each spell came from: the dragon that taught it, or the epoch that discovered it (PROPOSED, tentative, 2026-11-01). |
| `canon/brainstorm-classes.md` | Classes and subclasses: the SRD's twelve and the other 2024 PHB subclasses rated against the setting, with decisions for Troy (ON HOLD, 2026-11-05). |
| `canon/brainstorm-extended-traits.md` | Extended traits, which replace feats: where the rules depend on feats, design questions, the tech tree (the feat toolbox moved to `canon/parts-bin.md`) (PROPOSED, 2026-11-05). |
| `canon/brainstorm-progression.md` | Exploring a classless progression built for phasing: an experience tree kept on phasing, and a phasing tree reset on phasing (ADOPTED direction 2026-11-11: full class rebuild). |
| `canon/diagrams/` | The skills grid diagram: `skills_grid.py` draws `skills-grid.png`, `.svg` and `.pdf` (`--mono` for a greyscale copy); `print_wheels.py` makes `progression-wheels-print.pdf`, both wheels in colour on two Letter pages, for scribbling and reviews; edit its TILES and THEMES as the grid is designed (2026-11-07). |
| `canon/parts-bin.md` | Every SRD and PHB class and feat broken into parts, each with a best-guess points score on the Character Origins scale, a tree guess and a totals check (PROPOSED, tentative, 2026-11-05). |
| `canon/parts-bin-techniques.md` | Technique parts for one stamina system: monk, Battle Master manoeuvres, 4e warlord ideas and the bard, each with trigger, cost, target and a home on the skills grid (PROPOSED, 2026-11-07). |
| `canon/techniques.md` | Designed techniques (stamina system) as stat blocks with stackable stamina add-ons; the generic Attack Up tile (PROPOSED, 2026-11-07). |
| `canon/proposed-feat-changes.md` | Feat-by-feat clashes with the personality traits (SUPERSEDED 2026-11-05 by extended traits). |
| `canon/audit-planes.md` | Report: everything in the SRD (and well-known non-SRD subclasses) that depends on other planes (2026-10-31). |
| `canon/proposed-monster-changes.md` | Running list of proposed changes to the SRD monsters, each with its reason, to apply in one pass if accepted (PROPOSED, 2026-11-01). |
| `canon/proposed-spell-changes.md` | Running list of proposed changes to the SRD spells, each with its reason, to apply in one pass if accepted (PROPOSED, 2026-11-01). |
| `canon/factions.md` | Factions, the rules of a civilization: the concept (CANON), the entry layout and the Undertow (2026-10-30). |
| `canon/minigame-character-builds.md` | Rules for the build-testing minigame (famous characters, two builds). Its outputs stay in chat and are never recorded. |
| `canon/design-review-checklist.md` | Checks to run against the design (canon items only), plus a review log. |
| `canon/azhi-myth.md` | The myth: exact corrected text. `azhi-myth-corrected.rtf` is authoritative; `-original.rtf` is Troy's upload. |
| `srd/05-fighting-styles/` | The six fighting styles, verbatim from SRD 5.1 with a source note (2026-11-10). |
| `srd/` | SRD section files and `srd-tracker.md` (Phase 1 onward) |
| `worldgen/` | Terrain, map projection and 3D torus renderer. See `worldgen/README.md`. |
| `art/` | Cartoon library, style spec and renders. See `art/README.md` and `art/STYLE.md`. |
| `handouts/` | Player handouts. The myth handout lives online as a Claude Doc (link in `handouts/README.md`). |
| `project-instructions.md` | Text pasted into the Claude Project's custom instructions |
| `ATTRIBUTION.md` | SRD CC BY 4.0 attribution |

## Working style Troy has shown

- Give him numbered options to approve or reject, then apply exactly the approved set.
- He values verification. Check against the source before claiming something changed or didn't.
- He trims aggressively. Keep handouts focused, with session-zero or rules material going elsewhere.
- Long, multi-phase work. Prefer one SRD section (or a small batch) per session, committed at the end.
