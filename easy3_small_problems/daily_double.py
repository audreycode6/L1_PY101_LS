'''Write a function that takes a string argument and
returns a new string that contains the value of the
original string with all consecutive duplicate 
characters collapsed into a single character.'''
# TODO: clean up and use helper functions
def remove_duplicate_chars(string):
    '''take in string arg and if length of string > 2 
    loop through string and append non dupe chars to a new string'''
    need_final_char = ''
    length = len(string)

    if length > 2:
        current_char = 0
        next_char = 1
        last_char = string[-1]

        for char in string:
            # if not a dupe add to new string
            if char != string[next_char]:
                need_final_char += char
            if next_char == length - 1:
                no_dupe_string = need_final_char
                break
            current_char += 1
            next_char += 1
        # check if no_dupe_string's last char is dupe
        if len(no_dupe_string) > 1:
            penultimate_char = no_dupe_string[-2]
            if last_char != penultimate_char:
                no_dupe_string += last_char
            return no_dupe_string
        return string[0]
    return string

# TEST
print(remove_duplicate_chars('ddaaiillyy ddoouubbllee') == 'daily double')
print(remove_duplicate_chars('4444abcabccba') == '4abcabcba')
print(remove_duplicate_chars('ggggggggggggggg') == 'g')
print(remove_duplicate_chars('abc') == 'abc')
print(remove_duplicate_chars('a') == 'a')
print(remove_duplicate_chars('') == '')
