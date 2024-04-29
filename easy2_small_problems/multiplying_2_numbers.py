# Create a function that takes two arguments, multiplies them together, and returns the result.

# input: 2 number args --> turn to ints
# return product of 2 args

number1 = float(input('Enter a number: '))
number2 = float(input('Enter another number: '))

def multiply(number1, number2):
    return number1 * number2
    
print(multiply(number1, number2))