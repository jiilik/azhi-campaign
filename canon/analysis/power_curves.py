"""Power curves for the two-wheel progression (Troy, 2026-11-12).

12 archetypes (6 kits, 6 seam hybrids) x 3 strategies (grid only, species
first, even split), levels 1-12, phasing at levels 5 and 10. Writes
power-curves.md (tables) and power-curves.png (small multiples).

Model (simple, PROPOSED):
- Level 1: the kit tile and species ring 1 (the base form, no Hit Die).
- Each level-up: one point, on the grid or the species wheel (rings 2-6).
- Phasing at 5 and 10 (after that level's point): the character loses one
  species ring (Troy, 2026-11-12; was halving) and reinvests the rest in the
  new colour. The new
  colour is modelled with the same numbers, so only the halving shows. Lost
  rings take their Hit Dice, pools and bonuses with them.
- Hit points: the kit's die in full at level 1, then the SRD fixed value
  (die/2 + 1) per Hit Die. Constitution is ignored.
- The grid path: the best-valued connected set inside the archetype's
  wedges (moves outward only), taken highest-value-first. Tile value for
  choosing only: HP + 2 x mana + stamina + 8 per ability +1 + 10 Prof. Up
  + 12 Attack Up.
"""
import io, os, sys, math, re, contextlib
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

HERE = os.path.dirname(os.path.abspath(__file__))
DIAG = os.path.join(os.path.dirname(HERE), "diagrams")
sys.argv = ["x"]
import matplotlib
matplotlib.use("Agg")
src = open(os.path.join(DIAG, "skills_grid.py")).read().split("fig, ax = plt.subplots")[0]
G = {}
with contextlib.redirect_stdout(io.StringIO()):
    exec(src, G)
NUMBERS, BY_NUMBER, TILES, LINE3, DIRS = G["NUMBERS"], G["BY_NUMBER"], G["TILES"], G["LINE3"], G["DIRS"]
dist, wedge = G["dist"], G["wedge"]

W_ABIL, W_PROF, W_ATK = 8, 10, 12


def tile_stats(h):
    l1, l2, l3 = TILES.get(h, ("", "", LINE3.get(h, "")))
    d = re.search(r"\{H\}d(\d+)", l3)
    m = re.search(r"\{M\}(\d+)", l3)
    s = re.search(r"\{S\}(\d+)", l3)
    return dict(hd=int(d.group(1)) if d else 0, mana=int(m.group(1)) if m else 0,
                stam=int(s.group(1)) if s else 0, abil=int(bool(re.search(r"[A-Z][a-z]{2} \+1", l2))),
                prof=int("Prof. Up" in l2), atk=int("Attack Up" in l2))


def value(st, first=False):
    hp = st["hd"] if first else st["hd"] / 2 + 1
    return hp + 2 * st["mana"] + st["stam"] + W_ABIL * st["abil"] + W_PROF * st["prof"] + W_ATK * st["atk"]


KITS = {"Herald": ("Cha", "11"), "Scout": ("Dex", "12"), "Fighter": ("Str", "13"),
        "Tank": ("Con", "14"), "Mystic": ("Wis", "15"), "Mage": ("Int", "16")}
HYBRIDS = {"Cunning": ("Herald", "Scout", "202"), "Precision": ("Scout", "Fighter", "204"),
           "Might": ("Fighter", "Tank", "206"), "Vitality": ("Tank", "Mystic", "208"),
           "Lore": ("Mystic", "Mage", "210"), "Control": ("Mage", "Herald", "212")}
COLOUR = {"Herald": "Indigo", "Scout": "Blue", "Fighter": "Red", "Tank": "Brown", "Mystic": "White",
          "Mage": "Black", "Cunning": "Blue", "Precision": "Green", "Might": "Brown",
          "Vitality": "Green", "Lore": "Grey", "Control": "Black"}
# Species wheel per arc, rings 2-6 (from art/cartoon/species_advancement.py)
SP_HD = {"Red": 10, "Brown": 12, "Yellow": 8, "Green": 8, "Blue": 6, "Indigo": 6, "Black": 6, "Grey": 6, "White": 8}
SP_POOL = {"Red": (0, 3), "Brown": (1, 1), "Yellow": (3, 1), "Green": (2, 2), "Blue": (2, 2),
           "Indigo": (2, 2), "Black": (4, 0), "Grey": (4, 0), "White": (3, 1)}


