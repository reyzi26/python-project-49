#!/usr/bin/env python3
from ..games.brain_gcd import run_game_gcd
from ..games.general_module import general_function


def main():
    intro = 'Find the greatest common divisor of given numbers.'
    general_function(run_game_gcd, intro)


if __name__ == '__main__':
    main()
