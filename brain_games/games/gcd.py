import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    correct_answer = str(gcd(num1, num2))
    question = f"{num1} {num2}"

    return question, str(correct_answer)


hello_message = "Find the greatest common divisor of given numbers."
