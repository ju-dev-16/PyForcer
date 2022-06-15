from sys import path
path.append('.')

from string import ascii_letters, digits
from random import choice

from utils import Dictionary

class GuessPasswordBy: 
    def random_password(self, length: int) -> str:
        return ''.join(choice(ascii_letters + digits) for _ in range(length))
    
    def dictionary(self) -> Dictionary:
        return Dictionary('https://github.com/danielmiessler/SecLists/blob/master/Passwords/2020-200_most_used_passwords.txt')