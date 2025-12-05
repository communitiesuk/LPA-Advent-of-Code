import numpy as np

with open('input_jac.txt') as f:
    data = np.array([list(d.strip()) for d in f.readlines()])
    
def get_neighbours(row, col, data):
    moves = [-1, 0, 1]
    neighbours = [(row + i, col + j) for i in moves for j in moves]
    neighbours = ([(r, c) for r, c in neighbours if (row, col) != (r, c) and 
                   r >= 0 and r < data.shape[0] and c >= 0 and c < data.shape[1]])
    return neighbours
    
pt1 = 0
for row in range(data.shape[0]):
    for col in range(data.shape[1]):
        if data[row, col] == '@':
            count = 0
            neighbours = get_neighbours(row, col, data)
            for n in neighbours:
                if data[n] == '@':
                    count += 1
            if count < 4:
                pt1 += 1

pt2 = 0
removed = 1
while removed != 0:
    temp_data = data
    removed = 0
    for row in range(data.shape[0]):
        for col in range(data.shape[1]):
            if data[row, col] == '@':
                count = 0
                neighbours = get_neighbours(row, col, data)
                for n in neighbours:
                    if data[n] == '@':
                        count += 1
                if count < 4:
                    removed += 1
                    temp_data[row, col] = '.'
    pt2 += removed
    data = temp_data
                
print(pt1)
print(pt2)
    
