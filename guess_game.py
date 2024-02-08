"""Welcome to the Word Guessing Game! Try to guess the secret word. The game provides hints for each guess based on the rules below:

Hints:
- Underscore (_) for letters not present in the secret word.
- Lowercase for correct letters in different spots.
- Uppercase for correct letters in the exact spot.

Enjoy the game!
"""

def word_guess_game():
    # Set the secret word for the user to guess
    secret_word = "mosiah"  # You can change this to any word you'd like
    guesses = 0  # Initialize the number of guesses

    # Initialize the hint with underscores for each letter in the secret word
    hint = ['_' for _ in secret_word]

    # Loop until the user guesses the correct word
    while True:
        # Display the current state of the word with underscores for unrevealed letters
        print("Current Hint:", ' '.join(hint))

        # Get the user's guess and convert it to lowercase for case-insensitivity
        user_guess = input("What is your guess? ").lower()
        guesses += 1  # Increment the number of guesses

        # Check if the length of the guess is the same as the length of the secret word
        if len(user_guess) != len(secret_word):
            print("Please enter a guess with the same length as the secret word.")
            continue

        # Check if the user's guess is correct
        if user_guess == secret_word:
            print("Congratulations! You guessed it!")
            print(f"It took you {guesses} guesses.")
            break  # Exit the loop if the guess is correct
        else:
            # Update the hint based on the rules provided
            for i, (secret_char, guess_char) in enumerate(zip(secret_word, user_guess)):
                if guess_char == secret_char:
                    hint[i] = guess_char.upper()  # Correct letter at the correct spot (uppercase)
                elif guess_char in secret_word:
                    hint[i] = guess_char.lower()  # Correct letter at a different spot (lowercase)

            print("Your guess was not correct.")

if __name__ == "__main__":
    word_guess_game()
