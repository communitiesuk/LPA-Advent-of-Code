with open('input_jac.txt') as f:
    data = [d.strip() for d in f.readlines()]
    
data = [[d[0], int(d[1:])] for d in data]

start_position = 50
pt1 = 0

for direction, steps in data:
    if direction == 'L':
        directioniser = -1
    else:
        directioniser = 1
    start_position = (start_position + steps * directioniser) % 100
    if start_position == 0:
        pt1 += 1
        
print(pt1)

pt2 = 0
start_position = 50

for direction, steps in data:
    if direction == 'L':
        directioniser = -1
    else:
        directioniser = 1
    end_position = (start_position + steps * directioniser) % 100
    if start_position == end_position:
        pt2 += steps // 100
    elif start_position == 0 and end_position != 0:
        pt2 += steps // 100
    elif start_position != 0 and end_position == 0:
        pt2 += steps // 100 + 1
    elif start_position != 0 and end_position != 0:
        pt2 += steps // 100
        if direction == 'L' and end_position > start_position:
            pt2 += 1
        elif direction == 'R' and end_position < start_position:
            pt2 += 1
    # print(f'{direction=},{steps=},{start_position=},{end_position=},{pt2=}')
    start_position = end_position

print(pt2)