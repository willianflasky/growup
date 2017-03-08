import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',8080)) #拨通电话

while True:
    msg=input('>>: ')
    client.send(msg.encode('utf-8')) #客户端发消息
    print('=========>has send')
    data=client.recv(1024) #客户端收消息
    print(data)
client.close() #关闭