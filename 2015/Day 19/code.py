with open('input_jac.txt') as f:
    data = [d.strip() for d in f.readlines()]
    
import re
    
starter_molecule = 'e'
replacements = [(d.split(' => ')[0], d.split(' => ')[1]) for d in data[:-2]]
target_molecule = data[-1]

new_molecules = set()
for k, v in replacements:
    for match in re.finditer(k, target_molecule):
        new_molecules.add(target_molecule[:match.start()] + v + target_molecule[match.end():])

print(len(new_molecules))

steps = 0
while target_molecule != starter_molecule:
    for k, v in replacements:
        steps += len(re.findall(v, target_molecule))
        target_molecule = target_molecule.replace(v, k)
                 
print(steps)

