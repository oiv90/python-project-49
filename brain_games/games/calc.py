import prompt
import random
from brain_games.cli import welcome_user


def generate_question():
    num = random.randint(1, 100)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return num, correct_answer


def game_round():
    result_message = 'OKAY MAN'
    return result_message, 1


def run_game():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    print('HELLO WORLD')

    points = 0
    while points < 3:
        result_message, result_point = game_round()
        print(result_message)
        if result_point == 0:
            print(f"Let's try again, {username}!")
            return
        points += result_point

    print(f'Congratulations, {username}!')
