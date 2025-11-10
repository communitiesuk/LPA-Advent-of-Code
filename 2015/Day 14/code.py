with open('input_jac.txt') as f:
    data = [d.strip() for d in f.readlines()]
    
info = []
names = []
for d in data:
    split_d = d.split(' ')
    name = split_d[0]
    speed = int(split_d[3])
    duration = int(split_d[6])
    rest = int(split_d[-2])
    info.append((name, speed, duration, rest))
    names.append(name)
    
TIME = 2503

# info = [('Comet', 14, 10, 127),
#         ('Dancer', 16, 11, 162)]

pt1 = 0
distances = {n: 0 for n in names}
scores = {n: 0 for n in names}
for t in range(1, TIME + 1):
    for i in info:
        name, speed, duration, rest = i
        multiples = t // (duration + rest)
        remainder = t % (duration + rest)
        if remainder < duration:
            time_travelled = multiples * duration + remainder
        else:
            time_travelled = (multiples + 1) * duration
        distance_travelled = time_travelled * speed
        distances[name] = distance_travelled
        if distance_travelled > pt1:
            pt1 = distance_travelled
    for n in names:
        if distances[n] == pt1:
            scores[n] += 1
        
print(pt1)
print(max(scores.values()))