from typing import List

from Flashcards.task.flashcards.card import Card


class Input:
    def __init__(self):
        self._cards: List[Card] = []

    def set_data(self):
        count = int(input('Input the number of cards:\n'))
        self._cards = [Card(
            input(f'The term for card #{i}:\n'),
            input(f'The definition for card #{i}:\n')
        ) for i in range(1, count + 1)]
        return self

    @property
    def cards(self) -> List[Card]:
        return self._cards

    @cards.setter
    def cards(self, value):
        self._cards = value
