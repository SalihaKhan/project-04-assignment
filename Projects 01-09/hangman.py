import random
import string

def hangman():
    # Word selection
    words = ["python", "programming", "hangman", "computer", "keyboard", "developer", "algorithm"]
    secret_word = random.choice(words).lower()
    letters_to_guess = set(secret_word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    lives = 6

    # Game introduction
    print("Welcome to Hangman!")
    print(f"Guess the word. It has {len(secret_word)} letters.")
    
    # Game loop
    while len(letters_to_guess) > 0 and lives > 0:
        # Display current status
        word_list = [letter if letter in used_letters else '_' for letter in secret_word]
        print("\nCurrent word:", ' '.join(word_list))
        print(f"Lives left: {lives}")
        print("Used letters:", ' '.join(sorted(used_letters)))
        
        # Get user input
        user_letter = input("Guess a letter: ").lower()
        
        # Validate input
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in letters_to_guess:
                letters_to_guess.remove(user_letter)
                print("Good guess!")
            else:
                lives -= 1
                print(f"Wrong! The letter {user_letter} is not in the word.")
                print_hangman(lives)
        elif user_letter in used_letters:
            print("You've already used that letter. Try again.")
        else:
            print("Invalid input. Please enter a single letter.")

    # Game conclusion
    if lives == 0:
        print("\nYou lost! The word was:", secret_word)
        print_hangman(lives)
    else:
        print(f"\nCongratulations! You guessed the word: {secret_word}")

def print_hangman(lives):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    print(stages[lives])

# Start the game
hangman()