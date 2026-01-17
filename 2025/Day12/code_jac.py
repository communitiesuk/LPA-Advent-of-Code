import numpy as np

with open('input_jac.txt') as f:
    data = [d.strip() for d in f.readlines()]
    
shapes = [np.where(np.array([list(row) for row in shape]) == "#", 1, 0) for shape in [data[x * 5 + 1: x * 5 + 4] for x in range(6)]]
sizes = [np.sum(s) for s in shapes]
dimensions = [[int(x) for x in d.split(": ")[0].split("x")] for d in data[30:]]
numbers = [[int(x) for x in d.split(": ")[1].split(" ")] for d in data[30:]]
    
pt1 = 0
for d, n in zip(dimensions, numbers):
    grid_size = d[0] * d[1]
    presents_size = sum([_ * s for _, s in zip(n, sizes)])
    if presents_size < grid_size:
        pt1 += 1
        
print(pt1)