# Write a function that takes a number as an argument. 
# If the argument is a positive number, return the negative of that number.
#  If the argument is a negative number, return it as-is.


int = int(input('Enter a number: '))

def negative(int):
    if int > 0: # postive
        double = int * 2
        return int - double
    else: # negative
        return int
    
# TEST
print(negative(int))
print(negative(5) == -5)     # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True

# # OR
# def negative(int):
#     if int > 0: # postive
#         return - int 
#     else: # negative
#         return int

# OR
# def negative(int):
#         return -abs(int)