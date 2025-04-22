def get_first_element(lst):
    # Prints the first element of the list
    print(lst[0])

def main():
    lst = []
    print("Enter list elements one at a time (enter 'done' when finished):")
    while True:
        element = input("> ")  # Get user input
        if element.lower() == 'done':
            break
        lst.append(element)
    
    if lst:  # This check is redundant per problem statement, but good practice
        get_first_element(lst)
    else:
        print("The list is empty!")

if __name__ == '__main__':
    main()