from functools import reduce
input = open('input.txt', 'r')
lines = [tuple(int(c) for c in s) for s in input.read().splitlines()]
sums = reduce(lambda x, y: tuple(a + b for a,b in zip(x, y)), lines)
bits = [(1 if s >= len(lines)/2 else 0) for s in sums]
rbits = [(0 if b else 1) for b in bits]
def get_num(x):
    num = 0
    for b in x:
        num = (num << 1) | b
    return num
print(get_num(bits) * get_num(rbits))
