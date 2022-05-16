import random
guessTaken=0
name=input('Hello, What\'s your name? :')
print(f"==============Player:{name}===================")
number=random.randint(1, 10)
print(f'Well, {name}, I am thinking of a number between 1 and 10.')
for guessTaken in range(3):
    guess=int(input("Take a guess: "))
    
    if guess <number:
        print("Your guess is too low.")
    if guess>number:
        print("Your guess is too high")
    if guess==number:
        break
if guess==number:
    guessTaken=str(guessTaken+1)
    print(f'Good job, {name}, You guessed my Number! in {guessTaken} Guesses!')
if guess!=number:
    number=str(number)
    print(f'Oops!, the number I was thinking of was {number}') 
    
