from typing import Dict

TERM = 'term'
DEF = 'definition'


class UserInput:

    def __init__(self):
        self._term_to_def: Dict[str, str] = {}
        self._def_to_term: Dict[str, str] = {}

    def set_data(self):
        """Set all card data"""
        count = int(input('Input the number of cards:\n'))
        for i in range(1, count + 1):
            term = self._set_term_or_def(self._term_to_def, TERM)
            definition = self._set_term_or_def(self._def_to_term, DEF)
            self._term_to_def[term] = definition
            self._def_to_term[definition] = term
        return self

    @staticmethod
    def _set_term_or_def(dic: Dict[str, str], name: str) -> str:
        """
        Get a term or a definition from user input. Check if the term
        already exists. If so, ask user to enter a unique term or definition.
        """
        s = input(f'The {name} for card #{len(dic) + 1}:\n')
        while s in dic:
            s = input(f'The {name} "{s}" already exists. Try again:\n')
        return s

    @property
    def cards(self) -> Dict[str, str]:
        return self._term_to_def
