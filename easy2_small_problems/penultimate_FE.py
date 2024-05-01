# Further Exploration
# Our solution ignored two edge cases since we explicitly stated that you didn't have to handle 
# them: strings that contain no words or just one word.

# Suppose we need a function that retrieves the middle word of a phrase/sentence. 
# What edge cases need to be considered? How would you handle those edge cases without ignoring 
# them? Write a function that returns the middle word of a phrase or sentence. 
# It should handle all of the edge cases you thought of.


string = input('Enter a sentence: ')

def penultimate(string):
    word_list = string.split()
    wl_length = len(word_list)
    half = wl_length // 2

    if wl_length < 2: # string too litte
        return 'Error: Must have more than 1 word!'
    
    elif wl_length == 2: # 2 words: no middle
        return f'2 words have no middle ==> "{string}"'
    
    elif wl_length % 2 == 0: # even: 2 middle words
        return f'Even amount of words, returning the 2 middle words: "{word_list[half - 1]}", "{word_list[half]}"'
    
    elif wl_length == 3: # 3 words
        return word_list[1]
    
    else: # not 3, odd
        return word_list[half]

# TEST
print(penultimate(string)) 
