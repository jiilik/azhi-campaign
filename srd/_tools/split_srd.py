#!/usr/bin/env python3
"""Split the SRD 5.2.1 markdown (downfallx/dnd-5e-srd-markdown) into one file per section.

The text is not changed: each output file is an exact slice of a source file
(apart from a leading byte-order mark, which is dropped). The script checks that
the slices rejoin into the original byte-for-byte.

Usage: python3 srd/_tools/split_srd.py <path-to-dnd-5e-srd-markdown> srd/
"""
import re
import sys
import json
from pathlib import Path

SRC = Path(sys.argv[1])
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else "srd")

SPELL_TYPE = re.compile(r"^_(Level \d+ \w+|\w+ Cantrip) \(")
ITEM_TYPE = re.compile(r"^_.*(Common|Uncommon|Rare|Very Rare|Legendary|Artifact|Rarity Varies)(?![A-Za-z]).*_\s*$")


def slug(t):
    t = t.lower().replace("’", "").replace("'", "").replace('"', "")
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def read(name):
    text = (SRC / name).read_text(encoding="utf-8")
    return text.lstrip("﻿").splitlines(keepends=True)


def h2_starts(lines):
    return [i for i, l in enumerate(lines) if l.startswith("## ")]


def next_text(lines, i):
    for l in lines[i + 1:]:
        if l.strip():
            return l.strip()
    return ""


def by_h2(lines, folder, number=True, intro_name=None, merge=None):
    """One file per '## ' heading. Text before the first '## ' joins the first file.
    merge: {heading: heading-of-file-to-append-to} for small subsections."""
    starts = h2_starts(lines)
    merge = merge or {}
    pieces = []  # [name, start, end]
    for k, s in enumerate(starts):
        title = lines[s][3:].strip()
        e = starts[k + 1] if k + 1 < len(starts) else len(lines)
        if title in merge and pieces:
            pieces[-1][2] = e
            continue
        pieces.append([title, s, e])
    pieces[0][1] = 0
    files = []
    for n, (title, s, e) in enumerate(pieces, 1):
        name = f"{n:02d}-{slug(title)}.md" if number else f"{slug(title)}.md"
        files.append((f"{folder}/{name}", s, e))
    return files


def by_letter(lines, start, end, prefix, is_entry):
    """Group entries (detected by is_entry(lines, i)) by first letter."""
    entries = [i for i in range(start, end) if lines[i].startswith("#### ") and is_entry(lines, i)]
    groups = []
    for k, i in enumerate(entries):
        letter = re.sub(r"[^a-z]", "", lines[i][5:].lower())[:1]
        e = entries[k + 1] if k + 1 < len(entries) else end
        if groups and groups[-1][0] == letter:
            groups[-1][2] = e
        else:
            groups.append([letter, i, e])
    assert len({g[0] for g in groups}) == len(groups), "letters out of order"
    files = []
    if entries and entries[0] > start:
        files.append((f"{prefix}-00-introduction.md", start, entries[0]))
    files += [(f"{prefix}-{L}.md", s, e) for L, s, e in groups]
    return files


def spell_entry(lines, i):
    return bool(SPELL_TYPE.match(next_text(lines, i)))


def item_entry(lines, i):
    return bool(ITEM_TYPE.match(next_text(lines, i)))


def find(lines, heading):
    return next(i for i, l in enumerate(lines) if l.rstrip() == heading)


def main():
    plan = {}  # source file -> list of (out path, start, end)

    plan["playing-the-game.md"] = by_h2(read("playing-the-game.md"), "01-playing-the-game")
    plan["character-creation.md"] = by_h2(read("character-creation.md"), "02-character-creation")
    plan["classes.md"] = by_h2(read("classes.md"), "03-classes")
    plan["character-origins.md"] = by_h2(read("character-origins.md"), "04-character-origins")
    L = read("feats.md")
    plan["feats.md"] = [("05-feats/feats.md", 0, len(L))]
    plan["equipment.md"] = by_h2(read("equipment.md"), "06-equipment")

    # Spells: rules (matching the PDF's two bookmarks), then descriptions by letter
    L = read("spells.md")
    cs, sd = find(L, "## Casting Spells"), find(L, "## Spell Descriptions")
    plan["spells.md"] = [("07-spells/01-gaining-spells.md", 0, cs),
                         ("07-spells/02-casting-spells.md", cs, sd)] + \
        by_letter(L, sd, len(L), "07-spells/spells", spell_entry)

    L = read("rules-glossary.md")
    plan["rules-glossary.md"] = [("08-rules-glossary/rules-glossary.md", 0, len(L))]
    plan["gameplay-toolbox.md"] = by_h2(read("gameplay-toolbox.md"), "09-gameplay-toolbox")

    # Magic items: rules in two files, then A–Z by letter
    L = read("magic-items.md")
    r, az = find(L, "## Magic Item Rules"), find(L, "## Magic Items A–Z")
    plan["magic-items.md"] = [("10-magic-items/01-magic-item-categories.md", 0, r),
                              ("10-magic-items/02-magic-item-rules.md", r, az)] + \
        by_letter(L, az, len(L), "10-magic-items/items", item_entry)

    plan["monsters.md"] = by_h2(read("monsters.md"), "11-monsters")
    plan["monsters-A-Z.md"] = by_h2(read("monsters-A-Z.md"), "12-monsters-a-z", number=False)
    plan["animals.md"] = by_h2(read("animals.md"), "13-animals", number=False)

    # A–Z chapters: the chapter title lives in its own file, not glued to the first creature
    for src, folder in (("monsters-A-Z.md", "12-monsters-a-z"), ("animals.md", "13-animals")):
        L = read(src)
        first = h2_starts(L)[0]
        name, s, e = plan[src][0]
        plan[src][0] = (name, first, e)
        plan[src].insert(0, (f"{folder}/00-introduction.md", 0, first))

    index = []
    for src, files in plan.items():
        L = read(src)
        # integrity: contiguous, complete, exact
        pos = 0
        for name, s, e in files:
            assert s == pos, (src, name, s, pos)
            pos = e
        assert pos == len(L), (src, pos, len(L))
        assert "".join("".join(L[s:e]) for _, s, e in files) == "".join(L)
        for name, s, e in files:
            p = OUT / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("".join(L[s:e]), encoding="utf-8")
            heads = [l.strip("# \n") for l in L[s:e] if re.match(r"#{1,4} ", l)]
            index.append({"file": name, "source": src, "lines": [s + 1, e], "headings": heads})
    (OUT / "_tools" / "index.json").write_text(json.dumps(index, indent=1, ensure_ascii=False))
    print(len(index), "files written")


if __name__ == "__main__":
    main()
