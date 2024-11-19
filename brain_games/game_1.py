#!/usr/bin/env python3
import random
import prompt


''' Game 1 - “Parity Check”. The user is shown a random number (random_number)
and must answer “yes” if it is even or "no" if it is uneven.

The game is finished once a user gives 3 correct answers or 1 incorrect answer
(any answer except "yes" or "no" is counted as incorrect).'''


def find_correct_answer(number):  # finds a correct answer for game_1()
    if number % 2 == 0:
        correct_answer = "yes"
    elif number % 2 != 0:
        correct_answer = "no"
    return correct_answer


def game_1(user_name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(1, 4):
        random_number = random.randint(1, 1000)
        print('Question: ' + str(random_number))

        user_answer = prompt.string('Your answer: ')
        correct_answer = find_correct_answer(random_number)

        if user_answer == correct_answer:
            print("Correct!")
        elif user_answer != correct_answer:
            return print(f'"{user_answer}" is wrong answer ;( '
                         + f'Correct answer was "{correct_answer}". '
                         + f'Let\'s try again, {user_name}!')


    return print(f'Congratulations, {user_name}!')
