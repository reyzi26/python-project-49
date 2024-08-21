import random


def get_random_numbers(start, stop):
    num = random.randint(start, stop)
    return num


def get_expression():
    length = get_random_numbers(5, 10)
    step = get_random_numbers(1, 10)
    start = get_random_numbers(1, 20)
    expression = []
    for _ in range(length):
        expression.append(str(start))
        start += step
    return expression


def run_game_progression():
    expression = get_expression()
    number_random = random.choice(expression)
    index_num = expression.index(number_random)
    expression[index_num] = '..'
    res = ' '.join(expression)
    return res, str(number_random)
