from requests import get

from bs4 import BeautifulSoup

class Dictionary:
    def __init__(self, url: str):
        page = get(url)
        soup = BeautifulSoup(page.content, 'html-parser')
        
        container = soup.find_all('div', class_='CompareTable__cell CompareTable__cell--password text-base')
        childs = container.findChildren('span', recursive=False)
        
        for child in childs:
            print(child.text())