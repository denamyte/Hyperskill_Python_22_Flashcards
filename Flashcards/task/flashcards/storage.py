import random
from os.path import exists
from typing import Dict


class Storage:
    def __init__(self):
        self._term_to_def: Dict[str, str] = {}
        self._def_to_term: Dict[str, str] = {}
        self._term_in_progress = ''

    def add_term(self, term: str) -> bool:
        if term in self._term_to_def:
            return False
        self._term_in_progress = term
        return True

    def add_def(self, definition: str) -> bool:
        if definition in self._term_to_def.values():
            return False
        self._term_to_def[self._term_in_progress] = definition
        self._def_to_term[definition] = self._term_in_progress
        return True

    def remove(self, term: str) -> bool:
        if term in self._term_to_def:
            defi = self._term_to_def[term]
            del self._term_to_def[term]
            del self._def_to_term[defi]
            return True
        return False

    def import_cards(self, file_name: str) -> int:
        if not exists(file_name):
            return -1
        with open(file_name) as f:
            new_cards = {k: v[:-1] for k, v in (x.split('::') for x in f.readlines())}
        self._term_to_def.update(new_cards)
        self._def_to_term = {v: k for k, v in self._term_to_def.items()}
        return len(new_cards)

    def export_cards(self, file_name: str) -> int:
        with open(file_name, 'w') as f:
            f.writelines("::".join([k, v + '\n']) for k, v in self._term_to_def.items())
            return len(self._term_to_def)

    def get_random_card(self) -> (str, str):
        if not len(self._term_to_def):
            return '', ''
        return random.choice(list(self._term_to_def.items()))

    def get_term_by_def(self, definition: str) -> None | str:
        return self._def_to_term.get(definition)
