"""Draw the skills grid (canon/brainstorm-progression.md) as PNG and SVG.

Usage: python3 canon/diagrams/skills_grid.py
Writes skills-grid.png and skills-grid.svg next to this script.

Edit TILES (populated nodes) and THEMES (fantasy themes, shown faintly)
as the grid is designed. Coordinates are axial (q, r); ring n is the set
of hexes at distance n from the centre.
"""
import math
import sys
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
from PIL import Image, ImageDraw, ImageFont

EMOJI = {"H": "\u2764\ufe0f", "S": "\u2b50", "M": "\U0001f4dc"}
EMOJI_FONT = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
TEXT_FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
_cache = {}

def emoji_img(key):
    if key not in _cache:
        f = ImageFont.truetype(EMOJI_FONT, 109)
        im = Image.new("RGBA", (136, 128), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((0, 0), EMOJI[key], font=f, embedded_color=True)
        _cache[key] = im.crop(im.getbbox())
    return _cache[key]

def render_line(text, px=60):
    """Render text with {H}/{S}/{M} emoji tokens to an RGBA image."""
    import re
    f = ImageFont.truetype(TEXT_FONT, px)
    parts = re.split(r"(\{[HSM]\})", text)
    pieces = []
    for part in parts:
        if not part:
            continue
        if re.fullmatch(r"\{[HSM]\}", part):
            e = emoji_img(part[1])
            h = int(px * 0.95)
            pieces.append(e.resize((int(e.width * h / e.height), h)))
        else:
            w = int(f.getlength(part)) + 2
            im = Image.new("RGBA", (w, int(px * 1.25)), (0, 0, 0, 0))
            ImageDraw.Draw(im).text((0, 0), part, font=f, fill=(0, 0, 0, 255))
            pieces.append(im)
    W = sum(p.width for p in pieces) + 4 * (len(pieces) - 1)
    H = int(px * 1.25)
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    x = 0
    for p in pieces:
        out.paste(p, (x, (H - p.height) // 2), p)
        x += p.width + 4
    return np.asarray(out)

def place_line(ax, x, y, text, zoom=0.105):
    ab = AnnotationBbox(OffsetImage(render_line(text), zoom=zoom), (x, y),
                        frameon=False, box_alignment=(0.5, 0.5), zorder=3)
    ax.add_artist(ab)
from matplotlib.patches import RegularPolygon

RINGS = 6
SIZE = 1.0  # hex circumradius

# Flat-topped hexes. Axial neighbour directions, in drawing order,
# assigned to the ring order Charisma, Dexterity, Strength, Constitution,
# Wisdom, Intelligence (Troy, 2026-11-07). Physical abilities on top,
# mental below.
DIRS = [(-1, 1), (-1, 0), (0, -1), (1, -1), (1, 0), (0, 1)]
ABILITIES = ["Cha", "Dex", "Str", "Con", "Wis", "Int"]
COLOURS = {  # light tints per wedge
    "Cha": "#f6d6e8", "Dex": "#d9eefc", "Str": "#fbd9cf",
    "Con": "#fbe9c6", "Wis": "#dff3d8", "Int": "#e6defa",
}
EDGE = {  # stronger tints for ring 1 borders
    "Cha": "#b0306f", "Dex": "#2a7ab8", "Str": "#b8432a",
    "Con": "#b07a12", "Wis": "#3a8a2e", "Int": "#5b3fb0",
}

def to_xy(q, r):
    x = SIZE * 1.5 * q
    y = SIZE * math.sqrt(3) * (r + q / 2)
    return x, -y  # screen y up

def dist(q, r):
    return max(abs(q), abs(r), abs(-q - r))

# Populated tiles: (q, r) -> (line1, line2, line3)
TILES = {(0, 0): ("All kits", "PB +2", "")}
# Line 3 symbols (Troy, 2026-11-07): HEART = Hit Die (hit points),
# STAR = stamina (SP), SCROLL = mana (MP). Written {H}, {S}, {M}.
KITS = {
    "Cha": ("Req Cha 13", "Herald Kit", "{H}d6 {S}4"),
    "Dex": ("Req Dex 13", "Scout Kit", "{H}d8 {S}4 +5ft"),
    "Str": ("Req Str 13", "Fighter Kit", "{H}d10 {S}2"),
    "Con": ("Req Con 13", "Tank Kit", "{H}d12"),
    "Wis": ("Req Wis 13", "Mystic Kit", "{H}d8 {M}4"),
    "Int": ("Req Int 13", "Mage Kit", "{H}d4 {M}5"),
}
SEAM_TILES = set()
# Technique tiles (Troy, 2026-11-09). Ring 2 positions: 201 is straight out
# from the Herald, 202 the Herald-Scout seam.
TECH_TILES = {
    # Technique names stay in the text, not on tiles (Troy, 2026-11-09).
    (-2, 2): ("", "Techniques", ""),
    (-2, 1): ("", "Techniques", ""),
}
for (dq, dr), ab in zip(DIRS, ABILITIES):
    TILES[(dq, dr)] = KITS[ab]
    # Damage Boost (Troy, 2026-11-07): ring 5, straight out from each kit,
    # except the Fighter's 511, moved to 510 and 614 (Troy, 2026-11-10).
    if ab != "Str":
        TILES[(5 * dq, 5 * dr)] = ("", "Attack Up", "")
    # Proficiency Bonus +1 (Troy, 2026-11-07): ring 4, on each seam.
    nq, nr = DIRS[(ABILITIES.index(ab) + 1) % 6]
    SEAM_TILES.add((2 * (dq + nq), 2 * (dr + nr)))
    TILES[(2 * (dq + nq), 2 * (dr + nr))] = ("", "Prof. Up", "")

# Fantasy themes for ring 2 (Troy, 2026-11-07). Ring 2 alternates:
# straight out from an ability hex (its middle), then between two
# ability hexes (their seam).
MIDDLE = {
    "Cha": ("Command", "Warlord", "Hexer"),
    "Dex": ("Archery", "Mobility", ""),
    "Str": ("Hit hard", "", ""),
    "Con": ("Hit points", "", ""),
    "Wis": ("Shaman", "Oracle", "Seer"),
    "Int": ("Wizard", "", ""),
}
SEAM = {  # seam between ABILITIES[i] and ABILITIES[i+1]
    ("Cha", "Dex"): ("Swashbuckler", "Rogue", "Deception"),
    ("Dex", "Str"): ("Fighting", "styles", "Manoeuvres"),
    ("Str", "Con"): ("Armour, AC", "(slow)", ""),
    ("Con", "Wis"): ("Monk", "Blood magic", ""),
    ("Wis", "Int"): ("Sage", "Alchemist", ""),
    ("Int", "Cha"): ("Summoner", "", ""),
}
THEMES = {}
for i, ab in enumerate(ABILITIES):
    dq, dr = DIRS[i]
    THEMES[(2 * dq, 2 * dr)] = (MIDDLE[ab], ab, None)
    nq, nr = DIRS[(i + 1) % 6]
    nxt = ABILITIES[(i + 1) % 6]
    THEMES[(dq + nq, dr + nr)] = (SEAM[(ab, nxt)], ab, nxt)
for h, t in TECH_TILES.items():
    THEMES.pop(h, None)
    TILES[h] = t
SEAM_TILES.add((-2, 1))  # 202 sits on a seam

def ring_hexes(n):
    """Hexes of ring n in numbering order: start at the corner straight
    out from Charisma, then go round in ring order (towards Dexterity)."""
    out = []
    for i in range(6):
        cq, cr = DIRS[i][0] * n, DIRS[i][1] * n
        sq = DIRS[(i + 1) % 6][0] - DIRS[i][0]
        sr = DIRS[(i + 1) % 6][1] - DIRS[i][1]
        for k in range(n):
            out.append((cq + sq * k, cr + sr * k))
    return out

# Tile numbers (Troy, 2026-11-07): ring number first, then position.
# Ring 1 is 11-16; rings 2-6 use two-digit positions (201-212 ... 601-636).
NUMBERS = {(0, 0): "0"}
for n in range(1, RINGS + 1):
    for i, h in enumerate(ring_hexes(n), start=1):
        NUMBERS[h] = f"{n}{i}" if n == 1 else f"{n}{i:02d}"

# Ring 2 Hit Dice (Troy, 2026-11-09).
HIT_DICE = {"201": "d6", "202": "d6", "203": "d8", "204": "d8", "205": "d10",
            "206": "d10", "207": "d12", "208": "d10", "209": "d8",
            "210": "d6", "211": "d4", "212": "d6"}
# Ring 2 stamina and mana (Troy, 2026-11-09).
POOLS = {"201": "{S}4",  # 4 from 2026-11-11 (was 3)
          "202": "{S}4", "203": "{S}4", "204": "{S}4",
         "205": "{S}2", "206": "{S}1", "208": "{M}2", "209": "{M}4",
         "210": "{M}4", "211": "{M}5", "212": "{M}2{S}2"}
LINE3 = {}  # (q, r) -> line 3 for themed tiles

# Ring 6 Damage Boosts on the seams (Troy, 2026-11-09).
BY_NUMBER = {v: k for k, v in NUMBERS.items()}
for num in ("510", "614"):  # the Fighter's boosts (Troy, 2026-11-10)
    TILES[BY_NUMBER[num]] = ("", "Attack Up", "")
for num in ("604", "610", "616", "622", "628", "634"):
    TILES[BY_NUMBER[num]] = ("", "Attack Up", "")
    SEAM_TILES.add(BY_NUMBER[num])
# Ring 6 Proficiency Bonus tiles straight out from each kit (Troy, 2026-11-09).
for num in ("601", "607", "613", "619", "625", "631"):
    TILES[BY_NUMBER[num]] = ("", "Prof. Up", "")
for num, hd in HIT_DICE.items():
    h = BY_NUMBER[num]
    l3 = "{H}" + hd + (" " + POOLS[num] if num in POOLS else "")
    if h in TILES:
        l1, l2, _ = TILES[h]
        TILES[h] = (l1, l2, l3)
    else:
        LINE3[h] = l3

# Hit Dice propagated straight out along the rays from ring 2 (Troy,
# 2026-11-10). Kit rays are straight hex lines (rings 3-6). Seam rays have
# an exact hex only on even rings (4 and 6); odd rings are left open.
RAY_TILES = {}
for i in range(6):
    dq, dr = DIRS[i]
    nq, nr = DIRS[(i + 1) % 6]
    corner_hd = HIT_DICE[NUMBERS[(2 * dq, 2 * dr)]]
    for k in range(3, RINGS + 1):
        RAY_TILES[(k * dq, k * dr)] = corner_hd
    seam_hd = HIT_DICE[NUMBERS[(dq + nq, dr + nr)]]
    for m in (2, 3):
        RAY_TILES[(m * (dq + nq), m * (dr + nr))] = seam_hd
for h, hd in RAY_TILES.items():
    if h in TILES:
        l1, l2, l3 = TILES[h]
        extra = l3
        TILES[h] = (l1, l2, "{H}" + hd + (" " + extra if extra else ""))
    else:
        TILES[h] = ("", "", "{H}" + hd)

# Hit Dice filled in tile by tile, Herald-Scout side (Troy, voice, 2026-11-11).
FILL_HD = {}
for num in ("302", "402", "502", "503", "504", "602", "603", "605"):
    FILL_HD[num] = "d6"
for num in ("303", "305", "404", "406", "505", "507", "508", "509",
            "606", "608", "609", "611"):
    FILL_HD[num] = "d8"
# d10, Fighter side (Troy, voice, 2026-11-11).
for num in ("306", "308", "408", "410", "510", "512", "513", "514",
            "612", "614", "615", "617"):
    FILL_HD[num] = "d10"
# Tank, Mystic and Mage sides (Troy, voice, 2026-11-11).
for hd, nums in (("d12", "309 412 515 618 311 414 517 620"),
                 ("d10", "518 621 519 623"),
                 ("d8", "312 416 520 624 314 418 522 626"),
                 ("d6", "524 629 523 627 633 528 529 635"),
                 ("d4", "315 420 525 630 317 422 527 632"),
                 ("d6", "318 424 530 636")):  # the last four (Troy, voice)
    for num in nums.split():
        assert num not in FILL_HD, num
        FILL_HD[num] = hd
for num, hd in FILL_HD.items():
    h = BY_NUMBER[num]
    assert h not in RAY_TILES, num
    if h in TILES:  # e.g. a Damage Boost tile: add the Hit Die to line 3
        l1, l2, l3 = TILES[h]
        TILES[h] = (l1, l2, "{H}" + hd + (" " + l3 if l3 else ""))
    else:
        TILES[h] = ("", "", "{H}" + hd)
# Mana and stamina beyond ring 2 (Troy, voice, 2026-11-11). The Mage
# wedge is the reference curve: 5 mana a tile. The Herald's line gets 4
# stamina a tile; the summoner seam (Int-Cha) mixes the two.
MORE_POOLS = {}
for num in "315 316 317 420 421 422 524 525 526 527 629 630 631 632".split():
    MORE_POOLS[num] = "{M}5"
for num in ("423", "634"):
    MORE_POOLS[num] = "{M}2{S}2"
for num in ("528", "633"):
    MORE_POOLS[num] = "{M}4{S}1"
for num in ("529", "635"):
    MORE_POOLS[num] = "{M}1{S}3"
for num in "301 401 501 601 318 424 530 636".split():
    MORE_POOLS[num] = "{S}4"
# Mystic wedge, Wis-Int seam and the Tank's mana edge (Troy, voice, 2026-11-11).
for num in "312 313 314 416 417 418 519 520 521 522 523 623 624 625 626 627 419 628".split():
    MORE_POOLS[num] = "{M}4"
for num in "415 622 518 621".split():
    MORE_POOLS[num] = "{M}2"
for num in "311 414 517 620".split():
    MORE_POOLS[num] = "{M}1"
# Stamina, Herald-Scout-Fighter side (Troy, voice, 2026-11-11). Ring 2:
# 202-204 raised to 4, 206 lowered to 1 (in POOLS above).
for num in "302 402 502 602 503 603 403 604".split():  # Herald side of the seam
    MORE_POOLS[num] = "{S}4"
for num in ("303 304 305 404 405 406 504 505 506 507 508 "
            "605 606 607 608 609 407 610").split():   # Scout wedge and Fighter seam
    MORE_POOLS[num] = "{S}4"
for num in "306 307 308 408 409 410 510 511 512 513 612 613 614 615".split():
    MORE_POOLS[num] = "{S}2"                        # Fighter wedge
for num in ("509", "611"):                          # Fighter, next to the Scout
    MORE_POOLS[num] = "{S}3"
for num in "411 616 514 617".split():               # heavy-armour seam, Tank edge
    MORE_POOLS[num] = "{S}1"
for num, pool in MORE_POOLS.items():
    h = BY_NUMBER[num]
    l1, l2, l3 = TILES[h]
    TILES[h] = (l1, l2, l3 + " " + pool)
# Tile names (Troy, voice, 2026-11-11). Only kit tiles keep a prerequisite
# on the top line; elsewhere the top line is the tile's look-up name. Ring 3
# names the subclass fantasies; each gets a "II" tile straight out on ring 6.
RING3_NAMES = {"301": "Warlord", "302": "Tactician", "303": "Rogue",
               "304": "Ranger", "305": "Skirmisher", "306": "Virtuoso",
               "307": "Champion", "308": "Brute", "309": "Bulwark",
               "310": "Juggernaut", "311": "Blood Mage", "312": "Shaman",
               "313": "Oracle", "314": "Sage", "315": "Alchemist",
               "316": "Wizard", "317": "Summoner", "318": "Hexer"}
for num, name in RING3_NAMES.items():
    q, r = BY_NUMBER[num]
    for h, label in (((q, r), name), ((2 * q, 2 * r), name + " II")):
        _, l2, l3 = TILES[h]
        TILES[h] = (label, l2, l3)
# Ring 2 names (Troy, voice, 2026-11-11): kit lines are "<Kit> II"; seams
# evoke the two ring-3 subclasses beyond them, and carry on as II (ring 4)
# and III (ring 6) along the seam rays.
RING2_NAMES = {"201": "Herald II", "202": "Cunning", "203": "Scout II",
               "204": "Precision", "205": "Fighter II", "206": "Might",
               "207": "Tank II", "208": "Vitality", "209": "Mystic II",
               "210": "Lore", "211": "Mage II", "212": "Control"}
SEAM_NAMES = {"202", "204", "206", "208", "210", "212"}
def name_tile(h, label):
    if h in TILES:
        _, l2, l3 = TILES[h]
    else:
        l2, l3 = "", LINE3.pop(h, "")
    TILES[h] = (label, l2, l3)
for num, name in RING2_NAMES.items():
    q, r = BY_NUMBER[num]
    name_tile((q, r), name)
    if num in SEAM_NAMES:
        name_tile((2 * q, 2 * r), name + " II")
        name_tile((3 * q, 3 * r), name + " III")
print("ring 6 II tiles:", " ".join(NUMBERS[(2 * BY_NUMBER[n][0], 2 * BY_NUMBER[n][1])] for n in RING3_NAMES))
NOPOOL = sorted((NUMBERS[h] for h in NUMBERS if h != (0, 0) and "{S}" not in
                 (TILES.get(h, ("", "", LINE3.get(h, "")))[2]) and "{M}" not in
                 (TILES.get(h, ("", "", LINE3.get(h, "")))[2])), key=int)
print("no stamina or mana:", " ".join(NOPOOL))
EMPTY = sorted(NUMBERS[h] for h in NUMBERS if h not in TILES and h not in LINE3 and h != (0, 0))
print("no Hit Die yet:", " ".join(EMPTY))

def wedge(q, r):
    """Nearest ability direction by angle, or None for the centre."""
    if (q, r) == (0, 0):
        return None
    x, y = to_xy(q, r)
    ang = math.atan2(y, x)
    best, bd = None, 9
    for (dq, dr), ab in zip(DIRS, ABILITIES):
        ax, ay = to_xy(dq, dr)
        d = abs((math.atan2(ay, ax) - ang + math.pi) % (2 * math.pi) - math.pi)
        if d < bd - 1e-6:
            best, bd = ab, d
    return best

# Print mode (Troy, 2026-11-11): python3 skills_grid.py --print
# White faces, black outlines, light grey for special tiles; writes a
# letter-size PDF, skills-grid-print.pdf.
PRINT = "--print" in sys.argv

fig, ax = plt.subplots(figsize=(11, 12.4))
ax.set_aspect("equal")
ax.axis("off")

for q in range(-RINGS, RINGS + 1):
    for r in range(-RINGS, RINGS + 1):
        n = dist(q, r)
        if n > RINGS:
            continue
        x, y = to_xy(q, r)
        ab = wedge(q, r)
        face, edge, lw = "white", "#c8c8c8", 0.6
        if n == 1:
            face, edge, lw = COLOURS[ab], EDGE[ab], 2.2
        elif (q, r) in THEMES:
            _, a1, a2 = THEMES[(q, r)]
            face = COLOURS[a1] if a2 is None else "#f3f3f3"
            edge, lw = "#9a9a9a", 0.9
        elif n == 0:
            face, edge, lw = "#fffbe8", "#555555", 2.2
        elif (q, r) in SEAM_TILES:
            face, edge, lw = "#ececec", "#444444", 1.8
        elif (q, r) in TILES:
            face, edge, lw = COLOURS[ab], EDGE[ab], (1.8 if TILES[(q, r)][1] else 1.0)
        if PRINT:
            if n == 0 or (q, r) in SEAM_TILES:
                face = "#e6e6e6"
            elif (q, r) in THEMES and THEMES[(q, r)][2] is not None:
                face = "#f3f3f3"
            else:
                face = "white"
            if n <= 1 or (q, r) in TILES or (q, r) in SEAM_TILES or (q, r) in THEMES:
                edge, lw = "black", max(lw, 1.2)
            else:
                edge, lw = "#888888", 0.6
        ax.add_patch(RegularPolygon((x, y), 6, radius=SIZE * 0.97,
                                    orientation=math.pi / 6,
                                    facecolor=face, edgecolor=edge, lw=lw))
        busy = (q, r) in TILES or (q, r) in THEMES
        if busy:  # small number at the foot of a filled tile
            ax.text(x, y - 0.68, NUMBERS[(q, r)], ha="center", va="center",
                    fontsize=5.6, weight="bold", color="#555555" if PRINT else "#8a8a8a", zorder=3)
        else:     # large grey number in an empty tile
            ax.text(x, y, NUMBERS[(q, r)], ha="center", va="center",
                    fontsize=11, weight="bold", color="#9a9a9a" if PRINT else "#c4c4c4", zorder=2)
        if (q, r) in TILES:
            l1, l2, l3 = TILES[(q, r)]
            if l1 and not l1.startswith("Req") and (q, r) != (0, 0):
                # Top line: the tile's look-up name (Troy, 2026-11-11).
                ax.text(x, y + 0.36, l1, ha="center", va="center",
                        fontsize=7.4 if len(l1) <= 9 else (6.2 if len(l1) <= 11 else 5.4),
                        weight="bold", zorder=3)
                ax.text(x, y, l2, ha="center", va="center", fontsize=6.8, zorder=3)
            else:
                ax.text(x, y + 0.36, l1, ha="center", va="center", fontsize=6.6, color="#444", zorder=3)
                ax.text(x, y, l2, ha="center", va="center", fontsize=7.6 if len(l2) <= 10 else (5.9 if PRINT else 6.6), weight="bold", zorder=3)
            if "{" in l3:
                place_line(ax, x, y - 0.36, l3)
            else:
                ax.text(x, y - 0.36, l3, ha="center", va="center", fontsize=6.9, zorder=3)
        elif (q, r) in THEMES:
            # Fantasy themes are drawn outside ring 6 (Troy, 2026-11-09).
            if (q, r) in LINE3:
                place_line(ax, x, y - 0.36, LINE3[(q, r)])

# Ability labels outside the grid
for (dq, dr), ab in zip(DIRS, ABILITIES):
    x, y = to_xy(dq * (RINGS + 1.55), dr * (RINGS + 1.55))
    name = {"Cha": "CHARISMA", "Dex": "DEXTERITY", "Str": "STRENGTH",
            "Con": "CONSTITUTION", "Wis": "WISDOM", "Int": "INTELLIGENCE"}[ab]
    ax.text(x, y, name, ha="center", va="center", fontsize=11, weight="bold", color="black" if PRINT else EDGE[ab])

# Fantasy themes outside ring 6 (Troy, 2026-11-09): each kit's middle
# theme under its ability name, each seam's theme beyond the ring's side.
for i, ab in enumerate(ABILITIES):
    dq, dr = DIRS[i]
    x, y = to_xy(dq * (RINGS + 1.55), dr * (RINGS + 1.55))
    ax.text(x, y - 0.45, ", ".join(s for s in MIDDLE[ab] if s), ha="center",
            va="center", fontsize=7.5, style="italic", color="#555")
    nq, nr = DIRS[(i + 1) % 6]
    nxt = ABILITIES[(i + 1) % 6]
    f = (RINGS + 2.5) / 2
    x, y = to_xy((dq + nq) * f, (dr + nr) * f)
    ax.text(x, y, "\n".join(s for s in SEAM[(ab, nxt)] if s), ha="center",
            va="center", fontsize=7.5, style="italic", color="#555")

lim = SIZE * (RINGS * 1.5 + 3.4)
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim - 3.2, lim + 2.4)
title = "Azhi: the Skills Grid (print, 2026-11-11)" if PRINT else "Azhi: the Skills Grid (draft, 2026-11-07)"
ax.text(0, lim + 2.0, title, ha="center",
        va="center", fontsize=15, weight="bold")
ax.text(0, -lim - 2.0,
        "Centre and ring 1: populated (Req / name / what adds up).  Ring 2: 201-202 technique tiles.  Italic labels outside the grid: fantasy themes.\n"
        "Prof. Up (Proficiency Bonus +1): ring 4 seams and ring 6 corners.  Attack Up (Damage Boost): rings 5 and 6.  Every tile has a Hit Die.  127 hexes in all.  PROPOSED design; see canon/brainstorm-progression.md.",
        ha="center", va="center", fontsize=8, color="#444")
place_line(ax, 0, -lim - 2.6, "{H} Hit Die     {S} stamina (SP)     {M} mana (MP)", zoom=0.14)

here = os.path.dirname(os.path.abspath(__file__))
if PRINT:
    raw = os.path.join(here, "skills-grid-print-raw.pdf")
    fig.savefig(raw, bbox_inches="tight", pad_inches=0.1, dpi=600)
    from pypdf import PdfReader, PdfWriter, Transformation
    page = PdfReader(raw).pages[0]
    w, h = float(page.mediabox.width), float(page.mediabox.height)
    W, H, M = 612, 792, 27  # US Letter, 3/8 inch margin
    k = min((W - 2 * M) / w, (H - 2 * M) / h)
    out = PdfWriter()
    blank = out.add_blank_page(W, H)
    page.add_transformation(Transformation().scale(k).translate((W - w * k) / 2, (H - h * k) / 2))
    blank.merge_page(page)
    out.write(os.path.join(here, "skills-grid-print.pdf"))
    os.remove(raw)
    print("ok print")
    sys.exit()
fig.savefig(os.path.join(here, "skills-grid.png"), dpi=200, bbox_inches="tight")
fig.savefig(os.path.join(here, "skills-grid.svg"), bbox_inches="tight")
print("ok")
