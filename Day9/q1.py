lines = open('input.txt', 'r').read().splitlines()
hm = [[int(d) for d in line] for line in lines]
res = [[int(d) for d in line] for line in lines]
def is_low_point(i, j):
    neighs = [(max(0, i - 1), j), (min(len(hm) - 1, i + 1), j), (i, max(0, j - 1)), (i, min(len(hm[0]) - 1, j + 1))]
    neighs = list(filter((i, j).__ne__, neighs))
    return all(hm[i][j] < hm[m][n] for m, n in neighs)
for i in range(len(hm)):
    for j in range(len(hm[0])):
        res[i][j] = hm[i][j] + 1 if is_low_point(i, j) else 0
print(sum(sum(r) for r in res))
