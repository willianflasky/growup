import socket
import struct
import json
import subprocess
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #就是它，在bind前加
phone.bind(('127.0.0.1',8080)) #插入卡
phone.listen(5) #开机
while True: #链接循环
    conn,addr=phone.accept()
    print('client :',addr)
    while True: #通讯循环
        try:
            cmd=conn.recv(1024)
            if not cmd:break #针对linux，客户端断开链接的异常处理
            print('from client msg :%s' %cmd)

            res=subprocess.Popen(cmd.decode('utf-8'),
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

            err=res.stderr.read()
            if err:
                back_msg=err
            else:
                back_msg=res.stdout.read()
            #第一阶段：制作报头
            head_dic={
                'data_size':len(back_msg)
            }
            head_json=json.dumps(head_dic)
            head_bytes=head_json.encode('utf-8')

            #第二阶段：发送报头的长度
            conn.send(struct.pack('i', len(head_bytes)))

            #第三阶段：发报头
            conn.send(head_bytes)
            #第四阶段：发真实数据
            conn.sendall(back_msg)


        except Exception:
            break
    conn.close()
phone.close()