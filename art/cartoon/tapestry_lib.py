"""Drawing kit for the Tapestry Hall (2026-11-12): posable dragons, Azhi, dragonborn in
everyday poses, the Unphased shimmer, buildings, banners, the ring arch and the woven frame.
Saturday-Morning Bold throughout. Built on party.py; see art/tapestries.md for the plan."""
import math, os, random
import numpy as np
import colour_wheel  # noqa: F401  (adds Brown, Yellow, Indigo and Grey)
import party
from party import STYLES, P, limb, circ, glow, mix, dark, light, uid, head_svg, sword, staff, holy, \
    DRAGONS, HORN, col

st = STYLES['bold']
INK = st['line']
from forms import (catmull, dpath, frame, tube_outline, SIZE_K, WEBBED, TAIL_ITEMS, _unit, _rot,  # noqa: E402,F401
                   _hand, _foot, tail_item_svg, _green_tail, spectral_wings)


def S(scale, px=4.2):
    """A style whose outline renders about px pixels wide at this scale."""
    return dict(st, stroke=px / scale)


# ---------------------------------------------------------------- the Unphased shimmer
SHIMMER_SETS = {
    'all':  ['#2e6fd2', '#3c9a47', '#c8342b', '#4a4360', '#eceff4', '#e3a62a', '#aab5c2'],
    'warm': ['#ffc93c', '#f39c12', '#e3a62a', '#fff1b8', '#c8342b', '#eceff4', '#2e6fd2'],
    'cool': ['#cfd8e6', '#aab5c2', '#eef2f6', '#7fb2e6', '#4a4360', '#9ab0d0', '#3c9a47'],
}


def shimmer_defs(key, seed, size=140, s=1.0):
    """A blurred multi-colour pattern; returns (defs, pattern id)."""
    rnd = random.Random(seed)
    pid, fid = uid('shim'), uid('sf')
    cols = SHIMMER_SETS[key]
    blobs = ''
    for k in range(26):
        x, y = rnd.uniform(-20, size + 20), rnd.uniform(-20, size + 20)
        r = rnd.uniform(14, 28)
        c = cols[k % len(cols)]
        for dx in (-size, 0, size):
            for dy in (-size, 0, size):
                blobs += f'<circle cx="{x + dx:.0f}" cy="{y + dy:.0f}" r="{r:.0f}" fill="{c}"/>'
    d = (f'<filter id="{fid}" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="9"/></filter>'
         f'<pattern id="{pid}" patternUnits="userSpaceOnUse" width="{size}" height="{size}" '
         f'patternTransform="scale({s})"><rect width="{size}" height="{size}" fill="#b9a9d6"/>'
         f'<g filter="url(#{fid})">{blobs}</g></pattern>')
    return d, pid


# ---------------------------------------------------------------- posable dragon
def dragon(x, y, s, colour, pose, flip=1, rot=0, shimmer=None, seed=1, expr='open'):
    """A side-view dragon. Local units: about 220 long from tail tip to snout.

    pose: spine (tail tip -> head base, local points), widths along it, head angle (deg),
    wings ('spread', 'folded', 'up', 'none'), legs: list of (anchor index fraction, points, near?).
    colour: a DRAGONS key or (scale, belly). shimmer: None or 'all'/'warm'/'cool'.
    expr: 'open', 'closed' (eyes shut, content), 'happy', 'talk', 'wide'.
    """
    if shimmer:
        return _shimmer_dragon(x, y, s, pose, flip, rot, shimmer, seed, expr)
    skin, belly = DRAGONS[colour] if isinstance(colour, str) else colour
    horn = HORN.get(colour, '#efe4c9') if isinstance(colour, str) else '#efe4c9'
    pal = dict(skin=skin, belly=belly, far=dark(skin, .2), wing=light(skin, .12), wingfar=dark(skin, .12),
               horn=horn, line=INK, eye='#ffe27a', claw='#efe4c9', mouth='#7a1b2a')
    return _dragon_svg(x, y, s, pose, flip, rot, pal, expr)


def _shimmer_dragon(x, y, s, pose, flip, rot, key, seed, expr):
    sd, pid = shimmer_defs(key, seed, s=1.0 / max(s, 0.2) * 0.9)
    white = dict(skin='#ffffff', belly='#ffffff', far='#ffffff', wing='#ffffff', wingfar='#ffffff',
                 horn='#ffffff', line='#000000', eye='#ffffff', claw='#ffffff', mouth='#ffffff')
    ink = dict(skin=INK, belly=INK, far=INK, wing=INK, wingfar=INK, horn=INK, line=INK, eye=INK,
               claw=INK, mouth=INK)
    mask = _dragon_svg(x, y, s, pose, flip, rot, white, expr)
    sil = _dragon_svg(x, y, s, pose, flip, rot, ink, expr)
    mid = uid('dm')
    # the mask covers the dragon's area; the pattern fills a big rectangle under it
    o = sd + f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="-4000" y="-4000" width="9000" height="9000">'
    o += f'<rect x="-4000" y="-4000" width="9000" height="9000" fill="#000"/>{mask}</mask>'
    o += sil
    o += (f'<g mask="url(#{mid})"><rect x="{x - 400 * s}" y="{y - 400 * s}" width="{800 * s}" height="{800 * s}" '
          f'fill="url(#{pid})"/>'
          f'<rect x="{x - 400 * s}" y="{y - 400 * s}" width="{800 * s}" height="{800 * s}" fill="#ffffff" opacity=".18"/></g>')
    # the eyes, drawn on top so they read
    o += _dragon_svg(x, y, s, pose, flip, rot, None, expr, eyes_only=True)
    return o


