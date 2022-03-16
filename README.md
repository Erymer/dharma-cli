# dharma-cli
dharma-cli es a simple python program that prints random quotes on the terminal

It's intended use is for using it inside your bashrc (or in the configuration
file of your preferred shell) and then everytime that you open a new terminal
you are greeted with any of your favorite quotes, similar in the way that a lot
of people uses neofetch. 

You can use your own favorite quotes and choose the justification in which the
quotes are printed in the terminal.

# Quote Book
The file that contains all your selected quotes is known as "Quote Book".

By default dharma-cli uses the quotes that are in the quote book in
$HOME/.config/dharma/quotes.qb

If this quote book doesn't exist, dharma-cli will use a default quote book that
is in /usr/share/. You can also use this quote book as a reference to make your
own.

The syntaxis of the quote book is very similar to the way in which docstrings
are written in Python. By default three single quotes are used as delimitator
for each quote, but you can use a different delimitator if you wish.

```
'''
This is a Quote
'''

'''
This is another Quote

You can have empty lines inside the quote
'''
```
# Intended use
If you want that everytime you open your terminal you are received with a nice
quote just add this line at the end of the configuration file of your current
shell.

```
dharma
```

Really, that's it

By default it will print the quotes in the center of the terminal. If you want to use a
different position pick one of this lines.

```
dharma --justify left

dharma --justify right
```


# Installation
## Arch Linux
From AUR

## From Source

