from sys import path
path.append('.')

from pyforce import GuessPasswordBy

print(GuessPasswordBy().random_password(length=8))

for password in GuessPasswordBy().dictionary():
    print(password)