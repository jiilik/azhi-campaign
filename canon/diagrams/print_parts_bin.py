"""A printable, pencil-friendly listing of the parts bin (2026-11-14).

Reads canon/parts-bin.md (classes and feats) and canon/parts-bin-techniques.md
(techniques) and writes canon/diagrams/parts-bin-print.pdf: one entry per part,
with its source (SRD 5.2.1, or the 2024 PHB from memory, or 4th Edition ideas in
Claude's own words), the level it comes from, its points, and a ruled line for
notes. Run: python3 canon/diagrams/print_parts_bin.py
"""
import html
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
CANON = os.path.join(HERE, '..')
OUT = os.path.join(HERE, 'parts-bin-print.pdf')

SRD = 'SRD 5.2.1'
PHB = 'PHB 2024, from memory'
WARLORD = '4th Edition warlord, in Claude’s own words'

# Feat levels (SRD 5.2.1 categories; PHB categories from memory)
ORIGIN = {'Alert', 'Crafter', 'Healer', 'Lucky', 'Magic Initiate', 'Musician', 'Savage Attacker', 'Skilled',
          'Tavern Brawler', 'Tough'}
STYLES = {'Archery', 'Defense', 'Great Weapon Fighting', 'Two-Weapon Fighting', 'Blind Fighting', 'Dueling',
          'Interception', 'Protection', 'Thrown Weapon Fighting', 'Unarmed Fighting', 'Blessed Warrior',
          'Druidic Warrior'}


def feat_level(name):
    if 'Boon' in name or 'epic' in name.lower():
        return 'Epic Boon feat, level 19+'
    if name in ORIGIN:
        return 'Origin feat, level 1'
    if name in STYLES:
        return 'Fighting Style feat (needs a Fighting Style feature)'
    return 'General feat, level 4+'


MONK_LEVELS = [('Martial Arts', 1), ('Flurry', 2), ('Patient Defense', 2), ('Step of the Wind', 2),
               ('Uncanny Metabolism', 2), ('Deflect Attacks', 3), ('Slow Fall', 4), ('Stunning Strike', 5),
               ('Disciplined Survivor', 14), ('Superior Defense', 18), ('Open Hand Technique', '3 (Open Hand)'),
               ('Wholeness of Body', '6 (Open Hand)'), ('Quivering Palm', '17 (Open Hand)'),
               ('Warrior of Mercy', '3+ (subclass)'), ('Warrior of Shadow', '3+ (subclass)'),
               ('Warrior of the Elements', '3+ (subclass)')]
BARD_LEVELS = [('Bardic Inspiration', 1), ('Cutting Words', '3 (College of Lore)'), ('Countercharm', 7),
               ('Font', '5; Superior Inspiration 18'), ('Jack of All Trades', 2)]


def clean(s):
    s = s.strip()
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)
    s = re.sub(r'`(.+?)`', r'\1', s)
    return s


def rows(lines, i):
    """Read a markdown table starting at line i; return (header, rows, next index)."""
    head = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    i += 2
    out = []
    while i < len(lines) and lines[i].startswith('|'):
        out.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
        i += 1
    return head, out, i


def entry(part, meta, note=''):
    m = ' · '.join(f'<span>{x}</span>' for x in meta if x)
    n = f'<div class="note">{note}</div>' if note else ''
    return f'<div class="e"><div class="p">{part}</div><div class="m">{m}</div>{n}<div class="rule"></div></div>'


