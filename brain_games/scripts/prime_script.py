#!/usr/bin/env python3
from ..games.brain_prime import run_game_prime
from ..games.general_module import general_function


def main():
    intro = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    general_function(run_game_prime, intro)


if __name__ == '__main__':
    main()
