# srd: setting-specific SRD derivative

This folder is empty until Phase 1 (see `PLAN.md`).

## Intake plan

1. Add the source SRD under `srd/_source/`, with the PDF or markdown exactly as published. It is never edited.
2. Convert it to markdown, one file per section, in numbered folders that mirror the SRD's order. For example:
   ```
   srd/01-playing-the-game/…
   srd/02-character-creation/…
   srd/03-classes/cleric.md
   srd/04-species/dragonborn.md
   …
   ```
3. **Commit the untouched conversion first.** Every later revision then appears as a clean diff against the original wording.
4. Create `srd-tracker.md`:

| File | Status | Priority | Notes |
|---|---|---|---|
| `03-classes/cleric.md` | untouched | high | domains → seven dragons |

Status values: `untouched`, `keep`, `revise`, `delete`, `new`, `done`.

## Revision rules

- Change only what Troy approves, with proposals as numbered lists.
- New setting-specific sections get a `new-` prefix or a status of `new`.
- Keep the CC BY 4.0 attribution (`ATTRIBUTION.md`).
