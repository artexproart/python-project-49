import random

RULES_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_round():
    """Возвращает кортеж (question, correct_answer)."""
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer

