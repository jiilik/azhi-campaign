"""Tile and ring-segment details for the printable wheels (Troy, voice, 2026-11-15).

Writes canon/diagrams/_details.pdf, which print_wheels.py appends after the two
wheel pages. Every skills-grid tile, sorted by number, then every species-wheel
arc, sorted by colour (wheel order) then ring. Each entry gathers what the
repo says about it:
  - the grid itself (skills_grid.py): name, Hit Die, pools, Prof. Up, Attack Up,
    ability +1
  - the species wheel (art/cartoon/species_advancement.py): the same for arcs
  - kit contents (canon/decisions.md, 2026-11-08; canon/brainstorm-progression.md)
  - Expertise (canon/brainstorm-progression.md, item 10)
  - techniques (canon/techniques.md)
  - parts from the parts bin (canon/tile-assignments.md, all REVIEW)
Run through print_wheels.py, or alone: python3 canon/diagrams/print_details.py
"""
import contextlib
import html
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tile_points as TP  # noqa: E402  (temporary, for balancing)
POINTS = {}

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CARTOON = os.path.join(ROOT, 'art', 'cartoon')
OUT = os.path.join(HERE, '_details.pdf')

# Kit contents for a starting kit (canon/decisions.md, "Kit contents, ring 1";
# saves and skills from canon/brainstorm-progression.md items 9 and 10).
KITS = {
    '11': ['3 at-wills; light armour (command and control, not a caster).',
           'Save: Cha, Dex or Int. Skills: 2 of Deception, Insight, Intimidation, Performance, Persuasion.'],
    '12': ['2 at-wills; light armour; Finesse, Light and ranged martial weapons; 2 weapon masteries; +5 ft Speed.',
           'Save: Dex, Cha or Str. Skills: 2 of Acrobatics, Perception, Sleight of Hand, Stealth, Survival.'],
    '13': ['1 at-will; light and medium armour, Shields, martial weapons; 3 weapon masteries.',
           'Save: Str, Dex or Con. Skills: 1 of Acrobatics, Animal Handling, Athletics, Intimidation.'],
    '14': ['Hit points as its pool; light and medium armour, Shields, martial weapons; Second Wind.',
           'Save: Con, Str or Wis. Skills: 1 of Athletics, Intimidation, Perception, Survival.'],
    '15': ['2 cantrips; light armour. Counts as 4 prepared spells as a starting kit, 1 if taken later.',
           'Save: Wis, Con or Int. Skills: 2 of Animal Handling, History, Insight, Medicine, Nature, Religion.'],
    '16': ['3 cantrips; rituals. Starting kit: a spellbook of six spells (one of three books); taken later, three. '
           'Counts as 4 prepared spells as a starting kit, 1 if taken later.',
           'Save: Int, Wis or Cha. Skills: 1 of Arcana, History, Investigation, Religion.'],
}
EXPERTISE = {'202': 'Expertise in two skills you are proficient in',
             '403': 'Expertise in one skill you are proficient in',
             '604': 'Expertise in one skill you are proficient in',
             '210': 'Knowledge Expertise: one of Arcana, History, Investigation, Medicine, Nature or Religion'}
# canon/techniques.md, "Where techniques are learned" and the Scout tables.
TECHNIQUES = {
    '11': 'Rally; the coaching set (You’ve Got This!, There’s an Opening!, Heads Up!)',
    '201': 'the Invigorate family (Invigorate, Greater Invigorate, Reinvigorate); Momentum',
    '202': 'On Me!, Scatter!',
    '12': 'I’m Going First!, Sidestep, Superhero Landing',
    '304': 'Free Dash or Disengage (Bonus Action, 0 Stamina); Deflect Attacks; Take Aim',
    '305': 'Uncanny Dodge',
    '405': 'Greater Sidestep',
    '508': 'Evasion',
}


