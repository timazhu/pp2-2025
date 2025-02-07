#Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:

import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

guess_the_number()

# Hello! What is your name?
# KBTU
# Well, KBTU, I am thinking of a number between 1 and 20.
# Take a guess.
# 10
# Your guess is too low.
# Take a guess.
# 19
# Your guess is too high.
# Take a guess.
# 15
# Your guess is too high.
# Take a guess.
# 14
# Your guess is too high.
# Take a guess.
# 13
# Your guess is too high.
# Take a guess.
# 11
# Good job, KBTU! You guessed my number in 6 guesses!