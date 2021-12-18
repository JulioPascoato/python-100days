#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)

print("Welcome to he Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

is_game_over = False
computer_number = random.randint(1, 101)

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5


while not is_game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > computer_number:
        print("Too High.")
        print("Guess again.")
        attempts -= 1
    elif guess < computer_number:
        print("Too low.")
        print("Guess again.")
        attempts -= 1
    else:
        print(f"You got it! the answer was {computer_number}")
        is_game_over = True


    if attempts == 0:
        print("You've run out of guesses, you lose.")
        is_game_over = True
