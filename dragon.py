import random
import time
def displayintro():
    print('''
          You are in a land full of dragons. In front of you,
 you see two caves. In one cave, the dragon is friendly
 and will share his treasure with you. The other dragon
 is greedy and hungry, and will eat you on sight      
          ''')
    
    
def choose_cave():
        cave=''
        while cave != '1' and cave !='2':
            print("Which cave will you go into? (1 or 2)")
            cave=input("Cave: ")

def checkCave(choosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print("It's dark ans spooky inside...")            
    time.sleep(2)
    print('A large Dragon Jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)
    
    friendlyCave=random.randint(1, 2)
    if choosenCave==str(friendlyCave):
        print('Gives you his Treasure!')
    else:
        print("Gobbles you down in one bite!")
        
        print("++END++")
        
playAgain='yes'
while playAgain=='yes'or playAgain=='y':
    displayintro()
    caveNumber=choose_cave()
    checkCave(caveNumber)
    print('Do you want to play Again? (yes or no')
    playAgain=input()
    
    