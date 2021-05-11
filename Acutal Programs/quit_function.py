import sys

print(f'Type "quit", or "q" to quit: ')
userin = input("Please enter answer:") 
if userin.lower() == str(f"quit"):
        print(f'Program ended') 
        exit()
elif userin.lower() == str(f"q"):
        print(f'Program ended long time ago')
        exit()
else : 
        print(f'You entered: {userin}, The program is still running')