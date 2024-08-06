#!/usr/bin/env python3
import prompt


def general_function(my_func, intro):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(intro)
    count = 0
    while count != 3:
        expression, res = my_func()
        print(f'Question: {expression}')
        answer = input('Your answer: ')
        if res == answer:
            count += 1
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was "
                  f"'{res}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
