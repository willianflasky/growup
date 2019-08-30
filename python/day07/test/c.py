import time
import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8080))


client.send('hello'.encode('utf-8'))
time.sleep(5)
client.send('egon'.encode('utf-8'))