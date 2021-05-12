import logging

from app import books

logger = logging.getLogger('scrapping.menu')

USER_CHOICE = """Enter One of the Following
- 'b' to look at 5 start books
- 'c' to look at cheapest books
- 'n' to get the next book on the catalogue
- 'q' to exit

Enter Your Choice : """


def print_best_books():
    logger.info('Finding Best books by rating...')
    print('\n\n*** PRINTING 10 BEST BOOKS FROM THE CATALOGUE ***\n')
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in best_books:
        print(book)

"""
For sorting with multiple Keys - 
lambda x: (x.rating * -1, x.price)
"""


def print_cheapest_books():
    logger.info('Finding cheapest books...')
    print('\n\n*** PRINTING 10 CHEAPEST BOOKS FROM THE CATALOGUE ***\n')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)


def get_next_book():
    logger.info('Finding Next book...')
    print(next(books_generator))


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book,
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('Please Enter a Valid input')
        user_input = input(USER_CHOICE)
        logger.debug('Terminating Program...')

menu()

"""
Add Logs and page traversal.
"""