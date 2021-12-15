lines = open('input.txt', 'r').read().splitlines()
def simulate(grid, nsteps, step = 1):
    if not sum(cell for row in grid for cell in row):
        return step - 1
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

    return simulate(grid, nsteps, step + 1)
print(simulate([[int(c) for c in line] for line in lines], 100))
