import numpy as np
bingo_balls = []
with open("input_numbers_sample.txt", "r") as numbers:
    bingo_balls = numbers.read().split(',')
print(bingo_balls)
cards = np.loadtxt("input_boards_sample.txt", dtype=str)
cardz = cards.reshape(int(len(cards)/5), 5, 5)
all_cards = list.range(len(cards))
for ball in bingo_balls:
    cardz[cardz == ball] = "_"
    for i, card in enumerate(cardz):
        for y, row in enumerate(card):
            marks = (row == "_").sum()
            if marks == 5 and i not in winners:
                winners.append(i)
                #else:

                #break
        for z, column in enumerate(card.T):
            markz = (column == "_").sum()
            if markz == 5 and i not in winners:
                winners.append(i)
                #break
print (winners)
        #else:
        #    continue
        #break
    #else:
    #    continue
    #break
unmarked = []
for r in cardz[winner[-1]]:
    for space in r:
        if space != "_":
            unmarked.append(int(space))
print (sum(unmarked) * int(ball)
