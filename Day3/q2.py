from functools import reduce
input = open('input.txt', 'r')
lines = [tuple(int(c) for c in s) for s in input.read().splitlines()]
def rec(comp_fn, data, index):
    if len(data) == 1:
        return data[0]
    col =[d[index] for d in data]
    mode = comp_fn(col)
    data = list(filter(lambda x: x[index] == mode, data))
    return rec(comp_fn, data, index+1)
def to_int(x):
    res = 0
    for b in x:
        res = (res << 1) | b
    return res
o2 = rec(lambda x: 1 if x.count(1) >= x.count(0) else 0, lines, 0)
co2 = rec(lambda x: 0 if x.count(0) <= x.count(1) else 1, lines, 0)
print(to_int(o2) * to_int(co2))

