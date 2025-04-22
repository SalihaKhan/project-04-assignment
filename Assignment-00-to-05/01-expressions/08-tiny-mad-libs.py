SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

def main():
    print("Let's create a fun sentence!")
    
    # Get user input
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")
    
    # Create and print the complete sentence
    full_sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"
    print(f"\n{full_sentence}")

if __name__ == '__main__':
    main()