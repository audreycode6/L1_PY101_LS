'''Given a string that consists of some words 
and an assortment of non-alphabetic characters,
write a function that returns that string with
all of the non-alphabetic characters replaced by
spaces. 
If one or more non-alphabetic characters
occur in a row, you should only have one space in
the result (i.e., the result string should never
have consecutive spaces).'''
# pylint error: clean_up.py:23:0: R1710:
# Either all return statements in a function should return an
# expression, or none of them should. (inconsistent-return-statements)

def spaces_replace_non_alpha(string):
    '''helper function to clean_up():
    remove all non alpha digits from string 
    and replace with spaces'''
    alpha_string = ''
    for char in string:
        if not char.isalpha():
            char = ' '
        alpha_string += char
    return alpha_string

def remove_extra_spaces(alpha_string):
    '''helper function to clean_up():
    remove extra spaces from alpha_string'''
    no_space = ''
    next_char_index = 1
    alpha_string_length = len(alpha_string)
    last_char = alpha_string[-1]

    for char in alpha_string:
        # If char not consecutive space add to new no_string string
        if char != ' ' or (char == ' ' and char != alpha_string[next_char_index]):
            no_space += char
            next_char_index += 1
        else:
            next_char_index += 1
            continue
        if next_char_index == alpha_string_length:
            if last_char != char:
                no_space += last_char
            return no_space

def clean_up(string):
    '''main entry point:
    return original string with all
    non alpha digits replaced by spaces
    + removing any consecutive spaces'''
    alpha_string = spaces_replace_non_alpha(string)
    no_space = remove_extra_spaces(alpha_string)
    return no_space

# TEST
print(clean_up("---what's my +*& line?"))
print(clean_up("---what's my +*& line?") == " what s my line ")
print(clean_up("H! my*s"))
print(clean_up("H! my*s") == "H my s")
