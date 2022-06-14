from requests import get

from bs4 import BeautifulSoup

class Dictionary:
    def __init__(self, url: str) -> str:
        page = get(url)
        soup = BeautifulSoup(page.content, features='html.parser')
        
        container = soup.find_all('div', class_='CompareTable__cell CompareTable__cell--password text-base')
        
        print(container)
        
        return ""