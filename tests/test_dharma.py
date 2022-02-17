import unittest
from dharma import QuoteBook
from pathlib import Path


DEFAULT_SEPARATOR_TEST_FILE = Path(__file__).parent / "book_tests/default_separator.txt"
RANDOM_SEPARATOR_TEST_FILE = Path(__file__).parent / "book_tests/random_separator.txt"


class TestDharma(unittest.TestCase):

    def test_QuoteBook_class(self):
        default_separator_book = QuoteBook(DEFAULT_SEPARATOR_TEST_FILE)
        random_separator_book = QuoteBook(RANDOM_SEPARATOR_TEST_FILE, quote_separator="***")
        expected_quotes = ['\nThis is the first quote.\n',
                           '\nThis is the second quote.\n',
                           '\nThis is the third quote.\n\nThere is an empty line inside this quote.\n',
                           '\nThis is the fourth and last quote.\n']

        # Check correct quotes
        self.assertEqual(default_separator_book.quotes, expected_quotes)
        self.assertEqual(random_separator_book.quotes, expected_quotes)


if __name__ == '__main__':
    unittest.main()
