with open('input_jac.txt') as f:
    data = [d.strip('\n') for d in f.readlines()]

import numpy as np
    
numbers = np.array([list(map(int, d.split())) for d in data[:-1]], dtype=np.int64)
operations = [d for d in data[-1].split()]
    
pt1 = 0
for col, op in zip(range(numbers.shape[1]), operations):
    if op == "*":
        pt1 += np.prod(numbers[:, col])
    else:
        pt1 += np.sum(numbers[:, col])
        
reversed_numbers = [d[::-1] for d in data[:-1]]
reversed_operations = operations[::-1]

pt2 = 0
nums = []
count = 0
for a, b, c, d in zip(reversed_numbers[0], reversed_numbers[1], reversed_numbers[2], reversed_numbers[3]):
    if (a == ' ' and b == ' ' and c == ' ' and d == ' '):
        op = reversed_operations.pop(0)
        count += 1
        if op == '*':
            pt2 += np.prod(np.array(nums), dtype=np.int64)
        else:
            pt2 += np.sum(np.array(nums), dtype=np.int64)
        print(nums)
        nums = []
    elif (a == reversed_numbers[0][-1] and b == reversed_numbers[1][-1] and c == reversed_numbers[2][-1] and d == reversed_numbers[3][-1]):
        nums.append(int(a+b+c+d))
        op = reversed_operations.pop(0)
        count += 1
        if op == '*':
            pt2 += np.prod(np.array(nums), dtype=np.int64)
        else:
            pt2 += np.sum(np.array(nums), dtype=np.int64)
        nums = []
    else:
        nums.append(int(a+b+c+d))
        
print(pt1)
print(pt2)