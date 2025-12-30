import random 
while True:
    print("Welcome to the Number Guessing Game!")
    print("The computer is thinking of a number between 1 and 100.")
    print("1. Easy 10 attempts")
    print("2. Medium 5 attempts")
    print("3. Hard 3 attempts")

    difficulty = input("Select your difficulty: ").lower()

    if difficulty == '1' or difficulty =="easy":
        break
    elif difficulty == '2' or difficulty =="medium":
        break
    elif difficulty == '3' or difficulty =="hard":
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or type easy, medium, or hard.")

comp_number = random.randint(1,100)

def number_guessing_game(comp_number, difficulty):
    if difficulty == "1" or difficulty.lower() == "easy":
        attempts = 10
        diff = "easy"
    elif difficulty == "2" or difficulty.lower() == "medium":
        attempts = 5
        diff = "medium"
    elif difficulty == "3" or difficulty.lower() == "hard":
        attempts = 3
        diff = "hard"
    num_attempts = 1
    print(f"Great! you selected {diff} difficulty")
    while True:
        
        try:
            player_number = int(input("Enter your guess: "))
            if player_number < 1 or player_number > 100:
                print("Please enter a number between 1 and 100")
            elif player_number < comp_number:
                attempts -= 1
                num_attempts += 1
                print(f"The number is greater then {player_number} you have {attempts} left")
                if attempts <= 0:
                 print("Sorry you ran out of attempts")
                 break
                 
            elif player_number > comp_number:
                attempts -=1
                num_attempts += 1
                print(f"The number is less then {player_number} you have {attempts} left")
                if attempts <= 0:
                 print("Sorry you ran out of attempts")
                 break
                 
            elif player_number == comp_number:
                print(f"Congratulations!! you guessed correctly. You did it in {num_attempts} attempts")
                break
        except ValueError:
            print("Please enter a valid number")
            continue

if difficulty == '1' or difficulty.lower() == "easy":
    number_guessing_game(comp_number, difficulty)
elif difficulty == '2' or difficulty.lower() == "medium":
    number_guessing_game(comp_number, difficulty)
elif difficulty == '3' or difficulty.lower() == "hard":
    number_guessing_game(comp_number, difficulty)
