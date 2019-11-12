# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 20000

s.connect(('192.168.43.59', port))
print("test")
# receive data from the server
receievedMessage = s.recv(1024).decode('utf-8')

print(receievedMessage)
# close the connection
s.close()