from Flashcards.task.flashcards.card import Card


class Input:
    def __init__(self):
        self._card = Card()

    def set_data(self):
        self._card.term = input()
        self._card.definition = input()
        return self

    @property
    def card(self) -> Card:
        return self._card

    @card.setter
    def card(self, value):
        self._card = value
