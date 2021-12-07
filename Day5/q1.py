import re
input = open('input.txt', 'r')
lines = [re.findall(r'\d+', line) for line in input.read().splitlines()]
lines = list(map(lambda x: [(int(x[0]), int(x[1])), (int(x[2]), int(x[3]))], lines))
x_dim = max([max(line[0][0], line[1][0]) for line in lines])
y_dim = max([max(line[0][1], line[1][1]) for line in lines])
grid = [[0]*(x_dim+1) for _ in range(y_dim+1)]
for line in lines:
    start, end = line
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    if dx == 0:
        sign = int(dy/abs(dy))
        for i in range(start[1], start[1] + dy + 1*sign, sign):
            grid[i][start[0]] += 1
    if dy == 0:
        sign = int(dx/abs(dx))
        for i in range(start[0], start[0] + dx + 1*sign, sign):
            grid[start[1]][i] += 1
print(len(list(filter((2).__le__, [point for row in grid for point in row]))))
