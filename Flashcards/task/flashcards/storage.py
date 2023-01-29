import random
from functools import reduce
from os.path import exists
from typing import Dict, List

from Flashcards.task.flashcards.data import Card, HardestInfo


class Storage:
    def __init__(self):
        self._term_to_card: Dict[str, Card] = {}
        self._def_to_card: Dict[str, Card] = {}
        self._cards_cache: List[Card] = []
        self._term_in_progress = ''

    def _update_cache(self):
        self._cards_cache = list(self._term_to_card.values())

    def add_term(self, term: str) -> bool:
        if term in self._term_to_card:
            return False
        self._term_in_progress = term
        return True

    def add_def(self, definition: str) -> bool:
        if definition in self._def_to_card.keys():
            return False
        card = Card(self._term_in_progress, definition)
        self._term_to_card[self._term_in_progress] = card
        self._def_to_card[definition] = card
        self._update_cache()
        return True

    def remove(self, term: str) -> bool:
        if term in self._term_to_card:
            defi = self._term_to_card[term].definition
            del self._term_to_card[term]
            del self._def_to_card[defi]
            self._update_cache()
            return True
        return False

    def import_cards(self, file_name: str) -> int:
        if not exists(file_name):
            return -1
        with open(file_name) as f:
            cards = [Card(t, d, int(m[:-1])) for t, d, m
                     in (x.split('::') for x in f.readlines())]
        self._term_to_card.update({card.term: card for card in cards})
        self._def_to_card = {card.definition: card for card in self._term_to_card.values()}
        self._update_cache()
        return len(cards)

    def export_cards(self, file_name: str) -> int:
        with open(file_name, 'w') as f:
            f.writelines("::".join(
                (card.term, card.definition, str(card.mistakes) + '\n')
            ) for card in self._term_to_card.values())
            return len(self._term_to_card)

    def get_random_card(self) -> Card:
        if not len(self._term_to_card):
            return Card('', '')
        return random.choice(self._cards_cache)

    def get_card_by_def(self, definition: str) -> Card | None:
        return self._def_to_card.get(definition)

    def get_hardest_info(self) -> HardestInfo | None:
        max_mistakes = reduce(lambda x, card: x if x > card.mistakes else card.mistakes, self._cards_cache, 0)
        return None if not max_mistakes \
            else HardestInfo([card.term for card in self._cards_cache if card.mistakes == max_mistakes],
                             max_mistakes)

    def reset_stats(self):
        for card in self._cards_cache:
            card.mistakes = 0
