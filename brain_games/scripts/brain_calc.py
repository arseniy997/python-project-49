#!/usr/bin/env python3
from brain_games.game_mechanic import run_game
from brain_games.games.calc import GAME_RULES, generate_question_answer

'''This script runs game #2 - "Calculator".'''


def main():
    run_game(GAME_RULES, generate_question_answer)


if __name__ == '__main__':
    main()
