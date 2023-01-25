class Card:
    def __init__(self, term: str, definition: str):
        self.term = term
        self.definition = definition

    def __str__(self):
        return f"""\
Card:
{self.term}
Definition:
{self.definition}"""


def main():
    c = Card('purchase', 'buy')
    print(c)


if __name__ == '__main__':
    main()
