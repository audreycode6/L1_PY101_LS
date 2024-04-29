# Write a function that computes the sum of all numbers between 1 and some other number, inclusive,
# that are multiples of 3 or 5. For instance, if the supplied number is 20, 
# the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# You may assume that the number passed in is an integer greater than 1.

# steps to convert input to output:
# define function multisum(number) # maybe use int(input) to manually put in arg
# intialize empty list: number_range
# loop through range(1,number+1) and .append to new list: number_range
# intialize empty list: multiples_list
# loop through number_range and check if number multiple of 3 or 5, append to multiples_list
# loop through multiples_list and add each num to itself +=, intialize sum = 0
# return sum!


number = int(input("Enter a number greater than 0: "))

def multisum(number):
    multiples_list = []
    for num in range(1, number+1): # loop number_range to new list of multiples from number_range: multiples_list
        if num % 3 == 0 or num % 5 == 0:
            multiples_list.append(num)

    if len(multiples_list) > 0: # check if multiples present, ie. multiples_list has multiple(s)
        sum = 0 # initialize to 0 so it can add all multiples without being altered
    else:
        return 'No multiples found!' 
    
    for num in multiples_list: # loop through multiples_list and add each number together
        sum += num
    return sum

print(multisum(number))  

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)