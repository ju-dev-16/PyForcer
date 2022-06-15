from sys import path
path.append('.')

from pyforce import GuessPasswordBy

# print(GuessPasswordBy().random_password(length=8))

print(GuessPasswordBy().dictionary())