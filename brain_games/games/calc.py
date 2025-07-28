import random

RULES_TEXT = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def make_round():
    """
    Генерирует раунд для игры 'Калькулятор'.
    Возвращает: кортеж (вопрос, правильный_ответ)
    """
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    operator = random.choice(OPERATORS)

    question = f'{num1} {operator} {num2}'

    match operator:
        case '+':
            correct_answer = num1 + num2
        case '-':
            correct_answer = num1 - num2
        case '*':
            correct_answer = num1 * num2

    return question, str(correct_answer)

