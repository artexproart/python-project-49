from brain_games.cli import welcome_user
from brain_games.games.even import RULES_TEXT, make_round

ROUNDS_TO_WIN = 3


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(RULES_TEXT)
    right_answers = 0

    while right_answers < ROUNDS_TO_WIN:
        question, correct_answer = make_round()
        print(f'Question: {question}')
        answer = input('Your answer: ').lower()

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. "
                 f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print('Correct!')
        right_answers += 1

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

