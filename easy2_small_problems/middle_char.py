# Write a function that takes a non-empty string argument and returns the
# middle character(s) of the string. If the string has an odd length, 
# you should return exactly one character. If the string has an even length, 
# you should return exactly two characters.

string = input('Enter a word or sentence: ')

def center_of(string):
    length = len(string)
    center = length // 2

    if length < 1:
        return 'Error: Must input a word or sentence!'
    if length % 2 == 0:
        return string[center - 1] + string[center]
    else:
        return string[center]
    
print(center_of(string))

# print(center_of('I Love Python!!!') == "Py")    # True
# print(center_of('Launch School') == " ")        # True
# print(center_of('Launchschool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")                    # True