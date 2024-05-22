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
    # modify if duplicates : next to on another
    # return string with no duplicates
string = input('Enter a word or phrase: ')
def crunch(string):
    # print(set(string)) # does remove dups but scrambles string order ..

    set_string = set(string) # removes dupes
    string_length = len(string)
    if len(set_string) == string_length: # no dupes
        return string
    else: # has dupes
        # TODO: figure out how to alter string if has dupes
        for char in string:
            if string.count(char) > 1:
                dupe_char = char #hello --> l
                
                
                

                
    



print(crunch(string))
# These examples should all print True
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')