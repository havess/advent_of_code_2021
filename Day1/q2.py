input = open('input.txt', 'r')
lines = list(map(int, input.readlines()))
sums = [sum(lines[i:i+3]) for i in range(len(lines) - 2)]
sums = [sums[i:i+2] for i in range(len(sums) - 1)]
print(len(list(filter(lambda x: x[1] > x[0], sums))))
