import random


def run_game_progression():
    length = random.randint(5, 10)
    step = random.randint(1, 10)
    start = random.randint(1, 20)
    expression = []
    for i in range(length):
        expression.append(str(start))
        start += step
    number_random = random.choice(expression)
    index_num = expression.index(number_random)
    expression[index_num] = '..'
    res = ' '.join(expression)
    return res, str(number_random)
