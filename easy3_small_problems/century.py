'''Write a function that takes a year as input
and returns the century. The return value should
be a string that begins with the century number,
and ends with 'st', 'nd', 'rd', or 'th' as
appropriate for that number.

New centuries begin in years that end with 01.
So, the years 1901 - 2000 comprise the 20th century.'''

def get_century(year):
    '''helper function to century():
    returns int century from year input'''
    century_ = (year // 100) + 1
    if year < 100:
        century_ = 0
    elif year % 100 == 0:
        century_ -= 1
    return century_

def get_suffix(century_):
    '''helper function to century():
    determines ending to add century'''
    string_cent = str(century_)
    length = len(string_cent)
    last_char_cent = int(string_cent[-1:])
    if century_ == 0:
        return 'less than a century'

    # if 1 digit century
    if length < 2:
        if century_ == 1:
            return 'st'
        if century_ == 2:
            ending = 'nd'
        if century_ == 3:
            ending = 'rd'
        else: # 4, 5, 6, 7, 8, 9:
            ending = 'th'
        return ending

    penult_char_cent = int(string_cent[-2:-1])
    last2_chars = int(string_cent[-2:])
    # if century > 1 digit
    if last_char_cent == 1 and penult_char_cent != 1:
        ending = 'st'
    elif last_char_cent == 2 and penult_char_cent != 1:
        ending = 'nd'
    elif last_char_cent == 3 and penult_char_cent != 1:
        ending = 'rd'
    elif last_char_cent == 0 or (10 < last2_chars < 20):
        ending = 'th'
    else:
        ending = 'th'
    return ending

def format_century(year):
    '''main entry point:
    returns century + proper suffix
    of year arg'''
    century = get_century(year)
    century_string = str(century)
    suffix = get_suffix(century)
    if century == 0:
        return suffix
    return century_string + suffix

# TEST
print(format_century(2000))         # 20th
print(format_century(2001))         # 21th
print(format_century(1965))         # 20th
print(format_century(256))          # 3rd
print(format_century(5))            # less than a century
print(format_century(10103))        # 102nd
print(format_century(1052))         # 11th
print(format_century(1127))         # 12th
print(format_century(11201))        # 113th
print(format_century(2501))         # 26th
