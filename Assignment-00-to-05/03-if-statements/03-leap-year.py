def main():
    print("Tell us the leap year or not.")
    user_input = int(input("Please input a year: ")) 
    
    
    if (user_input % 400 == 0) or (user_input % 4 == 0 and user_input % 100 != 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

if __name__ == '__main__':
    main()