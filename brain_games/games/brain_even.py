import random


def run_game_even():
    expression = random.randint(1, 100)
    res = ''
    if expression % 2 == 0:
        res = 'yes'
    else:
        res = 'no'
    return expression, res
