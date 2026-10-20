"""Handout cover: colossal Azhi looming over the young spherical world (Saturday-Morning Bold) -> output/azhi_cover.png."""
import os
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
os.makedirs('build', exist_ok=True); os.makedirs('output', exist_ok=True)
import math, random, sys
import numpy as np
sys.path.insert(0, HERE)
from party import STYLES, P, limb, glow, circ, mix, dark, light

st = STYLES['bold']
SHOW_GIFTS = False   # streams of water/lava/frost/leaves from the young dragons; the user rejected these (2026-10-20)
INK = '#18120e'
W, H = 1600, 1000
rnd = random.Random(21)

# ---------- helpers ----------
def catmull(pts, n=900):
    pts = np.array(pts, float)
    P_ = np.vstack([pts[0]*2-pts[1], pts, pts[-1]*2-pts[-2]])
    seg = len(pts)-1; out = []
    for i in range(seg):
        p0, p1, p2, p3 = P_[i], P_[i+1], P_[i+2], P_[i+3]
        for t in np.linspace(0, 1, n//seg, endpoint=False):
            t2, t3 = t*t, t*t*t
            out.append(0.5*((2*p1)+(-p0+p2)*t+(2*p0-5*p1+4*p2-p3)*t2+(-p0+3*p1-3*p2+p3)*t3))
    out.append(pts[-1]); return np.array(out)

def dpath(arr, close=True):
    s = 'M ' + ' L '.join(f'{x:.1f},{y:.1f}' for x, y in arr)
    return s + (' Z' if close else '')

def blob(cx, cy, r, k, seed, rough=0.35):
    g = random.Random(seed)
    pts = [(cx + r*(1+g.uniform(-rough, rough))*math.cos(a), cy + r*(1+g.uniform(-rough, rough))*math.sin(a)*0.8)
           for a in np.linspace(0, 2*math.pi, k, endpoint=False)]
    c = catmull(pts + pts[:3], 200)[int(200/(k+2)):int(200*(k+1)/(k+2))]
    return dpath(c)

def young_dragon(cx, cy, s, colr, flip=1, extra=''):
    c = colr
    fw = 'M 0,-4 Q -6,-50 -14,-74 Q -2,-62 4,-58 Q 8,-74 14,-86 Q 18,-66 24,-58 Q 34,-68 48,-72 Q 36,-36 30,-6 Z'
    nw = 'M 4,-2 Q -18,-36 -36,-62 Q -20,-54 -10,-52 Q -12,-66 -8,-78 Q 2,-62 12,-52 Q 22,-60 34,-64 Q 26,-30 24,-2 Z'
    o = P(fw, dark(c, .18), st)
    o += limb([(-44, 8), (-78, 16), (-104, 4)], 5, c, st)
    o += P('M -104,4 L -118,-5 L -111,9 Z', c, st)
    o += limb([(-44, 8), (-12, 0), (20, -6), (44, -10)], 13, c, st)
    o += P('M 40,-17 L 70,-12 L 67,-4 L 42,-2 Z', c, st)
    o += P('M 44,-15 L 30,-27 L 40,-14 Z', light(c, .35) if c != '#eceff4' else '#9aa6b8', st)
    o += P(nw, light(c, .12), st)
    o += f'<circle cx="57" cy="-11" r="2.2" fill="#fff6c0" stroke="{INK}" stroke-width="1"/>'
    return f'<g transform="translate({cx},{cy}) scale({s*flip},{s})">{extra}{o}</g>'

def mouth_of(cx, cy, s, flip):     # where the snout tip of a young dragon lands
    return (cx + 70*s*flip, cy - 8*s)

out = []
# ---------- space ----------
out.append('<defs><radialGradient id="bg" cx="50%" cy="55%" r="75%"><stop offset="0" stop-color="#1d1840"/>'
           '<stop offset="1" stop-color="#07060f"/></radialGradient></defs>')
out.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
out.append(glow(330, 880, 230, '#c0392b').replace('.85', '.35'))
out.append(glow(420, 930, 180, '#27ae60').replace('.85', '.3'))
out.append(f'<circle cx="370" cy="900" r="9" fill="#fff4d0" stroke="{INK}" stroke-width="2"/>')
for _ in range(260):
    x, y, r = rnd.uniform(0, W), rnd.uniform(0, H), rnd.uniform(.6, 2.2)
    out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="#fff" opacity="{rnd.uniform(.35,.95):.2f}"/>')
for _ in range(14):   # four-point twinkles
    x, y, r = rnd.uniform(0, W), rnd.uniform(0, H), rnd.uniform(5, 10)
    out.append(f'<path d="M {x},{y-r} L {x+r*.22},{y} L {x},{y+r} L {x-r*.22},{y} Z M {x-r},{y} L {x},{y+r*.22} L {x+r},{y} L {x},{y-r*.22} Z" fill="#fff8dc"/>')

gold_pos, silver_pos = np.array([400, 470]), np.array([1000, 820])
out.append(glow(gold_pos[0], gold_pos[1], 330, '#ffd25a'))
out.append(glow(silver_pos[0], silver_pos[1], 240, '#bcd2ff'))
# ---------- Azhi: the colossal serpent ----------
spine = [(-260, 1180), (-40, 900), (70, 560), (210, 250), (520, 70), (900, 40), (1250, 120), (1480, 320),
         (1500, 560), (1380, 690), (1240, 640)]
C = catmull(spine, 1400)
T = np.gradient(C, axis=0); T /= np.linalg.norm(T, axis=1)[:, None]
N = np.stack([-T[:, 1], T[:, 0]], 1)
ctr = np.array([760, 560])
if np.mean(np.sum((ctr - C)*N, 1)) < 0: N = -N              # N points to the inner side (toward the world)
u = np.linspace(0, 1, len(C))
w = 150 + 40*np.sin(np.pi*np.clip(u*1.1, 0, 1)) - 20*np.clip((u-0.88)/0.12, 0, 1)
inner = C + N*(w/2)[:, None]; outer = C - N*(w/2)[:, None]
LAPIS, LAPIS_D, TURQ, GOLDO = '#3a3f8f', '#2a2c6a', '#4fc1b3', '#efbe48'

# flame tufts + dorsal crest on the outer edge (drawn behind the body)
for i in range(30, len(C)-40, 26):
    p, n, ww = outer[i], -N[i], w[i]
    tip = p + n*(34 + 10*math.sin(i)) - T[i]*22
    b1, b2 = p - T[i]*16 + n*4, p + T[i]*16 + n*4
    out.append(P(f'M {b1[0]:.1f},{b1[1]:.1f} Q {p[0]+n[0]*30:.1f},{p[1]+n[1]*30:.1f} {tip[0]:.1f},{tip[1]:.1f} '
                 f'Q {p[0]+n[0]*14+T[i][0]*10:.1f},{p[1]+n[1]*14+T[i][1]*10:.1f} {b2[0]:.1f},{b2[1]:.1f} Z', LAPIS_D, st))
for k, i in enumerate(range(120, len(C)-60, 170)):   # Persian-miniature flame wisps
    p, n = outer[i], -N[i]
    for j, (L, a) in enumerate([(90, -0.5), (70, 0.15), (55, 0.7)]):
        d = n*math.cos(a) - T[i]*math.sin(a)
        tip = p + d*L
        m = p + d*L*0.5 + T[i]*14
        out.append(P(f'M {p[0]-T[i][0]*14:.1f},{p[1]-T[i][1]*14:.1f} Q {m[0]:.1f},{m[1]:.1f} {tip[0]:.1f},{tip[1]:.1f} '
                     f'Q {m[0]-T[i][0]*26:.1f},{m[1]-T[i][1]*26:.1f} {p[0]+T[i][0]*14:.1f},{p[1]+T[i][1]*14:.1f} Z',
                     ['#f39c12', '#e74c3c', GOLDO][j], st))
# vestigial clawed legs on the inner side
def leg(i, side=1):
    p, n, t = inner[i], N[i], T[i]
    knee = p + n*55 + t*30*side
    foot = knee + n*30 - t*25*side
    o = limb([tuple(p - n*10), tuple(knee), tuple(foot)], 26, LAPIS_D, st)
    for a in (-0.6, 0, 0.6):
        d = n*math.cos(a) + t*math.sin(a)
        c = foot + d*20
        o += limb([tuple(foot), tuple(c)], 6, '#efe4c9', st)
    o += P(f'M {knee[0]-16},{knee[1]} Q {knee[0]-24-n[0]*30},{knee[1]-n[1]*30+10} {knee[0]-n[0]*-40},{knee[1]+n[1]*40} Z', '#f39c12', st)
    return o
for i in (420, 470, 980, 1030):
    out.append(leg(i))
# body
body = np.vstack([outer, inner[::-1]])
out.append(P(dpath(body), LAPIS, dict(st, stroke=0)))
# belly plates on the inner side
b_out = C + N*(w*0.06)[:, None]; b_in = C + N*(w*0.44)[:, None]
out.append(f'<path d="{dpath(np.vstack([b_out, b_in[::-1]]))}" fill="{TURQ}"/>')
for i in range(0, len(C)-1, 13):
    a, b = b_out[i], b_in[i]
    out.append(f'<path d="M {a[0]:.1f},{a[1]:.1f} L {b[0]:.1f},{b[1]:.1f}" stroke="{dark(TURQ,.45)}" stroke-width="2.4"/>')
# scale chevrons on the back
for i in range(8, len(C)-30, 22):
    for f in (0.12, 0.28):
        a = C[i] - N[i]*w[i]*f
        q1 = a + T[i]*10 - N[i]*10; q2 = a - T[i]*10 - N[i]*10
        out.append(f'<path d="M {q1[0]:.1f},{q1[1]:.1f} Q {a[0]+T[i][0]*0:.1f},{a[1]:.1f} {q2[0]:.1f},{q2[1]:.1f}" '
                   f'stroke="{LAPIS_D}" stroke-width="3" fill="none" stroke-linecap="round"/>')
# gold filigree diamonds + ribbon along the back
rib = C - N*(w*0.36)[:, None]
out.append(f'<path d="{dpath(rib[:-60], False)}" stroke="{GOLDO}" stroke-width="5" fill="none" stroke-dasharray="26 12"/>')
for i in range(40, len(C)-70, 64):
    a = C[i] - N[i]*w[i]*0.2
    t, n = T[i]*13, N[i]*13
    out.append(f'<path d="M {a[0]+t[0]:.1f},{a[1]+t[1]:.1f} L {a[0]+n[0]:.1f},{a[1]+n[1]:.1f} L {a[0]-t[0]:.1f},{a[1]-t[1]:.1f} '
               f'L {a[0]-n[0]:.1f},{a[1]-n[1]:.1f} Z" fill="{GOLDO}" stroke="{INK}" stroke-width="2"/>'
               f'<circle cx="{a[0]:.1f}" cy="{a[1]:.1f}" r="3.5" fill="#c0392b"/>')
out.append(f'<path d="{dpath(body)}" fill="none" stroke="{INK}" stroke-width="{st["stroke"]*2.6}" stroke-linejoin="round"/>')

# head (local: +x forward, origin at neck end, neck spans y -55..55)
end, tan = C[-1], T[-1]
ang = math.degrees(math.atan2(tan[1], tan[0])); sgn = 1 if math.cos(math.radians(ang)) >= 0 else -1
nw = w[-1]; hs = nw/110
head = []
head.append(P('M 30,-40 C -20,-110 -90,-120 -110,-80 C -125,-50 -90,-30 -70,-48 C -60,-58 -78,-72 -88,-62', '#efe4c9', st,
              extra='stroke-linecap="round"') )
for j, (bx, by, L, a) in enumerate([(10, -55, 110, -2.6), (40, -66, 120, -2.3), (75, -70, 95, -2.0), (0, 20, 100, 2.7)]):
    tip = (bx + L*math.cos(a), by + L*math.sin(a))
    m = (bx + L*0.5*math.cos(a+0.35), by + L*0.5*math.sin(a+0.35))
    head.append(P(f'M {bx-14},{by} Q {m[0]:.1f},{m[1]:.1f} {tip[0]:.1f},{tip[1]:.1f} Q {m[0]+20:.1f},{m[1]+8:.1f} {bx+14},{by+4} Z',
                  ['#f39c12', '#e74c3c', GOLDO, '#f39c12'][j], st))
head.append(P('M 70,10 C 120,14 170,22 228,38 C 244,43 240,62 222,62 L 150,58 C 90,60 40,62 0,55 L 0,18 Z', LAPIS, st))
head.append(P('M 60,-2 L 250,-6 L 226,40 L 72,16 Z', '#7a1b2a', st))
for k in range(8):
    x = 95 + k*19
    head.append(f'<path d="M {x},{-3 - k*0.1} L {x+7},{14} L {x+13},{-3}" fill="#fff8e6" stroke="{INK}" stroke-width="1.8"/>')
    xb = 92 + k*17
    head.append(f'<path d="M {xb},{18 + k*2.2} L {xb+7},{2 + k*2.2} L {xb+12},{19 + k*2.4}" fill="#fff8e6" stroke="{INK}" stroke-width="1.8"/>')
head.append(P('M 0,-55 C 50,-90 125,-86 165,-56 L 246,-38 C 272,-34 274,-6 250,-2 L 150,-2 C 100,-2 50,4 0,20 Z', LAPIS, st))
head.append(f'<path d="M 30,-14 C 80,-24 140,-22 240,-14" stroke="{GOLDO}" stroke-width="4" fill="none"/>')
head.append(f'<path d="M 30,40 C 80,40 140,44 210,52" stroke="{TURQ}" stroke-width="6" fill="none"/>')
head.append(f'<ellipse cx="256" cy="-24" rx="5" ry="3" fill="{INK}"/>')
head.append(P('M 88,-62 Q 120,-80 160,-60 Q 124,-66 92,-52 Z', LAPIS_D, st))
head.append(f'<ellipse cx="122" cy="-48" rx="17" ry="10" fill="#ffd34d" stroke="{INK}" stroke-width="3"/>')
head.append(f'<ellipse cx="124" cy="-48" rx="3.5" ry="9" fill="{INK}"/>')
head.append(f'<circle cx="118" cy="-52" r="2.5" fill="#fff"/>')
for (sx, sy, c1, c2, c3) in [(255, -10, 180, 60, 120), (238, 30, 170, 110, 70)]:   # barbels
    d = f'M {sx},{sy} C {sx-20},{sy+c1*0.5} {sx-c1*0.6},{sy+c2+40} {sx-c1},{sy+c2} C {sx-c1-30},{sy+c2-20} {sx-c1-10},{sy+c2-40} {sx-c1+10},{sy+c2-30}'
    head.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{7+st["stroke"]*2}" stroke-linecap="round"/>')
    head.append(f'<path d="{d}" fill="none" stroke="{GOLDO}" stroke-width="7" stroke-linecap="round"/>')
out.append(f'<g transform="translate({end[0]:.1f},{end[1]:.1f}) rotate({ang:.1f}) scale({hs:.3f},{hs*sgn:.3f})">{"".join(head)}</g>')
HEAD_INFO = (end, ang, sgn, hs)

# ---------- the young world ----------
pc, pr = np.array([700, 600]), 95
out.append(glow(gold_pos[0], gold_pos[1], 120, '#ffffff'))
out.append(glow(silver_pos[0], silver_pos[1], 80, '#ffffff'))
out.append(f'<clipPath id="pl"><circle cx="{pc[0]}" cy="{pc[1]}" r="{pr}"/></clipPath>')
out.append(f'<circle cx="{pc[0]}" cy="{pc[1]}" r="{pr}" fill="#2f86d6"/>')
pl = ['<g clip-path="url(#pl)">']
for (dx, dy, r, k, seed) in [(-40, -20, 40, 9, 1), (35, 30, 34, 8, 2), (45, -45, 22, 7, 3), (-30, 55, 20, 7, 4), (-80, 30, 18, 6, 5)]:
    pl.append(P(blob(pc[0]+dx, pc[1]+dy, r, k, seed), '#4caf50', dict(st, stroke=1.4)))
    pl.append(P(blob(pc[0]+dx+r*0.15, pc[1]+dy+r*0.1, r*0.45, 6, seed+9), '#2e7d32', dict(st, stroke=0)))
for (dx, dy) in [(-35, -25), (40, 25), (-28, 50)]:
    x, y = pc[0]+dx, pc[1]+dy
    pl.append(P(f'M {x-9},{y+6} L {x},{y-10} L {x+9},{y+6} Z', '#8d6e63', dict(st, stroke=1.4)))
    pl.append(f'<path d="M {x-3},{y-4} L {x},{y-10} L {x+3},{y-4} Z" fill="#ff5722"/>')
pl.append(P(f'M {pc[0]-pr},{pc[1]-pr} L {pc[0]+pr},{pc[1]-pr} L {pc[0]+pr},{pc[1]-pr+22} Q {pc[0]},{pc[1]-pr+38} {pc[0]-pr},{pc[1]-pr+22} Z', '#f4f8ff', dict(st, stroke=1.6)))
pl.append(P(f'M {pc[0]-pr},{pc[1]+pr} L {pc[0]+pr},{pc[1]+pr} L {pc[0]+pr},{pc[1]+pr-16} Q {pc[0]},{pc[1]+pr-30} {pc[0]-pr},{pc[1]+pr-16} Z', '#f4f8ff', dict(st, stroke=1.6)))
L = (gold_pos - pc); L = L/np.linalg.norm(L)
sh = pc - L*pr*0.75
pl.append(f'<circle cx="{sh[0]:.1f}" cy="{sh[1]:.1f}" r="{pr*1.12:.1f}" fill="#0e1430" opacity=".62"/>')
pl.append(f'<circle cx="{pc[0]+L[0]*pr*0.45:.1f}" cy="{pc[1]+L[1]*pr*0.45:.1f}" r="{pr*0.28:.1f}" fill="#fff6c8" opacity=".25"/>')
pl.append('</g>')
out += pl
S = silver_pos - pc; th = math.atan2(S[1], S[0]) % (2*math.pi); Cc = 2*math.pi*pr; arc = 0.28*Cc
out.append(f'<circle cx="{pc[0]}" cy="{pc[1]}" r="{pr-4}" fill="none" stroke="#cfe0ff" stroke-width="7" '
           f'stroke-dasharray="{arc:.1f} {Cc:.1f}" stroke-dashoffset="{-(th*(pr-4) - arc/2):.1f}"/>')
out.append(f'<circle cx="{pc[0]}" cy="{pc[1]}" r="{pr}" fill="none" stroke="{INK}" stroke-width="4.5"/>')

# ---------- the seven young dragons ----------
def stream(a, b, colr, wv=10, width=7, dash=None):
    a, b = np.array(a), np.array(b); d = b-a; n = np.array([-d[1], d[0]])/np.linalg.norm(d)
    m1, m2 = a + d*0.33 + n*wv, a + d*0.66 - n*wv
    p = f'M {a[0]:.1f},{a[1]:.1f} C {m1[0]:.1f},{m1[1]:.1f} {m2[0]:.1f},{m2[1]:.1f} {b[0]:.1f},{b[1]:.1f}'
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<path d="{p}" fill="none" stroke="{INK}" stroke-width="{width+3.4}" stroke-linecap="round"{ds}/>'
            f'<path d="{p}" fill="none" stroke="{colr}" stroke-width="{width}" stroke-linecap="round"{ds}/>')

