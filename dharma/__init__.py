from dharma.quotebook import QuoteBook
import random
import argparse
import os

DEFAULT_FILE_PATH = f'{os.path.expanduser("~")}/.config/dharma/quotebook.txt'
DEFAULT_JUSTIFICATION_POSITION = "center"
# EXAMPLE_FILE_PATH = "/usr/share/doc/dharma/quotebook.txt"
EXAMPLE_FILE_PATH = "/etc/quotebook.txt"


def main():
    '''
    Main function
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-j", "--justify",
                        help="Justification position. Accepted values are left, center, right,",
                        choices=["left", "right", "center"])
    parser.add_argument("-f", "--file", help="Specify a file with quotes")
    parser.add_argument("-q", "--quote", help="Print a specific quote", type=int)
    parser.add_argument("--quantity",
                        help="Tells how many quotes you have in your file",
                        action="store_true")

    args = parser.parse_args()

    if args.justify == "center":
        justification_position = "center"
    elif args.justify == "right":
        justification_position = "right"
    elif args.justify == "left":
        justification_position = "left"
    else:
        justification_position = DEFAULT_JUSTIFICATION_POSITION

    if args.file:
        file_path = args.file
    else:
        file_path = DEFAULT_FILE_PATH

    try:
        dharma = QuoteBook(file_path)
    except FileNotFoundError:
        try:
            dharma = QuoteBook(EXAMPLE_FILE_PATH)
            print(f"{file_path} Doesn't exist. Using example file")
        except FileNotFoundError:
            print("No configuration file found")
            exit(1)

    if args.quantity:
        print(f"You have {dharma.quotes_quantity} quotes in your file")
        exit(0)

    if args.quote:
        quote_num = args.quote
    else:
        quote_num=random.randint(1, dharma.quotes_quantity)

    try:
        dharma.print_quote(quote_num, justification_position)
    except IndexError:
        print("Quote number outside of scope")
        print(f"You have {dharma.quotes_quantity} quotes")
        exit(1)


if __name__ == "__main__":
    main()
