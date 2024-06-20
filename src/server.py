import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
serversocket = (socket.gethostname(), 1234)
s.bind(serversocket)

s.listen(1)
print('Server is waiting for a connection')

connection, clientAddress = s.accept()
print('Connection from', clientAddress)

try:
    while True:
        dataToSend = input("Enter Data to send to client: ")
        connection.sendall(bytes(dataToSend, "utf-8"))

        
        data = connection.recv(1024)
        if not data:
            break  
        print("Data received from the client:", data.decode('utf-8'))


finally:
    connection.close()