# Create a number guessing game
# What is a number guessing game? A game where there a 2 or more players guessing a random number between a range
# There will be only two players, the computer and player
# the computer will give a random number and the player will input a number
# If the player guesses wrong the computer will say guess higher/lower
# if the player guess correctly the computer will say "You Won"
# The game will continue until the player guess correctly

import random

minimum_number = random.randint(1, 50)
maximum_number = random.randint(51, 100)

number = random.randint(minimum_number, maximum_number)

guess = 0

while number != guess:

    try:
        user_input = int(input(f"Enter a number between {minimum_number} and {maximum_number}: "))

        if user_input > number:
            print("Guess Lower")

        elif user_input < number:
            print("Guess Higher")

        else:
            print("You Won!!!")
            break

    except ValueError:
        print("That's not a valid number. Please enter an integer.")