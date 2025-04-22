ADULT_AGE = 18  # Legal adult age in the United States

def is_adult(age):
    """Determines if a person is an adult based on their age."""
    return age >= ADULT_AGE

def main():
    """Handles user input and calls is_adult."""
    age = int(input("How old is this person?: "))
    print(is_adult(age))

if __name__ == "__main__":
    main()