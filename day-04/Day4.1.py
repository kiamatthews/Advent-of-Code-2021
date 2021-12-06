import numpy as np
bingo_balls = []
with open("input_numbers.txt", "r") as numbers:
    bingo_balls = numbers.read().split(',')
cards = np.loadtxt("input_boards.txt", dtype=str)
cardz = cards.reshape(int(len(cards)/5), 5, 5)
for ball in bingo_balls:
    cardz[cardz == ball] = "_"
    for i, card in enumerate(cardz):
        for y, row in enumerate(card):
            marks = (row == "_").sum()
            if marks == 5:
                break
        for z, column in enumerate(card.T):
            marks = (column == "_").sum()
            if marks == 5:
                break
        else:
            continue
        break
    else:
        continue
    break
unmarked = []
for r in cardz[i]:
    for space in r:
        if space != "_":
            unmarked.append(int(space))
print (sum(unmarked) * int(ball))
