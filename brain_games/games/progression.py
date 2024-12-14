#!/usr/bin/env python3
import random

''' Game 4 - “Arithmetic progression”. The user is shown
a list of mnumbers with 1 number missing and must write this number.

The game is finished once a user gives 3 correct answers
or 1 incorrect answer.'''


GAME_RULES = 'What number is missing in the progression?'


def generate_question_answer():
    progression_length = random.randint(5, 10)
    first_number = random.randint(1, 50)
    progression_step = random.randint(1, 10)
    progression = [str(first_number)]

    for i in range(1, progression_length):
        y = int(progression[-1]) + progression_step
        progression.append(str(y))

    correct_answer = progression[random.randint(0, (progression_length - 1))]
    progression[progression.index(correct_answer)] = '..'

    return [' '.join(progression), correct_answer]


if __name__ == '__main__':
    print('Cannot run this module. Run brain_progression.py instead.')
