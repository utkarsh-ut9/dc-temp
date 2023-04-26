import socket
import threading

SERVER_ADDRESS = 'localhost'  # IP address of the server
SERVER_PORT = 1234  # Port number the server is listening on
nodes = {}  # A dictionary to store information about connected client nodes

def handle_connection(conn, addr):

    # When a client node connects to the server, it sends its ID, which is used as a key in the dictionary
    node_id = conn.recv(1024).decode()

    # Store the connection object in the dictionary with the key as the node ID
    nodes[node_id] = conn
    
    while True:
        try:
            # Receive a message from the client node
            message = conn.recv(1024).decode()
            
            # Send the message to all other connected client nodes except the sender
            for node in nodes:
                if node != node_id:
                    nodes[node].sendall(message.encode())
        
        except:
            # If there is an error, remove the node from the dictionary and break the loop
            del nodes[node_id]
            break

    conn.close()


# Create a socket object for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket object to the IP address and port number
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))

# Listen for incoming connections
server_socket.listen()

# Print a message to indicate that the server is running and listening for connections
print(f"Central server listening on {SERVER_ADDRESS}:{SERVER_PORT}")

while True:

    # Accept incoming connections
    conn, addr = server_socket.accept()
    
    # Create a new thread to handle the connection
    threading.Thread(target=handle_connection, args=(conn, addr)).start()