import math
import random


def get_random_number():
    num = random.randint(1, 11)
    return num


def get_result(first_number, second_number):
    result = math.gcd(first_number, second_number)
    return result


def run_game_gcd():
    first_number, second_number = get_random_number(), get_random_number()
    expression = f'{first_number} {second_number}'
    result = get_result(first_number, second_number)
    return expression, str(result)