def _head(pal, sty, expr, size=1.0):
    """Dragon head, origin at the neck joint, facing +x. About 70 long."""
    sk, horn, line = pal['skin'], pal['horn'], pal['line']
    o = ''
    # horns and frill (behind)
    o += P('M 6,-16 C -6,-34 -26,-40 -42,-30 C -28,-30 -14,-24 -2,-10 Z', horn, sty)
    o += P('M 0,-8 C -14,-14 -28,-10 -38,0 C -26,-4 -14,-2 -2,2 Z', pal['wingfar'] if pal['wingfar'] != '#ffffff' else horn, sty)
    o += P('M -4,6 L -18,14 L -4,13 Z', pal['far'], sty)
    if expr == 'talk':
        # lower jaw dropped, mouth open (talking)
        o += P('M 10,10 C 26,26 50,26 64,16 L 60,10 C 48,14 28,14 14,4 Z', sk, sty)
        o += P('M 16,4 C 30,13 48,13 62,8 L 64,2 C 48,4 30,2 18,-2 Z', pal['mouth'], sty)
    # skull + snout
    d = 'M -6,-4 C -6,-20 10,-26 26,-22 L 62,-12 C 72,-10 74,2 66,5 L 30,10 C 14,14 -4,12 -6,-4 Z'
    o += P(d, sk, sty)
    o += f'<path d="M 30,9.5 L 66,4.5 Q 52,11 30,13 Z" fill="{pal["belly"]}"/>'
    # nostril, mouth line
    o += f'<ellipse cx="64" cy="-6" rx="2.4" ry="1.4" fill="{line}"/>'
    if expr in ('happy',):
        o += f'<path d="M 66,4 Q 52,12 38,8" stroke="{line}" stroke-width="{sty["stroke"] * 1.1}" fill="none" stroke-linecap="round"/>'
    elif expr != 'talk':
        o += f'<path d="M 66,4 L 40,9" stroke="{line}" stroke-width="{sty["stroke"]}" fill="none" stroke-linecap="round"/>'
    # eye
    ey = (26, -11)
    if expr in ('closed', 'happy'):
        o += f'<path d="M {ey[0] - 6},{ey[1]} Q {ey[0]},{ey[1] - 5} {ey[0] + 6},{ey[1]}" stroke="{line}" stroke-width="{sty["stroke"] * 1.3}" fill="none" stroke-linecap="round"/>'
    else:
        rx, ry = (6.5, 5.2) if expr == 'wide' else (6, 4.4)
        o += f'<ellipse cx="{ey[0]}" cy="{ey[1]}" rx="{rx}" ry="{ry}" fill="{pal["eye"]}" stroke="{line}" stroke-width="{sty["stroke"] * 0.8}"/>'
        o += f'<ellipse cx="{ey[0] + 1}" cy="{ey[1]}" rx="1.6" ry="{ry - 0.6}" fill="{line}"/>'
        o += f'<circle cx="{ey[0] - 2}" cy="{ey[1] - 2}" r="1.3" fill="#fff"/>'
    o += f'<path d="M {ey[0] - 10},{ey[1] - 6} Q {ey[0]},{ey[1] - 11} {ey[0] + 12},{ey[1] - 6}" stroke="{dark(sk, .45) if sk.startswith("#") and sk not in ("#ffffff",) else line}" stroke-width="{sty["stroke"] * 1.4}" fill="none" stroke-linecap="round"/>'
    return f'<g transform="scale({size})">{o}</g>'


WING_SPREAD = 'M 0,0 Q -10,-60 -30,-104 Q -12,-90 -2,-86 Q 0,-110 8,-128 Q 18,-96 26,-86 Q 40,-100 62,-104 Q 46,-50 40,-4 Z'
WING_FOLDED = 'M 0,0 Q -30,-22 -64,-24 Q -50,-16 -46,-12 Q -66,-10 -84,-4 Q -56,-2 -44,2 Q -50,10 -60,18 Q -26,12 8,6 Z'
WING_UP = 'M 0,0 Q 4,-50 -6,-98 Q 6,-88 12,-84 Q 18,-104 30,-118 Q 32,-90 34,-80 Q 48,-90 66,-90 Q 46,-44 34,-2 Z'
WINGS = {'spread': WING_SPREAD, 'folded': WING_FOLDED, 'up': WING_UP}


