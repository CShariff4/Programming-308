import random 

#building deck function
def buildDeck():
    deck =[]
    colors = ["Blue", "Green", "Yellow", "Red"]
    values = ["Draw Two", "Skip", "Reverse", 0,1,2,3,4,5,6,7,8,9]
    wildcards = ["Wild", "Wild Draw Four"]
    for color in colors:
        for value in values:
            cardvalue = "{} {}".format(color,value)
            deck.append(cardvalue)
            if value != 0:
                deck.append(cardvalue)
    for i in range(4):
        deck.append(wildcards[0])
        deck.append(wildcards[1])
    return deck

#shuffle deck function
def shuffleDeck(deck):
    for cardPosition in range(len(deck)):
        randPosition = random.randint(0,107)
        deck[cardPosition], deck[randPosition] = deck[randPosition], deck[cardPosition]
        return deck


def drawCards(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))
        return cardsDrawn




unoDeck = buildDeck()
unoDeck =shuffleDeck(unoDeck)
unoDeck =shuffleDeck(unoDeck)
print(unoDeck)

players = []
numPlayers = int(input("How many players are playing today? "))
for player in range(numPlayers):
    players.append(drawCards(5))

print(players)
