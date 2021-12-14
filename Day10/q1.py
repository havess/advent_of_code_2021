lines = open('input.txt', 'r').read().splitlines()
res = 0
start = ['(', '[', '{', '<']
end = [')', ']', '}', '>']
for line in lines:
    s = []
    for c in line:
        if c in end:
            last = s.pop()
            if end.index(c) != start.index(last):
                res += [3, 57, 1197, 25137][end.index(c)]
                break
        else:
            s.append(c)
print(res)


