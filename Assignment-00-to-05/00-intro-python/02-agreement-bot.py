def get_favorite_animal():
    """Prompt the user for their favorite animal."""
    return input("What's your favorite animal? ").strip().title()

def respond_to_animal(animal):
    """Generate a response with the given animal."""
    return f"My favorite animal is also {animal}!"

def main():
    print("Welcome to the Animal Preference Program!")
    animal = get_favorite_animal()
    
    # Validate input isn't empty
    while not animal:
        print("Please enter an actual animal name!")
        animal = get_favorite_animal()
    
    print(respond_to_animal(animal))

if __name__ == "__main__":
    main()