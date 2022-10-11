from random import randint
import prompt


def main():
    print("Welcome to the Brain Games!")

    def welcome_user():
        name = prompt.string('May I have your name? ')
        print('Hello, ' + name + '!')
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        cor_sum = 0
        i = 1

        while i <= 3:
            lower = 1
            upper = 100
            num = randint(lower, upper)
            question = str(num)
            print('Question: ' + question)
            answer = input('Your answer: ')

            def is_prime(num):
                if num == 1:
                    return 'no'
                for y in range(2, int(num ** 0.5 + 1)):
                    if num % y == 0:
                        return 'no'
                return 'yes'

            if answer == is_prime(num):
                print('Correct!')
                i += 1
                cor_sum += 1
            else:
                print('\'' + answer + '\' is wrong answer ;(. '
                      'Correct answer was \'' + is_prime(num) + '\'.')
                print('Let\'s try again, ' + name + '!')
                break

            if cor_sum == 3:
                print('Congratulations, ' + name + '!')

    welcome_user()


if __name__ == "__main__":
    main()
