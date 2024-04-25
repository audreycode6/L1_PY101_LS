# Print all even numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the even numbers?

# steps to convert input to output:
# make a for loop with range 1,100, test out what happens if we use step 2
# make loop body with conditon to check if odd or even
# odd == continue
# even == print
# code


# start range at 2 to iterate over evens only; if start with 1 will end up skipping all evens
for number in range(2, 100, 2): 
    if number % 2 == 0:
        print(number)
    else:
        continue

