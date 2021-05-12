import requests
from bs4 import BeautifulSoup

# Extracts from website

page = requests.get('http://www.example.com')
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find('h1').string)
