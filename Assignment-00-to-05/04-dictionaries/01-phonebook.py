def get_phone_book():
    phone_book = {}

    user_name = input("Enter your name: ")
    user_number = int(input("Enter your number: "))
    while True:
        if user_name =="":
            break
        else:
            phone_book[user_name] = user_number
    return phone_book

def print_phone_book(phone_book):
    for item in phone_book:
        print(str(item) + "->" + str(phone_book[item]) )

def check_num(phone_book):
    name = input("Enter a name: ")
    while True:
        if name == "":
            break;
        if name not in phone_book:
            print(name + " is not in the phonebook")
        else:
            print(phone_book[name])
def main():
    phonebook = get_phone_book()
    print_phone_book(phonebook)
    check_num(phonebook)

if __name__ == '__main__':
    main()