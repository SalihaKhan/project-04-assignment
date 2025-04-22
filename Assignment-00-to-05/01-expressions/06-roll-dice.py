import random
def main():
    """Simulate rolling two dice, and prints results of each roll as well as the total."""

    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2

    print(f"First Die: {die1}")
    print(f"Second Die: {die2}")
    print(f"The total of the first and second die is {total}")




if __name__ == '__main__':
    main()