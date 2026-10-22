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
- **Peoples:** dragonborn of seven colours (Gold, Silver, Black, Blue, White, Red, Green) are the only people. There are **no other sentient species**, in text or in art.
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
| `canon/brainstorm-species.md` | **Species design (CANON, 2026-10-21):** traits, affinities, hybrids, point budget. Spec for the SRD Species section. |
| `canon/brainstorm-personality.md` | Personality archetype research for reworking the traits (PROPOSED, 2026-10-22). |
| `canon/azhi-myth.md` | The myth: exact corrected text. `azhi-myth-corrected.rtf` is authoritative; `-original.rtf` is Troy's upload. |
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
