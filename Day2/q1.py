input = open('input.txt', 'r')
lines = [s.split(" ") for s in input.read().splitlines()]
mapping = {'forward': (1, 0), 'up': (0, -1), 'down': (0, 1)}
lines = list(map(lambda x: tuple(y * int(x[1]) for y in mapping[x[0]]), lines))
print(sum(x[0] for x in lines)*sum(x[1] for x in lines))
