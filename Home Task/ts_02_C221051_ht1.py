"""
        Number Guessing Game
    To create a Python program where the user has to guess a
    randomly chosen number between 1 and 100 within 7 attempts.
"""
# Generate a random number between 1 and 100
import random # to generate a random number
import time # to set sleep time
import os # to clear terminal screen

random_number = random.randint(1, 100)

# Initialize the number of attempts used by the user
user_attempts = 0

# Initialize the maximum number of attempts allowed
max_attempts = 7

# Initialize the state of the game(whether the user has guessed the number or not)
guessed = False

# Print instructions for the user
print("\tHello User! Let's play a number guessing game.\n")
print("\tYou have to guess the number between 1 and 100.\n")
print("\tYou have 7 attempts to guess the correct number.\n")
print("\n\tClick 'Enter' to start the game.",end="")

# Wait for the user to press 'Enter' to start the game
input()

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# Promt user to select a mode
game_mode = int(input("\n\t1. Normal(7 attempts)\n\t2. Hard(3 attempts)\n\n\tSelect a mode : "))

# Set the max attempts to 3 if selected Hard mode
if game_mode == 2:
    max_attempts = 3
    print("\t You have selected the hard mode, Guess the correct number in 3 attempts\n")

# wait 3 seconds before starting the game
time.sleep(3)

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# Print the message regarding the start of the game
print("\tI have selected a random number between 1 and 100. Start guessing.....")

# Using for loop until the user has used all the attempts or guessed the number
for user_attempts in range(max_attempts):
    # Take the user input for the guessed number
    guessed_number = input(f"\n\tAttempt {user_attempts + 1}/{max_attempts} - Guess the number between 1 and 100 : ")
    # Check if user input is a number or not
    if not guessed_number.isdigit():
        """
            Clear the screen before printing
            the message to enter a valid number
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\tPlease enter a valid number.")
        # Skip this attempts if the user input is not a number
        continue
    # If the user input is a number, convert it to an integer
    else:
        guessed_number = int(guessed_number)
    
    # Check if the guessed number is correct or not
    if guessed_number == random_number:
        
        guessed = True
        # Exit the loop if the number is guessed correctly
        break
    
    # Check if the user has guessed outside the range of 1 to 100
    elif guessed_number not in range(1, 101):
        """
            Clear the screen before printing the hint
            message to guess the number between 1 and 100
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\tPlease guess the number between 1 and 100.")
        
    # Check if the guessed number is greater than the random number
    elif guessed_number < random_number:
        # Clear the screen before printing the hint message
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\tOpps! The number is greater than your guess. Try again.")
        
    # Check if the guessed number is smaller than the random number
    elif guessed_number > random_number:
        # Clear the screen before printing the hint message
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\tOpps! The number is smaller than your guess. Try again.")
            
# Check if the user has guessed the number or not
if guessed:
    # Clear the screen before printing the congratulatory message
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n\t\t\tCongratulations! You have guessed the ",end="")
    print(f"correct number {random_number} in {user_attempts + 1} attempts.\n")
else:
    # Clear the screen before printing the message for failing to guess the number
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n\t\tSorry! You have used all the attempts. The correct number was {random_number}.\n")