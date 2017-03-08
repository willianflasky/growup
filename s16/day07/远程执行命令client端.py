import socket
import struct
import json
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8080))

while True:
    cmd=input('>>: ').strip()
    if not cmd:continue

    client.send(cmd.encode('utf-8'))

    # 收报头的长度
    head=client.recv(4)
    head_size=struct.unpack('i',head)[0]

    #收报头（根据报头长度）
    head_bytes=client.recv(head_size)
    head_json=head_bytes.decode('utf-8')
    head_dic=json.loads(head_json)
    '''
      head_dic={
                'data_size':len(back_msg)
            }
    '''
    data_size=head_dic['data_size'] #取出真实数据的长度

    #收真实的数据
    recv_size=0
    recv_bytes=b''
    while recv_size < data_size:
        res=client.recv(1024)
        recv_bytes+=res
        recv_size+=len(res)
    print(recv_bytes.decode('gbk'))