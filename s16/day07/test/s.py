import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',8080))
phone.listen(5)
conn,addr=phone.accept()

data=conn.recv(1024)
print(data)

# data1=conn.recv(10)
# print(data1)