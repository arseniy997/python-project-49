#!/usr/bin/env python3
import random
import brain_games.games.game_mechanic


''' Game 3 - “Greatest common divisor”. The user is shown
2 random mnumbers and must write the greatest common divisor.

The game is finished once a user gives 3 correct answers
or 1 incorrect answer.'''


rules_game_3 = 'Find the greatest common divisor of given numbers'


def get_question_answer_game_3():
    numbers = [random.randint(1, 100),
               random.randint(1, 100)]

    question_value = f'{numbers[0]} {numbers[1]}'

    if numbers[0] > numbers[1] is True:
        smallest_number = numbers[1]
    else:
        smallest_number = numbers[0]

    for i in range(smallest_number, 0, -1):
        if numbers[0] % i == 0 and numbers[1] % i == 0:
            correct_answer = str(i)
            break

    return [question_value, correct_answer]


def main():
    brain_games.games.game_mechanic.game_mechanic(rules_game_3,
                                                  get_question_answer_game_3)


if __name__ == '__main__':
    main()
