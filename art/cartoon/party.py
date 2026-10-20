"""Cartoon dragonborn library + four style presets (bold is the campaign default).
Run directly to write build/sheet_<style>.svg; see art/README.md."""
import os
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
os.makedirs('build', exist_ok=True); os.makedirs('output', exist_ok=True)
import math, random

# ---------- colour helpers ----------
def _h(c): c = c.lstrip('#'); return [int(c[i:i+2], 16) for i in (0, 2, 4)]
def _x(t): return '#%02x%02x%02x' % tuple(max(0, min(255, int(round(v)))) for v in t)
def mix(a, b, t): A, B = _h(a), _h(b); return _x([A[i]*(1-t)+B[i]*t for i in range(3)])
def dark(a, t=.3): return mix(a, '#000000', t)
def light(a, t=.3): return mix(a, '#ffffff', t)
def desat(a, t=.3):
    A = _h(a); g = sum(A)/3; return _x([A[i]*(1-t)+g*t for i in range(3)])

DRAGONS = {   # scale, belly
    'Gold':   ('#e3a62a', '#f8e09a'),
    'Silver': ('#aab5c2', '#eef2f6'),
    'Black':  ('#3a3546', '#77708a'),
    'Blue':   ('#2e6fd2', '#a3c8f3'),
    'White':  ('#eceff4', '#d5dde8'),
    'Red':    ('#c8342b', '#f3a37c'),
    'Green':  ('#3c9a47', '#b9e292'),
}
HORN = {'White': '#8b96a8', 'Black': '#cfc6dc'}

STYLES = {
    'bold': dict(name='Saturday-Morning Bold',
                 blurb='Thick black ink lines, flat saturated colour, heroic proportions.',
                 stroke=1.7, line='#18120e', head=1.05, leg=1.0, torso=1.08, snout=1.0,
                 eye='slit', cel=False, wc=False, geo=False, bgline=3.0, bgcol='#18120e', sat=0),
    'chibi': dict(name='Chibi Cel-Shaded',
                  blurb='Big heads, tiny bodies, coloured line art and hard cel shadows.',
                  stroke=1.25, line=None, head=1.85, leg=0.58, torso=0.74, snout=0.55,
                  eye='big', cel=True, wc=False, geo=False, bgline=2.2, bgcol=None, sat=-0.05),
    'storybook': dict(name='Storybook Watercolour',
                      blurb='Soft washes on textured paper, loose pencil edges, muted palette.',
                      stroke=0.8, line=None, lineop=0.55, head=1.0, leg=1.0, torso=1.0, snout=1.0,
                      eye='slit', cel=False, wc=True, geo=False, bgline=0, bgcol=None, sat=0.28),
    'geo': dict(name='Mid-Century Flat',
                blurb='Angular shapes, no outlines, limited palette and print grain.',
                stroke=0, line=None, head=1.0, leg=1.18, torso=1.0, snout=1.0,
                eye='dot', cel=False, wc=False, geo=True, bgline=0, bgcol=None, sat=0.18),
}

UID = [0]
def uid(p='u'):
    UID[0] += 1; return f'{p}{UID[0]}'

def col(c, st):
    if st['sat'] > 0: return desat(light(c, st['sat']*0.25), st['sat'])
    return c

def linecol(fill, st):
    if st['line']: return st['line']
    return dark(fill, 0.55)

def P(d, fill, st, extra='', op=None, bg=False):
    """filled path with style-dependent outline"""
    o = f' opacity="{op}"' if op is not None else ''
    if bg:
        w = st['bgline']
        s = f' stroke="{st["bgcol"] or dark(fill, .5)}" stroke-width="{w}" stroke-linejoin="round"' if w else ''
    else:
        w = st['stroke']
        s = (f' stroke="{linecol(fill, st)}" stroke-width="{w}" stroke-linejoin="{"miter" if st["geo"] else "round"}"'
             + (f' stroke-opacity="{st.get("lineop", 1)}"' if w else '')) if w else ''
    return f'<path d="{d}" fill="{fill}"{s}{o} {extra}/>'

def smooth(pts):
    if len(pts) == 2:
        return f'M {pts[0][0]:.1f},{pts[0][1]:.1f} L {pts[1][0]:.1f},{pts[1][1]:.1f}'
    d = f'M {pts[0][0]:.1f},{pts[0][1]:.1f}'
    for i in range(1, len(pts)-1):
        mx, my = (pts[i][0]+pts[i+1][0])/2, (pts[i][1]+pts[i+1][1])/2
        if i == len(pts)-2: mx, my = pts[-1]
        d += f' Q {pts[i][0]:.1f},{pts[i][1]:.1f} {mx:.1f},{my:.1f}'
    return d

