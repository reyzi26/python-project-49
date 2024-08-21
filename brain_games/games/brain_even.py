import random


def get_random_number():
    num = random.randint(1, 100)
    return num


def run_game_even():
    expression = get_random_number()
    res = ''
    if expression % 2 == 0:
        res = 'yes'
    else:
        res = 'no'
    return expression, res
