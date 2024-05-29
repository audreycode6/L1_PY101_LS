'''Write a function that determines the mean
(average) of the three scores passed to it,
and returns the letter associated with that grade.

Numerical score letter grade list:
90 <= score <= 100: 'A'
80 <= score < 90: 'B'
70 <= score < 80: 'C'
60 <= score < 70: 'D'
0 <= score < 60: 'F'
Tested values are all between 0 and 100.
There is no need to check for negative values or
values greater than 100.'''

def get_grade(score1, score2, score3):
    '''return grade from average of arg scores (0-100)'''
    average = (score1 + score2 + score3) // 3

    if 90 <= average <= 100:
        return 'A'
    if 80 <= average < 90:
        return 'B'
    if 70 <= average < 80:
        return 'C'
    if 60 <= average < 70:
        return 'D'
    return 'F'

# TEST
print(get_grade(95, 90, 93))    # True
print(get_grade(50, 50, 95))    # True

# OR ANOTHER WAY USING RANGE:
# if average in range(90, 101):
    #     return 'A'
    # if average in range(80, 90):
    #     return 'B'
    # if average in range(70, 80):
    #     return 'C'
    # if average in range(60, 70):
    #     return 'D'
    # if average in range(0, 60):
    #     return 'F'
    # return 'Scores not in grade range: 0-100'
