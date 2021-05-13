import random 

#building deck function
def buildDeck():
    deck =[]
    colors = ["Blue", "Green", "Yellow", "Red"]
    values = ["Draw Two", "Skip", "Reverse",0,1,2,3,4,5,6,7,8,9]
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

#draw cards function
def drawCards(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn

#player is integer
#playerHand is list
def showHand(player, playerHand):
    print("Player {}'s turn".format(player+1))
    print("Your Hand")
    print("-----------")
    y =1
    for card in playerHand:
        print('{}) {}'.format(y, card))
        y+=1
    print("")

#fuction to see if a player can place a card or not
def canPlay(color, value, playerHand):
    for card in playerHand:
        if "Wild" in card:
            return True
        elif color in card or value in card:
            return True
    return False

unoDeck = buildDeck()
unoDeck =shuffleDeck(unoDeck)
discards = []
#print(unoDeck)

players = []
numPlayers = int(input("How many players are playing today? Has to be between 2 and 4: "))
for player in range(numPlayers):
    players.append(drawCards(5))

print(players)

playerTurn = 0
playerDirection =1
playing = True
discards.append(unoDeck.pop(0))
splitCard = discards[0].split(" ", 1)
currentColor = splitCard[0]
if currentColor != "Wild":
    cardVal = splitCard[1]
else:
    cardVal = "Any"


while playing:
    showHand(playerTurn, players[playerTurn])
    print("Card on top of discard pile {}".format(discards[-1]))
    if canPlay(currentColor, cardVal, players[playerTurn]):
        cardChosen = int(input("Which card do you want to play? "))
        while not canPlay(currentColor, cardVal, [players[playerTurn][cardChosen-1]]):
            cardChosen = int(input("Not a vaild card. Please pick a different card"))
        print("You played {}".format(players[playerTurn][cardChosen-1]))
        discards.append(players[playerTurn].pop(cardChosen-1))
        #checking for special cards
        splitCard = discards[-1].split(' ', 1)
        currentColor = splitCard[0]
        if len(splitCard) == 1:
            cardVal = "Any"
        else: 
            cardVal = splitCard[1]
        if currentColor == "Wild":
            for z in range(len(colors)):
                print("{}) {}".format(z+1, colors[z]))
        newColor = int(input("Invalid option. Please pick a new color: "))    
        while newColor < 1 or newColor > 4:
            newColor = int(input("Invalid option. Please pick a new color: "))
        currentColor = colors[newColor-1]
    if cardVal == "Reverse":
        playerDirection = playerDirection * -1
    elif cardVal == "Skip":
        playerTurn += playerDirection
    elif cardVal == "Draw Two":
        playerDraw = playerTurn+playerDirection
        if playerTurn == numPlayers:
            playerTurn = 0
        elif playerTurn < 0:
            playerTurn = numPlayers-1
        players[playerTurn].extend(drawCards(2))
        print(' ')
    elif cardVal == "Draw Four":
        playerDraw = playerTurn+playerDirection
        if playerTurn == numPlayers:
            playerTurn = 0
        elif playerTurn < 0:
            playerTurn = numPlayers-1
        players[playerTurn].extend(drawCards(4))
        print(" ") 
    else:
        print("You cannot play. Must draw a card")
        players[playerTurn].extend(drawCards(1))
        print(" ")

    playerTurn += playerDirection
    if playerTurn >= numPlayers:
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = numPlayers-1