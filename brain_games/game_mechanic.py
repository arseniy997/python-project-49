#!/usr/bin/env python3
import prompt

import brain_games.cli

''' run_game() is a function that is responsible for the overall
logic (flow) of any brain game in the package.

run_game() welcomes a user, prints rules, gets user answer,
evaluates answer, shares evaluation with a user.

The user is shown a question and must answer it. Any game is finished
once a user gives 3 correct answers or 1 incorrect answer.

Each game has different rules (question), special function to generate
question and answer.'''


def run_game(rules, generate_pair_question_answer):
    user_name = brain_games.cli.welcome_user()
    print(rules)

    for i in range(1, 4):
        [question_value, correct_answer] = generate_pair_question_answer()
        print(f'Question: {question_value}')

        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print("Correct!")
        elif user_answer != correct_answer:
            return print(f'"{user_answer}" is wrong answer ;(. '
                         + f'Correct answer was "{correct_answer}". '
                         + f'Let\'s try again, {user_name}!')

    return print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    print('Cannot run this module. Run modules with games instead.')
