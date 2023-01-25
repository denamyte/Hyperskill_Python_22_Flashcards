from Flashcards.task.flashcards.card import Card


class Checker:
    def __init__(self, card: Card, definition: str):
        self.card = card
        self.definition = definition

    def __str__(self):
        somehow = "right!" \
            if self.card.definition == self.definition \
            else "wrong..."
        return f'Your answer is {somehow}'
