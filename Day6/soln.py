import re
input = open('input.txt', 'r')
initial_state = [int(x) for x in re.findall('\d+', input.read())]
fish = [initial_state.count(x) for x in range(9)]
def solve(fish, d):
    for i in range(d):
        fish[:] = fish[1:] + fish[0:1]
        fish[6] += fish[8]
    return sum(fish)
print(solve([initial_state.count(x) for x in range(9)], 80))
print(solve([initial_state.count(x) for x in range(9)], 256))
