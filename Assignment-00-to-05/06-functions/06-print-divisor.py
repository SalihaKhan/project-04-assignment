def print_divisors(num):
    """Prints all divisors of the given number."""
    print(f"Here are the divisors of {num}:", end=" ")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print()  


def main():
    """Handles user input and calls print_divisors."""
    num = int(input("Enter a number: "))
    print_divisors(num)

if __name__ == "__main__":
    main()        