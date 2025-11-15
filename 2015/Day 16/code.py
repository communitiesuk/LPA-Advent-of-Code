import re

with open('input_jac.txt') as f:
    data = [d.strip() for d in f.readlines()]

with open('result.txt') as f:
    result = [d.strip() for d in f.readlines()]

result = {r.split(':')[0]: int(r.split(':')[1]) for r in result}

for d in data:
    pt1 = True
    pt2 = True
    values = list(map(int, re.findall(': (\d+)', d)))
    keys = re.findall('(\w*):', d)
    id = int(keys[0])
    aunty = {k:v for k,v in zip( keys[1:], values)}
    for k, v in aunty.items():
        if result[k] != v:
            pt1 = False
        if k in ['cats', 'trees']:
            if v <= result[k]:
                pt2 = False
        elif k in ['pomeranians', 'goldfish']:
            if v >= result[k]:
                pt2 = False
        else:
            if v != result[k]:
                pt2 = False
    if pt1:
        print(id)
    if pt2:
        print(id)