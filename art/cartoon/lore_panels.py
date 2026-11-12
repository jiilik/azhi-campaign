"""Five lore panels: dragonborn adventurers visiting Azhi's history (2026-11-11).

-> output/lore_1_bones.png ... output/lore_5_campfire.png, and output/lore_panels.png (all
five on one sheet). Saturday-Morning Bold. The epochs are PROPOSED lore
(canon/brainstorm-epochs.md); the myth is canon. Only dragonborn appear as people.
"""
import os, sys, math, random, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE); sys.path.insert(0, HERE)
import colour_wheel  # noqa: F401  (adds Brown, Yellow, Indigo and Grey to the palette)
import party
from party import (STYLES, figure, glow, light, dark, P, col, circ, limb, sky, ring_arch,
                   sky_dragon, cloud, ridge, poly, wave, FANG, defs)

st = STYLES['bold']
INK = st['line']
BONE, BONE_SH = '#efe4c9', '#cbbd99'


def team(members, gy, base=2.1):
    return ''.join(figure(x, gy + (5 if i % 2 else 0), base * k, d, r, o, a, st, flip=f)
                   for i, (x, d, r, o, a, f, k) in enumerate(members))


def caption(title, line):
    w = max(len(title) * 21, len(line) * 11.2) + 40
    return (f'<rect x="24" y="22" width="{w:.0f}" height="86" rx="14" fill="#fbf4e3" stroke="{INK}" stroke-width="4"/>'
            f'<text x="44" y="60" font-family="DejaVu Serif" font-weight="bold" font-size="34" fill="{INK}">{title}</text>'
            f'<text x="44" y="92" font-family="DejaVu Sans" font-style="italic" font-size="19" fill="#4a4036">{line}</text>')


def rib(x, yb, h, span, w=34):
    """A giant bone arch rising from the ground."""
    d = f'M {x},{yb} C {x - 10},{yb - h} {x + span + 10},{yb - h} {x + span},{yb}'
    return (f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w + 8}" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="{BONE}" stroke-width="{w}" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="{BONE_SH}" stroke-width="{w * 0.3}" stroke-linecap="round" '
            f'transform="translate(4,6)" opacity=".7"/>')


def gear(cx, cy, r, teeth, fill, rot=0):
    pts = []
    for i in range(teeth * 4):
        a = math.radians(rot + i * 360 / (teeth * 4))
        rr = r if (i % 4) in (0, 1) else r * 0.84
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d = 'M ' + ' L '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + ' Z'
    o = P(d, fill, st, bg=True)
    o += circ(cx, cy, r * 0.62, dark(fill, .12), dict(st, stroke=3))
    o += circ(cx, cy, r * 0.2, dark(fill, .35), dict(st, stroke=3))
    for k in range(5):
        a = math.radians(rot + k * 72)
        o += (f'<line x1="{cx + r * .2 * math.cos(a):.1f}" y1="{cy + r * .2 * math.sin(a):.1f}" '
              f'x2="{cx + r * .6 * math.cos(a):.1f}" y2="{cy + r * .6 * math.sin(a):.1f}" stroke="{INK}" stroke-width="5"/>')
    return o


def vine(pts, w=7):
    return limb(pts, w, '#4f8f3a', st)


def column(x, yb, h, w=70, broken=False):
    top = yb - h
    if broken:
        d = (f'M {x},{yb} L {x},{top + 14} L {x + w * .3},{top} L {x + w * .5},{top + 22} '
             f'L {x + w * .75},{top + 6} L {x + w},{top + 28} L {x + w},{yb} Z')
        o = P(d, '#e3d9c4', st, bg=True)
    else:
        o = P(f'M {x},{yb} L {x},{top} L {x + w},{top} L {x + w},{yb} Z', '#e3d9c4', st, bg=True)
        o += P(f'M {x - 14},{top} L {x - 14},{top - 24} L {x + w + 14},{top - 24} L {x + w + 14},{top} Z', '#d6cbb2', st, bg=True)
    for k in (0.3, 0.55, 0.8):
        o += f'<line x1="{x + w * k:.1f}" y1="{yb - 4}" x2="{x + w * k:.1f}" y2="{top + 30}" stroke="#b9ad92" stroke-width="4"/>'
    return o


