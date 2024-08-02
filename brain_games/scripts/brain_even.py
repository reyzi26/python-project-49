import random
from ..cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = input('Your answer: ')
        if ((answer == 'yes' and number % 2 == 0)
                or (answer == 'no' and number % 2 != 0)):
            count += 1
            print('Correct!')
        else:
            correct_answer = 'no'
            if answer == 'no':
                correct_answer = 'yes'
            print(f"{answer} is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
