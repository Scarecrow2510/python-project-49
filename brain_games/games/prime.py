"""Prime-game"""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. ' \
              'Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER - 100


def is_prime(number):
    if number == 1:
        return 'no'
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return 'no'
    return 'yes'


def make_game():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)
    return question, is_prime(number)
