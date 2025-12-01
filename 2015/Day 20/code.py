data = 29000000

def get_factors(n):
    f = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            f.add(i)
            f.add(n // i)
    return f

pt1 = False
for n in range(1, data // 10):
    factors = sorted(get_factors(n))
    fn = sum(list(map(lambda x: x * 10, factors)))
    if fn >= data and not pt1:
        print(n)
        pt1 = True