# Create a simple tip calculator. The program should prompt for a bill amount 
# and a tip rate. The program must compute the tip, then print both the tip and 
# the total amount of the bill.
#  You can ignore input validation and assume that the user will enter valid numbers.


bill = float(input('What is the bill? \n$'))
tip_rate = float(input('What is the tip percentage? \n%: '))

def tip_and_bill(bill, tip_rate):
    tip_percent = tip_rate * .01 # convert to decimal format 
    tip = tip_percent * bill
    total_bill = tip + bill
    print(f'The tip is ${tip:.2f}\nThe total is ${total_bill:.2f}')

tip_and_bill(bill, tip_rate)
     