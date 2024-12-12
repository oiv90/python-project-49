#!/usr/bin/env python
import prompt
import random


def welcome_user():
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    return username


def game_round():
    num = random.randint(1, 100)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ')
    result_message = 'Correct!' if answer == correct_answer else f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
    result_point = 1 if result_message == 'Correct!' else 0

    return result_message, result_point


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    points = 0

    while points < 3:
        result_message, result_point = game_round()
        print(result_message)
        points += result_point

    print(f'Congratulations, {username}!')


if __name__ == '__main__':
    main()
