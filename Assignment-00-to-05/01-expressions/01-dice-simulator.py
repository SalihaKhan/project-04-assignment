import random

roll_count = 2
dice_roll = 3
def rolled_dice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    return die1,die2
def main():
    current_roll = 1
    while current_roll <= dice_roll:
        first_die,second_die = rolled_dice()

        print(f"Roll {current_roll}")
        print(f"First Die : {first_die}")
        print(f"Second Die : {second_die}")
        print("-" * 15)
        current_roll += 1

if __name__ == '__main__':
    main() 

 