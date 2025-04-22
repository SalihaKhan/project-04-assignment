
def main():
    copy_message = []
    
    user_input = input("Enter a message to copy: ")
    message = " ".join([user_input] * 3)  # Joins 3 copies with spaces
    copy_message.append(message)
    print(message)

if __name__ == '__main__':
    main()
