''' Original: function that takes a short line of text and prints it
within a box. may assume the output will always fit in your terminal window.
Extension: Modify this function so that it truncates the message if 
it doesn't fit inside a maximum width provided as a second argument 
(the width is the width of the box itself). 
You may assume no maximum if the second argument is omitted. '''
# TODO (optional) figure out how to break them up by words
def split_string(string, length, width):
    '''helper function for print_in_box:
    take in args to have each chunk of 70 chars split into new lines'''
    dashes = width * '-'
    space_sides = width + 2
    top_bottom_format = f'+-{dashes}-+'
    box_space = space_sides * ' '

    last_loop = (length // width) + 1
    difference = (last_loop * width) - length
    add_extra_spaces = difference * ' '

    index = 1
    start = 0
    end = width
    print(top_bottom_format)
    print(f'|{box_space}|')
    for num in range(0, length, width):
        start = num
        if index == last_loop:
            print(f'| {string[start: end]}{add_extra_spaces} |')
        else:
            print(f'| {string[start: end]} |')
        end += width
        index += 1
    print(f'|{box_space}|')
    print(top_bottom_format)

def format_box(string, length):
    '''helper function to print_in_box:
    if string < width, format it to print in box'''
    dashes = length * '-'
    space_sides = length + 2
    top_bottom_format = f'+-{dashes}-+'
    box_space = space_sides * ' '

    print( f'''{top_bottom_format}
|{box_space}|
| {string} |
|{box_space}|
{top_bottom_format}''')

def print_in_box(string, width = 80):
    '''main entry point'''
    length = len(string)

    if length > width:
        split_string(string, length, width)

    else:
        format_box(string, length)

# TEST
TEST1 = '''As the persuasive summary of any book, film, or creative work. '''
TEST2 = ('Luke Skywalker has returned to '
'his home planet of Tatooine in '
'an attempt to rescue his '
'friend Han Solo from the '
'clutches of the vile gangster '
'Jabba the Hutt. '
'Little does Luke know that the '
'GALACTIC EMPIRE has secretly '
'begun construction on a new '
'armored space station even '
'more powerful than the first '
'dreaded Death Star. '
'When completed, this ultimate '
'weapon will spell certain doom '
'for the small band of rebels '
'struggling to restore freedom '
'to the galaxy...')
TEST3 = ('One challenge you may face in writing a book blurb is length.'
' While there’s no concrete best practice for blurb length, the rule of'
' thumb is to target between 100 and 200 words, with a rough average'
' of 150 words for back cover book blurbs. However, some blurbs can'
' be as few as 50 words and others as long as 250+ words.'
' It largely depends on the nature of the book, your audience,'
' and how much space you have to write.')
TEST4 = ('Compelling blurbs employ a mindful balance of promotion,'
' psychology, and creativity to highlight the core of a book’s contents'
' without revealing too much information. Think of it as a sales pitch that'
' reels in readers by invoking a sense of interest and curiosity.'
' Blurbs can also include short snippets about the author or quotes and'
' testimonials from acclaimed readers and critics. In short, there'
' are no hard rules for writing book blurbs. But some practices can help'
' sharpen your blurb artistry.')

print_in_box(TEST1)
print_in_box(TEST2, 70)
print_in_box('')
print_in_box(TEST3, 10)
print_in_box(TEST4)
