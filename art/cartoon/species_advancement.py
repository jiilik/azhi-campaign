"""Species advancement wheel (Troy, 2026-11-11) -> output/species_advancement.png.

The nine-form colour wheel from colour_wheel.py (kept as is there), without
Gold and Silver, with six concentric advancement rings around it. Nine radial
lines carry each colour's spoke outward: 9 x 6 = 54 arcs to fill in. Arc text
follows the arc (curved text paths); on the lower half the path runs the other
way so the text stays upright.

Fill arcs in ARCS below: ARCS[(form, ring)] = ("Name", "subtitle").
Ring costs are linear for now (Troy, 2026-11-11). PROPOSED design.
"""
import os, sys, math, random, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE); sys.path.insert(0, HERE)
import colour_wheel as cw
import party
from party import figure, light, dark

st, INK = cw.st, cw.INK
RINGS = 6
R0 = cw.R_OUT + 14          # the colour wheel's outer edge (its thin outer circle)
RW = 112                     # width of each advancement ring
R_MAX = R0 + RINGS * RW
MARGIN = 130
W = H = int(2 * (R_MAX + MARGIN))
CX = CY = W // 2 + 20
# colour_wheel's helpers read these module globals.
cw.W, cw.H, cw.CX, cw.CY = W, H, CX, CY
STEP = cw.STEP

# Arc contents: (form, ring) -> (title, subtitle). Empty for now.
ARCS = {}


def pt(r, a_deg):
    a = math.radians(a_deg - 90)
    return CX + r * math.cos(a), CY + r * math.sin(a)


def arc_band(r_in, r_out, a0, a1, fill):
    p0, p1 = pt(r_out, a0), pt(r_out, a1)
    q1, q0 = pt(r_in, a1), pt(r_in, a0)
    return (f'<path d="M {p0[0]:.1f},{p0[1]:.1f} A {r_out},{r_out} 0 0 1 {p1[0]:.1f},{p1[1]:.1f} '
            f'L {q1[0]:.1f},{q1[1]:.1f} A {r_in},{r_in} 0 0 0 {q0[0]:.1f},{q0[1]:.1f} Z" '
            f'fill="{fill}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>')


def text_arc(pid, r, a0, a1):
    """A path along radius r from a0 to a1 (clockwise), reversed on the lower
    half so text along it reads upright."""
    mid = (a0 + a1) / 2 % 360
    if 90 < mid < 270:
        p, q = pt(r, a1), pt(r, a0)
        return f'<path id="{pid}" d="M {p[0]:.1f},{p[1]:.1f} A {r},{r} 0 0 0 {q[0]:.1f},{q[1]:.1f}" fill="none"/>', True
    p, q = pt(r, a0), pt(r, a1)
    return f'<path id="{pid}" d="M {p[0]:.1f},{p[1]:.1f} A {r},{r} 0 0 1 {q[0]:.1f},{q[1]:.1f}" fill="none"/>', False


def curved(pid, text, size, weight="bold", style="normal", fill=INK):
    return (f'<text font-family="DejaVu Sans" font-size="{size}" font-weight="{weight}" '
            f'font-style="{style}" fill="{fill}"><textPath href="#{pid}" startOffset="50%" '
            f'text-anchor="middle">{text}</textPath></text>')


def stars(n, seed):
    rnd = random.Random(seed); o = ''
    for _ in range(n):
        x, y = rnd.uniform(0, W), rnd.uniform(0, H)
        if math.hypot(x - CX, y - CY) < R_MAX + 25: continue
        o += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.uniform(.7, 2.2):.1f}" fill="#fff" opacity="{rnd.uniform(.35, .9):.2f}"/>'
    return o


