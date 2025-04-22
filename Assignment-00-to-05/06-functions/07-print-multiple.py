def print_multiple(message, repeats):
    """Prints the message the specified number of times."""
    for _ in range(repeats):
        print(message, end=' ')
    print()  # Add a newline after all repetitions

def main():
    """Handles user input and calls print_multiple."""
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == "__main__":
    main()