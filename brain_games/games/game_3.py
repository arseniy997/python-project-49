#!/usr/bin/env python3
import random
from brain_games.games.game_mechanic import run_game


''' Game 3 - “Greatest common divisor”. The user is shown
2 random mnumbers and must write the greatest common divisor.

The game is finished once a user gives 3 correct answers
or 1 incorrect answer.'''


RULES_GAME_3 = 'Find the greatest common divisor of given numbers.'


def generate_question_answer_game_3():
    numbers = [random.randint(1, 100),
               random.randint(1, 100)]

    question_value = f'{numbers[0]} {numbers[1]}'

    for i in range(min(numbers), 0, -1):
        if numbers[0] % i == 0 and numbers[1] % i == 0:
            return [question_value, str(i)]


def main():
    run_game(RULES_GAME_3, generate_question_answer_game_3)


if __name__ == '__main__':
    main()
