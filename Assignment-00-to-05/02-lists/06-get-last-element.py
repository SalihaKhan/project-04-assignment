def get_last_element(lst):
    # Prints the last element of the list
    print(lst[-1])  # Negative index -1 refers to the last element

def main():
    lst = []
    print("Enter list elements one at a time (enter 'done' when finished):")
    while True:
        element = input("> ")
        if element.lower() == 'done':
            break
        lst.append(element)
    
    if lst:  # This check is redundant per problem statement, but good practice
        get_last_element(lst)
    else:
        print("The list is empty!")

if __name__ == '__main__':
    main()