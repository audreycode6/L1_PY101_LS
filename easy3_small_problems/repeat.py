'''Write a function that takes two arguments,
a string and a positive integer, then prints the 
string as many times as the integer indicates.'''

def repeat(string, num):
    if num < 1:
        print('Error: Enter a postive number!')
    for _ in range(num):
        print(string)

string = input('Enter a word or phrase: ')
num = int(input('Enter a postive number: '))
repeat(string, num)
