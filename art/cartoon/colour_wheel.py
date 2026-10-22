"""The dragonborn colour wheel (brainstorm visual, PROPOSED) -> output/colour_wheel.png.

Five primary forms at the pentagon's corners and five bichrome hybrids between them,
the Unphased in the blank centre (a polychrome silhouette: every colour, none settled),
and Gold and Silver outside the wheel, watching but not taking part.
Saturday-Morning Bold. Hybrid colours and names are working values from
canon/brainstorm-species.md."""
import os, sys, math, random, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE); sys.path.insert(0, HERE)
import party
from party import STYLES, figure, glow, light, dark, P

st = STYLES['bold']
INK = st['line']
W, H = 1600, 1440
CX, CY = 800, 780
R_IN, R_OUT, R_FIG = 318, 560, 452

# Hybrid scale/belly colours (PROPOSED working values), mixed like paint pigments.
party.DRAGONS.update({
    'Marsh':   ('#23857f', '#a6dccd'),   # Blue + Green: teal
    'Soil':    ('#8a5a2b', '#ddb98c'),   # Green + Red: umber
    'Oxblood': ('#6e1f2a', '#c27e82'),   # Red + Black
    'Slate':   ('#66707f', '#c4cad3'),   # Black + White
    'Glacier': ('#8fc6ea', '#e4f3fc'),   # White + Blue
})
party.HORN.update({'Glacier': '#7d91a8', 'Slate': '#e3ddd2'})

# Clockwise from the top: Blue, then the wheel order Blue -> Green -> Red -> Black -> White.
WHEEL = [  # (form, label, sub, role, outfit, accent)
    ('Blue',    'Blue',    'water',          'rogue',   '#e9dfc6', '#1f3f73'),
    ('Marsh',   'Marsh',   'Blue + Green',   'rogue',   '#5c6b3a', '#3e5a4a'),
    ('Green',   'Green',   'life',           'cleric',  '#e8dcc0', '#5b7a3a'),
    ('Soil',    'Soil',    'Green + Red',    'fighter', '#7c6a4e', '#5b7a3a'),
    ('Red',     'Red',     'fire & stone',   'fighter', '#8d98a6', '#2f4f8f'),
    ('Oxblood', 'Oxblood', 'Red + Black',    'wizard',  '#3b3a40', '#d4a63c'),
    ('Black',   'Black',   'knowledge',      'wizard',  '#2f6b6b', '#e8c35a'),
    ('Slate',   'Slate',   'Black + White',  'rogue',   '#4a4f5c', '#7a2f3a'),
    ('White',   'White',   'ice',            'cleric',  '#6f7b8a', '#9b2d2d'),
    ('Glacier', 'Glacier', 'White + Blue',   'wizard',  '#8a6f4d', '#355f86'),
]

def pt(r, a_deg):
    a = math.radians(a_deg - 90)
    return CX + r*math.cos(a), CY + r*math.sin(a)

def wedge(a0, a1, fill):
    p0, p1 = pt(R_OUT, a0), pt(R_OUT, a1)
    q1, q0 = pt(R_IN, a1), pt(R_IN, a0)
    d = (f'M {p0[0]:.1f},{p0[1]:.1f} A {R_OUT},{R_OUT} 0 0 1 {p1[0]:.1f},{p1[1]:.1f} '
         f'L {q1[0]:.1f},{q1[1]:.1f} A {R_IN},{R_IN} 0 0 0 {q0[0]:.1f},{q0[1]:.1f} Z')
    return P(d, fill, st, bg=True)

def label(x, y, name, sub, big=False):
    fs, fs2 = (30, 17) if big else (24, 15)
    w = max(len(name)*fs*0.62, len(sub)*fs2*0.56) + 26
    h = fs + fs2 + 16
    o = (f'<rect x="{x-w/2:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h}" rx="12" fill="#fbf4e3" '
         f'stroke="{INK}" stroke-width="3"/>')
    o += (f'<text x="{x:.1f}" y="{y+fs+3:.1f}" text-anchor="middle" font-family="DejaVu Sans" '
          f'font-weight="bold" font-size="{fs}" fill="{INK}">{name}</text>')
    o += (f'<text x="{x:.1f}" y="{y+fs+fs2+8:.1f}" text-anchor="middle" font-family="DejaVu Sans" '
          f'font-style="italic" font-size="{fs2}" fill="#5a4e40">{sub}</text>')
    return o

