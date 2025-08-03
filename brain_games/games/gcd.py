import math
import random

RULES_TEXT = 'Find the greatest common divisor of given numbers.'


def make_round():
    """
    Генерирует раунд для игры 'НОД'.
    Возвращает: кортеж (вопрос, правильный_ответ)
    """
    # Using random for non-cryptographic game logic only
    num1 = random.randint(1, 100)  # nosec
    num2 = random.randint(1, 100)  # nosec
    
    question = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    
    return question, correct_answer

