'''Madlibs is a simple game where you create a story 
template with "blanks" for words. You, or another player, 
then construct a list of words and place them into the story,
creating an often silly or funny story as a result.

Create a simple madlib program that prompts for a noun,
a verb, an adverb, and an adjective, and injects them 
into a story that you create.'''

def display_welcome():
    '''helper function to madlibs():
    welcome message'''
    print('Welcome to the Launch School Madlib!\n')

def prompt(message):
    '''helper function to madlibs():
    format prompts'''
    print(f"==> {message}")

def get_noun():
    '''helper function to madlibs():
    get noun input'''
    prompt('Enter a noun (person, place or thing [ex: dog]) ')
    return input()

def get_verb():
    '''helper function to madlibs():
    get verb input'''
    prompt('Enter a verb (describes an action [ex: walk]) ')
    return input()

def get_adjective():
    '''helper function to madlibs():
    get adjective input'''
    prompt('''Enter an adjective
(describes a person, place, animal, object, thing, or thought [ex: blue]) ''')
    return input()

def get_adverb():
    '''helper function to madlibs():
    get adverb input'''
    prompt('Enter an adverb (describes a verb [ex: slowly] ')
    return input()

def madlibs():
    '''main entry point: 
    display madlibs program'''
    display_welcome()
    noun = get_noun()
    verb = get_verb()
    adjective = get_adjective()
    adverb = get_adverb()
    story = (f'I am a {noun} at Launch School.'
    f' At Launch School you learn how to {verb}!'
    f' If I get stuck on a problem, I {adverb} solve it.'
    f' Launch School is really {adjective}! ')
    return f'\nLaunch School: \n{story}'

print(madlibs())
