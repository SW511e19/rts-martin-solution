import socket

class Client():
    address = open("macaddress.txt", "r")

    s = socket.socket()
    #If on server, the server's own info. 
    #If on client, info on which server to connect to.
    host = address.read()
    port = 20000
    s.connect((host, port))
    
    def sendmsg(self, message):
        self.s.send(message)

    def recvmsg(self):
        message = self.s.recv(4)
        return message