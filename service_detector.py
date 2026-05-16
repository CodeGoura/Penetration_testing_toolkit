import socket

def grab_banner(host, port, timeout=2):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        banner = sock.recv(1024).decode('utf-8', errors='ignore')
        sock.close()
        return banner.strip()
    except Exception:
        return "No banner"

if __name__ == "__main__":
    print(grab_banner("127.0.0.1", 22)) 