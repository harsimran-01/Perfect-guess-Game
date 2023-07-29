# Perfect-Guess-Game

import random

randomNumber = random.randint(1, 101)
userGuess = None
guesses = 0

while userGuess != randomNumber:
    userGuess = int(input("Please enter a Number : "))
    guesses += 1
    if userGuess == randomNumber:
        print("You won the game!!!")
    else:
        if userGuess > randomNumber:
            print("You Guessed too High!!") 
        elif userGuess < randomNumber:
            print("You Guessed too Low!!!")
        
print(f"You Guessed in {guesses} turns.")
