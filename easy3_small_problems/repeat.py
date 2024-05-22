# Write a function that takes two arguments, a string and a positive integer, 
# then prints the string as many times as the integer indicates.

# input: 2 args, string and postive int
# output: string as many times as int
# requirements:
# 2 args: string, postive int (convert to int and return error if not positve)
# new line for each printing of string
# TODO:
# input(string)
# int(input('Enter a postive number: '))
# def function repeat(string, int)
# return string * 3 (play around with this)


string = input('Enter a word or phrase: ')
int = int(input('Enter a postive number: '))

def repeat(string, int):
    if int < 1:
        print('Error: Enter a postive number!')
    for number in range(int):
        print(string)
  
repeat(string, int)
