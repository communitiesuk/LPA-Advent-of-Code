data = 29000000

def get_factors(n):
    f = set()
    f2 = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            f.add(i)
            f.add(n // i)
        if n % i == 0 and n // i <= 50:
            f2.add(i)
        elif n % i == 0 and i <= 50:
            f2.add(n // i)
    return f, f2

pt1 = False
pt2 = False
for d in range(1, data):
    factors, factors2 = get_factors(d)
    fn = sum([x * 10 for x in factors])
    fn2 = sum([x * 11 for x in factors2])
    if fn >= data and not pt1:
        print(f'pt1 is {d}')
        pt1 = True
    if fn2 >= data and not pt2:
        print(f'pt2 is {d}')
        pt2 = True
    if pt1 and pt2:
        break