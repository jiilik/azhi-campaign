"""Draw the skills grid (canon/brainstorm-progression.md) as PNG and SVG.

Usage: python3 canon/diagrams/skills_grid.py
Writes skills-grid.png and skills-grid.svg next to this script.

Edit TILES (populated nodes) and THEMES (fantasy themes, shown faintly)
as the grid is designed. Coordinates are axial (q, r); ring n is the set
of hexes at distance n from the centre.
"""
import math
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
                        frameon=False, box_alignment=(0.5, 0.5))
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
TILES = {(0, 0): ("All kits", "PB +2", "Simple wpns")}
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
for (dq, dr), ab in zip(DIRS, ABILITIES):
    TILES[(dq, dr)] = KITS[ab]

# Fantasy themes for ring 2 (Troy, 2026-11-07). Ring 2 alternates:
# straight out from an ability hex (its middle), then between two
# ability hexes (their seam).
MIDDLE = {
    "Cha": ("Command", "Warlord", "Hexer"),
    "Dex": ("Movement", "In and out", ""),
    "Str": ("Hit hard", "", ""),
    "Con": ("Hit points", "", ""),
    "Wis": ("Shaman", "Oracle", "Seer"),
    "Int": ("Wizard", "", ""),
}
SEAM = {  # seam between ABILITIES[i] and ABILITIES[i+1]
    ("Cha", "Dex"): ("Swashbuckler", "Rogue", "Assassin"),
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
        ax.add_patch(RegularPolygon((x, y), 6, radius=SIZE * 0.97,
                                    orientation=math.pi / 6,
                                    facecolor=face, edgecolor=edge, lw=lw))
        if (q, r) in TILES:
            l1, l2, l3 = TILES[(q, r)]
            ax.text(x, y + 0.36, l1, ha="center", va="center", fontsize=6.6, color="#444")
            ax.text(x, y, l2, ha="center", va="center", fontsize=7.6, weight="bold")
            if "{" in l3:
                place_line(ax, x, y - 0.36, l3)
            else:
                ax.text(x, y - 0.36, l3, ha="center", va="center", fontsize=6.9)
        elif (q, r) in THEMES:
            lines = [s for s in THEMES[(q, r)][0] if s]
            k = len(lines)
            for j, s in enumerate(lines):
                ax.text(x, y + 0.3 * ((k - 1) / 2 - j), s, ha="center", va="center",
                        fontsize=5.7, style="italic", color="#555")

# Ability labels outside the grid
for (dq, dr), ab in zip(DIRS, ABILITIES):
    x, y = to_xy(dq * (RINGS + 0.9), dr * (RINGS + 0.9))
    name = {"Cha": "CHARISMA", "Dex": "DEXTERITY", "Str": "STRENGTH",
            "Con": "CONSTITUTION", "Wis": "WISDOM", "Int": "INTELLIGENCE"}[ab]
    ax.text(x, y, name, ha="center", va="center", fontsize=11, weight="bold", color=EDGE[ab])

lim = SIZE * (RINGS * 1.5 + 2.6)
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim - 2.6, lim + 1.8)
ax.text(0, lim + 1.3, "Azhi: the Skills Grid (draft, 2026-11-07)", ha="center",
        va="center", fontsize=15, weight="bold")
ax.text(0, -lim - 1.4,
        "Centre and ring 1: populated (Req / name / what adds up).  Ring 2, italic: fantasy themes only, not yet nodes.\n"
        "Rings 3-6: empty.  127 hexes in all.  PROPOSED design; see canon/brainstorm-progression.md.",
        ha="center", va="center", fontsize=8, color="#444")
place_line(ax, 0, -lim - 2.0, "{H} Hit Die     {S} stamina (SP)     {M} mana (MP)", zoom=0.14)

here = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(here, "skills-grid.png"), dpi=200, bbox_inches="tight")
fig.savefig(os.path.join(here, "skills-grid.svg"), bbox_inches="tight")
print("ok")
