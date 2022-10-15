"""Even-game"""

from random import randint

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_all_game():
    min_number = 1
    max_number = 99
    number = randint(min_number, max_number)
    question = str(number)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
