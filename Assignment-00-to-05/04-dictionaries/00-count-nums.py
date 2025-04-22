def main():
    print("Delete this line and write your code here! :)")

def user_num():
    user_numbers = []    
    """Get the number from the user"""
    user_input = int(input("Enter a number: "))  
    while True:

        if user_input == "":
            break
        else: 
            user_numbers.append(user_input) 
    return user_numbers

def count_num(num_lst):
    num_dict = {}
    for item in num_lst:
        if item not in num_dict:
            num_dict[item] = 1
        else:
            num_dict[item] += 1  
    return num_dict  

def print_counts(num_dict):
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")

def main():
    user_numbers = user_num()
    num_dict = count_num(user_numbers)
    print_counts(num_dict)        


if __name__ == '__main__':
    main()