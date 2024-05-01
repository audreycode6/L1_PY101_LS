# Write a function that returns a list that contains every other element of a list that is 
# passed in as an argument. The values in the returned list should be those values that are 
# in the 1st, 3rd, 5th, and so on elements of the argument list.


def oddities(input_list):
    return input_list[0:len(input_list):2] # OR simply: input_list[::2]

# TEST:
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

# non-slice way:
  # odd_elements = []
    # for element in range(0, len(input_list), 2):
    #     odd_elements.append(input_list[element])
    # return odd_elements

print()
# Further Exploration
# Write a companion function that returns the 2nd, 4th, 6th, and so on elements of a list.

def even_elements(list):
    if len(list) > 1:
        return list[1::2]
    return None

print(even_elements([2, 3, 4, 5, 6]) == [3, 5])  # True
print(even_elements([1, 2, 3, 4]) == [2, 4])     # True
print(even_elements(["abc", "def"]) == ['def'])  # True
print(even_elements([123]))                      # None
print(even_elements([]))                         # None