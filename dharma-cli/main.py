#!/usr/bin/env python3
# TODO: Hacer que se pueda imprimir texto en diferente color y formato
# TODO: Hacerle un exception catch a print_justified_quote para que solo pueda
        # recibir parámetros left, right center. Por ahora solo marca un error para el
        # usuario pero idealmente seria que si se pone el parámetro mal marcara un
        # error para el programador

import random
import shutil

JUSTIFY_POSITION = "right"
FILE_QUOTE_SEPARATOR = "'''"
QUOTES_FILE = '../example-file.txt'

def create_quotes_lists(file, separator):
    '''
    Creates a list from the quotes file. Each quote from the file must be
    separated by the character defined in the separator parameter
    :param1: String. Path of the file with the quotes.
    :param2: String. Character or set of character used to separate each quote
             in the file.
    :returns: List. Each element of the list is a different quote.
    '''

    with open(file) as quotes_file:
        quotes = quotes_file.read()

    file_list = quotes.split(separator)

    # Remove elements in the list that only contains spaces
    # This allows to separate each quote in the file with empty lines,
    # making it more readable.
    quotes_list = []
    for quote in file_list:
        if not quote.isspace():
            quotes_list.append(quote)

    # If the file is formated correctly the first element of the list is a new
    # line character. 
    quotes_list.pop(0)

    return quotes_list



def print_justified_quote(quote, justify_position):
    '''
    :param1: String. String that will be printed.
    :param2: String. Desided justified position. Valid positions: left, right,
             center.
    :returns: Prints string in the terminal in the desided position.
    '''

    # CYAN = '\033[96m'
    # DARKCYAN = '\033[36m'
    # BLUE = '\033[94m'
    # GREEN = '\033[92m'
    # YELLOW = '\033[93m'
    # RED = '\033[91m'
    BOLD = '\033[1m'
    # UNDERLINE = '\033[4m'
    # END = '\033[0m'

    quote_pick = quote.split('\n')

    print(BOLD)
    quote_len = len(quote_pick)
    for sentence in range(quote_len):
        current_sentence = quote_pick[sentence]
        terminal_size = shutil.get_terminal_size().columns
        if justify_position.lower() == "left":
            print(current_sentence.ljust(terminal_size)) #  Left justification

        elif justify_position.lower() == "right":
            print(current_sentence.rjust(terminal_size)) #  Right justification

        elif justify_position.lower() == "center":
            print(current_sentence.center(terminal_size)) #  Center justification
        else:
            print("Invalid parameter. Only left, center or right is allowed")
            exit(1)


def main():
    quotes_list = create_quotes_lists(QUOTES_FILE, FILE_QUOTE_SEPARATOR)
    quote_pick = random.choice(quotes_list)
    print_justified_quote(quote_pick, JUSTIFY_POSITION)

main()
