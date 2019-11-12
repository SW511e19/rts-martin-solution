import socket

class Server:
    #address = open("hostaddress.txt", "r")

    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    #If on server, the server's own info. 
    #If on client, info on which server to connect to.
    host = 'b0:05:94:eb:7c:4f'
    port = 20000
    s.bind((host, port))
    
    def listen(self):
        self.s.listen(5)
        print("Awaiting connections...")
        self.slave, self.slaveinfo = self.s.accept()
        #self.pie, self.pieinfo = self.s.accept()

    def sendslavemsg(self, message):
        self.slave.send(message)

    #def sendpiemsg(self, message):
    #    self.pie.send(message)

        