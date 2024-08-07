import math
import random


def run_game_gcd():
    num_1 = random.randint(1, 11)
    num_2 = random.randint(1, 11)
    expression = f'{num_1} {num_2}'
    res = math.gcd(num_1, num_2)
    return expression, str(res)