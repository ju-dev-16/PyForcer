# Guess password by
## Import
```python
from pyforce import GuessPasswordBy
```
## Instance
```python
pw_guesser = GuessPasswordBy()
```
### Methods
- **random_string**
> - **usage**: Returns a random generated string
> - **params**: length: int
- dictionary
> - **usage**: Returns a list of the most 200 common passwords
> - **params**: /
## How to implement
### random_string
```python
password = pw_guesser.random_string(length=8)
ssh_auth.login(hostname="localhost", username="root", password=password)
```
### dictionary
```python
for password in pw_guesser.dictionary():
ssh_auth.login(hostname="localhost", username="root", password=password)
```