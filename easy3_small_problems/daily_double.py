# Write a function that takes a string argument and returns a new string that 
# contains the value of the original string with all consecutive duplicate characters 
# collapsed into a single character.


#input: string
#output: new string with no duplicates of chars: ddubb --> dub
#requirements:
    # take in string
    # if string doesnt have duplicate chars return string unchanged
    # if string has duplicate chars modify string to not have duplicate chars
# TODO:
    # string input
    # define function takes in string
    # loop through chars and look for duplicates
    # store 1st char == next element if so pop if not continue and next char == 1st char?
    # modify if duplicates : next to one another
    # return string with no duplicates

# string = input('Enter a word or phrase: ')
def remove_duplicate_chars(string):
    if len(string) > 1: # if string longer than 1 char
        no_dupe_list = []
        length = len(string)
        next_index = 1

        for char in string:
            if char == string[next_index]:
                print(f'{char} is a dupe')
            else:
                no_dupe_list.append(char)
                # print(no_dupe_string)
            next_index += 1
            if next_index == length:
                last_char = string[-1]
                no_dupe_list.append(last_char)
                break # look up what break does, i think it just cancels whole function, does it return(?)
# TODO find out how to make no_dope_list to str 
        return(no_dupe_list)
    else: # if string less than 2 chars just return string
        return(string)

# remove_duplicate_chars(string)
# print(remove_duplicate_chars(string))



# str.replace(old, new[, count])Return a copy of the string with all occurrences of substring 
    # old replaced by new. If the optional argument count is given,
    # only the first count occurrences are replaced.
                
  

# These examples should all print True
print(remove_duplicate_chars('ddaaiillyy ddoouubbllee') == 'daily double')
print(remove_duplicate_chars('4444abcabccba') == '4abcabcba')
print(remove_duplicate_chars('ggggggggggggggg') == 'g')
print(remove_duplicate_chars('abc') == 'abc')
print(remove_duplicate_chars('a') == 'a')
print(remove_duplicate_chars('') == '')