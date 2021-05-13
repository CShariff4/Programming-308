import random 

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


    def shuffleDeck(deck):
        for cardPosition in range(len(deck)):
    unoDeck = buildDeck()