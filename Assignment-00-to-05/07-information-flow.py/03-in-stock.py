def  num_in_stock(fruit):
    if fruit == "apple":
        return 2
    elif fruit == "pear":
        return 3
    elif fruit == "mango":
        return 4
    else:
        return 0

def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")    
        print(stock)

if __name__ == '__main__':
    main()        