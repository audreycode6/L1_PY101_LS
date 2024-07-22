'''Write a function that takes a year as input and returns the century.
 The return value should be a string that begins with the century number,
 and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.
New centuries begin in years that end with 01. So, the years 1901
- 2000 comprise the 20th century. '''

'''helper function to century: returns suffix for input century'''
def add_suffix(century):
    str_century = str(century)
    last_char = str_century[-1]
    if str_century[-2:] in ['11', '12', '13']:
        suffix = 'th'
    elif last_char == '1':
        suffix = 'st'
    elif last_char == '2':
        suffix = 'nd'
    elif last_char == '3':
        suffix = 'rd'
    else:
        suffix = 'th'
    return suffix

'''main entry point: return century for input year'''
def century(year):
    if int(year) < 0:
        return 'Error: negative years do not exist, enter positive integer'
    century = (year // 100) + 1
    if year % 100 == 0:
        century = century - 1
    suffix = add_suffix(century)
    return str(century) + suffix

print(century(-2) == 'Error: negative years do not exist, enter positive integer')
print(century(2000) == "20th")          # True
print(century(200100))         # 2001st
print(century(2001) == "21st")  # True
print(century(1965) == "20th")  # True
print(century(256) == "3rd")  # True
print(century(5) == "1st")  # True
print(century(10103) == "102nd")  # True
print(century(1052) == "11th")  # True
print(century(1127) == "12th")  # True
print(century(11201) == "113th")  # True