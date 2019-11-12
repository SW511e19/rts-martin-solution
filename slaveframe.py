from EV3Slave import platform_control
from Network import client

c = client.Client()
msg = 0

while True:
    msg = c.recvmsg()
    platform_control.move(msg)