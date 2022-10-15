"""GCD-game"""

from math import gcd
from random import randint

description = 'Find the greatest common divisor of given numbers.'


def make_all_game():
    min_number = 1
    max_number = 99
    number_first = randint(min_number, max_number)
    number_second = randint(min_number, max_number)
    question = f'{number_first} {number_second}'
    correct_answer = gcd(number_first, number_second)
    return question, str(correct_answer)
