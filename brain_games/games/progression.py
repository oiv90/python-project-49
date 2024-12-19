import random

HELLO_MESSAGE = "What number is missing in the progression?"


def calculate_progression():
    step = random.randint(2, 9)
    start = random.randint(1, 20)
    progression = []

    for i in range(10):
        progression.append(str(start))
        start += step

    pos_to_replace = random.randint(0, 9)
    num = progression[pos_to_replace]
    progression[pos_to_replace] = ".."
    correct_answer = str(num)

    return progression, correct_answer


def generate_question():
    progression, correct_answer = calculate_progression()
    question = " ".join(progression)

    return question, correct_answer
