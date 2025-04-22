import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock")
    
    choices = ['rock', 'paper', 'scissors']
    score = {'player': 0, 'computer': 0}
    
    while True:
        print("\nMake your choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        
        try:
            player_choice = input("Enter your choice (1-4): ").strip()
            
            if player_choice == '4':
                print("\nFinal Scores:")
                print(f"Player: {score['player']}")
                print(f"Computer: {score['computer']}")
                print("Thanks for playing!")
                break
                
            player_choice = int(player_choice)
            if player_choice not in [1, 2, 3]:
                print("Please enter a number between 1 and 4")
                continue
                
            player_choice = choices[player_choice - 1]
            computer_choice = random.choice(choices)
            
            print(f"\nYou chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")
            
            if player_choice == computer_choice:
                print("It's a tie!")
            elif (
                (player_choice == 'rock' and computer_choice == 'scissors') or
                (player_choice == 'scissors' and computer_choice == 'paper') or
                (player_choice == 'paper' and computer_choice == 'rock')
            ):
                print("You win this round!")
                score['player'] += 1
            else:
                print("Computer wins this round!")
                score['computer'] += 1
                
            print(f"\nCurrent Score - Player: {score['player']} | Computer: {score['computer']}")
            
        except ValueError:
            print("Please enter a valid number!")
            
# Start the game
rock_paper_scissors()