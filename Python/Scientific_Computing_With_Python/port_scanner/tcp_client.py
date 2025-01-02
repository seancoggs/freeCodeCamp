import socket

class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        """Connect to the server."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send(self, message):
        """Send a message to the server."""
        self.socket.sendall(message.encode('utf-8'))

    def receive(self):
        """Receive a message from the server."""
        return self.socket.recv(1024).decode('utf-8')

    def close(self):
        """Close the connection."""
        if self.socket:
            self.socket.close()
