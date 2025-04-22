import random
import string

def generate_password(length, use_letters, use_digits, use_symbols):
    character_pool = ""

    if use_letters:
        character_pool += string.ascii_letters  # a-zA-Z
    if use_digits:
        character_pool += string.digits         # 0-9
    if use_symbols:
        character_pool += string.punctuation    # !@#$%^&*()_+ etc.

    if not character_pool:
        return "⚠️ You must choose at least one character type."

    if length < 4:
        return "⚠️ Password too short. Choose at least 4 characters."

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

# User input section
try:
    length = int(input("Enter desired password length: "))

    print("What should the password include?")
    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_letters, use_digits, use_symbols)
    print("🗝️ Your generated password:", password)

except ValueError:
    print("⚠️ Please enter a valid number for the length.")
