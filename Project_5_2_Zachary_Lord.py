#!/usr/bin/env python3
#Zachary Lord

import random
#Display title initialization
def display_title():
    print("Guess the number!")
    print()

#Gets the limit of the range of numbers
def get_limit():
    limit = int(input("Enter the upper limit for the range of numbers: "))
    return limit

#plays the game
def play_game(limit):
    number = random.randint(1, limit)
    print("I'm thinking of a number from 1 to " + str(limit) + "\n")
    count = 1
    while True:
        guess = int(input("Your guess: "))
        print(guess)
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
        elif guess == number:
            print("You guessed it in " + str(count) + " tries.\n")
            return

def main():
    display_title()
    again = "y"
    #While loop to see if the user wants to play again.
    while again.lower() == "y":
        limit = get_limit()
        play_game(limit)
        again = input("Play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

