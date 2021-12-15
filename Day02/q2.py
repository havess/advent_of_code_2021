input = open('input.txt', 'r')
lines = [s.split(" ") for s in input.read().splitlines()]
aim, depth, horiz = 0, 0, 0
for k, v in lines:
    v = int(v)
    if k == 'forward':
        horiz += v
        depth += v * aim
    elif k == 'up':
        aim -= v
    else:
        aim += v
print(depth*horiz)
