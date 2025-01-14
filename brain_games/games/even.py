#!/usr/bin/env python3
import random

''' Game 1 - “Parity Check”. The user is shown a random number
and must answer “yes” if it is even or "no" if it is uneven.

The game is finished once a user gives 3 correct answers or 1 incorrect answer
(any answer except "yes" or "no" is counted as incorrect).'''


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer():
    question_value = random.randint(1, 500)

    if question_value % 2 == 0:
        correct_answer = "yes"
    elif question_value % 2 != 0:
        correct_answer = "no"

    return [question_value, correct_answer]


if __name__ == '__main__':
    print('Cannot run this module. Run brain_even.py instead.')
