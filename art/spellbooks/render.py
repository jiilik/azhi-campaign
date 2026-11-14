"""The three Mage Kit starting spellbooks as unrolled scrolls (Troy, 2026-11-13).

One page per book, each unrolled only as far as its spells, with the rest of
the text still rolled up at the edges:
  primer   The Junior Wizard's Primer      a herald's proclamation scroll (portrait)
  summons  Selected Summons for Novices     a painted handscroll (landscape)
  alchemy  Practical Alchemy                a papyrus roll (landscape)
Spell text is SRD 5.2.1, verbatim (spells.py reads it from srd/07-spells).
Fonts in fonts/ are OFL 1.1 (via @fontsource). Run: python3 render.py [key ...]
-> output/<key>.png (3x) and output/<key>.pdf.
"""
import html as H
import math
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'cartoon'))
import party  # noqa: E402
import tapestry_lib as T  # noqa: E402
from spells import BOOKS, spell  # noqa: E402

INK = T.INK
ATTRIB = ('This work includes material from the System Reference Document 5.2.1 (“SRD 5.2.1”) by Wizards of the Coast LLC, '
          'available at https://www.dndbeyond.com/srd. The SRD 5.2.1 is licensed under the Creative Commons Attribution 4.0 '
          'International License, available at https://creativecommons.org/licenses/by/4.0/legalcode.')

FONTS = {
    'Fraktur': 'unifrakturmaguntia-latin-400-normal', 'Fell': 'im-fell-english-latin-400-normal',
    'FellItalic': 'im-fell-english-latin-400-italic', 'FellSC': 'im-fell-english-sc-latin-400-normal',
    'Cinzel': 'cinzel-latin-700-normal', 'CinzelDeco': 'cinzel-decorative-latin-700-normal',
    'Corm': 'cormorant-garamond-latin-500-normal', 'CormBold': 'cormorant-garamond-latin-700-normal',
    'CormItalic': 'cormorant-garamond-latin-500-italic', 'Mincho': 'shippori-mincho-latin-500-normal',
    'MinchoBold': 'shippori-mincho-latin-800-normal', 'ZenOld': 'zen-old-mincho-latin-700-normal',
    'Marcellus': 'marcellus-latin-400-normal',
}
FONT_CSS = ''.join(f"@font-face{{font-family:'{k}';src:url(fonts/{v}.woff2) format('woff2')}}" for k, v in FONTS.items())


# ---------------------------------------------------------------- spell text
def md(s):
    s = H.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<!\w)_(.+?)_(?!\w)', r'<i>\1</i>', s)
    return s


def spell_html(name):
    paras = [p.strip() for p in spell(name).split('\n\n') if p.strip()]
    school, stats, rest = paras[0], paras[1], paras[2:]
    o = f'<div class="spell"><h2>{H.escape(name)}</h2><div class="school">{md(school)}</div>'
    o += '<div class="stats">' + '<br>'.join(md(ln) for ln in stats.split('\n')) + '</div>'
    for k, p in enumerate(rest):
        o += f'<p class="{"first" if k == 0 else ""}">{md(p)}</p>'
    return o + '</div>'


def spells_html(key):
    return ''.join(spell_html(n) for n in BOOKS[key][1])


# ---------------------------------------------------------------- shared svg bits
def svg(W, Hh, body, cls='layer', z=0):
    return (f'<svg class="{cls}" style="z-index:{z}" xmlns="http://www.w3.org/2000/svg" width="{W}" height="{Hh}" '
            f'viewBox="0 0 {W} {Hh}">{body}</svg>')


def noise_filter(fid, freq, seed, rgb, alpha, octaves=3):
    r, g, b = rgb
    return (f'<filter id="{fid}" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="{freq}" '
            f'numOctaves="{octaves}" seed="{seed}"/><feColorMatrix type="matrix" values="0 0 0 0 {r}  0 0 0 0 {g}  0 0 0 0 {b}  '
            f'{alpha} 0 0 0 {-alpha * 0.45:.3f}"/></filter>')


def wobble(x0, y0, x1, y1, amp, n, seed, vertical=True):
    """Points along a slightly irregular edge from (x0,y0) to (x1,y1)."""
    rnd = random.Random(seed)
    pts = []
    for k in range(n + 1):
        t = k / n
        x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
        j = 0 if k in (0, n) else rnd.uniform(-amp, amp)
        pts.append((x + j, y) if vertical else (x, y + j))
    return pts


def cyl_grad(gid, base, vertical_axis=False):
    """A shaded gradient that makes a rectangle read as a cylinder."""
    x2, y2 = ('1', '0') if vertical_axis else ('0', '1')
    d, l_ = party.dark, party.light
    return (f'<linearGradient id="{gid}" x1="0" y1="0" x2="{x2}" y2="{y2}">'
            f'<stop offset="0" stop-color="{d(base, .38)}"/><stop offset=".22" stop-color="{l_(base, .28)}"/>'
            f'<stop offset=".42" stop-color="{base}"/><stop offset=".8" stop-color="{d(base, .22)}"/>'
            f'<stop offset="1" stop-color="{d(base, .45)}"/></linearGradient>')


def spiral_end(cx, cy, rx, ry, colour, turns=4):
    """The end of a roll: an ellipse with the rolled layers drawn as a spiral."""
    o = f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{colour}" stroke="{INK}" stroke-width="3"/>'
    pts = []
    for k in range(200):
        t = k / 199
        a = t * turns * 2 * math.pi
        r = 0.12 + 0.82 * t
        pts.append((cx + rx * r * math.cos(a), cy + ry * r * math.sin(a)))
    o += '<path d="M ' + ' L '.join(f'{a:.1f},{b:.1f}' for a, b in pts) + f'" fill="none" stroke="{party.dark(colour, .4)}" stroke-width="1.4"/>'
    return o


def figure_svg(x, y, s, drag, pose, outfit, accent, flip=1, item=None, look=0, **kw):
    return T.person(x, y, s, drag, pose, outfit, accent, flip=flip, item=item, look=look, **kw)


def page(key, W, Hh, css, layers, attrib_colour='#2b1d12'):
    return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{FONT_CSS}'
            f'html,body{{margin:0;padding:0}} body{{width:{W}px;height:{Hh}px;position:relative;overflow:hidden}}'
            f'.layer{{position:absolute;left:0;top:0}} .abs{{position:absolute}}'
            f'.spell h2,.school{{break-after:avoid-column;margin:0}} .stats{{break-inside:avoid-column}} p{{margin:0;orphans:2;widows:2}}'
            f'.attrib{{position:absolute;left:40px;right:40px;bottom:10px;text-align:center;font:7.4px/1.3 "Corm",serif;color:{attrib_colour};opacity:.9}}'
            f'{css}</style></head><body>{"".join(layers)}'
            f'<div class="attrib">Azhi · a starting spellbook of the Mage Kit · {ATTRIB}</div></body></html>')


