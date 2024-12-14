#!/usr/bin/env python3
import random

''' Game 2 - “Calculator”. The user is shown a random mathematical
expression (only +, -, or *) and must calculate answer.

The game is finished once a user gives 3 correct answers
or 1 incorrect answer.'''


GAME_RULES = 'What is the result of the expression?'


def generate_question_answer():
    SYMBOLS = ('+', '-', '*')
    expression = [random.randint(1, 100),
                  random.randint(1, 10),
                  random.choice(SYMBOLS)]

    question_value = f'{expression[0]} {expression[2]} {expression[1]}'

    if expression[2] == '+':
        correct_answer = expression[0] + expression[1]
    elif expression[2] == '-':
        correct_answer = expression[0] - expression[1]
    else:
        correct_answer = expression[0] * expression[1]

    return [question_value, str(correct_answer)]


if __name__ == '__main__':
    print('Cannot run this module. Run brain_calc.py instead.')
