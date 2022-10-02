
from random import randint
from random import choice
import prompt


def main():
    print("Welcome to the Brain Games!")

    def welcome_user():
        name = prompt.string('May I have your name? ')
        print('Hello, ' + name + '!')
        print('What is the result of the expression?')

        cor_sum = 0
        i = 1
        while i <= 3:
            math_op = ['+', '-', '*']
            ran1 = randint(0, 99)
            ran2 = randint(0, 99)
            rmo = choice(math_op)
            term = str(ran1) + ' ' + rmo + ' ' + str(ran2)
            print('Question: ' + str(term)) 
            answer = input('Your answer: ')

            if rmo == '+':
                result = ran1 + ran2
                if result == int(answer):
                    print('Correct!')
                    i += 1
                    cor_sum += 1
                else:
                    print('\'' + str(answer) + '\' is wrong answer ;(. Correct answer was \'' + str(result) + '\'.')
                    print('Let\'s try again, ' + name + '!')
                    break

            elif rmo == '-':
                result = ran1 - ran2
                if result == int(answer):
                    print('Correct!')
                    i += 1
                    cor_sum += 1
                else:
                    print('\'' + str(answer) + '\' is wrong answer ;(. Correct answer was \'' + str(result) + '\'.')
                    print('Let\'s try again, ' + name + '!')
                    break

            else:
                result = ran1 * ran2
                if result == int(answer):
                    print('Correct!')
                    i += 1
                    cor_sum += 1
                else:
                    print('\'' + str(answer) + '\' is wrong answer ;(. Correct answer was \'' + str(result) + '\'.')
                    print('Let\'s try again, ' + name + '!')
                    break

        if cor_sum == 3:
            print('Congratulations, ' + name + '!')

    welcome_user()


if __name__ == "__main__":
    main()
