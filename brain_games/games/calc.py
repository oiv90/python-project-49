import random

HELLO_MESSAGE = "What is the result of the expression?"


def calculate_expression(num1, num2):
    operations = ["+", "-", "*"]
    operation = random.choice(operations)

    match operation:
        case "+":
            correct_answer = num1 + num2
        case "-":
            correct_answer = num1 - num2
        case "*":
            correct_answer = num1 * num2

    return operation, str(correct_answer)


def generate_question():
    num1 = random.randint(1, 35)
    num2 = random.randint(1, 35)
    operation, correct_answer = calculate_expression(num1, num2)
    question = f"{num1} {operation} {num2}"

    return question, correct_answer
