# Average.py Application - Calculates average of a series of project scores.
# By: Michael Bauer
# September 24, 2018


SENTINEL = -1
sum = 0
count = 0
score = float(input('Enter a project score: '))
while score != -1:
    count = count + 1
    sum = sum + score
    score = float(input('Enter a project score: '))
average = sum/count
print('\nThe average score on the project is ', average)
