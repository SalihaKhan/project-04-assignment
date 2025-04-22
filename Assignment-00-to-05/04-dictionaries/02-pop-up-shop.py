def main():
    print()

fruit_prices = {
    'apple': 5.0,
    'durian': 15.0,
    'jackfruit': 10.0,
    'kiwi': 2.5,
    'rambutan': 8.0,
    'mango': 7.5
}

total_cost = 0

print("Welcome to the fruit shop!")
fruits = fruit_prices.keys()
print("Available fruits:", ", ".join(fruit_prices.keys()))
for fruits, price in fruit_prices.items():
    while True:
         quantity = int(input(f"How many ({fruits}) do you want?: "))
         if quantity >= 0:
             print("Please enter a positive number or zero.")
         else:
            total_cost += quantity * price
         print(f"\nYour total is ${total_cost:.2f}")   


if __name__ == '__main__':
    main()