"""The Tapestry Hall (2026-11-12): six tapestries of Azhi's history, as woven by White monks.

-> output/tapestry_0.png ... tapestry_5.png, output/tapestry_hall.png (all six), and the
Epoch 3 faith icons -> output/icon_black_church.png, icon_cult_of_the_ring.png,
icon_machine_revivalists.png, output/icons_epoch3.png.
Plan and lore checks: art/tapestries.md. Saturday-Morning Bold, the White dragonborn's
favoured style. Run: python3 tapestries.py [0 1 2 ...]
"""
import os, sys, math, random, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE); sys.path.insert(0, HERE)
os.makedirs('build', exist_ok=True); os.makedirs('output', exist_ok=True)
import numpy as np
from tapestry_lib import *          # noqa: F401,F403
from tapestry_lib import catmull, frame, dpath
import party
from party import P, limb, circ, glow, mix, dark, light, uid, sky_dragon, cloud, ridge, poly, wave, FANG, defs

LAPIS, LAPIS_D, TURQ, GOLDO = '#3a3f8f', '#2a2c6a', '#4fc1b3', '#efbe48'


# ============================================================ poses
def pose_sit(head_angle=-8, wings='folded', wing_rot=-12, wing_scale=1.35, tail='curl'):
    tail_pts = {'curl': [(-150, 14), (-120, 22), (-75, 20)], 'up': [(-120, -60), (-110, -10), (-75, 18)]}[tail]
    return dict(spine=tail_pts + [(-40, 0), (-12, -28), (12, -62), (24, -96), (38, -116)],
                widths=[3, 9, 20, 40, 46, 40, 20, 17], head_angle=head_angle, wings=wings, wing_at=0.62,
                wing_rot=wing_rot, wing_scale=wing_scale,
                legs=[(0.52, [(-4, 22), (6, 20)], False), (0.66, [(4, 40), (8, 68)], False),
                      (0.5, [(14, 18), (2, 22), (14, 22)], True), (0.68, [(12, 40), (14, 70)], True)],
                belly=(0.45, 0.95), spikes=12)


def pose_fly(head_angle=10, wings='spread', bank=0):
    return dict(spine=[(-170, 10), (-130, -6), (-80, 4), (-40, 2), (0, -4), (30, -14), (50, -30), (70, -40)],
                widths=[3, 8, 18, 30, 30, 24, 14, 13], head_angle=head_angle, wings=wings, wing_at=0.6,
                wing_rot=bank, legs=[(0.5, [(-10, 16), (-26, 20)], True), (0.72, [(8, 14), (18, 22)], True)],
                belly=(0.4, 0.95))


def pose_back(head_angle=-30):
    """Floating on its back, paws folded on its belly."""
    return dict(spine=[(-150, -30), (-110, -10), (-70, 0), (-35, 4), (0, 4), (30, 0), (52, -10), (66, -26)],
                widths=[3, 9, 20, 32, 34, 28, 15, 14], head_angle=head_angle, wings='folded', wing_at=0.62,
                wing_rot=170, legs=[(0.5, [(-6, -20), (4, -24)], True), (0.72, [(-14, -18), (-22, -16)], True)],
                belly=(0.4, 0.95))


def pose_lounge(head_angle=6):
    """Lying along a surface, chin on its paws, tail dangling."""
    return dict(spine=[(-140, 60), (-130, 20), (-100, 0), (-60, -6), (-20, -8), (20, -8), (46, -6), (60, -2)],
                widths=[3, 8, 18, 30, 32, 28, 15, 14], head_angle=head_angle, wings='folded', wing_at=0.58,
                wing_rot=0, wing_scale=1.15,
                legs=[(0.45, [(4, 10), (18, 10)], True), (0.82, [(16, 8), (34, 8)], True)], belly=(0.4, 0.95))


def pose_cling(head_angle=-20):
    """Clinging upright to something with its front claws, tail hanging."""
    return dict(spine=[(-10, 150), (-14, 110), (-8, 70), (0, 30), (6, 0), (10, -26), (20, -46), (34, -58)],
                widths=[3, 8, 18, 30, 32, 26, 15, 14], head_angle=head_angle, wings='up', wing_at=0.62,
                wing_rot=-90, wing_scale=0.9,
                legs=[(0.42, [(20, 8), (26, 26)], True), (0.8, [(24, -10), (36, -24)], True),
                      (0.8, [(18, -14), (30, -30)], False)], belly=(0.35, 0.95))


def pose_hang(head_angle=10):
    """Hanging by the front claws, body swinging below."""
    return dict(spine=[(40, 150), (20, 120), (0, 90), (-6, 60), (-4, 30), (4, 6), (16, -14), (32, -24)],
                widths=[3, 8, 18, 30, 32, 26, 15, 14], head_angle=head_angle, wings='spread', wing_at=0.62,
                wing_rot=-60, wing_scale=0.75,
                legs=[(0.8, [(4, -30), (2, -50)], True), (0.8, [(14, -28), (16, -48)], False),
                      (0.4, [(16, 14), (26, 30)], True)], belly=(0.35, 0.95))


# ============================================================ Azhi
def azhi_body(spine, w0, w1, fade_from=0.0, legs=(), wings=(), sty_px=4.2, mask_fade=None):
    """Azhi's long body (tail first, neck last), after azhi_cover.py, with stubby wings.

    legs/wings: fractions along the body (0 = tail, 1 = neck)."""
    C = catmull(spine, 1500)
    T, N = frame(C)
    u = np.linspace(0, 1, len(C))
    w = w0 + (w1 - w0) * u ** 0.85
    # N points to the belly side; choose it so the belly faces down on average
    if np.mean(N[:, 1]) < 0:
        N = -N
    sty = dict(party.STYLES['bold'], stroke=sty_px)
    inner = C + N * (w / 2)[:, None]
    outer = C - N * (w / 2)[:, None]
    o = []
    # flame tufts and dorsal crest along the back (behind)
    for i in range(20, len(C) - 20, 22):
        p, n = outer[i], -N[i]
        k = w[i] / 150
        tip = p + n * (34 + 10 * math.sin(i)) * k - T[i] * 22 * k
        b1, b2 = p - T[i] * 16 * k + n * 4 * k, p + T[i] * 16 * k + n * 4 * k
        o.append(P(f'M {b1[0]:.1f},{b1[1]:.1f} Q {p[0] + n[0] * 30 * k:.1f},{p[1] + n[1] * 30 * k:.1f} {tip[0]:.1f},{tip[1]:.1f} '
                   f'Q {p[0] + n[0] * 14 * k + T[i][0] * 10 * k:.1f},{p[1] + n[1] * 14 * k + T[i][1] * 10 * k:.1f} {b2[0]:.1f},{b2[1]:.1f} Z',
                   LAPIS_D, dict(sty, stroke=sty_px * max(k, 0.35))))
    for i in range(160, len(C) - 60, 190):
        p, n = outer[i], -N[i]
        k = w[i] / 150
        for j, (Lr, a) in enumerate([(90, -0.5), (70, 0.15), (55, 0.7)]):
            d = n * math.cos(a) - T[i] * math.sin(a)
            tip = p + d * Lr * k
            m = p + d * Lr * 0.5 * k + T[i] * 14 * k
            o.append(P(f'M {p[0] - T[i][0] * 14 * k:.1f},{p[1] - T[i][1] * 14 * k:.1f} Q {m[0]:.1f},{m[1]:.1f} {tip[0]:.1f},{tip[1]:.1f} '
                       f'Q {m[0] - T[i][0] * 26 * k:.1f},{m[1] - T[i][1] * 26 * k:.1f} {p[0] + T[i][0] * 14 * k:.1f},{p[1] + T[i][1] * 14 * k:.1f} Z',
                       ['#f39c12', '#e74c3c', GOLDO][j], dict(sty, stroke=sty_px * max(k, 0.35))))
    # stubby wings on the back (behind the body)
    for f in wings:
        i = int(f * (len(C) - 1))
        p, n, t = outer[i], -N[i], T[i]
        k = w[i] / 150
        base = p + n * 2
        ang = math.degrees(math.atan2(n[1], n[0])) + 90
        wing = ('M 0,0 Q -14,-46 -40,-70 Q -26,-60 -18,-58 Q -22,-80 -10,-96 Q 0,-70 6,-62 Q 16,-84 34,-92 '
                'Q 30,-50 30,-2 Z')
        o.append(f'<g transform="translate({base[0]:.1f},{base[1]:.1f}) rotate({ang:.1f}) scale({1.25 * k:.3f})">'
                 f'{P(wing, "#5b5fb0", dict(sty, stroke=sty_px / (1.25 * k)))}'
                 f'<path d="M 0,0 L -18,-58 M 2,0 L 6,-62 M 4,0 L 30,-60" stroke="{LAPIS_D}" stroke-width="{3 / (1.25 * k):.2f}"/></g>')
    # stubby clawed legs on the belly side (behind)
    for f in legs:
        i = int(f * (len(C) - 1))
        p, n, t = inner[i], N[i], T[i]
        k = w[i] / 150
        knee = p + n * 50 * k + t * 26 * k
        foot = knee + n * 26 * k - t * 22 * k
        o.append(limb([tuple(p - n * 10 * k), tuple(knee), tuple(foot)], 26 * k, LAPIS_D, dict(sty, stroke=sty_px * max(k, .4))))
        for a in (-0.6, 0, 0.6):
            dv = n * math.cos(a) + t * math.sin(a)
            c = foot + dv * 18 * k
            o.append(limb([tuple(foot), tuple(c)], 6 * k, '#efe4c9', dict(sty, stroke=sty_px * max(k, .4) * 0.6)))
    body = np.vstack([outer, inner[::-1]])
    o.append(P(dpath(body), LAPIS, dict(sty, stroke=0)))
    b_out = C + N * (w * 0.06)[:, None]
    b_in = C + N * (w * 0.44)[:, None]
    o.append(f'<path d="{dpath(np.vstack([b_out, b_in[::-1]]))}" fill="{TURQ}"/>')
    for i in range(0, len(C) - 1, 11):
        a, b = b_out[i], b_in[i]
        o.append(f'<path d="M {a[0]:.1f},{a[1]:.1f} L {b[0]:.1f},{b[1]:.1f}" stroke="{dark(TURQ, .45)}" stroke-width="{max(1.0, 2.4 * w[i] / 150):.2f}"/>')
    for i in range(8, len(C) - 30, 20):
        k = w[i] / 150
        for fr in (0.12, 0.28):
            a = C[i] - N[i] * w[i] * fr
            q1 = a + T[i] * 10 * k - N[i] * 10 * k
            q2 = a - T[i] * 10 * k - N[i] * 10 * k
            o.append(f'<path d="M {q1[0]:.1f},{q1[1]:.1f} Q {a[0]:.1f},{a[1]:.1f} {q2[0]:.1f},{q2[1]:.1f}" '
                     f'stroke="{LAPIS_D}" stroke-width="{max(1.2, 3 * k):.2f}" fill="none" stroke-linecap="round"/>')
    rib = C - N * (w * 0.36)[:, None]
    o.append(f'<path d="{dpath(rib, False)}" stroke="{GOLDO}" stroke-width="{max(2, 5 * w1 / 150):.1f}" fill="none" stroke-dasharray="26 12"/>')
    for i in range(30, len(C) - 30, 60):
        k = w[i] / 150
        a = C[i] - N[i] * w[i] * 0.2
        t, n = T[i] * 13 * k, N[i] * 13 * k
        o.append(f'<path d="M {a[0] + t[0]:.1f},{a[1] + t[1]:.1f} L {a[0] + n[0]:.1f},{a[1] + n[1]:.1f} L {a[0] - t[0]:.1f},{a[1] - t[1]:.1f} '
                 f'L {a[0] - n[0]:.1f},{a[1] - n[1]:.1f} Z" fill="{GOLDO}" stroke="{INK}" stroke-width="{max(1, 2 * k):.2f}"/>'
                 f'<circle cx="{a[0]:.1f}" cy="{a[1]:.1f}" r="{3.5 * k:.1f}" fill="#c0392b"/>')
    o.append(f'<path d="{dpath(body)}" fill="none" stroke="{INK}" stroke-width="{sty_px:.1f}" stroke-linejoin="round"/>')
    g = ''.join(o)
    if mask_fade:
        g = f'<g mask="url(#{mask_fade})">{g}</g>'
    return g, C, T, N, w


