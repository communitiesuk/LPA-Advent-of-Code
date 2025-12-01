with open('input_jac.txt') as f:
    data = [d.strip() for d in f.readlines()]
    
data = [[d[0], int(d[1:])] for d in data]

position = 50
zeros = 0

for direction, steps in data:
    if direction == 'L':
        directioniser = -1
    else:
        directioniser = 1
    position = (position + steps * directioniser) % 100
    if position == 0:
        zeros += 1
        
print(zeros)