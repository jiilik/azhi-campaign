"""Pull SRD 5.2.1 spell entries verbatim from srd/07-spells (2026-11-13)."""
import os, re
SRD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'srd', '07-spells')


def spell(name):
    f = os.path.join(SRD, f'spells-{name[0].lower()}.md')
    t = open(f).read()
    m = re.search(rf'^#### {re.escape(name)}\n(.*?)(?=^#{{2,4}} |\Z)', t, re.M | re.S)
    assert m, name
    return m.group(1).strip()


BOOKS = {
    'primer': ("The Junior Wizard's Primer", ['Magic Missile', 'Shield', 'Mage Armor', 'Burning Hands', 'Thunderwave', 'Chromatic Orb']),
    'summons': ('Selected Summons for Novices', ['Find Familiar', 'Unseen Servant', 'Silent Image', 'Fog Cloud', 'Color Spray', 'Floating Disk']),
    'alchemy': ('Practical Alchemy', ['Detect Magic', 'Identify', 'Illusory Script', 'False Life', 'Sleep', 'Grease']),
}

if __name__ == '__main__':
    for k, (title, names) in BOOKS.items():
        words = 0
        for n in names:
            s = spell(n)
            words += len(s.split())
            if '|' in s or re.search(r'^\s*[-*] ', s, re.M):
                print('  structure in', n)
        print(title, words)
