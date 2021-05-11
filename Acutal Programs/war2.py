import random
from random import shuffle


SUITS = ['H', 'D', 'S', 'C']
FACES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
DECK = [f + s for f in FACES for s in SUITS]
VALUE = dict((DECK[i], (i + 3) // 4) for i in range(len(DECK)))
 
class WarCardGame:
    ## start card game War
    def __init__(self):
        deck = DECK.copy()
        shuffle(deck)
        self.deck1, self.deck2 = deck[:26], deck[26:]
        self.pending = []
 
    def flip(self):
        ##one card turn
        if len(self.deck1) == 0 or len(self.deck2) == 0:
            return self.gameover()
        ##user input to advance hands
        userin = input("Press enter to see next hand:") 
        if userin.lower() == str(f"h"):
            print(f'continue')
            self.flip 
        ##quit game early
        elif userin.lower() == str(f"quit"):
            print(f'Game eneded')
            exit()
        
        card1, card2 = self.deck1.pop(0), self.deck2.pop(0)
        stregnth1, stregnth2 = VALUE[card1], VALUE[card2]
        print("{:10}{:10}".format(card1, card2), end='')
        
        if stregnth1 > stregnth2:
            print('Player 1 takes the cards.')
            self.deck1.extend([card1, card2])
            self.deck1.extend(self.pending)
            self.pending = []
            account123 = int(len(self.deck1))
            print ("Player 1 has ",account123, "cards now" )

        elif stregnth1 < stregnth2:
            print('The computer takes the cards.')
            self.deck2.extend([card2, card1])
            self.deck2.extend(self.pending)
            self.pending = []
            account223 = int(len(self.deck2))
            print ("The computer has ",account223, "cards now" )
        else:  ##if cards are a tie
            print('Tie!')
            if len(self.deck1) == 0 or len(self.deck2) == 0:
                return self.gameover()
 
            card3, card4 = self.deck1.pop(0), self.deck2.pop(0)
            self.pending.extend([card1, card2, card3, card4])
            print("{:10}{:10}".format("?", "?"), 'Cards are face down.', sep='')
            return self.flip()
 
        return True
 
    def gameover(self):
        ##who won/end of game message
        if len(self.deck2) == 0:
            if len(self.deck1) == 0:
                print('\nGame ends as a tie.')
            else:
                print('\nPlayer 1 wins the game.')
        else:
            print('\nComputer wins the game.')
 
        return False
 
if __name__ == '__main__':
    WG = WarCardGame()
    while WG.flip():
        continue