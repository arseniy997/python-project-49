#!/usr/bin/env python3
import random
from brain_games.games.game_mechanic import run_game


''' Game 4 - “Arithmetic progression”. The user is shown
a list of mnumbers with 1 number missing and must write this number.

The game is finished once a user gives 3 correct answers
or 1 incorrect answer.'''


RULES_GAME_4 = 'What number is missing in the progression?'


def generate_question_answer_game_4():
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


def main():
    run_game(RULES_GAME_4, generate_question_answer_game_4)


if __name__ == '__main__':
    main()
