import random

HELLO_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    num = random.randint(1, 100)
    correct_answer = "yes" if num % 2 == 0 else "no"
    return num, correct_answer
