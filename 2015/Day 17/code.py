with open('input_jac.txt') as f:
    data = tuple([int(d.strip()) for d in f.readlines()])
    
LITRES = 150

# data = (20, 15, 10, 5, 5)

def eggnog(n, cups):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        results = 0
        for i in range(len(cups)):
            results += eggnog(n - cups[i], cups[i + 1:])
        return results

def more_eggnog(n, cups, cups_used=None):
    if cups_used is None:
        cups_used = []
    if n < 0:
        return []
    elif n == 0:
        return [cups_used]
    else:
        results = []
        for i in range(len(cups)):
            results += more_eggnog(n - cups[i], cups[i + 1:], cups_used + [cups[i]])
        return results

print(eggnog(LITRES, data))
combos = more_eggnog(LITRES, data)
len_combos = [len(c) for c in combos]
min_len_combo = min(len_combos)
count_min_len_combos = [1 if c == min_len_combo else 0 for c in len_combos]
print(sum(count_min_len_combos))