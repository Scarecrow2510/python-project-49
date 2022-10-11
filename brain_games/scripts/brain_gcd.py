from random import randint
import prompt
import math


def main():
    print("Welcome to the Brain Games!")

    def welcome_user():
        name = prompt.string('May I have your name? ')
        print('Hello, ' + name + '!')
        print('Find the greatest common divisor of giver numbers.')

        cor_sum = 0
        i = 1

        while i <= 3:
            ran1 = randint(0, 99)
            ran2 = randint(0, 99)
            gcd = math.gcd(ran1, ran2)
            print('Question: ' + str(ran1) + ' ' + str(ran2))
            answer = input('Your answer: ')

            if int(answer) == gcd:
                print('Correct!')
                i += 1
                cor_sum += 1
            else:
                print('\'' + answer + '\' is wrong answer ;(. '
                      'Correct answer was \'' + str(gcd) + '\'.')
                print('Let\'s try again, ' + name + '!')
                break

        if cor_sum == 3:
            print('Congratulations, ' + name + '!')

    welcome_user()


if __name__ == "__main__":
    main()
