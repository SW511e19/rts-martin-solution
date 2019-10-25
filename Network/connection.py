import socket

#This file is unused, do not bother

class Connection:

    address = open("hostaddress.txt", "r")

    s = socket.socket()
    #If on server, the server's own info. 
    #If on client, info on which server to connect to.
    host = address.read()
    port = 20000

    def server(self):
        self.s.bind((self.host, self.port))
        self.s.listen(5)

        print("Awaiting connection...")
        while True:
            c, addr = self.s.accept()

    def client(self):
        self.s.connect((self.host, self.port))
