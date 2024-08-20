#!/usr/bin/env python3
from ..games.brain_progression import run_game_progression
from ..engine import engine_function
from ..game_constants import INSTRUCTION_PROGRESSION


def main():
    engine_function(run_game_progression, INSTRUCTION_PROGRESSION)


if __name__ == '__main__':
    main()
