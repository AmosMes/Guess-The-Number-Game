import random
from art import logo
import os

print(logo)

# Creating a function for cleaning the screan between games. The function will check if the computer running on linux or windows and will
# be executed either way.
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")

# Define a function for playing the game so we can call it recursivley later on when we win or lose a game and
# want to play again.
def play_game():
    random_number = random.randint(0, 100)

    #Creating a difficulty level for the game, hard will give 5 attempts and easy will give 10 attempts.
    difficulty = input(f"Choose your difficulty: 'hard' or 'easy': ").lower()
    lives = 0

    if difficulty == 'hard':
        lives += 5
    else:
        lives += 10
    print(f"You chose the {difficulty} difficulty, you have {lives} guesses to guess the number.")

    game_end = False

    while not game_end:
        guess = int(input(f"Please guess a number: "))
        if guess == random_number:
            game_end = True
            print(f"Congratulations, you were able to guess the right number which was {random_number}.")
        else:
            lives -= 1
        if lives == 0:
            print("You've ran out of guesses, you lose.")
            game_end = True
        if guess > random_number:
            print(f"Too high \nGuess again \nYou have {lives} guesses remaining.")
        elif guess < random_number:
            print(f"Too low \nGuess again \nYou have {lives} guesses remaining.")
play_game()

# Creating a while loop at the end of the game so we can give the user another go at it.
while input(f"Would you like to play again: 'y' or 'n' ") == 'y':
    clearConsole()
    play_game()
