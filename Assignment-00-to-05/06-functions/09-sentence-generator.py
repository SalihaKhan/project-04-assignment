def make_sentence(word, part_of_speech):
    """Prints a sentence with the word inserted based on its part of speech."""
    if part_of_speech == 0:  # Noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:  # Verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:  # Adjective
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech. Please enter 0, 1, or 2.")

def main():
    """Handles user input and calls make_sentence."""
    word = input("Please type a noun, verb, or adjective: ")
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

if __name__ == "__main__":
    main()