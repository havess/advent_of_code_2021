input = open('input.txt', 'r')
lines = list(map(int, input.readlines()))
print(len(list(filter(lambda x: x[1] > x[0], [lines[i:i+2] for i in range(len(lines) - 1)]))))



