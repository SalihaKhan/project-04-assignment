def main():
    print("This program calculates the sum of two integers.")
    while True:
        try:
             num1 = int(input("Enter first number: "))
             break
        except ValueError:
            print("Invalid input.")
    while True:
        try:
             num2 = int(input("Enter second number: "))
             break
        except ValueError:
            print("Invalid input.")        
    
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}.")

if __name__ == '__main__':
    main()
       

  

