#!/usr/bin/env python3
from ..games.brain_calc import run_game_calc
from ..engine import engine_function
from ..game_constants import INSTRUCTION_CALC


def main():
    engine_function(run_game_calc, INSTRUCTION_CALC)


if __name__ == '__main__':
    main()
