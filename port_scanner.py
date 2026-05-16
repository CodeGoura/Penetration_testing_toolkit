import socket
import threading
from queue import Queue

def scan_port(host, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return True
    except Exception:
        pass
    return False

def run_scanner(target, ports=[21, 22, 80, 443], threads=10):
    open_ports = []
    queue = Queue()
    
    for port in ports:
        queue.put(port)
        
    def worker():
        while not queue.empty():
            port = queue.get()
            if scan_port(target, port):
                open_ports.append(port)
            queue.task_done()
            
    threads_list = []
    for _ in range(threads):
        t = threading.Thread(target=worker)
        t.start()
        threads_list.append(t)
        
    for t in threads_list:
        t.join()
        
    return sorted(open_ports)

if __name__ == "__main__":
    print(run_scanner("127.0.0.1", [22, 80]))