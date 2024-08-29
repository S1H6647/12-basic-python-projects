import random

def numGuess(x):
    randomNumber = random.randint(1,x) 
    print(f"Guess the number from 1 to {x}")
    guess = 0 # random number can never be 0 so the while loop keeps on running until Correct num hasn't been guessed
    while guess != randomNumber:
        guess = int(input("Guess the number: "))
        if guess< randomNumber:
            print("Try again. Too low")
        elif guess>randomNumber:
            print("Try again. Too high")

    print(f"You've guessed the correct number {randomNumber} correctly!")

x = int(input("Enter the max number you want to guess from: "))
numGuess(x)