def eggshell(cx, yb, rw, rh, fill, speck, seed, lean=0):
    """Lower half of a giant cracked egg, with a zigzag rim."""
    rnd = random.Random(seed)
    top = yb - rh
    n = 9
    zig = []
    for i in range(n + 1):
        x = cx - rw + 2 * rw * i / n
        y = top + (0 if i % 2 else rnd.uniform(28, 55))
        zig.append((x, y))
    d = f'M {cx - rw},{top + 30} '
    d += ' '.join(f'L {x:.1f},{y:.1f}' for x, y in zig)
    d += f' C {cx + rw},{yb - rh * 0.2} {cx + rw * 0.6},{yb} {cx},{yb} C {cx - rw * 0.6},{yb} {cx - rw},{yb - rh * 0.2} {cx - rw},{top + 30} Z'
    o = f'<g transform="rotate({lean},{cx},{yb})">' + P(d, fill, st, bg=True)
    for _ in range(14):
        x = cx + rnd.uniform(-rw * .75, rw * .75); y = yb - rnd.uniform(18, rh * .8)
        o += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rnd.uniform(6, 13):.0f}" ry="{rnd.uniform(4, 9):.0f}" fill="{speck}" opacity=".8"/>'
    o += f'<path d="M {cx - rw * .55},{yb - rh * .55} Q {cx - rw * .7},{yb - rh * .2} {cx - rw * .35},{yb - 18}" fill="none" stroke="#ffffff" stroke-width="9" opacity=".45" stroke-linecap="round"/>'
    return o + '</g>'


# ---------- the five scenes ----------
def scene_bones():
    b = sky(['#5fb2ea', '#9fd3f2', '#fff0c8'], st, 0, 620)
    b += ring_arch('M -80,520 Q 520,-120 1300,60', 34, st, op=.6)
    b += sky_dragon(980, 150, 0.9, '#ffc93c', '#ffd25a', st, flip=-1)
    b += cloud(230, 210, .9, st) + cloud(620, 140, .7, st)
    b += P(poly(ridge(4, 470, 40, 70)), '#a8b6d6', st, bg=True)
    b += P(wave(560, 16, 5, 1.0), '#8cc067', st, bg=True)
    # ribs of Azhi, receding
    for x, yb, h, span, w in [(90, 600, 470, 260, 26), (420, 600, 520, 300, 30), (790, 600, 470, 260, 26)]:
        b += rib(x, yb, h, span, w)
    b += P(wave(640, 18, 4, 2.4), '#6aa84a', st, bg=True)
    b += P(poly([(-20, 712), (200, 700), (420, 708), (640, 696), (860, 704), (1080, 694), (1230, 702)]), '#c79a5c', st, bg=True)
    b += rib(980, 760, 260, 190, 22)
    f = team([(250, 'Red', 'fighter', '#8d98a6', '#2f4f8f', 1, 1.04),
              (440, 'Yellow', 'wizard', '#7a3a2a', '#f2d16b', 1, 0.98),
              (630, 'Blue', 'cleric', '#efe4cc', '#2b5fa8', 1, 0.96),
              (820, 'Green', 'ranger', '#5c6b3a', '#7a4e2a', -1, 1.0)], 724)
    return b + f + caption('The Bones of Azhi', 'The world is a dragon. Its ribs still stand where it fell.')


