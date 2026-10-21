# srd: setting-specific SRD derivative

The rules base is **SRD 5.2.1** (the April 2025 update of SRD 5.2, the 2024 core rules), CC BY 4.0. Attribution: `ATTRIBUTION.md`.

## Sources

- `_source/SRD_CC_v5.2.1.pdf`: the official PDF, exactly as published. **Authoritative. Never edited.**
- The markdown was imported from [downfallx/dnd-5e-srd-markdown](https://github.com/downfallx/dnd-5e-srd-markdown) at commit `1b4b99dcb786cdd1a2fb26f8acec1551191f1ca4` (2026-01-09). At intake it was checked word by word against the PDF: about 120 of about 202,000 words differ, mostly table headers that the PDF repeats when a table continues onto a new page, plus words hyphenated across line breaks. Known style differences from the PDF: straight quotes and apostrophes, HTML tables, and `_italic_` run-in labels. These were left as imported.
- `00-legal.md` was transcribed from PDF page 1 (the markdown source lacks it).

## Layout

One file per section, in numbered folders that follow the SRD's order. The import commit contains the text exactly as converted (only a byte-order mark was dropped), so every later change shows as a diff against it.

| Folder | Split |
|---|---|
| `01-playing-the-game/`, `02-character-creation/`, `06-equipment/`, `09-gameplay-toolbox/` | one file per section |
| `03-classes/` | one file per class, including its spell list and subclass |
| `04-character-origins/` | backgrounds; species |
| `05-feats/`, `08-rules-glossary/` | one file each |
| `07-spells/` | the two rules sections, then `spells-a.md` … `spells-z.md` by first letter |
| `10-magic-items/` | categories; rules; an introduction; then `items-a.md` … by first letter |
| `11-monsters/` | stat block rules |
| `12-monsters-a-z/`, `13-animals/` | one file per creature group (for example `goblins.md`, `black-dragons.md`) |

`_tools/split_srd.py` reproduces the split from the markdown source and checks that the pieces rejoin byte-for-byte. `_tools/index.json` maps each file to its source lines and headings.

## Tracker

`srd-tracker.md` lists every file. Status values: `untouched`, `keep`, `revise`, `delete`, `new`, `done`.

## Revision rules

- Change only what Troy approves, with proposals as numbered lists.
- New setting-specific sections get a `new-` prefix or a status of `new`.
- Keep the CC BY 4.0 attribution (`ATTRIBUTION.md`).
