#!/usr/bin/env python3
from ..games.brain_progression import run_game_progression
from ..games.general_module import general_function


def main():
    intro = 'Find the greatest common divisor of given numbers.'
    general_function(run_game_progression, intro)


if __name__ == '__main__':
    main()
