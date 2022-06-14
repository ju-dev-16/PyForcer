from sys import path
path.append(".")

from string import ascii_letters, digits
from random import choice

from paramiko import SSHClient

from pyforce import SSHAuthentication

client = SSHClient()

ssh_auth = SSHAuthentication(client, known_hosts_path="C:\\Users\\JuDEV\\.ssh\\known_hosts")

def try_to_login():  
    password = ''.join(choice(ascii_letters + digits) for _ in range(8))
    
    ssh_auth.login(hostname="192.168.0.192", username="pi", password=password)
    
    stdin, stdout, stderr = client.exec_command("hostname")
    
    ssh_auth.debug_info(stdout, stderr)
        
    stdin.close()
    stdout.close()
    stderr.close() 
    
try_to_login()

client.close()