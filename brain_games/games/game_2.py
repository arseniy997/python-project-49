#!/usr/bin/env python3
import random
from brain_games.games.game_mechanic import game_mechanic


''' Game 2 - “Calculator”. The user is shown a random mathematical
expression (only +, -, or *) and must calculate answer.

The game is finished once a user gives 3 correct answers
or 1 incorrect answer.'''


RULES_GAME_2 = 'What is the result of the expression?'


def generate_question_answer_game_2():
    symbols = ('+', '-', '*')
    expression = [random.randint(1, 100),
                  random.randint(1, 10),
                  random.choice(symbols)]

    question_value = f'{expression[0]} {expression[2]} {expression[1]}'

    if expression[2] == '+':
        correct_answer = expression[0] + expression[1]
    elif expression[2] == '-':
        correct_answer = expression[0] - expression[1]
    else:
        correct_answer = expression[0] * expression[1]

    return [question_value, str(correct_answer)]


def main():
    game_mechanic(RULES_GAME_2, generate_question_answer_game_2)


if __name__ == '__main__':
    main()
