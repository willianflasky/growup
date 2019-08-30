import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.bind(('127.0.0.1',8080)) #插入卡

phone.listen(5) #开机

conn,addr=phone.accept() #接电话
print('tcp的链接',conn)
print('客户端的地址',addr)

data=conn.recv(1024) #收消息
print('from client msg :%s' %data)


conn.send(data.upper()) #发消息

conn.close() #挂电话
phone.close() #关手机