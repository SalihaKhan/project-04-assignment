def print_ones_digit(num):
    """Prints the ones digit of a given integer."""
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    """Handles user input and calls print_ones_digit."""
    num = int(input("Enter a number: "))
    print_ones_digit(num)

if __name__ == "__main__":
    main()