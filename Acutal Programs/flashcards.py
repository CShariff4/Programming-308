import random                  
from random import randint     

class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        
        #we will return a string 
        return self.word+' ( '+self.meaning+' )'
        
global deck
deck = []
print("welcome to my flashcard application")
  
#Adding flashcards until stop
while(True): 
    word = input("enter the name you want to add to flashcard : ")
    meaning = input("enter the meaning of the word : ")
      
    deck.append(flashcard(word, meaning))
    option = int(input("enter 0 if you want to add another flashcard, 1 to start reviewing : "))
      

    if(option):
        break        
          
# printing all the flashcards that were just made
print("\nYour flashcards")
for i in deck:
    print(">", i)

#quiz

