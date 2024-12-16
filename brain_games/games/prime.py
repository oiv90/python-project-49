import random


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def generate_question():
    num = random.randint(1, 100)
    prime = is_prime(num)
    correct_answer = "yes" if prime else "no"
    question = f"{num}"

    return question, correct_answer


hello_message = 'Answer "yes" if given number is prime. Otherwise answer "no".'
