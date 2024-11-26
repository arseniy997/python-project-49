#!/usr/bin/env python3
import random
from brain_games.games.game_mechanic import run_game


''' Game 5 - “Prime number”. The user is shown a random
number and must answer “yes” if it is prime or "no" if it is uneven.

The game is finished once a user gives 3 correct answers or 1 incorrect
answer (any answer except "yes" or "no" is counted as incorrect).'''


RULES_GAME_5 = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer_game_5():
    question_value = random.randint(1, 250)

    if question_value == 1:
        return [question_value, "yes"]

    for i in range(2, int(question_value ** 0.5 + 1)):
        if question_value % i == 0:
            return [question_value, "no"]

    return [question_value, "yes"]


def main():
    run_game(RULES_GAME_5, generate_question_answer_game_5)


if __name__ == '__main__':
    main()
