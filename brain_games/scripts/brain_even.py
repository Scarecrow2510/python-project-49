from random import randint
import prompt


def main():
    print("Welcome to the Brain Games!")

    def welcome_user():
        name = prompt.string('May I have your name? ')
        print('Hello, ' + name + '!')
        print('Answer "yes" if the number is even, otherwise answer "no".')

        Cor_Sum = 0
        i = 1

        while i <= 3:
            ran = randint(0, 99)
            print('Question: ' + str(ran))
            answer = input('Your answer: ')

            if ran % 2 != 0 and answer == 'yes':
                print('"yes" if wrong answer ;(. Correct answer was "no".\n'
                      'Let\'s try again, ' + name + '!')
                break

            elif ran % 2 != 0 and answer == 'no':
                print('Correct!')
                i = i + 1
                Cor_Sum = Cor_Sum + 1

            elif ran % 2 != 0:
                print(answer + 'is wrong answer ;(. Correct answer was "no".\n'
                               'Let\'s try again, ' + name + '!')
                break

            else:
                if ran % 2 == 0 and answer == 'yes':
                    print('Correct!')
                    i = i + 1
                    Cor_Sum = Cor_Sum + 1

                elif ran % 2 == 0 and answer == 'no':
                    print('"no" is wrong answer ;(. Correct answer was "yes".\n'
                          'Let\'s try again, ' + name + '!')
                    break

                else:
                    print(answer + ' is wrong answer ;(. '
                          'Correct answer was "yes".\n')
                    print('Let\'s try again, ' + name + '!')
                    break

        if Cor_Sum == 3:
            print('Congratulations, ' + name + '!')

    welcome_user()


if __name__ == '__main__':
    main()
