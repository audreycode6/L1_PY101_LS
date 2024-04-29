# Write a program that asks for user's name, then greets the user. 
# If the user appends a ! to their name, the computer will yell the greeting 
# (print it using all uppercase).

name = input("What is your name?: ")

def greeting(name):
    if name[-1] == '!':
        return f'HELLO {name.upper()} WHY ARE WE SO EXCITED?!' 
    else:
        return f'Hello {name.title()}.'
    
print(greeting(name))


# PEDAC:
    # input: input name
    # output: greet user based on input name: 
    # ! == HELLO name! WHY ARE WE SO EXCITED?! / else Hello Name.

    # steps to convert input to output:
    #name variable: input("What is your name?: ")
    # function take in name variable as arg
    # error if name empty
    # condtion if name has !  index(!) or find(!) --> greeting and name to upper
    # else: simple hello: f'Hello {name}. # maybe use title to have first char cap