#!/usr/bin/env python3
import random


def run_game_calc():
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    expression = f"{num_1} {operator} {num_2}"
    res = 0
    if operator == "+":
        res = num_1 + num_2
    elif operator == '-':
        res = num_1 - num_2
    else:
        res = num_1 * num_2
    return expression, str(res)