def grid():
    """Run skills_grid.py up to its drawing code and return its tables."""
    os.chdir(HERE)
    src = open('skills_grid.py').read().split('\n')
    stop = next(i for i, l in enumerate(src) if l.startswith('fig, ax = plt.subplots'))
    g = {'__file__': os.path.join(HERE, 'skills_grid.py')}
    argv, sys.argv = sys.argv, ['skills_grid.py']
    with contextlib.redirect_stdout(io.StringIO()):
        exec('\n'.join(src[:stop]), g)
    sys.argv = argv
    return g


def wheel():
    os.chdir(CARTOON)
    sys.path.insert(0, CARTOON)
    argv, sys.argv = sys.argv, ['species_advancement.py']
    with contextlib.redirect_stdout(io.StringIO()):
        import species_advancement as sa
    sys.argv = argv
    return sa


def numbers(l3):
    out = []
    for m in re.finditer(r'\{([HMS])\}(\S+?)(?=\{|\s|$)|(\+\d+ ?ft)', l3):
        if m.group(3):
            out.append(m.group(3).replace('ft', ' ft') .replace('  ', ' ') + ' Speed')
        else:
            k, v = m.group(1), m.group(2)
            out.append({'H': f'Hit Die {v}', 'M': f'{v} Mana', 'S': f'{v} Stamina'}[k])
    return out


def clean(s):
    s = html.escape(s.strip(), quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)
    return re.sub(r'`(.+?)`', r'\1', s)


def table(lines, head):
    i = next(k for k, l in enumerate(lines) if l.startswith(head)) + 2
    rows = []
    while i < len(lines) and lines[i].startswith('|'):
        rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
        i += 1
    return rows


def assignments():
    lines = open(os.path.join(ROOT, 'canon', 'tile-assignments.md')).read().split('\n')
    tiles, cur = {}, None
    for r in table(lines, '| Tile | Name'):
        m = re.match(r'\*\*(\d+)(?:–(\d+))?\*\*', r[0])
        if m:  # a single tile, or a range such as 311–318 (every tile in it)
            lo, hi = int(m.group(1)), int(m.group(2) or m.group(1))
            cur = [str(n) for n in range(lo, hi + 1)]
        for t in cur:
            tiles.setdefault(t, []).append((r[2], r[3], r[4]))
    arcs, cur = {}, None
    for r in table(lines, '| Arc | Assigned'):
        m = re.match(r'\*\*(\w+)(?: (\d))?\*\*', r[0])
        if m:
            cur = (m.group(1), int(m.group(2)) if m.group(2) else None)
        arcs.setdefault(cur, []).append((r[1], r[2], r[3]))
    return tiles, arcs


def pair(sa, form, sep):
    """The colour's two abilities, from the ring-4 label ("Str +1 or Wis +1")."""
    return sep.join(x.split()[0] for x in sa.STAT_UP[form].split(' or '))


def part_html(parts):
    o = []
    for what, src, note in parts:
        meta = ' · '.join(x for x in (clean(src), clean(note)) if x)
        tag = '' if 'APPROVED' in note else ' <span class="rev">REVIEW</span>'
        o.append(f'<li>{clean(what)}{tag}' + (f'<div class="src">{meta}</div>' if meta else '') + '</li>')
    return '<ul>' + ''.join(o) + '</ul>'


def entry(title, facts, parts, cls=''):
    body = ''.join(f'<div class="f">{f}</div>' for f in facts)
    if parts:
        body += '<div class="lab">Parts</div>' + part_html(parts)
    return f'<div class="e {cls}"><div class="t">{title}</div>{body}</div>'


