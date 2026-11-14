# Mage Kit starting spellbooks (2026-11-13)

Each book is a distinct item with a set list of six spells (spells are found, not picked from class lists). One page per book, drawn as a scroll unrolled only as far as its spells, with the rest of the text still rolled up at the edges.

| Book | Branch | Style | Output |
|---|---|---|---|
| The Junior Wizard's Primer | straight on (Wizard) | a herald's proclamation scroll, portrait | `output/primer.png`, `.pdf` |
| Selected Summons for Novices | right, through Control | a painted handscroll, landscape | `output/summons.png`, `.pdf` |
| Practical Alchemy | left, through Lore | a papyrus roll, landscape | `output/alchemy.png`, `.pdf` |

- **Spell text:** SRD 5.2.1, verbatim, read from `srd/07-spells` by `spells.py`. Each page carries the SRD attribution statement.
- **Run:** `python3 render.py [primer summons alchemy]` (Playwright Chromium). PNGs at 3× (Letter, 2550 × 3300 or 3300 × 2550); PDFs are vector, one Letter page each. The body text is sized automatically to fill its columns.
- **Fonts** (`fonts/`, all SIL Open Font License 1.1, from @fontsource): UnifrakturMaguntia, IM Fell English, Cinzel, Cinzel Decorative, Cormorant Garamond, Shippori Mincho, Zen Old Mincho, Marcellus.
- **Figures** come from `art/cartoon/tapestry_lib.py`, so the dragonborn follow the form rules in `art/STYLE.md`: two heralds (Red and White) sounding horns; a Black summoner calling a cat familiar; a Yellow alchemist at the alembic.
- The fragments of other text at the rolled edges are invented filler, not canon.
