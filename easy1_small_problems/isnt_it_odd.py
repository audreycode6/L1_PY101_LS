# Write a function that takes one integer argument and returns 
# True when the number's absolute value is odd, False otherwise.

def is_odd(integer):
    if type(integer) != int: # check arg is whole number
        return "Must input an integer for the function's argument!"
    if integer % 2 == 0:
        return False
    else:
        return True

# TEST 
print(is_odd(0)) # False
print(is_odd(28)) # F
print(is_odd(37)) # T
# print(is_odd()) # error
# print(is_odd([5,10])) # error
print(is_odd(10.4)) # Must input an integer for the function's argument
print(is_odd(5.58)) # Must input an integer for the function's argument
# print(is_odd("Hi")) # error

# FOrgot to test for negatives!!
print(is_odd(-63849222)) # F
print()

# LS answer
def is_it_odd(number):
    return abs(number) % 2 == 1
# TEST
print(is_it_odd(0)) # False
print(is_it_odd(28)) # F
print(is_it_odd(37)) # T
# print(is_odd()) # error
# print(is_odd([5,10])) # error
print(is_it_odd(10.4)) # False
# print(is_it_odd("Hi")) # error