import random

def user_guesses():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("🎮 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != number_to_guess:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! 🔽")
            elif guess > number_to_guess:
                print("Too high! 🔼")
            else:
                print(f"🎉 Congrats! You guessed it in {attempts} tries.")
        except ValueError:
            print("Please enter a valid number!")

# Run the game
user_guesses()
