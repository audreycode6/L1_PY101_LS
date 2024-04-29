# Write a program that prompts the user for two positive numbers (floating-point), 
# then prints the results of the following operations on those two numbers: 
# addition, subtraction, product, quotient, floor quotient, remainder, and power.
# Do not worry about validating the input.

# float input: 2 inputs: postive numbers
# output: print result of:
# addition (+), subtraction(-), product(iemultiply: *),quotient (iedivide /), floor quotient(//), remainder (%), power (**)
# requirments: take in 2 float inputs from user
# 7 arithmetic: (+, -, *, /, //, %, **)
# positive float, print error if number 1 or number2 < 0
# steps

number1 = float(input('Enter a postive number: '))
number2 = float(input('Enter a postive number: '))

if number1 or number2 >= 0:
    print() # LEFT OFF HERE!!
else:
    print('Error: Numbers entered must be greater than 0')

# EXAMPLES:
# ==> Enter the first number:
# 3.141529
# ==> Enter the second number:
# 2.718282
# ==> 3.141529 + 2.718282 = 5.859811
# ==> 3.141529 - 2.718282 = 0.42324699999999993
# ==> 3.141529 * 2.718282 = 8.539561733178
# ==> 3.141529 / 2.718282 = 1.1557038600115808
# ==> 3.141529 // 2.718282 = 1.0
# ==> 3.141529 % 2.718282 = 0.42324699999999993
# ==> 3.141529 ** 2.718282 = 22.45792517468373