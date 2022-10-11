from random import randint
import prompt


def main():
    print("Welcome to the Brain Games!")

    def welcome_user():
        name = prompt.string('May I have your name? ')
        print('Hello, ' + name + '!')
        print('What number is missing in the progression?')

        progression_length = 10
        cor_sum = 0
        i = 1

        while i <= 3:
            def get_progression(start, step, progression_length):
                end = start + (progression_length * step)
                progression = list(range(start, end, step))
                return progression

            def game():
                start = randint(1, 100)
                step = randint(1, 10)
                miss_index = randint(1, progression_length - 1)
                progression = get_progression(start, step, progression_length)
                global answer
                answer = progression.pop(miss_index)
                progression.insert(miss_index, '..')
                question = " ".join([str(i) for i in progression])
                return question

            start_game = game()
            print('Question: ' + start_game)
            user_answ = input('Your answer: ')

            if int(user_answ) == answer:
                print('Correct!')
                i += 1
                cor_sum += 1
            else:
                print('\'' + str(user_answ) + '\' is wrong answer ;(. '
                      'Correct answer was \'' + str(answer) + '\'.')
                print('Let\'s try again, ' + name + '!')
                break

            if cor_sum == 3:
                print('Congratulations, ' + name + '!')

    welcome_user()


if __name__ == "__main__":
    main()
