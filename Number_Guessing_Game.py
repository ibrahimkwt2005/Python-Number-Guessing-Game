import random

comp_number = random.randint(1, 100)
attempts = 0
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
while True:
    try:
        player_guess = int(input("Make a guess: "))
        attempts += 1
        if player_guess < 1 or player_guess > 100:
            print("Please guess a number within the range of 1 to 100.")
            continue
        if player_guess < comp_number:
            print("")