def classes_and_feats():
    lines = open(os.path.join(CANON, 'parts-bin.md')).read().split('\n')
    o, i = [], 0
    section, cls, src = None, None, SRD
    count = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith('## '):
            section = ln[3:].strip()
            if section.startswith('2.'):
                o.append('<h1>Classes</h1><p class="lede">The SRD’s twelve classes and their SRD subclasses, plus the other 2024 '
                         '<i>Player’s Handbook</i> subclasses (summaries written from memory; check the book before relying on one). '
                         '<b>Level</b> is the class level the part arrives at. <b>Tree</b>: E experience, P phasing, ? unsure.</p>')
            elif section.startswith('4.'):
                o.append('<h1 class="br">Feats</h1><p class="lede">Every SRD 5.2.1 and 2024 <i>Player’s Handbook</i> feat, broken into parts '
                         'and grouped by what the parts do. SRD parts quote the SRD; PHB parts are summaries written from memory. <b>Level</b> is the '
                         'feat’s category and prerequisite level.</p>')
            i += 1
            continue
        if section and section.startswith('2.') and ln.startswith('### '):
            cls = ln[4:].strip()
            src = SRD
            o.append(f'<h2>{clean(cls)}</h2>')
        elif section and section.startswith('2.') and ln.startswith('**Starting kit'):
            o.append('<h3>Starting kit</h3>')
            m = re.match(r'\*\*Starting kit \(entry node\): ([\d.]+) points\.\*\* (.*)', ln)
            o.append(entry(clean(m.group(2)), [SRD, f'{cls} level 1', f'{m.group(1)} pts'] if m else [SRD]))
            count += 1
        elif section and section.startswith('2.') and re.match(r'\*\*.+\*\* \((SRD|PHB) subclass', ln):
            name = re.match(r'\*\*(.+?)\*\*', ln).group(1)
            src = SRD if '(SRD subclass' in ln else PHB
            o.append(f'<h3>{clean(name)} <small>({"SRD subclass" if src == SRD else "PHB subclass, from memory"})</small></h3>')
        elif section and section.startswith('4.') and ln.startswith('### '):
            o.append(f'<h2>{clean(ln[4:].split(" ", 1)[1])}</h2>')
        if ln.startswith('| Level | Part') and section.startswith('2.'):
            if not o[-1].startswith('<h3>'):
                o.append(f'<h3>{clean(cls)} <small>(class features, SRD)</small></h3>')
            _, rs, i = rows(lines, i)
            for r in rs:
                lvl, part, pts, tree, note = (r + [''] * 5)[:5]
                o.append(entry(clean(part), [src, f'{cls} level {lvl}', f'{clean(pts)} pts', f'Tree {tree}'], clean(note)))
                count += 1
            continue
        if ln.startswith('| Part | Feat'):
            _, rs, i = rows(lines, i)
            for r in rs:
                part, feat, used, pts = (r + [''] * 4)[:4]
                names = re.findall(r"([A-Z][A-Za-z' -]+?) \(([SP](?:, [SP])?)(?:, epic)?\)", feat)
                metas = []
                for (nm, s) in names:
                    nm = nm.strip().split('. ')[-1].strip('"')
                    nm = re.sub(r'^(most General feats|every Epic Boon)$', r'\1', nm)
                    srcs = ' and '.join(SRD if x.strip() == 'S' else PHB for x in s.split(','))
                    metas.append(f'<b>{html.escape(nm)}</b>: {srcs}; {feat_level(nm)}')
                if not metas:
                    metas = [clean(feat)]
                note = f'In use: {clean(used)}' if used else ''
                o.append(entry(clean(part), metas + [f'{clean(pts)} pts'], note))
                count += 1
            continue
        i += 1
    return ''.join(o), count


def level_for(part, table):
    for key, lv in table:
        if key in part:
            return lv
    return '—'


def techniques():
    lines = open(os.path.join(CANON, 'parts-bin-techniques.md')).read().split('\n')
    o = ['<h1 class="br">Techniques</h1><p class="lede">Parts for the stamina system. <b>Trigger</b>: A action, BA Bonus Action, R Reaction, Hit a rider on a hit. '
         '<b>Cost</b>: at-will or SP (stamina). <b>Home</b>: where on the skills grid it might live. These are tagged with where they were proposed in November; '
         'the placed techniques are in <i>canon/techniques.md</i>.</p>']
    i, section, count = 0, '', 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith('## '):
            section = ln[3:].strip()
            if section[0] in '2345':
                o.append(f'<h2>{clean(section.split(" ", 1)[1])}</h2>')
            i += 1
            continue
        if ln.startswith('| Part | Trigger') and section[0] in '2345':
            _, rs, i = rows(lines, i)
            for r in rs:
                part, trig, cost, tgt, home, pts = (r + [''] * 6)[:6]
                note = r[6] if len(r) > 6 else ''
                if section.startswith('2.'):
                    src = PHB if '(PHB' in part else SRD
                    lv = f'Monk level {level_for(part, MONK_LEVELS)}'
                elif section.startswith('3.'):
                    src, lv = PHB, 'Battle Master, Fighter level 3+'
                elif section.startswith('4.'):
                    src, lv = WARLORD, 'no 5e level'
                else:
                    src, lv = SRD, f'Bard level {level_for(part, BARD_LEVELS)}'
                o.append(entry(clean(part), [src, lv, f'{trig} · {cost} · {tgt}', f'Home: {clean(home)}', f'{pts} pts'], clean(note)))
                count += 1
            continue
        if ln.startswith('| Level (SP)'):
            o.append('<h3>Bard spells that could become techniques <small>(SP cost = the spell’s mana price)</small></h3>')
            _, rs, i = rows(lines, i)
            for r in rs:
                lv, ref, magic = (r + [''] * 3)[:3]
                o.append(entry(f'<b>Could become techniques:</b> {clean(ref)}', [SRD, f'Bard spell level {clean(lv)}'],
                               f'Stays magic: {clean(magic)}'))
                count += 1
            continue
        i += 1
    return ''.join(o), count


