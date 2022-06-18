# SSH Authentication
## Import
```python
from pyforce import SSHAuthentication
```
## Instance
```python
ssh_auth = SSHAuthentication()
```
### Required parameters
- client: SSHClient
- known_hosts_path: str 
### Methods
- login
--- usage: Connect you everytime again with the server on a AuthenticationException from paramiko.ssh
--- params: hostname: str, username: str, password: str
- debug_info
--- usage: Writes stdout, stderr and the return code formatted
--- params: stdout, stderr from client.exec_command(command)

## How to implement
```python
from paramiko import SSHClient

from pyforce import SSHAuthentication, GuessPasswordBy

client = SSHClient()

# Add your paramiko client instance and your known hosts path here
ssh_auth = SSHAuthentication(client, known_hosts_path="C:\\Users\\USERNAME\\.ssh\\known_hosts")

def  try_to_login():
	# Choose a method to guess the password
	password = ''.join(choice(ascii_letters + digits) for _ in  range(8 + 1))

	# Put the known and guessed data here
	ssh_auth.login(hostname="localhost", username="root", password=password)

	stdin, stdout, stderr = client.exec_command("hostname")

	# Debugging infos about the test command
	ssh_auth.debug_info(stdout, stderr)

	stdin.close()
	stdout.close()
	stderr.close()

try_to_login()

client.close()
```
