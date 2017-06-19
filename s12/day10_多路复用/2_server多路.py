#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import socket
import select

sk=socket.socket()
sk.bind(('127.0.0.1',9999,))
sk.listen(5)

inputs=[sk,]
outputs=[]
messages={}
while True:
    rlist,wlist,e = select.select(inputs,outputs,[],1)
    print(len(inputs),len(rlist),len(wlist),len(outputs))

    for r in rlist:
        if r == sk:
            conn,address=r.accept()
            inputs.append(conn)
            messages[conn]=[]
            conn.sendall(bytes('hello',encoding='utf8'))
        else:
            print('========')
            try:
                ret=r.recv(1024)
                #r.sendall(ret)
                if not ret:
                    raise Exception('bye')
                else:
                    outputs.append(r)
                    messages[r].append(ret)
            except Exception as e:
                inputs.remove(r)
                del messages[r]

    #所有给我发过消息的人
    for w in wlist:
        msg=messages[w].pop()
        resp=msg+ bytes('reponse',encoding='utf8')
        w.sendall(resp)
        outputs.remove(w)
