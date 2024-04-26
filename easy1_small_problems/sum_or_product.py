# Write a program that asks the user to enter an integer greater than 0, 
# then asks whether the user wants to determine the sum or the product of all numbers 
# between 1 and the entered integer, inclusive.


number = int(input("Please enter an integer greater than 0: "))
determine_s_p = input("Enter 's' to compute the sum, or 'p' to compute the product: ")

def sum_or_product(number, determine_s_p):
    if number <= 0:
        return "Try again! Input must be greater than 0."
    elif determine_s_p == 's':
        sum = 0
        for number in range(1,number+1):
            sum += number 
        return f"The sum of the integers between 1 and {number} is {sum}!"
    elif determine_s_p == 'p':
        product = 1
        for number in range(1,number+1):
            product *= number
        return f"The product of the integers between 1 and {number} is {product}!" 
    else: # not 's' or 'p'
        return "Try again! Input must be either: 's' OR 'p'!"  

print(sum_or_product(number, determine_s_p))  

# Further Exploration
# Suppose the input was a list of space separated integers instead of just 
# a single integer? How would your compute_sum and compute_product functions change?