import prompt

from brain_games.cli import welcome_user
from brain_games.games import calc, even, gcd, prime, progression


def select_game(game_name):
    match game_name:
        case "even":
            return even
        case "calc":
            return calc
        case "gcd":
            return gcd
        case "progression":
            return progression
        case "prime":
            return prime


def game_round(game):
    num, correct_answer = game.generate_question()
    print(f"Question: {num}")
    answer = prompt.string("Your answer: ")
    correct_mess = "Correct!"
    wrong_mess = (
        f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
    )
    result_message = correct_mess if answer == correct_answer else wrong_mess
    result_point = 1 if result_message == "Correct!" else 0
    return result_message, result_point


def run_game(game_name):
    print("Welcome to the Brain Games!")

    username = welcome_user()
    game = select_game(game_name)
    print(game.HELLO_MESSAGE)

    points = 0
    while points < 3:
        result_message, result_point = game_round(game)
        print(result_message)
        if result_point == 0:
            print(f"Let's try again, {username}!")
            return
        points += result_point

    print(f"Congratulations, {username}!")