def build():
    g = grid()
    TILES, NUMBERS, BY = g['TILES'], g['NUMBERS'], g['BY_NUMBER']
    tparts, aparts = assignments()
    o = ['<h1>Skills grid tiles, by number</h1>']
    for num in sorted(NUMBERS.values(), key=int):
        h = BY[num]
        l1, l2, l3 = TILES.get(h, ('', '', ''))
        if num in KITS:
            name, req = l2, l1
        else:
            name, req = (l1 or ''), ''
        ab = ''  # the nearest ability misleads on seams; kits show their Req
        title = f'<span class="n">{num}</span> {html.escape(name) or "<span class=\'un\'>unnamed</span>"}'
        title += f' <span class="w">{" · ".join(x for x in (req, ab) if x)}</span>' if (req or ab) else ''
        facts = []
        nums = numbers(l3)
        if num != '0' and l2 and num not in KITS:
            nums.append(f'<b>{html.escape(l2)}</b>')
        if num == '0':
            nums = [f'<b>{html.escape(l2)}</b> (every character)']
        if nums:
            facts.append(' · '.join(nums))
        for k in KITS.get(num, []):
            facts.append(html.escape(k))
        if num in EXPERTISE:
            facts.append('<b>Expertise:</b> ' + EXPERTISE[num])
        if num in TECHNIQUES:
            facts.append('<b>Techniques:</b> ' + html.escape(TECHNIQUES[num]))
        # Rough points, for balancing (temporary; canon/diagrams/tile_points.py).
        if num != '0':
            tot, items, unscored = TP.tile_points(num, l2, l3, [p[0] for p in tparts.get(num, [])], numbers)
            facts.append('<span class="pts">Points ≈ ' + TP.fmt(tot) + '</span> <span class="ptsb">('
                         + ', '.join(f'{html.escape(k)} {TP.fmt(v)}' for k, v in items) + ')</span>')
            for u in unscored:
                print('unscored part on', num, ':', u[:60], file=sys.stderr)
            POINTS[num] = tot
        o.append(entry(title, facts, tparts.get(num), 'kit' if num in KITS else ''))

    sa = wheel()
    o.append('<h1 class="br">Species wheel arcs, by colour then ring</h1>')
    for form, name, sub, *_ in sa.cw.WHEEL:
        o.append(f'<h2>{html.escape(name)} <small>{html.escape(sub)}</small></h2>')
        loose = aparts.get((form, None))
        if loose:
            o.append(entry(f'<span class="n">{html.escape(name)}</span> <span class="w">several arcs, to settle</span>', [], loose))
        o.append(entry(f'<span class="n">{html.escape(name)} 0</span> base form',
                       [f'Saving throw proficiency: {pair(sa, form, " or ")}. Ability +1: {pair(sa, form, " or ")}.',
                        'No Hit Die, no pools, no prepared spell. '
                        'Its traits are in canon/brainstorm-species.md and canon/brainstorm-colour-wheel.md.'],
                       aparts.get((form, 0))))
        m, s = sa.POOL[form]
        for k in range(sa.FIRST, sa.LAST + 1):
            nums = [f'Hit Die {sa.HIT_DIE[form]}'] + ([f'{m} Mana'] if m else []) + ([f'{s} Stamina'] if s else [])
            pitems = [(sa.HIT_DIE[form], TP.HIT_DIE[sa.HIT_DIE[form]])] + ([(f'{m} Mana', m * TP.MANA), ('prepared spell', TP.PREPARED)] if m else []) + ([(f'{s} Stamina', s * TP.STAMINA)] if s else [])
            pitems += [('Prof. Up', TP.PROF_UP)] if k == 3 else [('Attack Up', TP.ATTACK_UP)] if k == 6 else [('ability +1', TP.ABILITY_UP)] if k == 4 else []
            for text, _, _ in aparts.get((form, k), []):
                hit = TP.part_points(TP.ARC_PARTS.get((form, k), {}), text)
                if hit:
                    pitems.append(hit)
                else:
                    print('unscored part on', form, k, ':', text[:60], file=sys.stderr)
            extra = sa.STAT_UP[form] if k == 4 else sa.FIXED.get(k, '')
            if extra:
                nums.append(f'<b>{html.escape(extra)}</b>')
            ptxt = ('<span class="pts">Points ≈ ' + TP.fmt(sum(v for _, v in pitems)) + '</span> <span class="ptsb">('
                    + ', '.join(f'{html.escape(str(k_))} {TP.fmt(v)}' for k_, v in pitems) + ')</span>')
            o.append(entry(f'<span class="n">{html.escape(name)} {k}</span>', [' · '.join(nums), ptxt], aparts.get((form, k))))
    return ''.join(o)