# ================================================================ 1. the herald's scroll
def primer():
    W, Hh = 850, 1100
    PX0, PX1 = 128, 722
    TOP, BOT = 138, 966          # roll centres
    RT, RB = 36, 24
    rnd = random.Random(11)
    g = ['<defs>', noise_filter('stain', 0.012, 4, (0.45, 0.3, 0.12), 0.9), noise_filter('grain', 0.9, 7, (0.4, 0.28, 0.12), 0.55, 2),
         cyl_grad('rollT', '#ead4a1'), cyl_grad('rollB', '#ead4a1'), cyl_grad('rod', '#7a4a26', True),
         '<radialGradient id="parch" cx=".5" cy=".45" r=".75"><stop offset="0" stop-color="#f6e9c6"/><stop offset=".7" stop-color="#ecd6a2"/>'
         '<stop offset="1" stop-color="#d4b06c"/></radialGradient>',
         '<linearGradient id="wood" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4a2c18"/><stop offset="1" stop-color="#22130a"/></linearGradient>',
         '<radialGradient id="vign" cx=".5" cy=".5" r=".7"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></radialGradient>',
         '<filter id="soft"><feGaussianBlur stdDeviation="6"/></filter>', '</defs>']
    # the table
    g.append(f'<rect width="{W}" height="{Hh}" fill="url(#wood)"/>')
    for k in range(46):
        y = rnd.uniform(0, Hh)
        g.append(f'<path d="M -10,{y:.0f} C 200,{y + rnd.uniform(-30, 30):.0f} 600,{y + rnd.uniform(-30, 30):.0f} {W + 10},{y + rnd.uniform(-20, 20):.0f}" '
                 f'stroke="#{rnd.choice(["5a3820", "2c1a0e", "6a4426"])}" stroke-width="{rnd.uniform(1, 3):.1f}" fill="none" opacity=".5"/>')
    g.append(f'<rect width="{W}" height="{Hh}" fill="url(#vign)"/>')
    # shadow, then the sheet
    left = wobble(PX0, TOP, PX0, BOT, 3, 18, 1)
    right = wobble(PX1, BOT, PX1, TOP, 3, 18, 2)
    d = 'M ' + ' L '.join(f'{a:.1f},{b:.1f}' for a, b in left + right) + ' Z'
    g.append(f'<path d="{d}" fill="#000" opacity=".45" transform="translate(10,12)" filter="url(#soft)"/>')
    g.append(f'<path d="{d}" fill="url(#parch)" stroke="{INK}" stroke-width="3"/>')
    g.append(f'<clipPath id="sheet"><path d="{d}"/></clipPath><g clip-path="url(#sheet)">'
             f'<rect x="0" y="0" width="{W}" height="{Hh}" filter="url(#stain)" opacity=".55"/>'
             f'<rect x="0" y="0" width="{W}" height="{Hh}" filter="url(#grain)" opacity=".35"/>'
             f'<rect x="{PX0}" y="{TOP}" width="{PX1 - PX0}" height="40" fill="#5a3a1a" opacity=".22"/>'
             f'<rect x="{PX0}" y="{BOT - 34}" width="{PX1 - PX0}" height="34" fill="#5a3a1a" opacity=".18"/></g>')
    # a red-ruled margin, as a herald's clerk would draw
    g.append(f'<rect x="{PX0 + 22}" y="{TOP + 44}" width="{PX1 - PX0 - 44}" height="{BOT - TOP - 82}" fill="none" stroke="#9b2d2d" stroke-width="1.4" opacity=".7"/>')
    g.append(f'<rect x="{PX0 + 27}" y="{TOP + 49}" width="{PX1 - PX0 - 54}" height="{BOT - TOP - 92}" fill="none" stroke="#9b2d2d" stroke-width=".7" opacity=".6"/>')
    back = svg(W, Hh, ''.join(g))

    # header art: a shield with the ring, two heralds sounding horns
    hw, hh = 470, 120
    a = [party.defs(party.STYLES['bold'])]
    cx = hw / 2
    for side in (-1, 1):   # pennants on the horns, swallow-tailed
        pass
    a.append(f'<path d="M {cx - 34},18 L {cx + 34},18 L {cx + 34},62 Q {cx + 34},96 {cx},112 Q {cx - 34},96 {cx - 34},62 Z" fill="#b3261e" stroke="{INK}" stroke-width="3.4"/>')
    a.append(f'<path d="M {cx - 34},18 L {cx},18 L {cx},112 Q {cx - 34},96 {cx - 34},62 Z" fill="#c8342b" opacity=".6"/>')
    a.append(f'<circle cx="{cx}" cy="62" r="20" fill="none" stroke="{INK}" stroke-width="9"/><circle cx="{cx}" cy="62" r="20" fill="none" stroke="#f0c43c" stroke-width="5"/>')
    a.append(f'<path d="M {cx + 13},44 L {cx + 26},38 L {cx + 22},50 Z" fill="#f0c43c" stroke="{INK}" stroke-width="2"/>')
    a.append(f'<path d="M {cx - 40},14 Q {cx},2 {cx + 40},14" fill="none" stroke="{INK}" stroke-width="3"/>')
    for k, (fx, flip, drag, outfit) in enumerate([(cx - 120, 1, 'Red', '#2b5fa8'), (cx + 120, -1, 'White', '#2b5fa8')]):
        a.append(figure_svg(fx, 116, 0.78, drag, 'hold', outfit, '#e8c35a', flip=flip, item='horn', look=-24))
        # a pennant hanging from the horn: the ring device on blue
        px = fx + flip * 58
        a.append(f'<path d="M {px},40 L {px + flip * 2},44 L {px + flip * 4},84 L {px + flip * 16},74 L {px + flip * 28},86 L {px + flip * 30},46 Z" '
                 f'fill="#2b5fa8" stroke="{INK}" stroke-width="2.4"/>')
        a.append(f'<circle cx="{px + flip * 16}" cy="58" r="7" fill="none" stroke="#f0c43c" stroke-width="2.6"/>')
    for side in (-1, 1):   # little notes from the horns
        nx = cx + side * 200
        a.append(f'<path d="M {nx},38 q 6,-6 12,0 M {nx + side * 10},26 q 6,-6 12,0" stroke="{INK}" stroke-width="2" fill="none"/>')
    header_art = (f'<svg width="{hw}" height="{hh}" viewBox="0 0 {hw} {hh}" style="display:block;margin:0 auto">{"".join(a)}</svg>')

    # the rolls and the seal, drawn over the text edges
    o = ['<defs>', cyl_grad('rT', '#e8d09a'), cyl_grad('rB', '#e8d09a'), '</defs>']
    for (cy, r, gid) in ((TOP, RT, 'rT'), (BOT, RB, 'rB')):
        x0, x1 = PX0 - 16, PX1 + 16
        o.append(f'<rect x="{x0 - 26}" y="{cy - 7}" width="{x1 - x0 + 52}" height="14" rx="5" fill="#7a4a26" stroke="{INK}" stroke-width="3"/>')
        for ex in (x0 - 30, x1 + 30):
            o.append(f'<circle cx="{ex}" cy="{cy}" r="11" fill="#d9a531" stroke="{INK}" stroke-width="3"/>'
                     f'<circle cx="{ex - 3}" cy="{cy - 3}" r="3.5" fill="#fff3b8"/>')
        o.append(f'<rect x="{x0}" y="{cy - r}" width="{x1 - x0}" height="{2 * r}" fill="url(#{gid})" stroke="{INK}" stroke-width="3"/>')
        for k in range(3):   # a few loose turns of the roll
            yy = cy - r + 2 * r * (0.3 + 0.2 * k)
            o.append(f'<path d="M {x0 + 6},{yy:.0f} L {x1 - 6},{yy:.0f}" stroke="#b9975a" stroke-width="1" opacity=".55"/>')
        o.append(spiral_end(x0, cy, r * 0.32, r, '#f0dcae'))
        o.append(spiral_end(x1, cy, r * 0.32, r, '#f0dcae'))
    # seal and ribbons hanging from the lower roll
    sx, sy = W / 2, BOT + 58
    for (dx, ex) in ((-10, -34), (10, 30)):
        o.append(f'<path d="M {sx + dx - 7},{BOT + 6} L {sx + dx + 7},{BOT + 6} L {sx + ex + 9},{sy + 34} L {sx + ex},{sy + 26} L {sx + ex - 9},{sy + 34} Z" '
                 f'fill="#8f1d1d" stroke="{INK}" stroke-width="2.6"/>')
    pts = [(sx + (30 + (3 if k % 2 else -1)) * math.cos(k * math.pi / 9), sy + (30 + (3 if k % 2 else -1)) * math.sin(k * math.pi / 9)) for k in range(18)]
    o.append('<path d="M ' + ' L '.join(f'{a:.1f},{b:.1f}' for a, b in pts) + f' Z" fill="#b3261e" stroke="{INK}" stroke-width="3"/>')
    o.append(f'<circle cx="{sx}" cy="{sy}" r="20" fill="#9a1f19" stroke="#6e1410" stroke-width="2"/>')
    o.append(f'<circle cx="{sx}" cy="{sy}" r="12" fill="none" stroke="#d9473d" stroke-width="4.5"/>')
    o.append(f'<path d="M {sx + 8},{sy - 10} L {sx + 15},{sy - 14} L {sx + 13},{sy - 6} Z" fill="#d9473d"/>')
    o.append(f'<ellipse cx="{sx - 10}" cy="{sy - 12}" rx="7" ry="3.5" fill="#fff" opacity=".35" transform="rotate(-30 {sx - 10} {sy - 12})"/>')
    front = svg(W, Hh, ''.join(o), z=3)

    css = f'''
    .text{{left:{PX0 + 40}px;width:{PX1 - PX0 - 80}px;top:{TOP + 58}px;height:{BOT - TOP - 104}px;z-index:2;color:#2b1d12}}
    .run{{font:13px 'FellSC',serif;text-align:center;letter-spacing:2px;color:#6b4a2a;margin:2px 0 0}}
    .title{{font:31px/1.05 'Fraktur',serif;text-align:center;color:#8f1d1d;margin:2px 0 6px}}
    .rule{{height:9px;margin:0 30px 9px;background:radial-gradient(circle,#8f1d1d 1.6px,transparent 2px) center/14px 9px repeat-x;border-top:1px solid #8f1d1d;border-bottom:1px solid #8f1d1d}}
    .cols{{column-count:2;column-gap:26px;column-rule:1px solid rgba(143,29,29,.45);height:var(--colh);font-family:'Fell',serif;line-height:1.27}}
    .spell h2{{font:20px/1.1 'Fraktur',serif;color:#8f1d1d;border-bottom:1px solid rgba(143,29,29,.4);padding-bottom:1px;margin-top:2px}}
    .spell h2::before{{content:'\\2766 ';font-family:'Fell';font-size:15px;color:#b88a1e}}
    .school{{font-family:'FellItalic';color:#6b4a2a;margin:1px 0 2px}}
    .stats{{font-size:.93em;margin-bottom:3px;padding:2px 0 3px;border-bottom:1px dotted rgba(107,74,42,.6)}}
    .stats b{{font-family:'FellSC';font-weight:normal;color:#6b4a2a}}
    p{{text-align:justify;hyphens:auto;margin-bottom:3px}} p i{{font-family:'FellItalic';font-style:normal;color:#5a3a1a}}
    p.first::first-letter{{font:2.3em/1 'CinzelDeco',serif;float:left;color:#8f1d1d;background:#f0c43c;border:1.5px solid #2a1a10;
       padding:2px 4px 0;margin:2px 5px 0 0;box-shadow:2px 2px 0 #2a1a10}}
    .spell{{margin-bottom:9px}}
    .frag{{z-index:1;white-space:nowrap;font:italic 12px 'FellItalic',serif;color:#5a3a1a;opacity:.75;left:{PX0 + 50}px;width:{PX1 - PX0 - 100}px;text-align:center}}
    .catch{{z-index:1;font:13px 'FellSC',serif;color:#6b4a2a;right:{W - PX1 + 54}px}}
    '''
    text = (f'<div class="abs text"><div class="run">✠ The Junior Wizard’s Primer · the Fourth Skin ✠</div>{header_art}'
            f'<div class="title">Of the Spells of the First Circle</div><div class="rule"></div>'
            f'<div class="cols">{spells_html("primer")}</div></div>')
    frags = (f'<div class="abs frag" style="top:{TOP + RT - 4}px">…and practise each of them daily, with the windows open.</div>'
             f'<div class="abs catch" style="top:{BOT - RB - 12}px">Of Mishaps, and their Remedies …</div>')
    return page('primer', W, Hh, css, [back, frags, text, front], '#e8d6b0'), W, Hh


