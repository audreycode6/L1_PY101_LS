'''Write a function that takes a short line of text and prints it within a box.'''

def print_in_box(string):
    if string == '':
        length = 2
        print('empty string')
    else:
        length = len(string)
        print(length)

    box_top = '+-' + ('-' * length) + '-+'
    space = '|' + (length * ' ') + '  |'
    text = '| ' + string + ' |'
    space = '|' + (length * ' ') + '  |'
    box_top = '+-' + ('-' * length) + '-+'
 
   
    print(box_top)
    print(space)
    print(text)
    print(space)
    print(box_top)


print_in_box('')
print_in_box('To boldly go where no one has gone before hehehhahs ehsrk svnl kvn sls erg.')