def _dragon_svg(x, y, s, pose, flip, rot, pal, expr, eyes_only=False):
    sty = S(s * 1.0)
    spine = pose['spine']
    widths = pose['widths']
    C = catmull(spine, 260)
    u = np.linspace(0, 1, len(C))
    knots = np.linspace(0, 1, len(widths))
    w = np.interp(u, knots, widths)
    T, N = frame(C)
    # belly side: N pointing to +y on average over the torso
    if np.mean(N[len(C) // 3: 2 * len(C) // 3, 1]) < 0:
        N = -N
    ang = pose.get('head_angle', 0)
    hp = C[-1]
    head_size = pose.get('head_size', 0.85)
    if eyes_only:
        # re-create only the eye in true colours on top of a shimmer dragon
        pal2 = dict(skin='none', belly='none', far='none', wing='none', wingfar='none', horn='none',
                    line=INK, eye='#ffe27a', claw='none', mouth='none')
        ey = (26, -11)
        if expr in ('closed', 'happy'):
            e = f'<path d="M {ey[0] - 6},{ey[1]} Q {ey[0]},{ey[1] - 5} {ey[0] + 6},{ey[1]}" stroke="{INK}" stroke-width="{sty["stroke"] * 1.3}" fill="none" stroke-linecap="round"/>'
        else:
            e = (f'<ellipse cx="{ey[0]}" cy="{ey[1]}" rx="6" ry="4.4" fill="#ffe27a" stroke="{INK}" stroke-width="{sty["stroke"] * 0.8}"/>'
                 f'<ellipse cx="{ey[0] + 1}" cy="{ey[1]}" rx="1.6" ry="3.8" fill="{INK}"/>'
                 f'<circle cx="{ey[0] - 2}" cy="{ey[1] - 2}" r="1.3" fill="#fff"/>')
        g = f'<g transform="translate({hp[0]:.1f},{hp[1]:.1f}) rotate({ang}) scale({head_size})">{e}</g>'
        return f'<g transform="translate({x},{y}) rotate({rot}) scale({s * flip},{s})">{g}</g>'
    o = []
    sty_line = dict(sty, line=pal['line'])
    # anchors
    def at(f):
        i = int(np.clip(f, 0, 1) * (len(C) - 1))
        return C[i], T[i], N[i], w[i]
    wings = pose.get('wings', 'folded')
    wing_at = pose.get('wing_at', 0.6)
    wing_rot = pose.get('wing_rot', 0)
    wing_scale = pose.get('wing_scale', 1.0)
    wp, wt, wn, ww = at(wing_at)
    wang = math.degrees(math.atan2(wt[1], wt[0]))
    top = wp - wn * ww * 0.35
    if wings != 'none':
        # far wing (slightly offset, darker)
        o.append(f'<g transform="translate({top[0] + 10:.1f},{top[1] - 6:.1f}) rotate({wang + wing_rot - 8:.1f}) scale({wing_scale * 0.92})">'
                 f'{P(WINGS[wings], pal["wingfar"], sty_line)}</g>')
    # far legs
    for (f, pts, near) in pose.get('legs', []):
        if near:
            continue
        o.append(_leg(at(f), pts, pal['far'], pal, sty_line))
    # body tube
    body = tube_outline(C, w)
    o.append(P(dpath(body), pal['skin'], sty_line))
    # belly plates from hips to throat
    i0, i1 = int(pose.get('belly', (0.35, 0.92))[0] * len(C)), int(pose.get('belly', (0.35, 0.92))[1] * len(C))
    bo = C[i0:i1] + N[i0:i1] * (w[i0:i1] * 0.08)[:, None]
    bi = C[i0:i1] + N[i0:i1] * (w[i0:i1] * 0.46)[:, None]
    o.append(f'<path d="{dpath(np.vstack([bo, bi[::-1]]))}" fill="{pal["belly"]}"/>')
    for i in range(0, len(bo), 9):
        o.append(f'<path d="M {bo[i][0]:.1f},{bo[i][1]:.1f} L {bi[i][0]:.1f},{bi[i][1]:.1f}" '
                 f'stroke="{dark(pal["belly"], .3) if pal["belly"].startswith("#") and pal["belly"] not in ("#ffffff", INK) else pal["belly"]}" stroke-width="{sty["stroke"] * 0.7}"/>')
    # dorsal spikes
    for f in np.linspace(0.12, 0.86, pose.get('spikes', 14)):
        p, t, n, ww_ = at(f)
        b = p - n * ww_ * 0.48
        tip = b - n * (5 + ww_ * 0.16) - t * 5
        o.append(P(f'M {b[0] - t[0] * 4:.1f},{b[1] - t[1] * 4:.1f} L {tip[0]:.1f},{tip[1]:.1f} L {b[0] + t[0] * 4:.1f},{b[1] + t[1] * 4:.1f} Z',
                   pal['far'], sty_line))
    o.append(P(dpath(body), 'none', sty_line))
    # near legs
    for (f, pts, near) in pose.get('legs', []):
        if not near:
            continue
        o.append(_leg(at(f), pts, pal['skin'], pal, sty_line))
    # near wing
    if wings != 'none':
        o.append(f'<g transform="translate({top[0]:.1f},{top[1]:.1f}) rotate({wang + wing_rot:.1f}) scale({wing_scale})">'
                 f'{P(WINGS[wings], pal["wing"], sty_line)}</g>')
    # head
    o.append(f'<g transform="translate({hp[0]:.1f},{hp[1]:.1f}) rotate({ang})">{_head(pal, sty_line, expr, head_size)}</g>')
    g = ''.join(o)
    return f'<g transform="translate({x},{y}) rotate({rot}) scale({s * flip},{s})">{g}</g>'


def _leg(anchor, pts, fill, pal, sty):
    p, t, n, w = anchor
    base = p + n * w * 0.15
    pts = [tuple(base)] + [(base[0] + a, base[1] + b) for a, b in pts]
    o = limb(pts, max(w * 0.32, 7), fill, sty)
    foot = pts[-1]
    prev = pts[-2]
    d = np.array(foot) - np.array(prev)
    d /= (np.linalg.norm(d) + 1e-9)
    for a in (-0.7, 0, 0.7):
        c, s_ = math.cos(a), math.sin(a)
        dv = (d[0] * c - d[1] * s_, d[0] * s_ + d[1] * c)
        o += limb([foot, (foot[0] + dv[0] * 7, foot[1] + dv[1] * 7)], 2.4, pal['claw'], sty)
    return o


# ---------------------------------------------------------------- dragonborn in everyday poses
def megaphone_bell(x, y, s, drag, look=0, flip=1):
    """Where a standing figure's speaking horn opens, in the picture (to hang a speech scroll on)."""
    s = s * SIZE_K.get(drag, 1.0)
    sy = -46 - 34 * 1.08
    hc = (10, sy - 9 - 10 * 1.05)
    bx, by = _rot((72, 6), math.radians(look))
    return (x + (hc[0] + bx) * s * flip, y + (hc[1] + by) * s)


def fly_hand(x, y, s, drag, flip=1):
    """Where a flying figure's raised front hand ends up in the picture (for streamers and the like)."""
    s = s * SIZE_K.get(drag, 1.0)
    hipY = -46
    sy = hipY - 34 * 1.08
    hx, hy = _rot((-16, sy - 32 - hipY), math.radians(62))
    return (x + hx * s * flip, y + hy * s)


def person(x, y, s, drag, pose='stand', outfit='#6f7b8a', accent='#9b2d2d', flip=1, item=None,
           look=0, robe=False, kneel=False, child=False, tail_item='auto', wings=None):
    """A dragonborn in an everyday pose. Feet at (0,0), about 115 tall at scale 1.

    pose: 'stand', 'point' (front arm up and out), 'awe' (hands to cheeks), 'raise' (both arms up),
    'pray' (hands together), 'offer' (both arms forward), 'read' (holding item in front), 'wave',
    'rest' (hands at sides), 'hold' (front hand up holding item), 'fly' (body level, arms ahead;
    (x, y) is then the hip). item: None, 'scroll', 'book', 'staff', 'banner:<colour>', 'lantern',
    'tape', 'tablet', 'brush'. look: head tilt in degrees (negative looks up). kneel: kneeling.
    child: smaller, rounder. tail_item: what a Green's prehensile tail holds ('auto' picks one).
    wings: 'spectral' for a White in flight. Red is drawn a touch larger and Blue a touch smaller;
    Blue and Indigo have webbed fingers and toes where the figure is big enough to show them.
    """
    s = s * SIZE_K.get(drag, 1.0)
    detail = s >= 0.68 and not child or s >= 0.5 and child
    sty = S(s, 3.6)
    skin, belly = DRAGONS[drag]
    horn = HORN.get(drag, '#efe4c9')
    far = dark(skin, .18)
    webbed = drag in WEBBED
    fly = pose == 'fly'
    L, Tt, Hs = 1.0, 1.08, 1.05
    if child:
        L, Tt, Hs = 0.7, 0.8, 1.25
    hipY = -46 * L if not kneel else -30
    sy = hipY - 34 * Tt
    sw = 15 * Tt + 2
    hw = 11 * Tt + 1
    o = [] if fly else [f'<ellipse cx="0" cy="0" rx="{30 * max(Tt, 0.8)}" ry="5" fill="#000" opacity=".2"/>']
    # tail
    if drag == 'Green' and not fly:
        if tail_item == 'auto':
            tail_item = random.Random(int(x * 7 + y * 13)).choice(TAIL_ITEMS[:6] + (None,))
        o.append(_green_tail(hipY, sy, far, skin, sty, tail_item))
    elif fly:
        o.append(P(f'M -4,{hipY - 2} C -14,{hipY + 14} -10,{-8} -26,{24} C -6,{2} -4,{hipY + 16} 4,{hipY + 8} Z', far, sty))
    else:
        o.append(P(f'M -4,{hipY - 2} C -20,{hipY + 2} -36,-20 -62,-4 C -36,-12 -20,{hipY + 16} -2,{hipY + 12} Z', far, sty))
    fs, bs = (6, sy + 5), (-6, sy + 5)
    hands = {
        'stand': ((16, hipY - 2), (-12, hipY)),
        'rest': ((12, hipY + 4), (-10, hipY + 4)),
        'point': ((34, sy - 26), (-12, hipY)),
        'awe': ((16, sy - 12), (2, sy - 10)),
        'raise': ((22, sy - 34), (-14, sy - 32)),
        'pray': ((16, sy + 6), (14, sy + 8)),
        'offer': ((30, sy + 8), (24, sy + 10)),
        'read': ((22, sy + 14), (14, sy + 16)),
        'wave': ((26, sy - 30), (-12, hipY)),
        'hold': ((24, sy - 8), (-12, hipY)),
        'fly': ((-16, sy - 32), (-8, hipY + 10)),
    }
    fh, bh = hands[pose]

    def elbow(sh, h):
        el = ((sh[0] + h[0]) / 2 - 2, (sh[1] + h[1]) / 2 + 6)
        if h[1] < sh[1] - 10:
            el = ((sh[0] + h[0]) / 2 + 6, (sh[1] + h[1]) / 2 + 2)
        return el

    def arm(sh, h, c):
        return limb([sh, elbow(sh, h), h], 7, c, sty)

    o.append(arm(bs, bh, far))
    o.append(_hand(bh, elbow(bs, bh), far, webbed, sty, detail))
    # legs
    if kneel:
        o.append(limb([(-4, hipY + 4), (-2, -4), (-24, -2)], 9, far, sty))
        o.append(limb([(5, hipY + 4), (16, hipY + 10), (14, -2)], 9, skin, sty))
        o.append(_foot(19, skin, webbed, sty, detail))
    elif fly:
        o.append(limb([(-5, hipY + 4), (-2, hipY * 0.45), (-8, -6)], 9, far, sty))
        o.append(f'<g transform="translate(-8,-6) rotate(70)">{_foot(4, far, webbed, sty, detail)}</g>')
        o.append(limb([(5, hipY + 4), (12, hipY * 0.5), (4, -12)], 9, skin, sty))
        o.append(f'<g transform="translate(4,-12) rotate(60)">{_foot(4, skin, webbed, sty, detail)}</g>')
    else:
        o.append(limb([(-5, hipY + 4), (1, hipY * 0.5), (-8, -7 * L), (-2, -1)], 9, far, sty))
        o.append(_foot(0, far, webbed, sty, detail))
        o.append(limb([(5, hipY + 4), (12, hipY * 0.5), (5, -7 * L), (9, -1)], 9, skin, sty))
        o.append(_foot(13, skin, webbed, sty, detail))
    if robe:
        bottom = -3 if not kneel else -4
        d = (f'M {-hw - 1},{hipY - 2} L {hw + 1},{hipY - 2} L {hw + 9},{bottom} Q 0,{bottom + 4} {-hw - 9},{bottom} Z')
        o.append(P(d, outfit, sty))
        o.append(f'<path d="M {-hw - 9},{bottom - 1} L {hw + 9},{bottom - 1}" stroke="{accent}" stroke-width="2.5"/>')
    d = (f'M {-sw},{sy + 4} Q {-sw},{sy - 2} {-sw + 6},{sy - 3} L {sw - 6},{sy - 3} Q {sw},{sy - 2} {sw},{sy + 4} '
         f'L {hw + 1},{hipY + 2} Q 0,{hipY + 7} {-hw - 1},{hipY + 2} Z')
    o.append(P(d, outfit, sty))
    o.append(f'<path d="M -3,{sy - 2} L 3,{hipY}" stroke="{accent}" stroke-width="3"/>')
    o.append(f'<rect x="{-hw - 1}" y="{hipY - 3}" width="{2 * hw + 2}" height="4" fill="{party.LEATHER}"/>')
    if detail:   # costume details: hem trim, collar, buckle and a belt pouch
        o.append(f'<path d="M {-hw},{hipY + 1} Q 0,{hipY + 5.5} {hw},{hipY + 1}" stroke="{accent}" stroke-width="1.8" fill="none" opacity=".8"/>')
        o.append(f'<path d="M {-sw + 5},{sy - 2} L 0,{sy + 7} L {sw - 5},{sy - 2}" stroke="{mix(outfit, "#ffffff", .45)}" stroke-width="2.2" fill="none"/>')
        o.append(f'<rect x="-3" y="{hipY - 4}" width="6" height="6" rx="1" fill="#e8c35a" stroke="{INK}" stroke-width="1"/>')
        o.append(P(f'M {-hw + 1},{hipY - 1} L {-hw + 8},{hipY - 1} L {-hw + 8},{hipY + 7} Q {-hw + 4.5},{hipY + 10} {-hw + 1},{hipY + 7} Z', party.LEATHER, dict(sty, stroke=sty['stroke'] * 0.6)))
    hc = (10, sy - 9 - 10 * Hs)
    o.append(limb([(2, sy + 3), (6, sy - 4), (hc[0] - 1, hc[1] + 5)], 10, skin, sty))
    o.append(limb([(6, sy + 1), (9, sy - 4), (hc[0] + 3, hc[1] + 8)], 3.5, belly, dict(sty, stroke=0)))
    hl = look - 54 if fly else look
    o.append(f'<g transform="translate({hc[0]},{hc[1]}) rotate({hl}) scale({Hs},{Hs})">{head_svg(drag, sty, skin, belly, horn)}</g>')
    # held item (front hand)
    if item == 'scroll':
        o.append(f'<g transform="translate({fh[0]},{fh[1]}) rotate(-20)">'
                 + P('M -4,-14 L 4,-14 L 4,14 L -4,14 Z', '#f4ead2', sty)
                 + circ(0, -14, 4, '#d8c9a3', sty) + circ(0, 14, 4, '#d8c9a3', sty) + '</g>')
    elif item == 'book':
        o.append(f'<g transform="translate({fh[0] - 4},{fh[1] - 6}) rotate(-10)">'
                 + P('M -12,-8 L 0,-6 L 0,10 L -12,8 Z', '#f4ead2', sty)
                 + P('M 0,-6 L 12,-8 L 12,8 L 0,10 Z', '#efe3c4', sty)
                 + P('M -13,9 L 0,11 L 13,9 L 13,11 L 0,13 L -13,11 Z', '#7a2f3a', sty) + '</g>')
    elif item == 'tablet':
        o.append(f'<g transform="translate({fh[0] - 2},{fh[1] - 4}) rotate(-8)">'
                 + P('M -11,-14 L 11,-14 L 11,12 L -11,12 Z', '#c9a77a', sty)
                 + ''.join(f'<path d="M -7,{-9 + k * 5} L {3 + (k % 2) * 4},{-9 + k * 5}" stroke="#7a5233" stroke-width="2"/>' for k in range(4)) + '</g>')
    elif item == 'brush':
        o.append(limb([(fh[0] - 6, fh[1] + 8), (fh[0] + 10, fh[1] - 12)], 2.4, '#7a5233', sty))
        o.append(P(f'M {fh[0] + 9},{fh[1] - 11} L {fh[0] + 14},{fh[1] - 18} L {fh[0] + 13},{fh[1] - 10} Z', '#4fc1b3', sty))
    elif item == 'staff':
        o.append(limb([(fh[0], -1), (fh[0] + 2, sy - 40)], 3, party.WOOD, sty))
    elif item and item.startswith('banner:'):
        c = item.split(':')[1]
        top = (fh[0] + 1, sy - 70)
        o.append(limb([(fh[0], fh[1] + 20), top], 3, party.WOOD, sty))
        o.append(P(f'M {top[0]},{top[1] + 2} L {top[0] + 34},{top[1] + 8} Q {top[0] + 26},{top[1] + 20} {top[0] + 36},{top[1] + 32} '
                   f'L {top[0]},{top[1] + 30} Z', c, sty))
    elif item == 'lantern':
        o.append(glow(fh[0], fh[1] + 12, 26, '#ffd27a'))
        o.append(limb([fh, (fh[0], fh[1] + 6)], 1.4, INK, sty))
        o.append(P(f'M {fh[0] - 5},{fh[1] + 6} L {fh[0] + 5},{fh[1] + 6} L {fh[0] + 6},{fh[1] + 18} L {fh[0] - 6},{fh[1] + 18} Z', '#ffe9a8', sty))
    elif item == 'drum':
        o.append(f'<path d="M -10,{sy + 2} L 16,{hipY - 8}" stroke="{party.LEATHER}" stroke-width="2.4"/>')
        o.append(P(f'M 4,{hipY - 16} L 26,{hipY - 16} L 24,{hipY + 4} L 6,{hipY + 4} Z', '#c46b4a', sty))
        o.append(f'<ellipse cx="15" cy="{hipY - 16}" rx="11" ry="3.6" fill="#f3ead2" stroke="{INK}" stroke-width="{sty["stroke"]:.2f}"/>')
        o.append(f'<path d="M 6,{hipY - 12} L 15,{hipY} L 24,{hipY - 12}" stroke="#f3ead2" stroke-width="1.6" fill="none"/>')
        o.append(f'<path d="M {fh[0] + 6},{fh[1] - 12} q 3,-3 6,0 M {fh[0] + 10},{fh[1] - 18} q 3,-3 6,0" stroke="{INK}" stroke-width="1.6" fill="none"/>')
    elif item == 'horn':
        mx, my = hc[0] + 14, hc[1] + 6
        o.append(P(f'M {mx},{my - 2} Q {mx + 24},{my - 8} {mx + 40},{my - 26} L {mx + 50},{my - 18} Q {mx + 30},{my + 4} {mx},{my + 3} Z', '#e8c35a', sty))
        o.append(f'<ellipse cx="{mx + 45}" cy="{my - 22}" rx="7" ry="4" transform="rotate(38 {mx + 45} {my - 22})" fill="#9a7428" stroke="{INK}" stroke-width="{sty["stroke"]:.2f}"/>')
        o.append(f'<path d="M {mx + 54},{my - 34} q 6,-2 8,4 M {mx + 58},{my - 26} q 6,-2 8,4" stroke="{INK}" stroke-width="1.8" fill="none"/>')
    elif item == 'megaphone':
        o.append(f'<g transform="translate({hc[0]},{hc[1]}) rotate({hl})">'
                 + P('M 34,4 L 66,-10 L 68,22 L 34,10 Z', '#d4a63c', sty)
                 + f'<ellipse cx="67" cy="6" rx="5" ry="16" fill="#9a7428" stroke="{INK}" stroke-width="{sty["stroke"]:.2f}"/>'
                 + P('M 30,3 L 36,3 L 36,11 L 30,11 Z', '#9a7428', sty) + '</g>')
    elif item == 'tape':
        o.append(limb([fh, (fh[0] + 8, fh[1] + 10), (fh[0] + 2, fh[1] + 26), (fh[0] + 10, fh[1] + 40)], 5, '#f4ead2', sty))
    o.append(arm(fs, fh, skin))
    o.append(_hand(fh, elbow(fs, fh), skin, webbed, sty, detail))
    g = ''.join(o)
    if fly:
        # level the body out, then add the wings of light at the shoulder (outside the rotation)
        ang = 62
        shx, shy = _rot((-6, sy + 8 - hipY), math.radians(ang))
        body = f'<g transform="rotate({ang} 0 {hipY})">{g}</g>'
        wl = ''
        if wings == 'spectral':
            wl = spectral_wings((shx, shy + hipY), s=1.05, spread=1.0, seed=int(x + y))
        return f'<g transform="translate({x},{y - hipY * s}) scale({s * flip},{s})">{wl}{body}</g>'
    return f'<g transform="translate({x},{y}) scale({s * flip},{s})">{g}</g>'


# ---------------------------------------------------------------- scenery
FARSIDE_UF = 0.18      # the arch's feet in the normalized band grid (worldgen/farside.py)


def _band_xy(u, v, hz, top_side, top_mid, foot_in, arch_mid, W=1200):
    """Map the normalized band grid (u across, v from the top edge to the underside) to the picture."""
    L, R = -80, W + 80
    uf = FARSIDE_UF
    x = np.interp(u, [0, uf, 0.5, 1 - uf, 1], [L, foot_in, W / 2, W - foot_in, R])
    tt = (x - L) / (R - L)
    ytop = hz - top_side - 4 * tt * (1 - tt) * (top_mid - top_side)
    sa = (x - foot_in) / (W - 2 * foot_in)
    ybot = np.where((sa > 0) & (sa < 1), hz - 4 * sa * (1 - sa) * arch_mid, hz)
    return x, ytop + v * (ybot - ytop)


def _farside_layers(view, xy, night):
    """Real coastlines, highlands, snow and clouds on the far side, from worldgen/farside.py.
    xy(u, v) maps the normalized band grid to the picture."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from scipy.ndimage import gaussian_filter
    d = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', f'farside_t{view}.npz'))
    E, C = d['E'].astype(float), d['C'].astype(float)
    nv, nu = E.shape
    U, V = np.meshgrid(np.linspace(0, 1, nu), np.linspace(0, 1, nv))
    E = gaussian_filter(E, (1.6, 1.2), mode='nearest')
    C = gaussian_filter(C, (2.0, 2.4), mode='nearest')
    fig, ax = plt.subplots()

    def shapes(Z, lo, fill, stroke=None, sw=1.6, opacity=1.0, min_area=40):
        cs = ax.contourf(U, V, Z, levels=[lo, 1e9])
        out = ''
        for path in cs.get_paths():
            dd = ''
            for ring in path.to_polygons():
                if len(ring) < 4:
                    continue
                x, y = xy(ring[:, 0], ring[:, 1])
                area = 0.5 * abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
                if area < min_area:
                    continue
                dd += 'M ' + ' L '.join(f'{a:.1f},{b:.1f}' for a, b in zip(x, y)) + ' Z '
            if dd:
                stk = f'stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"' if stroke else 'stroke="none"'
                out += f'<path d="{dd}" fill="{fill}" fill-rule="evenodd" {stk} opacity="{opacity}"/>'
        return out
    if night:
        pal = dict(shallow='#4a6c98', land='#3d5a46', high='#5d5a52', snow='#c9d2e6', cloud='#8fa0c4')
    else:
        pal = dict(shallow='#a3cde6', land='#7fa35a', high='#a58a64', snow='#ffffff', cloud='#ffffff')
    o = shapes(E, -0.14, pal['shallow'], opacity=0.75, min_area=60)
    o += shapes(E, 0.0, pal['land'], INK, 1.6, min_area=30)
    o += shapes(E, 0.7, pal['high'], INK, 1.1, min_area=12)
    o += shapes(E, 1.25, pal['snow'], INK, 0.9, min_area=6)
    o += shapes(C, 0.62, pal['cloud'], None, opacity=0.8, min_area=50)
    plt.close(fig)
    return o


def ring_band(hz, top_side=300, top_mid=380, foot_in=130, arch_mid=250, sky_under='#bcd8ef', seed=3,
              night=False, op=1.0, W=1200, view=None):
    """The far side of the ring across the sky, shaped after worldgen/skyview.py (flank, leaning inner).

    hz: horizon y. The band's top edge sits top_side above the horizon at the sides and top_mid in
    the middle; its underside is an arch from (foot_in, hz) up to arch_mid above the horizon.
    view: the viewer's ringwise angle in degrees. When given, the far side shows the map's real
    coastlines, highlands and clouds (art/cartoon/data/farside_t<view>.npz, from worldgen/farside.py).
    """
    rnd = random.Random(seed)
    L, R = -80, W + 80
    cx = W / 2
    top = (f'M {L},{hz} L {L},{hz - top_side} Q {cx},{hz - top_mid * 2 + top_side} {R},{hz - top_side} L {R},{hz} '
           f'L {W - foot_in},{hz} Q {cx},{hz - arch_mid * 2} {foot_in},{hz} Z')
    cid = uid('band')
    sea = '#5e8fb8' if not night else '#2d4466'
    sea2 = '#86b4cf' if not night else '#3f5c84'
    land = '#7fa35a' if not night else '#3d5a46'
    o = f'<clipPath id="{cid}"><path d="{top}"/></clipPath><g opacity="{op}">'
    gid = uid('bg')
    o += (f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sea2}"/>'
          f'<stop offset="1" stop-color="{sea}"/></linearGradient>')
    o += P(top, f'url(#{gid})', st, bg=True)
    o += f'<g clip-path="url(#{cid})">'
    # latitude lines following the band, for curvature
    for k in range(1, 5):
        f = k / 5
        a = hz - top_side * (1 - f) - 0
        d = f'M {L},{a + f * 40} Q {cx},{hz - (top_mid * 2 - top_side) * (1 - f) - arch_mid * 2 * f + f * 40} {R},{a + f * 40}'
        o += f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="1.5" opacity=".18"/>'
    if view is not None:
        o += _farside_layers(view, lambda u, v: _band_xy(u, v, hz, top_side, top_mid, foot_in, arch_mid, W), night)
    # land patches (continents seen from afar): blobs squashed along the band (old, without a view)
    for _ in range(16 if view is None else 0):
        xx = rnd.uniform(L, R)
        t = (xx - cx) / (R - cx)
        ytop = hz - top_side - (top_mid - top_side) * (1 - t * t)
        yarch = hz - arch_mid * (1 - t * t)
        yy = rnd.uniform(ytop + 10, max(ytop + 20, yarch - 10)) if abs(t) < 0.75 else rnd.uniform(ytop + 10, hz - 20)
        rw, rh = rnd.uniform(30, 90), rnd.uniform(8, 22)
        o += f'<ellipse cx="{xx:.0f}" cy="{yy:.0f}" rx="{rw:.0f}" ry="{rh:.0f}" fill="{land}" stroke="{INK}" stroke-width="1.6" opacity=".95"/>'
        o += f'<ellipse cx="{xx + rw * 0.2:.0f}" cy="{yy + rh * 0.2:.0f}" rx="{rw * 0.45:.0f}" ry="{rh * 0.4:.0f}" fill="{dark(land, .2)}" opacity=".7"/>'
    # clouds over the far side (old, without a view)
    for _ in range(26 if view is None else 0):
        xx = rnd.uniform(L, R)
        t = (xx - cx) / (R - cx)
        ytop = hz - top_side - (top_mid - top_side) * (1 - t * t)
        yy = rnd.uniform(ytop + 8, hz - 10)
        r = rnd.uniform(6, 16)
        cc = '#ffffff' if not night else '#8fa0c4'
        o += f'<ellipse cx="{xx:.0f}" cy="{yy:.0f}" rx="{r * 2.4:.0f}" ry="{r * 0.6:.0f}" fill="{cc}" opacity=".85"/>'
    # haze: strongest in the middle, the farthest part
    hid = uid('hz')
    o += (f'<radialGradient id="{hid}" cx="50%" cy="20%" r="60%"><stop offset="0" stop-color="{"#e4eef8" if not night else "#2a3352"}" stop-opacity=".55"/>'
          f'<stop offset="1" stop-color="{"#e4eef8" if not night else "#2a3352"}" stop-opacity="0"/></radialGradient>'
          f'<rect x="{L}" y="{hz - top_mid - 40}" width="{R - L}" height="{top_mid + 40}" fill="url(#{hid})"/>')
    o += '</g>'
    o += P(top, 'none', st, bg=True)
    o += '</g>'
    return o


def farside_ribbon(p0, c, p1, w, view, night=False, op=1.0, sty=None):
    """The ring arch as a ribbon along the quadratic curve p0 -> c -> p1 (w wide), showing the
    real far side of the map (the Inner Sea scene's style of arch)."""
    sty = sty or st
    P0, C_, P1 = (np.array(q, float) for q in (p0, c, p1))

    def xy(u, v):
        u = np.asarray(u)[:, None]
        B = (1 - u) ** 2 * P0 + 2 * u * (1 - u) * C_ + u ** 2 * P1
        T = 2 * (1 - u) * (C_ - P0) + 2 * u * (P1 - C_)
        N = np.stack([T[:, 1], -T[:, 0]], 1) / np.linalg.norm(T, axis=1)[:, None]
        Q = B + N * ((0.5 - np.asarray(v))[:, None] * w)
        return Q[:, 0], Q[:, 1]
    d = f'M {p0[0]},{p0[1]} Q {c[0]},{c[1]} {p1[0]},{p1[1]}'
    sea = '#5e8fb8' if not night else '#3f5c84'
    o = f'<g opacity="{op}">'
    o += f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w + 2 * sty["bgline"]}"/>'
    o += f'<path d="{d}" fill="none" stroke="{sea}" stroke-width="{w}"/>'
    o += _farside_layers(view, xy, night)
    o += f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="{w * 0.08:.1f}" opacity=".25" transform="translate(0,{-w * 0.36:.1f})"/>'
    return o + '</g>'


def gradient_rect(x, y, w, h, stops, vertical=True):
    gid = uid('gr')
    s_ = ''.join(f'<stop offset="{k / (len(stops) - 1):.2f}" stop-color="{c}"/>' for k, c in enumerate(stops))
    xy = 'x1="0" y1="0" x2="0" y2="1"' if vertical else 'x1="0" y1="0" x2="1" y2="0"'
    return f'<linearGradient id="{gid}" {xy}>{s_}</linearGradient><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{gid})"/>'


def stars(n, seed, W=1200, H=800, ymax=None, twinkles=0):
    rnd = random.Random(seed)
    o = ''
    for _ in range(n):
        x, y = rnd.uniform(0, W), rnd.uniform(0, ymax or H)
        o += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.uniform(.6, 2.0):.1f}" fill="#fff" opacity="{rnd.uniform(.35, .95):.2f}"/>'
    for _ in range(twinkles):
        x, y, r = rnd.uniform(0, W), rnd.uniform(0, ymax or H), rnd.uniform(5, 10)
        o += (f'<path d="M {x},{y - r} L {x + r * .22},{y} L {x},{y + r} L {x - r * .22},{y} Z '
              f'M {x - r},{y} L {x},{y + r * .22} L {x + r},{y} L {x},{y - r * .22} Z" fill="#fff8dc"/>')
    return o


def banner(x, y, h, w, colour, trim, phase=0.0, emblem='', sty=None):
    """A long flowing banner hanging from a pole top at (x, y), rippling in the wind."""
    sty = sty or st
    pts_l, pts_r = [], []
    for k in range(9):
        t = k / 8
        dx = math.sin(t * 3.4 + phase) * 10 * t + t * 26
        pts_l.append((x + dx, y + t * h))
        pts_r.append((x + dx + w * (1 - 0.15 * t), y + t * h + math.sin(t * 3 + phase + 1) * 4))
    tail = (x + 26 + w * 0.42, y + h + 26)
    poly_ = pts_l + [tail] + pts_r[::-1]
    d = 'M ' + ' L '.join(f'{a:.1f},{b:.1f}' for a, b in poly_) + ' Z'
    o = P(d, colour, sty)
    o += f'<path d="M {pts_l[0][0] + 5:.1f},{pts_l[0][1]:.1f} ' + ' '.join(f'L {a + 5:.1f},{b:.1f}' for a, b in pts_l[1:7]) + f'" stroke="{trim}" stroke-width="4" fill="none"/>'
    if emblem:
        ex, ey = pts_l[3][0] + w * 0.5, pts_l[3][1]
        o += f'<g transform="translate({ex:.1f},{ey:.1f})">{emblem}</g>'
    return o


CAPTION_SIZE = 34
_CAPTION_FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'


def caption_lines(text, avail):
    """Split a caption into one line, or two at the punctuation nearest the middle, to fit avail px."""
    from PIL import ImageFont
    f = ImageFont.truetype(_CAPTION_FONT, CAPTION_SIZE)

    def width(t):
        return f.getlength(t) + len(t) * 1.0
    if width(text) <= avail:
        return [text]
    cuts = [i + 1 for i, ch in enumerate(text) if ch in ',:;' and i < len(text) - 2] or \
           [i for i, ch in enumerate(text) if ch == ' ']
    i = min(cuts, key=lambda c: abs(c - len(text) / 2))
    return [text[:i].strip(), text[i:].strip()]


def woven_frame(scene_svg, caption, label, W=1640, H=1340, wall='#cfc6b4', border='#3c4f7a',
                accent='#e8c35a', cloth='#f3ecdc'):
    """Hang a 1200x800 scene as a tapestry: rod, border, woven caption, fringe, stone wall."""
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    # monastery wall: pale stone blocks
    o.append(f'<rect width="{W}" height="{H}" fill="{wall}"/>')
    rnd = random.Random(7)
    for row in range(0, H, 90):
        off = 0 if (row // 90) % 2 else 110
        for col_ in range(-off, W, 220):
            sh = rnd.uniform(-0.04, 0.04)
            o.append(f'<rect x="{col_ + 3}" y="{row + 3}" width="214" height="84" rx="6" fill="{mix(wall, "#ffffff" if sh > 0 else "#8d8370", abs(sh) * 4)}" '
                     f'stroke="#a99f8b" stroke-width="2"/>')
    o.append(f'<rect width="{W}" height="{H}" fill="#000" opacity=".06"/>')
    cx0, cy0, cw, chh = 60, 70, W - 120, H - 160
    # shadow
    o.append(f'<rect x="{cx0 + 14}" y="{cy0 + 18}" width="{cw}" height="{chh}" fill="#000" opacity=".25"/>')
    # cloth with border
    o.append(f'<rect x="{cx0}" y="{cy0}" width="{cw}" height="{chh}" fill="{border}" stroke="{INK}" stroke-width="4"/>')
    # border motif: small rings (ouroboros knots) and diamonds
    for xx in range(cx0 + 40, cx0 + cw - 20, 64):
        for yy in (cy0 + 22, cy0 + chh - 22):
            o.append(f'<circle cx="{xx}" cy="{yy}" r="9" fill="none" stroke="{accent}" stroke-width="3.5"/>'
                     f'<circle cx="{xx + 7}" cy="{yy - 6}" r="2.6" fill="{accent}"/>')
            o.append(f'<path d="M {xx + 32},{yy - 6} L {xx + 38},{yy} L {xx + 32},{yy + 6} L {xx + 26},{yy} Z" fill="#f3ecdc"/>')
    for yy in range(cy0 + 70, cy0 + chh - 40, 64):
        for xx in (cx0 + 22, cx0 + cw - 22):
            o.append(f'<circle cx="{xx}" cy="{yy}" r="9" fill="none" stroke="{accent}" stroke-width="3.5"/>'
                     f'<circle cx="{xx + 7}" cy="{yy - 6}" r="2.6" fill="{accent}"/>')
            if yy + 32 < cy0 + chh - 40:
                o.append(f'<path d="M {xx - 6},{yy + 32} L {xx},{yy + 26} L {xx + 6},{yy + 32} L {xx},{yy + 38} Z" fill="#f3ecdc"/>')
    # inner field
    fx, fy, fw, fh = cx0 + 46, cy0 + 46, cw - 92, chh - 92
    o.append(f'<rect x="{fx - 4}" y="{fy - 4}" width="{fw + 8}" height="{fh + 8}" fill="{accent}"/>')
    o.append(f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" fill="{cloth}"/>')
    # scene window (3:2) and caption panel
    sw_ = fw - 24
    sh_ = sw_ * 2 / 3
    sx, sy_ = fx + 12, fy + 12
    o.append(f'<svg x="{sx}" y="{sy_}" width="{sw_}" height="{sh_}" viewBox="0 0 1200 800" preserveAspectRatio="xMidYMid slice">{scene_svg}</svg>')
    o.append(f'<rect x="{sx}" y="{sy_}" width="{sw_}" height="{sh_}" fill="none" stroke="{INK}" stroke-width="5"/>')
    capy = sy_ + sh_ + 14
    caph = fy + fh - capy - 12
    o.append(f'<rect x="{sx}" y="{capy}" width="{sw_}" height="{caph}" fill="{cloth}" stroke="{INK}" stroke-width="3"/>')
    # woven caption: one size on every tapestry; a long one breaks at its comma or colon
    lines = caption_lines(caption, sw_ - 2 * 104)
    lh = CAPTION_SIZE * 1.22
    y0 = capy + caph / 2 - (len(lines) - 1) * lh / 2 + CAPTION_SIZE * 0.35
    for k, ln in enumerate(lines):
        o.append(f'<text x="{sx + sw_ / 2}" y="{y0 + k * lh:.1f}" text-anchor="middle" font-family="DejaVu Serif" '
                 f'font-weight="bold" font-size="{CAPTION_SIZE}" fill="{INK}" letter-spacing="1">{ln}</text>')
    # epoch medallions at both ends of the caption
    for mx in (sx + 54, sx + sw_ - 54):
        my = capy + caph / 2
        o.append(f'<circle cx="{mx}" cy="{my}" r="30" fill="{border}" stroke="{INK}" stroke-width="3"/>'
                 f'<circle cx="{mx}" cy="{my}" r="24" fill="none" stroke="{accent}" stroke-width="2.5"/>'
                 f'<text x="{mx}" y="{my + 11}" text-anchor="middle" font-family="DejaVu Serif" font-weight="bold" '
                 f'font-size="30" fill="{accent}">{label}</text>')
    # weave texture over the cloth
    pid = uid('weave')
    o.append(f'<pattern id="{pid}" width="6" height="6" patternUnits="userSpaceOnUse">'
             f'<rect width="6" height="3" fill="#000" opacity=".05"/><rect x="0" y="0" width="3" height="6" fill="#fff" opacity=".05"/></pattern>'
             f'<rect x="{cx0}" y="{cy0}" width="{cw}" height="{chh}" fill="url(#{pid})"/>')
    # gentle cloth folds
    for k in range(1, 6):
        xx = cx0 + cw * k / 6
        o.append(f'<rect x="{xx - 30}" y="{cy0}" width="60" height="{chh}" fill="#000" opacity=".025"/>')
    # rod and finials, hanging cords
    o.append(f'<path d="M {cx0 + 120},{cy0 - 2} L {W / 2},{18} L {cx0 + cw - 120},{cy0 - 2}" fill="none" stroke="#6b4a2f" stroke-width="5"/>')
    o.append(f'<rect x="{cx0 - 26}" y="{cy0 - 18}" width="{cw + 52}" height="22" rx="11" fill="#7a5233" stroke="{INK}" stroke-width="4"/>')
    for ex in (cx0 - 30, cx0 + cw + 30):
        o.append(f'<circle cx="{ex}" cy="{cy0 - 7}" r="17" fill="{accent}" stroke="{INK}" stroke-width="4"/>')
    o.append(f'<circle cx="{W / 2}" cy="18" r="10" fill="#7a5233" stroke="{INK}" stroke-width="3"/>')
    # fringe
    for xx in range(cx0 + 8, cx0 + cw - 4, 16):
        ln = 34 + 6 * math.sin(xx * 0.3)
        o.append(f'<path d="M {xx},{cy0 + chh} L {xx + 2},{cy0 + chh + ln}" stroke="{border}" stroke-width="7" stroke-linecap="round"/>'
                 f'<path d="M {xx},{cy0 + chh} L {xx + 2},{cy0 + chh + ln}" stroke="{accent}" stroke-width="2" opacity=".6"/>')
    o.append('</svg>')
    return ''.join(o)
