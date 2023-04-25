import socket
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    print(f'Starting server on {server_address[0]}:{server_address[1]}')
    server_socket.bind(server_address)
    server_socket.listen(5)
    clients = []
    while True:
        print('Waiting for connections...')
        client_socket, client_address = server_socket.accept()
        print(f'Accepted connection from {client_address[0]}:{client_address[1]}')
        client_socket.send(b'Welcome to the group!')
        clients.append(client_socket)
        for client in clients:
            if client != client_socket:
                client.send(b'A new member joined the group!')
    server_socket.close()
if __name__ == '__main__':
    start_server()