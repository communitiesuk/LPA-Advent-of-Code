with open('input_jac.txt') as f:
    data = [list(map(int, list(d.strip()))) for d in f.readlines()]
    
pt1 = 0
for d in data:
    first = max(d[:-1])
    second = max(d[d.index(first) + 1:])
    pt1 += int(str(first) + str(second))

pt2 = 0
for d in data:
    temp_d = d
    first = max(d[:-11])
    temp_d = temp_d[temp_d.index(first) + 1:]
    second = max(temp_d[:len(temp_d) - 10])
    temp_d = temp_d[temp_d.index(second) + 1:]
    third = max(temp_d[:len(temp_d) - 9])
    temp_d = temp_d[temp_d.index(third) + 1:]
    fourth = max(temp_d[:len(temp_d) - 8])
    temp_d = temp_d[temp_d.index(fourth) + 1:]
    fifth = max(temp_d[:len(temp_d) - 7])
    temp_d = temp_d[temp_d.index(fifth) + 1:]
    sixth = max(temp_d[:len(temp_d) - 6])
    temp_d = temp_d[temp_d.index(sixth) + 1:]
    seventh = max(temp_d[:len(temp_d) - 5])
    temp_d = temp_d[temp_d.index(seventh) + 1:]
    eighth = max(temp_d[:len(temp_d) - 4])
    temp_d = temp_d[temp_d.index(eighth) + 1:]
    ninth = max(temp_d[:len(temp_d) - 3])
    temp_d = temp_d[temp_d.index(ninth) + 1:]
    tenth = max(temp_d[:len(temp_d) - 2])
    temp_d = temp_d[temp_d.index(tenth) + 1:]
    eleventh = max(temp_d[:len(temp_d) - 1])
    temp_d = temp_d[temp_d.index(eleventh) + 1:]
    twelfth = max(temp_d)
    pt2 += int(''.join(map(str, [first, second, third, fourth, fifth, sixth, 
                                 seventh, eighth, ninth, tenth, eleventh, twelfth])))
    
print(pt1)
print(pt2)