#!/usr/bin/env python3
from ..games.brain_prime import run_game_prime
from ..engine import engine_function
from ..game_constants import INSTRUCTION_PRIME


def main():
    engine_function(run_game_prime, INSTRUCTION_PRIME)


if __name__ == '__main__':
    main()
