# About

dharma-cli is a simple Python program that prints random quotes on
the terminal. It adds a touch of inspiration or amusement to your daily terminal
experience.

dharma-cli is like a little companion for your terminal, ready to sprinkle some
magic and inspiration into your day! It's a simple Python program that delivers
random quotes right to your command line.

# Usage

The program is designed to be integrated into your bashrc or preferred shell
configuration file. By doing so, every time you open a new terminal session,
you'll be greeted with a random quote of your choice. It's similar to how many
people use neofetch for displaying system information everytime a new terminal
is opened.


# Quote Book

The collection of quotes used by dharma-cli is stored in a file known as the
"Quote Book". By default, the program looks for the quote book at
$HOME/.config/dharma/quotes.qb. If this file doesn't exist, dharma-cli falls
back to using a default quote book located at /usr/share/.

Feel free to use the default quote book as a reference to create your own
personalized collection. By default the syntax of the quote book is similar to
Python docstrings, with three single quotes (''') used as delimiters for the
beginning and the end of each quote. However, you can choose a different
delimiter if you prefer.

```
'''
This is a Quote
'''

'''
This is another Quote

You can have empty lines inside the quote
'''
```


# Customization

You have the freedom to populate the quote book with your own favorite quotes.
Choose the quotes that resonate with you, whether they are inspirational, funny,
or thought-provoking. Additionally, you can customize the justification style in
which the quotes are printed in the terminal. Pick from left, right, or center
justification based on your preference.


# Installation

To use dharma-cli, simply clone this repository and integrate it into your shell
configuration file. Make sure you have Python installed on your system.