def unphased(x, y, s):
    """Ink silhouette with a soft, shifting blend of all five colours inside the lines."""
    ink_skin = dict(st)
    party.DRAGONS['_ink'] = (INK, INK); party.HORN['_ink'] = INK
    party.DRAGONS['_mask'] = ('#ffffff', '#ffffff'); party.HORN['_mask'] = '#ffffff'
    sil = figure(x, y, s, '_ink', 'rogue', INK, INK, ink_skin)
    mask_st = dict(st, line='#000000')
    m = figure(x, y, s, '_mask', 'rogue', '#ffffff', '#ffffff', mask_st)
    B, G, R, K, Wt = '#2e6fd2', '#3c9a47', '#c8342b', '#4a4360', '#eceff4'
    spots = [  # (dx, dy, colour, r): patches of every colour, none dominant
        (14, -140, B, 22), (34, -128, Wt, 18), (-8, -128, R, 20), (2, -108, G, 22),
        (-14, -88, K, 20), (14, -86, R, 22), (30, -66, B, 20), (-6, -62, Wt, 18),
        (-20, -44, G, 22), (12, -40, K, 20), (-30, -20, B, 20), (8, -14, R, 20),
        (-56, -10, G, 18), (-42, -40, R, 18), (-26, -110, B, 16)]
    blobs = ''.join(f'<circle cx="{x+dx*s:.1f}" cy="{y+dy*s:.1f}" r="{r*s:.1f}" fill="{c}"/>'
                    for dx, dy, c, r in spots)
    o = (f'<filter id="poly" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="{9*s:.1f}"/></filter>'
         f'<mask id="upm" maskUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}">'
         f'<rect width="{W}" height="{H}" fill="#000"/>{m}</mask>')
    o += glow(x, y - 62*s, 150*s, '#ffffff')
    o += sil
    o += f'<g mask="url(#upm)"><rect x="{x-90*s}" y="{y-180*s}" width="{180*s}" height="{190*s}" fill="#9a8fb0"/>'
    o += f'<g filter="url(#poly)">{blobs}</g></g>'
    return o

def stars(n, seed):
    rnd = random.Random(seed); o = ''
    for _ in range(n):
        x, y = rnd.uniform(0, W), rnd.uniform(0, H)
        if math.hypot(x-CX, y-CY) < R_OUT + 20: continue
        o += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.uniform(.7, 2.0):.1f}" fill="#fff" opacity="{rnd.uniform(.35, .9):.2f}"/>'
    return o

def build():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    o.append('<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
             '<stop offset="0" stop-color="#1d2148"/><stop offset=".55" stop-color="#3b3a6e"/>'
             '<stop offset="1" stop-color="#25233f"/></linearGradient></defs>')
    o.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
    o.append(stars(160, 3))
    # Gold (sun-warm) and Silver (moon-cool) glows outside the wheel
    o.append(glow(150, 330, 260, '#ffd25a'))
    o.append(glow(1450, 330, 260, '#bcd2ff'))
    # the wheel
    o.append(f'<circle cx="{CX}" cy="{CY}" r="{R_OUT+14}" fill="none" stroke="{INK}" stroke-width="3" opacity=".5"/>')
    for i, (form, *_rest) in enumerate(WHEEL):
        scale, belly = party.DRAGONS[form]
        o.append(wedge(i*36 - 18, i*36 + 18, light(scale, .55)))
    o.append(f'<circle cx="{CX}" cy="{CY}" r="{R_IN}" fill="#f6eedb" stroke="{INK}" stroke-width="3"/>')
    # figures and labels
    figs, labs = [], []
    for i, (form, name, sub, role, outfit, accent) in enumerate(WHEEL):
        a = i*36
        x, y = pt(R_FIG, a)
        s = 1.12
        flip = -1 if 0 < a < 180 else 1
        feet = y + 52
        figs.append(figure(x, feet, s, form, role, outfit, accent, st, flip=flip))
        labs.append(label(x, feet + 10, name, sub, big=(i % 2 == 0)))
    o += figs + labs
    # the Unphased, centre
    o.append(unphased(CX, CY + 95, 1.75))
    o.append(label(CX, CY + 112, 'Unphased', 'all colours, none settled', big=True))
    # Gold and Silver, outside, looking in
    o.append(figure(170, 420, 1.45, 'Gold', 'cleric', '#f3efe6', '#c08a1e', st, flip=1))
    o.append(label(170, 432, 'Gold', 'the sun, watching', big=True))
    o.append(figure(1430, 420, 1.45, 'Silver', 'wizard', '#4b3a7a', '#f2d16b', st, flip=-1))
    o.append(label(1430, 432, 'Silver', 'the moon, watching', big=True))
    # title
    o.append(f'<text x="{CX}" y="70" text-anchor="middle" font-family="DejaVu Serif" font-weight="bold" '
             f'font-size="46" fill="#f3e8cf">The Dragonborn Colour Wheel</text>')
    o.append(f'<text x="{CX}" y="106" text-anchor="middle" font-family="DejaVu Serif" font-style="italic" '
             f'font-size="21" fill="#c9bda3">Brainstorm sketch (PROPOSED): five colours, five blends, the Unphased at the heart</text>')
    o.append('</svg>')
    return ''.join(o)

if __name__ == '__main__':
    os.makedirs('build', exist_ok=True); os.makedirs('output', exist_ok=True)
    open('build/colour_wheel.svg', 'w').write(build())
    subprocess.run([sys.executable, 'svg2png.py', 'build/colour_wheel.svg', 'output/colour_wheel.png', str(W), str(H)], check=True)
    print('output/colour_wheel.png')
