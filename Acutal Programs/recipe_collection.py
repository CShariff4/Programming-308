import json                 #neeed to work on add fucntion!!!
import sys                  #get help on making dict instead of json
                            #after option selected it always goes to add
print('Hello welcome to my recipe book. What would you like to do today? Press "M", or type "menu" or "help" to access the menu')
userin = input("Please enter your answer:")

if userin.lower() == str(f'm'):
    print(f'Menu Options: (N=>Add New Recipe) (L=>List Existing Recipes) (R=>Read Recipes) (Q=>Quit)')
elif userin.lower() == str(f'menu'):
    print(f'Menu Options: (N=>Add New Recipe) (L=>List Existing Recipes) (R=>Read Recipes) (Q=>Quit)')
elif userin.lower() == str(f'help'):
    print(f'Menu Options: (N=>Add New Recipe) (L=>List Existing Recipes) (R=>Read Recipes) (Q=>Quit)')

#menu slection
userin2 = input("Please select option:")

#quit option
if userin2.lower() == str(f"q"):
        print(f'Program ended') 
        exit()
elif userin2.lower() == str(f"quit"):
        print(f'Program ended long time ago')
        exit()


#Read Existing recipes
data = json.load(open('recipe_collection.json')) 
#read recipe
if userin2.lower() == str(f'r'):
    food_index = input('What do you want to eat?')
    if food_index in data:
        print(data[food_index])       
    elif food_index not in data:
        print("Recipe not in files yet")       
        exit()

#need to add more data in the dictionary
#List recipes
if userin2.lower() == str(f"l"):
        print(data)  
        exit()

#new recipe variables
name = input(f"What would you like to add to the recipe book")
ingred = input(f"What are the necessary ingredients?")
instruc =input(f'How do you prepare this food?')


if userin2.lower() == str(f"n"):
    #name = input(f"What would you like to add to the recipe book")
    #ingred = input(f"What are the necessary ingredients?")
    #instruc =input(f'How do you prepare this food?')    
    print(name + ' recipe added to dictionary')
elif name == data in "recipe_collection.json": 
    print("Recipe already exists")    


def write_to_jsonfile(path, fileName, data):
    ##filepathnameWExt = './' + path = './' + fileName + '.json'
    with open(recipe_collection.json, 'w') as fp:
        json.dump(data, fp) 

path ='./'
fileName = 'recipe_collection.py'
data = [json]
data = [name]== name, [ingred]== ingred, [instruc]== instruc    