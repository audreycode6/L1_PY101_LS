# Write a function that returns the next to last word in the string argument.

# Words are any sequence of non-blank characters.

# You may assume that the input string will always contain at least two words.

string = input('Enter a sentence: ')

def penultimate(string):
    word_list = string.split()
    return word_list[-2]

# TEST
print(penultimate(string)) 


