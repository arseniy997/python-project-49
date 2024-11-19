#!/usr/bin/env python3
import brain_games.cli
import brain_games.game_1


def main():
    user_name = brain_games.cli.welcome_user()
    brain_games.game_1.game_1(user_name)


if __name__ == '__main__':
    main()
