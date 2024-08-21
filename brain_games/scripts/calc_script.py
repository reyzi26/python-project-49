#!/usr/bin/env python3
from ..games.brain_calc import get_math_question_and_result
from ..engine import engine_function
from ..game_constants import INSTRUCTION_CALC


def main():
    engine_function(get_math_question_and_result, INSTRUCTION_CALC)


if __name__ == '__main__':
    main()
