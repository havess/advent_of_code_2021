lines = open('input.txt', 'r').read().splitlines()
hm = [[int(d) for d in line] for line in lines]
res = [[int(d) for d in line] for line in lines]
def is_low_point(i, j):
    neighs = [(max(0, i - 1), j), (min(len(hm) - 1, i + 1), j), (i, max(0, j - 1)), (i, min(len(hm[0]) - 1, j + 1))]
    neighs = list(filter((i, j).__ne__, neighs))
    return all(hm[i][j] < hm[m][n] for m, n in neighs)
basins = []
num_basins = 0
for i in range(len(hm)):
    for j in range(len(hm[0])):
        if is_low_point(i, j):
            num_basins += 1
            basins.append((i, j, -num_basins))

while len(basins):
    i, j, basin = basins.pop()
    if hm[i][j] == basin:
        continue
    neighs = [(max(0, i - 1), j), (min(len(hm) - 1, i + 1), j), (i, max(0, j - 1)), (i, min(len(hm[0]) - 1, j + 1))]
    basins += [(m, n, basin) for m, n in neighs if hm[m][n] != basin and hm[m][n] != 9]
    hm[i][j] = basin

all_cells = [cell for row in hm for cell in row if cell < 0]
basin_sizes = sorted([all_cells.count(-basin) for basin in range(1, num_basins + 1)])
import math
print(math.prod(basin_sizes[-3:]))
