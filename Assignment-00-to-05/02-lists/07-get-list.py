def main():
    items = []
    while True:
        user_input = int(input("Enter a value: "))
        if user_input == "":  # If user just presses Enter
            break
        items.append(user_input)
    
    print(f"Here's the list: {items}")

if __name__ == "__main__":
    main()