import random                  #get help with checking flashcard answers
from random import randint     #get help with reviewing flashcards

class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        
        #we will return a string 
        return self.word+' ( '+self.meaning+' )'
        
global deckS
deck = []
print("welcome to my flashcard application")
  
#the following loop will be repeated until
#user stops to add the flashcards
while(True): 
    word = input("enter the name you want to add to flashcard : ")
    meaning = input("enter the meaning of the word : ")
      
    flash.append(flashcard(word, meaning))
    option = int(input("enter 0 if you want to add another flashcard, 1 to exit builder: "))
      
    if(option):
        break
          
# printing all the flashcards 
print("\nYour flashcards")
for i in flash:
    print(">", i)

#start reviewing flash cards
reviewtime = input(f'would you like to start studying your flashcards now? Type "y" to review: ')
randomizer = randint(0, len(deck)-1)
pickedcard = deck[randomizer]
if reviewtime.lower == str(f'y'):
    print(pickedcard)
    random.shuffle.append(deck)
    print(deck)

#flashcards correct/incorrect
while(True):
