# Build a program that displays when the user will retire and 
# how many years she has to work till retirement.

# input: 2 int args --> ask user age and age for when they want to retire?
# output: how many years left to retire
# requires:
    # user input be translated to ints
    # variables to track: age, retire_age, time_left, current_year, retire_year
    # find current year (datetime module (?))
    # calc:  time_left = retire age - current age 
    # calc: what year will retire: time_left + current year

    # f-string years
    # f-string time left

# TODO:
import datetime

current_age = int(input('What is your age: ')) 
retire_age = int(input('At what age would you like to retire: ')) 

current_year = datetime.date.today().year

time_left = retire_age - current_age
retire_year = current_year + time_left

print(f"It's {current_year}. You will retire in {retire_year}.")

# OPTIONAL: options for what to print based on time_left
if time_left < 1: 
    print(f'You are so close! You have less than a year of work left!')
elif time_left == 1: 
    print(f'You have 1 more year of work left!')
else:
    print(f"You have only {time_left} years of work to go!") 