def scene_machines():
    b = sky(['#f0a35e', '#f7c98a', '#fde7c0'], st, 0, 600)
    b += ring_arch('M -100,560 Q 600,-200 1320,520', 40, st, op=.35)
    b += P(poly(ridge(9, 420, 50, 60)), '#7c9a6a', st, bg=True)
    # trees
    rnd = random.Random(5)
    for x in range(-20, 1260, 95):
        h = rnd.uniform(170, 260)
        b += P(f'M {x - 8},560 L {x - 8},{560 - h * .4} L {x + 8},{560 - h * .4} L {x + 8},560 Z', '#6b4a2f', st, bg=True)
        b += P(f'M {x - 52},{560 - h * .35} Q {x},{560 - h * 1.1} {x + 52},{560 - h * .35} Z', '#3f7d3c', st, bg=True)
    b += P(wave(580, 12, 5, 0.3), '#5d8f45', st, bg=True)
    # the relic: a half-buried engine with a big gear and a dead glass eye
    b += P('M 520,640 L 560,420 Q 700,330 860,420 L 900,640 Z', '#8a7b66', st, bg=True)
    b += gear(560, 470, 120, 12, '#c99a46', rot=8)
    b += circ(760, 470, 62, '#2c3640', dict(st, stroke=5))
    b += glow(760, 470, 80, '#5ff0e0')
    b += circ(760, 470, 34, '#7ff7ea', dict(st, stroke=4))
    b += circ(748, 458, 9, '#ffffff', dict(st, stroke=0))
    b += vine([(520, 640), (560, 560), (610, 520), (680, 540), (720, 600)], 9)
    b += vine([(880, 640), (850, 560), (830, 500), (860, 440)], 8)
    for (x, y) in [(600, 548), (700, 560), (842, 520), (560, 590)]:
        b += P(f'M {x},{y} q 14,-14 26,0 q -12,12 -26,0 Z', '#6fbf4a', st)
    b += P(poly([(-20, 706), (240, 694), (520, 702), (800, 690), (1060, 700), (1230, 694)]), '#9b7a4c', st, bg=True)
    b += gear(470, 728, 40, 9, '#b98a3c', rot=20)
    f = team([(170, 'White', 'fighter', '#6f7b8a', '#9b2d2d', 1, 1.02),
              (340, 'Grey', 'wizard', '#4a4f5c', '#c9d2e0', 1, 1.0),
              (960, 'Brown', 'fighter', '#7c6a4e', '#5b7a3a', -1, 1.06),
              (1110, 'Black', 'wizard', '#2f6b6b', '#e8c35a', -1, 0.96)], 724)
    return b + f + caption('The Machine War', 'Epoch 2: the thinking engines ate themselves. Their pieces are forbidden.')


def scene_temple():
    b = sky(['#3b2f6b', '#7a5aa8', '#e6a6c4'], st, 0, 620)
    rnd = random.Random(7)
    for _ in range(40):
        x, y = rnd.uniform(0, 1200), rnd.uniform(0, 300)
        b += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.uniform(.8, 2):.1f}" fill="#fff" opacity="{rnd.uniform(.4, .9):.2f}"/>'
    b += sky_dragon(200, 170, .75, '#e6edf8', '#bcd2ff', st)
    b += P(poly(ridge(12, 500, 30, 80)), '#6d5a8a', st, bg=True)
    # stepped floor
    b += P('M -20,800 L -20,600 L 1220,600 L 1220,800 Z', '#cbbfa6', st, bg=True)
    b += P('M 360,600 L 400,560 L 800,560 L 840,600 Z', '#ddd2bb', st, bg=True)
    for x, h, br in [(40, 380, False), (200, 250, True), (900, 330, True), (1070, 400, False)]:
        b += column(x, 600, h, broken=br)
    # the broken ouroboros altar, still faintly glowing
    b += P('M 520,560 L 520,470 L 680,470 L 680,560 Z', '#b9ad92', st, bg=True)
    b += glow(600, 360, 170, '#c58bff')
    b += (f'<path d="M 690,360 A 90,90 0 1 1 650,286" fill="none" stroke="{INK}" stroke-width="30" stroke-linecap="round"/>'
          f'<path d="M 690,360 A 90,90 0 1 1 650,286" fill="none" stroke="#e8c35a" stroke-width="20" stroke-linecap="round"/>')
    b += circ(690, 360, 16, '#e8c35a', dict(st, stroke=5))
    for _ in range(18):
        x, y = 600 + rnd.uniform(-160, 160), 360 + rnd.uniform(-150, 120)
        b += f'<path d="M {x:.0f},{y - 7:.0f} L {x + 3:.0f},{y:.0f} L {x:.0f},{y + 7:.0f} L {x - 3:.0f},{y:.0f} Z" fill="#fff4b0" opacity=".85"/>'
    # cracks
    b += f'<path d="M 120,640 l 60,30 l -10,40 l 70,30 M 980,630 l -40,40 l 30,30" fill="none" stroke="#8f8370" stroke-width="5"/>'
    f = team([(240, 'Indigo', 'rogue', '#2a2a33', '#7a2f3a', 1, 0.98),
              (400, 'White', 'cleric', '#6f7b8a', '#9b2d2d', 1, 1.0),
              (820, 'Blue', 'wizard', '#e9dfc6', '#1f3f73', -1, 0.98),
              (980, 'Red', 'ranger', '#55663a', '#7a4e2a', -1, 1.04)], 724)
    return b + f + caption('The Age of Faith', 'Epoch 3: the churches drew on the dragons, until the taps were shut.')


