from typing import Callable, Dict, List

from Flashcards.task.flashcards.storage import Storage

ADD_PROMPTS = {
    'term': ['The card:', 'The card "{}" already exists. Try again:'],
    'def': ['The definition of the card:',
            'The definition "{}" already exists. Try again:']
}
HARDEST_INFO_NONE = 'There are no cards with errors.\n'
HARDEST_INFO = 'The hardest card is "{}". You have {} errors answering it.\n'
HARDEST_INFO_MUL = 'The hardest cards are {}. You have {} errors answering them.\n'


class Menus:
    def __init__(self):
        self._storage = Storage()
        self._log_list: List[str] = []

    def log(self, line: str, input_mode=False) -> str | None:
        print(line)
        self._log_list.append(line + '\n')
        if input_mode:
            s = input()
            self._log_list.append(s + '\n')
            return s

    def add_card(self):
        term = self._add_term_or_def('term', self._storage.add_term)
        defi = self._add_term_or_def('def', self._storage.add_def)
        self.log(f'The pair ("{term}":"{defi}") has been added.\n')

    def _add_term_or_def(self, name: str, try_add: Callable[[str], bool]) -> str:
        """
        Get a term or a definition from user input. Check if the term or the definition
        already exist. If so, ask user to enter a unique term or definition.
        """
        s = self.log(ADD_PROMPTS[name][0], True)
        while not try_add(s):
            s = self.log(ADD_PROMPTS[name][1].format(s), True)
        return s

    def remove_card(self):
        term = self.log('Which card?', True)
        self.log('The card has been removed.\n' if self._storage.remove(term)
                 else f'Can\'t remove "{term}": there is no such card.\n')

    def import_cards(self):
        file_name = self.log('File name:', True)
        count = self._storage.import_cards(file_name)
        self.log('File not found.\n' if count == -1
                 else f'{count} cards have been loaded.\n')

    def export_cards(self):
        file_name = self.log('File name:', True)
        count = self._storage.export_cards(file_name)
        self.log(f'{count} cards have been saved.\n')

    def test(self):
        times = int(self.log('How many times to ask?', True))
        for _ in range(times):
            card = self._storage.get_random_card()
            answer = self.log(f'Print the definition of "{card.term}":', True)
            if answer != card.definition:
                card.mistakes += 1
                line = f'Wrong. The right answer is "{card.definition}"'
                card2 = self._storage.get_card_by_def(answer)
                if card2 is not None:
                    line += f', but your definition is correct for "{card2.term}"'
                line += '.'
                self.log(line)
            else:
                self.log('Correct!')
        print()

    def save_log(self):
        file_name = self.log('File name:', True)
        with open(file_name, 'w') as f:
            f.writelines(self._log_list)
        self.log('The log has been saved.\n')

    def hardest_card(self):
        info = self._storage.get_hardest_info()
        info_s = HARDEST_INFO_NONE if not info \
            else HARDEST_INFO.format(info.terms[0], info.mistakes) if len(info.terms) == 1 \
            else HARDEST_INFO_MUL.format(', '.join(f'"{t}"' for t in info.terms), info.mistakes)
        self.log(info_s)

    def reset_stats(self):
        self._storage.reset_stats()
        self.log('Card statistics have been reset.\n')


menus = Menus()
COMMAND_DICT: Dict[str, Callable[[], None]] = {
    'add': menus.add_card,
    'remove': menus.remove_card,
    'import': menus.import_cards,
    'export': menus.export_cards,
    'ask': menus.test,
    'exit': lambda: print('Bye bye!'),
    'log': menus.save_log,
    'hardest card': menus.hardest_card,
    'reset stats': menus.reset_stats,
}

INPUT_ACTION = f'Input the action ({", ".join(k for k in COMMAND_DICT.keys())}):'


def menu_run():
    cmd = ''
    while cmd != 'exit':
        cmd = menus.log(INPUT_ACTION, True)
        cmd in COMMAND_DICT and COMMAND_DICT[cmd]()
