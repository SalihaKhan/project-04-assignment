def main():
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7]
    doubled_numbers = []  # Create an empty list to store the doubled values
    for i in numbers:
        doubled_numbers.append(i + i)  # Double each number and add it to the list
    
    print(doubled_numbers)  # Print out the entire list of doubled numbers

if __name__ == '__main__':
    main()

