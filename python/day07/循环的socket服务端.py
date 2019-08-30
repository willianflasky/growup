import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #就是它，在bind前加
phone.bind(('127.0.0.1',8080)) #插入卡
phone.listen(5) #开机
while True: #链接循环
    conn,addr=phone.accept()
    print('client :',addr)
    while True: #通讯循环
        try:
            data=conn.recv(1024)
            if not data:break #针对linux，客户端断开链接的异常处理
            print('from client msg :%s' %data)
            conn.send(data.upper())
        except Exception:
            break
    conn.close()
phone.close()