import time

def main():
    print("\n🌟 MAD LIBS GENERATOR 🌟")
    print("\nChoose a story:")
    print("1. The Crazy Vacation")
    print("2. The Spooky Night")
    print("3. The Silly Job Interview")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == "1":
        the_crazy_vacation()
    elif choice == "2":
        the_spooky_night()
    elif choice == "3":
        the_silly_job_interview()
    else:
        print("Invalid choice! Try again.")
        time.sleep(1)
        main()  # Restart if input is wrong

def the_crazy_vacation():
    print("\n--- THE CRAZY VACATION ---")
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb (past tense): ")
    food = input("Enter a type of food: ")
    animal = input("Enter an animal: ")
    
    print("\nHere's your Mad Libs story:")
    print(f"Last summer, I went on a {adjective1} trip to {noun1}.")
    print(f"I {verb1} so much that I ate {food} for breakfast,")
    print(f"and then a wild {animal} chased me all the way home!")

def the_spooky_night():
    print("\n--- THE SPOOKY NIGHT ---")
    place = input("Enter a spooky place: ")
    monster = input("Enter a scary monster: ")
    weapon = input("Enter a weapon: ")
    sound = input("Enter a scary sound: ")
    
    print("\nHere's your Mad Libs story:")
    print(f"One dark night, I wandered into {place}.")
    print(f"Suddenly, a {monster} jumped out and roared!")
    print(f"I grabbed my {weapon} and heard {sound}...")
    print("I ran away as fast as I could!")

def the_silly_job_interview():
    print("\n--- THE SILLY JOB INTERVIEW ---")
    job = input("Enter a weird job title: ")
    skill = input("Enter a useless skill: ")
    celebrity = input("Enter a famous person: ")
    object = input("Enter a random object: ")
    
    print("\nHere's your Mad Libs story:")
    print(f"So, you want to be a {job}? Interesting!")
    print(f"Can you demonstrate your skill in {skill}?")
    print(f"Great! Now, pretend this {object} is {celebrity}.")
    print("You're hired... maybe.")

if __name__ == "__main__":
    main()