def limb(pts, w, fill, st, cap=None):
    d = smooth(pts)
    cap = cap or ('butt' if st['geo'] else 'round')
    out = ''
    if st['stroke']:
        lo = st.get('lineop', 1)
        out += (f'<path d="{d}" fill="none" stroke="{linecol(fill, st)}" stroke-opacity="{lo}" '
                f'stroke-width="{w+2*st["stroke"]}" stroke-linecap="{cap}" stroke-linejoin="round"/>')
    out += f'<path d="{d}" fill="none" stroke="{fill}" stroke-width="{w}" stroke-linecap="{cap}" stroke-linejoin="round"/>'
    return out

def circ(cx, cy, r, fill, st, op=None):
    s = f' stroke="{linecol(fill, st)}" stroke-width="{st["stroke"]}" stroke-opacity="{st.get("lineop",1)}"' if st['stroke'] else ''
    o = f' opacity="{op}"' if op is not None else ''
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}"{s}{o}/>'

def cel(d, st, fill, shape):
    """hard cel shadow clipped to path d"""
    if not st['cel']: return ''
    i = uid('c')
    return (f'<clipPath id="{i}"><path d="{d}"/></clipPath>'
            f'<g clip-path="url(#{i})">{shape.format(f=dark(fill, .28))}</g>')

# ---------- weapons ----------
STEEL = '#dfe6ee'; WOOD = '#7a5233'; LEATHER = '#5a3a22'; BRASS = '#d4a63c'

