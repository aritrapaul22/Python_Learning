import re
from bs4 import BeautifulSoup

sample_html = ('<html><head></head><body>'
               '<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n'
               '    <article class="product_pod">\n'
               '            <div class="image_container">\n'
               '                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>\n'
               '            </div>\n'
               '                <p class="star-rating Three">\n'
               '                    <i class="icon-star"></i>\n'
               '                    <i class="icon-star"></i>\n'
               '                    <i class="icon-star"></i>\n'
               '                    <i class="icon-star"></i>\n'
               '                    <i class="icon-star"></i>\n'
               '                </p>\n'
               '            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>\n'
               '            <div class="product_price">\n'
               '        <p class="price_color">£51.77</p>\n'
               '<p class="instock availability">\n'
               '    <i class="icon-ok"></i>\n'
               '        In stock\n'
               '</p>\n'
               '    <form>\n'
               '        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n'
               '    </form>\n'
               '            </div>\n'
               '    </article>\n'
               '</li>'
               '</body>'
               '</html>')


class ParsedItemLocator:
    NAME_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'


class ParsedItem:

    def __init__(self):
        self.soup = BeautifulSoup(sample_html, 'html.parser')

    @property
    def name(self):
        locator = ParsedItemLocator.NAME_LOCATOR
        item_name = self.soup.select_one(locator).attrs['title']
        return item_name

    @property
    def price(self):
        locator = ParsedItemLocator.PRICE_LOCATOR
        price = self.soup.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, price)
        return float(matcher.group(1))

    @property
    def rating(self):
        locator = ParsedItemLocator.RATING_LOCATOR
        rating = self.soup.select_one(locator)
        classes = rating.attrs['class']
        rat_class = [r for r in classes if r != 'star-rating']
        return rat_class[0]


article = ParsedItem()
print(article.name)
print(article.rating)
print(article.price)

'''
Download the entire page and found which books have Five stars and under 20.00. 
'''
