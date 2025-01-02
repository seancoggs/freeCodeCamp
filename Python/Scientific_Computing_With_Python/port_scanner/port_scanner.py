import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def scan_port(target_ip, port):
    """Scan a single port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        socket.setdefaulttimeout(1)  # Timeout in seconds
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            return port
    return None

def scan_ports(target, port_range):
    """Scan a range of ports."""
    target_ip = socket.gethostbyname(target)
    open_ports = []
    start_time = datetime.now()

    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda port: scan_port(target_ip, port), port_range)
        open_ports = [port for port in results if port is not None]

    end_time = datetime.now()
    print(f"Scan completed in: {end_time - start_time}")
    return open_ports
