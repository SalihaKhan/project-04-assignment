def count_even():
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break  # Stop if user presses Enter
        try:
            num = int(user_input)
            lst.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer or press enter to stop.")
    
    # Count even numbers
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
    
    print(f"Number of even numbers: {even_count}")

# Example usage
count_even()