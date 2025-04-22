import math
def main():
    print("By Using Pythagorean Theorem!!")

    AB = int(input("Enter the length of AB : "))
    AC = int(input("Enter the length of AC : "))

    BC = math.sqrt(AB**2 + AC**2)
    try:
         # Calculate hypotenuse using Pythagorean theorem
        print(f"The length of the hypotenuse is {BC}")
        
    except ValueError:
        print("Please enter valid number")    
if __name__ == '__main__':
    main()