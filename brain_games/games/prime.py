"""Prime-game"""

from random import randint

description = 'Answer "yes" if given number is prime. ' \
              'Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return 'no'
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return 'no'
    return 'yes'


def make_all_game():
    min_number = 1
    max_number = 100
    number = randint(min_number, max_number)
    question = str(number)
    return question, is_prime(number)
