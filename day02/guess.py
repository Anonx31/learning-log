# Import the random module
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize the user's guess
guess = 0

# Continue the game until the user guesses correctly
while guess != secret_number:

    # Ask the user to guess the number
    guess = int(input("Guess a number between 1 and 10: "))

    # Check if the guess is too low
    if guess < secret_number:
        print("Too low! Try again.")

    # Check if the guess is too high
    elif guess > secret_number:
        print("Too high! Try again.")

    # If neither condition is true, the guess is correct
    else:
        print("Congratulations! You guessed the correct number.")