import random
import json
import sys


class flashcard:
	def __init__(self):
			
		self.word= json.load(open('flashcards.json'))
		global data
		data = json.load(open('flashcards.json'))
		#new recipe variables
	word = input(f"What is the name of the flashcard: ")
if self == data in "flashcards.json":
    print(f"Flashcard already exists")
else:
    newword = input(f"Enter flashcard word now: ")
    meaning =input(f'Enter meaning now: ')
    data[newword]={"Word": newword,"Meaning": meaning }
    print(data)

#Read Existing recipes
data = json.load(open('flashcards.json')) 
#read recipe
if word() == str(f'r'):
    word = input('What do you want to eat?')
    if word in data:
        print(data[word])       
    elif word not in data:
        print("Recipe not in files yet")       
        exit()



def write_to_jsonfile(path, fileName, data):
    ##filepathnameWExt = './' + path = './' + fileName + '.json'
    with open(path + fileName, 'w') as fp:
        json.dump(data, fp) 

path ='./'
fileName = 'flashcards.json'
write_to_jsonfile(path,fileName, data)  
		#self.card={'apple':'red',
					#'orange':'orange',
					#'watermelon':'green',
					#'banana':'yellow'}



def quiz(self):
		while (True):
			
			data = json.load(open('flashcards.json'))
			word, meaning = random.choice(list(self.card.items()))
			
			print("What does the word {}".format(word) + " mean?")
			user_answer = input()
			
			if(user_answer.lower() == meaning):
				print("Correct answer")
			else:
				print("Wrong answer")
				
				
			option = int(input("enter 0 , if you want to play again: "))
			if (option):
				break

print("welcome to the flashcard quiz:  ")
fc=flashcard()
fc.quiz()
