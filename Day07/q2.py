import re
input = open('input.txt', 'r')
initial_state = [int(x) for x in re.findall('\d+', input.read())]
crabs = [initial_state.count(x) for x in range(max(initial_state) + 1)]
cost = [0]*(max(initial_state)+1)
step_cost = num_crabs = crabs[0]
for i, c in enumerate(crabs[1:]):
    cost[i+1] = cost[i] + step_cost
    num_crabs += c
    step_cost += num_crabs

step_cost = num_crabs = crabs[-1]
last_cost = 0
for i, c in reversed(list(enumerate(crabs[:-1]))):
    last_cost = last_cost + step_cost
    cost[i] += last_cost
    num_crabs += c
    step_cost += num_crabs

print(min(cost))

