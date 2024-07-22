'''Write a function that takes a string argument and 
returns a new string that contains the value of the original
 string with all consecutive duplicate characters collapsed 
 into a single character.'''

''' Take in stirng arg and return string with all consecutive duplicates char removed '''
def crunch(string):
    no_dupes_str = ''
    for index, char in enumerate(string):
        if index == 0 or char != no_dupes_str[-1]:
            no_dupes_str += char

    return no_dupes_str 

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')