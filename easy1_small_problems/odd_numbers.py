# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# steps to convert input to output:
# 1. make a for loop with range 1,100 (stops before 100 == 99)
# 2. body of for loop:
#     condition: if even (i%2==0) continue, else print i

for i in range(1,100):
    if i % 2 == 0:
        continue
    else:
        print(i)

print() # space between mine and Ls answer

# LS answer to bonus question, use range step 2 to go over 2 each iteration
# i.e on iterate over odd
for number in range(1, 100, 2):
    print(number)

print()
# Consider adding a way for the user to specify the 
# starting and ending values of the odd numbers printed.

start = int(input("Enter a number to be the starting point: "))
end = int(input("Enter a number to be the end point: "))
if end < start:
        print("End point must be greater than starting point!")

for number in range(start, end):
    if number % 2 == 0:
        continue
    else:
        print(number)

