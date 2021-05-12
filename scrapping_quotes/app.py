from selenium import webdriver

from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

try:
    author = input("Enter the author you'd like quotes from: ")
    tags = input("Enter the tags: ")

    chrome = webdriver.Chrome(executable_path='/home/aritrapaul/Documents/chromedriver_linux64/chromedriver')
    chrome.get("http://quotes.toscrape.com/search.aspx")
    page = QuotesPage(chrome)

    print(page.search_for_quotes(author, tags))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error happened.  Please try again.")
