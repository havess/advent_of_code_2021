lines = open('input.txt', 'r').read().splitlines()
def simulate(grid, steps, nflashes = 0):
    if not steps:
        return nflashes
    grid = list(map(lambda row: list(map(lambda cell: cell + 1, row)), grid))
    flash = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 10]
    for i, j in flash:
        for m in range(max(0, i - 1), min(len(grid) - 1, i+1) + 1):
            for n in range(max(0, j - 1), min(len(grid[0]) - 1, j+1) + 1):
                if (m,n) == (i, j) or grid[m][n] == 0:
                    continue
                grid[m][n] += 1
                if grid[m][n] == 10:
                    flash.append((m, n))
        grid[i][j] = 0
        nflashes += 1

    return simulate(grid, steps-1, nflashes)
print(simulate([[int(c) for c in line] for line in lines], 100))
