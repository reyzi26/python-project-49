#!/usr/bin/env python3
from ..games.brain_progression import run_game_progression
from ..games.general_module import general_function


def main():
    intro = 'What number is missing in the progression?'
    general_function(run_game_progression, intro)


if __name__ == '__main__':
    main()
