import prompt
from brain_games.game_constants import COUNT_ROUNDS


def engine_function(my_func, instruction):
    name = prompt.string("Welcome to the Brain Games!\nMay I have your name? ")
    print(f'Hello, {name}!\n{instruction}')
    count = 0
    for _ in range(COUNT_ROUNDS):
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
    if count == COUNT_ROUNDS:
        print(f'Congratulations, {name}!')
