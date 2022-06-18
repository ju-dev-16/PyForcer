from paramiko import SSHClient

from pyforce import SSHAuthentication, GuessPasswordBy

client = SSHClient()

# Add your client instance and your known hosts path here
ssh_auth = SSHAuthentication(client, known_hosts_path="C:\\Users\\JuDEV\\.ssh\\known_hosts")

def try_to_login():  
    # Guess password by a random generated string
    password = GuessPasswordBy().random_string(length=8)
    
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