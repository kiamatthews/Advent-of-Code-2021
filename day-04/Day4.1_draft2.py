import numpy as np
bingo_balls = []
with open("my_numbers.txt", "r") as numbers:
    bingo_balls = numbers.read().split(',')
#print (bingo_balls)

cards = np.loadtxt("my_boards.txt", dtype=str)
#print (cards)
#cardz = np.split(cards, len(cards)/5)
cardz = cards.reshape(int(len(cards)/5), 5, 5)
#print (cardz)


for ball in bingo_balls[0:10]:
    print ("The number called is " + ball)
    cardz[cardz == ball] = "_"
    print (cardz)
    print ("I am done marking cards.")
    print ("-----")
    print ("I am now checking cards.")
    for i, card in enumerate(cardz):
        for y, row in enumerate(card):
            marks = (row == "_").sum()
            if marks == 5:
                print("There are " + str(marks) + " numbers marked in row " + str(y+1) + " of card " + str(i+1))
                #break
        #else:
            #continue
        #break

        for z, column in enumerate(card.T):
            markz = (column == "_").sum()
            if markz == 5:
                print("There are " + str(markz) + " numbers marked in column " + str(z+1) + " of card " + str(i+1))
                #break
        #else:
             #continue
        #break
    #else:
        #continue
    #break

    print ("-----")
