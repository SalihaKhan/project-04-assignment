MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(f"Removed: {removed_item}")

def main():
    lst = []
    print("Enter list elements one at a time (enter 'done' when finished):")
    while True:
        element = input("> ")
        if element.lower() == 'done':
            break
        lst.append(element)
    
    print(f"\nOriginal list: {lst}")
    shorten(lst)
    print(f"Final list: {lst}")

if __name__ == '__main__':
    main()