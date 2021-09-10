# SERVER PROGRAM

import socket

SERVER_HOST = socket.gethostname()
SERVER_PORT = 9999
BUFFER_SIZE = 1024

# create a socket object
s = socket.socket()
s.bind((SERVER_HOST,SERVER_PORT))

print("Waiting for connection...")
s.listen(5)

# accept any connections attempted
client_socket, client_address = s.accept()
print("Got connection from",client_address)
# sending a message
message = "This is a server to client communcation, showing remote command execution!".encode()
client_socket.send(message)

while True:
    # get the command from prompt
    command = input("Enter the command:")
    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    results = client_socket.recv(BUFFER_SIZE).decode()
    print(results)

# close connection to the client
client_socket.close()

# close server connection
s.close()