import numpy as np
bingo_balls = []
with open("input_numbers_sample.txt", "r") as numbers:
    bingo_balls = numbers.read().split(',')

cards = np.loadtxt("input_boards_sample.txt", dtype=str)
cardz = cards.reshape(int(len(cards)/5), 5, 5)
clean_cards = cardz.copy()

winners =[]
winning_balls = []
for ball in bingo_balls:
    cardz[cardz == ball] = "_"
    for i, card in enumerate(cardz):
        for y, row in enumerate(card):
            marks = (row == "_").sum()
            if marks == 5 and i not in dict(winners):
                winners.append((i, ball))
                #else:

                #break
        for z, column in enumerate(card.T):
            markz = (column == "_").sum()
            if markz == 5 and i not in dict(winners):
                winners.append((i, ball))
                #break
print (winners)
#print (cardz[winners[-1][0]])
print (winners[-1][1])

for ball in bingo_balls:
    clean_cards[clean_cards == ball] = "_"
    if ball == winners[-1][1]:
        print (clean_cards[winners[-1][0]])
        break
unmarked = []
for r in clean_cards[winners[-1][0]]:
    print (r)
    for space in r:
        print (space)
        if space != "_":
            unmarked.append(int(space))
print (unmarked)
print (sum(unmarked) * int(winners[-1][1]))
