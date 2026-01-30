from itertools import product
from math import ceil

with open('shop.txt') as f:
    data = [d.strip() for d in f.readlines()]
    
data = [d.replace(' +', '_') for d in data]
weapons = data[1:6]
armour = data[8:13]
rings = data[15:22]

weapons = {row.split()[0].lower(): {'cost': int(row.split()[1]),
                                   'damage': int(row.split()[2]),
                                   'armour': int(row.split()[3])} for row in weapons}

armour = {row.split()[0].lower(): {'cost': int(row.split()[1]),
                                   'damage': int(row.split()[2]),
                                   'armour': int(row.split()[3])} for row in armour}

rings = {row.split()[0].lower(): {'cost': int(row.split()[1]),
                                   'damage': int(row.split()[2]),
                                   'armour': int(row.split()[3])} for row in rings}

shop = {**weapons, **armour, **rings}

cpu = {'hp': 100, 'damage': 8, 'armour': 2}
    
weapons_armour_2_rings = list(product(weapons.keys(), armour.keys(), rings.keys(), rings.keys()))
weapons_armour_2_rings = [lst for lst in weapons_armour_2_rings if len(lst) == len(set(lst))]
weapons_armour_rings = list(product(weapons.keys(), armour.keys(), rings.keys()))
weapons_armour = list(product(weapons.keys(), armour.keys()))
weapons_rings = list(product(weapons.keys(),rings.keys()))
weapons_2_rings = list(product(weapons.keys(), rings.keys(), rings.keys()))
weapons_2_rings = [lst for lst in weapons_2_rings if len(lst) == len(set(lst))]
just_weapons = [(k,) for k,v in weapons.items()]
everything = weapons_armour_rings + weapons_armour + weapons_rings + just_weapons + weapons_armour_2_rings + weapons_2_rings
cost_of_everything = {e: sum([shop[item]['cost'] for item in e]) for e in everything}
cost_of_everything = dict(sorted(cost_of_everything.items(), key=lambda x: x[1]))
    
for selection in cost_of_everything:
    player = {'hp': 100, 'damage': 0, 'armour': 0}
    for item in selection:
        player['damage'] += shop[item]['damage']
        player['armour'] += shop[item]['armour']
    player_survives_rounds = ceil(player['hp'] / max(1, cpu['damage'] - player['armour']))
    cpu_survives_rounds = ceil(cpu['hp'] / max(1, player['damage'] - cpu['armour']))
    if player_survives_rounds >= cpu_survives_rounds:
        print(cost_of_everything[selection])
        break

for selection in list(reversed(cost_of_everything)):
    player = {'hp': 100, 'damage': 0, 'armour': 0}
    for item in selection:
        player['damage'] += shop[item]['damage']
        player['armour'] += shop[item]['armour']
    player_survives_rounds = ceil(player['hp'] / max(1, cpu['damage'] - player['armour']))
    cpu_survives_rounds = ceil(cpu['hp'] / max(1, player['damage'] - cpu['armour']))
    if player_survives_rounds < cpu_survives_rounds:
        print(cost_of_everything[selection])
        break