CSS = '''
@page{size:Letter;margin:.55in .6in .6in}
body{font:10pt/1.32 'DejaVu Serif',Georgia,serif;color:#1a1a1a}
h1{font:bold 17pt 'DejaVu Sans',sans-serif;margin:0 0 4pt;border-bottom:2px solid #333;padding-bottom:3pt}
h1.br{break-before:page}
h2{font:bold 12.5pt 'DejaVu Sans',sans-serif;margin:16pt 0 4pt;color:#7a1f1f;break-after:avoid}
h3{font:bold 10.5pt 'DejaVu Sans',sans-serif;margin:10pt 0 3pt;color:#333;break-after:avoid}
h3 small{font-weight:normal;color:#666}
.lede{font-size:9pt;color:#444;margin:0 0 8pt}
.e{break-inside:avoid;padding:4pt 0 0}
.p{font-size:10pt}
.m{font:8.2pt 'DejaVu Sans',sans-serif;color:#555;margin-top:1pt}
.m span:first-child{color:#7a1f1f}
.note{font:italic 8.6pt 'DejaVu Serif',serif;color:#444;margin-top:1pt}
.rule{height:20pt;border-bottom:.6pt solid #bbb}
.title{font:bold 24pt 'DejaVu Sans',sans-serif;margin:0}
.sub{font-size:10pt;color:#555;margin:2pt 0 10pt}
.key{font-size:8.8pt;border:1px solid #bbb;padding:6pt 8pt;margin-bottom:10pt}
'''


def main():
    from playwright.sync_api import sync_playwright
    a, n1 = classes_and_feats()
    b, n2 = techniques()
    head = (f'<p class="title">Azhi: the Parts Bin</p><p class="sub">Every class, subclass, feat and technique part, for review with a pencil. '
            f'{n1 + n2} entries. Generated 2026-11-14 from canon/parts-bin.md and canon/parts-bin-techniques.md (PROPOSED, tentative).</p>'
            f'<div class="key"><b>Source</b> (in red on each entry): <b>{SRD}</b> means the rules text is in our SRD files (CC BY 4.0); '
            f'<b>{PHB}</b> means a summary Claude wrote from memory of the 2024 <i>Player’s Handbook</i>, not checked against the book; '
            f'<b>{WARLORD}</b> means ideas from a non-open source, described generically. <b>Points</b> are best guesses on the Character Origins scale '
            f'(+1 to an ability = 4).</div>')
    doc = f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{head}{a}{b}</body></html>'
    tmp = os.path.join(HERE, '_parts_bin.html')
    open(tmp, 'w').write(doc)
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page()
        pg.goto('file://' + tmp)
        pg.pdf(path=OUT, format='Letter', print_background=True, display_header_footer=True,
               header_template='<span></span>',
               footer_template='<div style="font-size:7pt;width:100%;text-align:center;color:#888">Azhi parts bin · '
                               '<span class="pageNumber"></span> / <span class="totalPages"></span></div>',
               margin={'top': '.55in', 'bottom': '.6in', 'left': '.6in', 'right': '.6in'})
        br.close()
    os.remove(tmp)
    print(OUT, n1 + n2, 'entries')


if __name__ == '__main__':
    main()
