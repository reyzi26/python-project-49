#!/usr/bin/env python3
from ..games.brain_even import run_game_even
from ..games.general_module import general_function


def main():
    intro = 'Answer "yes" if the number is even, otherwise answer "no".'
    general_function(run_game_even, intro)


if __name__ == '__main__':
    main()