CSS = '''
@page{size:Letter;margin:.5in .55in .55in}
body{font:9pt/1.3 'DejaVu Serif',Georgia,serif;color:#1a1a1a}
h1{font:bold 15pt 'DejaVu Sans',sans-serif;margin:0 0 6pt;border-bottom:2px solid #333;padding-bottom:3pt}
h1.br{break-before:page}
.cols{columns:2;column-gap:.3in}
h2{font:bold 11.5pt 'DejaVu Sans',sans-serif;margin:8pt 0 2pt;color:#7a1f1f;break-after:avoid;column-span:none}
h2 small{font-weight:normal;font-style:italic;color:#666}
.e{break-inside:avoid;padding:3pt 0 4pt;border-bottom:.5pt solid #ccc}
.t{font:bold 9.6pt 'DejaVu Sans',sans-serif}
.n{color:#7a1f1f}
.un{font-weight:normal;color:#999;font-style:italic}
.w{font-weight:normal;color:#666;font-size:8pt}
.f{margin-top:1pt}
.lab{font:bold 7.5pt 'DejaVu Sans',sans-serif;color:#c46a12;margin-top:2pt;text-transform:uppercase;letter-spacing:.04em}
ul{margin:1pt 0 0 12pt;padding:0}
li{margin:1pt 0}
.src{font:italic 7.6pt 'DejaVu Serif',serif;color:#555}
.kit{background:#f4f1e8}
.rev{font:bold 6.6pt 'DejaVu Sans',sans-serif;color:#c46a12}
.pts{font:bold 8.2pt 'DejaVu Sans',sans-serif;color:#1d5c8a}
.ptsb{font:7.4pt 'DejaVu Sans',sans-serif;color:#557}
.lede{font-size:8.6pt;color:#444;margin:0 0 6pt}
'''


def main():
    from playwright.sync_api import sync_playwright
    body = build()
    lede = ('<p class="lede">Generated 2026-11-15 from skills_grid.py, species_advancement.py, canon/techniques.md, '
            'canon/brainstorm-progression.md, canon/decisions.md and canon/tile-assignments.md. PROPOSED design; every part is REVIEW. '
            '<b>Prof. Up:</b> Proficiency Bonus +1. <b>Attack Up:</b> one extra attack with the Attack action, or one extra cantrip damage die. '
            '<b>Points ≈</b> (blue): a rough balancing score on the Character Origins scale, REVIEW parts included; temporary (tile_points.py). <b>Upgrade rule:</b> an upgrade taken without its base tile gives nothing from that part. A starting kit gives everything listed; '
            'a later kit gives no save or skills.</p>')
    # Two columns: split the h1 sections so each heading spans the page.
    parts = body.split('<h1')
    doc_body = ''
    for p in parts[1:]:
        head, rest = p.split('</h1>', 1)
        doc_body += f'<h1{head}</h1>' + (lede if not doc_body else '') + f'<div class="cols">{rest}</div>'
    doc = f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{doc_body}</body></html>'
    tmp = os.path.join(HERE, '_details.html')
    open(tmp, 'w').write(doc)
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page()
        pg.goto('file://' + tmp)
        pg.pdf(path=OUT, format='Letter', print_background=True, display_header_footer=True,
               header_template='<span></span>',
               footer_template='<div style="font-size:7pt;width:100%;text-align:center;color:#888">Azhi progression: tile and arc details · '
                               '<span class="pageNumber"></span> / <span class="totalPages"></span></div>',
               margin={'top': '.5in', 'bottom': '.55in', 'left': '.55in', 'right': '.55in'})
        br.close()
    os.remove(tmp)
    print(OUT)


if __name__ == '__main__':
    main()