def build():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    o.append('<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
             '<stop offset="0" stop-color="#1d2148"/><stop offset=".55" stop-color="#3b3a6e"/>'
             '<stop offset="1" stop-color="#25233f"/></linearGradient></defs>')
    o.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
    o.append(stars(260, 3))

    # Six advancement rings, nine spokes. Each spoke fades lighter outward.
    defs, texts = [], []
    for i, (form, name, *_rest) in enumerate(cw.WHEEL):
        scale, _belly = party.DRAGONS[form]
        a0, a1 = i * STEP - STEP / 2, i * STEP + STEP / 2
        for k in range(1, RINGS + 1):
            r_in, r_out = R0 + (k - 1) * RW, R0 + k * RW
            o.append(arc_band(r_in, r_out, a0, a1, light(scale, 0.35 + 0.08 * k)))
            title, sub = ARCS.get((form, k), (f"{name} {k}", "to be designed"))
            pid = f"t_{form}_{k}"
            # two lines: title nearer the outer edge, subtitle nearer the inner
            mid_r = (r_in + r_out) / 2
            lower = 90 < (i * STEP) % 360 < 270
            r_title = mid_r + (-10 if lower else 10)
            r_sub = mid_r + (24 if lower else -24)
            pad = 2.0
            d1, _ = text_arc(pid + "a", r_title, a0 + pad, a1 - pad)
            d2, _ = text_arc(pid + "b", r_sub, a0 + pad, a1 - pad)
            defs += [d1, d2]
            texts.append(curved(pid + "a", title, 30))
            texts.append(curved(pid + "b", sub, 20, weight="normal", style="italic", fill="#4a4036"))
    o.append('<defs>' + ''.join(defs) + '</defs>')
    o += texts
    # The colour wheel itself, as in colour_wheel.py (no Gold or Silver).
    o.append(f'<circle cx="{CX}" cy="{CY}" r="{R0}" fill="#2a2850" stroke="{INK}" stroke-width="3"/>')
    for i, (form, *_rest) in enumerate(cw.WHEEL):
        scale, _belly = party.DRAGONS[form]
        o.append(cw.wedge(i * STEP - STEP / 2, i * STEP + STEP / 2, light(scale, .55)))
    o.append(f'<circle cx="{CX}" cy="{CY}" r="{cw.R_IN}" fill="#f6eedb" stroke="{INK}" stroke-width="3"/>')
    figs, labs = [], []
    for i, (form, name, sub, role, outfit, accent) in enumerate(cw.WHEEL):
        a = i * STEP
        x, y = pt(cw.R_FIG, a)
        flip = -1 if 0 < a < 180 else 1
        feet = y + 52
        figs.append(figure(x, feet, 1.12, form, role, outfit, accent, st, flip=flip))
        labs.append(cw.label(x, feet + 10, name, sub, big=(form in cw.PRIMARY)))
    o += figs + labs
    o.append(cw.unphased(CX, CY + 95, 1.75))
    o.append(cw.label(CX, CY + 112, 'Unphased', 'all colours, none settled', big=True))
    # Nine radial lines, drawn over the rings
    for i in range(len(cw.WHEEL)):
        a = i * STEP - STEP / 2
        p, q = pt(R0, a), pt(R_MAX, a)
        o.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    o.append(f'<circle cx="{CX}" cy="{CY}" r="{R_MAX}" fill="none" stroke="{INK}" stroke-width="6"/>')
    # Title
    o.append(f'<text x="{W/2}" y="80" text-anchor="middle" font-family="DejaVu Serif" font-weight="bold" '
             f'font-size="56" fill="#f3e8cf">Species Advancement</text>')
    o.append(f'<text x="{W/2}" y="120" text-anchor="middle" font-family="DejaVu Serif" font-style="italic" '
             f'font-size="24" fill="#c9bda3">The colour wheel, with six rings of advancement on each spoke (draft, 2026-11-11; PROPOSED)</text>')
    o.append('</svg>')
    return ''.join(o)


if __name__ == '__main__':
    os.makedirs('build', exist_ok=True); os.makedirs('output', exist_ok=True)
    open('build/species_advancement.svg', 'w').write(build())
    subprocess.run([sys.executable, 'svg2png.py', 'build/species_advancement.svg',
                    'output/species_advancement.png', str(W), str(H)], check=True)
    print('output/species_advancement.png', W, H)
