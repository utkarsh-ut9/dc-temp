import socket
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    print(f'Connecting to {server_address[0]}:{server_address[1]}')
    client_socket.connect(server_address)
    while True:
        message = client_socket.recv(1024)
        if message:
            print(f'Received message: {message.decode("utf-8")}')
        else:
            break
    client_socket.close()
if __name__ == '__main__':
    start_client()