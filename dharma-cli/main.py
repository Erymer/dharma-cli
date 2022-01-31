#!/usr/bin/env python3
# TODO: Ponerle un exception error por si se pone algo que no sea un int en
# argumento q
# TODO: Un argumento para que sea una frase diferente cada día en ves de cada
# que se abre una terminal

from QuoteBook import QuoteBook
import random
import sys
import getopt
import os

file_path = f'{os.path.expanduser("~")}/.config/dharma/dharma-quotes.txt'

justification_position = "center"

arguments = sys.argv[1:]
short_options = "hf:j:q:"
long_options = ["help", "file", "justify-to", "quote"]

quote_select = False

try:
    opts, args = getopt.getopt(arguments, short_options, long_options)

except getopt.GetoptError:
    print("Error, not a valid option")
    sys.exit(1)

for opt, arg in opts:
    if opt in ("-h", "--help"):
        print("Help text")
        sys.exit(0)

    elif opt in ("-j", "--justify-to"):
        if ((arg.lower() == "left") or
            (arg.lower() == "right") or
            (arg.lower() == "center")):
            justification_position = arg
        else:
            print(f"{arg} is an invalid value")
            print("Valid positions = left, center or right")
            sys.exit(1)

    elif opt in ("-f", "--file"):
        file_path = arg

    elif opt in ("-q", "--quote"):
        quote_select = True
        quote_num = int(arg)


try:
    dharma = QuoteBook(file_path)
except FileNotFoundError:
    print(f"{file_path} Doesn't exist. Using example file")
    dharma = QuoteBook("../example-file.txt")

if quote_select:
    dharma.print_quote(quote_num, justification_position)
else:
    quote_num=random.randint(1, dharma.quotes_quantity)
    dharma.print_quote(quote_num, justification_position)
