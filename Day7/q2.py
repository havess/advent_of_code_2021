import re
input = open('input.txt', 'r')
initial_state = [int(x) for x in re.findall('\d+', input.read())]
crabs = [initial_state.count(x) for x in range(max(initial_state) + 1)]
cost = [0]*(max(initial_state)+1)
step_cost = num_crabs = crabs[0]
last_cost = 0
for i, c in enumerate(crabs):
    if i == 0:
        continue
    cost[i] = last_cost + step_cost
    last_cost = cost[i]
    num_crabs += c
    step_cost += num_crabs

step_cost = num_crabs = crabs[-1]
last_cost = 0
for i, c in reversed(list(enumerate(crabs))):
    if i == len(crabs) - 1:
        continue
    temp = cost[i]
    cost[i] += last_cost + step_cost
    last_cost = (cost[i] - temp)
    num_crabs += c
    step_cost += num_crabs

print(min(cost))