def scene_eggs():
    b = sky(['#ffb3a0', '#ffd9b0', '#fff3d6'], st, 0, 600)
    b += glow(600, 520, 360, '#ffd25a')
    b += ring_arch('M -80,480 Q 600,-160 1280,480', 30, st, op=.45)
    b += cloud(200, 200, .8, st) + cloud(980, 170, 1.0, st)
    b += P(poly(ridge(21, 470, 35, 65)), '#a9a0c9', st, bg=True)
    b += P(wave(560, 14, 5, 0.8), '#9cc77a', st, bg=True)
    # the nest crater
    b += P('M 140,700 Q 600,470 1060,700 Z', '#b98d5c', st, bg=True)
    b += P('M 250,680 Q 600,540 950,680 Z', '#9a7046', st, bg=True)
    b += eggshell(515, 650, 130, 220, '#bfe0f7', '#5f9bd8', 3, lean=-8)
    b += eggshell(790, 655, 130, 210, '#d3edc0', '#5aa64a', 8, lean=9)
    # a fallen shard
    b += P('M 640,700 L 670,665 L 705,690 L 680,712 Z', '#bfe0f7', st, bg=True)
    b += P(poly([(-20, 712), (300, 700), (600, 708), (900, 696), (1230, 706)]), '#c9a46c', st, bg=True)
    f = team([(130, 'Green', 'rogue', '#5a3e2b', '#3d2f4f', 1, 0.98),
              (270, 'Brown', 'fighter', '#7c6a4e', '#5b7a3a', 1, 1.06),
              (990, 'Blue', 'cleric', '#efe4cc', '#2b5fa8', -1, 0.96),
              (1120, 'Indigo', 'wizard', '#2a2a33', '#7a2f3a', -1, 1.0)], 728)
    return b + f + caption("The Twins' Nest", 'Epoch 4: the first dragon eggs ever seen, from Blue and Green.')


def scene_campfire():
    b = sky(['#171a3a', '#2c2f63', '#4b4a86'], st, 0, 640)
    rnd = random.Random(11)
    for _ in range(90):
        x, y = rnd.uniform(0, 1200), rnd.uniform(0, 420)
        b += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.uniform(.6, 2):.1f}" fill="#fff" opacity="{rnd.uniform(.4, .95):.2f}"/>'
    b += ring_arch('M -160,600 Q 600,-380 1360,600', 56, st, op=.75)
    b += sky_dragon(1000, 170, .8, '#e6edf8', '#bcd2ff', st, flip=-1)
    b += P(poly(ridge(17, 520, 40, 70)), '#2e3358', st, bg=True)
    b += P(wave(610, 14, 5, 1.7), '#3b4a3a', st, bg=True)
    b += P(poly([(-20, 706), (260, 696), (540, 704), (820, 694), (1080, 702), (1230, 696)]), '#4d4a3e', st, bg=True)
    # campfire, and the story taking shape in the smoke: two homunculi dragons
    b += glow(600, 690, 260, '#ffb347')
    b += (f'<path d="M 600,560 C 560,500 640,460 600,400 C 570,350 630,310 600,250" fill="none" '
          f'stroke="#d8d2e6" stroke-width="40" stroke-linecap="round" opacity=".35"/>')
    b += f'<g opacity=".7">{sky_dragon(500, 300, .55, "#f0cf2e", "#fbf0b0", st)}{sky_dragon(700, 290, .55, "#7d838c", "#d3d6db", st, flip=-1)}</g>'
    for k, (dx, h) in enumerate([(-30, 60), (0, 90), (28, 66)]):
        c = ['#ff7a2a', '#ffc53a', '#ff9a2a'][k]
        b += P(f'M {600 + dx - 22},700 Q {600 + dx - 18},{700 - h * .6} {600 + dx},{700 - h} '
               f'Q {600 + dx + 18},{700 - h * .6} {600 + dx + 22},700 Z', c, st)
    b += limb([(560, 708), (640, 696)], 12, '#6b4423', st) + limb([(560, 696), (640, 708)], 12, '#7a5233', st)
    f = team([(200, 'Yellow', 'rogue', '#7a3a2a', '#f2d16b', 1, 0.96),
              (380, 'Red', 'fighter', '#8d98a6', '#2f4f8f', 1, 1.02),
              (830, 'Grey', 'wizard', '#4a4f5c', '#c9d2e0', -1, 1.04),
              (1010, 'Green', 'ranger', '#5c6b3a', '#7a4e2a', -1, 0.98)], 724)
    return b + f + caption('The Homunculi War', 'Epoch 5: two centuries ago. Some veterans still tell it, in another colour.')


