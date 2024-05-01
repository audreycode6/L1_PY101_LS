# Write a program that prompts the user for two positive numbers (floating-point), 
# then prints the results of the following operations on those two numbers: 
# addition, subtraction, product, quotient, floor quotient, remainder, and power.
# Do not worry about validating the input.

number1 = float(input('==> Enter a postive number: '))
number2 = float(input('==> Enter a postive number: '))
add = number1 + number2
subtract = number1 - number2
product = number1 * number2
quotient = number1 / number2
floor_quotient = number1 // number2
remainder = number1 % number2
power = number1 ** number2

if number1 and number2 >= 0:
    print(f'==> {number1} + {number2} = {add}')
    print(f'==> {number1} + {number2} = {subtract}')
    print(f'==> {number1} + {number2} = {product}')
    print(f'==> {number1} + {number2} = {quotient}')
    print(f'==> {number1} + {number2} = {floor_quotient}')
    print(f'==> {number1} + {number2} = {remainder}')
    print(f'==> {number1} + {number2} = {power}')
    
# else: # OPTIONAL error message
#     print('Error: Numbers entered must be greater than 0')