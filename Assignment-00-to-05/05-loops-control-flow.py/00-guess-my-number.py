import random

def main():
    number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99")
    
    while True:
        guess_number = int(input("Enter a number: "))
        
        if guess_number == number:
            print("Congrats!! Your guess is correct")
            break
        elif guess_number < number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Add blank line for better readability

if __name__ == '__main__':
    main()