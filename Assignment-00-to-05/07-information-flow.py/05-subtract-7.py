def subtract_seven(num):
    """Subtracts 7 from the given number."""
    return num - 7

def main():
    """Main function that demonstrates subtract_seven."""
    number = int(input("Enter a number: "))
    result = subtract_seven(number)
    print(f"{number} minus 7 equals {result}")

if __name__ == "__main__":
    main()