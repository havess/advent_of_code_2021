# I realise that there is a much nicer way to go about this using sets but I thought of it as I was hammering out this naive solution so :shrug:

# Parse input
lines = open('input.txt', 'r').read().splitlines()
coords = [line.split(",") for line in lines[:lines.index('')]]
coords = list(map(lambda x: (int(x[0]), int(x[1])), coords))
folds = [line[len("fold along "):].split('=') for line in lines[lines.index('') + 1:]]
folds = list(map(lambda x: (x[0], int(x[1])), folds))

# Init state
width = max([int(x) for x, _ in coords]) + 1
height = max([int(y) for _, y in coords]) + 1
paper = [['.']*width for _ in range(height)]
for x, y in coords:
    paper[y][x] = '#'

def solve(folds, paper, print_result):
    for orient, ind in folds:
        new_width = max(ind - 1, len(paper[0]) - ind) - 1 if orient == 'x' else len(paper[0])
        new_height = max(ind, len(paper) - ind) - 1 if orient == 'y' else len(paper)
        a_width = ind if orient == 'x' else len(paper[0])
        a_height = ind if orient == 'y' else len(paper)
        a_side = [row[:a_width] for row in paper[:a_height]]
        b_width = ind + 1 if orient == 'x' else 0
        b_height = ind + 1 if orient == 'y' else 0
        b_side = [row[b_width:] for row in paper[b_height:]]
        b_side = b_side[::-1] if orient == 'y' else [row[::-1] for row in b_side]
        new_paper = [['.']*new_width for _ in range(new_height)]
        for side in [a_side, b_side]:
            for i, row in enumerate(side):
                for j, c in enumerate(row):
                    new_paper[i][j] = '#' if '#' in [c, paper[i][j]] else '.'
        paper = new_paper

    if print_result:
        for row in paper:
            for c in row:
                print(c, end='')
            print("")
    return paper

# Q1
soln = solve(folds[:1], paper, False)
soln = [cell for row in soln for cell in row]
print(soln.count('#'))

# Q2
solve(folds, paper, True)