def species_ring(colour, k):
    m, s = SP_POOL[colour]
    return dict(hd=SP_HD[colour], mana=m, stam=s, abil=int(k == 4), prof=int(k == 3), atk=int(k == 6))


def grid_order(name, n=12):
    """Best n-tile connected set in the archetype's region, then ordered."""
    if name in KITS:
        abil, kit = KITS[name]
        region = {h for h in NUMBERS if h != (0, 0) and wedge(*h) == abil}
        kits, must = [BY_NUMBER[kit]], None
    else:
        a, b, seam = HYBRIDS[name]
        abs_ = {KITS[a][0], KITS[b][0]}
        region = {h for h in NUMBERS if h != (0, 0) and wedge(*h) in abs_} | {BY_NUMBER[seam]}
        kits, must = [BY_NUMBER[KITS[a][1]], BY_NUMBER[KITS[b][1]]], BY_NUMBER[seam]
    tiles = [h for h in region if dist(*h) >= 1]
    tiles = [h for h in tiles if dist(*h) > 1 or h in kits]
    idx = {h: i for i, h in enumerate(tiles)}
    N = len(tiles)
    A, lb, ub = [], [], []
    for h in tiles:
        if dist(*h) == 1:
            continue
        row = np.zeros(N); row[idx[h]] = 1
        for dq, dr in DIRS:
            p = (h[0] + dq, h[1] + dr)
            if p in idx and dist(*p) == dist(*h) - 1:
                row[idx[p]] -= 1
        A.append(row); lb.append(-np.inf); ub.append(0)
    row = np.zeros(N)
    for k in kits: row[idx[k]] = 1
    A.append(row); lb.append(1); ub.append(1)          # exactly one starting kit
    A.append(np.ones(N)); lb.append(n); ub.append(n)
    if must is not None:
        row = np.zeros(N); row[idx[must]] = 1; A.append(row); lb.append(1); ub.append(1)
    c = -np.array([value(tile_stats(h), first=(dist(*h) == 1)) for h in tiles])
    r = milp(c, constraints=LinearConstraint(np.array(A), lb, ub), integrality=np.ones(N), bounds=Bounds(0, 1))
    chosen = {tiles[i] for i in range(N) if r.x[i] > 0.5}
    order, have = [], set()
    while len(order) < n:
        avail = [h for h in chosen - have if dist(*h) == 1 or any(
            (h[0] + dq, h[1] + dr) in have and dist(h[0] + dq, h[1] + dr) == dist(*h) - 1 for dq, dr in DIRS)]
        h = max(avail, key=lambda t: (value(tile_stats(t), dist(*t) == 1), -dist(*t)))
        order.append(h); have.add(h)
    return order


def simulate(name, strategy, levels=12, phases=(5, 10)):
    colour = COLOUR[name]
    order = grid_order(name, levels)
    g, sp, rows = 1, 0, []          # grid tiles taken, species rings beyond ring 1
    for L in range(1, levels + 1):
        if L > 1:
            if strategy == "grid only":
                g += 1
            elif strategy == "species first":
                if sp < 5: sp += 1
                else: g += 1
            else:  # even split: alternate, species on even levels
                if L % 2 == 0 and sp < 5: sp += 1
                else: g += 1
        if L in phases:
            sp = max(0, sp - 1)
        stats = [tile_stats(h) for h in order[:g]]
        hp = order and tile_stats(order[0])["hd"]
        hp += sum(s["hd"] / 2 + 1 for s in stats[1:])
        sps = [species_ring(colour, k) for k in range(2, 2 + sp)]
        hp += sum(s["hd"] / 2 + 1 for s in sps)
        tot = lambda key: sum(s[key] for s in stats + sps)
        rows.append(dict(level=L, grid=g, species=sp, points=g + sp, hp=hp, mana=tot("mana"), stam=tot("stam"),
                         abil=tot("abil"), prof=tot("prof"), atk=tot("atk")))
    return rows, order


