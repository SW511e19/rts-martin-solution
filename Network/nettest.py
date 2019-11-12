import host
h = host.Server()
print("listening")
h.listen()
h.sendslavemsg(100)