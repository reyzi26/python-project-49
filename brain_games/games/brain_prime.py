import random


def get_random_number():
    num = random.randint(1, 100)
    return num


def run_game_prime():
    expression = get_random_number()
    count = 0
    res = ''
    for i in range(1, expression + 1):
        if expression % i == 0:
            count += 1
    if count == 2:
        res = 'yes'
    else:
        res = 'no'
    return expression, res
