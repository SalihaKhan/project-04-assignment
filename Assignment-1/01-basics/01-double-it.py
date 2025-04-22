# Ask the user to enter a number
curr_value  = int(input("Enter a number: "))

# Double the number and print until curr_value is 100 or greater
while curr_value < 100:
    curr_value = curr_value * 2
    print(curr_value, end=' ')

# Print a newline at the end for better formatting
print()