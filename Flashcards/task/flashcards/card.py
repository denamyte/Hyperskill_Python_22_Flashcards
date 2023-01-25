from dataclasses import dataclass


@dataclass
class Card:
    term: str = ''
    definition: str = ''

    def __str__(self):
        return f"""\
Card:
{self.term}
Definition:
{self.definition}"""