def azhi_head(expr='talk'):
    """Azhi's head in local coordinates (neck at the origin, facing +x), after azhi_cover.py.

    A calmer, philosophical version: half-lidded eye, mouth open in speech, a few small fangs,
    and an ear fin behind the eye. Returns (svg, landmarks)."""
    sty = party.STYLES['bold']
    h = []
    lm = {}
    # horn curl
    h.append(P('M 30,-40 C -20,-110 -90,-120 -110,-80 C -125,-50 -90,-30 -70,-48 C -60,-58 -78,-72 -88,-62', '#efe4c9', sty,
               extra='stroke-linecap="round"'))
    # flame tufts
    for j, (bx, by, Lr, a) in enumerate([(10, -55, 110, -2.6), (40, -66, 120, -2.3), (75, -70, 95, -2.0), (0, 20, 100, 2.7)]):
        tip = (bx + Lr * math.cos(a), by + Lr * math.sin(a))
        m = (bx + Lr * 0.5 * math.cos(a + 0.35), by + Lr * 0.5 * math.sin(a + 0.35))
        h.append(P(f'M {bx - 14},{by} Q {m[0]:.1f},{m[1]:.1f} {tip[0]:.1f},{tip[1]:.1f} Q {m[0] + 20:.1f},{m[1] + 8:.1f} {bx + 14},{by + 4} Z',
                   ['#f39c12', '#e74c3c', GOLDO, '#f39c12'][j], sty))
    # lower jaw, gently dropped for speech
    h.append(f'<g transform="rotate({5 if expr == "talk" else 0} 90 10)">')
    h.append(P('M 70,10 C 120,14 170,22 228,38 C 244,43 240,62 222,62 L 150,58 C 90,60 40,62 0,55 L 0,18 Z', LAPIS, sty))
    if expr == 'talk':
        h.append(P('M 130,2 L 244,-4 L 230,26 L 140,14 Z', '#7a1b2a', sty))
        h.append(P('M 150,14 C 180,14 210,18 228,22 L 226,18 C 200,12 172,8 150,9 Z', '#d0566a', dict(sty, stroke=1.2)))  # tongue
    for k in range(2):
        xb = 186 + k * 26
        h.append(f'<path d="M {xb},{20 + k * 2} L {xb + 5},{10 + k * 2} L {xb + 10},{21 + k * 2}" fill="#fff8e6" stroke="{INK}" stroke-width="1.8"/>')
    h.append(f'<path d="M 30,40 C 80,40 140,44 210,52" stroke="{TURQ}" stroke-width="6" fill="none"/>')
    h.append('</g>')
    # upper head
    h.append(P('M 0,-55 C 50,-90 125,-86 165,-56 L 246,-38 C 272,-34 274,-6 250,-2 L 150,-2 C 100,-2 50,4 0,20 Z', LAPIS, sty))
    for k in range(2):
        x = 196 + k * 26
        h.append(f'<path d="M {x},-3 L {x + 5},7 L {x + 10},-3" fill="#fff8e6" stroke="{INK}" stroke-width="1.8"/>')
    h.append(f'<path d="M 30,-14 C 80,-24 140,-22 240,-14" stroke="{GOLDO}" stroke-width="4" fill="none"/>')
    h.append(f'<ellipse cx="256" cy="-24" rx="5" ry="3" fill="{INK}"/>')
    # ear fin (drawn over the head, behind the eye), for the lint-picker
    h.append(P('M 58,-30 C 30,-60 0,-74 -26,-70 C -6,-56 10,-40 26,-18 Z', TURQ, sty))
    h.append(f'<path d="M 50,-30 C 30,-50 10,-60 -10,-64" stroke="{dark(TURQ, .4)}" stroke-width="3" fill="none"/>')
    h.append(f'<ellipse cx="40" cy="-30" rx="8" ry="5" fill="{LAPIS_D}" stroke="{INK}" stroke-width="2"/>')
    lm['ear'] = (36, -40)
    # brow, raised in thought
    h.append(P('M 84,-66 Q 122,-92 166,-66 Q 124,-76 90,-56 Z', LAPIS_D, sty))
    # half-lidded, kindly eye
    h.append(f'<ellipse cx="124" cy="-46" rx="22" ry="13" fill="#ffd34d" stroke="{INK}" stroke-width="3"/>')
    h.append(f'<ellipse cx="128" cy="-43" rx="4.5" ry="9" fill="{INK}"/>')
    h.append(f'<circle cx="121" cy="-47" r="3" fill="#fff"/>')
    if expr == 'talk':   # heavy, kindly lid over the upper half of the eye
        h.append(P('M 101,-46 Q 124,-70 147,-46 Q 124,-52 101,-46 Z', LAPIS_D, dict(sty, stroke=2.4)))
    else:                # wide-eyed wonder
        h.append(f'<circle cx="118" cy="-52" r="4" fill="#fff"/>')
    lm['crown'] = (120, -84)
    lm['mouth'] = (250, 14)
    # barbels (whiskers): long curling gold, the swinger hangs on the lower one
    bars = []
    for (sx, sy_, c1, c2) in [(255, -10, 180, 60), (238, 34, 150, 70)]:
        d = (f'M {sx},{sy_} C {sx - 20},{sy_ + c1 * 0.5} {sx - c1 * 0.6},{sy_ + c2 + 40} {sx - c1},{sy_ + c2} '
             f'C {sx - c1 - 30},{sy_ + c2 - 20} {sx - c1 - 10},{sy_ + c2 - 40} {sx - c1 + 10},{sy_ + c2 - 30}')
        bars.append(d)
        h.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{7 + 3.4}" stroke-linecap="round"/>')
        h.append(f'<path d="{d}" fill="none" stroke="{GOLDO}" stroke-width="7" stroke-linecap="round"/>')
    # lowest point of the upper barbel's first curve, for the swinger
    sx, sy_, c1, c2 = 255, -10, 180, 60
    b0, b1, b2, b3 = np.array([sx, sy_]), np.array([sx - 20, sy_ + c1 * 0.5]), np.array([sx - c1 * 0.6, sy_ + c2 + 40]), np.array([sx - c1, sy_ + c2])
    best = max((((1 - t) ** 3) * b0 + 3 * ((1 - t) ** 2) * t * b1 + 3 * (1 - t) * t * t * b2 + t ** 3 * b3 for t in np.linspace(0, 1, 60)), key=lambda q: q[1])
    lm['barbel_low'] = (float(best[0]), float(best[1]))
    return ''.join(h), lm


def to_scene(lm, ox, oy, hs, flip=-1, rot=0.0):
    x, y = lm
    x, y = x * hs * flip, y * hs
    a = math.radians(rot)
    return (ox + x * math.cos(a) - y * math.sin(a), oy + x * math.sin(a) + y * math.cos(a))


def motion_lines(pts, colour, n=3, gap=9, width=5):
    """Cartoon swooshes trailing along a path (list of points, oldest first)."""
    C = catmull(pts, 80)
    T, N = frame(C)
    o = ''
    for k in range(n):
        off = (k - (n - 1) / 2) * gap
        seg = C[int(len(C) * 0.1 * k): len(C) - int(len(C) * 0.1 * (n - 1 - k)) - 1] + N[int(len(C) * 0.1 * k): len(C) - int(len(C) * 0.1 * (n - 1 - k)) - 1] * off
        d = dpath(seg, False)
        o += f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{width + 3}" stroke-linecap="round" opacity=".9"/>'
        o += f'<path d="{d}" fill="none" stroke="{colour}" stroke-width="{width}" stroke-linecap="round"/>'
    return o


# ============================================================ Epoch 0
def scene0():
    rnd = random.Random(40)
    o = []
    o.append('<defs><radialGradient id="sp0" cx="62%" cy="48%" r="80%"><stop offset="0" stop-color="#2a2160"/>'
             '<stop offset=".6" stop-color="#140f33"/><stop offset="1" stop-color="#07060f"/></radialGradient>'
             '<linearGradient id="fade0" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000"/>'
             '<stop offset=".22" stop-color="#555"/><stop offset=".5" stop-color="#fff"/></linearGradient>'
             '<mask id="m0" maskUnits="userSpaceOnUse" x="0" y="0" width="1200" height="800">'
             '<rect width="1200" height="800" fill="url(#fade0)"/></mask></defs>')
    o.append('<rect width="1200" height="800" fill="url(#sp0)"/>')
    # nebulae and a distant spiral galaxy: the depths of space and time
    o.append(glow(180, 620, 260, '#7b3fa0').replace('.85', '.35'))
    o.append(glow(980, 120, 220, '#2b6fa8').replace('.85', '.3'))
    o.append(glow(420, 160, 180, '#a0405a').replace('.85', '.22'))
    o.append(stars(260, 4, twinkles=16))
    gx, gy = 150, 150
    for k in range(3):
        a0 = k * 2.1
        pts = [(gx + (6 + t * 5) * math.cos(a0 + t * 0.5) * 1.6, gy + (6 + t * 5) * math.sin(a0 + t * 0.5) * 0.7) for t in range(14)]
        o.append(f'<path d="{dpath(np.array(pts), False)}" stroke="#d8c6ff" stroke-width="3" fill="none" opacity=".55" stroke-linecap="round"/>')
    o.append(glow(gx, gy, 30, '#fff1d6'))
    # a moon with a bite taken out of it (Azhi "samples pieces of moons")
    mx, my = 590, 735
    o.append(f'<clipPath id="bite0"><path d="M {mx - 60},{my - 60} L {mx + 60},{my - 60} L {mx + 60},{my + 60} L {mx - 60},{my + 60} Z '
             f'M {mx + 44},{my - 34} a 22,22 0 1 0 0.1,0 Z M {mx + 30},{my - 4} a 16,16 0 1 0 0.1,0 Z" clip-rule="evenodd"/></clipPath>')
    o.append(f'<g clip-path="url(#bite0)">' + circ(mx, my, 44, '#cfc9bd', S(1)) +
             f'<circle cx="{mx - 14}" cy="{my + 8}" r="9" fill="#a9a194"/><circle cx="{mx - 4}" cy="{my - 18}" r="6" fill="#a9a194"/></g>')
    # a comet
    o.append(f'<path d="M 1060,690 Q 1120,640 1190,600" stroke="#bfe8ff" stroke-width="10" fill="none" opacity=".35" stroke-linecap="round"/>'
             f'<path d="M 1060,690 Q 1120,640 1190,600" stroke="#ffffff" stroke-width="3" fill="none" opacity=".7" stroke-linecap="round"/>'
             f'<circle cx="1058" cy="692" r="7" fill="#ffffff" stroke="{INK}" stroke-width="2"/>')

    # a ringed planet far off, and the path of the lazy circles, traced in faint stardust
    px_, py_ = 150, 640
    o.append(glow(px_, py_, 70, '#7fb2e6').replace('.85', '.35'))
    o.append(f'<ellipse cx="{px_}" cy="{py_}" rx="62" ry="13" fill="none" stroke="{INK}" stroke-width="9" transform="rotate(-16 {px_} {py_})"/>'
             f'<ellipse cx="{px_}" cy="{py_}" rx="62" ry="13" fill="none" stroke="#e9c66a" stroke-width="5" transform="rotate(-16 {px_} {py_})"/>')
    o.append(circ(px_, py_, 32, '#5f8fd0', S(1, 3.4)))
    o.append(f'<path d="M {px_ - 30},{py_ - 6} Q {px_},{py_ - 2} {px_ + 30},{py_ - 12}" stroke="#8fb8e8" stroke-width="5" fill="none"/>'
             f'<path d="M {px_ - 26},{py_ + 12} Q {px_},{py_ + 16} {px_ + 26},{py_ + 6}" stroke="#4a76b8" stroke-width="5" fill="none"/>')
    o.append(f'<clipPath id="ringfront0"><rect x="{px_ - 80}" y="{py_ + 2}" width="160" height="60"/></clipPath>'
             f'<g clip-path="url(#ringfront0)"><ellipse cx="{px_}" cy="{py_}" rx="62" ry="13" fill="none" stroke="{INK}" stroke-width="9" transform="rotate(-16 {px_} {py_})"/>'
             f'<ellipse cx="{px_}" cy="{py_}" rx="62" ry="13" fill="none" stroke="#e9c66a" stroke-width="5" transform="rotate(-16 {px_} {py_})"/></g>')
    o.append(f'<ellipse cx="820" cy="470" rx="640" ry="320" fill="none" stroke="#fff4c0" stroke-width="3" stroke-dasharray="2 16" stroke-linecap="round" opacity=".55"/>')

    # ---- Azhi: the body trails up and away into the stars, the face is enormous
    spine = [(-120, 60), (40, 150), (190, 120), (340, 100), (520, 140), (700, 130), (870, 110), (1030, 120), (1180, 190),
             (1250, 320), (1170, 452)]
    body, C, T, N, w = azhi_body(spine, 14, 230, legs=(0.5, 0.84), wings=(0.67, 0.71), sty_px=4.2, mask_fade='m0')
    o.append(body)
    hs = 2.0
    ox, oy = 1170, 470
    head, lm = azhi_head()
    o.append(f'<g transform="translate({ox},{oy}) scale({-hs},{hs})">{head}</g>')
    mouth = to_scene(lm['mouth'], ox, oy, hs)
    ear = to_scene(lm['ear'], ox, oy, hs)
    crown = to_scene(lm['crown'], ox, oy, hs)
    bar = to_scene(lm['barbel_low'], ox, oy, hs)

    # words of wisdom: golden curls drifting from the mouth toward the listener
    for k in range(3):
        x0 = mouth[0] - 30 - k * 70
        y0 = mouth[1] + 10 + k * 8
        o.append(f'<path d="M {x0},{y0} q -18,-22 -36,0 q -18,22 -36,0" stroke="{INK}" stroke-width="9" fill="none" stroke-linecap="round" opacity=".9"/>'
                 f'<path d="M {x0},{y0} q -18,-22 -36,0 q -18,22 -36,0" stroke="{GOLDO}" stroke-width="5" fill="none" stroke-linecap="round"/>')
    for (sx, sy_) in [(mouth[0] - 120, mouth[1] - 40), (mouth[0] - 210, mouth[1] + 46), (mouth[0] - 60, mouth[1] + 56)]:
        o.append(f'<path d="M {sx},{sy_ - 9} L {sx + 2.5},{sy_} L {sx},{sy_ + 9} L {sx - 2.5},{sy_} Z M {sx - 9},{sy_} L {sx},{sy_ + 2.5} L {sx + 9},{sy_} L {sx},{sy_ - 2.5} Z" fill="#fff4c0"/>')

    # ---- the young dragons, playing (none has a colour yet)
    # 1. floating on its back before Azhi's face, listening, eyes closed in contentment
    o.append(dragon(470, 610, 0.9, None, pose_back(-20), flip=1, rot=4, shimmer='all', seed=3, expr='closed'))
    # 2. perched on the crown of Azhi's head, chin up, attentive
    o.append(dragon(crown[0] + 6, crown[1] + 4, 0.72, None, pose_sit(head_angle=-20, wing_rot=-6), flip=-1,
                    shimmer='all', seed=5, expr='open'))
    # 3. picking lint out of Azhi's ear
    o.append(dragon(ear[0] + 40, ear[1] + 76, 0.6, None, pose_cling(-40), flip=-1, rot=8, shimmer='all', seed=8, expr='wide'))
    lx, ly = ear[0] - 2, ear[1] - 4
    for (dx, dy, r) in [(0, 0, 9), (8, -5, 7), (-6, -6, 6), (5, 5, 6)]:
        o.append(f'<circle cx="{lx + dx}" cy="{ly + dy}" r="{r}" fill="#ece6f2" stroke="{INK}" stroke-width="2"/>')
    # 4. swinging from a barbel
    o.append(dragon(bar[0] - 4, bar[1] + 40, 0.5, None, pose_hang(20), flip=-1, rot=14, shimmer='all', seed=11, expr='happy'))
    o.append(f'<path d="M {bar[0] - 70},{bar[1] + 70} q -12,10 -24,0 M {bar[0] - 80},{bar[1] + 88} q -10,8 -20,0" stroke="#fff4c0" stroke-width="3" fill="none" stroke-linecap="round"/>')
    # 5. lounging along Azhi's back, chin on its paws
    i5 = int(0.52 * (len(C) - 1))
    p5 = C[i5] - N[i5] * w[i5] * 0.5
    a5 = math.degrees(math.atan2(T[i5][1], T[i5][0]))
    o.append(dragon(p5[0], p5[1] - 2, 0.52, None, pose_lounge(10), flip=1, rot=a5, shimmer='all', seed=13, expr='happy'))
    # 6 and 7. the future Gold and Silver, chasing each other in great lazy circles around Azhi
    cx, cy, rx, ry = 820, 470, 640, 320
    def orbit(a):
        return (cx + rx * math.cos(a), cy + ry * math.sin(a))
    lead, chase = math.radians(212), math.radians(180)
    for a, key, c, seed in [(lead, 'warm', '#ffcf5a', 21), (chase, 'cool', '#c9d8ee', 23)]:
        trail = [orbit(a - math.radians(d)) for d in (30, 22, 14, 7)]
        o.append(motion_lines(trail, c, n=3, gap=12, width=5))
        p = orbit(a)
        tangent = (-rx * math.sin(a), ry * math.cos(a))   # direction of increasing a (clockwise on screen)
        ang = math.degrees(math.atan2(tangent[1], tangent[0]))
        o.append(dragon(p[0], p[1], 0.68, None, pose_fly(head_angle=-4), flip=1, rot=ang, shimmer=key, seed=seed, expr='happy'))
    return ''.join(o)