# ================================================================ 2. the painted handscroll
def summons():
    W, Hh = 1100, 850
    X0, X1 = 136, 978              # paper
    Y0, Y1 = 112, 732              # mount (brocade bands outside the paper)
    B = 18                         # brocade band
    rnd = random.Random(5)
    g = ['<defs>', noise_filter('silk', 0.02, 9, (0.55, 0.5, 0.42), 0.5), noise_filter('fib', 0.7, 3, (0.5, 0.45, 0.35), 0.4, 2),
         '<radialGradient id="lac" cx=".5" cy=".4" r=".8"><stop offset="0" stop-color="#6b1a14"/><stop offset="1" stop-color="#2a0806"/></radialGradient>',
         '<linearGradient id="mist" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6f8796" stop-opacity=".0"/>'
         '<stop offset=".35" stop-color="#6f8796" stop-opacity=".22"/><stop offset="1" stop-color="#3f5664" stop-opacity=".34"/></linearGradient>',
         '<pattern id="brocade" width="26" height="18" patternUnits="userSpaceOnUse"><rect width="26" height="18" fill="#1f3d6b"/>'
         '<circle cx="6.5" cy="9" r="4.2" fill="none" stroke="#d9b35a" stroke-width="1.3"/><path d="M 4,9 q 2.5,-3 5,0" stroke="#d9b35a" stroke-width="1" fill="none"/>'
         '<circle cx="19.5" cy="0" r="1.6" fill="#d9b35a"/><circle cx="19.5" cy="18" r="1.6" fill="#d9b35a"/></pattern>',
         '<pattern id="wrap" width="30" height="30" patternUnits="userSpaceOnUse"><rect width="30" height="30" fill="#5b2a6e"/>'
         '<circle cx="15" cy="15" r="8" fill="none" stroke="#e8c35a" stroke-width="1.6"/><circle cx="15" cy="15" r="3" fill="#e8c35a"/>'
         '<circle cx="0" cy="0" r="3" fill="#e8c35a"/><circle cx="30" cy="0" r="3" fill="#e8c35a"/><circle cx="0" cy="30" r="3" fill="#e8c35a"/><circle cx="30" cy="30" r="3" fill="#e8c35a"/></pattern>',
         cyl_grad('rollL', '#5b2a6e', True), cyl_grad('rollR', '#efe6cf', True), cyl_grad('jade', '#5fae8a'),
         '<filter id="soft"><feGaussianBlur stdDeviation="7"/></filter>', '</defs>']
    g.append(f'<rect width="{W}" height="{Hh}" fill="url(#lac)"/>')
    for k in range(5):   # lacquer sheen
        g.append(f'<path d="M {-50 + k * 260},{Hh} L {120 + k * 260},0" stroke="#ffffff" stroke-width="{18 + k * 4}" opacity=".035"/>')
    g.append(f'<rect x="{X0}" y="{Y0}" width="{X1 - X0}" height="{Y1 - Y0}" fill="#000" opacity=".5" transform="translate(12,14)" filter="url(#soft)"/>')
    # brocade mount and the silk-paper
    g.append(f'<rect x="{X0}" y="{Y0}" width="{X1 - X0}" height="{Y1 - Y0}" fill="url(#brocade)" stroke="{INK}" stroke-width="3"/>')
    g.append(f'<rect x="{X0}" y="{Y0 + B}" width="{X1 - X0}" height="{Y1 - Y0 - 2 * B}" fill="#f3ead4" stroke="{INK}" stroke-width="2"/>')
    g.append(f'<clipPath id="paper"><rect x="{X0}" y="{Y0 + B}" width="{X1 - X0}" height="{Y1 - Y0 - 2 * B}"/></clipPath><g clip-path="url(#paper)">')
    g.append(f'<rect width="{W}" height="{Hh}" filter="url(#silk)" opacity=".35"/><rect width="{W}" height="{Hh}" filter="url(#fib)" opacity=".25"/>')
    # faint ink-wash mountains and mist along the foot, painted behind the writing
    for (base, amp, seed, op) in ((Y1 - B - 8, 150, 3, .5), (Y1 - B + 6, 95, 8, .8)):
        r2 = random.Random(seed)
        pts = [(X0 - 20, Y1)]
        x = X0 - 20
        while x < X1 + 40:
            x += r2.uniform(40, 90)
            pts.append((x, base - r2.uniform(0.25, 1) * amp))
            x += r2.uniform(30, 70)
            pts.append((x, base - r2.uniform(0, 0.3) * amp))
        pts.append((X1 + 40, Y1))
        g.append(f'<path d="M ' + ' L '.join(f'{a:.0f},{b:.0f}' for a, b in pts) + f' Z" fill="url(#mist)" opacity="{op}"/>')
    for k in range(4):
        yy = Y1 - B - 60 - k * 38
        g.append(f'<path d="M {X0 + rnd.uniform(0, 300):.0f},{yy} q 60,-12 120,0 t 120,0" stroke="#ffffff" stroke-width="10" fill="none" opacity=".5" stroke-linecap="round"/>')
    g.append('</g>')
    # a red seal low on the paper
    back = svg(W, Hh, ''.join(g))

    # the rolls: the rest of the scroll, in its purple wrapper, at left; the rolled paper at right
    o = ['<defs>', cyl_grad('rL', '#5b2a6e', True), cyl_grad('rR', '#efe6cf', True), cyl_grad('rod', '#3b2316', True), '</defs>']
    lx, lr = 104, 32
    o.append(f'<rect x="{lx - lr}" y="{Y0 - 12}" width="{2 * lr}" height="{Y1 - Y0 + 24}" fill="url(#wrap)" stroke="{INK}" stroke-width="3"/>')
    o.append(f'<rect x="{lx - lr}" y="{Y0 - 12}" width="{2 * lr}" height="{Y1 - Y0 + 24}" fill="url(#rL)" opacity=".55"/>')
    o.append(f'<rect x="{lx - lr}" y="{Y0 - 12}" width="{2 * lr}" height="{Y1 - Y0 + 24}" fill="none" stroke="{INK}" stroke-width="3"/>')
    o.append(spiral_end(lx, Y0 - 12, lr, lr * 0.3, '#e9dcbc', 5))
    o.append(f'<rect x="{lx + lr - 6}" y="{Y0 + 30}" width="10" height="{Y1 - Y0 - 60}" fill="#d9b35a" stroke="{INK}" stroke-width="2"/>')   # the gilt edge band
    # the silk cord and its jade toggle, hanging loose
    o.append(f'<path d="M {lx + 4},{(Y0 + Y1) / 2} C {lx + 40},{(Y0 + Y1) / 2 + 70} {lx - 30},{Y1 + 10} {lx + 6},{Y1 + 34}" stroke="{INK}" stroke-width="8" fill="none" stroke-linecap="round"/>'
             f'<path d="M {lx + 4},{(Y0 + Y1) / 2} C {lx + 40},{(Y0 + Y1) / 2 + 70} {lx - 30},{Y1 + 10} {lx + 6},{Y1 + 34}" stroke="#c9a2e0" stroke-width="4" fill="none" stroke-linecap="round"/>')
    o.append(f'<rect x="{lx - 9}" y="{Y1 + 28}" width="30" height="16" rx="8" fill="url(#jade)" stroke="{INK}" stroke-width="2.6"/>')
    for k in range(5):
        o.append(f'<path d="M {lx + 6 + (k - 2) * 3},{Y1 + 44} L {lx + 6 + (k - 2) * 4.5},{Y1 + 66}" stroke="#a16cc4" stroke-width="2.4" stroke-linecap="round"/>')
    rx_, rr = 994, 22
    o.append(f'<rect x="{rx_ - 7}" y="{Y0 - 34}" width="14" height="{Y1 - Y0 + 68}" fill="url(#rod)" stroke="{INK}" stroke-width="2.6"/>')
    for ey in (Y0 - 40, Y1 + 40):
        o.append(f'<ellipse cx="{rx_}" cy="{ey}" rx="15" ry="10" fill="url(#jade)" stroke="{INK}" stroke-width="3"/>'
                 f'<ellipse cx="{rx_ - 4}" cy="{ey - 3}" rx="5" ry="2.5" fill="#d8f5e6" opacity=".8"/>')
    o.append(f'<rect x="{rx_ - rr}" y="{Y0 - 6}" width="{2 * rr}" height="{Y1 - Y0 + 12}" fill="url(#rR)" stroke="{INK}" stroke-width="3"/>')
    o.append(f'<rect x="{rx_ - rr}" y="{Y0 - 6}" width="{2 * rr}" height="{B + 6}" fill="url(#brocade)" opacity=".85"/>'
             f'<rect x="{rx_ - rr}" y="{Y1 - B}" width="{2 * rr}" height="{B + 6}" fill="url(#brocade)" opacity=".85"/>'
             f'<rect x="{rx_ - rr}" y="{Y0 - 6}" width="{2 * rr}" height="{Y1 - Y0 + 12}" fill="url(#rR)" opacity=".45"/>'
             f'<rect x="{rx_ - rr}" y="{Y0 - 6}" width="{2 * rr}" height="{Y1 - Y0 + 12}" fill="none" stroke="{INK}" stroke-width="3"/>')
    o.append(spiral_end(rx_, Y0 - 6, rr, rr * 0.3, '#efe6cf', 4))
    front = svg(W, Hh, ''.join(o), z=3)

    # the painted vignette: a Black summoner calling a cat familiar out of a cloud
    vw, vh = 230, 128
    v = [party.defs(party.STYLES['bold'])]
    v.append(f'<path d="M 120,96 q -14,-26 12,-34 q 6,-26 34,-18 q 18,-20 40,0 q 26,-2 22,24 q 18,14 -2,30 Z" fill="#ffffff" stroke="{INK}" stroke-width="3" opacity=".95"/>')
    v.append(f'<path d="M 108,104 q 30,-12 60,0 t 60,0" stroke="#9fb7c9" stroke-width="3" fill="none"/>')
    # the cat, sitting up on the cloud, tail curled
    cat = (f'<path d="M -2,0 Q -18,-2 -16,-16 Q -14,-24 -8,-22" stroke="{INK}" stroke-width="9" fill="none" stroke-linecap="round"/>'
           f'<path d="M -2,0 Q -18,-2 -16,-16 Q -14,-24 -8,-22" stroke="#f0a050" stroke-width="5" fill="none" stroke-linecap="round"/>'
           f'<path d="M -12,0 Q -14,-22 0,-26 Q 14,-22 12,0 Z" fill="#f0a050" stroke="{INK}" stroke-width="3"/>'
           f'<path d="M -4,-6 Q 0,-14 4,-6" stroke="#ffe2b8" stroke-width="4" fill="none"/>'
           f'<circle cx="0" cy="-34" r="12" fill="#f0a050" stroke="{INK}" stroke-width="3"/>'
           f'<path d="M -10,-40 L -11,-53 L -2,-45 Z M 10,-40 L 11,-53 L 2,-45 Z" fill="#f0a050" stroke="{INK}" stroke-width="2.6"/>'
           f'<circle cx="-4.5" cy="-35" r="2.2" fill="{INK}"/><circle cx="4.5" cy="-35" r="2.2" fill="{INK}"/>'
           f'<path d="M -2,-30 q 2,2 4,0" stroke="{INK}" stroke-width="1.6" fill="none"/>'
           f'<path d="M -16,-31 L -8,-31 M -16,-27 L -8,-29 M 16,-31 L 8,-31 M 16,-27 L 8,-29" stroke="{INK}" stroke-width="1.2"/>')
    v.append(f'<g transform="translate(176,78)">{cat}</g>')
    for (sx, sy, sr) in ((150, 36, 4), (214, 26, 3.4), (132, 58, 3), (226, 52, 2.6)):
        v.append(f'<path d="M {sx},{sy - sr * 2} L {sx + sr * .5},{sy} L {sx},{sy + sr * 2} L {sx - sr * .5},{sy} Z M {sx - sr * 2},{sy} L {sx},{sy + sr * .5} '
                 f'L {sx + sr * 2},{sy} L {sx},{sy - sr * .5} Z" fill="#e8c35a" stroke="{INK}" stroke-width="1"/>')
    v.append(f'<path d="M 74,52 q 18,-10 36,4" stroke="#7a5bd6" stroke-width="3" fill="none" stroke-dasharray="3 5" stroke-linecap="round"/>')
    v.append(figure_svg(56, 122, 0.88, 'Black', 'offer', '#5b2a6e', '#e8c35a', flip=1, look=-10, robe=True))
    vignette = f'<svg class="vig" viewBox="0 0 {vw} {vh}">{"".join(v)}</svg>'

    css = f'''
    .text{{left:{X0 + 52}px;width:{X1 - X0 - 124}px;top:{Y0 + B + 16}px;height:{Y1 - Y0 - 2 * B - 30}px;z-index:2;color:#1c1a24}}
    .cols{{column-count:4;column-gap:22px;column-rule:1px solid rgba(28,26,36,.35);height:100%;font-family:'Mincho',serif;line-height:1.26}}
    .vig{{display:block;width:100%;height:auto;margin:0 auto 4px}}
    .spell{{margin-bottom:8px}}
    .spell h2{{font:16px/1.15 'ZenOld',serif;color:#1c1a24;padding:0 0 2px;border-bottom:2px solid #c0281e;letter-spacing:.5px}}
    .spell h2::before{{content:'';display:inline-block;width:9px;height:9px;background:#c0281e;margin-right:6px;transform:rotate(45deg) translateY(-2px)}}
    .school{{font-style:italic;color:#6b2d26;margin:2px 0}} .school i{{font-style:italic}}
    .stats{{font-size:.92em;padding:2px 0 3px;margin-bottom:3px;border-bottom:1px solid rgba(28,26,36,.3)}} .stats b{{font-family:'MinchoBold';color:#3c2f4a}}
    p{{text-align:justify;hyphens:auto;margin-bottom:3px}} p b{{font-family:'MinchoBold'}} p i{{color:#6b2d26}}
    .slip{{z-index:2;right:{W - X1 + 14}px;top:{Y0 + B + 14}px;width:46px;height:{Y1 - Y0 - 2 * B - 110}px;background:#dfe9ee;
       border:2.5px solid #1c1a24;box-shadow:3px 3px 0 #1c1a24;writing-mode:vertical-rl;text-align:center;
       font:21px/46px 'ZenOld',serif;letter-spacing:3px;color:#1c1a24}}
    .slip small{{font:11px 'Mincho',serif;letter-spacing:2px;color:#6b2d26}}
    .chop{{z-index:2;right:{W - X1 + 20}px;top:{Y1 - B - 84}px;width:40px;height:40px;background:#c0281e;border-radius:4px;opacity:.9}}
    .frag{{z-index:1;font:8px/1.26 'Mincho',serif;color:#1c1a24;opacity:.6;width:{X0 + 36 - 104}px;height:{Y1 - Y0 - 2 * B - 30}px;overflow:hidden;text-align:right}}
    '''
    frag_txt = ('…and before any of these, the novice learns to listen. A summons is an invitation and never a command; '
                'what answers a courteous call stays longer, and works more gladly. Set out water, and a little bread. ') * 6
    text = (f'<div class="abs text"><div class="cols">{vignette}{spells_html("summons")}</div></div>'
            f'<div class="abs slip">Selected Summons for Novices</div>'
            f'<div class="abs chop"><svg width="40" height="40"><path d="M 9,29 q 0,-18 12,-18 q 12,0 12,11 q 0,8 -8,8 q -6,0 -6,-6" stroke="#f3ead4" stroke-width="3" fill="none"/></svg></div>'
            f'<div class="abs frag" style="left:104px;top:{Y0 + B + 16}px">{frag_txt}</div>')
    return page('summons', W, Hh, css, [back, text, front], '#e8c9b8'), W, Hh


