from port_scanner import scan_ports
from tcp_client import TCPClient

def main():
    # Port Scanning
    target = input("Enter the target IP or hostname: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    port_range = range(start_port, end_port + 1)

    open_ports = scan_ports(target, port_range)
    print(f"Open ports on {target}: {open_ports}")

    # Connect to a chosen port
    if open_ports:
        chosen_port = int(input(f"Choose a port to connect to from {open_ports}: "))
        client = TCPClient(target, chosen_port)
        try:
            client.connect()
            print(f"Connected to {target} on port {chosen_port}")
            
            # Send an HTTP request if connecting to port 80
            if chosen_port == 80:
                client.send("GET / HTTP/1.1\r\nHost: {target}\r\n\r\n")
            
            # Receive and print the server response
            print("Message from server:", client.receive())
        finally:
            client.close()

if __name__ == "__main__":
    main()
