import random
def main():
    print("Guess My Number")

    generated_num = random.randint(0 , 99)
    print("I am thinking of a number between 0 and 99... ")

    user_guess_num = int(input("Enter a guess: "))

    while user_guess_num < generated_num:
        if user_guess_num > generated_num:
            print("Your guess is too high")
        print("Your guess is too low")  

        print()
        user_guess_num = int(input("Enter a guess: "))
    print("Congrats!! You have choosed a right one..")    




# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()