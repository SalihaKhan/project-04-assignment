def greet(name):
    return name

def main():
    name = input("Enter your name here.")
    greetings = greet(name)
    print(f"Greetings {greetings}")

if __name__ == '__main__':
    main()    