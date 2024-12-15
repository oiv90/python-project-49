import random


def generate_question():
    num1 = random.randint(1, 35)
    num2 = random.randint(1, 35)
    
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    
    match operation:
        case '+':
            correct_answer = num1 + num2
        case '-':
            correct_answer = num1 - num2
        case '*':
            correct_answer = num1 * num2
    
    question = f"{num1} {operation} {num2}"
    
    return question, str(correct_answer)


hello_message = 'What is the result of the expression?'

