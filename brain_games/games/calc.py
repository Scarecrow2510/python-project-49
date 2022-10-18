"""Calc-game"""

from random import choice, randint
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100


def make_game():
    operand_first = randint(MIN_NUMBER, MAX_NUMBER)
    operand_second = randint(MIN_NUMBER, MAX_NUMBER)
    operation, operator = choice([(add, '+'), (sub, '-'), (mul, '*'), ])
    correct_answer = operation(operand_first, operand_second)
    question = f'{operand_first} {operator} {operand_second}'
    return question, str(correct_answer)
