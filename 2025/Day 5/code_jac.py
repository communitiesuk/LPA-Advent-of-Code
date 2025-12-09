with open('input_jac.txt') as f:
    data = [d.strip() for d in f.readlines()]
    
ranges = [list(map(int, d.split('-'))) for d in data if '-' in d]
ids = [int(d) for d in data if '-' not in d and d != '']

pt1 = 0
for id in ids:
    for r in ranges:
        low, high = r
        if id >= low and id <= high:
            pt1 += 1
            break
        
ranges = sorted(ranges, key=lambda x: x[0])
current_low, current_high = ranges[0]
pt2 = current_high - current_low + 1
for r in ranges[1:]:
    new_low, new_high = r
    if new_low > current_high:
        pt2 += new_high - new_low + 1
        current_low = new_low
        current_high = new_high
    elif new_high > current_high:
        pt2 += new_high - current_high
        current_high = new_high
     
print(pt1)
print(pt2)
    