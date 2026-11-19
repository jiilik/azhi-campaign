"""Rough points per tile and arc, for balancing (Troy, 2026-11-15; temporary).

The Character Origins scale (+1 to an ability = 4), as extended in
canon/parts-bin.md §1. print_details.py prints each tile's total with its
breakdown. Every REVIEW part counts, since most will be approved or reworked.
Remove this file (and its use in print_details.py) when balancing is done.

Base values (Claude, 2026-11-15; PROPOSED):
  Hit Die: d4 -4, d6 0, d8 4, d10 8, d12 12 (per step above d6, parts bin)
  Stamina 1 a point; Mana 2 a point (Troy, 2026-11-07)
  Prepared spell: 1 for each tile with Mana ("four prepared spells about 4")
  Prof. Up 8 (Claude's guess: +1 to every proficient roll and DC, like +2 to abilities)
  Attack Up 16 (the parts bin's first Extra Attack)
  Ability +1: 4; Expertise 2.5 a skill; a technique 2 (an at-will)
Part values come from canon/parts-bin.md where the part is listed; new or
reworked parts are Claude's estimates.
"""

HIT_DIE = {'d4': -4, 'd6': 0, 'd8': 4, 'd10': 8, 'd12': 12, 'd20': 28}  # 4 points per +1 average
# A second Hit Die on one tile (the Juggernaut line): 4 points per point of its average.
EXTRA_HIT_DIE = {'d4': 10, 'd6': 14, 'd8': 18}
STAMINA, MANA, PREPARED = 1, 2, 1
PROF_UP, ATTACK_UP, ABILITY_UP, EXPERTISE, TECHNIQUE = 8, 16, 4, 2.5, 2

# Starting kits, whole (a later kit is meant to be worth about one tile).
# canon/brainstorm-progression.md, "The kits"; values from the parts bin.
KIT_PARTS = {
    '11': [('4 techniques', 8), ('save', 4), ('2 skills', 3), ('light armour', 2), ('1 Weapon Mastery', 3)],
    '12': [('3 techniques', 6), ('+5 ft Speed', 1.5), ('Fighting Style', 5), ('save', 4), ('2 skills', 3),
           ('light armour', 2), ('Finesse, Light and ranged weapons', 2), ('2 Weapon Masteries', 4)],
    '13': [('Fighting Style', 5), ('save', 4), ('1 skill', 1.5), ('light and medium armour, Shields', 6),
           ('martial weapons', 3.5), ('3 Weapon Masteries', 5)],
    '14': [('Fighting Style', 5), ('Second Wind', 5), ('save', 4), ('1 skill', 1.5),
           ('light and medium armour, Shields', 6), ('martial weapons', 3.5), ('1 Weapon Mastery', 3)],
    '15': [('2 cantrips', 4), ('4 prepared spells', 4), ('save', 4), ('2 skills', 3), ('light armour', 2)],
    '16': [('3 cantrips', 6), ('4 prepared spells', 4), ('rituals', 2), ('spellbook', 3), ('save', 4), ('1 skill', 1.5)],
}

