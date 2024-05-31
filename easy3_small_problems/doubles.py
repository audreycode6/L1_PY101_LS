'''A double number is an even-length number whose left-side 
digits are exactly the same as its right-side digits. 
For example, 44, 3333, 103103, and 7676 are all double numbers, 
whereas 444, 334433, and 107 are not.

Write a function that returns the number provided as an 
argument multiplied by two, unless the argument is a double number. 
If the argument is a double number, return the double number as-is.'''

def is_double_number(number):
    '''check if number is a double number:
    if double number: return number unchanged,
    else return number * 2'''

    string_number = str(number)
    num_length = len(string_number)
    middle = num_length // 2
    left_half = string_number[: middle]
    right_half = string_number[middle :]

    if num_length == 2 and string_number[0] == string_number[1]:
        return number
    if num_length % 2 == 0 and left_half == right_half:
        return number
    return number * 2

# TEST
print(is_double_number(9) == 18 )                  # True
print(is_double_number(37) == 74)                  # True
print(is_double_number(44) == 44)                  # True
print(is_double_number(334433) == 668866)          # True
print(is_double_number(444) == 888)                # True
print(is_double_number(107) == 214)                # True
print(is_double_number(103103) == 103103)          # True
print(is_double_number(3333) == 3333)              # True
print(is_double_number(7676) == 7676)              # True

# OR using helper function:
def is_double_num(number):
    '''helper function check if number is a double number:
    double number: return True.
    else return False'''
    string_number = str(number)
    num_length = len(string_number)
    middle = num_length // 2
    left_half = string_number[: middle]
    right_half = string_number[middle :]

    if num_length == 2 and string_number[0] == string_number[1]:
        return True
    if num_length % 2 == 0 and left_half == right_half:
        return True
    return False

def double_number_or_multiply(number):
    ''' main entry point:
    if double number: return number unchanged,
    else return number * 2'''
    return number if is_double_num(number) else number * 2

# TEST
print(double_number_or_multiply(9) == 18 )                  # True
print(double_number_or_multiply(37) == 74)                  # True
print(double_number_or_multiply(44) == 44)                  # True
print(double_number_or_multiply(334433) == 668866)          # True
print(double_number_or_multiply(444) == 888)                # True
print(double_number_or_multiply(107) == 214)                # True
print(double_number_or_multiply(103103) == 103103)          # True
print(double_number_or_multiply(3333) == 3333)              # True
print(double_number_or_multiply(7676) == 7676)              # True
