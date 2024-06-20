import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
server_address = (socket.gethostname(), 1234)
client_socket.connect(server_address)

try:
    while True:
        message = input("Enter message to send to server: ")
        client_socket.sendall(bytes(message,'utf-8'))


        data = client_socket.recv(1024)
        if not data:
            break  
        print('Received from server:', data.decode('utf-8'))

finally:
    client_socket.close()