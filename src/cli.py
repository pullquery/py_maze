import argparse


def cli():
    parser = argparse.ArgumentParser(description="Generate maze in text")
    parser.add_argument("width", metavar="width",
                        type=int,
                        help="Width of maze")
    parser.add_argument("height", metavar="height",
                        type=int,
                        help="Height of maze")
    parser.add_argument("-p", "--print",
                        action="store_true",
                        help="Print maze")
    parser.add_argument("-s", "--save", metavar="save",
                        type=str,
                        help="Save maze")

    args = parser.parse_args()
    return args.width, args.height, args.print, args.save
