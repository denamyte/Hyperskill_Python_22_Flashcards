from typing import Callable, Dict

from Flashcards.task.flashcards.storage import Storage

TERM, DEF = 'term', 'definition'
ADD_PROMPTS = {
    TERM: ['The card:\n', 'The card "{}" already exists. Try again:\n'],
    DEF: ['The definition of the card:\n',
          'The definition "{}" already exists. Try again:\n']
}


class Menus:
    def __init__(self):
        self._storage = Storage()

    def add_card(self):
        term = self._add_term_or_def(TERM, self._storage.add_term)
        defi = self._add_term_or_def(DEF, self._storage.add_def)
        print(F'The pair ("{term}":"{defi}") has been added.\n')

    @staticmethod
    def _add_term_or_def(name: str, try_add: Callable[[str], bool]) -> str:
        """
        Get a term or a definition from user input. Check if the term
        already exists. If so, ask user to enter a unique term or definition.
        """
        s = input(ADD_PROMPTS[name][0])
        while not try_add(s):
            s = input(ADD_PROMPTS[name][1].format(s))
        return s

    def remove_card(self):
        term = input('Which card?\n')
        print('The card has been removed.\n' if self._storage.remove(term)
              else f'Can\'t remove "{term}": there is no such card.\n')

    def import_cards(self):
        file_name = input('File name:\n')
        count = self._storage.import_cards(file_name)
        print('File not found.\n' if count == -1
              else f'{count} cards have been loaded.\n')

    def export_cards(self):
        file_name = input('File name:\n')
        count = self._storage.export_cards(file_name)
        print(f'{count} cards have been saved.\n')

    def test(self):
        times = int(input('How many times to ask?\n'))
        for _ in range(times):
            term, defi = self._storage.get_random_card()
            answer = input(f'Print the definition of "{term}":\n')
            if answer != defi:
                print(f'Wrong. The right answer is "{defi}"', end='')
                term2 = self._storage.get_term_by_def(answer)
                if term2 is not None:
                    print(', but your definition is correct for '
                          f'"{term2}"', end='')
                print('.')
            else:
                print('Correct!')
        print()


menus = Menus()
COMMAND_DICT: Dict[str, Callable[[], None]] = {
    'add': menus.add_card,
    'remove': menus.remove_card,
    'import': menus.import_cards,
    'export': menus.export_cards,
    'ask': menus.test
}


def menu_run():
    while True:
        cmd = input('Input the action (add, remove, import, export, '
                    'ask, exit):\n')
        if cmd == 'exit':
            print('Bye bye!')
            break
        cmd in COMMAND_DICT and COMMAND_DICT[cmd]()
