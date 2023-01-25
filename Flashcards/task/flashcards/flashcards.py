from Flashcards.task.flashcards.checker import Checker
from Flashcards.task.flashcards.userinput import UserInput


def main():
    cards = UserInput().set_data().cards
    Checker(cards).check()


if __name__ == '__main__':
    main()
