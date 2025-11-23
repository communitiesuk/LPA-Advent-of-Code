with open('input_jac.txt') as f:
    data = [list(d.strip()) for d in f.readlines()]

import numpy as np
data = np.array(data)

STEPS = 100

def get_neighbours(row, col, grid):
    moves = [-1, 0, 1]
    neighbours = [(row + r, col + c) for r in moves for c in moves]
    neighbours = [neighbour for neighbour in neighbours if 0 <= neighbour[0] < grid.shape[1] 
                  and 0 <= neighbour[1] < grid.shape[1] and neighbour != (row, col)]
    lights_on = sum([1 if grid[neighbour] == '#' else 0 for neighbour in neighbours])
    return lights_on

# for s in range(STEPS):
#     temp_data = data.copy()
#     for row in range(100):
#         for col in range(100):
#             old_val = data[row, col]
#             lights = get_neighbours(row, col, data)
#             if old_val == '#':
#                 if lights == 2 or lights == 3:
#                     new_val = '#'
#                 else:
#                     new_val = '.'
#             else:
#                 if lights == 3:
#                     new_val = '#'
#                 else:
#                     new_val = '.'
#             temp_data[row, col] = new_val
#     data = temp_data

for s in range(STEPS):
    temp_data = data.copy()
    for row in range(100):
        for col in range(100):
            old_val = data[row, col]
            lights = get_neighbours(row, col, data)
            if (row, col) in [(0, 0), (0, 99), (99, 0), (99, 99)]:
                new_val = '#'
            elif old_val == '#':
                if lights == 2 or lights == 3:
                    new_val = '#'
                else:
                    new_val = '.'
            else:
                if lights == 3:
                    new_val = '#'
                else:
                    new_val = '.'
            temp_data[row, col] = new_val
    data = temp_data
    
print(np.sum(data == '#'))