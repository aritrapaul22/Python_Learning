from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

from locators.quotes_page_locators import QuotesPageLocator
from parsers.quotes import QuoteParser


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        return [
            QuoteParser(e)
            for e in self.browser.find_elements_by_css_selector(
                QuotesPageLocator.QUOTE
                )
            ]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(
            QuotesPageLocator.AUTHOR_DROPDOWN
        )
        return Select(element)

    @property
    def tag_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(
            QuotesPageLocator.TAG_DROPDOWN
        )
        return Select(element)

    @property
    def search_button(self):
        return self.browser.find_element_by_css_selector(
            QuotesPageLocator.SEARCH_BUTTON
        )

    """
    select_author : Selects the Author name matching with the args
    """

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def select_tag(self, tag_name: str):
        self.tag_dropdown.select_by_visible_text(tag_name)

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tag_dropdown.options]

    def search_for_quotes(self, author: str, tag: str) -> List[QuoteParser]:
        self.select_author(author)

        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, QuotesPageLocator.TAG_DROPDOWN_VALUE_OPTION)
            )
        )

        try:
            self.select_tag(tag)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(
                f"{author} does not have any quotes tagged with - {tag}"
            )
        self.search_button.click()
        return self.quotes


class InvalidTagForAuthorError(ValueError):
    pass
