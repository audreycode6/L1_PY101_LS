# Using the multiply function from the "Multiplying Two Numbers" exercise, 
# write a function that computes the square of its argument 
# (the square is the result of multiplying a number by itself).


def multiply(number1, number2):
    return number1 * number2

# def square(number):
#     return multiply(number,number)

# FE:
def square(exponent): 
    number1 = float(input('Enter a number to multiply: '))
    number2 = float(input(f'Enter another number to multiply to {number1}: '))
    return multiply(number1, number2) ** exponent


# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True


print(square(4)) 


# Further Exploration
# Suppose we want to generalize this function to a "power to the n" type function: 
# cubed, to the 4th power, to the 5th, etc. 
# How would we go about doing so while still using the multiply function?

#  change square body: return multiply(number, number) , change 2nd arg
# ** exponential