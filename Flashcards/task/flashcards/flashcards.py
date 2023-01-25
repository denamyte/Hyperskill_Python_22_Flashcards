from Flashcards.task.flashcards.checker import Checker
from Flashcards.task.flashcards.input import Input


def main():
    card = Input().set_data().card
    print(Checker(card, input()))


if __name__ == '__main__':
    main()
