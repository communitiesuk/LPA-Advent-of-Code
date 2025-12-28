from itertools import combinations
from shapely.geometry import Polygon

with open('input_jac.txt') as f:
    data = [tuple(map(int, d.strip().split(','))) for d in f.readlines()]
    
def get_size(combo):
    a, b = combo
    x1, y1 = a
    x2, y2 = b
    size = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    return size

combos = combinations(data, 2)
combos = sorted(combos, key=get_size, reverse=True)
outer = Polygon(data)

print(get_size(combos[0]))

for c in combos:
    a, b = c
    x1, y1 = a
    x2, y2 = b
    inner = Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])
    if inner.within(outer):
        print(get_size(c))
        break