# ============================================================ scenery helpers
def bstyle(px=3.0):
    return dict(party.STYLES['bold'], stroke=px)


def mountain(x, base, h, w, fill, snow=None, lean=0, seed=0):
    rnd = random.Random(seed)
    pts = [(x - w / 2, base)]
    n = 7
    for k in range(1, n):
        t = k / n
        peak = 1 - abs(t - 0.5 - lean * 0.1) * 2
        pts.append((x - w / 2 + w * t, base - h * max(peak, 0) - rnd.uniform(-h * 0.06, h * 0.06) * (0.3 < t < 0.7)))
    pts.append((x + w / 2, base))
    d = 'M ' + ' L '.join(f'{a:.1f},{b:.1f}' for a, b in pts) + ' Z'
    o = P(d, fill, bstyle(), bg=False)
    if snow:
        top = min(pts, key=lambda q: q[1])
        sd = (f'M {top[0] - w * 0.16:.1f},{top[1] + h * 0.26:.1f} L {top[0]:.1f},{top[1]:.1f} L {top[0] + w * 0.17:.1f},{top[1] + h * 0.28:.1f} '
              f'L {top[0] + w * 0.08:.1f},{top[1] + h * 0.2:.1f} L {top[0] + 2:.1f},{top[1] + h * 0.3:.1f} L {top[0] - w * 0.07:.1f},{top[1] + h * 0.2:.1f} Z')
        o += P(sd, snow, bstyle(2.2))
    return o


def volcano(x, base, h, w, fill='#7d5a50'):
    tw = w * 0.16
    d = f'M {x - w / 2},{base} L {x - tw},{base - h} L {x + tw},{base - h} L {x + w / 2},{base} Z'
    o = P(d, fill, bstyle())
    o += P(f'M {x - tw},{base - h} Q {x},{base - h + 10} {x + tw},{base - h} Q {x},{base - h - 8} {x - tw},{base - h} Z', '#ff7a1c', bstyle(2))
    for k, dx in enumerate((-0.6, 0.1, 0.5)):
        o += P(f'M {x + dx * tw},{base - h + 4} Q {x + dx * tw * 2.2 + 6},{base - h * 0.55} {x + dx * w * 0.32},{base - h * 0.12} '
               f'L {x + dx * w * 0.32 + 8},{base - h * 0.12} Q {x + dx * tw * 2.2 + 16},{base - h * 0.55} {x + dx * tw + 8},{base - h + 4} Z',
               ['#ff8a1c', '#ffb02e', '#ff6a1c'][k], bstyle(1.6))
    o += glow(x, base - h, h * 0.55, '#ff8a1c')
    for k in range(4):
        o += f'<circle cx="{x - 10 + k * 14}" cy="{base - h - 26 - k * 22}" r="{14 + k * 6}" fill="#8a8590" opacity="{0.55 - k * 0.1:.2f}"/>'
    return o


def tree(x, base, s, fill='#3f8a3c', trunk='#6b4a2f', blossom=None, seed=0):
    rnd = random.Random(seed)
    o = P(f'M {x - 5 * s},{base} L {x - 4 * s},{base - 30 * s} L {x + 4 * s},{base - 30 * s} L {x + 5 * s},{base} Z', trunk, bstyle(2))
    d = (f'M {x - 34 * s},{base - 28 * s} Q {x - 44 * s},{base - 60 * s} {x - 18 * s},{base - 66 * s} Q {x - 10 * s},{base - 92 * s} {x + 12 * s},{base - 80 * s} '
         f'Q {x + 40 * s},{base - 82 * s} {x + 36 * s},{base - 54 * s} Q {x + 48 * s},{base - 30 * s} {x + 20 * s},{base - 24 * s} Q {x},{base - 18 * s} {x - 34 * s},{base - 28 * s} Z')
    o += P(d, fill, bstyle(2.2))
    o += f'<path d="M {x - 20 * s},{base - 40 * s} Q {x},{base - 34 * s} {x + 22 * s},{base - 42 * s}" stroke="{dark(fill, .25)}" stroke-width="{3 * s:.1f}" fill="none"/>'
    if blossom:
        for _ in range(6):
            bx, by = x + rnd.uniform(-28, 30) * s, base - rnd.uniform(34, 76) * s
            o += f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="{3.6 * s:.1f}" fill="{blossom}" stroke="{INK}" stroke-width="1.2"/>'
    return o


