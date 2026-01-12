import re
from collections import deque

with open('input_jac.txt') as f:
    data = [d.strip() for d in f.readlines()]
    
indicators = [list(re.findall(r'\[(.*)\]', d)[0]) for d in data]
button_sets = [re.findall(r'(\(.+?\))', d) for d in data]
button_sets = [[list(map(int, re.findall('\d', n))) for n in numbers] for numbers in button_sets]
joltages = [re.findall(r'(\{.+?\})', d)[0] for d in data]
joltages = [list(map(int, re.findall(r'\d+', j))) for j in joltages]

def press_button(current, button):
    for effect in button:
        if current[effect] == '.':
            current = current[:effect] + ['#'] + current[effect + 1:]
        else:
            current = current[:effect] + ['.'] + current[effect + 1:]
    return current

def press_joltage(current, button, presses):
    current = list(current)
    for effect in button:
        current[effect] += presses
    return current

def count_presses(target, current, buttons):
    visited = {tuple(current)}
    candidates = [current]
    presses = 0
    while target not in candidates:
        presses += 1
        temp_candidates = []
        for candidate in candidates:
            for b in buttons:
                new_candidate = press_button(candidate, b)
                if tuple(new_candidate) not in visited:
                    visited.add(tuple(new_candidate))
                    temp_candidates.append(new_candidate)
        candidates = temp_candidates
    return presses

# def is_joltage_valid(current, target):
#     for c, t in zip(current, target):
#         if c > t:
#             return False
#     return True
            
# def config_joltage(target, current, buttons):
#     visited = {tuple(current)}
#     candidates = deque([current])
#     presses = 0
#     while candidates:
#         next_candidates = deque([])
#         for _ in range(len(candidates)):
#             candidate = candidates.popleft()
#             if candidate == target:
#                 return presses
#             for b in buttons:
#                 new_candidate = tuple(press_joltage(candidate, b))
#                 if new_candidate not in visited and is_joltage_valid(new_candidate, target):
#                     visited.add(new_candidate)
#                     next_candidates.append(new_candidate)
#         candidates = next_candidates
#         presses += 1
#     return -1    

def get_chunks(current, target, buttons, deduction=0):
    return [(i, min([target[idx] - current[idx] - deduction for idx in b])) for i, b in enumerate(buttons) if min([target[idx] - current[idx] - deduction for idx in b]) > 0]
    
def process_chunks(current, target, buttons, total_presses=0, first_pass=True):
    
    if current == target:
        return total_presses
    # print(f'{target=}, {current=}, {first_pass=}')
    if first_pass:
        chunks = get_chunks(current, target, buttons)
        print(chunks)
    else:
        chunks = get_chunks(current, target, buttons, 5)
    
    if not chunks:
        return float('inf')
    
    return min(process_chunks(press_joltage(current, buttons[idx], presses), 
                              target, 
                              buttons, 
                              total_presses + presses,
                              False
                              ) 
               for idx, presses in chunks)

pt1 = []
pt2 = []
for i, b, j in zip(indicators, button_sets, joltages):
    start = ['.'] * len(i)
    current = [0] * len(i)
    pt1.append(count_presses(i, start, b))
    pt2.append(process_chunks(current, j, b))
    
print(sum(pt1))
print(sum(pt2))