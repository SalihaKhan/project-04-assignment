

def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))
    
    # Keep doubling until we reach 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the current value
        print(curr_value, end=' ')   # Print with space separator

    print()  # Add a newline at the end

if __name__ == '__main__':
    main()