# ================================================================ 3. the papyrus
def glyph(kind, x, y, s=1.0):
    """Painted signs for the frieze: dragon-age motifs, not real hieroglyphs."""
    k = f'<g transform="translate({x},{y}) scale({s})">'
    st = f'stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"'
    if kind == 'sun':
        k += f'<circle r="9" fill="#c8342b" {st}/><path d="M -13,6 Q 0,-2 13,6" fill="none" {st}/>'
    elif kind == 'moon':
        k += f'<path d="M 3,-10 A 10,10 0 1 0 3,10 A 7.5,7.5 0 1 1 3,-10 Z" fill="#e9eef4" {st}/>'
    elif kind == 'ring':
        k += f'<circle r="8" fill="none" stroke="{INK}" stroke-width="6"/><circle r="8" fill="none" stroke="#1f5f9e" stroke-width="3"/><path d="M 5,-8 L 11,-11 L 9,-4 Z" fill="#1f5f9e" {st}/>'
    elif kind == 'eye':
        k += f'<path d="M -12,0 Q 0,-10 12,0 Q 0,8 -12,0 Z" fill="#f3ead4" {st}/><circle r="4" fill="#c89a2e" {st}/><path d="M 0,-3 L 0,3" stroke="{INK}" stroke-width="2"/><path d="M -6,5 Q -6,12 -11,12" fill="none" {st}/>'
    elif kind == 'flask':
        k += f'<path d="M -3,-12 L 3,-12 L 3,-4 L 10,9 Q 10,12 6,12 L -6,12 Q -10,12 -10,9 L -3,-4 Z" fill="#3f8a6a" {st}/><path d="M -7,5 L 7,5" stroke="#bfe8d0" stroke-width="2"/>'
    elif kind == 'water':
        k += f'<path d="M -12,-5 l 4,-4 l 4,4 l 4,-4 l 4,4 l 4,-4 l 4,4 M -12,3 l 4,-4 l 4,4 l 4,-4 l 4,4 l 4,-4 l 4,4" fill="none" stroke="#1f5f9e" stroke-width="2.6"/>'
    elif kind == 'star':
        k += f'<path d="M 0,-11 L 3,-3 L 11,0 L 3,3 L 0,11 L -3,3 L -11,0 L -3,-3 Z" fill="#c89a2e" {st}/>'
    elif kind == 'dragon':
        k += (f'<path d="M -12,6 Q -8,-8 4,-8 L 12,-5 L 6,-1 L 12,2 Q 2,6 -2,2 Q -6,8 -12,6 Z" fill="#3f7a4a" {st}/>'
              f'<path d="M -2,-8 L 0,-14 L 3,-8" fill="#f0c43c" {st}/><circle cx="4" cy="-4" r="1.4" fill="{INK}"/>')
    elif kind == 'alembic':
        k += (f'<circle cy="4" r="8" fill="#c8342b" {st}/><path d="M -4,-3 Q 0,-14 6,-10 L 14,-2" fill="none" stroke="{INK}" stroke-width="4"/>'
              f'<path d="M -4,-3 Q 0,-14 6,-10 L 14,-2" fill="none" stroke="#c89a2e" stroke-width="2"/>')
    elif kind == 'feather':
        k += f'<path d="M 0,12 Q -8,0 0,-12 Q 8,0 0,12 Z" fill="#f3ead4" {st}/><path d="M 0,12 L 0,-12" stroke="{INK}" stroke-width="1.2"/>'
    return k + '</g>'


