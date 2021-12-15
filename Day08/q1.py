input = open('input.txt', 'r')
lens = [list(map(len, line.split('|')[1].split())) for line in input.read().splitlines()]
print(sum(map(lambda x: sum(x.count(y) for y in [2, 3, 4, 7]), lens)))
