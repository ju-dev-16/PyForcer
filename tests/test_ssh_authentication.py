from sys import path
path.append('.')

from pyforce import SSHAuthentication, Guess

from paramiko import SSHClient

client = SSHClient()

ssh_auth = SSHAuthentication(client, known_hosts_path='C:\\Users\\JuDEV\\.ssh\\known_hosts')

def try_to_login() -> None:  
    password = Guess().by_random_string(length=8)
    
    ssh_auth.login(hostname='192.168.0.192', username='pi', password=password)
    
    stdin, stdout, stderr = client.exec_command('hostname')
    
    ssh_auth.debug_info(stdout, stderr)
        
    stdin.close()
    stdout.close()
    stderr.close() 
    
try_to_login()

client.close()