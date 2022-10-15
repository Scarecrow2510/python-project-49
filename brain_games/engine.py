"""Engine for all games"""


import prompt

max_rounds = 3


def run_game(game_name):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_name.description)
    round_num = 1
    while round_num <= max_rounds:
        question, correct_answer = game_name.make_all_game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let\'s try again, {user_name}!")
            break
        print('Correct!')
        round_num += 1
    else:
        print(f'Congratulations, {user_name}!')
