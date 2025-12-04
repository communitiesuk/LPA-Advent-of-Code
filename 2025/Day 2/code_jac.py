with open('input_jac.txt') as f:
    data = [list(map(int, id.split('-'))) for id in f.read().split(',')]
    
pt1 = 0
pt2 = 0
for start, end in data:
    for x in range(start, end + 1):
        str_x = str(x)
        half = len(str_x) // 2
        if str_x[:half] == str_x[half:]:
            pt1 += x
        for y in range(1, len(str_x) // 2 + 1):
            chunks = [str_x[i:i+y] for i in range(0, len(str_x), y)]
            if len(set(chunks)) == 1:
                pt2 += x
                break
                
print(pt1)
print(pt2)