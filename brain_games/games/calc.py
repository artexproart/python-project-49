import random

RULES_TEXT = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def make_round():
    """
    Генерирует раунд для игры 'Калькулятор'.
    Возвращает: кортеж (вопрос, правильный_ответ)
    """
    # Using random for non-cryptographic game logic only
    num1 = random.randint(1, 25)   # NOSONAR
    num2 = random.randint(1, 25)   # NOSONAR
    operator = random.choice(OPERATORS)   # NOSONAR

    question = f'{num1} {operator} {num2}'

    match operator:
        case '+':
            correct_answer = num1 + num2
        case '-':
            correct_answer = num1 - num2
        case '*':
            correct_answer = num1 * num2

    return question, str(correct_answer)

