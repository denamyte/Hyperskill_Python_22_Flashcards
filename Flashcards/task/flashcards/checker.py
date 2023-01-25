from typing import Dict


class Checker:
    def __init__(self, cards: Dict[str, str]):
        self._term_to_def = cards
        self._def_to_term = {v: k for k, v in cards.items()}

    def check(self):
        for term, definition in self._term_to_def.items():
            answer = input(f'Print the definition of "{term}":\n')
            if answer != definition:
                print(f'Wrong. The right answer is "{definition}"', end='')
                if answer in self._def_to_term:
                    print(', but your definition is correct for '
                          f'"{self._def_to_term[answer]}"', end='')
                print('.')
            else:
                print('Correct!')
