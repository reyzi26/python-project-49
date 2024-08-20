#!/usr/bin/env python3
from ..games.brain_gcd import run_game_gcd
from ..engine import engine_function
from ..game_constants import INSTRUCTION_GCD


def main():
    engine_function(run_game_gcd, INSTRUCTION_GCD)


if __name__ == '__main__':
    main()
