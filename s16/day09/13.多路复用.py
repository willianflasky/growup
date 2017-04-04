#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import select
import socket

sk1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk1.bind(('127.0.0.1', 8001),)
sk1.listen(5)

sk2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk2.bind(('127.0.0.1', 8002),)
sk2.listen(5)

inputs = [sk1, sk2]
w_inputs = []
while True:
    # IO多路复用,同时监听多个SOCKET对象.
    r, w, e = select.select(inputs, w_inputs, inputs, 0.05)  #

    for obj in r:
        print("obj::::", obj)
        print("sk1::::", sk1)
        if obj in [sk1, sk2]:
            # 新连接
            print("新连接....", obj)
            conn, addr = obj.accept()
            inputs.append(conn)
        else:
            # 有连接用户发送消息来了...
            print("有用户发数据了", obj)
            try:
                data = obj.recv(1024)
            except Exception as e:
                data = ""
            if data:
                w_inputs.append(obj)
                # obj.sendall(data)
            else:
                obj.close()
                inputs.remove(obj)
                w_inputs.remove(obj)

    for obj in w_inputs:
        obj.sendall(b'ok')
        w_inputs.remove(obj)


"""
    IO多路复用
        监听多个socket对象是否有变化(可读,可写,发送错误)

句柄列表11, 句柄列表22, 句柄列表33 = select.select(句柄序列1, 句柄序列2, 句柄序列3, 超时时间)
参数： 可接受四个参数（前三个必须）
返回值：三个列表
select方法用来监视文件句柄，如果句柄发生变化，则获取该句柄。
1、当 参数1 序列中的句柄发生可读时（accetp和read），则获取发生变化的句柄并添加到 返回值1 序列中
2、当 参数2 序列中含有句柄时，则将该序列中所有的句柄添加到 返回值2 序列中
3、当 参数3 序列中的句柄发生错误时，则将该发生错误的句柄添加到 返回值3 序列中
4、当 超时时间 未设置，则select会一直阻塞，直到监听的句柄发生变化
   当 超时时间 ＝ 1时，那么如果监听的句柄均无任何变化，则select会阻塞 1 秒，之后返回三个空列表，如果监听的句柄有变化，则直接执行。

"""
