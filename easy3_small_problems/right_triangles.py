'''function that takes a positive integer, n, as an argument 
and prints a right triangle whose sides each have n stars.
The hypotenuse of the triangle (the diagonal side in the images below)
should have one end at the lower-left of the triangle,
and the other end at the upper-right.'''

def valid_arg(num):
    '''helper function for triangle():
    check that arg is valid'''
    try:
        if num > 0:
            return True
        return False
    except TypeError:
        return False

def triangle(num):
    '''main entry point'''
    if valid_arg(num):
        for _ in range(num):
            space_before_stars = num - (_ + 1)
            spaces = ' ' * space_before_stars
            stars = '*' * (_ + 1)
            print(f'{spaces + stars}')
    else:
        print('ERROR: Your arg must be an integer greater than 0.')

# TEST
triangle(5)
triangle(9)
triangle(0)
triangle(-2)
triangle('')
