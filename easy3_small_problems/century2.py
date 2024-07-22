'''Write a function that takes a year as input and returns the century.
 The return value should be a string that begins with the century number,
 and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.
New centuries begin in years that end with 01. So, the years 1901 - 2000
comprise the 20th century.'''

'''Write a function that takes a year as input and returns the century.
 The return value should be a string that begins with the century number,
 and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.
New centuries begin in years that end with 01. So, the years 1901 - 2000
comprise the 20th century.'''
# LS uses pattern (year % 100)

def add_suffix(century):
    str_century = str(century)
    if len(str_century) >= 2:
        if (str_century in ['11', '12', '13'] or
            str_century[1:] in ['11', '12', '13']):
            suffix = 'th'
            return suffix

    last_char = str_century[-1]
    match last_char:
        case '1':
            suffix = 'st'
        case '2':
            suffix = 'nd'
        case '3':
            suffix = 'rd'
        case _:
            suffix = 'th'
    return suffix

def century(year):
    if int(year) < 0:
        return 'Error: negative years do not exist, enter positive integer'
    string_year = str(year)
    century_string_length = len(string_year)
    if century_string_length < 3:
        century = 1
    else:
        digits_after_century = century_string_length - 2
        if string_year[digits_after_century:] != '00':
            century = int(string_year[:digits_after_century]) + 1
        else:
            century = string_year[:digits_after_century]

    suffix = add_suffix(century)
    century = str(century)
    return century + suffix
    
print(century(-2) == 'Error: negative years do not exist, enter positive integer')          # True
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

# BEFORE: else in century
#     elif century_string_length == 3: # century = ### (3 == [1:]/ [0], len - 2)
#         if string_year[1:] != '00':
#             century = int(string_year[0]) + 1
#         else:
#             century = string_year[0]
#     elif century_string_length == 4: # century = #### (4 == [2:]/ [:2], len -2)
#         if string_year[2:] != '00':
#             century = int(string_year[:2]) + 1
#         else:
#             century = string_year[0:2]
#     elif century_string_length == 5: # century = ##### (5 == [3:] / [:3], len - 2)
#         if string_year[3:] != '00':
#             century = int(string_year[:3]) + 1
#         else:
#             century = string_year[:3]
