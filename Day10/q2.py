import functools
lines = open('input.txt', 'r').read().splitlines()
start = ['(', '[', '{', '<']
end = [')', ']', '}', '>']
line_scores = []
for line in lines:
    s = []
    corrupt = False
    for c in line:
        if c in end:
            last = s.pop()
            if end.index(c) != start.index(last):
                corrupt = True
                break
        else:
            s.append(c)
    if len(s) and not corrupt:
        scores = [[1,2,3,4][start.index(e)] for e in s[::-1]]
        line_scores.append(functools.reduce(lambda a, b: a*5 + b, scores))

print(sorted(line_scores)[int(len(line_scores)/2)])


