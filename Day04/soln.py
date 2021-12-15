from typing import List
input = open('input.txt', 'r')
class Bingo(object):
    def __init__(self, lines: List[str]):
        self._board = [[[int(n), False] for n in line.split()] for line in lines]
        self._row_score = [0] * 5
        self._col_score = [0] * 5

    def number_called(self, num):
        r, c = -1, -1
        for i, row in enumerate(self._board):
            for j, n in enumerate(row):
                if n[0] == num:
                    r, c = i, j
                    n[1] = True
                    break
            else:
                continue
            break

        if r == -1:
            return False, -1

        self._row_score[r] += 1
        self._col_score[c] += 1

        if 5 in (self._row_score[r], self._col_score[c]):
            s = 0
            for row in self._board:
                for n in row:
                    s += n[0] if not n[1] else 0
            return True, s*num

        return False, -1


lines = input.read().splitlines()
called_nums = [int(n) for n in lines[0].split(',')]
lines = list(filter(('').__ne__, lines))[1:]
boards = [lines[i:i + 5] for i in range(0, len(lines), 5)]
cards = []
for board in boards:
    cards.append(Bingo(board))

for num in called_nums:
    for i, card in enumerate(cards):
        won, result = card.number_called(num)
        if won:
            print("P1",i, result)
            break
    else:
        continue
    break

# P2
last_win = -1
cards = []
for board in boards:
    cards.append(Bingo(board))
for num in called_nums:
    to_remove = []
    for i, card in enumerate(cards):
        won, result = card.number_called(num)
        if won:
            last_win = result
            to_remove.append(i)
    for i in to_remove[::-1]:
        cards.pop(i)

print("P2", last_win)



