import random

def play_high_low(rounds=5):
    player_score = 0
    computer_score = 0
    
    print("Welcome to High-Low Game!")
    print(f"You'll play {rounds} rounds. Guess if your number is higher or lower than the computer's.")
    
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        
        # Generate numbers
        player_num = random.randint(1, 100)
        computer_num = random.randint(1, 100)
        
        print(f"Your number: {player_num}")
        
        # Get valid guess
        while True:
            guess = input("Is your number (H)igher or (L)ower than the computer's? ").upper()
            if guess in ['H', 'L']:
                break
            print("Invalid input. Please enter 'H' or 'L'.")
        
        # Determine outcome
        if (guess == 'H' and player_num > computer_num) or (guess == 'L' and player_num < computer_num):
            print("Correct! You earn a point.")
            player_score += 1
        elif player_num == computer_num:
            print(f"Tie! Both numbers were {player_num}. No points awarded.")
        else:
            print(f"Incorrect. Computer's number was {computer_num}. Computer earns a point.")
            computer_score += 1
    
    # Game results
    print("\n--- Game Over ---")
    print(f"Final Score - You: {player_score} | Computer: {computer_score}")
    
    if player_score > computer_score:
        print("Congratulations! You won!")
    elif player_score < computer_score:
        print("Computer wins. Better luck next time!")
    else:
        print("It's a tie!")

# Start the game with 5 rounds
play_high_low()