# Parts on tiles: a phrase from the part's text -> points. Matched in order.
PARTS = {
    '201': {'Bardic Inspiration': 8, 'Mantle of Inspiration': 6},
    '202': {'Charm Person': 4, 'Fast Hands': 5},
    '203': {'Deft Explorer': 4},
    '204': {'Gambits': 12},
    '205': {'Action Surge': 9},
    '206': {'Smite': 6},
    '616': {'d12': 3},
    '412': {'Planted': 3, 'Unshakeable': 3},
    '514': {'Second breath': 4, 'Concentration': 3},
    '614': {'Legendary presence': 6},
    '618': {'saving throw': 4, 'Last stand': 6},
    '619': {'d20 Hit Die': 0, 'Chain Taunt': 4},
    '207': {'Unarmored Defense': 4, 'Danger Sense': 3, 'Rope-a-dope': 4},
    '208': {'Vital Reserve': 4, 'Warrior of the Gods': 5, 'Warding Flare': 5},
    '209': {'Light Domain': 6, 'Radiance of the Dawn': 5, 'Otherworldly Glamour': 3, 'Mystic Wanderer': 4},
    '301': {'Guided Strike': 4},
    '302': {'Inspiring Movement': 4},
    '303': {'Unarmored Defense': 4, 'Sneak Attack': 6, 'Hide': 2},
    '304': {'Favored Enemy': 6},
    '305': {'Grappling': 3, 'Uncanny Dodge': 6, 'Flurry of Blows': 4},
    '406': {'Martial Arts': 10},
    '306': {'Weapon Mastery': 2, 'Remarkable Athlete': 3, 'Retaliation': 5},
    '307': {'Weapon Mastery': 1},
    '308': {'Intimidating Presence': 6, 'Improved Critical': 4, 'Brutal Strike': 6, 'with AC': 3},
    '309': {'on AC': 4},
    '310': {'Taunt': 5, 'Hit Dice': 0},
    '413': {'Hit Dice': 0, 'Powerful Build': 2},
    '516': {'Hit Dice': 0, 'Colossal': 5},
    '312': {'Animal Speaker': 2, 'Life Domain': 6, 'Wild Shape': 10, 'Wild Companion': 3, 'Primal Companion': 12},
    '317': {'Mystic Reinforcements': 4},
    '318': {'Beguiling Magic': 6, 'Dreadful Strikes': 5},
    '403': {'Invisibility': 4},
    '404': {'Dread Ambusher': 6},
    '405': {'Fast Movement': 3, 'Climb Speed': 3},
    '407': {'Improved Gambits': 3, 'Stunning Strike': 8},
    '410': {'Take the hit': 5, 'Heavy armour': 4},
    '411': {'d10': 4},
    '415': {'Vital Reserve': 2, 'Improved Warding Flare': 3},
    '418': {'teleport': 5},
    '419': {'Magical Secrets': 6},
    '423': {'Countercharm': 2, 'Mantle of Majesty': 6},
    '505': {'Jumper': 1},
    '506': {'Fighting Style': 5, "Hunter's Lore": 2, "Hunter's Prey": 5},
    '507': {'Open Hand Technique': 6, 'Defensive Tactics': 4},
    '509': {'Resistance': 3},
    '511': {'Fighting Style': 5},
    '512': {'Heroic Warrior': 6},
    '513': {'Exhaustion': 4, 'Reckless Attack': 6},
    '515': {'Resistance': 3, 'damage reduction': 4},
    '518': {'hit points to Mana': 4},
    '519': {'Blessed Healer': 3},
    '520': {'Exceptional Training': 3},
    '522': {'forced teleportation': 4},
    '525': {'Shatter': 2},
    '601': {'War Cry': 6, 'Superior Inspiration': 3},
    '602': {'Leading Evasion': 5},
    '604': {'Hypnotic Pattern': 4, "Nature's Veil": 5, 'Wisdom saving throw': 4},
    '605': {'Unarmored Movement': 3, 'Sneak Attack improves': 8, 'Cunning Strike': 7},
    '607': {'Know Your Enemy': 1, 'Tireless': 4, 'Relentless Hunter': 2},
    '608': {'Acrobatic Movement': 2},
    '609': {'Improved grappling': 3},
    '610': {'Ultimate Gambits': 3},
    '611': {'Studied Attacks': 3, 'Fighting Styles': 10},
    '613': {'Weapon Mastery': 1},
    '615': {'Superior Critical': 3, 'Improved Brutal Strike': 3},
    '617': {'Bulwark of Force': 3, 'adjacent ally': 4},
    '620': {'Resistance': 3, 'forcibly phased': 6},
    '622': {'Vital Reserve': 2},
    '623': {'Wild Shape forms grow': 6, 'Supreme Healing': 4, 'Beast Spells': 3},
    '624': {'Resistance': 3},
    '625': {'Divine Intervention': 8},
    '626': {'Misty Wanderer': 4},
    '628': {'Magical Secrets': 6},
    '630': {'feeds back': 4},
    '634': {'Guarded Mind': 4},
}
CANTRIP_ROW = ('One new cantrip', 2)   # the 311–318 row
# Techniques taught on non-kit tiles (canon/techniques.md); kits count theirs above,
# and 305's Uncanny Dodge is scored as a part.
TECHNIQUE_COUNT = {'201': 4, '202': 2, '304': 3, '405': 1, '508': 1}
EXPERTISE_SKILLS = {'202': 2, '403': 1, '604': 1, '210': 1}


def fmt(x):
    return str(int(x)) if x == int(x) else str(x)


def tile_points(num, l2, l3, parts, numbers_fn):
    """(total, breakdown list, unscored parts) for one grid tile."""
    import re
    items = []
    for m in re.finditer(r'\{([HMS])\}(\d+|d\d+(?:\+d\d+)?)', l3):
        k, v = m.groups()
        if k == 'H':
            main, _, extra = v.partition('+')
            items.append((f'{main}', HIT_DIE[main]))
            if extra:
                items.append((f'extra {extra}', EXTRA_HIT_DIE[extra]))
        elif k == 'S':
            items.append((f'{v} Stamina', int(v) * STAMINA))
        else:
            items.append((f'{v} Mana', int(v) * MANA))
            if num not in KIT_PARTS:
                items.append(('prepared spell', PREPARED))
    if l2 == 'Prof. Up':
        items.append(('Prof. Up', PROF_UP))
    elif l2 == 'Attack Up':
        items.append(('Attack Up', ATTACK_UP))
    elif re.match(r'(Str|Dex|Con|Int|Wis|Cha) \+1', l2 or ''):
        items.append((l2, ABILITY_UP))
    items += KIT_PARTS.get(num, [])
    if num in TECHNIQUE_COUNT:
        n = TECHNIQUE_COUNT[num]
        items.append((f'{n} technique' + ('s' if n > 1 else ''), n * TECHNIQUE))
    if num in EXPERTISE_SKILLS:
        n = EXPERTISE_SKILLS[num]
        items.append((f'Expertise ×{n}', n * EXPERTISE))
    unscored = []
    for text in parts:
        if text.startswith('*(empty'):
            continue
        hit = part_points(PARTS.get(num, {}), text)
        if hit:
            items.append(hit)
        else:
            unscored.append(text)
    return sum(v for _, v in items), items, unscored

# Species-wheel arcs: (colour, ring) -> {phrase: points}.
ARC_PARTS = {
    ('Brown', 1): {'Rage': 12}, ('Brown', 3): {'Rage of the Wilds': 8}, ('Brown', 5): {'Relentless Rage': 6},
    ('Grey', 3): {'Travel along the Tree': 6}, ('Green', 1): {'Uncanny Metabolism': 3},
    ('White', 1): {'Channel Divinity': 8}, ('White', 6): {'Divine Wings': 10, 'Blessed Strikes': 5},
}


def part_points(table, text):
    """Points for one part, matched by phrase; None if unscored."""
    for phrase, pts in table.items():
        if phrase.lower() in text.lower():
            return phrase, pts
    if CANTRIP_ROW[0].lower() in text.lower():
        return CANTRIP_ROW
    return None
