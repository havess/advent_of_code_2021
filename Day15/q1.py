from queue import PriorityQueue
def dijkstra(grid):
    dist = [[float('inf') for _ in row] for row in grid]
    dist[0][0] = 0
    visited = set()
    q = PriorityQueue()
    q.put((0, (0, 0)))

    while not q.empty():
        (distance, (i, j)) = q.get()
        visited.add((i, j))

        neighs = [(max(0, i - 1), j), (i, max(0, j - 1)), (min(len(grid) - 1, i + 1), j), (i, min(len(grid[0]) - 1, j + 1))]
        for m, n in neighs:
            if (m, n) not in visited:
                old_cost = dist[m][n]
                new_cost = dist[i][j] + grid[m][n]
                if new_cost < old_cost:
                    q.put((new_cost, (m, n)))
                    dist[m][n] = new_cost

    print(dist[len(grid) - 1][len(grid[0]) - 1])


lines = open("input.txt", 'r').read().splitlines()

# Q1
grid = [[int(v) for v in line] for line in lines]
dijkstra(grid)

# Q2
m, n = len(grid), len(grid[0])
large_grid = []
for i in range(5):
    for row in grid:
        large_grid.append(5*row)
grid = large_grid
for i in range(len(grid)):
    for j in range(len(grid[0])):
        grid[i][j] = (grid[i][j] + int(i/m) + int(j/n) - 1) % 9 + 1

dijkstra(grid)
