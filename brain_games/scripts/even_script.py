#!/usr/bin/env python3
from ..games.brain_even import run_game_even
from ..engine import engine_function
from ..game_constants import INSTRUCTION_EVEN


def main():
    engine_function(run_game_even, INSTRUCTION_EVEN)


if __name__ == '__main__':
    main()
