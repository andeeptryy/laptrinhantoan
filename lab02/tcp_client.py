import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = "127.0.0.1"
server_port = 8080
try:
    client_socket.connect((server_ip, server_port))
    print(f"Connected to {server_ip} on port {server_port}")
    client_socket.send(b"Hello, Server!")
    response = client_socket.recv(1024)
    print(f"Received from server: {response.decode()}")
except Exception as e:
    print(f"Error connecting to {server_ip} on port {server_port}: {e}")
finally:
    client_socket.close()
