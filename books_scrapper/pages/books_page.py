import re
import logging
from bs4 import BeautifulSoup

from locators.booksPage_locators import BooksPageLocators
from parsers.books_parser import BooksParser

logger = logging.getLogger('scrapping.books_page')


class BooksPage:
    def __init__(self, content):
        logger.debug('Parsing page content with BeautifulSoup HTML Parser.')
        self.content = content
        self.soup = BeautifulSoup(self.content, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all Books in the page using `{BooksPageLocators.BOOKS }`.')
        locator = BooksPageLocators.BOOKS
        book_tags = self.soup.select(locator)
        return [BooksParser(e) for e in book_tags]

    @property
    def page_count(self):
        logger.debug('Finding All number of catalogue pages available')
        content = self.soup.select_one(BooksPageLocators.PAGER).string
        logger.info(f'Found number of pages available: `{content}`')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages as Integers: `{pages}`')
        return pages