YD = [  # name, pos, scale, colour, flip, gift-target, gift colour
    ('Gold', gold_pos, .62, '#ffc93c', 1, None, None),
    ('Silver', silver_pos, .58, '#e6edf8', -1, None, None),
    ('Blue', (560, 400), .56, '#2e6fd2', 1, (650, 520), '#6ec6ff'),
    ('Red', (900, 700), .56, '#d63a2f', -1, (778, 640), '#ff8a1c'),
    ('White', (520, 760), .56, '#eceff4', 1, (628, 660), '#d9f1ff'),
    ('Green', (860, 420), .56, '#3c9a47', -1, (755, 525), '#9be36b'),
    ('Black', (1020, 300), .56, '#3a3546', -1, None, None),
]
for name, pos, s, c, f, tgt, gc in YD:
    if SHOW_GIFTS and tgt:
        m = mouth_of(pos[0], pos[1], s, f)
        if name == 'White':
            out.append(stream(m, tgt, gc, wv=6, width=6, dash='2 10'))
        elif name == 'Green':
            out.append(stream(m, tgt, gc, wv=12, width=5))
            for k in range(5):
                t = (k+1)/6; q = np.array(m)*(1-t) + np.array(tgt)*t
                out.append(f'<path d="M {q[0]:.0f},{q[1]-7:.0f} q 6,4 0,12 q -6,-4 0,-12 Z" fill="#9be36b" stroke="{INK}" stroke-width="1.5"/>')
        else:
            out.append(stream(m, tgt, gc, wv=12, width=8))
    if name == 'Black': out.append(glow(pos[0], pos[1]-15, 90, '#9b7bd6'))
    out.append(young_dragon(pos[0], pos[1], s, c, flip=f))

svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(out)}</svg>'
open('build/azhi_cover.svg', 'w').write(svg)
import subprocess
subprocess.run([sys.executable, 'svg2png.py', 'build/azhi_cover.svg', 'output/azhi_cover.png', str(W), str(H)], check=True)
print('head end', HEAD_INFO)
