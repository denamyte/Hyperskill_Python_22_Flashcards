from argparse import ArgumentParser

from Flashcards.task.flashcards.menu import menu_run

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--import_from')
    parser.add_argument('--export_to')
    args = parser.parse_args()

    menu_run(args.import_from, args.export_to)