def alchemy():
    W, Hh = 1100, 850
    X0, X1 = 150, 976
    Y0, Y1 = 104, 748
    rnd = random.Random(21)
    g = ['<defs>', noise_filter('stain', 0.01, 12, (0.35, 0.22, 0.08), 0.8), noise_filter('speck', 0.85, 5, (0.3, 0.2, 0.1), 0.6, 2),
         '<linearGradient id="sand" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d2ad73"/><stop offset="1" stop-color="#9c7440"/></linearGradient>',
         '<radialGradient id="vign" cx=".5" cy=".5" r=".75"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#3a2410" stop-opacity=".5"/></radialGradient>',
         '<filter id="soft"><feGaussianBlur stdDeviation="7"/></filter>']
    # papyrus fibres: horizontal strips over vertical ones
    fib = ['<pattern id="fibH" width="400" height="200" patternUnits="userSpaceOnUse">']
    y = 0
    while y < 200:
        h = rnd.uniform(3, 9)
        fib.append(f'<rect x="0" y="{y:.1f}" width="400" height="{h:.1f}" fill="{rnd.choice(["#e8d29a", "#e4cd92", "#ebd6a2", "#e1c98e"])}"/>')
        y += h
    fib.append('</pattern><pattern id="fibV" width="200" height="400" patternUnits="userSpaceOnUse">')
    x = 0
    while x < 200:
        w_ = rnd.uniform(3, 10)
        fib.append(f'<rect x="{x:.1f}" y="0" width="{w_:.1f}" height="400" fill="{rnd.choice(["#7a5a2a", "#a07a3a", "#ffffff"])}" opacity=".05"/>')
        x += w_
    fib.append('</pattern>')
    g += fib + [cyl_grad('rP', '#e2ca8c', True), '</defs>']
    g.append(f'<rect width="{W}" height="{Hh}" fill="url(#sand)"/><rect width="{W}" height="{Hh}" filter="url(#speck)" opacity=".5"/>')
    g.append(f'<rect width="{W}" height="{Hh}" fill="url(#vign)"/>')
    top = wobble(X0, Y0, X1, Y0, 4, 40, 31, vertical=False)
    bot = wobble(X1, Y1, X0, Y1, 4, 40, 32, vertical=False)
    # a bite out of the top edge, and a little tear low down
    top = [(a, b + (14 * math.exp(-((a - 640) / 22) ** 2))) for a, b in top]
    d = 'M ' + ' L '.join(f'{a:.1f},{b:.1f}' for a, b in top + bot) + ' Z'
    g.append(f'<path d="{d}" fill="#000" opacity=".45" transform="translate(10,12)" filter="url(#soft)"/>')
    g.append(f'<path d="{d}" fill="url(#fibH)" stroke="{INK}" stroke-width="3"/>')
    g.append(f'<clipPath id="sheet"><path d="{d}"/></clipPath><g clip-path="url(#sheet)">'
             f'<rect width="{W}" height="{Hh}" fill="url(#fibV)"/><rect width="{W}" height="{Hh}" filter="url(#stain)" opacity=".5"/>')
    for jx in (420, 712):   # the joins between sheets
        g.append(f'<rect x="{jx}" y="0" width="14" height="{Hh}" fill="#b8975a" opacity=".22"/><path d="M {jx},0 L {jx},{Hh}" stroke="#8a6a32" stroke-width="1" opacity=".5"/>')
    g.append(f'<path d="M {X0},{Y0} L {X1},{Y0} L {X1},{Y0 + 26} L {X0},{Y0 + 26} Z" fill="#7a5a2a" opacity=".12"/></g>')
    # friezes, top and bottom, between double rules: painted signs of the ages
    signs = ['sun', 'dragon', 'flask', 'eye', 'ring', 'alembic', 'water', 'star', 'feather', 'moon']
    for (fy, seed) in ((Y0 + 34, 1), (Y1 - 34, 4)):
        for dy in (-20, -16, 16, 20):
            g.append(f'<path d="M {X0 + 18},{fy + dy} L {X1 - 18},{fy + dy}" stroke="{INK if abs(dy) == 20 else "#b8322a"}" stroke-width="{2 if abs(dy) == 20 else 1.4}"/>')
        n = int((X1 - X0 - 60) / 38)
        for k in range(n):
            gx = X0 + 40 + k * (X1 - X0 - 80) / (n - 1)
            if seed == 1 and 526 < gx < 774:
                continue     # leave room for the cartouche
            g.append(glyph(signs[(k + seed) % len(signs)], gx, fy, 0.9))
    # the cartouche with the book's name, set into the top frieze
    cx, cy = 650, Y0 + 34
    g.append(f'<rect x="{cx - 98}" y="{cy - 17}" width="196" height="34" rx="17" fill="#f3e4b8" stroke="{INK}" stroke-width="3.2"/>'
             f'<rect x="{cx + 98}" y="{cy - 17}" width="7" height="34" fill="{INK}"/>')
    back = svg(W, Hh, ''.join(g))

    # the rolls: thick at left (the rest of the text), thin at right
    o = ['<defs>', cyl_grad('rP2', '#dcc283', True), '</defs>']
    for (rx_, rr, ext) in ((118, 36, 8), (996, 18, 4)):
        o.append(f'<rect x="{rx_ - rr}" y="{Y0 - ext}" width="{2 * rr}" height="{Y1 - Y0 + 2 * ext}" fill="url(#rP2)" stroke="{INK}" stroke-width="3"/>')
        for k in range(rr // 6):
            xx = rx_ - rr + 5 + k * 12
            o.append(f'<path d="M {xx},{Y0} L {xx + 2},{Y1}" stroke="#a88a50" stroke-width="1" opacity=".5"/>')
        o.append(spiral_end(rx_, Y0 - ext, rr, rr * 0.28, '#e9d49c', 4 if rr > 20 else 3))
    # a reed pen and an ink palette set down beside it
    o.append(f'<g transform="translate(1032,560) rotate(-12)"><rect x="-9" y="0" width="18" height="120" rx="4" fill="#c4995a" stroke="{INK}" stroke-width="2.6"/>'
             f'<circle cx="0" cy="22" r="5" fill="#b8322a" stroke="{INK}" stroke-width="1.6"/><circle cx="0" cy="40" r="5" fill="{INK}"/></g>')
    o.append(f'<path d="M 1018,700 L 1074,560" stroke="{INK}" stroke-width="7" stroke-linecap="round"/><path d="M 1018,700 L 1074,560" stroke="#d8b878" stroke-width="3.6" stroke-linecap="round"/>')
    front = svg(W, Hh, ''.join(o), z=3)

    # vignette: a Yellow alchemist offering a flask at the alembic, in profile, papyrus-painting fashion
    vw, vh = 196, 118
    v = [party.defs(party.STYLES['bold'])]
    v.append(f'<path d="M 120,112 L 180,112 L 176,104 L 124,104 Z" fill="#8a5a2b" stroke="{INK}" stroke-width="2.4"/>')
    v.append(f'<path d="M 132,104 L 136,84 M 168,104 L 164,84" stroke="{INK}" stroke-width="3"/>')
    v.append(f'<path d="M 140,90 Q 150,100 160,90" fill="#ff8a3a" stroke="{INK}" stroke-width="2"/>')
    v.append(f'<circle cx="150" cy="70" r="16" fill="#c8342b" stroke="{INK}" stroke-width="3"/>')
    v.append(f'<path d="M 156,56 Q 166,34 182,38 L 190,58" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
             f'<path d="M 156,56 Q 166,34 182,38 L 190,58" fill="none" stroke="#c89a2e" stroke-width="3.6" stroke-linecap="round"/>')
    for (bx, by, br) in ((144, 40, 4), (138, 28, 3), (148, 18, 2.4)):
        v.append(f'<circle cx="{bx}" cy="{by}" r="{br}" fill="#bfe8d0" stroke="{INK}" stroke-width="1.4"/>')
    v.append(figure_svg(64, 114, 0.84, 'Yellow', 'offer', '#efe4cc', '#c8342b', flip=1, look=-6))
    v.append(f'<g transform="translate(98,62) scale(.8)">{glyph("flask", 0, 0)}</g>')
    vignette = f'<svg class="vig" viewBox="0 0 {vw} {vh}">{"".join(v)}</svg>'

    css = f'''
    .text{{left:{X0 + 56}px;width:{X1 - X0 - 82}px;top:{Y0 + 70}px;height:{Y1 - Y0 - 140}px;z-index:2;color:#241a10}}
    .cols{{column-count:4;column-gap:24px;column-rule:3px double rgba(184,50,42,.75);height:100%;font-family:'Corm',serif;line-height:1.22}}
    .vig{{display:block;width:100%;height:auto;margin:0 auto 4px}}
    .spell{{margin-bottom:9px}}
    .spell h2{{font:16.5px/1.1 'Cinzel',serif;color:#b8322a;letter-spacing:.5px}}
    .school{{font-family:'CormItalic';color:#b8322a;margin:1px 0 2px}}
    .stats{{padding:1px 0 3px;margin-bottom:3px;border-bottom:1px solid rgba(36,26,16,.35)}} .stats b{{font-family:'CormBold';font-weight:normal}}
    p{{text-align:justify;hyphens:auto;margin-bottom:3px}} p b{{font-family:'CormBold';font-weight:normal}} p i{{font-family:'CormItalic';font-style:normal;color:#b8322a}}
    .cart{{z-index:2;left:552px;width:196px;top:{Y0 + 34 - 17}px;height:34px;text-align:center;font:17px/34px 'Cinzel',serif;color:#241a10;letter-spacing:1px}}
    .frag{{z-index:1;font:10px/1.22 'Corm',serif;color:#241a10;opacity:.6;width:{X0 + 40 - 118}px;overflow:hidden;text-align:right}}
    '''
    frag_txt = ('…so the seventh tincture is made, and set aside to cool. These are the workings of the hand; '
                'now follow the workings of the word, which the student must copy out fair, in red and black. ') * 6
    text = (f'<div class="abs text"><div class="cols">{vignette}{spells_html("alchemy")}</div></div>'
            f'<div class="abs cart">Practical Alchemy</div>'
            f'<div class="abs frag" style="left:118px;top:{Y0 + 70}px;height:{Y1 - Y0 - 140}px">{frag_txt}</div>')
    return page('alchemy', W, Hh, css, [back, text, front]), W, Hh


# ================================================================ render
FIT_JS = '''() => {
  const el = document.querySelector('.cols');
  const ok = () => el.scrollWidth <= el.clientWidth + 1 && el.scrollHeight <= el.clientHeight + 1;
  let lo = 6, hi = 16;
  for (let i = 0; i < 18; i++) { const m = (lo + hi) / 2; el.style.fontSize = m + 'px'; if (ok()) lo = m; else hi = m; }
  el.style.fontSize = lo + 'px';
  return lo;
}'''


def render(key, maker):
    from playwright.sync_api import sync_playwright
    html_, W, Hh = maker()
    os.makedirs(os.path.join(HERE, 'build'), exist_ok=True)
    os.makedirs(os.path.join(HERE, 'output'), exist_ok=True)
    path = os.path.join(HERE, f'{key}.build.html')   # beside fonts/, so the font urls resolve
    open(path, 'w').write(html_)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': W, 'height': Hh}, device_scale_factor=3)
        pg.goto('file://' + path)
        pg.evaluate('document.fonts.ready')
        pg.wait_for_timeout(400)
        if key == 'primer':   # the header takes a share of the text box; columns get the rest
            pg.evaluate('''() => { const t = document.querySelector('.text'), c = document.querySelector('.cols');
                c.style.setProperty('--colh', (t.clientHeight - c.offsetTop) + 'px'); }''')
        size = pg.evaluate(FIT_JS)
        pg.wait_for_timeout(200)
        pg.screenshot(path=os.path.join(HERE, 'output', f'{key}.png'))
        pg.pdf(path=os.path.join(HERE, 'output', f'{key}.pdf'), width=f'{W}px', height=f'{Hh}px', print_background=True, page_ranges='1')
        b.close()
    os.replace(path, os.path.join(HERE, 'build', f'{key}.html'))
    print(key, f'body text {size:.2f}px')


MAKERS = {'primer': primer, 'summons': summons, 'alchemy': alchemy}

if __name__ == '__main__':
    for k in (sys.argv[1:] or MAKERS):
        render(k, MAKERS[k])
