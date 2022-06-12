from paramiko import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import AuthenticationException

class Authentication:
    def __init__(self, client: SSHClient, known_hosts_path: str):
        self.__client = client

        self.__client.load_host_keys(known_hosts_path)
        self.__client.load_system_host_keys()

        self.__client.set_missing_host_key_policy(AutoAddPolicy())

    def ssh_login(self, hostname: str, username: str, password: str):
        try:
            self.__client.connect(hostname=hostname, username=username, password=password)
        except AuthenticationException:
            self.ssh_login(hostname, username, password)  
            print("Authentication failed.")
    
    def debug_info(self, stdout, stderr):
        print(f"STDOUT: {stdout.read().decode('utf8')}")
        print(f"STDERR: {stderr.read().decode('utf8')}")
        
        print(f"Return code: {stdout.channel.recv_exit_status()}")