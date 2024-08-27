import requests
from bs4 import BeautifulSoup


def get_table():
    url = "https://webscraper.io/test-sites/tables"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')

    table = soup.find('table', class_='table table-bordered')
    rows = table.findAll('tr')[1:]

    with open('tableContent.txt', 'w') as file:
        for row in rows:
            columns = row.findAll('td')
            first_name = columns[1].text.strip()
            last_name = columns[2].text.strip()
            username = columns[3].text.strip()
            file.write(f"{first_name} {last_name} - {username}\n")


get_table()
