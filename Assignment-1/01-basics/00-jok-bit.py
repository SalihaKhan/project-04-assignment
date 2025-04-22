JOKE = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs."
PROMPT = "What do you want?"  
SORRY = "Sorry! I only tell jokes.."

def main():
    print("Here's a simple joke bot!!")


    user_input = input(PROMPT)
    if user_input == "joke":
        print(JOKE.strip().lower())
    else:
        print(SORRY)    

if __name__ == '__main__':
    main()