def ziggurat(cx, base, w, tier_h, tiers, fill='#d9cdb2', trim='#8a6a3c', stair='#efe4c9'):
    o = ''
    for k in range(tiers):
        ww = w * (1 - k * 0.22)
        y0 = base - k * tier_h
        o += P(f'M {cx - ww / 2},{y0} L {cx - ww / 2 + 10},{y0 - tier_h} L {cx + ww / 2 - 10},{y0 - tier_h} L {cx + ww / 2},{y0} Z',
               mix(fill, '#ffffff', 0.08 * k), bstyle(2.6))
        o += f'<path d="M {cx - ww / 2 + 6},{y0 - tier_h + 8} L {cx + ww / 2 - 6},{y0 - tier_h + 8}" stroke="{trim}" stroke-width="4"/>'
        for j in range(int(ww // 40)):
            xx = cx - ww / 2 + 22 + j * 40
            if abs(xx - cx) < w * 0.12:
                continue
            o += f'<rect x="{xx - 5}" y="{y0 - tier_h * 0.62}" width="10" height="{tier_h * 0.4}" fill="{dark(fill, .28)}" rx="3"/>'
    sw = w * 0.2
    top = base - tiers * tier_h
    o += P(f'M {cx - sw / 2},{base} L {cx - sw * 0.28},{top} L {cx + sw * 0.28},{top} L {cx + sw / 2},{base} Z', stair, bstyle(2.4))
    for k in range(1, 14):
        y = base - (base - top) * k / 14
        f = 1 - k / 14 * 0.44
        o += f'<path d="M {cx - sw / 2 * f:.1f},{y:.1f} L {cx + sw / 2 * f:.1f},{y:.1f}" stroke="#b9ab8c" stroke-width="2"/>'
    return o, top


def crowd(spots, seed, colours, scale, poses, outfits=None, look=-18):
    """Draw a crowd. spots: list of (x, y); scale: base scale (smaller = farther)."""
    rnd = random.Random(seed)
    outfits = outfits or ['#efe4cc', '#6f7b8a', '#8d98a6', '#5c6b3a', '#7a3a2a', '#4b3a7a', '#2f6b6b', '#e9dfc6']
    accents = ['#9b2d2d', '#2b5fa8', '#c08a1e', '#3d2f4f', '#e8c35a', '#2f4f8f']
    o = ''
    for (x, y) in sorted(spots, key=lambda q: q[1]):
        drag = rnd.choice(colours)
        pose = rnd.choice(poses)
        kneel = pose in ('pray', 'raise') and rnd.random() < 0.5
        o += person(x, y, scale * rnd.uniform(0.92, 1.06), drag, pose, rnd.choice(outfits), rnd.choice(accents),
                    flip=rnd.choice((1, -1)) if pose == 'stand' else (1 if x < 600 else -1) if False else rnd.choice((1, 1, -1)),
                    look=look, robe=rnd.random() < 0.5, kneel=kneel,
                    item=rnd.choice((None, None, 'scroll', 'book')) if pose in ('read', 'hold') else None)
    return o


def glyph(kind, x, y, r, sty=None):
    """Small elemental glyphs: fire, water, earth, ice, eye (knowledge)."""
    sty = sty or bstyle(2.2)
    o = circ(x, y, r, '#2a2140', sty) + f'<circle cx="{x}" cy="{y}" r="{r - 4}" fill="none" stroke="#c58bff" stroke-width="2"/>'
    k = r * 0.55
    if kind == 'fire':
        o += P(f'M {x},{y - k} Q {x + k},{y} {x},{y + k} Q {x - k},{y} {x},{y - k} Z', '#ff8a1c', bstyle(1.4))
    elif kind == 'water':
        o += P(f'M {x},{y - k} Q {x + k},{y + k * 0.4} {x},{y + k} Q {x - k},{y + k * 0.4} {x},{y - k} Z', '#6ec6ff', bstyle(1.4))
    elif kind == 'earth':
        o += P(f'M {x - k},{y + k * 0.7} L {x - k * 0.2},{y - k} L {x + k * 0.3},{y - k * 0.1} L {x + k},{y + k * 0.7} Z', '#9a7a4c', bstyle(1.4))
    elif kind == 'ice':
        for a in (0, 60, 120):
            ra = math.radians(a)
            o += f'<path d="M {x - k * math.cos(ra):.1f},{y - k * math.sin(ra):.1f} L {x + k * math.cos(ra):.1f},{y + k * math.sin(ra):.1f}" stroke="#e6f6ff" stroke-width="3" stroke-linecap="round"/>'
    elif kind == 'eye':
        o += f'<ellipse cx="{x}" cy="{y}" rx="{k}" ry="{k * 0.55}" fill="#ffe27a" stroke="{INK}" stroke-width="1.5"/><ellipse cx="{x}" cy="{y}" rx="{k * 0.2}" ry="{k * 0.5}" fill="{INK}"/>'
    return o


def haze(x, y, w, h, colour, op):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{colour}" opacity="{op}"/>'


def flower_tuft(x, y, seed, petals=('#ffb3d1', '#fff2a8', '#ffffff'), s=1.0, n=3):
    """A clump of grass with a few flowers on stems (clearly flowers, not loose dots)."""
    rnd = random.Random(seed)
    o = ''
    for k in range(5):
        a = math.radians(-90 + rnd.uniform(-38, 38))
        L_ = rnd.uniform(10, 18) * s
        bx = x + rnd.uniform(-8, 8) * s
        o += P(f'M {bx - 2.4 * s:.1f},{y} Q {bx + math.cos(a) * L_ * 0.4:.1f},{y + math.sin(a) * L_ * 0.6:.1f} {bx + math.cos(a) * L_:.1f},{y + math.sin(a) * L_:.1f} '
               f'Q {bx + math.cos(a) * L_ * 0.5 + 2:.1f},{y + math.sin(a) * L_ * 0.5:.1f} {bx + 2.4 * s:.1f},{y} Z', rnd.choice(['#4f9a40', '#3f8a3c', '#5aa64a']), bstyle(1.2))
    for k in range(n):
        fx = x + (k - (n - 1) / 2) * 9 * s + rnd.uniform(-2, 2)
        fy = y - rnd.uniform(16, 26) * s
        o += f'<path d="M {fx:.1f},{fy:.1f} Q {fx + 3:.1f},{(fy + y) / 2:.1f} {x + (k - 1) * 3 * s:.1f},{y}" stroke="{INK}" stroke-width="{3.4 * s:.1f}" fill="none"/>'
        o += f'<path d="M {fx:.1f},{fy:.1f} Q {fx + 3:.1f},{(fy + y) / 2:.1f} {x + (k - 1) * 3 * s:.1f},{y}" stroke="#4f9a40" stroke-width="{1.6 * s:.1f}" fill="none"/>'
        c = petals[(k + seed) % len(petals)]
        r = 3.6 * s
        for j in range(5):
            a = math.radians(j * 72 - 90 + seed * 7)
            px, py = fx + r * math.cos(a), fy + r * math.sin(a)
            o += f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{r * 0.95:.1f}" ry="{r * 0.62:.1f}" transform="rotate({j * 72 + seed * 7 - 90} {px:.1f} {py:.1f})" fill="{c}" stroke="{INK}" stroke-width="1"/>'
        o += f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="{r * 0.55:.1f}" fill="#ffc93c" stroke="{INK}" stroke-width="1"/>'
    return o


def swimmer(x, wl, s, drag, outfit, accent, flip=1, pose='wave', look=-10):
    """A dragonborn swimming: only the part above the water line wl shows, with ripples."""
    cid = uid('swim')
    o = f'<clipPath id="{cid}"><rect x="{x - 80}" y="{wl - 140}" width="160" height="{140 + 2}"/></clipPath>'
    o += f'<g clip-path="url(#{cid})">' + person(x, wl + 44 * s, s, drag, pose, outfit, accent, flip=flip, look=look) + '</g>'
    for k, (rx, op) in enumerate(((26, .9), (40, .6), (54, .35))):
        o += f'<ellipse cx="{x}" cy="{wl + 2 + k * 2}" rx="{rx * s / 0.6:.0f}" ry="{4 + k * 1.5:.1f}" fill="none" stroke="#e6f4ff" stroke-width="2.4" opacity="{op}"/>'
    return o


def dragonfly(x, y, s=1.0, rot=0):
    o = f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">'
    for (a, l) in ((-20, 16), (20, 16), (-160, 14), (160, 14)):
        o += f'<ellipse cx="{l * 0.55 * math.cos(math.radians(a)):.1f}" cy="{l * 0.55 * math.sin(math.radians(a)) - 2:.1f}" rx="{l * 0.6:.1f}" ry="3.4" transform="rotate({a} {l * 0.55 * math.cos(math.radians(a)):.1f} {l * 0.55 * math.sin(math.radians(a)) - 2:.1f})" fill="#e8f8ff" fill-opacity=".75" stroke="{INK}" stroke-width="1"/>'
    o += limb([(-4, -2), (22, -2)], 3.2, '#2e9fb8', bstyle(1)) + circ(-6, -2, 3.4, '#2e6fd2', bstyle(1))
    return o + '</g>'


def lantern_string(x0, y0, x1, y1, sag, n, seed, colours=('#ffd27a', '#ffb3d1', '#bfe8ff')):
    """A sagging cord of little glowing paper lanterns."""
    o = f'<path d="M {x0},{y0} Q {(x0 + x1) / 2},{(y0 + y1) / 2 + sag * 2} {x1},{y1}" stroke="{INK}" stroke-width="1.6" fill="none"/>'
    for k in range(1, n + 1):
        t = k / (n + 1)
        x = (1 - t) ** 2 * x0 + 2 * t * (1 - t) * (x0 + x1) / 2 + t * t * x1
        y = (1 - t) ** 2 * y0 + 2 * t * (1 - t) * ((y0 + y1) / 2 + sag * 2) + t * t * y1
        c = colours[(k + seed) % len(colours)]
        o += glow(x, y + 9, 16, c)
        o += f'<ellipse cx="{x:.1f}" cy="{y + 9:.1f}" rx="6" ry="8" fill="{c}" stroke="{INK}" stroke-width="1.4"/>'
        o += f'<path d="M {x - 4:.1f},{y + 3:.1f} L {x + 4:.1f},{y + 3:.1f} M {x - 4:.1f},{y + 15:.1f} L {x + 4:.1f},{y + 15:.1f}" stroke="{INK}" stroke-width="1.6"/>'
    return o


def bunting(x0, y0, x1, y1, sag, n, colours):
    o = f'<path d="M {x0},{y0} Q {(x0 + x1) / 2},{(y0 + y1) / 2 + sag * 2} {x1},{y1}" stroke="{INK}" stroke-width="1.8" fill="none"/>'
    for k in range(n):
        t0, t1 = (k + 0.15) / n, (k + 0.85) / n

        def at(t):
            return ((1 - t) ** 2 * x0 + 2 * t * (1 - t) * (x0 + x1) / 2 + t * t * x1,
                    (1 - t) ** 2 * y0 + 2 * t * (1 - t) * ((y0 + y1) / 2 + sag * 2) + t * t * y1)
        a, b = at(t0), at(t1)
        m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + 20)
        o += P(f'M {a[0]:.1f},{a[1]:.1f} L {b[0]:.1f},{b[1]:.1f} L {m[0]:.1f},{m[1]:.1f} Z', colours[k % len(colours)], bstyle(1.6))
    return o


def chalkboard(x, base):
    """A slate on an easel, chalked with geometry (no words)."""
    o = limb([(x - 26, base), (x - 8, base - 96)], 4, party.WOOD, bstyle(2))
    o += limb([(x + 26, base), (x + 8, base - 96)], 4, party.WOOD, bstyle(2))
    o += limb([(x, base - 40), (x + 4, base - 96)], 3, party.WOOD, bstyle(2))
    o += P(f'M {x - 40},{base - 104} L {x + 40},{base - 104} L {x + 40},{base - 46} L {x - 40},{base - 46} Z', '#2f4a3c', bstyle(2.6))
    o += f'<rect x="{x - 40}" y="{base - 104}" width="80" height="58" fill="none" stroke="#8a5a2b" stroke-width="3"/>'
    o += (f'<circle cx="{x - 14}" cy="{base - 76}" r="16" fill="none" stroke="#f1f1e6" stroke-width="2"/>'
          f'<path d="M {x - 28},{base - 68} L {x - 6},{base - 91} L {x + 1},{base - 70} Z" fill="none" stroke="#f1f1e6" stroke-width="2"/>'
          f'<path d="M {x + 10},{base - 94} L {x + 34},{base - 94} M {x + 10},{base - 84} L {x + 28},{base - 84} M {x + 10},{base - 74} L {x + 32},{base - 74} '
          f'M {x + 12},{base - 62} Q {x + 22},{base - 70} {x + 32},{base - 58}" stroke="#f1f1e6" stroke-width="2" fill="none" stroke-dasharray="4 3"/>')
    return o


def kite(x, y, hand, s=1.0):
    """A diamond kite with a bow tail, flown from hand."""
    o = f'<path d="M {hand[0]},{hand[1]} Q {(hand[0] + x) / 2 + 40},{(hand[1] + y) / 2 + 30} {x},{y + 26 * s}" stroke="{INK}" stroke-width="1.4" fill="none"/>'
    o += P(f'M {x},{y - 26 * s} L {x + 18 * s},{y} L {x},{y + 26 * s} L {x - 18 * s},{y} Z', '#ff7a5a', bstyle(2.2))
    o += P(f'M {x},{y - 26 * s} L {x + 18 * s},{y} L {x},{y} Z', '#ffd34d', bstyle(1.6))
    o += P(f'M {x},{y} L {x - 18 * s},{y} L {x},{y + 26 * s} Z', '#ffd34d', bstyle(1.6))
    o += f'<path d="M {x},{y + 26 * s} q 10,14 0,28 q -10,14 0,28" stroke="{INK}" stroke-width="1.4" fill="none"/>'
    for k, c in enumerate(('#2e6fd2', '#3c9a47', '#c8342b')):
        by = y + 26 * s + 14 + k * 14
        bx = x + (6 if k % 2 == 0 else -6)
        o += P(f'M {bx},{by} L {bx - 7},{by - 4} L {bx - 7},{by + 4} Z M {bx},{by} L {bx + 7},{by - 4} L {bx + 7},{by + 4} Z', c, bstyle(1.2))
    return o


def easel(x, base, painting):
    o = limb([(x - 24, base), (x - 6, base - 104)], 4, party.WOOD, bstyle(2))
    o += limb([(x + 24, base), (x + 6, base - 104)], 4, party.WOOD, bstyle(2))
    o += limb([(x + 2, base), (x, base - 60)], 3, party.WOOD, bstyle(2))
    o += P(f'M {x - 36},{base - 104} L {x + 36},{base - 104} L {x + 36},{base - 50} L {x - 36},{base - 50} Z', '#fbf4e3', bstyle(2.6))
    o += f'<g transform="translate({x},{base - 77})">{painting}</g>'
    o += limb([(x - 40, base - 48), (x + 40, base - 48)], 4, party.WOOD, bstyle(2))
    return o


def splash(x, y, s=1.0, c='#d8eeff'):
    """A cartoon splash: a crown of water and a few teardrop droplets."""
    o = P(f'M {x - 34 * s},{y} Q {x - 30 * s},{y - 18 * s} {x - 22 * s},{y - 26 * s} L {x - 16 * s},{y - 10 * s} L {x - 8 * s},{y - 32 * s} '
          f'L {x},{y - 12 * s} L {x + 9 * s},{y - 30 * s} L {x + 15 * s},{y - 10 * s} L {x + 24 * s},{y - 24 * s} Q {x + 30 * s},{y - 14 * s} {x + 34 * s},{y} Z',
          c, bstyle(2))
    for (dx, dy, r) in [(-30, -40, 4), (-14, -48, 3.4), (6, -52, 4.2), (24, -42, 3.4)]:
        cx_, cy_ = x + dx * s, y + dy * s
        o += P(f'M {cx_:.1f},{cy_ - r * 1.9:.1f} Q {cx_ + r:.1f},{cy_ - r * 0.2:.1f} {cx_:.1f},{cy_ + r:.1f} Q {cx_ - r:.1f},{cy_ - r * 0.2:.1f} {cx_:.1f},{cy_ - r * 1.9:.1f} Z', c, bstyle(1.4))
    return o


# ============================================================ Epoch 1
def pose_teach():
    p = pose_sit(head_angle=-14, wings='folded', wing_rot=-14, wing_scale=1.4)
    p['legs'] = [(0.52, [(-4, 22), (6, 20)], False), (0.66, [(4, 40), (8, 68)], False),
                 (0.5, [(14, 18), (2, 22), (14, 22)], True), (0.7, [(30, 6), (52, -22)], True)]
    return p


def scene1():
    rnd = random.Random(41)
    o = []
    o.append(gradient_rect(0, 0, 1200, 480, ['#16224f', '#2f5aa8', '#6fa8e0', '#b9dcf3', '#f8ead0']))
    o.append(stars(40, 9, ymax=110))
    # the Gold dragon as the sun, the Silver faint by day
    o.append(sky_dragon(250, 118, 0.62, '#ffc93c', '#ffd25a', party.STYLES['bold']))
    o.append('<g opacity=".7">' + sky_dragon(1010, 92, 0.36, '#e6edf8', '#bcd2ff', party.STYLES['bold'], flip=-1) + '</g>')
    # Azhi, faint, peeking over the horizon in wonder
    head, lm = azhi_head(expr='wonder')
    neck = [(1330, 560), (1310, 480), (1290, 418)]
    nb, *_ = azhi_body(neck, 190, 210, sty_px=3)
    o.append('<g opacity=".55">' + nb + f'<g transform="translate(1286,414) rotate(-14) scale(-1.22,1.22)">{head}</g></g>')
    o.append('<defs><linearGradient id="az1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe4f6" stop-opacity="0"/>'
             '<stop offset="1" stop-color="#e8f2fa" stop-opacity=".55"/></linearGradient></defs>'
             '<rect x="860" y="200" width="340" height="300" fill="url(#az1)"/>')
    # glacier range (left) with White perched on the tallest peak
    def hz(x):
        return 2440 - math.sqrt(2000 ** 2 - (x - 600) ** 2)
    for (x, h, w, c) in [(70, 150, 230, '#a9bfd9'), (360, 130, 220, '#9fb5d0'), (220, 215, 270, '#b5c9e0')]:
        o.append(mountain(x, hz(x) + 22, h, w, c, snow='#ffffff', seed=int(x)))
    # a White dragonborn on wings of light, swooping down from the glacier toward the teaching
    o.append(person(420, 330, 0.64, 'White', 'fly', '#eceff4', '#9fb7d4', look=6, wings='spectral'))
    o.append(dragon(214, hz(220) + 22 - 215 + 30, 0.42, 'White', pose_sit(head_angle=-6, wings='up', wing_rot=-20, wing_scale=1.1), flip=1, expr='happy'))
    for (x, y) in [(150, 330), (300, 300), (270, 380), (120, 400), (330, 360)]:
        o.append(f'<path d="M {x},{y - 8} L {x + 2.5},{y} L {x},{y + 8} L {x - 2.5},{y} Z M {x - 8},{y} L {x},{y + 2.5} L {x + 8},{y} L {x},{y - 2.5} Z" fill="#ffffff" stroke="#7fa6c8" stroke-width=".8"/>')
    # the young world's land: a great curved horizon
    o.append('<clipPath id="land1"><circle cx="600" cy="2440" r="2000"/></clipPath>')
    o.append('<g clip-path="url(#land1)">' + gradient_rect(0, 430, 1200, 370, ['#c4dd96', '#8cbf5f', '#5f9a42']) + '</g>')
    o.append(f'<circle cx="600" cy="2440" r="2000" fill="none" stroke="{INK}" stroke-width="3"/>')
    o.append('<defs><linearGradient id="atm1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff" stop-opacity="0"/>'
             '<stop offset="1" stop-color="#ffffff" stop-opacity=".5"/></linearGradient></defs>'
             '<path d="M 0,560 L 0,532 A 2000,2000 0 0 1 1200,532 L 1200,560 Z" fill="none"/>')
    # volcanic range (right) with Red raising a mountain
    o.append(mountain(1150, hz(1150) + 24, 105, 230, '#8a6a5c', seed=3))
    o.append(mountain(850, hz(850) + 22, 110, 200, '#94776a', seed=4))
    o.append(volcano(990, hz(990) + 24, 190, 270))
    o.append(dragon(870, 300, 0.5, 'Red', pose_fly(head_angle=6), flip=1, rot=-8, expr='happy'))
    # atmospheric haze on the far land
    o.append('<defs><linearGradient id="mist1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2f8fc" stop-opacity="0"/>'
             '<stop offset=".7" stop-color="#f2f8fc" stop-opacity=".45"/><stop offset="1" stop-color="#f2f8fc" stop-opacity="0"/></linearGradient></defs>'
             '<rect x="0" y="400" width="1200" height="140" fill="url(#mist1)"/>')
    # the sea (left), with Blue leaping
    sea = 'M -20,500 Q 180,488 420,512 Q 470,560 400,606 Q 220,640 -20,628 Z'
    o.append(P(sea, '#3f86c8', bstyle()))
    for k in range(12):
        x, y = rnd.uniform(20, 380), rnd.uniform(520, 610)
        o.append(f'<path d="M {x},{y} q 8,-6 16,0 q 8,-6 16,0" stroke="#d8eeff" stroke-width="2.4" fill="none" stroke-linecap="round"/>')
    o.append(dragon(210, 556, 0.46, 'Blue', pose_fly(head_angle=-10, wings='up'), flip=1, rot=-28, expr='happy'))
    o.append(splash(168, 552, 0.62))
    o.append(swimmer(330, 540, 0.42, 'Blue', '#efe4cc', '#2b5fa8', flip=-1, pose='wave', look=-24))
    # rolling hills and Green's forest (right), blossoming
    o.append(P(wave(560, 14, 4, 1.1), '#7db558', bstyle(), bg=False))
    for k, x in enumerate(range(760, 1240, 46)):
        o.append(tree(x + rnd.uniform(-8, 8), 545 + (k % 2) * 12, 0.62, fill=rnd.choice(['#3f8a3c', '#4f9a40', '#2f7a3a']), blossom='#ffb3d1', seed=k))
    for k, x in enumerate(range(800, 1220, 54)):
        if 960 < x < 1110:
            continue
        o.append(tree(x + rnd.uniform(-10, 10), 640 + (k % 2) * 10, 0.75, fill=rnd.choice(['#3f8a3c', '#4f9a40']), blossom='#fff2a8', seed=50 + k))
    o.append(dragon(1040, 628, 0.56, 'Green', pose_lounge(4), flip=-1, expr='closed'))
    for k, (x, y) in enumerate([(975, 652), (1112, 650)]):
        o.append(flower_tuft(x, y, 30 + k, s=0.75, n=2))
    for (x, y) in [(940, 520), (1080, 530), (900, 590)]:
        o.append(f'<path d="M {x},{y} q -8,-8 -12,0 q 4,8 12,0 q 8,-8 12,0 q -4,8 -12,0 Z" fill="#ffd34d" stroke="{INK}" stroke-width="1.4"/>')
    # the temple hill, the temple, and the Black, teaching
    o.append(P('M 250,800 Q 300,640 470,612 Q 600,592 730,612 Q 900,640 960,800 Z', '#a7c972', bstyle()))
    zg, top = ziggurat(600, 640, 330, 46, 3)
    o.append(zg)
    o.append(glow(596, top - 70, 190, '#a77bff'))
    o.append(dragon(586, top - 12, 0.86, 'Black', pose_teach(), flip=1, expr='talk'))
    for k, kind in enumerate(['fire', 'water', 'earth', 'ice', 'eye']):
        a = math.radians(-160 + k * 34)
        o.append(glyph(kind, 640 + 150 * math.cos(a) + 60, top - 120 + 70 * math.sin(a), 15))
    # worshippers and students on the steps and the plaza
    cols7 = ['Red', 'Blue', 'Green', 'White', 'Black', 'Gold', 'Silver']
    stairs = [(600 + rnd.uniform(-22, 22), y) for y in (600, 620)]
    o.append(crowd(stairs, 5, cols7, 0.3, ['raise', 'pray']))
    spots = []
    for r, y in enumerate((664, 696, 730)):
        for x in range(320 + (r % 2) * 24, 900, 50):
            if 548 < x < 652:
                continue
            spots.append((x + rnd.uniform(-8, 8), y + rnd.uniform(-4, 4)))
    o.append(crowd(spots, 6, cols7, 0.4, ['raise', 'pray', 'read', 'awe', 'raise', 'pray', 'stand']))
    # the path and the pilgrims in front
    o.append(P('M 520,800 Q 560,750 575,740 L 625,740 Q 640,750 680,800 Z', '#e9d9b0', bstyle(2.4)))
    o.append(person(150, 790, 0.78, 'Green', 'hold', '#5c6b3a', '#7a4e2a', item='scroll', look=-20, tail_item='basket'))
    o.append(person(236, 792, 0.5, 'Green', 'point', '#f2d16b', '#7a4e2a', child=True, look=-30, tail_item='fruit'))
    # a scribe, taking the teaching down on a clay tablet
    o.append(person(1060, 790, 0.8, 'White', 'read', '#6f7b8a', '#9b2d2d', flip=-1, item='tablet', look=-6, robe=True))
    o.append(person(1140, 794, 0.76, 'Red', 'awe', '#8d98a6', '#2f4f8f', flip=-1, look=-24))
    for k, (x, y) in enumerate([(40, 778), (320, 796), (930, 794), (1186, 780)]):
        o.append(flower_tuft(x, y, 10 + k))
    return ''.join(o)


# ============================================================ Epoch 2
BRASS2, BRASS_D, STONE2 = '#d4a63c', '#9a7428', '#d8cfbf'


def lens(cx, cy, r, glowc='#5ff0e0'):
    """The thinking machine's great eye (also the revivalists' icon)."""
    sty = bstyle(3)
    o = glow(cx, cy, r * 1.9, glowc)
    o += circ(cx, cy, r * 1.18, BRASS2, sty)
    for k in range(16):
        a = math.radians(k * 22.5)
        o += f'<circle cx="{cx + r * 1.09 * math.cos(a):.1f}" cy="{cy + r * 1.09 * math.sin(a):.1f}" r="{r * 0.045:.1f}" fill="{BRASS_D}"/>'
    o += circ(cx, cy, r, '#1f3540', sty)
    o += circ(cx, cy, r * 0.72, '#2f6f74', bstyle(2))
    o += circ(cx, cy, r * 0.5, '#7ff7ea', bstyle(2))
    for k in range(6):   # iris aperture blades
        a = math.radians(k * 60 + 15)
        o += f'<path d="M {cx + r * 0.5 * math.cos(a):.1f},{cy + r * 0.5 * math.sin(a):.1f} L {cx + r * 0.22 * math.cos(a + 1.2):.1f},{cy + r * 0.22 * math.sin(a + 1.2):.1f}" stroke="#2f6f74" stroke-width="{r * 0.04:.1f}"/>'
    o += circ(cx, cy, r * 0.2, '#e8fffb', bstyle(2))
    o += f'<circle cx="{cx - r * 0.28}" cy="{cy - r * 0.3}" r="{r * 0.12}" fill="#ffffff" opacity=".85"/>'
    return o


def thinking_machine(cx, base):
    """An enormous thinking machine of brass and stone (our own design). Returns (svg, landmarks)."""
    sty = bstyle(3.4)
    o = []
    lm = {}
    # side towers with steam
    for side in (-1, 1):
        x = cx + side * 230
        o.append(P(f'M {x - 34},{base} L {x - 30},{base - 330} L {x + 30},{base - 330} L {x + 34},{base} Z', STONE2, sty))
        o.append(P(f'M {x - 40},{base - 330} L {x + 40},{base - 330} L {x + 30},{base - 356} L {x - 30},{base - 356} Z', BRASS2, sty))
        for k in range(5):
            o.append(f'<rect x="{x - 16}" y="{base - 300 + k * 52}" width="32" height="30" rx="5" fill="#2a3a44" stroke="{INK}" stroke-width="2"/>')
            for j in range(3):
                c = random.Random(int(x) + k * 7 + j).choice(['#7ff7ea', '#ffd34d', '#ff7a7a', '#2f6f74'])
                o.append(f'<circle cx="{x - 9 + j * 9}" cy="{base - 285 + k * 52}" r="3.2" fill="{c}"/>')
        o.append(limb([(x - 4, base - 356), (x - 4, base - 392)], 10, BRASS_D, sty))
        for k in range(3):
            o.append(f'<circle cx="{x - 4 + side * (10 + k * 26)}" cy="{base - 404 - k * 18}" r="{12 + k * 6}" fill="#f4f4f0" stroke="#b8b8b0" stroke-width="2" opacity="{0.9 - k * 0.2:.2f}"/>')
        # pipes to the core
        o.append(limb([(x - side * 30, base - 250), (cx + side * 140, base - 250)], 14, BRASS_D, sty))
        o.append(limb([(x - side * 30, base - 140), (cx + side * 150, base - 140)], 14, BRASS2, sty))
    # plinth with stairs
    o.append(P(f'M {cx - 200},{base} L {cx - 186},{base - 70} L {cx + 186},{base - 70} L {cx + 200},{base} Z', STONE2, sty))
    o.append(P(f'M {cx - 60},{base} L {cx - 44},{base - 70} L {cx + 44},{base - 70} L {cx + 60},{base} Z', '#efe4c9', bstyle(2.6)))
    for k in range(1, 7):
        y = base - 70 * k / 7
        f = 1 - k / 7 * 0.27
        o.append(f'<path d="M {cx - 60 * f:.1f},{y:.1f} L {cx + 60 * f:.1f},{y:.1f}" stroke="#b9ab8c" stroke-width="2"/>')
    # the question slot and the answer tape (front of the plinth)
    o.append(f'<rect x="{cx - 160}" y="{base - 58}" width="70" height="16" rx="6" fill="#1b1b1b" stroke="{BRASS_D}" stroke-width="4"/>')
    lm['slot'] = (cx - 125, base - 50)
    o.append(f'<rect x="{cx + 90}" y="{base - 58}" width="70" height="16" rx="6" fill="#1b1b1b" stroke="{BRASS_D}" stroke-width="4"/>')
    lm['tape'] = (cx + 125, base - 44)
    # main body: a great drum
    o.append(P(f'M {cx - 170},{base - 70} L {cx - 160},{base - 380} Q {cx},{base - 420} {cx + 160},{base - 380} L {cx + 170},{base - 70} Z', BRASS2, sty))
    o.append(P(f'M {cx - 150},{base - 90} L {cx - 142},{base - 360} Q {cx},{base - 396} {cx + 142},{base - 360} L {cx + 150},{base - 90} Z', '#e9c66a', bstyle(2.4)))
    # panels of lights
    rnd = random.Random(2)
    for side in (-1, 1):
        x0 = cx + side * 110 - 26
        for r in range(6):
            for c in range(3):
                col_ = rnd.choice(['#7ff7ea', '#ffd34d', '#ff7a7a', '#2f6f74', '#7ff7ea'])
                o.append(f'<circle cx="{x0 + c * 18}" cy="{base - 120 - r * 34}" r="5" fill="{col_}" stroke="{INK}" stroke-width="1.6"/>')
    # dials
    for (dx, dy) in [(-60, -110), (60, -110)]:
        o.append(circ(cx + dx, base + dy, 22, '#f6f1e3', bstyle(2.6)))
        o.append(f'<path d="M {cx + dx},{base + dy} L {cx + dx + 12},{base + dy - 12}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    # the great eye
    lm['eye'] = (cx, base - 250)
    o.append(lens(cx, base - 250, 82))
    # orrery ring around the eye
    o.append(f'<ellipse cx="{cx}" cy="{base - 250}" rx="150" ry="36" fill="none" stroke="{INK}" stroke-width="12" transform="rotate(-12 {cx} {base - 250})"/>'
             f'<ellipse cx="{cx}" cy="{base - 250}" rx="150" ry="36" fill="none" stroke="{BRASS2}" stroke-width="7" transform="rotate(-12 {cx} {base - 250})"/>')
    for (a, c) in [(20, '#7ff7ea'), (150, '#ff7a7a'), (250, '#ffd34d')]:
        ra = math.radians(a)
        px, py = 150 * math.cos(ra), 36 * math.sin(ra)
        t = math.radians(-12)
        o.append(circ(cx + px * math.cos(t) - py * math.sin(t), base - 250 + px * math.sin(t) + py * math.cos(t), 10, c, bstyle(2.4)))
    # shoulders: broad platforms for the dragons
    for side in (-1, 1):
        o.append(P(f'M {cx + side * 120},{base - 392} L {cx + side * 250},{base - 380} L {cx + side * 250},{base - 360} L {cx + side * 110},{base - 368} Z', BRASS_D, sty))
        lm['perch_l' if side < 0 else 'perch_r'] = (cx + side * 190, base - 386)
    # dome and antenna
    o.append(P(f'M {cx - 120},{base - 392} Q {cx},{base - 520} {cx + 120},{base - 392} Z', '#c7cfd6', sty))
    for k in (-60, 0, 60):
        o.append(f'<path d="M {cx + k * 0.4},{base - 488 + abs(k) * 0.3} Q {cx + k},{base - 440} {cx + k * 1.6},{base - 396}" stroke="#8d98a6" stroke-width="3" fill="none"/>')
    o.append(limb([(cx, base - 480), (cx, base - 560)], 6, BRASS_D, sty))
    o.append(circ(cx, base - 566, 10, '#7ff7ea', sty))
    o.append(glow(cx, base - 566, 40, '#7ff7ea'))
    return ''.join(o), lm


def city_block(x, base, w, h, fill, roof='dome', sty=None):
    sty = sty or bstyle(2.6)
    o = P(f'M {x - w / 2},{base} L {x - w / 2},{base - h} L {x + w / 2},{base - h} L {x + w / 2},{base} Z', fill, sty)
    for k in range(int(w // 22)):
        xx = x - w / 2 + 11 + k * 22
        o += f'<rect x="{xx - 4}" y="{base - h + 14}" width="8" height="{h - 24}" fill="{dark(fill, .15)}"/>'
    if roof == 'dome':
        o += P(f'M {x - w * 0.42},{base - h} Q {x},{base - h - w * 0.6} {x + w * 0.42},{base - h} Z', '#9fb7c8', sty)
    elif roof == 'gable':
        o += P(f'M {x - w / 2 - 6},{base - h} L {x},{base - h - w * 0.32} L {x + w / 2 + 6},{base - h} Z', '#c46b4a', sty)
    elif roof == 'flat':
        o += P(f'M {x - w / 2 - 6},{base - h} L {x + w / 2 + 6},{base - h} L {x + w / 2 + 6},{base - h - 10} L {x - w / 2 - 6},{base - h - 10} Z', '#b9ab8c', sty)
    return o



def banderole(x, y, w, text, flip=1, size=22):
    """A medieval speech scroll with a word or symbol."""
    sty = bstyle(2.2)
    d = (f'M {x},{y} L {x + w},{y} Q {x + w + 10},{y + 10} {x + w},{y + 22} L {x},{y + 22} Q {x - 10},{y + 12} {x},{y} Z')
    o = P(d, '#fbf4e3', sty)
    o += P(f'M {x + w},{y} Q {x + w + 14},{y - 6} {x + w + 12},{y + 8} Z', '#e3d6bb', sty)
    o += P(f'M {x},{y + 22} Q {x - 14},{y + 28} {x - 12},{y + 14} Z', '#e3d6bb', sty)
    o += (f'<text x="{x + w / 2}" y="{y + 18}" text-anchor="middle" font-family="DejaVu Serif" font-weight="bold" '
          f'font-size="{size}" fill="{INK}">{text}</text>')
    tail = f'M {x + w * (0.3 if flip > 0 else 0.7)},{y + 22} L {x + w * (0.3 if flip > 0 else 0.7) - 8 * flip},{y + 40} L {x + w * (0.3 if flip > 0 else 0.7) + 8},{y + 22} Z'
    o += P(tail, '#fbf4e3', sty)
    return o

def scene2():
    rnd = random.Random(42)
    o = []
    hzn = 520
    o.append(gradient_rect(0, 0, 1200, hzn, ['#3f74c4', '#7fb2e6', '#bcdcf3', '#eef6fb']))
    o.append(sky_dragon(170, 110, 0.55, '#ffc93c', '#ffd25a', party.STYLES['bold']))
    o.append(ring_band(hzn, top_side=262, top_mid=340, foot_in=150, arch_mid=210, seed=8, view=110))
    for (x, y, sc) in [(380, 140, 0.8), (930, 120, 1.0), (1100, 230, 0.6)]:
        o.append(cloud(x, y, sc, party.STYLES['bold']))
    # the near land: the flank of the ring, lush and settled
    o.append(P(f'M -20,800 L -20,{hzn} Q 600,{hzn - 24} 1220,{hzn} L 1220,800 Z', '#8cbf5f', bstyle()))
    o.append(gradient_rect(0, hzn + 4, 1200, 300, ['#a7cf78', '#7db558', '#5f9a42']))
    # the academy city on either side
    for (x, w, h, roof, fill) in [(70, 90, 120, 'dome', '#efe4cc'), (170, 80, 90, 'gable', '#e3d6bb'), (260, 70, 140, 'flat', '#d8cfbf'),
                                  (950, 80, 110, 'gable', '#e3d6bb'), (1040, 100, 150, 'dome', '#efe4cc'), (1140, 80, 95, 'flat', '#d8cfbf')]:
        o.append(city_block(x, hzn + 70, w, h, fill, roof))
    for (x, c) in [(120, '#c8342b'), (310, '#2e6fd2'), (900, '#2e6fd2'), (1180, '#c8342b')]:
        o.append(limb([(x, hzn + 70), (x, hzn - 60)], 4, party.WOOD, bstyle(2)))
        o.append(banner(x, hzn - 58, 60, 26, c, '#e8c35a', phase=x * 0.01, sty=bstyle(2)))
    # plaza
    o.append(P('M -20,800 L 120,640 L 1080,640 L 1220,800 Z', '#e6dcc6', bstyle(2.6)))
    for k in range(1, 7):
        y = 640 + k * 26
        t = (y - 640) / 160
        o.append(f'<path d="M {120 - 140 * t:.0f},{y} L {1080 + 140 * t:.0f},{y}" stroke="#c9bc9f" stroke-width="2"/>')
    for k in range(-6, 7):
        o.append(f'<path d="M {600 + k * 80},640 L {600 + k * 110},800" stroke="#c9bc9f" stroke-width="2"/>')
    # the thinking machine, with Red and Blue perched proudly on its shoulders
    m, lm = thinking_machine(600, 660)
    o.append(m)
    pl, pr = lm['perch_l'], lm['perch_r']
    o.append(dragon(pl[0] + 4, pl[1] - 14, 0.78, 'Red', pose_sit(head_angle=-20, wings='up', wing_rot=-26, wing_scale=1.15, tail='up'), flip=-1, expr='open'))
    o.append(dragon(pr[0] - 4, pr[1] - 14, 0.78, 'Blue', pose_sit(head_angle=-16, wings='folded', wing_rot=-14, wing_scale=1.35), flip=1, expr='happy'))
    # a White courier on wings of light, bringing a question up to the machine
    o.append(person(1010, 330, 0.6, 'White', 'fly', '#eceff4', '#9fb7d4', flip=-1, look=4, wings='spectral', item='scroll'))
    # a slate of geometry for the debaters
    o.append(chalkboard(64, 760))
    o.append(person(128, 784, 0.86, 'Gold', 'offer', '#f3efe6', '#c08a1e', flip=-1, look=-8, item='brush'))
    # dragonborn at the base: asking, reading answers, debating, marvelling
    sx, sy_ = lm['slot']
    tx, ty = lm['tape']
    o.append(f'<g transform="translate({sx - 14},{sy_ - 2}) rotate(-88)">' + P('M -5,-18 L 5,-18 L 5,18 L -5,18 Z', '#f4ead2', bstyle(1.6)) + '</g>')
    o.append(person(sx - 66, 712, 0.82, 'White', 'offer', '#6f7b8a', '#9b2d2d', flip=1, robe=True, look=-6))
    o.append(person(sx - 126, 718, 0.8, 'Black', 'hold', '#2f6b6b', '#e8c35a', item='scroll', look=-14))
    o.append(person(sx - 186, 724, 0.78, 'Green', 'read', '#5c6b3a', '#7a4e2a', item='book', tail_item='quill'))

    # the answer tape, curling down to a reader
    o.append(limb([(tx, ty), (tx + 30, ty + 20), (tx + 10, ty + 40), (tx + 40, ty + 58)], 8, '#f4ead2', bstyle(2)))
    for k in range(4):
        o.append(f'<rect x="{tx + 8 + k * 8}" y="{ty + 14 + k * 12}" width="4" height="4" fill="{INK}"/>')
    o.append(person(tx + 74, 714, 0.84, 'Silver', 'read', '#4b3a7a', '#f2d16b', flip=-1, item='tape'))
    o.append(person(tx + 140, 722, 0.8, 'Red', 'awe', '#8d98a6', '#2f4f8f', flip=-1, look=-12))
    o.append(person(tx + 200, 728, 0.8, 'Blue', 'point', '#efe4cc', '#2b5fa8', flip=-1, look=-30))
    # debaters and children at the front
    o.append(person(212, 792, 0.95, 'Blue', 'wave', '#e9dfc6', '#1f3f73', look=-6))
    o.append(person(296, 796, 0.95, 'Red', 'hold', '#55663a', '#7a4e2a', flip=-1, item='book'))
    o.append(person(980, 792, 0.9, 'Green', 'point', '#5c6b3a', '#3e5a4a', look=-34, flip=-1))
    o.append(person(1050, 796, 0.55, 'White', 'awe', '#9fd0f0', '#2b5fa8', flip=-1, child=True, look=-30))
    o.append(kite(1150, 446, (1098, 745), s=0.9))
    o.append(person(1110, 796, 0.55, 'Black', 'raise', '#c58bff', '#e8c35a', flip=-1, child=True, look=-30))
    o.append(banderole(160, 626, 60, '?', size=24))
    o.append(banderole(336, 600, 60, '∴', flip=-1, size=24))
    o.append(banderole(tx + 46, 590, 56, '!', flip=-1, size=24))
    return ''.join(o)


# ============================================================ Epoch 3: the faiths and their icons
def icon_black_church(cx, cy, r):
    """The Black dragon's church: an open dragon's eye in a dark diamond, with four points of light."""
    sty = bstyle(max(1.6, r * 0.06))
    o = P(f'M {cx},{cy - r} L {cx + r * 0.86},{cy} L {cx},{cy + r} L {cx - r * 0.86},{cy} Z', '#2b2638', sty)
    o += f'<path d="M {cx},{cy - r * 0.84} L {cx + r * 0.72},{cy} L {cx},{cy + r * 0.84} L {cx - r * 0.72},{cy} Z" fill="none" stroke="#e8c35a" stroke-width="{r * 0.05:.1f}"/>'
    o += P(f'M {cx - r * 0.55},{cy} Q {cx},{cy - r * 0.48} {cx + r * 0.55},{cy} Q {cx},{cy + r * 0.48} {cx - r * 0.55},{cy} Z', '#ffe27a', sty)
    o += f'<circle cx="{cx}" cy="{cy}" r="{r * 0.2:.1f}" fill="#9b6bd6"/>'
    o += f'<ellipse cx="{cx}" cy="{cy}" rx="{r * 0.06:.1f}" ry="{r * 0.19:.1f}" fill="{INK}"/>'
    for (dx, dy) in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        o += f'<circle cx="{cx + dx * r * 0.62:.1f}" cy="{cy + dy * r * 0.62:.1f}" r="{r * 0.06:.1f}" fill="#c58bff"/>'
    return o


def icon_ring(cx, cy, r):
    """The Cult of the Ring (one of Blue's creations): Azhi devouring its own tail."""
    from tapestry_lib import tube_outline
    sty = bstyle(max(1.6, r * 0.06))
    o = circ(cx, cy, r, '#eaf3fb', sty)
    R_ = r * 0.62
    a0, a1 = math.radians(-30), math.radians(-30 + 312)
    angs = np.linspace(a0, a1, 200)
    C = np.stack([cx + R_ * np.cos(angs), cy + R_ * np.sin(angs)], 1)
    w = np.linspace(r * 0.27, r * 0.07, len(C))
    body = tube_outline(C, w)
    o += P(dpath(body), '#2e6fd2', sty)
    inner = C + (np.stack([cx - C[:, 0], cy - C[:, 1]], 1) / R_) * (w * 0.28)[:, None]
    o += f'<path d="{dpath(inner[:-20], False)}" stroke="#4fc1b3" stroke-width="{r * 0.07:.1f}" fill="none" stroke-dasharray="{r * 0.06:.1f} {r * 0.05:.1f}"/>'
    # the head at a0, its jaws closing on the tail tip
    hx, hy = C[0]
    tip = C[-1]
    d = np.array(tip) - np.array([hx, hy])
    ang = math.degrees(math.atan2(d[1], d[0]))
    k = r / 100
    head = (P('M -6,-18 C 6,-30 30,-28 44,-14 L 62,-8 L 40,-2 L 62,6 L 40,14 C 20,22 0,18 -6,10 Z', '#2e6fd2', dict(sty, stroke=sty['stroke'] / k))
            + P('M 2,-20 C -10,-40 -26,-44 -34,-34 C -24,-32 -12,-26 -4,-14 Z', '#efe4c9', dict(sty, stroke=sty['stroke'] / k))
            + f'<ellipse cx="22" cy="-12" rx="5" ry="4" fill="#ffe27a" stroke="{INK}" stroke-width="{1.4 / k:.2f}"/>'
            + f'<ellipse cx="23" cy="-12" rx="1.4" ry="3.4" fill="{INK}"/>')
    o += f'<g transform="translate({hx:.1f},{hy:.1f}) rotate({ang:.1f}) scale({k * 0.9:.3f},{-k * 0.9:.3f})">{head}</g>'
    o += f'<circle cx="{cx}" cy="{cy}" r="{r * 0.18:.1f}" fill="#5e8fb8" stroke="{INK}" stroke-width="{r * 0.03:.1f}"/>'
    return o


def icon_machine(cx, cy, r):
    """The machine revivalists: a gear around the great eye, with an orbiting ring."""
    sty = bstyle(max(1.6, r * 0.06))
    pts = []
    for i in range(48):
        a = math.radians(i * 7.5)
        rr = r if (i % 4) in (0, 1) else r * 0.84
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    o = P('M ' + ' L '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + ' Z', BRASS2, sty)
    o += circ(cx, cy, r * 0.66, '#1f3540', sty)
    o += circ(cx, cy, r * 0.42, '#7ff7ea', bstyle(max(1.2, r * 0.04)))
    o += circ(cx, cy, r * 0.14, '#e8fffb', bstyle(max(1.2, r * 0.03)))
    o += f'<ellipse cx="{cx}" cy="{cy}" rx="{r * 1.12:.1f}" ry="{r * 0.28:.1f}" fill="none" stroke="{INK}" stroke-width="{r * 0.12:.1f}" transform="rotate(-18 {cx} {cy})"/>'
    o += f'<ellipse cx="{cx}" cy="{cy}" rx="{r * 1.12:.1f}" ry="{r * 0.28:.1f}" fill="none" stroke="#e9c66a" stroke-width="{r * 0.07:.1f}" transform="rotate(-18 {cx} {cy})"/>'
    t = math.radians(-18)
    px, py = r * 1.12 * math.cos(0.4), r * 0.28 * math.sin(0.4)
    o += circ(cx + px * math.cos(t) - py * math.sin(t), cy + px * math.sin(t) + py * math.cos(t), r * 0.1, '#ff7a7a', bstyle(max(1.2, r * 0.03)))
    return o


ICONS = {'black_church': icon_black_church, 'cult_of_the_ring': icon_ring, 'machine_revivalists': icon_machine}
ICON_NAMES = {'black_church': "The Black's Church", 'cult_of_the_ring': 'The Cult of the Ring',
              'machine_revivalists': 'The Machine Revivalists'}


def cathedral(cx, base):
    sty = bstyle(3)
    o = ''
    for side in (-1, 1):
        x = cx + side * 70
        o += P(f'M {x - 26},{base} L {x - 26},{base - 230} L {x},{base - 330} L {x + 26},{base - 230} L {x + 26},{base} Z', '#4a4360', sty)
        o += P(f'M {x - 10},{base - 200} Q {x},{base - 222} {x + 10},{base - 200} L {x + 10},{base - 160} L {x - 10},{base - 160} Z', '#b48cff', bstyle(2))
    o += P(f'M {cx - 50},{base} L {cx - 50},{base - 250} L {cx},{base - 300} L {cx + 50},{base - 250} L {cx + 50},{base} Z', '#5a5274', sty)
    o += circ(cx, base - 200, 34, '#7a5aa8', sty)
    o += icon_black_church(cx, base - 200, 26)
    o += P(f'M {cx - 22},{base} L {cx - 22},{base - 70} Q {cx},{base - 96} {cx + 22},{base - 70} L {cx + 22},{base} Z', '#2b2638', bstyle(2.4))
    return o, (cx, base - 330)


def ring_temple(cx, base):
    """The Cult of the Ring: an open colonnade crowned by a great standing hoop, the ring itself,
    with the ouroboros at its heart (no dome: the dome belongs to the machine and its revivalists)."""
    sty = bstyle(3)
    o = P(f'M {cx - 150},{base} L {cx - 150},{base - 14} L {cx + 150},{base - 14} L {cx + 150},{base} Z', '#d8cfbf', sty)
    o += P(f'M {cx - 130},{base - 14} L {cx - 130},{base - 110} L {cx + 130},{base - 110} L {cx + 130},{base - 14} Z', '#eaf3fb', sty)
    for k in range(6):
        x = cx - 110 + k * 44
        o += P(f'M {x - 12},{base - 14} L {x - 12},{base - 70} Q {x},{base - 88} {x + 12},{base - 70} L {x + 12},{base - 14} Z', '#2e6fd2', bstyle(2.2))
    o += P(f'M {cx - 150},{base - 110} L {cx + 150},{base - 110} L {cx + 140},{base - 128} L {cx - 140},{base - 128} Z', '#d4a63c', sty)
    # wave frieze along the cornice
    o += f'<path d="M {cx - 138},{base - 119} ' + ' '.join(f'q 5,-6 10,0' for _ in range(27)) + '" stroke="#2e6fd2" stroke-width="2.4" fill="none"/>'
    # stepped attic, then the great hoop
    o += P(f'M {cx - 96},{base - 128} L {cx - 96},{base - 146} L {cx + 96},{base - 146} L {cx + 96},{base - 128} Z', '#eaf3fb', sty)
    hy = base - 230
    o += f'<circle cx="{cx}" cy="{hy}" r="80" fill="none" stroke="{INK}" stroke-width="30"/>'
    o += f'<circle cx="{cx}" cy="{hy}" r="80" fill="none" stroke="#5e8fb8" stroke-width="23"/>'
    o += f'<circle cx="{cx}" cy="{hy}" r="80" fill="none" stroke="#d4a63c" stroke-width="4" stroke-dasharray="14 10"/>'
    o += P(f'M {cx - 40},{base - 146} L {cx - 30},{hy + 70} L {cx + 30},{hy + 70} L {cx + 40},{base - 146} Z', '#d4a63c', sty)
    o += icon_ring(cx, hy, 52)
    for side in (-1, 1):   # corner pinnacles with little flames of blue light
        x = cx + side * 122
        o += P(f'M {x - 9},{base - 128} L {x - 6},{base - 176} L {x + 6},{base - 176} L {x + 9},{base - 128} Z', '#eaf3fb', sty)
        o += P(f'M {x},{base - 198} Q {x + 9},{base - 182} {x},{base - 176} Q {x - 9},{base - 182} {x},{base - 198} Z', '#7fc6ff', bstyle(1.8))
    return o, (cx, hy - 90)


def gear_temple(cx, base):
    """The machine revivalists' temple, built to echo the Epoch 2 thinking machine: brass, steam
    towers, lit panels, the ribbed dome with its glowing antenna, and the orrery ring round the eye."""
    sty = bstyle(3)
    o = ''
    for side in (-1, 1):   # steam towers like the machine's
        x = cx + side * 92
        o += P(f'M {x - 16},{base} L {x - 14},{base - 300} L {x + 14},{base - 300} L {x + 16},{base} Z', STONE2, sty)
        o += P(f'M {x - 20},{base - 300} L {x + 20},{base - 300} L {x + 15},{base - 314} L {x - 15},{base - 314} Z', BRASS2, sty)
        for k in range(4):
            o += f'<rect x="{x - 9}" y="{base - 280 + k * 46}" width="18" height="20" rx="4" fill="#2a3a44" stroke="{INK}" stroke-width="2"/>'
            o += f'<circle cx="{x - 3}" cy="{base - 270 + k * 46}" r="2.6" fill="{["#7ff7ea", "#ffd34d", "#ff7a7a", "#7ff7ea"][k]}"/>'
            o += f'<circle cx="{x + 4}" cy="{base - 270 + k * 46}" r="2.6" fill="{["#ffd34d", "#7ff7ea", "#7ff7ea", "#ff7a7a"][k]}"/>'
        for k in range(3):
            o += f'<circle cx="{x + side * (6 + k * 16)}" cy="{base - 330 - k * 18}" r="{9 + k * 5}" fill="#c8c2c8" opacity="{0.8 - k * 0.2:.2f}"/>'
    o += P(f'M {cx - 74},{base} L {cx - 70},{base - 210} Q {cx},{base - 232} {cx + 70},{base - 210} L {cx + 74},{base} Z', BRASS2, sty)
    o += P(f'M {cx - 62},{base - 14} L {cx - 58},{base - 198} Q {cx},{base - 216} {cx + 58},{base - 198} L {cx + 62},{base - 14} Z', '#e9c66a', bstyle(2.2))
    # the ribbed dome and the glowing antenna, as on the machine
    o += P(f'M {cx - 64},{base - 214} Q {cx},{base - 300} {cx + 64},{base - 214} Z', '#c7cfd6', sty)
    for k in (-34, 0, 34):
        o += f'<path d="M {cx + k * 0.4},{base - 282 + abs(k) * 0.3} Q {cx + k},{base - 250} {cx + k * 1.6},{base - 216}" stroke="#8d98a6" stroke-width="2.4" fill="none"/>'
    o += limb([(cx, base - 276), (cx, base - 330)], 5, BRASS_D, sty)
    o += glow(cx, base - 336, 34, '#7ff7ea')
    o += circ(cx, base - 336, 8, '#7ff7ea', sty)
    o += icon_machine(cx, base - 126, 50)
    o += P(f'M {cx - 18},{base} L {cx - 18},{base - 36} Q {cx},{base - 48} {cx + 18},{base - 36} L {cx + 18},{base} Z', '#5a3a22', bstyle(2.4))
    return o, (cx, base - 336)


def faith_beam(x, top, colour, seed):
    """Power drawn down from the sky into a temple: a soft column with sparkles."""
    rnd = random.Random(seed)
    gid = uid('beam')
    o = (f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{colour}" stop-opacity="0"/>'
         f'<stop offset="1" stop-color="{colour}" stop-opacity=".55"/></linearGradient>'
         f'<path d="M {x - 70},0 L {x + 70},0 L {x + 24},{top} L {x - 24},{top} Z" fill="url(#{gid})"/>')
    o += glow(x, top, 90, colour)
    for _ in range(10):
        sx, sy_ = x + rnd.uniform(-40, 40), rnd.uniform(20, top - 20)
        r = rnd.uniform(4, 8)
        o += f'<path d="M {sx},{sy_ - r} L {sx + r * .25},{sy_} L {sx},{sy_ + r} L {sx - r * .25},{sy_} Z M {sx - r},{sy_} L {sx},{sy_ + r * .25} L {sx + r},{sy_} L {sx},{sy_ - r * .25} Z" fill="#fff8dc" opacity=".9"/>'
    return o


def scene3():
    rnd = random.Random(43)
    o = []
    hzn = 520
    o.append(gradient_rect(0, 0, 1200, hzn, ['#2b2357', '#5a3f86', '#b46a98', '#f0a98a', '#f8d6a0']))
    o.append(stars(60, 12, ymax=200))
    o.append(sky_dragon(1050, 110, 0.5, '#e6edf8', '#bcd2ff', party.STYLES['bold'], flip=-1))
    o.append(ring_band(hzn, top_side=250, top_mid=320, foot_in=160, arch_mid=200, seed=11, night=True, op=0.92, view=20))
    # the three great temples (drawn below); power is drawn down into each
    c1, t1 = cathedral(250, hzn + 110)
    c2, t2 = ring_temple(600, hzn + 100)
    c3, t3 = gear_temple(960, hzn + 110)
    for (t_, c, sd) in [(t1, '#b48cff', 1), (t2, '#7fc6ff', 2), (t3, '#7ff7ea', 3)]:
        o.append(faith_beam(t_[0], t_[1], c, sd))
    # land
    o.append(P(f'M -20,800 L -20,{hzn} Q 600,{hzn - 20} 1220,{hzn} L 1220,800 Z', '#7a8f5a', bstyle()))
    o.append(gradient_rect(0, hzn + 4, 1200, 300, ['#8fa66a', '#6f8a4f', '#556e3d']))
    # many faiths in the distance: small shrines and towers
    for (x, kind) in [(60, 'obelisk'), (140, 'pagoda'), (420, 'stupa'), (790, 'obelisk'), (1110, 'pagoda'), (1170, 'stupa')]:
        base = hzn + 40
        if kind == 'obelisk':
            o.append(P(f'M {x - 10},{base} L {x - 6},{base - 90} L {x},{base - 104} L {x + 6},{base - 90} L {x + 10},{base} Z', '#d8cfbf', bstyle(2)))
        elif kind == 'pagoda':
            for k in range(3):
                w_ = 52 - k * 12
                y = base - k * 26
                o.append(P(f'M {x - w_ / 2},{y} L {x - w_ / 2},{y - 18} L {x + w_ / 2},{y - 18} L {x + w_ / 2},{y} Z', '#c46b4a', bstyle(2)))
                o.append(P(f'M {x - w_ / 2 - 8},{y - 18} Q {x},{y - 30} {x + w_ / 2 + 8},{y - 18} Z', '#4a6a5a', bstyle(2)))
        else:
            o.append(P(f'M {x - 30},{base} Q {x},{base - 80} {x + 30},{base} Z', '#efe4cc', bstyle(2)))
            o.append(limb([(x, base - 58), (x, base - 82)], 4, '#d4a63c', bstyle(1.6)))
    o += [c1, c2, c3]
    # banners on poles in the colours of the faiths
    for (x, c, trim, ic) in [(110, '#2b2638', '#c58bff', 'black_church'), (390, '#2b2638', '#c58bff', 'black_church'),
                             (450, '#2e6fd2', '#ffffff', 'cult_of_the_ring'), (750, '#2e6fd2', '#ffffff', 'cult_of_the_ring'),
                             (820, '#8a5a2b', '#7ff7ea', 'machine_revivalists'), (1110, '#8a5a2b', '#7ff7ea', 'machine_revivalists')]:
        o.append(limb([(x, hzn + 150), (x, hzn - 40)], 4, party.WOOD, bstyle(2)))
        o.append(circ(x, hzn - 44, 6, '#d4a63c', bstyle(2)))
        o.append(banner(x, hzn - 38, 110, 40, c, trim, phase=x * 0.02, emblem=ICONS[ic](0, 0, 14), sty=bstyle(2.2)))
    # the plaza between them: a bazaar of ideas
    o.append(P('M -20,800 L 80,660 L 1120,660 L 1220,800 Z', '#d9c9a8', bstyle(2.6)))
    for k in range(1, 6):
        y = 660 + k * 28
        t = (y - 660) / 140
        o.append(f'<path d="M {80 - 100 * t:.0f},{y} L {1120 + 100 * t:.0f},{y}" stroke="#bfae8a" stroke-width="2"/>')
    # market awnings along the back of the plaza
    for (x, c) in [(150, '#c8342b'), (430, '#2e6fd2'), (770, '#e3a62a'), (1050, '#3c9a47')]:
        o.append(P(f'M {x - 50},{668} L {x - 50},{628} L {x + 50},{628} L {x + 50},{668} Z', '#e9dfc6', bstyle(2)))
        for k in range(5):
            o.append(P(f'M {x - 56 + k * 22},{628} L {x - 56 + k * 22 + 22},{628} L {x - 56 + k * 22 + 22},{614} Q {x - 56 + k * 22 + 11},{622} {x - 56 + k * 22},{614} Z',
                       c if k % 2 == 0 else '#ffffff', bstyle(1.8)))
    # icons for sale, hung under the awnings
    for (x, ic) in [(150, 'black_church'), (430, 'cult_of_the_ring'), (770, 'machine_revivalists'), (1050, 'cult_of_the_ring')]:
        for k in (-30, 0, 30):
            o.append(f'<path d="M {x + k},{628} L {x + k},{640}" stroke="{INK}" stroke-width="1.2"/>')
            o.append(ICONS[ic](x + k, 650, 9))
    # strings of paper lanterns across the plaza, lit for the evening
    o.append(lantern_string(200, 622, 380, 622, 14, 5, 1))
    o.append(lantern_string(820, 622, 1000, 622, 14, 5, 2))
    o.append(lantern_string(-10, 600, 100, 622, 10, 2, 3))
    o.append(lantern_string(1100, 622, 1210, 600, 10, 2, 4))
    # a Blue huckster preaching from a crate, with a speaking horn, under the ring banner
    o.append(P('M 520,740 L 520,712 L 580,712 L 580,740 Z', '#a8743c', bstyle(2.4)))
    o.append(person(550, 712, 0.86, 'Blue', 'wave', '#e9dfc6', '#2e6fd2', look=-10))
    o.append(P('M 584,606 L 620,590 L 622,618 Z', '#d4a63c', bstyle(2)))
    o.append(banderole(470, 560, 104, 'The Ring!', flip=1, size=17))
    # processions and worshippers
    cols7 = ['Red', 'Blue', 'Green', 'White', 'Black', 'Gold', 'Silver']
    o.append(person(160, 760, 0.82, 'Black', 'hold', '#2b2638', '#c58bff', item='banner:#2b2638', look=-8))
    o.append(person(220, 768, 0.8, 'Silver', 'pray', '#4b3a7a', '#c58bff', kneel=True, robe=True, look=-20))
    o.append(person(290, 762, 0.8, 'Red', 'raise', '#2b2638', '#c58bff', look=-30))
    o.append(person(680, 770, 0.8, 'Gold', 'awe', '#f3efe6', '#2e6fd2', flip=-1, look=-20))
    o.append(person(740, 764, 0.8, 'Green', 'pray', '#5c6b3a', '#2e6fd2', flip=-1, kneel=True, tail_item='censer'))
    o.append(person(930, 766, 0.84, 'Red', 'hold', '#8a5a2b', '#7ff7ea', flip=-1, item='banner:#8a5a2b', look=-8))
    o.append(person(1000, 772, 0.8, 'Blue', 'raise', '#8a5a2b', '#7ff7ea', flip=-1, look=-30))
    o.append(person(1060, 768, 0.8, 'Black', 'read', '#5a3a22', '#7ff7ea', flip=-1, item='book'))
    back = [(x + rnd.uniform(-6, 6), 690 + rnd.uniform(-4, 6)) for x in range(110, 1100, 58) if not 500 < x < 640]
    o.append(crowd(back, 9, cols7, 0.46, ['raise', 'pray', 'stand', 'awe', 'hold']))
    # a White monk on the edge, quietly sketching the scene (the weavers' own)
    o.append(person(1150, 790, 0.86, 'White', 'read', '#eceff4', '#9fb7d4', flip=-1, item='scroll', robe=True, look=8))
    return ''.join(o)


# ============================================================ Epoch 4
def eggshell(cx, yb, rw, rh, fill, speck, seed, lean=0):
    """Lower half of a giant cracked egg, with a zigzag rim (after lore_panels.py)."""
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
    o = f'<g transform="rotate({lean},{cx},{yb})">' + P(d, fill, bstyle(3.2))
    # the inside of the shell, glimpsed over the rim
    o += f'<path d="M {cx - rw * 0.86},{top + 40} Q {cx},{top + 70} {cx + rw * 0.86},{top + 40}" stroke="{dark(fill, .18)}" stroke-width="6" fill="none" opacity=".6"/>'
    for _ in range(14):
        x = cx + rnd.uniform(-rw * .75, rw * .75); y = yb - rnd.uniform(18, rh * .8)
        o += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rnd.uniform(6, 13):.0f}" ry="{rnd.uniform(4, 9):.0f}" fill="{speck}" opacity=".8"/>'
    o += f'<path d="M {cx - rw * .55},{yb - rh * .55} Q {cx - rw * .7},{yb - rh * .2} {cx - rw * .35},{yb - 18}" fill="none" stroke="#ffffff" stroke-width="9" opacity=".45" stroke-linecap="round"/>'
    return o + '</g>'


def heart(x, y, r, fill='#ff8fb1'):
    return P(f'M {x},{y + r} C {x - r * 1.6},{y - r * 0.2} {x - r * 0.6},{y - r * 1.3} {x},{y - r * 0.4} '
             f'C {x + r * 0.6},{y - r * 1.3} {x + r * 1.6},{y - r * 0.2} {x},{y + r} Z', fill, bstyle(2))


def scene4():
    rnd = random.Random(44)
    o = []
    hzn = 520
    o.append(gradient_rect(0, 0, 1200, hzn, ['#7fb2e6', '#b9d6f0', '#ffd9c0', '#ffe9c8']))
    o.append(sky_dragon(1080, 150, 0.5, '#ffc93c', '#ffd25a', party.STYLES['bold'], flip=-1))
    o.append(ring_band(hzn, top_side=240, top_mid=310, foot_in=170, arch_mid=190, seed=14, op=0.9, view=250))
    for (x, y, sc) in [(240, 120, 0.7), (760, 90, 0.9)]:
        o.append(cloud(x, y, sc, party.STYLES['bold']))
    # land: a green valley by a lake
    o.append(P(f'M -20,800 L -20,{hzn} Q 600,{hzn - 20} 1220,{hzn} L 1220,800 Z', '#8cbf5f', bstyle()))
    o.append(gradient_rect(0, hzn + 4, 1200, 300, ['#b5d98a', '#8cbf5f', '#6aa84a']))
    o.append(P('M 640,560 Q 900,520 1220,540 L 1220,640 Q 980,650 760,620 Q 640,600 640,560 Z', '#3f86c8', bstyle()))
    for k in range(10):
        x, y = rnd.uniform(700, 1180), rnd.uniform(552, 626)
        o.append(f'<path d="M {x},{y} q 8,-6 16,0 q 8,-6 16,0" stroke="#d8eeff" stroke-width="2.4" fill="none" stroke-linecap="round"/>')
    o.append(P('M -20,600 Q 160,520 420,560 L 420,620 L -20,640 Z', '#7db558', bstyle()))
    for k, x in enumerate(range(30, 460, 70)):
        o.append(tree(x, 590 + (k % 2) * 8, 0.55, fill=rnd.choice(['#3f8a3c', '#4f9a40']), blossom='#ffb3d1', seed=70 + k))
    # Blue and Green, nuzzling in the background (on the lake shore)
    o.append(P('M 880,600 Q 900,566 990,560 Q 1100,556 1140,580 Q 1120,604 1010,606 Q 920,610 880,600 Z', '#9cc96e', bstyle(2.6)))
    o.append(dragon(962, 582, 0.62, 'Blue', pose_sit(head_angle=22, wings='folded', wing_rot=-10), flip=1, expr='closed'))
    o.append(dragon(1062, 582, 0.62, 'Green', pose_sit(head_angle=22, wings='folded', wing_rot=-10, tail='curl'), flip=-1, expr='closed'))
    o.append(heart(1012, 470, 9))
    o.append(heart(1028, 452, 6))
    # dragonflies over the water
    o.append(dragonfly(868, 600, 0.9, -10))
    o.append(dragonfly(1150, 556, 0.8, 12))
    # a picnic on the grass, abandoned mid-bite
    o.append(P('M 40,700 L 200,690 L 236,724 L 70,738 Z', '#f6f1e3', bstyle(2.4)))
    for k in range(4):
        o.append(f'<path d="M {48 + k * 40},{699 - k * 2.5} L {78 + k * 41},{737 - k * 3}" stroke="#e2432b" stroke-width="5" opacity=".7"/>')
    for k in range(3):
        o.append(f'<path d="M {52 + k * 6},{706 + k * 10} L {206 + k * 10},{696 + k * 9}" stroke="#e2432b" stroke-width="5" opacity=".7"/>')
    o.append(f'<g transform="translate(110,700)">{tail_item_svg("basket", bstyle(2.2))}</g>')
    o.append(f'<g transform="translate(176,708)">{tail_item_svg("cup", bstyle(2.2))}</g>')
    # the two young Unphased dragons, cruising about overhead
    o.append(motion_lines([(330, 300), (380, 270), (430, 250), (470, 244)], '#e6dcff', n=3, gap=10, width=4))
    o.append(dragon(540, 236, 0.62, None, pose_fly(head_angle=-8), flip=1, rot=-12, shimmer='all', seed=41, expr='happy'))
    o.append(motion_lines([(900, 140), (850, 170), (800, 186), (760, 190)], '#e6dcff', n=3, gap=10, width=4))
    o.append(dragon(690, 196, 0.58, None, pose_fly(head_angle=4), flip=-1, rot=8, shimmer='all', seed=43, expr='happy'))
    # the nest and the two empty eggshells
    o.append(P('M 300,712 Q 600,646 900,712 Q 600,752 300,712 Z', '#9a7046', bstyle(3)))
    for k in range(26):
        a = math.radians(rnd.uniform(200, 340))
        x0 = 600 + 300 * math.cos(a) * rnd.uniform(0.7, 1.0)
        y0 = 712 + 80 * math.sin(a) * rnd.uniform(0.6, 1.0)
        o.append(f'<path d="M {x0:.0f},{y0:.0f} l {rnd.uniform(-40, 40):.0f},{rnd.uniform(-10, 10):.0f}" stroke="#6b4a2f" stroke-width="5" stroke-linecap="round"/>')
    o.append(eggshell(500, 690, 120, 200, '#bfe0f7', '#5f9bd8', 3, lean=-8))
    o.append(eggshell(710, 694, 118, 190, '#d3edc0', '#5aa64a', 8, lean=9))
    o.append(P('M 600,712 L 628,676 L 660,700 L 640,716 Z', '#bfe0f7', bstyle(2.4)))
    o.append(P('M 380,722 L 404,696 L 430,716 Z', '#d3edc0', bstyle(2.4)))
    # dragonborn marvelling: pointing up at the new dragons
    o.append(person(170, 776, 0.98, 'Red', 'point', '#8d98a6', '#2f4f8f', look=-34))
    o.append(person(262, 784, 0.92, 'Gold', 'awe', '#f3efe6', '#c08a1e', look=-28))
    o.append(person(330, 790, 0.58, 'Silver', 'point', '#9fd0f0', '#4b3a7a', child=True, look=-40))
    # a White painter, catching the moment on canvas (the weavers' own art)
    paint = (f'<path d="M -26,14 Q -10,4 0,10 Q 12,2 26,12" stroke="#7fb2e6" stroke-width="3" fill="none"/>'
             f'<path d="M -22,-6 q 8,-8 16,-2 l 6,-6 l -2,9 q -8,6 -20,-1 Z" fill="#e3d2ff" stroke="{INK}" stroke-width="1.2"/>'
             f'<path d="M 4,-14 q 8,-6 15,0 l 6,-5 l -2,8 q -8,5 -19,-3 Z" fill="#ffe2a8" stroke="{INK}" stroke-width="1.2"/>'
             f'<path d="M -12,22 Q -12,14 -6,14 L -2,18 L 2,14 Q 8,14 8,22 Z" fill="#bfe0f7" stroke="{INK}" stroke-width="1.2"/>')
    o.append(easel(820, 788, paint))
    o.append(person(894, 786, 0.92, 'White', 'hold', '#6f7b8a', '#9b2d2d', flip=-1, look=-26, robe=True, item='brush'))
    o.append(person(980, 776, 0.98, 'Black', 'point', '#2f6b6b', '#e8c35a', flip=-1, look=-36))
    o.append(person(1070, 786, 0.94, 'Green', 'raise', '#5c6b3a', '#7a4e2a', flip=-1, look=-30, tail_item='parasol'))
    o.append(person(610, 790, 0.9, 'Blue', 'offer', '#efe4cc', '#2b5fa8', flip=1, look=-4))
    for k, (x, y) in enumerate([(60, 770), (430, 790), (790, 796), (1160, 780)]):
        o.append(flower_tuft(x, y, 20 + k, petals=('#ffb3d1', '#fff2a8', '#b3d1ff')))
    return ''.join(o)


# ============================================================ Epoch 5
def emblem_sun(r):
    o = ''
    for k in range(8):
        a = math.radians(k * 45)
        o += f'<path d="M {r * 0.62 * math.cos(a):.1f},{r * 0.62 * math.sin(a):.1f} L {r * math.cos(a + 0.2):.1f},{r * math.sin(a + 0.2):.1f} L {r * math.cos(a - 0.2):.1f},{r * math.sin(a - 0.2):.1f} Z" fill="#fff4b0"/>'
    return o + f'<circle cx="0" cy="0" r="{r * 0.55:.1f}" fill="#fff4b0" stroke="{INK}" stroke-width="1.6"/>'


def emblem_moon(r):
    return (f'<path d="M {r * 0.2},{-r * 0.8} A {r * 0.8},{r * 0.8} 0 1 0 {r * 0.2},{r * 0.8} A {r * 0.6},{r * 0.6} 0 1 1 {r * 0.2},{-r * 0.8} Z" '
            f'fill="#e8ecf2" stroke="{INK}" stroke-width="1.6"/>')


def scene5():
    rnd = random.Random(45)
    o = []
    hzn = 520
    o.append(gradient_rect(0, 0, 1200, hzn, ['#3a3f7a', '#7a6aa8', '#d9a0a8', '#f6c98a']))
    o.append(glow(120, 420, 420, '#ffb347').replace('.85', '.55'))
    o.append(glow(1080, 120, 320, '#bcd2ff').replace('.85', '.5'))
    o.append(stars(50, 15, ymax=180).replace('<circle cx="', '<circle opacity=".7" cx="', 0))
    # the real Gold (setting) and Silver (rising), so no one confuses them with Yellow and Grey
    o.append(ring_band(hzn, top_side=236, top_mid=300, foot_in=170, arch_mid=186, seed=17, op=0.88, view=60))
    o.append(sky_dragon(150, 200, 0.62, '#ffc93c', '#ffd25a', party.STYLES['bold']))
    o.append(sky_dragon(1050, 100, 0.56, '#e6edf8', '#bcd2ff', party.STYLES['bold'], flip=-1))
    # land and the great hill
    o.append(P(f'M -20,800 L -20,{hzn} Q 600,{hzn - 20} 1220,{hzn} L 1220,800 Z', '#86b25a', bstyle()))
    o.append(gradient_rect(0, hzn + 4, 1200, 300, ['#a7c972', '#86b25a', '#6a9a46']))
    o.append(P('M 120,800 Q 230,520 440,478 Q 600,452 760,478 Q 970,520 1080,800 Z', '#9cc96e', bstyle(3)))
    o.append(f'<path d="M 250,700 Q 330,540 470,500" stroke="#b8db8a" stroke-width="10" fill="none" opacity=".7" stroke-linecap="round"/>')
    # banners of the new colours on the hilltop
    for (x, c, em) in [(300, '#f0cf2e', emblem_sun(13)), (900, '#7d838c', emblem_moon(13))]:
        o.append(limb([(x, 600), (x, 440)], 4, party.WOOD, bstyle(2)))
        o.append(banner(x, 444, 90, 36, c, '#ffffff', phase=x * 0.03, emblem=em, sty=bstyle(2.2)))
    # sun-and-moon bunting strung across the hilltop for the festival
    o.append(bunting(300, 452, 900, 452, 30, 16, ['#f0cf2e', '#7d838c']))
    # the Yellow and Grey dragons, side by side like heraldic supporters
    o.append(glow(600, 380, 260, '#fff2c0'))
    # each gazes up at the one it reflects: Yellow toward the setting Gold, Grey toward the rising Silver
    o.append(dragon(486, 474, 0.84, 'Yellow', pose_sit(head_angle=-34, wings='up', wing_rot=-18, wing_scale=1.15, tail='curl'), flip=-1, expr='open'))
    o.append(dragon(714, 474, 0.84, 'Grey', pose_sit(head_angle=-34, wings='up', wing_rot=-18, wing_scale=1.15, tail='curl'), flip=1, expr='open'))
    # their newly phased followers on the slopes
    slots = [(380, 568), (440, 560), (500, 556), (340, 612), (400, 606), (460, 600), (520, 596), (300, 660), (370, 654), (440, 648)]
    left = [(x + rnd.uniform(-6, 6), y) for (x, y) in slots]
    right = [(1200 - x + rnd.uniform(-6, 6), y) for (x, y) in slots]
    o.append(crowd(left, 21, ['Yellow'], 0.42, ['raise', 'pray', 'awe'], outfits=['#7a3a2a', '#f2d16b', '#efe4cc', '#c46b4a']))
    o.append(crowd(right, 22, ['Grey'], 0.42, ['raise', 'pray', 'awe'], outfits=['#4a4f5c', '#c9d2e0', '#e9dfc6', '#6f7b8a']))
    # everyone else, all nine colours, gathered at the foot of the hill
    front = [
        (110, 770, 'Brown', 'wave', '#7c6a4e', '#5b7a3a', 1, 'drum'),
        (200, 778, 'Indigo', 'stand', '#2a2a33', '#7a2f3a', 1, None),
        (290, 786, 'Red', 'awe', '#8d98a6', '#2f4f8f', 1, None),
        (380, 792, 'Yellow', 'hold', '#7a3a2a', '#f2d16b', 1, 'banner:#f0cf2e'),
        (820, 792, 'Grey', 'hold', '#4a4f5c', '#c9d2e0', -1, 'banner:#7d838c'),
        (910, 786, 'Blue', 'point', '#efe4cc', '#2b5fa8', -1, None),
        (1000, 778, 'Green', 'awe', '#5c6b3a', '#3e5a4a', -1, None),
        (1090, 770, 'White', 'pray', '#6f7b8a', '#9b2d2d', -1, None),
        (1160, 780, 'Black', 'hold', '#2f6b6b', '#e8c35a', -1, 'horn'),
    ]
    for (x, y, drag, pose, out, acc, fl, item) in front:
        o.append(person(x, y, 0.9, drag, pose, out, acc, flip=fl, item=item, look=-22 if item != 'horn' else -30, robe=(drag in ('White', 'Grey')),
                        tail_item='lantern'))
    for k, (x, y) in enumerate([(40, 768), (530, 796), (670, 796), (1186, 770)]):
        o.append(flower_tuft(x, y, 40 + k, petals=('#fff2a8', '#ffffff', '#e3e8f0')))
    # a White dragonborn on wings of light, trailing a yellow and grey streamer between the two lights
    fx, fy = 640, 180
    hx, hy = fly_hand(fx, fy, 0.56, 'White', flip=1)
    for k, c in enumerate(('#f0cf2e', '#7d838c')):
        d = f'M {hx},{hy + k * 6} C {hx - 90},{hy - 40 + k * 6} {hx - 160},{hy + 50 + k * 6} {hx - 260},{hy + 10 + k * 6}'
        o.append(f'<path d="{d}" stroke="{INK}" stroke-width="9" fill="none" stroke-linecap="round"/><path d="{d}" stroke="{c}" stroke-width="5" fill="none" stroke-linecap="round"/>')
    o.append(person(fx, fy, 0.56, 'White', 'fly', '#eceff4', '#9fb7d4', look=0, wings='spectral'))
    return ''.join(o)

CAPTIONS = {
    0: 'Azhi Meets the Young Dragons, in the Depths of Space and Time',
    1: 'The wisest of them gave us knowing, and we embraced it.',
    2: 'The Great Thinking Machines, and the Second Age of Philosophy',
    3: 'Tapping into the very power of creation itself, philosophies diverge.',
    4: 'An accidental discovery: life springs forth anew.',
    5: 'Earthly reflections of the sun and moon.',
}
SCENES = {0: scene0, 1: scene1, 2: scene2, 3: scene3, 4: scene4, 5: scene5}


def render(n):
    scene = defs(party.STYLES['bold']) + SCENES[n]()
    svg = woven_frame(scene, CAPTIONS[n], str(n))
    open(f'build/tapestry_{n}.svg', 'w').write(svg)
    subprocess.run([sys.executable, 'svg2png.py', f'build/tapestry_{n}.svg', f'output/tapestry_{n}.png', '1640', '1340'], check=True)
    print('tapestry', n)


def render_icons():
    sheet = ['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="480" viewBox="0 0 1200 480">'
             '<rect width="1200" height="480" fill="#f3ecdc"/>']
    for k, (key, fn) in enumerate(ICONS.items()):
        one = (f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" viewBox="0 0 400 400">'
               f'<rect width="400" height="400" fill="#f3ecdc"/>{fn(200, 200, 150)}</svg>')
        open(f'build/icon_{key}.svg', 'w').write(one)
        subprocess.run([sys.executable, 'svg2png.py', f'build/icon_{key}.svg', f'output/icon_{key}.png', '400', '400'], check=True)
        cx = 200 + k * 400
        sheet.append(fn(cx, 200, 140))
        sheet.append(f'<text x="{cx}" y="420" text-anchor="middle" font-family="DejaVu Serif" font-weight="bold" '
                     f'font-size="28" fill="{INK}">{ICON_NAMES[key]}</text>')
    sheet.append('</svg>')
    open('build/icons_epoch3.svg', 'w').write(''.join(sheet))
    subprocess.run([sys.executable, 'svg2png.py', 'build/icons_epoch3.svg', 'output/icons_epoch3.png', '1200', '480'], check=True)
    print('icons')


def render_hall():
    W, H = 3360, 4140
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#cfc6b4"/>']
    o.append(f'<text x="{W / 2}" y="120" text-anchor="middle" font-family="DejaVu Serif" font-weight="bold" font-size="84" fill="{INK}">The Tapestry Hall</text>')
    o.append(f'<text x="{W / 2}" y="190" text-anchor="middle" font-family="DejaVu Serif" font-style="italic" font-size="40" fill="#5a4e40">'
             f'The history of Azhi, as the White monks wove it</text>')
    for n in sorted(SCENES):
        x = 20 + (n % 2) * 1660
        y = 240 + (n // 2) * 1300
        svg = open(f'build/tapestry_{n}.svg').read()
        inner = svg[svg.index('>') + 1: svg.rindex('</svg>')]
        o.append(f'<svg x="{x}" y="{y}" width="1640" height="1340" viewBox="0 0 1640 1340">{inner}</svg>')
    o.append('</svg>')
    open('build/tapestry_hall.svg', 'w').write(''.join(o))
    subprocess.run([sys.executable, 'svg2png.py', 'build/tapestry_hall.svg', 'output/tapestry_hall.png', str(W), str(H)], check=True)
    print('hall')


if __name__ == '__main__':
    which = [int(a) for a in sys.argv[1:]] or sorted(SCENES)
    for n in which:
        render(n)
    if not sys.argv[1:]:
        render_icons()
        render_hall()
