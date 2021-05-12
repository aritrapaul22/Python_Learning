import re
import logging
from locators.books_locators import BooksLocators

logger = logging.getLogger('scrapping.books_parser')


class BooksParser:
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, page):
        self.page = page

    def __repr__(self):
        return f'{self.name} -- {self.rating}/5 -- {self.price}'

    @property
    def name(self):
        logger.debug('Finding the Book Name...')
        locator = BooksLocators.NAME
        item_name = self.page.select_one(locator).attrs['title']
        logger.debug(f'Found Book Name: `{item_name}`')
        return item_name

    @property
    def price(self):
        logger.debug('Finding the Book Price...')
        locator = BooksLocators.PRICE
        price = self.page.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, price)
        logger.debug(f'Found Book Price: `{matcher.group(1)}`')
        return float(matcher.group(1))

    @property
    def rating(self):
        logger.debug('Finding the Book Rating...')
        locator = BooksLocators.RATING
        rating = self.page.select_one(locator)
        classes = rating.attrs['class']
        rat_class = [r for r in classes if r != 'star-rating']
        rating_number = BooksParser.RATINGS.get(rat_class[0])
        logger.debug(f'Found Book Rating: `{rating_number}`')
        return rating_number
