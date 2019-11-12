import socket

# Sets the READY message, which means that the ev3 is ready to communicate with the PI
msgFromClient = "READY"

# Settings Up
bytesToSend = str.encode(msgFromClient)
bufferSize = 1024
serverAddressPort = ("localhost", 20001) # IP and Port of the Raspberry PI

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Upcode from the Rasberry Pi {}".format(msgFromServer[0])
print(msg)
