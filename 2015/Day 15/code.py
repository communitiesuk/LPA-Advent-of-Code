with open('input_jac.txt') as f:
    data = [d.strip() for d in f.readlines()]
    
import re
import numpy as np

data = np.array([list(map(int, re.findall('-?\d', d))) for d in data])

limit = 100
pt1 = 0
pt2 = 0
for a in range(limit):
    for b in range(limit - a):
        for c in range(limit - a - b):
            d = limit - a
            d = limit - a - b - c
            weights = np.array([a, b, c, d]).reshape(-1, 1)
            weighted_data = data * weights
            summed_data = np.sum(weighted_data, axis=0)
            zeroed_data = np.where(summed_data < 0, 0, summed_data)
            score = np.product(zeroed_data[:-1])
            if score > pt1:
                pt1 = score
            if summed_data[-1] == 500 and score > pt2:
                pt2 = score

print(pt1)
print(pt2)

