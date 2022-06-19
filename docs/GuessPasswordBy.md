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
- random_string
-- usage: 
-- params: 
- dictionary
-- usage: 
-- params: 
## How to implement
### random_string
```python
password = GuessPasswordBy().random_string(length=8)
ssh_auth.login(hostname="localhost", username="root", password=password)
```
### dictionary
```python
for password in GuessPasswordBy.dictionary():
	ssh_auth.login(hostname="localhost", username="root", password=password)
```