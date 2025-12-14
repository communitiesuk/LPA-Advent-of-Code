with open('input_jac.txt') as f:
    data = [d.strip() for d in f.readlines()]
    
def split(indeces, row):
    new_indeces = set()
    splits = 0
    for i in indeces:
        if row[i] == '^':
            splits += 1
            new_indeces.update([i - 1, i + 1])
        else:
            new_indeces.add(i)
    return new_indeces, splits

pt1 = 0
indeces = set([data[0].index('S')])
for row in data[1:]:
    indeces, splits = split(indeces, row)
    pt1 += splits
    
timelines = [[0 for x in range(len(d))] for d in data]
for i in range(len(data)):
    if "S" in data[i]:
        timelines[0][data[0].index('S')] = 1
    else:
        for j in range(len(data[i])):
            if j > 0:
                if data[i][j - 1] == '^':
                    timelines[i][j] += timelines[i - 1][j - 1]
            if j < len(data[0]) - 2:
                if data[i][j + 1] == '^':
                    timelines[i][j] += timelines[i - 1][j + 1]
            if data[i][j] != '^':
                timelines[i][j] += timelines[i - 1][j]

print(pt1)
print(sum(timelines[-1]))