#Further Exploration
# Suppose the input was a list of space separated integers instead of just 
# a single integer? How would your compute_sum and compute_product functions change?


numbers = input("Please enter a list of integers seperated by spaces, ex. 1 2 3 4: ")
num_split = numbers.split() 
num_list = []
for number in num_split: 
   num_list.append(int(number)) # user input now ready to be used (num_list): list and number format!

determine_s_p = input("Enter 's' to compute the sum, or 'p' to compute the product: ")

def sum_or_product(num_list, determine_s_p):
    if len(num_list) <= 1:
        return "Try again! Must input a list numbers."
    elif determine_s_p == 's':
        sum = 0
        for number in num_list:  
            sum += number 
        return f"The sum of {num_list} is {sum}!"  
    elif determine_s_p == 'p':
        product = 1
        for number in num_list:
            product *= number
        return f"The product of {num_list} is {product}!"  
    else: # not 's' or 'p'
        return "Try again! Input must be either: 's' OR 'p'!"  

print(sum_or_product(num_list, determine_s_p))  