def glow(cx, cy, r, colr):
    i = uid('g')
    return (f'<radialGradient id="{i}"><stop offset="0" stop-color="{colr}" stop-opacity=".85"/>'
            f'<stop offset="1" stop-color="{colr}" stop-opacity="0"/></radialGradient>'
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="url(#{i})"/>')

def sword(h, dirv, st, L=40):
    n = math.hypot(*dirv); dx, dy = dirv[0]/n, dirv[1]/n; px, py = -dy, dx
    tip = (h[0]+dx*L, h[1]+dy*L)
    o = limb([(h[0]-dx*7, h[1]-dy*7), h], 3, LEATHER, st)
    o += limb([(h[0]+dx*3, h[1]+dy*3), tip], 4.5, col(STEEL, st), st)
    o += limb([(h[0]+dx*3+px*7, h[1]+dy*3+py*7), (h[0]+dx*3-px*7, h[1]+dy*3-py*7)], 3, col(BRASS, st), st)
    o += circ(h[0]-dx*8, h[1]-dy*8, 2.2, col(BRASS, st), st)
    return o

def dagger(h, dirv, st):
    return sword(h, dirv, st, L=16)

def shield(h, accent, st):
    o = circ(h[0], h[1], 14, col(accent, st), st)
    o += f'<circle cx="{h[0]}" cy="{h[1]}" r="8.5" fill="none" stroke="{col(BRASS, st)}" stroke-width="2.4"/>'
    o += f'<circle cx="{h[0]+6}" cy="{h[1]-6}" r="2" fill="{col(BRASS, st)}"/>'   # ouroboros head
    return o

def staff(h, top_y, orb, st):
    o = glow(h[0]+4, top_y, 22, orb)
    o += limb([(h[0]+1, -1), (h[0]+4, top_y+5)], 3, col(WOOD, st), st)
    o += circ(h[0]+4, top_y, 6, light(orb, .35), st)
    return o

def holy(h, st):
    c = (h[0]+1, h[1]-10)
    o = glow(c[0], c[1], 20, '#ffe08a')
    o += f'<circle cx="{c[0]}" cy="{c[1]}" r="6" fill="none" stroke="{linecol(BRASS, st) if st["stroke"] else dark(BRASS,.3)}" stroke-width="{4.2 if st["stroke"] else 0}"/>'
    o += f'<circle cx="{c[0]}" cy="{c[1]}" r="6" fill="none" stroke="#f3cc52" stroke-width="2.6"/>'
    o += limb([(h[0], h[1]), (c[0], c[1]+6)], 1.6, col(BRASS, st), st)
    return o

def mace(h, st):
    e = (h[0]-5, h[1]+19)
    o = limb([h, e], 2.6, col(WOOD, st), st)
    for a in range(0, 360, 60):
        r = math.radians(a)
        o += limb([e, (e[0]+8*math.cos(r), e[1]+8*math.sin(r))], 2.2, col('#8d96a0', st), st)
    o += circ(e[0], e[1], 5, col('#a9b2bc', st), st)
    return o

def bow(h, back, st):
    top, bot = (h[0]-3, h[1]-30), (h[0]-3, h[1]+30)
    o = f'<path d="M {top[0]},{top[1]} L {back[0]},{back[1]} L {bot[0]},{bot[1]}" fill="none" stroke="#e8e2d0" stroke-width=".9"/>'
    o += limb([back, (h[0]+16, h[1])], 1.4, col(WOOD, st), st)
    o += f'<path d="M {h[0]+20},{h[1]} L {h[0]+13},{h[1]-3} L {h[0]+13},{h[1]+3} Z" fill="{col(STEEL, st)}"/>'
    o += limb([top, (h[0]+15, h[1]-12), (h[0]+15, h[1]+12), bot], 3, col(WOOD, st), st)
    return o

# ---------- dragonborn ----------
def head_svg(drag, st, skin, belly, horn):
    sn = st['snout']; S = 17*sn
    if st['geo']:
        d = f'M -11,-6 L 2,-12 L {9+S},-4 L {7+S},3 L 4,9 L -9,6 Z'
        o = P('M -6,-10 L -36,-21 L -12,-3 Z', horn, st)
        o += P('M -10,-1 L -33,5 L -10,5 Z', dark(horn, .15), st)
        o += P(d, skin, st)
        o += P(f'M 4,9 L {7+S},3 L {5+S},6 L 6,11 Z', belly, st)
        o += P(f'M -11,-6 L 2,-12 L 6,-3 L -4,0 Z', dark(skin, .15), st)
        o += f'<circle cx="7" cy="-5" r="2.6" fill="#fff6c8"/><circle cx="7.6" cy="-5" r="1.2" fill="#111"/>'
        return o
    d = (f'M -13,-1 C -14,-13 -2,-16 8,-11 L {8+S},-6 C {14+S},-5 {15+S},4 {9+S},6 '
         f'L 10,10 C 2,13 -12,10 -13,-1 Z')
    lc = linecol(skin, st)
    o = P('M -5,-11 C -12,-21 -25,-22 -33,-14 C -25,-16 -16,-13 -10,-5 Z', horn, st)
    o += P('M -11,-4 C -20,-8 -29,-5 -34,2 C -26,-1 -19,0 -12,3 Z', dark(horn, .12), st)
    o += P('M -11,5 L -20,10 L -12,11 Z', dark(skin, .2), st)
    o += P(d, skin, st)
    o += cel(d, st, skin, '<ellipse cx="-6" cy="11" rx="26" ry="9" fill="{f}"/>')
    o += f'<path d="M 9,9.6 L {8+S},6.3 Q {3+S*0.7},11 9,11.6 Z" fill="{belly}"/>'
    o += f'<path d="M {9+S},4 L 11,5.6" stroke="{lc}" stroke-width="1" fill="none" stroke-linecap="round"/>'
    o += f'<ellipse cx="{5+S}" cy="-1.8" rx="1.3" ry=".8" fill="{lc}"/>'
    if st['eye'] == 'big':
        o += '<ellipse cx="4" cy="-3" rx="4.6" ry="5.6" fill="#221d2c"/>'
        o += '<ellipse cx="4" cy="-1.2" rx="3.4" ry="3" fill="#c98a1e" opacity=".75"/>'
        o += '<circle cx="2.6" cy="-5" r="1.7" fill="#fff"/><circle cx="5.6" cy="-0.6" r=".8" fill="#fff"/>'
        o += f'<path d="M -1,-10 Q 4,-11.5 9,-9" stroke="{lc}" stroke-width="1.2" fill="none" stroke-linecap="round"/>'
    else:
        o += f'<ellipse cx="6" cy="-5" rx="3.3" ry="2.6" fill="#ffe27a" stroke="{lc}" stroke-width=".7"/>'
        o += '<ellipse cx="6.3" cy="-5" rx=".9" ry="2.2" fill="#111"/>'
        o += f'<path d="M -1,-9.5 Q 6,-11.8 12,-8.3" stroke="{dark(skin,.5)}" stroke-width="1.7" fill="none" stroke-linecap="round"/>'
    return o

def figure(x, y, s, drag, role, outfit, accent, st, flip=1, look_back=False):
    skin, belly = DRAGONS[drag]
    skin, belly = col(skin, st), col(belly, st)
    horn = col(HORN.get(drag, '#efe4c9'), st)
    outfit, accent = col(outfit, st), col(accent, st)
    L, T, Hs = st['leg'], st['torso'], st['head']
    hipY = -46*L; sy = hipY - 34*T
    sw = 15*T + 2; hw = 11*T + 1
    far = dark(skin, .18)
    o = [f'<ellipse cx="0" cy="0" rx="{30*max(T,0.8)}" ry="5" fill="#000" opacity=".22"/>']
    geo = st['geo']
    # cape / quiver
    if role in ('rogue', 'ranger'):
        cape = accent if role == 'rogue' else dark(outfit, .1)
        d = (f'M {-sw+4},{sy+1} L {-sw-24},{-6*L} L {-sw-8},{-2*L} L -2,{hipY+8} L {sw-6},{sy+4} Z' if geo else
             f'M {-sw+4},{sy+1} Q {-sw-10},{(sy+hipY)/2} {-sw-24},{-6*L} Q {-sw-12},{-1} {-4},{hipY+10} L {sw-6},{sy+4} Z')
        o.append(P(d, cape, st))
    if role == 'ranger':
        o.append(limb([(-6, sy-6), (-15, hipY+4)], 7, col('#6b4423', st), st))
        for k in range(3):
            o.append(f'<path d="M {-6+k*2.5},{sy-6} l -3,-6 l 4,1 Z" fill="{col("#e9e2cf", st)}"/>')
    # tail
    d = (f'M -4,{hipY-2} L -62,{-4} L -2,{hipY+12} Z' if geo else
         f'M -4,{hipY-2} C -20,{hipY+2} -36,-20 -62,-4 C -36,-12 -20,{hipY+16} -2,{hipY+12} Z')
    o.append(P(d, far, st))
    # back arm + back leg
    pose = {
        'fighter': ((22, sy-4), (-12, sy+16)),
        'wizard':  ((19, sy+12), (-14, hipY+2)),
        'cleric':  ((28, sy+6), (-13, hipY+3)),
        'rogue':   ((22, hipY-6), (-16, hipY-2)),
        'ranger':  ((27, sy+2), (5, sy+1)),
    }[role]
    fh, bh = pose
    fs, bs = (6, sy+5), (-6, sy+5)
    def arm(sh, h, c):
        el = ((sh[0]+h[0])/2 - 2, (sh[1]+h[1])/2 + 6)
        return limb([sh, h] if geo else [sh, el, h], 2.8 if geo else 7, c, st)
    if role == 'rogue': o.append(dagger(bh, (-0.6, 1), st))
    if role == 'cleric': o.append(mace(bh, st))
    o.append(arm(bs, bh, far))
    o.append(circ(bh[0], bh[1], 2.2 if geo else 3.8, far, st))
    lw = 2.8 if geo else 9
    if geo:
        o.append(limb([(-4, hipY), (-11, -2)], lw, far, st))
        o.append(limb([(4, hipY), (8, -2)], lw, skin, st))
        o.append(P('M -15,0 L -7,-4 L -5,0 Z', far, st)); o.append(P('M 5,0 L 11,-4 L 15,0 Z', skin, st))
    else:
        o.append(limb([(-5, hipY+4), (1, hipY*0.5), (-8, -7*L), (-2, -1)], lw, far, st))
        o.append(P('M -9,0 Q -6,-6 4,-3 L 6,0 Z', far, st))
        o.append(limb([(5, hipY+4), (12, hipY*0.5), (5, -7*L), (9, -1)], lw, skin, st))
        o.append(P('M 4,0 Q 7,-6 17,-3 L 19,0 Z', skin, st))
    # robe
    if role in ('wizard', 'cleric'):
        bottom = -3 if role == 'wizard' else hipY*0.35
        d = (f'M 0,{sy+8} L {hw+12},{bottom} L {-hw-12},{bottom} Z' if geo else
             f'M {-hw-1},{hipY-2} L {hw+1},{hipY-2} L {hw+9},{bottom} Q 0,{bottom+4} {-hw-9},{bottom} Z')
        o.append(P(d, outfit, st))
        o.append(f'<path d="M {-hw-9 if not geo else -hw-12},{bottom-1} L {hw+9 if not geo else hw+12},{bottom-1}" stroke="{accent}" stroke-width="2.5"/>')
    # torso
    d = (f'M {-sw-2},{sy} L {sw+2},{sy} L 6,{hipY+2} L -6,{hipY+2} Z' if geo else
         f'M {-sw},{sy+4} Q {-sw},{sy-2} {-sw+6},{sy-3} L {sw-6},{sy-3} Q {sw},{sy-2} {sw},{sy+4} '
         f'L {hw+1},{hipY+2} Q 0,{hipY+7} {-hw-1},{hipY+2} Z')
    o.append(P(d, outfit, st))
    if geo:
        o.append(f'<path d="M 0,{sy} L {sw+2},{sy} L 6,{hipY+2} L 0,{hipY+2} Z" fill="{dark(outfit,.2)}"/>')
    o.append(cel(d, st, outfit, f'<rect x="{-sw-4}" y="{sy-6}" width="{sw*0.75}" height="80" fill="{{f}}"/>'))
    if role == 'fighter':
        td = (f'M -6,{sy+2} L 6,{sy+2} L 0,{hipY+14} Z' if geo else
              f'M -7,{sy+3} L 7,{sy+3} L 8,{hipY+15} L 0,{hipY+19} L -8,{hipY+15} Z')
        o.append(P(td, accent, st))
        o.append(f'<circle cx="0" cy="{(sy+hipY)/2}" r="4" fill="none" stroke="{col(BRASS, st)}" stroke-width="1.8"/>')
    if role == 'cleric':
        o.append(f'<circle cx="2" cy="{sy+10}" r="4.5" fill="none" stroke="{col(BRASS, st)}" stroke-width="2"/>')
    if not geo:
        o.append(f'<rect x="{-hw-1}" y="{hipY-3}" width="{2*hw+2}" height="4" fill="{col(LEATHER, st)}"/>')
    # neck + head
    hc = (10, sy - 9 - 10*Hs)
    if geo:
        o.append(P(f'M -1,{sy+2} L 8,{sy+2} L 12,{hc[1]+4} L 6,{hc[1]+6} Z', skin, st))
    else:
        o.append(limb([(2, sy+3), (6, sy-4), (hc[0]-1, hc[1]+5)], 10, skin, st))
        o.append(limb([(6, sy+1), (9, sy-4), (hc[0]+3, hc[1]+8)], 3.5, belly, dict(st, stroke=0)))
    hflip = -1 if look_back else 1
    o.append(f'<g transform="translate({hc[0]},{hc[1]}) scale({Hs*hflip},{Hs})">{head_svg(drag, st, skin, belly, horn)}</g>')
    if role == 'fighter':
        o.append(shield(bh, accent, st))
        o.append(circ(fs[0]+1, fs[1]-1, 7 if not geo else 5, light(outfit, .15), st))
    # front arm + held item
    if role == 'fighter': o.append(sword(fh, (0.3, -1), st))
    if role == 'wizard': o.append(staff(fh, sy-38, '#7ff0ff' if drag != 'Black' else '#c58bff', st))
    if role == 'cleric': o.append(holy(fh, st))
    if role == 'rogue': o.append(dagger(fh, (1, -0.25), st))
    o.append(arm(fs, fh, skin))
    o.append(circ(fh[0], fh[1], 2.2 if geo else 3.8, skin, st))
    if role == 'ranger': o.append(bow(fh, bh, st))
    g = ''.join(o)
    return f'<g transform="translate({x},{y}) scale({s*flip},{s})">{g}</g>'

# ---------- sky dragons ----------
def sky_dragon(cx, cy, s, colr, glowc, st, flip=1):
    c = col(colr, st)
    o = glow(0, -10, 230, glowc)
    o += glow(0, -10, 95, '#ffffff')
    fw = 'M 0,-4 L -14,-72 L 4,-58 L 14,-84 L 24,-58 L 46,-70 L 30,-6 Z'
    nw = 'M 4,-2 L -34,-60 L -10,-52 L -8,-76 L 12,-52 L 32,-62 L 24,-2 Z'
    if not st['geo']:
        fw = 'M 0,-4 Q -6,-50 -14,-74 Q -2,-62 4,-58 Q 8,-74 14,-86 Q 18,-66 24,-58 Q 34,-68 48,-72 Q 36,-36 30,-6 Z'
        nw = 'M 4,-2 Q -18,-36 -36,-62 Q -20,-54 -10,-52 Q -12,-66 -8,-78 Q 2,-62 12,-52 Q 22,-60 34,-64 Q 26,-30 24,-2 Z'
    o += P(fw, dark(c, .15), st)
    o += limb([(-44, 8), (-78, 16), (-104, 4)], 5, c, st)
    o += P('M -104,4 L -116,-4 L -110,8 Z', c, st)
    o += limb([(-44, 8), (-12, 0), (20, -6), (44, -10)], 13, c, st)
    o += P('M 40,-17 L 70,-12 L 67,-4 L 42,-2 Z', c, st)
    o += P('M 44,-15 L 30,-26 L 40,-14 Z', light(c, .3), st)
    o += P(nw, light(c, .1), st)
    o += f'<circle cx="58" cy="-10" r="1.6" fill="{dark(c,.6)}"/>'
    return f'<g transform="translate({cx},{cy}) scale({s*flip},{s})">{o}</g>'

# ---------- scene pieces ----------
def sky(stops, st, y0=0, y1=800):
    if st['geo']:
        n = 6; h = (y1-y0)/n; o = ''
        for i in range(n):
            t = i/(n-1); k = t*(len(stops)-1); j = min(int(k), len(stops)-2)
            c = mix(stops[j], stops[j+1], k-j)
            o += f'<rect x="0" y="{y0+i*h:.1f}" width="1200" height="{h+1:.1f}" fill="{col(c, st)}"/>'
        return o
    i = uid('sky')
    st_ = ''.join(f'<stop offset="{k/(len(stops)-1):.2f}" stop-color="{col(c, st)}"/>' for k, c in enumerate(stops))
    return (f'<linearGradient id="{i}" x1="0" y1="0" x2="0" y2="1">{st_}</linearGradient>'
            f'<rect x="0" y="{y0}" width="1200" height="{y1-y0}" fill="url(#{i})"/>')

def ring_arch(d, w, st, op=1.0):
    sea, land = col('#86b4cf', st), col('#7fa35a', st)
    o = f'<g opacity="{op}">'
    if st['bgline']:
        o += f'<path d="{d}" fill="none" stroke="{st["bgcol"] or dark(sea,.5)}" stroke-width="{w+2*st["bgline"]}"/>'
    o += f'<path d="{d}" fill="none" stroke="{sea}" stroke-width="{w}"/>'
    o += f'<path d="{d}" fill="none" stroke="{land}" stroke-width="{w*0.62}" stroke-dasharray="70 40 25 60 120 35 40 90"/>'
    o += f'<path d="{d}" fill="none" stroke="{light(sea,.5)}" stroke-width="{w*0.12}" transform="translate(0,{-w*0.38})"/>'
    o += '</g>'
    return o

def cloud(x, y, s, st, c='#ffffff'):
    if st['geo']:
        return f'<path d="M {x-60*s},{y} L {x-30*s},{y-22*s} L {x+10*s},{y-30*s} L {x+60*s},{y} Z" fill="{col(c,st)}" opacity=".85"/>'
    d = (f'M {x-60*s},{y} Q {x-62*s},{y-24*s} {x-34*s},{y-22*s} Q {x-26*s},{y-46*s} {x},{y-38*s} '
         f'Q {x+20*s},{y-56*s} {x+38*s},{y-30*s} Q {x+64*s},{y-28*s} {x+60*s},{y} Z')
    return P(d, col(c, st), st, bg=True, op=.95)

def ridge(seed, y, amp, step, rough=1.0):
    rnd = random.Random(seed); pts = []
    x = -40
    while x < 1260:
        pts.append((x, y + rnd.uniform(-amp, amp*0.4)*rough)); x += step*rnd.uniform(0.6, 1.4)
    return pts

def poly(pts, bottom=820):
    d = f'M {pts[0][0]:.1f},{bottom} ' + ' '.join(f'L {a:.1f},{b:.1f}' for a, b in pts) + f' L {pts[-1][0]:.1f},{bottom} Z'
    return d

def wave(y, amp, n, phase, bottom=820):
    d = f'M -20,{bottom} L -20,{y}'
    for i in range(n+1):
        x = -20 + i*1240/n
        cy = y + amp*math.sin(i*1.7+phase)
        if i: d += f' Q {x-620/n:.1f},{cy-amp*0.8:.1f} {x:.1f},{cy:.1f}'
    return d + f' L 1220,{bottom} Z'

def fang(x, yb, h, w, lean):
    return (f'M {x-w/2},{yb} C {x-w/2},{yb-h*0.5} {x+lean*0.6-w*0.15},{yb-h*0.85} {x+lean},{yb-h} '
            f'C {x+lean*0.6+w*0.12},{yb-h*0.7} {x+w/2},{yb-h*0.4} {x+w/2},{yb} Z')

def fang_geo(x, yb, h, w, lean):
    return f'M {x-w/2},{yb} L {x+lean},{yb-h} L {x+w/2},{yb} Z'

def FANG(st, *a): return fang_geo(*a) if st['geo'] else fang(*a)

# ---------- filters / overlays ----------
def defs(st):
    o = ''
    if st['wc']:
        o += ('<filter id="wcbg" x="-5%" y="-5%" width="110%" height="110%">'
              '<feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="3" seed="4" result="n"/>'
              '<feDisplacementMap in="SourceGraphic" in2="n" scale="14" xChannelSelector="R" yChannelSelector="G" result="d"/>'
              '<feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="11" result="m"/>'
              '<feColorMatrix in="m" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -0.55 1.18" result="ma"/>'
              '<feComposite in="d" in2="ma" operator="in" result="c"/><feGaussianBlur in="c" stdDeviation="1.1"/></filter>'
              '<filter id="wcfig" x="-10%" y="-10%" width="120%" height="120%">'
              '<feTurbulence type="fractalNoise" baseFrequency="0.06" numOctaves="2" seed="7" result="n"/>'
              '<feDisplacementMap in="SourceGraphic" in2="n" scale="4" xChannelSelector="R" yChannelSelector="G" result="d"/>'
              '<feTurbulence type="fractalNoise" baseFrequency="0.09" numOctaves="2" seed="3" result="m"/>'
              '<feColorMatrix in="m" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -0.35 1.12" result="ma"/>'
              '<feComposite in="d" in2="ma" operator="in"/></filter>'
              '<filter id="paper"><feTurbulence type="fractalNoise" baseFrequency="1.3" numOctaves="2" seed="9"/>'
              '<feColorMatrix type="matrix" values="0 0 0 0 .55  0 0 0 0 .47  0 0 0 0 .36  0.6 0 0 0 -0.22"/></filter>')
    if st['geo']:
        o += ('<pattern id="grain" width="7" height="7" patternUnits="userSpaceOnUse">'
              '<circle cx="1.5" cy="1.5" r=".8" fill="#000" opacity=".16"/><circle cx="5" cy="4.5" r=".6" fill="#fff" opacity=".14"/>'
              '<circle cx="3.5" cy="6" r=".5" fill="#000" opacity=".1"/></pattern>')
    return f'<defs>{o}</defs>'

def overlay(st):
    if st['wc']:
        return ('<rect width="1200" height="800" fill="#f2ead8" opacity=".18" style="mix-blend-mode:multiply"/>'
                '<rect width="1200" height="800" filter="url(#paper)" opacity=".4" style="mix-blend-mode:multiply"/>')
    if st['geo']:
        return '<rect width="1200" height="800" fill="url(#grain)"/>'
    return ''

def wrapbg(st, inner):
    return f'<rect width="1200" height="800" fill="#f4ecdc"/><g filter="url(#wcbg)">{inner}</g>' if st['wc'] else inner

def wrapfig(st, inner):
    return f'<g filter="url(#wcfig)">{inner}</g>' if st['wc'] else inner

# ---------- scenes ----------
PARTY_A = [  # crossing the Spine Range under the wandering Gold
    (300, 'Blue', 'cleric', '#efe4cc', '#2b5fa8', 1, False, 0.96),
    (480, 'Silver', 'wizard', '#4b3a7a', '#f2d16b', 1, True, 1.0),
    (690, 'Red', 'fighter', '#8d98a6', '#2f4f8f', 1, False, 1.06),
    (900, 'Green', 'rogue', '#5a3e2b', '#3d2f4f', 1, False, 0.98),
]
PARTY_B = [  # on the shore of the Inner Sea beneath the Lower Jaw
    (290, 'White', 'fighter', '#6f7b8a', '#9b2d2d', 1, False, 1.04),
    (490, 'Black', 'wizard', '#2f6b6b', '#e8c35a', 1, False, 1.0),
    (690, 'Gold', 'cleric', '#f3efe6', '#c08a1e', -1, False, 0.98),
    (900, 'Red', 'ranger', '#55663a', '#7a4e2a', -1, False, 1.0),
]

def party(lst, gy, st, base):
    sc = base*(0.92 if st['head'] > 1.5 else 1.0)
    return ''.join(figure(x, gy + (6 if i % 2 else 0), sc*k, d, r, o, a, st, flip=f, look_back=lb)
                   for i, (x, d, r, o, a, f, lb, k) in enumerate(lst))

def scene_spine(st):
    b = sky(['#5fb2ea', '#9fd3f2', '#ffe7b0'], st, 0, 600)
    b += ring_arch('M -80,560 Q 420,-40 1300,70', 30, st, op=.55)
    b += sky_dragon(330, 190, 1.15, '#ffc93c', '#ffd25a', st)
    if not st['geo'] or True:
        b += cloud(820, 180, 1.0, st) + cloud(1030, 250, .7, st) + cloud(120, 300, .8, st)
    far = ridge(3, 440, 60, 55)
    b += P(poly(far), col('#9aa6c8', st), st, bg=True)
    # vertebral spires along the spine
    rnd = random.Random(8)
    for i, x in enumerate(range(40, 1240, 112)):
        h = 150 + 55*math.sin(i*0.9) + rnd.uniform(-15, 15)
        b += P(FANG(st, x, 520, h, 46, -18), col('#e7dcc3', st), st, bg=True)
        b += f'<path d="{FANG(st, x+8, 520, h*0.92, 22, -14)}" fill="{col("#c9b994", st)}" opacity=".7"/>'
    b += P(poly(ridge(5, 520, 25, 70)), col('#8c94b2', st), st, bg=True)
    b += P(wave(575, 18, 5, 0.5), col('#7fb357', st), st, bg=True)
    b += P(wave(630, 20, 4, 2.0), col('#5f9a42', st), st, bg=True)
    led = [(-20, 712), (120, 700), (260, 706), (420, 694), (600, 700), (760, 692), (940, 702), (1100, 696), (1230, 704)]
    b += P(poly(led), col('#b08955', st), st, bg=True)
    b += P(poly([(a, c+10) for a, c in led]), col('#94703f', st), st, bg=False and None or True) if False else ''
    b += f'<path d="{poly([(a, c+12) for a, c in led])}" fill="{col("#8f6a3c", st)}" opacity=".55"/>'
    for (sx, sy_, r) in [(80, 760, 18), (1060, 770, 22), (560, 785, 14), (230, 790, 10), (1160, 740, 12)]:
        b += P(f'M {sx-r},{sy_} Q {sx-r},{sy_-r} {sx},{sy_-r} Q {sx+r},{sy_-r} {sx+r},{sy_} Z' if not st['geo']
               else f'M {sx-r},{sy_} L {sx-r*0.3},{sy_-r} L {sx+r},{sy_} Z', col('#7d6a52', st), st, bg=True)
    f = party(PARTY_A, 708, st, 2.25)
    return wrapbg(st, b) + wrapfig(st, f)

def scene_sea(st):
    b = sky(['#232650', '#5b5a8f', '#b7b8d4', '#d9dfe6'], st, 0, 520)
    rnd = random.Random(2)
    for _ in range(70):
        x, y = rnd.uniform(0, 1200), rnd.uniform(0, 330)
        b += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.uniform(.6, 1.8):.1f}" fill="#fff" opacity="{rnd.uniform(.4, .9):.2f}"/>'
    b += ring_arch('M -160,640 Q 600,-420 1360,640', 64, st, op=.9)
    b += sky_dragon(880, 210, 0.95, '#e6edf8', '#bcd2ff', st, flip=-1)
    # sea
    if st['geo']:
        for i, c in enumerate(['#6f8fa8', '#5a7b96', '#476883', '#36566f', '#2a4860']):
            b += f'<rect x="0" y="{480+i*64}" width="1200" height="66" fill="{col(c, st)}"/>'
    else:
        i = uid('sea')
        b += (f'<linearGradient id="{i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{col("#7f9db4", st)}"/>'
              f'<stop offset="1" stop-color="{col("#284660", st)}"/></linearGradient>'
              f'<rect x="0" y="480" width="1200" height="320" fill="url(#{i})"/>')
    # the Lower Jaw on the horizon: long ridge with a row of teeth
    jaw = [(-20, 486), (80, 470), (220, 462), (380, 466), (520, 474), (640, 484), (700, 490)]
    for k, (x, y) in enumerate([(60, 474), (120, 468), (180, 464), (240, 462), (300, 463), (360, 465), (420, 467), (480, 471), (540, 476), (600, 480)]):
        b += P(FANG(st, x, y+4, 26 + 8*math.sin(k), 12, -3), col('#d9d2c2', st), st, bg=True)
    b += P(poly(jaw, 492), col('#5b5f70', st), st, bg=True)
    # fog
    b += f'<rect x="0" y="440" width="1200" height="70" fill="#e6ecf2" opacity=".35"/>'
    # sea-stack fangs
    for (x, yb, h, w, lean) in [(620, 520, 90, 26, 6), (1000, 560, 160, 46, -14), (170, 600, 175, 52, 18), (1120, 610, 210, 58, -22), (800, 650, 250, 74, -10)]:
        b += P(FANG(st, x, yb, h, w, lean), col('#4b5060', st), st, bg=True)
        b += f'<path d="{FANG(st, x - w*0.18, yb, h*0.9, w*0.45, lean)}" fill="{col("#8a90a3", st)}" opacity=".55"/>'
        b += f'<ellipse cx="{x}" cy="{yb}" rx="{w*0.8}" ry="{w*0.08+2}" fill="#dfe8ef" opacity=".35"/>'
    for k in range(14):
        y = 540 + k*18; x = rnd.uniform(0, 1000)
        b += f'<path d="M {x:.0f},{y} l {rnd.uniform(60, 180):.0f},0" stroke="#dbe7f0" stroke-width="2" opacity=".25"/>'
    # shore
    shore = [(-20, 706), (160, 694), (330, 700), (520, 690), (720, 698), (900, 688), (1080, 700), (1230, 694)]
    b += f'<path d="{poly([(a, c-8) for a, c in shore])}" fill="#e8eef3" opacity=".35"/>'
    b += P(poly(shore), col('#8c8577', st), st, bg=True)
    for k in range(40):
        x, y = rnd.uniform(0, 1200), rnd.uniform(720, 795)
        r = rnd.uniform(3, 9)
        b += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{r:.1f}" ry="{r*0.55:.1f}" fill="{col("#6e675b", st)}" opacity=".7"/>'
    f = party(PARTY_B, 730, st, 2.25)
    return wrapbg(st, b) + wrapfig(st, f)

def scene_svg(st, which):
    body = scene_spine(st) if which == 'A' else scene_sea(st)
    return defs(st) + body + overlay(st)

def sheet(key):
    st = STYLES[key]
    W, H = 2440, 960
    a = scene_svg(st, 'A'); b = scene_svg(st, 'B')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="#1c1916"/>
<text x="40" y="70" font-family="DejaVu Serif, serif" font-size="46" fill="#f3e8cf" font-weight="bold">{st["name"]}</text>
<text x="40" y="112" font-family="DejaVu Serif, serif" font-size="24" fill="#c9bda3" font-style="italic">{st["blurb"]}</text>
<svg x="20" y="140" width="1200" height="800" viewBox="0 0 1200 800">{a}</svg>
<svg x="1220" y="140" width="1200" height="800" viewBox="0 0 1200 800">{b}</svg>
</svg>'''

if __name__ == '__main__':
    import sys
    for k in STYLES:
        open(f'build/sheet_{k}.svg', 'w').write(sheet(k))
    print('ok')
