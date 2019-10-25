import socket

class Server:
    address = open("macaddress.txt", "r")

    s = socket.socket()
    #If on server, the server's own info. 
    #If on client, info on which server to connect to.
    host = address.read()
    port = 20000
    s.bind((host, port))
    
    def listen(self):
        self.s.listen(5)
        print("Awaiting connections...")
        self.slave, self.slaveinfo = self.s.accept()
        self.pie, self.pieinfo = self.s.accept()

    def sendslavemsg(self, message):
        self.slave.send(message)

    def sendpiemsg(self, message):
        self.pie.send(message)

        