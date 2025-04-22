def computer_guesses():
    print("Think of a number between 1 and 100, and I’ll try to guess it!")

    low = 1
    high = 100
    attempts = 0
    feedback = ""

    while feedback != "c":
        if low > high:
            print("Hmm, something went wrong. Are you giving honest feedback? 😅")
            break

        guess = (low + high) // 2
        attempts += 1

        print(f"My guess is {guess}.")
        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            print(f"🎉 Yay! I guessed your number in {attempts} tries.")
        else:
            print("Please enter 'H', 'L', or 'C'.")

# Run the game
computer_guesses()
