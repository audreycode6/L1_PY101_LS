# Build a program that randomly generates and prints Teddy's age. 
# To get the age, you should generate a random number between 20 and 100, inclusive.

import random

age = random.randrange(20, 101)
print(f'Teddy is {age} years old!')

print()

# Further Exploration:
# Modify this program to ask for a name, then print the age for that person. 
# For an extra challenge, use "Teddy" as the name if no name is entered.

age = random.randrange(20, 101)
name_input = input('Enter a name: ')

if len(name_input) > 0: # if name input
    name = name_input
else: # no name input
    name = 'Teddy' 
print(f'{name.title()} is {age} years old!')
