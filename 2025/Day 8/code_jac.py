from itertools import combinations, combinations_with_replacement
import numpy as np

with open('input_jac.txt') as f:
    data = [tuple(map(int, d.strip().split(','))) for d in f.readlines()]
    
def get_distance(pair):
    a, b = pair
    x1, y1, z1 = a
    x2, y2, z2 = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5

PAIRS = 1000

combos = tuple(combinations(data, 2))
distances = {c: get_distance(c) for c in combos}
distances = sorted(distances.items(), key=lambda x: x[1])

circuits = []
for d in distances[:PAIRS]:
    new = True
    k = d[0]
    a, b = k
    if not circuits:
        # if empty add first circuit
        circuits.append(set(k))
    for c in circuits:
        if a in c or b in c:
            # add to existing circuit
            c.update(k)
            new = False
            break
    if new:    
        # add new circuit
        circuits.append(set(k))
            
def merge_circuits(circuits):
# combine overlapping circuits
    changed = True
    while changed:
        changed = False
        merged = []
        for c in circuits:
            for i, t in enumerate(merged):
                if c & t:
                    merged[i] |= c
                    changed = True
                    break
            else:
                merged.append(c)
        circuits = merged
    return circuits

largest = sorted([len(c) for c in merge_circuits(circuits)])
pt1 = np.product(np.array(largest[-3:]))
print(pt1)

circuits = []
for d in distances:
    new = True
    k = d[0]
    a, b = k
    if not circuits:
        # if empty add first circuit
        circuits.append(set(k))
    for c in circuits:
        if a in c or b in c:
            # add to existing circuit
            c.update(k)
            new = False
            break
    if new:    
        # add new circuit
        circuits.append(set(k))
    circuits = merge_circuits(circuits)
    if len(circuits) == 1 and len(circuits[0]) == PAIRS:
        print(a[0] * b[0])
        break
