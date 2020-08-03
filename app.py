import argparse
from gooey import Gooey
from functools import reduce


@Gooey
def main():
    parser = argparse.ArgumentParser(description="Do stuff with numbers.")
    parser.add_argument('-a',
                        '--add',
                        help='Add numbers together',
                        required=False,
                        nargs='+')
    parser.add_argument('-m',
                        '--multiply',
                        help='Multiply numbers together',
                        required=False,
                        nargs='+')

    args = vars(parser.parse_args())

    if args['add']:
        print(sum(list(map(int, args['add']))))

    if args['multiply']:
        print(reduce(lambda a, b: a * b, list(map(int, args['multiply']))))


main()