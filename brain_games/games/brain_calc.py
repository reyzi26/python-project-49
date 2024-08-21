import random


def get_random_number():
    num = random.randint(1, 100)
    return num


def get_random_math_sign_and_result(first_num, second_num):
    signs = ['+', '-', '*']
    sign = random.choice(signs)
    res = 0
    if sign == "+":
        res = first_num + second_num
    elif sign == '-':
        res = first_num - second_num
    else:
        res = first_num * second_num
    return sign, res


def get_math_question_and_result():
    first_num, second_num = get_random_number(), get_random_number()
    sign, result = get_random_math_sign_and_result(first_num, second_num)
    question = f'{first_num} {sign} {second_num}'
    return question, str(result)
