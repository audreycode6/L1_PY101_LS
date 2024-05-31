'''function that takes one argument, a positive integer, and 
returns a string of alternating '1's and '0's, always starting with a '1'. 
The length of the string should match the given integer.'''

def invalid_arg(num):
    '''helper function for string_01:
    try/catch for invalid argument'''
    try:
        if num > 0:
            return False
        return True
    except TypeError:
        return True

def string_01(num):
    '''main entry point'''
    if invalid_arg(num) is False:
        string_10 = ''
        for _ in range(num):
            digit = '1' if _ % 2 == 0 else '0'
            string_10 += digit
        return string_10
    return 'ERROR: Invalid argument: expecting an integer greater than 0.'

# TEST
print(string_01(3)) # 101
print(string_01('')) # ERROR: Invalid argument: expecting an integer greater than 0.
print(string_01(5)) # 10101
print(string_01(0)) # ERROR: Invalid argument: expecting an integer greater than 0.
print(string_01(10)) # 1010101010
