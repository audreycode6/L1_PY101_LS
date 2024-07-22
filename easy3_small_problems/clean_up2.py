'''function that returns that string with all of the non-alphabetic 
characters replaced by spaces. If one or more non-alphabetic
characters occur in a row, you should only have one space
in the result (i.e., the result string should never have consecutive spaces).'''

def clean_up(string):
    clean_string = ''
    for index, char in enumerate(string):
        if char.isalpha():
            clean_string += char
        elif index == 0 or clean_string[-1] != ' ':
            clean_string += ' '
    return clean_string


print(clean_up("---what's my +*& line?")) # == " what s my line ")
# True