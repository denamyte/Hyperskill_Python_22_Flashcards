from typing import List

from Flashcards.task.flashcards.card import Card


class Checker:
    def __init__(self, cards: List[Card]):
        self._cards = cards

    def check(self):
        for card in self._cards:
            definition = input(f'Print the definition of "{card.term}":\n')
            print('Correct!' if definition == card.definition else \
                      f'Wrong. The right answer is "{card.definition}".')
