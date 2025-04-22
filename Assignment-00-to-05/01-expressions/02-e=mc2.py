def main():

    speed_of_light = 299792458 


    print("Einstein's Mass-Energy Equivalence Calculator")
    print("Enter 'quit' to exit")

    while True:
        user_input = input("Enter kilos of mass : ").strip().lower()

        if user_input == "quit":
            print("Good bye")
            break;

        try:
            mass = float(user_input)
            energy = mass* (speed_of_light**2)
            print(f"Energy = m x c^2")
            print(f"Mass is {mass} kg")
            print(f"{energy} joules of energy")
        except ValueError:
            print("Please enter a valid number or 'quit' to exit")
if __name__ =='__main__':
    main()   