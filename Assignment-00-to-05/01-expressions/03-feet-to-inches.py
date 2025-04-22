inches_to_foot = 12

def main():
    print("Convert feet into inches")

    user_input = int(input("Enter a number in feet for conversion into inches: "))

    conversion = user_input * inches_to_foot

    print(f"Here's the conversion of feet to inches {conversion}!!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()