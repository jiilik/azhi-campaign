"""Dragonborn form details shared by every Saturday-Morning Bold drawing (2026-11-12, Troy):
Red a touch larger and Blue a touch smaller; Green's prehensile tail holding an everyday thing
(never a weapon or a shield); webbed fingers and toes for Blue and Indigo; the White form's
Spectral Wings. Used by party.figure() (adventurers: colour wheel, adventuring scenes) and by
tapestry_lib.person() (the tapestries). See art/STYLE.md, "Dragonborn by form"."""
import math, random
import numpy as np
from party import STYLES, P, limb, circ, glow, mix, uid

INK = STYLES['bold']['line']


# ---------------------------------------------------------------- geometry
def catmull(pts, n=200):
    pts = np.array(pts, float)
    if len(pts) == 2:
        return np.linspace(pts[0], pts[1], n)
    Q = np.vstack([pts[0] * 2 - pts[1], pts, pts[-1] * 2 - pts[-2]])
    seg = len(pts) - 1
    out = []
    for i in range(seg):
        p0, p1, p2, p3 = Q[i], Q[i + 1], Q[i + 2], Q[i + 3]
        for t in np.linspace(0, 1, max(2, n // seg), endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2
                              + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(pts[-1])
    return np.array(out)


def dpath(arr, close=True):
    s = 'M ' + ' L '.join(f'{x:.1f},{y:.1f}' for x, y in arr)
    return s + (' Z' if close else '')


def frame(C):
    T = np.gradient(C, axis=0)
    T /= np.maximum(np.linalg.norm(T, axis=1)[:, None], 1e-9)
    N = np.stack([-T[:, 1], T[:, 0]], 1)
    return T, N


def tube_outline(C, w):
    T, N = frame(C)
    a = C + N * (w / 2)[:, None]
    b = C - N * (w / 2)[:, None]
    # round caps
    return np.vstack([a, b[::-1]])


SIZE_K = {'Red': 1.07, 'Blue': 0.93}        # Red (Large) a touch bigger, Blue (Small) a touch smaller
WEBBED = ('Blue', 'Indigo')                 # Amphibious / Deep-Born: webbed fingers and toes
TAIL_ITEMS = ('flower', 'cup', 'lantern', 'basket', 'fruit', 'bell', 'quill', 'parasol', 'censer', 'scroll')


def _unit(a, b):
    d = np.array(b, float) - np.array(a, float)
    return d / (np.linalg.norm(d) + 1e-9)


def _rot(v, a):
    c, s_ = math.cos(a), math.sin(a)
    return (v[0] * c - v[1] * s_, v[0] * s_ + v[1] * c)


def _hand(h, el, fill, webbed, sty, detail):
    """A hand: a plain mitt when small, three fingers when the figure is big enough to show them."""
    if not detail:
        return circ(h[0], h[1], 3.8, fill, sty)
    d = _unit(el, h)
    tips = [(h[0] + v[0] * 6.4, h[1] + v[1] * 6.4) for v in (_rot(d, a) for a in (-0.62, 0, 0.62))]
    o = ''
    if webbed:
        mids = []
        for a, b in ((tips[0], tips[1]), (tips[1], tips[2])):
            m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
            mids.append((m[0] * 0.72 + h[0] * 0.28, m[1] * 0.72 + h[1] * 0.28))
        o += P(f'M {h[0]:.1f},{h[1]:.1f} L {tips[0][0]:.1f},{tips[0][1]:.1f} Q {mids[0][0]:.1f},{mids[0][1]:.1f} {tips[1][0]:.1f},{tips[1][1]:.1f} '
               f'Q {mids[1][0]:.1f},{mids[1][1]:.1f} {tips[2][0]:.1f},{tips[2][1]:.1f} Z', mix(fill, '#ffffff', .38), dict(sty, stroke=sty['stroke'] * 0.45))
    for t in tips:
        o += limb([h, t], 2.3, fill, dict(sty, stroke=sty['stroke'] * 0.6))
    o += circ(h[0], h[1], 3.4, fill, sty)
    return o


def _foot(x0, fill, webbed, sty, detail):
    """A foot on the ground at y = 0, toes forward (+x). Webbed for Blue and Indigo."""
    if not detail:
        return P(f'M {x0 - 9},0 Q {x0 - 6},-6 {x0 + 4},-3 L {x0 + 6},0 Z', fill, sty)
    a = x0 - 9
    if webbed:
        tips = [(a + 21, -8.5), (a + 23, -4.2), (a + 22.5, 0)]
        o = P(f'M {a},0 Q {a + 1},-7 {a + 9},-6 L {tips[0][0]},{tips[0][1]} Q {a + 19},-5.5 {tips[1][0]},{tips[1][1]} '
              f'Q {a + 19.5},-1.8 {tips[2][0]},{tips[2][1]} Z', mix(fill, '#ffffff', .38), sty)
        for t in tips:
            o += limb([(a + 9, -3), t], 2.0, fill, dict(sty, stroke=sty['stroke'] * 0.55))
        return o + P(f'M {a},0 Q {a + 1},-7 {a + 9},-6 L {a + 11},0 Z', fill, sty)
    o = P(f'M {a},0 Q {a + 1},-7 {a + 9},-6 L {a + 14},-6.4 Q {a + 18},-6 {a + 16},-3.6 Q {a + 21},-3.4 {a + 19.4},-1.2 '
          f'Q {a + 22},-0.6 {a + 19},0 Z', fill, sty)
    for (cx_, cy_) in ((a + 16.5, -6.2), (a + 20, -3.2), (a + 21, -0.4)):
        o += f'<path d="M {cx_ - 1.6},{cy_ - 1.2} L {cx_ + 2.4},{cy_ + 0.4} L {cx_ - 1.4},{cy_ + 1.4} Z" fill="#f3ead2" stroke="{INK}" stroke-width="{sty["stroke"] * 0.4:.2f}"/>'
    return o


def tail_item_svg(kind, sty):
    """Something held by a Green dragonborn's tail, gripped at (0, 0). Never a weapon or a shield."""
    th = dict(sty, stroke=sty['stroke'] * 0.7)
    if kind == 'flower':
        o = limb([(0, 0), (3, -12), (2, -24)], 2.2, '#3f8a3c', th)
        o += P('M 2,-12 Q 12,-16 14,-10 Q 8,-8 2,-12 Z', '#5aa64a', th)
        for k in range(5):
            a = math.radians(k * 72 - 90)
            o += f'<ellipse cx="{2 + 5.4 * math.cos(a):.1f}" cy="{-26 + 5.4 * math.sin(a):.1f}" rx="4.4" ry="3" transform="rotate({k * 72} {2 + 5.4 * math.cos(a):.1f} {-26 + 5.4 * math.sin(a):.1f})" fill="#ff9ec4" stroke="{INK}" stroke-width="{th["stroke"]:.2f}"/>'
        return o + circ(2, -26, 3, '#ffd34d', th)
    if kind == 'cup':
        o = P('M -2,-2 L 16,-2 L 14,10 Q 7,14 0,10 Z', '#f6f1e3', th) + P('M 16,0 Q 22,2 15,7', 'none', th)
        o += f'<path d="M 0,2 L 15,2" stroke="#4fc1b3" stroke-width="2"/>'
        o += f'<path d="M 5,-6 q -4,-5 0,-10 q 4,-5 0,-10 M 11,-6 q -4,-5 0,-10" stroke="#ffffff" stroke-width="2" fill="none" opacity=".85" stroke-linecap="round"/>'
        return o
    if kind == 'lantern':
        o = glow(0, 18, 24, '#ffd27a')
        o += limb([(0, 0), (0, 6)], 1.4, INK, th)
        o += P('M -6,6 L 6,6 L 7,22 L -7,22 Z', '#ffe9a8', th) + P('M -7,4 L 7,4 L 5,7 L -5,7 Z', '#7a5233', th)
        return o + P('M -7,22 L 7,22 L 5,25 L -5,25 Z', '#7a5233', th)
    if kind == 'basket':
        o = f'<path d="M -12,16 Q 0,-6 12,16" stroke="{INK}" stroke-width="5" fill="none"/><path d="M -12,16 Q 0,-6 12,16" stroke="#b07a3c" stroke-width="2.6" fill="none"/>'
        o += circ(-5, 14, 4.6, '#e2432b', th) + circ(3, 13, 4.4, '#ffcf3a', th) + circ(8, 15, 4, '#7bc04a', th)
        o += P('M -14,15 L 14,15 L 11,30 L -11,30 Z', '#c9945a', th)
        return o + f'<path d="M -12,20 L 12,20 M -11,25 L 11,25" stroke="#8a5a2b" stroke-width="1.6"/>'
    if kind == 'fruit':
        return (circ(0, 8, 8, '#e2432b', th) + f'<ellipse cx="-3" cy="5" rx="2.4" ry="1.6" fill="#fff" opacity=".7"/>'
                + P('M 0,0 Q 6,-5 10,-2 Q 5,1 0,0 Z', '#5aa64a', th))
    if kind == 'bell':
        o = P('M -8,16 Q -8,2 0,2 Q 8,2 8,16 L 10,18 L -10,18 Z', '#e8c35a', th) + circ(0, 19, 2.4, '#9a7428', th)
        return o + f'<path d="M -13,6 q -3,4 0,8 M 13,6 q 3,4 0,8" stroke="{INK}" stroke-width="1.6" fill="none"/>'
    if kind == 'quill':
        return (P('M 0,0 Q 6,-14 18,-28 Q 10,-12 2,2 Z', '#f6f1e3', th)
                + f'<path d="M 0,2 L 15,-24" stroke="{INK}" stroke-width="1"/>')
    if kind == 'scroll':
        return (f'<g transform="rotate(30)">' + P('M -3,-10 L 3,-10 L 3,10 L -3,10 Z', '#f4ead2', th)
                + circ(0, -10, 3, '#d8c9a3', th) + circ(0, 10, 3, '#d8c9a3', th) + '</g>')
    if kind == 'censer':
        o = f'<path d="M 0,0 L -4,16 M 0,0 L 4,16" stroke="{INK}" stroke-width="1.4"/>'
        o += P('M -8,16 L 8,16 Q 8,26 0,27 Q -8,26 -8,16 Z', '#d4a63c', th) + P('M -6,16 Q 0,9 6,16 Z', '#b07a3c', th)
        return o + ''.join(f'<path d="M {dx},{8 - k * 2} q -5,-6 0,-12 q 5,-6 0,-12" stroke="#e9e4f2" stroke-width="2.4" fill="none" opacity="{0.8 - k * 0.2:.2f}" stroke-linecap="round"/>'
                           for k, dx in enumerate((-4, 3, 9)))
    if kind == 'parasol':
        o = limb([(0, 0), (26, -36)], 2.2, '#7a5233', th)
        cx_, cy_ = 30, -40
        o += P(f'M {cx_ - 30},{cy_ + 4} Q {cx_},{cy_ - 30} {cx_ + 30},{cy_ + 4} Q {cx_ + 22},{cy_} {cx_ + 15},{cy_ + 5} Q {cx_ + 8},{cy_} {cx_},{cy_ + 5} '
               f'Q {cx_ - 8},{cy_} {cx_ - 15},{cy_ + 5} Q {cx_ - 22},{cy_} {cx_ - 30},{cy_ + 4} Z', '#ffb3d1', th)
        o += f'<path d="M {cx_},{cy_ - 22} L {cx_ - 15},{cy_ + 5} M {cx_},{cy_ - 22} L {cx_ + 15},{cy_ + 5}" stroke="#ffffff" stroke-width="2.4"/>'
        return o + circ(cx_, cy_ - 23, 2.4, '#e8c35a', th)
    return ''


def _green_tail(hipY, sy, far, skin, sty, item):
    """The prehensile tail: up and over, its tip curled round whatever it holds like a hand."""
    C = catmull([(-2, hipY + 8), (-24, hipY + 15), (-44, hipY + 5), (-55, hipY - 14), (-57, sy + 2), (-52, sy - 9)], 120)
    w = np.linspace(10, 3.4, len(C))
    o = P(dpath(tube_outline(C, w)), far, sty)
    T, N = frame(C)
    for k in range(10, len(C) - 12, 11):          # a leafy frill along the top of the tail
        n_ = -N[k]
        p_ = C[k] + n_ * w[k] * 0.42
        t_ = T[k]
        o += P(f'M {p_[0]:.1f},{p_[1]:.1f} Q {p_[0] + n_[0] * 7 + t_[0] * 2:.1f},{p_[1] + n_[1] * 7 + t_[1] * 2:.1f} '
               f'{p_[0] + t_[0] * 8:.1f},{p_[1] + t_[1] * 8:.1f} Z', mix(skin, '#c9f08a', .45), dict(sty, stroke=sty['stroke'] * 0.5))
    k = int(len(C) * 0.8)                           # a gold cuff, the embellishment
    a, b = C[k] + N[k] * w[k] * 0.62, C[k] - N[k] * w[k] * 0.62
    o += f'<path d="M {a[0]:.1f},{a[1]:.1f} L {b[0]:.1f},{b[1]:.1f}" stroke="{INK}" stroke-width="5.6" stroke-linecap="round"/>'
    o += f'<path d="M {a[0]:.1f},{a[1]:.1f} L {b[0]:.1f},{b[1]:.1f}" stroke="#e8c35a" stroke-width="3" stroke-linecap="round"/>'
    tip = C[-1]
    grip = (tip[0] + 2, tip[1] - 4)
    if item:
        o += f'<g transform="translate({grip[0]:.1f},{grip[1]:.1f})">{tail_item_svg(item, sty)}</g>'
    # three little tail-fingers curled round the grip
    for (dx, dy) in ((-1, -6), (4, -5), (6, -1)):
        o += limb([tuple(tip), (grip[0] + dx * 0.5, grip[1] + dy * 0.9), (grip[0] + dx, grip[1] + dy * 0.2)], 2.3, skin,
                  dict(sty, stroke=sty['stroke'] * 0.6))
    return o


def spectral_wings(sh, s=1.0, flip=1, spread=1.0, seed=1):
    """Wings of shimmering light (the White form's Spectral Wings), rooted at the shoulder sh."""
    rnd = random.Random(seed)
    gid = uid('spw')
    o = (f'<linearGradient id="{gid}" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#ffffff" stop-opacity=".95"/>'
         f'<stop offset=".5" stop-color="#cdeeff" stop-opacity=".7"/><stop offset="1" stop-color="#e3d2ff" stop-opacity=".45"/></linearGradient>')
    o += glow(sh[0] - 30 * s, sh[1] - 40 * s, 80 * s, '#d8f2ff')
    for (k, sc, ang, op) in ((0, 0.82, -14, 0.55), (1, 1.0, 0, 0.8)):
        g = []
        wrist = (-14 * spread, -64)
        tips = [(-78 * spread, -82), (-92 * spread, -46), (-80 * spread, -12), (-48 * spread, 4)]
        d = f'M 0,0 Q {-4 * spread},{-40} {wrist[0]},{wrist[1]} L {tips[0][0]},{tips[0][1]} '
        prev = tips[0]
        for t in tips[1:]:
            mx, my = (prev[0] + t[0]) / 2 + 10 * spread, (prev[1] + t[1]) / 2 + 6
            d += f'Q {mx},{my} {t[0]},{t[1]} '
            prev = t
        d += 'Q -20,6 0,0 Z'
        g.append(f'<path d="{d}" fill="url(#{gid})" stroke="#9fdcff" stroke-width="{2.4 / s:.2f}" stroke-linejoin="round"/>')
        for t in tips:
            g.append(f'<path d="M {wrist[0]},{wrist[1]} L {t[0]},{t[1]}" stroke="#ffffff" stroke-width="{1.8 / s:.2f}" opacity=".85"/>')
        g.append(f'<path d="M 0,0 Q {-4 * spread},{-40} {wrist[0]},{wrist[1]}" stroke="#ffffff" stroke-width="{3 / s:.2f}" fill="none"/>')
        o += f'<g opacity="{op}" transform="translate({sh[0]},{sh[1]}) scale({s * sc * flip},{s * sc}) rotate({ang})">{"".join(g)}</g>'
    for _ in range(9):                            # shimmer: sparkles shed from the trailing edge
        x_ = sh[0] + flip * rnd.uniform(-110, -20) * s
        y_ = sh[1] + rnd.uniform(-70, 20) * s
        r_ = rnd.uniform(2.5, 5.5) * s
        o += (f'<path d="M {x_:.1f},{y_ - r_:.1f} L {x_ + r_ * .25:.1f},{y_:.1f} L {x_:.1f},{y_ + r_:.1f} L {x_ - r_ * .25:.1f},{y_:.1f} Z '
              f'M {x_ - r_:.1f},{y_:.1f} L {x_:.1f},{y_ + r_ * .25:.1f} L {x_ + r_:.1f},{y_:.1f} L {x_:.1f},{y_ - r_ * .25:.1f} Z" fill="#ffffff" opacity=".9"/>')
    return o
