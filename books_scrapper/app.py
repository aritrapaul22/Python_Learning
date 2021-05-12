"""
Scraps from - http://books.toscrape.com/
to compare price and rating of displayed books
"""
import requests
import logging
# from datetime import datetime
from pages.books_page import BooksPage, BeautifulSoup

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-',
                    level=logging.INFO,
                    filename='logs.txt')

logger = logging.getLogger('scrapping')

logger.info('Loading the Books list...')

content = requests.get(f'http://books.toscrape.com').content
page = BooksPage(content)

books = page.books

for page_num in range(1, page.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    content = requests.get(url).content
    page = BooksPage(content)
    books.extend(page.books)

# with open('StoreBooks.txt', 'w') as my_file:
#     my_file.truncate()
#     my_file.writelines(f'DATETIME : {datetime.now()}\n\n')

# for item in page.books:
#     print(f'{item.name} -- {item.rating}/5 -- {item.price}')
# with open('StoreBooks.txt', 'a') as my_file:
#     my_file.writelines(f'{item.name} -- {item.rating}/5 -- {item.price}\n')
