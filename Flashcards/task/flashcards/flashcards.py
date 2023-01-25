from Flashcards.task.flashcards.checker import Checker
from Flashcards.task.flashcards.input import Input


def main():
    cards = Input().set_data().cards
    Checker(cards).check()


if __name__ == '__main__':
    main()
