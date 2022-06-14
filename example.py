from pyforce import SSHAuthentication

from string import ascii_letters, digits
from random import choice

from paramiko import SSHClient

client = SSHClient()

# Add your client instance and your known hosts path here
ssh_auth = SSHAuthentication(client, known_hosts_path="C:\\Users\\JuDEV\\.ssh\\known_hosts")

def try_to_login():  
    password = ''.join(choice(ascii_letters + digits) for _ in range(8))

    # Put the known and guessed informations here
    ssh_auth.login(hostname="localhost", username="root", password=password)
    
    stdin, stdout, stderr = client.exec_command("hostname")
    
    # Debuging infos about the test command
    ssh_auth.debug_info(stdout, stderr)
        
    stdin.close()
    stdout.close()
    stderr.close() 
    
try_to_login()

client.close()