#!/usr/bin/env python3
from brain_games.games.even import GAME_RULES, generate_question_answer
from brain_games.game_mechanic import run_game


'''This script runs game #1 - "Parity Check".'''


def main():
    run_game(GAME_RULES, generate_question_answer)


if __name__ == '__main__':
    main()
