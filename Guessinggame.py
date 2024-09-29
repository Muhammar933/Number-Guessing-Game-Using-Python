import random

# Step 1: Define a function for the guessing game
def guessing_game():
    # Step 2: Variables and Data Types
    secret_number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0  # To track the number of guesses
    guess = None  # The player's guess
    
    # Step 3: Tuples to define range
    valid_range = (1, 100)  # Tuple defining the range of valid numbers

    # Step 4: Game loop using while
    while guess != secret_number:
        # Step 5: Taking input and type casting
        guess = int(input(f"Guess a number between {valid_range[0]} and {valid_range[1]}: "))
        attempts += 1  # Increment the number of attempts

        # Step 6: Conditionals to check guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
    
    # Step 7: Storing the result in a dictionary
    result = {
        "secret_number": secret_number,
        "attempts": attempts,
    }
    return result  # Return the result for future use

# Step 8: Call the function to start the game
game_result = guessing_game()

# Optional: Store game history in a list (this can be expanded for multiple rounds)
game_history = []
game_history.append(game_result)

# Print game history using a loop (for example purposes)
print("Game History:")
for game in game_history:
    print(f"Secret Number: {game['secret_number']}, Attempts: {game['attempts']}")
