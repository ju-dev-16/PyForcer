from requests import get

from bs4 import BeautifulSoup

class Dictionary(object):
    def __init__(self, url: str) -> None:
        page = get(url)
        soup = BeautifulSoup(page.content, features='html.parser')
        
        self.__most_used_passwords = soup.find_all('td', class_='blob-code blob-code-inner js-file-line')
        
    @property
    def __get_password(self) -> str:
        for password in self.__most_used_passwords:
            return password.text