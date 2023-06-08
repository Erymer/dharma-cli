# About

dharma-cli is a simple Python program that prints random quotes on the terminal.
It adds a touch of inspiration or amusement to your daily terminal experience.

dharma-cli is like a little companion for your terminal, ready to sprinkle some
magic and inspiration into your day!


# Usage

The program is designed to be integrated into your bashrc, zshrc or preferred
shell configuration file. By doing so, every time you open a new terminal
session, you'll be greeted with a random quote of your choice. It's similar to
how many people use [neofetch](https://github.com/dylanaraps/neofetch) for
displaying system information everytime a new terminal is opened.


# Quote Book

The collection of quotes used by dharma-cli is stored in a file known as the
`Quote Book`. By default, the program looks for the `quote book` at
`$HOME/.config/dharma/quotebook.txt`. If this file doesn't exist, dharma-cli
falls back to using a default quote book located at `/etc/quotebook.txt`.

Feel free to use the default `quote book` as a reference to create your own
personalized collection. By default the syntax of the `quote book` is similar to
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

You have the freedom to populate the `quote book` with your own favorite quotes.
Choose the quotes that resonate with you, whether they are inspirational, funny,
or thought-provoking. Additionally, you can customize the justification style in
which the quotes are printed in the terminal. Pick from left, right, or center
justification based on your preference.


# Installation


## Arch linux

Install from AUR


## From a clone

Dharma requires `build` and `installer` python modules to install.

To check if these modules are installed run this lines in a terminal.

``` bash
python -c "import build" 2>/dev/null && \
  echo "python-build is installed" || \
  echo "python-build is NOT installed";
python -c "import installer" 2>/dev/null && \
  echo "python-installer is installed" || \
  echo "python-installer is NOT installed"
```

If this modules are not present, install them using `pip` or your system package
manager

After doing this follow this instructions:

- Clone this repository
- Change to the created directory
- Run `sudo make install`

Or copy this lines and run them in a terminal

``` bash
git clone https://github.com/Erymer/dharma-cli
cd dharma-cli
sudo make install
```


# Using Dharma

To use it as intended just include one of the following lines in the
configuration file of your shell (bashrc, zshrc, etc).

``` bash
dharma # Text in the center of the terminal
dharma --justify right # Text to the far right
dharma --justify left # Text to the far left
```

And thas it! Now everytime you open a new terminal you will be greeted with a
quote.