ARCH = list(KITS) + list(HYBRIDS)
FINDINGS = ["", "## Findings (Claude, 2026-11-12, one ring lost per phase)", "",
    "1. **A gentle penalty.** With a phase every five levels, species-first and even-split characters hold **10 of 12** points at level 12 (grid-only keeps 12). Under the earlier halving rule they held 8 and 9.",
    "2. **Hit points barely move on a phase:** the level's new point offsets the lost ring. At worst they dip by 1 (for example a Mage taking a d4 grid tile the level it loses a d6 ring).",
    "3. **Bonuses keep pace:** by level 12, species investors have about the same ability +1s and Prof. Ups as grid-only builds; they trail mainly in Attack Up (usually 1 against 2).",
    "4. **The penalty no longer depends on how much you invested:** losing one ring costs everyone the same, so party members who phase at different times stay within a couple of points of each other.",
    "5. **Archetypes look alike in shape**; the differences are Hit Die size. The Mage line is the thinnest (39 HP at 12 grid-only, against a 2024 wizard's 50 without Con).", ""]
STRATS = ["grid only", "species first", "even split"]

if __name__ == "__main__":
    R = {(a, s): simulate(a, s) for a in ARCH for s in STRATS}
    out = ["# Power curves: grid vs species wheel, with phasing (PROPOSED analysis, 2026-11-12)", "",
           "Generated by `power_curves.py`; the model and its assumptions are in that file's docstring.",
           "Phases at levels **5** and **10** (one species ring lost each time). Rows show the state **after** that level's phase.",
           "HP excludes Constitution. **+1s** = ability increases, **PU** = Prof. Up, **AU** = Attack Up. "
           "**Pts** = points still held (level 12 has 12 if nothing was lost).", ""]
    for a in ARCH:
        kind = "kit" if a in KITS else "hybrid"
        out.append(f"## {a} ({kind}, {COLOUR[a]})")
        path = " → ".join(NUMBERS[h] for h in R[(a, STRATS[0])][1])
        out.append(f"Grid path (grid only, in order): {path}")
        out.append("")
        out.append("| Strategy | L4 HP / ◆ / ★ / +1s / PU / AU / Pts | L5 (phased) | L9 | L10 (phased) | L12 |")
        out.append("|---|---|---|---|---|---|")
        for s in STRATS:
            rows = R[(a, s)][0]
            cell = lambda r: f'{r["hp"]:.0f} / {r["mana"]} / {r["stam"]} / {r["abil"]} / {r["prof"]} / {r["atk"]} / {r["points"]}'
            out.append(f"| {s} | " + " | ".join(cell(rows[L - 1]) for L in (4, 5, 9, 10, 12)) + " |")
        out.append("")
    # Summary: points lost by level 12, and HP gap at 10
    out.append("## Summary at level 12")
    out.append("")
    out.append("| Archetype | Pts held (grid only / species first / even) | HP | +1s | Prof. Up | Attack Up |")
    out.append("|---|---|---|---|---|---|")
    for a in ARCH:
        r = [R[(a, s)][0][-1] for s in STRATS]
        f = lambda k, fmt="{:.0f}": " / ".join(fmt.format(x[k]) for x in r)
        out.append(f"| {a} | {f('points')} | {f('hp')} | {f('abil')} | {f('prof')} | {f('atk')} |")
    out += FINDINGS
    open(os.path.join(HERE, "power-curves.md"), "w").write("\n".join(out) + "\n")

    import matplotlib.pyplot as plt
    COL = {"grid only": "#2a78d6", "species first": "#eb6834", "even split": "#1baf7a"}
    fig, axs = plt.subplots(3, 4, figsize=(15, 10.5), sharex=True)
    for ax, a in zip(axs.flat, ARCH):
        for s in STRATS:
            rows = R[(a, s)][0]
            ax.plot([r["level"] for r in rows], [r["hp"] for r in rows], color=COL[s], lw=2, label=s)
        for L in (5, 10):
            ax.axvline(L, color="#c3c2b7", lw=1, ls=":")
        ax.set_title(f"{a} ({COLOUR[a]})", fontsize=11, loc="left")
        ax.grid(axis="y", color="#e6e5e0", lw=0.6)
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
        ax.tick_params(labelsize=8, colors="#52514e")
    for ax in axs[-1]:
        ax.set_xlabel("level", fontsize=9, color="#52514e")
    for ax in axs[:, 0]:
        ax.set_ylabel("hit points (no Con)", fontsize=9, color="#52514e")
    fig.legend(*axs.flat[0].get_legend_handles_labels(), loc="upper center", bbox_to_anchor=(0.5, 0.965), ncol=3, frameon=False, fontsize=10)
    fig.suptitle("Hit points by level; dotted lines mark phasing at levels 5 and 10", y=0.995, fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(os.path.join(HERE, "power-curves.png"), dpi=150)
    print("ok")
