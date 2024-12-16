import random


def generate_question():
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
    question = " ".join(progression)

    return question, correct_answer


hello_message = "What number is missing in the progression?"
