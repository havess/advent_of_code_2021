import re
lines = open("input.txt", 'r').read().splitlines()
template = lines[0]
rules = {k: v for line in lines[2:] for k, v in re.findall(r'(\w+) -> (\w+)', line)}
elements = {c: template.count(c) for c in set(template)}
pairs = [template[i:i+2] for i in range(len(template))]
pairs = {k: pairs.count(k) for k, _ in rules.items()}

def sim(steps):
    for _ in range(steps):
        old_state = dict(pairs)
        for k, v in old_state.items():
            a, b = k
            result = rules[k]
            elements[result] = elements[result] + v if result in elements else v
            pairs[a + result] += v
            pairs[result + b] += v
            pairs[k] -= v

sim(10)
print(max(elements.values()) - min(elements.values()))
sim(30)
print(max(elements.values()) - min(elements.values()))
