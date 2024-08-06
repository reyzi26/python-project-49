#!/usr/bin/env python3
from ..games.brain_calc import run_game_calc
from ..games.general_module import general_function


def main():
    intro = 'What is the result of the expression?'
    general_function(run_game_calc, intro)


if __name__ == '__main__':
    main()