SCENES = [('lore_1_bones', scene_bones), ('lore_2_machines', scene_machines),
          ('lore_3_temple', scene_temple), ('lore_4_eggs', scene_eggs),
          ('lore_5_campfire', scene_campfire)]


def panel_svg(fn):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800">{defs(st)}{fn()}</svg>'


def sheet(bodies):
    W, H = 2480, 2560
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         f'<rect width="{W}" height="{H}" fill="#1c1916"/>']
    slots = [(40, 40), (1240, 40), (40, 880), (1240, 880), (40, 1720)]
    for (x, y), body in zip(slots, bodies):
        o.append(f'<svg x="{x}" y="{y}" width="1200" height="800" viewBox="0 0 1200 800">{body}</svg>')
        o.append(f'<rect x="{x}" y="{y}" width="1200" height="800" fill="none" stroke="#f3e8cf" stroke-width="6"/>')
    # title card in the sixth slot
    x, y = 1240, 1720
    o.append(f'<rect x="{x}" y="{y}" width="1200" height="800" fill="#fbf4e3" stroke="#f3e8cf" stroke-width="6"/>')
    o.append(f'<circle cx="{x + 600}" cy="{y + 300}" r="150" fill="none" stroke="{INK}" stroke-width="40"/>'
             f'<circle cx="{x + 600}" cy="{y + 300}" r="150" fill="none" stroke="#3a3f8f" stroke-width="28" stroke-dasharray="880 60"/>'
             f'<circle cx="{x + 750}" cy="{y + 300}" r="26" fill="#3a3f8f" stroke="{INK}" stroke-width="6"/>')
    o.append(f'<text x="{x + 600}" y="{y + 560}" text-anchor="middle" font-family="DejaVu Serif" font-weight="bold" font-size="64" fill="{INK}">A Short History of Azhi</text>')
    o.append(f'<text x="{x + 600}" y="{y + 620}" text-anchor="middle" font-family="DejaVu Serif" font-style="italic" font-size="30" fill="#5a4e40">as visited by some curious dragonborn</text>')
    o.append('</svg>')
    return ''.join(o)


if __name__ == '__main__':
    os.makedirs('build', exist_ok=True); os.makedirs('output', exist_ok=True)
    bodies = []
    for name, fn in SCENES:
        svg = panel_svg(fn)
        bodies.append(defs(st) + fn())
        open(f'build/{name}.svg', 'w').write(svg)
        subprocess.run([sys.executable, 'svg2png.py', f'build/{name}.svg', f'output/{name}.png', '1200', '800'], check=True)
        print(name)
    open('build/lore_panels.svg', 'w').write(sheet(bodies))
    subprocess.run([sys.executable, 'svg2png.py', 'build/lore_panels.svg', 'output/lore_panels.png', '2480', '2560'], check=True)
    print('lore_panels')
