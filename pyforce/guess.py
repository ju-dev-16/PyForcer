from sys import path
path.append('.')

from string import ascii_letters, digits
from random import choice

from utils import Dictionary

class Guess:
    def __init__(self) -> None:
        pass
    
    def by_random_string(self, length: int) -> str:
        return ''.join(choice(ascii_letters + digits) for _ in range(length))
    
    def by_dictionary(self) -> Dictionary:
        return Dictionary('https://nordpass.com/de/most-common-passwords-list')